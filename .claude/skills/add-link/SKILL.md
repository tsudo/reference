# /add-link — Add an External Reference to tsudo/reference

## Trigger

`/add-link [URL]`

Examples:
- `/add-link https://github.com/usnistgov/OSCAL`
- `/add-link https://attack.mitre.org/`
- `/add-link https://www.cisa.gov/known-exploited-vulnerabilities-catalog`

---

## What This Does

Creates a lightweight reference stub — a `.md` file with YAML frontmatter pointing
to an external resource — so it appears in `CATALOG.csv` and `INDEX.md`.

**Use this instead of `/ingest` when:**
- You want to index a resource without storing it locally
- The source is live/updated frequently (CISA advisories, NVD, ATT&CK)
- The resource is a GitHub repo or documentation site
- You want AI tools to discover the resource from your reference library

The stub file is small (~10 lines of frontmatter + brief description). Future Claude
sessions reading `CATALOG.csv` will find it and know to look at the external URL.

---

## Procedure

### Step 1 — Run add_link.py

**Interactive (recommended):**
```bash
python scripts/add_link.py "https://github.com/usnistgov/OSCAL"
```

**Non-interactive (for scripted use):**
```bash
python scripts/add_link.py \
  --non-interactive \
  --url "https://github.com/usnistgov/OSCAL" \
  --title "NIST OSCAL" \
  --org "NIST" \
  --type framework \
  --year ongoing \
  --tags oscal nist controls compliance \
  --description "XML/JSON/YAML schemas for security control documentation."
```

### Step 2 — GitHub repos: automatic metadata

For GitHub URLs, `add_link.py` automatically calls:
```bash
gh repo view usnistgov/OSCAL --json name,description,repositoryTopics
```
This pre-populates the title, description, and tags from the repo's own metadata.
Review and edit during the interactive prompts.

### Step 3 — Verify

After the script completes:
- [ ] Stub `.md` file exists in the correct bucket folder
- [ ] `CATALOG.csv` shows a new entry with `format=LINK`
- [ ] `INDEX.md` → External Resources section shows the new entry with a clickable link

---

## Stub Format

Every stub gets this YAML frontmatter:

```yaml
---
title: "NIST OSCAL (Open Security Controls Assessment Language)"
organization: "NIST"
content_type: framework
year: ongoing
tags: ["oscal", "nist", "automation", "controls", "compliance"]
source_url: "https://github.com/usnistgov/OSCAL"
description: "XML/JSON/YAML schemas for representing security controls..."
format: link
date_ingested: 2026-02-22
---
```

---

## Content Type → Folder Mapping

| Content Type | Folder |
|-------------|--------|
| `framework` | `frameworks/` |
| `standard` | `standards/` |
| `government` | `government/` |
| `threat-intel` | `threat-intel/` |
| `research` | `research/` |
| `tool-template` | `tools-templates/` |
| `breach-report` | `breach-reports/` |
| `misc` | `z_misc/` |

---

## How AI Tools Discover These

When a Claude session reads `CATALOG.csv`, it sees entries like:

```
NIST_OSCAL.md,frameworks,NIST,framework,...,https://github.com/usnistgov/OSCAL,...,LINK,link,...
```

The `format=LINK` and `source_url` make it clear: this is an external resource at that URL.
`INDEX.md` renders it as a clickable link in the External Resources section.

---

## Adding Multiple Links in Bulk

To add several external sources at once without interaction:

```bash
python scripts/add_link.py --non-interactive --url URL1 --title "..." --org "..." --type framework --no-push
python scripts/add_link.py --non-interactive --url URL2 --title "..." --org "..." --type government --no-push
python scripts/catalog.py --repo-root .
git add . && git commit -m "link: add batch external references" && git push
```
