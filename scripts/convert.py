#!/usr/bin/env python3
"""
convert.py -- PDF-to-Markdown and XLSX/ZIP conversion for tsudo/reference.

Usage:
    python scripts/convert.py --file path/to/document.pdf [--meta-org ORG] [--meta-year YEAR] ...
    python scripts/convert.py --file path/to/sheet.xlsx
    python scripts/convert.py --file path/to/bundle.zip

Converted files are written alongside the original (same folder, .md extension).
YAML frontmatter is injected at the top of every converted .md file.
"""

import argparse
import re
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

def _safe_sheet_name(name: str) -> str:
    """Sanitize a sheet name for use in filenames."""
    return re.sub(r"[^\w\-]", "_", name).strip("_")


def _df_to_markdown(df) -> str:
    """Convert a DataFrame to a markdown table, with tabulate if available."""
    try:
        return df.to_markdown(index=False)
    except ImportError:
        # Fallback: simple pipe-delimited table without tabulate
        cols = list(df.columns)
        header = "| " + " | ".join(str(c) for c in cols) + " |"
        sep    = "| " + " | ".join("---" for _ in cols) + " |"
        rows   = []
        for _, row in df.iterrows():
            rows.append("| " + " | ".join(str(v) for v in row) + " |")
        return "\n".join([header, sep] + rows)


def convert_xlsx(src: Path, meta: dict) -> tuple:
    """
    Convert an XLSX to:
      - One CSV per sheet  (src_SheetName.csv, or src.csv if single sheet)
      - One .md with frontmatter + a full table section per non-empty sheet

    Returns (csv_paths: list[Path], md_path: Path).
    """
    try:
        import pandas as pd
    except ImportError:
        sys.exit("pandas not installed -- run: pip install pandas openpyxl")

    dfs = pd.read_excel(src, sheet_name=None, engine="openpyxl")
    multi = len(dfs) > 1

    csv_paths = []
    sheet_sections = []

    for sheet_name, df in dfs.items():
        if df.empty:
            print(f"[convert]   Sheet '{sheet_name}' is empty -- skipping")
            continue

        # Drop rows that are entirely NaN (common in questionnaire XLSXs)
        df = df.dropna(how="all").reset_index(drop=True)

        # Per-sheet CSV
        csv_name = f"{src.stem}_{_safe_sheet_name(sheet_name)}.csv" if multi else f"{src.stem}.csv"
        csv_path = src.parent / csv_name
        df.to_csv(csv_path, index=False, encoding="utf-8")
        csv_paths.append(csv_path)
        print(f"[convert]   Sheet '{sheet_name}': {len(df)} rows x {len(df.columns)} cols -> {csv_path.name}")

        # Full markdown table for this sheet (all rows)
        md_table = _df_to_markdown(df)
        sheet_sections.append(
            f"## Sheet: {sheet_name}\n\n"
            f"_{len(df)} rows x {len(df.columns)} columns_\n\n"
            f"{md_table}\n"
        )

    if not sheet_sections:
        print(f"[convert] WARNING: no usable sheets found in {src.name}")
        return csv_paths, src.with_suffix(".md")

    title = meta.get("title", src.stem.replace("_", " "))
    body = (
        f"# {title}\n\n"
        f"_{len(sheet_sections)} sheet(s): {', '.join(dfs.keys())}_\n\n"
        + "\n\n".join(sheet_sections)
    )

    frontmatter = build_frontmatter(
        title=title,
        organization=meta.get("organization", "Unknown"),
        content_type=meta.get("content_type", "misc"),
        year=meta.get("year", "unknown"),
        tags=meta.get("tags", []),
        source_url=meta.get("source_url", ""),
        license_text=meta.get("license"),
        original_format="xlsx",
    )

    md_path = src.with_suffix(".md")
    md_path.write_text(frontmatter + body, encoding="utf-8")
    total_rows = sum(len(df) for df in dfs.values())
    print(f"[convert] XLSX -> {md_path.name} ({len(sheet_sections)} sheets, {total_rows} total rows)")

    return csv_paths, md_path


# ---------------------------------------------------------------------------
# ZIP handling -- extract and convert contained XLSX/PDF files
# ---------------------------------------------------------------------------

def convert_zip(src: Path, meta: dict) -> list:
    """
    Extract a ZIP and convert all contained XLSX/XLS/PDF files.
    Extracted files land in a subfolder named after the ZIP stem.
    Returns list of generated .md paths.
    """
    import zipfile

    extract_dir = src.parent / src.stem
    extract_dir.mkdir(exist_ok=True)

    with zipfile.ZipFile(src, "r") as zf:
        zf.extractall(extract_dir)
    print(f"[convert] ZIP extracted to {extract_dir.name}/")

    targets = sorted(
        f for f in extract_dir.rglob("*")
        if f.is_file()
        and f.suffix.lower() in (".xlsx", ".xls", ".pdf")
        and not f.name.startswith("~$")  # skip Excel temp/lock files
    )

    if not targets:
        print(f"[convert] WARNING: no XLSX/PDF files found inside {src.name}")
        return []

    md_paths = []
    for f in targets:
        print(f"[convert] Processing {f.name} from ZIP...")
        file_meta = dict(meta)
        file_meta["title"] = f.stem.replace("_", " ").replace("-", " ")
        if f.suffix.lower() in (".xlsx", ".xls"):
            _, md = convert_xlsx(f, file_meta)
        else:
            md = convert_pdf(f, file_meta)
        md_paths.append(md)

    return md_paths


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args():
    p = argparse.ArgumentParser(description="Convert PDF/XLSX/ZIP to Markdown for tsudo/reference.")
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
    elif suffix == ".zip":
        convert_zip(src, meta)
    else:
        sys.exit(f"Unsupported format: {suffix}. Supported: .pdf, .xlsx, .xls, .zip")


if __name__ == "__main__":
    main()
