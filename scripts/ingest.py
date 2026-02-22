#!/usr/bin/env python3
"""
ingest.py — Interactive ingest CLI for tsudo/reference.

Downloads (if URL), converts to Markdown, prompts for metadata,
writes to the correct bucket folder, then regenerates CATALOG.csv and INDEX.md.

Usage:
    python scripts/ingest.py [URL or local path]
    python scripts/ingest.py --non-interactive --file path --org ORG --type TYPE --year YEAR --title TITLE
"""

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path

# Repo root is the parent of scripts/
REPO_ROOT = Path(__file__).parent.parent

BUCKET_MAP = {
    "framework": "frameworks",
    "threat-intel": "threat-intel",
    "breach-report": "breach-reports",
    "government": "government",
    "research": "research",
    "standard": "standards",
    "tool-template": "tools-templates",
    "misc": "z_misc",
}

CONTENT_TYPE_CHOICES = list(BUCKET_MAP.keys())


# ---------------------------------------------------------------------------
# Download helpers
# ---------------------------------------------------------------------------

def try_jina(url: str) -> str | None:
    """Try fetching via Jina AI Reader (returns markdown text or None)."""
    try:
        import requests
        jina_url = f"https://r.jina.ai/{url}"
        resp = requests.get(jina_url, timeout=30)
        if resp.ok and len(resp.text) > 500:
            return resp.text
    except Exception as e:
        print(f"[ingest] Jina fetch failed: {e}")
    return None


def download_file(url: str, dest_dir: Path) -> Path:
    """Download a file from URL to dest_dir. Returns local path."""
    try:
        import requests
    except ImportError:
        sys.exit("requests not installed — run: pip install requests")

    resp = requests.get(url, timeout=60, stream=True)
    resp.raise_for_status()

    # Determine filename
    cd = resp.headers.get("Content-Disposition", "")
    if "filename=" in cd:
        fname = cd.split("filename=")[-1].strip().strip('"')
    else:
        fname = url.rstrip("/").split("/")[-1]
        if "." not in fname:
            ctype = resp.headers.get("Content-Type", "")
            if "pdf" in ctype:
                fname += ".pdf"
            else:
                fname += ".html"

    dest = dest_dir / fname
    with dest.open("wb") as f:
        for chunk in resp.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"[ingest] Downloaded → {dest}")
    return dest


# ---------------------------------------------------------------------------
# Conversion
# ---------------------------------------------------------------------------

def convert_file(src: Path, meta: dict) -> Path:
    """Convert src to .md using convert.py. Returns path to .md file."""
    args = [
        sys.executable, str(REPO_ROOT / "scripts" / "convert.py"),
        "--file", str(src),
        "--meta-title", meta["title"],
        "--meta-org", meta["organization"],
        "--meta-type", meta["content_type"],
        "--meta-year", str(meta["year"]),
        "--meta-url", meta.get("source_url", ""),
    ]
    if meta.get("tags"):
        args += ["--meta-tags"] + meta["tags"]

    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"[ingest] Conversion error:\n{result.stderr}")
        sys.exit(1)
    print(result.stdout.strip())
    return src.with_suffix(".md")


# ---------------------------------------------------------------------------
# Interactive metadata prompts
# ---------------------------------------------------------------------------

def prompt(label: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    val = input(f"{label}{suffix}: ").strip()
    return val if val else default


def prompt_meta(source_hint: str = "", url: str = "") -> dict:
    print("\n--- Metadata ---")
    title = prompt("Title", source_hint)
    organization = prompt("Organization (e.g. Verizon, CISA)")
    print(f"Content types: {', '.join(CONTENT_TYPE_CHOICES)}")
    content_type = prompt("Content type", "misc")
    while content_type not in CONTENT_TYPE_CHOICES:
        print(f"  Must be one of: {', '.join(CONTENT_TYPE_CHOICES)}")
        content_type = prompt("Content type", "misc")
    year = prompt("Publication year", "unknown")
    tags_raw = prompt("Tags (space-separated, e.g. ransomware phishing ai)", "")
    tags = tags_raw.split() if tags_raw else []
    source_url = prompt("Source URL", url)
    return {
        "title": title,
        "organization": organization,
        "content_type": content_type,
        "year": year,
        "tags": tags,
        "source_url": source_url,
    }


# ---------------------------------------------------------------------------
# Place file in correct bucket
# ---------------------------------------------------------------------------

def place_in_bucket(src: Path, meta: dict) -> Path:
    """Copy/move converted .md (and original) to correct bucket folder."""
    bucket = BUCKET_MAP.get(meta["content_type"], "z_misc")
    dest_dir = REPO_ROOT / bucket
    dest_dir.mkdir(exist_ok=True)

    md_src = src.with_suffix(".md")
    md_dest = dest_dir / md_src.name
    md_src.rename(md_dest)
    print(f"[ingest] Placed MD → {md_dest.relative_to(REPO_ROOT)}")

    # Move original file too if it's not already in the right place
    if src.parent != dest_dir and src.exists():
        orig_dest = dest_dir / src.name
        src.rename(orig_dest)
        print(f"[ingest] Placed original → {orig_dest.relative_to(REPO_ROOT)}")
        return orig_dest

    return src


# ---------------------------------------------------------------------------
# Catalog regeneration
# ---------------------------------------------------------------------------

def regen_catalog():
    result = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "catalog.py"),
         "--repo-root", str(REPO_ROOT)],
        capture_output=True, text=True
    )
    print(result.stdout.strip())
    if result.returncode != 0:
        print(f"[ingest] Catalog error:\n{result.stderr}")


# ---------------------------------------------------------------------------
# Git commit and push
# ---------------------------------------------------------------------------

def git_commit_push(meta: dict):
    msg = f"ingest: add {meta['title']} ({meta['organization']}, {meta['year']})"
    subprocess.run(["git", "-C", str(REPO_ROOT), "add", "."], check=True)
    subprocess.run(["git", "-C", str(REPO_ROOT), "commit", "-m", msg], check=True)

    push = input("\nPush to remote? [Y/n]: ").strip().lower()
    if push != "n":
        subprocess.run(["git", "-C", str(REPO_ROOT), "push"], check=True)
        print("[ingest] Pushed to remote.")
    else:
        print("[ingest] Skipped push — run 'git push' when ready.")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    p = argparse.ArgumentParser(description="Ingest a document into tsudo/reference")
    p.add_argument("source", nargs="?", help="URL or local file path")
    p.add_argument("--non-interactive", action="store_true")
    p.add_argument("--file", help="Local file path (non-interactive mode)")
    p.add_argument("--org", help="Organization")
    p.add_argument("--type", dest="content_type", choices=CONTENT_TYPE_CHOICES)
    p.add_argument("--year", help="Publication year")
    p.add_argument("--title", help="Document title")
    p.add_argument("--url", default="", help="Source URL")
    p.add_argument("--tags", nargs="+", help="Tags")
    p.add_argument("--no-push", action="store_true", help="Skip git push")
    args = p.parse_args()

    source = args.source or args.file
    if not source:
        p.print_help()
        sys.exit(1)

    is_url = source.startswith(("http://", "https://"))

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)

        if is_url:
            url = source
            # Try Jina for web documents first
            if not source.endswith(".pdf"):
                jina_text = try_jina(url)
                if jina_text:
                    print(f"[ingest] Fetched via Jina AI Reader ({len(jina_text)} chars)")
                    meta = prompt_meta(source_hint=url.split("/")[-1], url=url) if not args.non_interactive else {
                        "title": args.title or url.split("/")[-1],
                        "organization": args.org or "Unknown",
                        "content_type": args.content_type or "misc",
                        "year": args.year or "unknown",
                        "tags": args.tags or [],
                        "source_url": url,
                    }
                    bucket = BUCKET_MAP.get(meta["content_type"], "z_misc")
                    dest_dir = REPO_ROOT / bucket
                    dest_dir.mkdir(exist_ok=True)
                    safe_name = re.sub(r"[^\w\-.]", "_", meta["title"])[:80] + ".md"
                    from convert import build_frontmatter
                    fm = build_frontmatter(
                        title=meta["title"],
                        organization=meta["organization"],
                        content_type=meta["content_type"],
                        year=meta["year"],
                        tags=meta.get("tags", []),
                        source_url=meta["source_url"],
                        license_text=None,
                        original_format="html",
                    )
                    out = dest_dir / safe_name
                    out.write_text(fm + jina_text, encoding="utf-8")
                    print(f"[ingest] Saved → {out.relative_to(REPO_ROOT)}")
                    regen_catalog()
                    if not args.no_push:
                        git_commit_push(meta)
                    return

            # Download PDF
            local_file = download_file(url, tmp_path)
        else:
            local_file = Path(source)
            url = args.url or ""

        if not local_file.exists():
            sys.exit(f"File not found: {local_file}")

        if args.non_interactive:
            meta = {
                "title": args.title or local_file.stem.replace("_", " "),
                "organization": args.org or "Unknown",
                "content_type": args.content_type or "misc",
                "year": args.year or "unknown",
                "tags": args.tags or [],
                "source_url": url,
            }
        else:
            meta = prompt_meta(source_hint=local_file.stem.replace("_", " "), url=url)

        # Convert
        md_path = convert_file(local_file, meta)

        # Place in bucket
        place_in_bucket(local_file, meta)

        # Regen catalog
        regen_catalog()

        # Commit + push
        if not args.no_push:
            git_commit_push(meta)


if __name__ == "__main__":
    import re
    main()
