#!/usr/bin/env python3
"""
update_routine.py — Semiannual update check for tsudo/reference.

Reads sources.yaml and compares latest_known_year against the current year
to surface potentially outdated entries. Does NOT automatically download;
it produces a report for human review.

Usage:
    python scripts/update_routine.py [--sources scripts/sources.yaml]
    python scripts/update_routine.py --catalog CATALOG.csv --check-missing
"""

import argparse
import csv
import sys
from datetime import date
from pathlib import Path

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False
    sys.exit("pyyaml required — run: pip install pyyaml")


REPO_ROOT = Path(__file__).parent.parent
CURRENT_YEAR = date.today().year


def load_sources(sources_path: Path) -> list[dict]:
    with sources_path.open(encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data.get("sources", [])


def load_catalog(catalog_path: Path) -> list[dict]:
    if not catalog_path.exists():
        print(f"[update] CATALOG.csv not found at {catalog_path} — run catalog.py first.")
        return []
    with catalog_path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def check_outdated(sources: list[dict]) -> list[dict]:
    """Flag sources where latest_known_year < current_year - 1 (more than 1 year behind)."""
    stale = []
    for s in sources:
        lky = s.get("latest_known_year")
        if lky is None:
            s["_status"] = "NOT IN COLLECTION"
            stale.append(s)
        elif isinstance(lky, int) and lky < CURRENT_YEAR - 1:
            years_behind = CURRENT_YEAR - lky
            s["_status"] = f"STALE ({years_behind} year(s) behind)"
            stale.append(s)
        elif isinstance(lky, int) and lky == CURRENT_YEAR - 1:
            s["_status"] = "CHECK — may have new edition"
            stale.append(s)
    return stale


def check_missing_from_catalog(sources: list[dict], catalog: list[dict]) -> list[dict]:
    """Find sources.yaml entries with latest_known_year but no matching catalog entry."""
    catalog_orgs = {r["organization"].lower() for r in catalog}
    missing = []
    for s in sources:
        if s.get("latest_known_year") is None:
            continue  # already flagged as not in collection
        org_lower = s["org"].lower()
        if org_lower not in catalog_orgs:
            missing.append(s)
    return missing


def print_report(stale: list[dict]):
    print(f"\n{'='*60}")
    print(f"  Semiannual Update Check — {date.today().isoformat()}")
    print(f"  Current year: {CURRENT_YEAR}")
    print(f"{'='*60}\n")

    not_in_collection = [s for s in stale if s["_status"] == "NOT IN COLLECTION"]
    needs_update = [s for s in stale if "STALE" in s["_status"]]
    check_items = [s for s in stale if "CHECK" in s["_status"]]

    if not_in_collection:
        print(f"NOT IN COLLECTION ({len(not_in_collection)} sources):")
        print("-" * 40)
        for s in not_in_collection:
            print(f"  [ ] {s['org']} — {s['name']}")
            print(f"      Type: {s['content_type']} | URL: {s.get('url_pattern', 'N/A')}")
            if s.get("notes"):
                print(f"      Note: {s['notes']}")
        print()

    if needs_update:
        print(f"STALE — Needs Update ({len(needs_update)} sources):")
        print("-" * 40)
        for s in needs_update:
            print(f"  [ ] {s['org']} — {s['name']} (last: {s['latest_known_year']})")
            print(f"      {s['_status']} | URL: {s.get('url_pattern', 'N/A')}")
        print()

    if check_items:
        print(f"CHECK — Possible New Edition ({len(check_items)} sources):")
        print("-" * 40)
        for s in check_items:
            print(f"  [ ] {s['org']} — {s['name']} (last: {s['latest_known_year']})")
            print(f"      URL: {s.get('url_pattern', 'N/A')}")
        print()

    total = len(not_in_collection) + len(needs_update) + len(check_items)
    if total == 0:
        print("Collection is up to date!")
    else:
        print(f"Total items to review: {total}")
        print(f"\nTo ingest a new document:")
        print("  python scripts/ingest.py <URL or path>")
        print("  # or from Claude Code:")
        print("  /ingest <URL or path>")

    print()


def main():
    p = argparse.ArgumentParser(description="Semiannual reference collection update check")
    p.add_argument("--sources", default=str(REPO_ROOT / "scripts" / "sources.yaml"),
                   help="Path to sources.yaml")
    p.add_argument("--catalog", default=str(REPO_ROOT / "CATALOG.csv"),
                   help="Path to CATALOG.csv")
    p.add_argument("--check-missing", action="store_true",
                   help="Also check for sources.yaml entries missing from CATALOG.csv")
    args = p.parse_args()

    sources_path = Path(args.sources)
    if not sources_path.exists():
        sys.exit(f"sources.yaml not found: {sources_path}")

    sources = load_sources(sources_path)
    stale = check_outdated(sources)

    if args.check_missing:
        catalog = load_catalog(Path(args.catalog))
        if catalog:
            missing = check_missing_from_catalog(sources, catalog)
            for s in missing:
                if not any(x["org"] == s["org"] and x["name"] == s["name"] for x in stale):
                    s["_status"] = "IN SOURCES BUT NOT CATALOG"
                    stale.append(s)

    print_report(stale)


if __name__ == "__main__":
    main()
