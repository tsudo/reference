#!/usr/bin/env python3
"""
batch_ingest.py -- Batch ingest local files into tsudo/reference.

Two modes:

  1. MANIFEST mode (recommended for medium-large batches):
     Fill in batch_manifest.csv with metadata, then run:
       python scripts/batch_ingest.py --manifest path/to/batch_manifest.csv

  2. DIRECTORY mode (for auto-classification from filenames):
     Point at a folder, files are auto-classified and grouped for confirmation:
       python scripts/batch_ingest.py --batch-dir path/to/folder

In both modes, converted .md files are written to the correct bucket folders,
then CATALOG.csv and INDEX.md are regenerated once at the end.
"""

import argparse
import csv
import re
import shutil
import subprocess
import sys
from pathlib import Path
from datetime import date

REPO_ROOT = Path(__file__).parent.parent

BUCKET_MAP = {
    "framework":    "frameworks",
    "threat-intel": "threat-intel",
    "breach-report":"breach-reports",
    "government":   "government",
    "research":     "research",
    "standard":     "standards",
    "tool-template":"tools-templates",
    "misc":         "z_misc",
}

CONTENT_TYPE_CHOICES = list(BUCKET_MAP.keys())

MANIFEST_FIELDS = [
    "file_path", "title", "organization", "content_type",
    "year", "tags", "source_url",
]

# ---------------------------------------------------------------------------
# Auto-classification heuristics (same logic as catalog.py)
# ---------------------------------------------------------------------------

def guess_content_type(stem, src_folder_name=""):
    """Guess content_type from filename stem and source folder name."""
    s = (stem + " " + src_folder_name).lower()
    if any(k in s for k in ["dbir", "breach", "incident", "ponemon", "ibm_cost", "equifax", "anthem"]):
        return "breach-report"
    if any(k in s for k in ["cisa", "nist", "dhs", "fbi", "wwta", "ata-20", "unclassified"]):
        return "government"
    if any(k in s for k in ["wef", "global_risk", "enisa"]):
        return "research"
    if any(k in s for k in ["framework", "csf", "oscal", "cis_control", "cmmc", "iso_27"]):
        return "framework"
    if any(k in s for k in ["sp_800", "sp800", "fips", "nist_sp", "standard"]):
        return "standard"
    if any(k in s for k in ["checklist", "playbook", "template", "cheatsheet", "password", "passphrase",
                             "questionnaire", "vsa", "caiq", "vsaq", "tprm", "scrm", "vendor_assessment",
                             "third_party", "supply_chain"]):
        return "tool-template"
    return "threat-intel"  # default for vendor reports


def guess_org(stem):
    """Guess organization from filename stem."""
    s = stem.lower()
    if "verizon" in s or "dbir" in s:           return "Verizon"
    if "ponemon" in s or "ibm" in s:             return "IBM/Ponemon"
    if "cisco" in s:                             return "Cisco"
    if "proofpoint" in s or "pfpt" in s:         return "Proofpoint"
    if "crowdstrike" in s:                       return "CrowdStrike"
    if "mandiant" in s:                          return "Mandiant"
    if "symantec" in s or "istr" in s:           return "Symantec"
    if "coveware" in s:                          return "Coveware"
    if "accenture" in s:                         return "Accenture"
    if "webroot" in s:                           return "Webroot"
    if "securityscore" in s or "ssc" in s:       return "SecurityScorecard"
    if "cisa" in s:                              return "CISA"
    if "nist" in s:                              return "NIST"
    if "wef" in s:                               return "World Economic Forum"
    if "enisa" in s:                             return "ENISA"
    if "microsoft" in s or "msft" in s:          return "Microsoft"
    if "google" in s:                            return "Google"
    if "paloalto" in s or "unit42" in s:         return "Palo Alto / Unit 42"
    if "sans" in s:                              return "SANS"
    return "Unknown"


def extract_year(stem):
    """Extract 4-digit year from filename stem."""
    m = re.search(r"(?<![0-9])(19|20)[0-9]{2}(?![0-9])", stem)
    return m.group(0) if m else "unknown"


def auto_classify(path):
    """Return best-guess metadata dict for a file."""
    stem = path.stem
    src_folder = path.parent.name
    return {
        "file_path":    str(path),
        "title":        stem.replace("_", " ").replace("-", " "),
        "organization": guess_org(stem),
        "content_type": guess_content_type(stem, src_folder),
        "year":         extract_year(stem),
        "tags":         "",
        "source_url":   "",
    }


# ---------------------------------------------------------------------------
# Manifest mode
# ---------------------------------------------------------------------------

def load_manifest(manifest_path):
    """Read batch_manifest.csv and return list of row dicts."""
    rows = []
    with open(manifest_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Skip blank or comment rows
            if not row.get("file_path") or row["file_path"].startswith("#"):
                continue
            rows.append(row)
    return rows


def validate_manifest(rows):
    """Check for missing required fields. Returns list of (row_idx, issue) tuples."""
    issues = []
    for i, row in enumerate(rows):
        path = Path(row.get("file_path", ""))
        if not path.exists():
            issues.append((i, f"File not found: {path}"))
        ct = row.get("content_type", "").strip()
        if ct and ct not in CONTENT_TYPE_CHOICES:
            issues.append((i, f"Invalid content_type '{ct}' -- must be one of: {', '.join(CONTENT_TYPE_CHOICES)}"))
    return issues


# ---------------------------------------------------------------------------
# Conversion
# ---------------------------------------------------------------------------

def convert_file(src_path, meta, dry_run=False):
    """Convert a single file using convert.py. Returns dest .md path."""
    args = [
        sys.executable, str(REPO_ROOT / "scripts" / "convert.py"),
        "--file", str(src_path),
        "--meta-title",  meta.get("title", src_path.stem),
        "--meta-org",    meta.get("organization", "Unknown"),
        "--meta-type",   meta.get("content_type", "misc"),
        "--meta-year",   str(meta.get("year", "unknown")),
        "--meta-url",    meta.get("source_url", ""),
    ]
    tags = meta.get("tags", "")
    if tags:
        tag_list = [t.strip() for t in tags.replace(",", " ").split() if t.strip()]
        if tag_list:
            args += ["--meta-tags"] + tag_list

    if dry_run:
        print(f"  [DRY RUN] would convert: {src_path.name}")
        return src_path.with_suffix(".md")

    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  [ERROR] Conversion failed for {src_path.name}:\n{result.stderr[:300]}")
        return None
    if result.stdout.strip():
        print(f"  {result.stdout.strip()}")
    return src_path.with_suffix(".md")


def place_file(src_pdf, md_src, meta, dry_run=False):
    """Move original PDF and its .md to the correct bucket folder."""
    bucket = BUCKET_MAP.get(meta.get("content_type", "misc"), "z_misc")
    dest_dir = REPO_ROOT / bucket

    if dry_run:
        print(f"  [DRY RUN] would place in: {bucket}/")
        return

    dest_dir.mkdir(exist_ok=True)

    # Move MD
    if md_src and md_src.exists():
        md_dest = dest_dir / md_src.name
        md_src.rename(md_dest)

    # Copy/move original PDF if it's not already in the bucket
    if src_pdf.exists() and src_pdf.parent != dest_dir:
        pdf_dest = dest_dir / src_pdf.name
        if not pdf_dest.exists():
            shutil.copy2(str(src_pdf), str(pdf_dest))
            print(f"  Copied PDF -> {bucket}/{src_pdf.name}")
        else:
            print(f"  PDF already exists in {bucket}/ -- skipping copy")


# ---------------------------------------------------------------------------
# Directory scan + group confirmation
# ---------------------------------------------------------------------------

def scan_directory(scan_dir):
    """Scan a directory for PDF/XLSX files and auto-classify each one."""
    scan_path = Path(scan_dir)
    files = sorted(
        f for f in scan_path.rglob("*")
        if f.is_file() and f.suffix.lower() in (".pdf", ".xlsx", ".xls")
    )
    return [auto_classify(f) for f in files]


def group_by_classification(rows):
    """Group rows by (org, content_type) for batch confirmation."""
    from collections import defaultdict
    groups = defaultdict(list)
    for row in rows:
        key = (row["organization"], row["content_type"])
        groups[key].append(row)
    return groups


def prompt_group_confirmation(groups):
    """
    Show auto-classified groups and let user confirm, reclassify, or skip.
    Returns final list of confirmed rows.
    """
    confirmed = []
    total_groups = len(groups)
    print(f"\n{total_groups} classification group(s) found:\n")

    for i, ((org, ct), rows) in enumerate(sorted(groups.items()), 1):
        print(f"Group {i}/{total_groups}: {org} / {ct} ({len(rows)} files)")
        for r in rows[:5]:
            print(f"    {Path(r['file_path']).name}  (year: {r['year']})")
        if len(rows) > 5:
            print(f"    ... and {len(rows) - 5} more")

        ans = input(
            f"\n  [C]onfirm, [R]eclassify, [S]kip, [E]dit individually? [C]: "
        ).strip().lower() or "c"

        if ans == "s":
            print(f"  Skipped {len(rows)} files.")
            continue
        elif ans == "r":
            new_org = input(f"  New organization [{org}]: ").strip() or org
            print(f"  Content types: {', '.join(CONTENT_TYPE_CHOICES)}")
            new_ct = input(f"  New content type [{ct}]: ").strip() or ct
            while new_ct not in CONTENT_TYPE_CHOICES:
                print(f"  Must be one of: {', '.join(CONTENT_TYPE_CHOICES)}")
                new_ct = input(f"  New content type [{ct}]: ").strip() or ct
            for r in rows:
                r["organization"] = new_org
                r["content_type"] = new_ct
            confirmed.extend(rows)
            print(f"  Reclassified {len(rows)} files -> {new_org} / {new_ct}")
        elif ans == "e":
            for r in rows:
                print(f"\n  File: {Path(r['file_path']).name}")
                r["title"]        = input(f"    Title [{r['title'][:50]}]: ").strip() or r["title"]
                r["organization"] = input(f"    Org [{r['organization']}]: ").strip() or r["organization"]
                print(f"    Types: {', '.join(CONTENT_TYPE_CHOICES)}")
                new_ct = input(f"    Content type [{r['content_type']}]: ").strip() or r["content_type"]
                if new_ct in CONTENT_TYPE_CHOICES:
                    r["content_type"] = new_ct
                r["year"]         = input(f"    Year [{r['year']}]: ").strip() or r["year"]
                confirmed.append(r)
        else:
            confirmed.extend(rows)
            print(f"  Confirmed {len(rows)} files.")

    return confirmed


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    p = argparse.ArgumentParser(description="Batch ingest files into tsudo/reference")
    mode = p.add_mutually_exclusive_group(required=True)
    mode.add_argument("--manifest", metavar="CSV", help="Path to batch_manifest.csv")
    mode.add_argument("--batch-dir", metavar="DIR", help="Directory to scan and ingest")
    p.add_argument("--dry-run", action="store_true",
                   help="Show what would happen without writing files")
    p.add_argument("--no-convert", action="store_true",
                   help="Copy PDFs to buckets without converting to MD")
    p.add_argument("--no-push", action="store_true", help="Skip git push")
    args = p.parse_args()

    dry = args.dry_run
    if dry:
        print("[batch-ingest] DRY RUN -- no files will be written\n")

    # Load rows
    if args.manifest:
        rows = load_manifest(args.manifest)
        issues = validate_manifest(rows)
        if issues:
            print("[batch-ingest] Manifest validation issues:")
            for idx, msg in issues:
                print(f"  Row {idx + 2}: {msg}")
            if not args.dry_run:
                cont = input("Continue anyway? [y/N]: ").strip().lower()
                if cont != "y":
                    sys.exit(1)
    else:
        print(f"[batch-ingest] Scanning {args.batch_dir}...")
        rows = scan_directory(args.batch_dir)
        if not rows:
            print("No PDF/XLSX files found.")
            sys.exit(0)
        print(f"Found {len(rows)} files.\n")
        groups = group_by_classification(rows)
        rows = prompt_group_confirmation(groups)
        if not rows:
            print("Nothing to ingest.")
            sys.exit(0)

    print(f"\n[batch-ingest] Ingesting {len(rows)} files...\n")
    success, failed = 0, 0

    for row in rows:
        src = Path(row["file_path"])
        print(f"Processing: {src.name}")

        if not src.exists():
            print(f"  [SKIP] File not found: {src}")
            failed += 1
            continue

        if not args.no_convert and src.suffix.lower() in (".pdf", ".xlsx", ".xls"):
            md_path = convert_file(src, row, dry_run=dry)
        else:
            md_path = None

        place_file(src, md_path, row, dry_run=dry)
        success += 1

    print(f"\n[batch-ingest] Done: {success} ingested, {failed} failed/skipped")

    if dry:
        print("[batch-ingest] DRY RUN complete -- no files were written")
        return

    # Regen catalog
    r = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "catalog.py"),
         "--repo-root", str(REPO_ROOT)],
        capture_output=True, text=True
    )
    print(r.stdout.strip())

    # Git commit + push
    msg = f"ingest: batch add {success} documents"
    subprocess.run(["git", "-C", str(REPO_ROOT), "add", "."], check=True)
    subprocess.run(["git", "-C", str(REPO_ROOT), "commit", "-m", msg], check=True)

    if not args.no_push:
        ans = input("Push to remote? [Y/n]: ").strip().lower()
        if ans != "n":
            subprocess.run(["git", "-C", str(REPO_ROOT), "push"], check=True)
            print("[batch-ingest] Pushed.")


if __name__ == "__main__":
    main()
