# /ingest — Ingest a Document into tsudo/reference

## Trigger

`/ingest [URL or local path]`

Examples:
- `/ingest https://www.verizon.com/business/resources/reports/dbir/2025-dbir.pdf`
- `/ingest ~/Downloads/CISA-Advisory-AA25-001.pdf`
- `/ingest https://www.cisa.gov/sites/default/files/2025-01/advisory.pdf`

---

## What This Does

Ingests a cybersecurity reference document into the `tsudo/reference` collection:

1. **Fetch** — If URL, attempt Jina AI Reader first (token-optimal for web docs); fall back to direct download for PDFs
2. **Convert** — Use `markitdown` to convert PDF → Markdown; add YAML frontmatter
3. **Classify** — Prompt for metadata (org, content type, year, tags, source URL)
4. **Place** — Write to the correct bucket folder (`breach-reports/`, `government/`, etc.)
5. **Catalog** — Regenerate `CATALOG.csv` and `INDEX.md`
6. **Commit** — `git add .` + `git commit` + optional `git push`

---

## Procedure

### Step 1 — Check prerequisites

```bash
python -c "import markitdown; print('markitdown OK')"
python -c "import yaml; print('pyyaml OK')"
python -c "import requests; print('requests OK')"
# If any fail:
pip install -r scripts/requirements.txt
```

### Step 2 — Run ingest

**Interactive (recommended for one-off ingests):**
```bash
python scripts/ingest.py "<URL or path>"
```

**Non-interactive (for scripted/batch use):**
```bash
python scripts/ingest.py \
  --file path/to/document.pdf \
  --org "Verizon" \
  --type breach-report \
  --year 2025 \
  --title "2025 Data Breach Investigations Report" \
  --url "https://www.verizon.com/business/resources/reports/dbir/" \
  --tags dbir breach verizon
```

### Step 3 — Verify

After ingest completes, confirm:
- [ ] Converted `.md` file exists in correct bucket folder with YAML frontmatter
- [ ] `CATALOG.csv` has a new entry for this document
- [ ] `INDEX.md` shows the document under the correct content type section
- [ ] Git shows clean working tree (if push was confirmed)

---

## Content Type → Folder Mapping

| Content Type | Folder |
|-------------|--------|
| `threat-intel` | `threat-intel/` |
| `breach-report` | `breach-reports/` |
| `government` | `government/` |
| `research` | `research/` |
| `framework` | `frameworks/` |
| `standard` | `standards/` |
| `tool-template` | `tools-templates/` |
| `misc` | `z_misc/` |

---

## Token-Optimal Fetching Strategy

| Document type | Approach |
|--------------|----------|
| Public web page / HTML report | Jina AI Reader: `curl https://r.jina.ai/{url}` |
| PDF (public URL) | Download with `requests`, convert with `markitdown` |
| PDF (local file) | Pass local path directly to `ingest.py` |
| XLSX/spreadsheet | `markitdown` + pandas CSV export |

Jina Reader is preferred for HTML-based reports — it returns clean markdown without requiring a local download or PDF conversion.

---

## YAML Frontmatter Schema

Every ingested document gets frontmatter like:

```yaml
---
title: "2025 Data Breach Investigations Report"
organization: "Verizon"
content_type: breach-report
year: 2025
tags: ["dbir", "breach", "verizon", "annual"]
source_url: "https://www.verizon.com/business/resources/reports/dbir/"
license: "© Verizon Business. Reproduced for research and educational purposes per 17 U.S.C. § 107 (fair use)."
date_ingested: 2025-06-01
original_format: pdf
---
```

---

## Semiannual Update Check

Run before ingesting a batch to see what's potentially outdated:

```bash
python scripts/update_routine.py
```

This reads `scripts/sources.yaml` and reports stale or missing entries relative to the current year.

---

## Troubleshooting

**`markitdown` fails on a PDF:**
Some PDFs are image-only scans. markitdown will return minimal text. Acceptable — frontmatter + whatever text was extracted is still useful metadata.

**Jina returns 403 or short response:**
Document is behind auth/paywall. Download manually, then ingest with local path.

**Git push fails:**
Check `gh auth status`. Re-authenticate with `gh auth login` if needed.

**Duplicate detected:**
Check `CATALOG.csv` — if a similar entry exists, ingest skips or overwrites. Run `python scripts/catalog.py` to resync if needed.
