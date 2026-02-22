#!/usr/bin/env python3
"""
catalog.py — Regenerate CATALOG.csv and INDEX.md from all files in tsudo/reference.

Reads YAML frontmatter from every .md file (skipping README, INDEX).
Falls back to filename parsing for PDFs without a paired .md file.

Usage:
    python scripts/catalog.py [--repo-root PATH]

Outputs:
    CATALOG.csv   — machine-readable catalog
    INDEX.md      — human-readable index (by content type + by organization)
"""

import csv
import re
import sys
from pathlib import Path
from datetime import date

# Optional yaml support
try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False
    print("[catalog] Warning: pyyaml not installed — frontmatter parsing disabled", file=sys.stderr)


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

CATALOG_FIELDS = [
    "filename",
    "folder",
    "organization",
    "content_type",
    "title",
    "year",
    "tags",
    "source_url",
    "format",
    "md_available",
    "date_ingested",
]

SKIP_FILES = {"README.md", "INDEX.md", "CATALOG.csv", "stats.md"}

BUCKET_DIRS = {
    "frameworks", "threat-intel", "breach-reports", "government",
    "research", "standards", "tools-templates", "z_misc",
}

CONTENT_TYPE_LABELS = {
    "threat-intel": "Threat Intelligence",
    "breach-report": "Breach Reports",
    "government": "Government & Regulatory",
    "research": "Research",
    "framework": "Frameworks",
    "standard": "Standards",
    "tool-template": "Tools & Templates",
    "misc": "Miscellaneous",
}


# ---------------------------------------------------------------------------
# Frontmatter parsing
# ---------------------------------------------------------------------------

def parse_frontmatter(md_path: Path) -> dict:
    """Extract YAML frontmatter from a markdown file."""
    if not HAS_YAML:
        return {}
    text = md_path.read_text(encoding="utf-8", errors="replace")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return {}
    try:
        return yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        return {}


def guess_meta_from_filename(path: Path, folder: str) -> dict:
    """Derive best-effort metadata from filename when no frontmatter exists."""
    stem = path.stem
    # Try to extract year (4-digit number)
    year_match = re.search(r"(?<![0-9])(19|20)[0-9]{2}(?![0-9])", stem)
    year = year_match.group(0) if year_match else "unknown"

    # Derive organization from folder or filename prefix
    org_map = {
        "breach-reports": _guess_org_breach(stem),
        "government": _guess_org_gov(stem),
        "threat-intel": _guess_org_threat(stem),
        "research": _guess_org_research(stem),
        "tools-templates": "Various",
        "z_misc": "Various",
    }
    org = org_map.get(folder, "Unknown")

    content_type_map = {
        "breach-reports": "breach-report",
        "government": "government",
        "threat-intel": "threat-intel",
        "research": "research",
        "frameworks": "framework",
        "standards": "standard",
        "tools-templates": "tool-template",
        "z_misc": "misc",
    }

    return {
        "title": stem.replace("_", " ").replace("-", " "),
        "organization": org,
        "content_type": content_type_map.get(folder, "misc"),
        "year": year,
        "tags": [],
        "source_url": "",
    }


def _guess_org_breach(stem: str) -> str:
    stem_lower = stem.lower()
    if "verizon" in stem_lower or "dbir" in stem_lower:
        return "Verizon"
    if "ponemon" in stem_lower or "ibm" in stem_lower or "cost" in stem_lower.replace(" ", ""):
        return "IBM/Ponemon"
    if "anthem" in stem_lower:
        return "Anthem"
    if "equifax" in stem_lower:
        return "Equifax"
    return "Unknown"


def _guess_org_gov(stem: str) -> str:
    stem_lower = stem.lower()
    if "cisa" in stem_lower or "chinese-cyber" in stem_lower:
        return "CISA"
    if "ata" in stem_lower or "wwta" in stem_lower or "usni" in stem_lower:
        return "US Intelligence Community"
    return "US Government"


def _guess_org_threat(stem: str) -> str:
    stem_lower = stem.lower()
    if "cisco" in stem_lower:
        return "Cisco"
    if "accenture" in stem_lower:
        return "Accenture"
    if "proofpoint" in stem_lower or "pfpt" in stem_lower:
        return "Proofpoint"
    if "webroot" in stem_lower:
        return "Webroot"
    if "ssc" in stem_lower or "securityscore" in stem_lower:
        return "SecurityScorecard"
    if "symantec" in stem_lower or "istr" in stem_lower:
        return "Symantec"
    if "coveware" in stem_lower:
        return "Coveware"
    return "Unknown"


def _guess_org_research(stem: str) -> str:
    if "wef" in stem.lower():
        return "World Economic Forum"
    return "Unknown"


# ---------------------------------------------------------------------------
# Catalog builder
# ---------------------------------------------------------------------------

def build_catalog(repo_root: Path) -> list[dict]:
    """Walk repo, collect metadata for every document."""
    records = []
    seen_stems = set()  # avoid double-counting PDF + MD pairs

    for bucket in BUCKET_DIRS:
        bucket_path = repo_root / bucket
        if not bucket_path.exists():
            continue

        for item in sorted(bucket_path.iterdir()):
            if item.is_dir():
                continue
            if item.name in SKIP_FILES:
                continue
            if item.suffix.lower() not in (".pdf", ".md", ".csv", ".xlsx"):
                continue

            stem = item.stem
            is_md = item.suffix.lower() == ".md"
            is_pdf = item.suffix.lower() == ".pdf"

            # For MD files paired with a PDF, we'll handle when we see the PDF
            paired_pdf = item.with_suffix(".pdf")
            paired_md = item.with_suffix(".md")

            if is_md and paired_pdf.exists():
                continue  # skip — will be captured via PDF entry

            md_available = False
            meta = {}

            if is_md:
                md_available = True
                meta = parse_frontmatter(item)
            elif is_pdf:
                if paired_md.exists():
                    md_available = True
                    meta = parse_frontmatter(paired_md)

            if not meta:
                meta = guess_meta_from_filename(item, bucket)

            tags = meta.get("tags", [])
            if isinstance(tags, list):
                tags_str = ",".join(tags)
            else:
                tags_str = str(tags)

            record = {
                "filename": item.name,
                "folder": bucket,
                "organization": meta.get("organization", "Unknown"),
                "content_type": meta.get("content_type", "misc"),
                "title": meta.get("title", stem.replace("_", " ")),
                "year": str(meta.get("year", "unknown")),
                "tags": tags_str,
                "source_url": meta.get("source_url", ""),
                "format": item.suffix.lstrip(".").upper(),
                "md_available": "yes" if md_available else "no",
                "date_ingested": str(meta.get("date_ingested", "")),
            }
            records.append(record)

    # Also include top-level files in tools-templates bucket (GPG cheatsheet etc.)
    return records


# ---------------------------------------------------------------------------
# CATALOG.csv writer
# ---------------------------------------------------------------------------

def write_catalog(records: list[dict], output: Path):
    with output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CATALOG_FIELDS)
        writer.writeheader()
        writer.writerows(records)
    print(f"[catalog] Wrote {len(records)} records -> {output}")


# ---------------------------------------------------------------------------
# INDEX.md writer
# ---------------------------------------------------------------------------

def write_index(records: list[dict], output: Path):
    lines = [
        "# Reference Library Index",
        "",
        f"_Auto-generated {date.today().isoformat()} — {len(records)} documents_",
        "",
        "## Contents",
        "",
        "- [By Content Type](#by-content-type)",
        "- [By Organization](#by-organization)",
        "",
        "---",
        "",
        "## By Content Type",
        "",
    ]

    # Group by content_type
    from collections import defaultdict
    by_type = defaultdict(list)
    for r in records:
        by_type[r["content_type"]].append(r)

    for ct, label in CONTENT_TYPE_LABELS.items():
        items = by_type.get(ct, [])
        if not items:
            continue
        lines.append(f"### {label}")
        lines.append("")
        lines.append("| Title | Organization | Year | Format | MD |")
        lines.append("|-------|-------------|------|--------|----|")
        for r in sorted(items, key=lambda x: (x["organization"], x["year"])):
            md_flag = "✓" if r["md_available"] == "yes" else ""
            title = r["title"]
            if r["source_url"]:
                title = f"[{title}]({r['source_url']})"
            lines.append(f"| {title} | {r['organization']} | {r['year']} | {r['format']} | {md_flag} |")
        lines.append("")

    # Misc catch-all
    misc_items = by_type.get("misc", [])
    if misc_items:
        lines.append("### Miscellaneous")
        lines.append("")
        lines.append("| Title | Year | Format |")
        lines.append("|-------|------|--------|")
        for r in sorted(misc_items, key=lambda x: x["year"]):
            lines.append(f"| {r['title']} | {r['year']} | {r['format']} |")
        lines.append("")

    lines += [
        "---",
        "",
        "## By Organization",
        "",
    ]

    by_org = defaultdict(list)
    for r in records:
        by_org[r["organization"]].append(r)

    for org in sorted(by_org.keys()):
        items = by_org[org]
        lines.append(f"### {org}")
        lines.append("")
        for r in sorted(items, key=lambda x: x["year"]):
            md_flag = " [MD]" if r["md_available"] == "yes" else ""
            lines.append(f"- {r['title']} ({r['year']}) — `{r['folder']}/{r['filename']}`{md_flag}")
        lines.append("")

    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[catalog] Wrote index -> {output}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    import argparse
    p = argparse.ArgumentParser(description="Regenerate CATALOG.csv and INDEX.md")
    p.add_argument("--repo-root", default=".", help="Path to repo root (default: current dir)")
    args = p.parse_args()

    repo_root = Path(args.repo_root).resolve()
    records = build_catalog(repo_root)

    if not records:
        print("[catalog] No records found — check that bucket folders exist and contain files.")
        return

    write_catalog(records, repo_root / "CATALOG.csv")
    write_index(records, repo_root / "INDEX.md")


if __name__ == "__main__":
    main()
