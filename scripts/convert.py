#!/usr/bin/env python3
"""
convert.py — PDF-to-Markdown and XLSX-to-CSV conversion for tsudo/reference.

Usage:
    python scripts/convert.py --file path/to/document.pdf [--meta-org ORG] [--meta-year YEAR] ...
    python scripts/convert.py --file path/to/sheet.xlsx

Converted files are written alongside the original (same folder, .md extension).
YAML frontmatter is injected at the top of every converted .md file.
"""

import argparse
import sys
from pathlib import Path
from datetime import date


# ---------------------------------------------------------------------------
# YAML frontmatter template
# ---------------------------------------------------------------------------

FRONTMATTER_TEMPLATE = """\
---
title: "{title}"
organization: "{organization}"
content_type: {content_type}
year: {year}
tags: {tags}
source_url: "{source_url}"
license: "{license}"
date_ingested: {date_ingested}
original_format: {original_format}
---

"""

DEFAULT_LICENSE = "© {organization}. Reproduced for research and educational purposes per 17 U.S.C. § 107 (fair use)."

CONTENT_TYPE_CHOICES = [
    "threat-intel",
    "breach-report",
    "government",
    "research",
    "framework",
    "standard",
    "tool-template",
    "misc",
]


def build_frontmatter(
    title: str,
    organization: str,
    content_type: str,
    year: int | str,
    tags: list[str],
    source_url: str,
    license_text: str | None,
    original_format: str,
) -> str:
    if license_text is None:
        license_text = DEFAULT_LICENSE.format(organization=organization)
    tags_str = "[" + ", ".join(f'"{t}"' for t in tags) + "]"
    return FRONTMATTER_TEMPLATE.format(
        title=title,
        organization=organization,
        content_type=content_type,
        year=year,
        tags=tags_str,
        source_url=source_url,
        license=license_text,
        date_ingested=date.today().isoformat(),
        original_format=original_format,
    )


# ---------------------------------------------------------------------------
# PDF conversion via markitdown
# ---------------------------------------------------------------------------

def convert_pdf(src: Path, meta: dict) -> Path:
    """Convert a PDF to Markdown using markitdown, inject frontmatter."""
    try:
        from markitdown import MarkItDown
    except ImportError:
        sys.exit("markitdown not installed — run: pip install markitdown[all]")

    md_converter = MarkItDown()
    result = md_converter.convert(str(src))
    body = result.text_content

    frontmatter = build_frontmatter(
        title=meta.get("title", src.stem.replace("_", " ")),
        organization=meta.get("organization", "Unknown"),
        content_type=meta.get("content_type", "misc"),
        year=meta.get("year", "unknown"),
        tags=meta.get("tags", []),
        source_url=meta.get("source_url", ""),
        license_text=meta.get("license"),
        original_format="pdf",
    )

    out_path = src.with_suffix(".md")
    out_path.write_text(frontmatter + body, encoding="utf-8")
    print(f"[convert] PDF → {out_path}")
    return out_path


# ---------------------------------------------------------------------------
# XLSX conversion via pandas
# ---------------------------------------------------------------------------

def convert_xlsx(src: Path, meta: dict) -> tuple[Path, Path]:
    """Convert an XLSX to CSV + a Markdown summary table."""
    try:
        import pandas as pd
    except ImportError:
        sys.exit("pandas not installed — run: pip install pandas openpyxl")

    dfs = pd.read_excel(src, sheet_name=None, engine="openpyxl")

    # Write CSV for first (or only) sheet
    first_sheet = list(dfs.keys())[0]
    df = dfs[first_sheet]
    csv_path = src.with_suffix(".csv")
    df.to_csv(csv_path, index=False)
    print(f"[convert] XLSX → CSV: {csv_path}")

    # Build Markdown summary (first 20 rows of first sheet)
    md_table = df.head(20).to_markdown(index=False)
    frontmatter = build_frontmatter(
        title=meta.get("title", src.stem.replace("_", " ")),
        organization=meta.get("organization", "Unknown"),
        content_type=meta.get("content_type", "misc"),
        year=meta.get("year", "unknown"),
        tags=meta.get("tags", []),
        source_url=meta.get("source_url", ""),
        license_text=meta.get("license"),
        original_format="xlsx",
    )
    summary = f"# {src.stem}\n\n_Sheet: {first_sheet} — first 20 rows shown_\n\n{md_table}\n"
    md_path = src.with_suffix(".md")
    md_path.write_text(frontmatter + summary, encoding="utf-8")
    print(f"[convert] XLSX → MD summary: {md_path}")

    return csv_path, md_path


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args():
    p = argparse.ArgumentParser(description="Convert PDF/XLSX to Markdown for tsudo/reference.")
    p.add_argument("--file", required=True, help="Path to source file (PDF or XLSX)")
    p.add_argument("--meta-title", dest="title", help="Document title")
    p.add_argument("--meta-org", dest="organization", help="Publishing organization")
    p.add_argument("--meta-type", dest="content_type", choices=CONTENT_TYPE_CHOICES, help="Content type bucket")
    p.add_argument("--meta-year", dest="year", help="Publication year")
    p.add_argument("--meta-tags", dest="tags", nargs="+", help="Space-separated tags")
    p.add_argument("--meta-url", dest="source_url", default="", help="Source URL")
    return p.parse_args()


def main():
    args = parse_args()
    src = Path(args.file)
    if not src.exists():
        sys.exit(f"File not found: {src}")

    meta = {
        "title": args.title or src.stem.replace("_", " "),
        "organization": args.organization or "Unknown",
        "content_type": args.content_type or "misc",
        "year": args.year or "unknown",
        "tags": args.tags or [],
        "source_url": args.source_url,
    }

    suffix = src.suffix.lower()
    if suffix == ".pdf":
        convert_pdf(src, meta)
    elif suffix in (".xlsx", ".xls"):
        convert_xlsx(src, meta)
    else:
        sys.exit(f"Unsupported format: {suffix}. Supported: .pdf, .xlsx, .xls")


if __name__ == "__main__":
    main()
