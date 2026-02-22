#!/usr/bin/env python3
"""
add_link.py -- Add an external reference stub to tsudo/reference.

Creates a lightweight .md file with YAML frontmatter pointing to an external
resource so it appears in CATALOG.csv and INDEX.md for AI discovery.

Usage:
    python scripts/add_link.py [URL]
    python scripts/add_link.py --non-interactive --url URL --title TITLE --org ORG --type TYPE
"""

import argparse
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

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

STUB_TEMPLATE = """\
---
title: "{title}"
organization: "{organization}"
content_type: {content_type}
year: {year}
tags: [{tags}]
source_url: "{source_url}"
description: "{description}"
format: link
date_ingested: {date_ingested}
---

# {title}

**Organization:** {organization}
**Source:** [{source_url}]({source_url})

{description}
"""


# ---------------------------------------------------------------------------
# Metadata fetchers
# ---------------------------------------------------------------------------

def fetch_github_meta(url):
    """Try to get repo metadata via gh CLI. Returns dict or None."""
    match = re.search(r"github\.com/([^/]+/[^/?#]+)", url)
    if not match:
        return None
    repo_path = match.group(1).rstrip(".git")
    try:
        result = subprocess.run(
            ["gh", "repo", "view", repo_path,
             "--json", "name,description,repositoryTopics,homepageUrl"],
            capture_output=True, text=True, timeout=15
        )
        if result.returncode == 0:
            data = json.loads(result.stdout)
            topics = [t["topic"]["name"] for t in data.get("repositoryTopics", [])]
            return {
                "title": data.get("name", repo_path.split("/")[-1]),
                "topics": topics,
                "description": data.get("description") or "",
            }
    except Exception:
        pass
    return None


def try_jina(url):
    """Fetch URL via Jina AI Reader and extract title + first paragraph."""
    try:
        import requests
        resp = requests.get(f"https://r.jina.ai/{url}", timeout=20)
        if resp.ok:
            lines = [l.strip() for l in resp.text.splitlines() if l.strip()]
            title = lines[0].lstrip("# ") if lines else ""
            desc = ""
            for line in lines[1:8]:
                if len(line) > 40 and not line.startswith("#"):
                    desc = line[:200]
                    break
            return title, desc
    except Exception:
        pass
    return "", ""


def slugify(text):
    """Convert title to safe filename slug."""
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", text)
    return slug[:60].strip("_")


def prompt(label, default=""):
    suffix = f" [{default}]" if default else ""
    val = input(f"{label}{suffix}: ").strip()
    return val if val else default


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    p = argparse.ArgumentParser(description="Add external reference stub to tsudo/reference")
    p.add_argument("url", nargs="?", help="URL to reference")
    p.add_argument("--url", dest="url_flag", help="URL (alternative to positional)")
    p.add_argument("--non-interactive", action="store_true")
    p.add_argument("--title")
    p.add_argument("--org")
    p.add_argument("--type", dest="content_type", choices=CONTENT_TYPE_CHOICES)
    p.add_argument("--year", default="ongoing")
    p.add_argument("--tags", nargs="+")
    p.add_argument("--description", dest="desc")
    p.add_argument("--no-push", action="store_true")
    args = p.parse_args()

    url = args.url or args.url_flag
    if not url:
        p.print_help()
        sys.exit(1)

    # Auto-fetch metadata
    gh_meta = None
    jina_title, jina_desc = "", ""

    if "github.com" in url:
        print("[add-link] Fetching GitHub repo metadata...")
        gh_meta = fetch_github_meta(url)
        if gh_meta:
            print(f"  Found: {gh_meta['title']}")
        else:
            print("  gh CLI unavailable or not authenticated -- skipping")

    if not gh_meta:
        print("[add-link] Fetching page metadata via Jina...")
        jina_title, jina_desc = try_jina(url)

    default_title = (gh_meta["title"] if gh_meta else jina_title) or url.rstrip("/").split("/")[-1]
    default_desc  = (gh_meta["description"] if gh_meta else jina_desc) or ""
    default_tags  = gh_meta["topics"] if gh_meta else []

    if args.non_interactive:
        meta = {
            "title":        args.title or default_title,
            "organization": args.org or "Unknown",
            "content_type": args.content_type or "misc",
            "year":         args.year,
            "tags":         args.tags or default_tags,
            "description":  args.desc or default_desc,
        }
    else:
        print()
        meta = {
            "title":        prompt("Title", default_title),
            "organization": prompt("Organization"),
            "year":         prompt("Year", args.year),
            "description":  prompt("Description (1-2 sentences)", default_desc[:120]),
        }
        print(f"Content types: {', '.join(CONTENT_TYPE_CHOICES)}")
        ct = prompt("Content type", "misc")
        while ct not in CONTENT_TYPE_CHOICES:
            print(f"  Must be one of: {', '.join(CONTENT_TYPE_CHOICES)}")
            ct = prompt("Content type", "misc")
        meta["content_type"] = ct
        tags_raw = prompt("Tags (space-separated)", " ".join(default_tags))
        meta["tags"] = tags_raw.split() if tags_raw else []

    # Build stub
    tags_yaml = ", ".join(f'"{t}"' for t in meta["tags"])
    content = STUB_TEMPLATE.format(
        title=meta["title"],
        organization=meta["organization"],
        content_type=meta["content_type"],
        year=meta["year"],
        tags=tags_yaml,
        source_url=url,
        description=meta["description"],
        date_ingested=date.today().isoformat(),
    )

    bucket = BUCKET_MAP.get(meta["content_type"], "z_misc")
    dest_dir = REPO_ROOT / bucket
    dest_dir.mkdir(exist_ok=True)
    fname = slugify(meta["title"]) + ".md"
    dest = dest_dir / fname
    dest.write_text(content, encoding="utf-8")
    print(f"[add-link] Created: {bucket}/{fname}")

    # Regen catalog
    r = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "catalog.py"),
         "--repo-root", str(REPO_ROOT)],
        capture_output=True, text=True
    )
    print(r.stdout.strip())

    # Git commit + push
    msg = f"link: add external reference -- {meta['title']}"
    subprocess.run(["git", "-C", str(REPO_ROOT), "add", "."], check=True)
    subprocess.run(["git", "-C", str(REPO_ROOT), "commit", "-m", msg], check=True)
    if not args.no_push:
        ans = input("Push to remote? [Y/n]: ").strip().lower()
        if ans != "n":
            subprocess.run(["git", "-C", str(REPO_ROOT), "push"], check=True)
            print("[add-link] Pushed.")


if __name__ == "__main__":
    main()
