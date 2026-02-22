# /batch-ingest — Batch Ingest Local Files into tsudo/reference

## Trigger

`/batch-ingest` or mention "batch ingest", "add multiple files", "bulk add"

---

## Two Modes

### Mode 1 — Manifest (recommended for 10+ files or when you know the metadata)

Fill in `batch_manifest.csv` then run:
```bash
python scripts/batch_ingest.py --manifest path/to/batch_manifest.csv
```

**Get the template:**
```bash
cp scripts/batch_manifest_template.csv ~/Desktop/my_batch.csv
# Edit in Excel or a text editor
```

**Manifest format:**
```csv
file_path,title,organization,content_type,year,tags,source_url
/path/to/CrowdStrike_GTR_2025.pdf,2025 Global Threat Report,CrowdStrike,threat-intel,2025,"crowdstrike annual",https://...
/path/to/NIST_SP800-207.pdf,,NIST,standard,2020,,
```

- `file_path` and `content_type` are required
- Everything else auto-guessed from filename if left blank
- Comment rows start with `#`

---

### Mode 2 — Directory scan (for unorganized folders)

```bash
python scripts/batch_ingest.py --batch-dir /path/to/folder/of/pdfs
```

**What happens:**
1. Scans the directory recursively for all PDFs and XLSX files
2. Auto-classifies each file using filename heuristics (org, type, year)
3. Groups files by (organization, content_type)
4. Presents groups for confirmation — you can: **[C]onfirm**, **[R]eclassify**, **[S]kip**, or **[E]dit individually**
5. Converts each confirmed file to Markdown
6. Places in correct bucket folder
7. Regenerates CATALOG.csv and INDEX.md
8. Commits + optional push

---

## Dry Run (preview without writing)

Always safe to run first:
```bash
python scripts/batch_ingest.py --batch-dir /path/to/folder --dry-run
python scripts/batch_ingest.py --manifest my_batch.csv --dry-run
```

---

## Skip Conversion (PDFs only, no Markdown)

If markitdown isn't installed or you just want to add the PDFs:
```bash
python scripts/batch_ingest.py --manifest my_batch.csv --no-convert
```
Files get placed in the correct buckets and cataloged, but no .md conversion.
Run a conversion pass later when ready.

---

## Common Workflows

### "I have a Downloads folder with 30 PDFs I want to add"
```bash
python scripts/batch_ingest.py --batch-dir ~/Downloads/security-reports --dry-run
# Review the output, then:
python scripts/batch_ingest.py --batch-dir ~/Downloads/security-reports
```

### "I organized them already and filled in a spreadsheet"
```bash
python scripts/batch_ingest.py --manifest ~/Desktop/my_batch.csv
```

### "I want to add them without pushing yet"
```bash
python scripts/batch_ingest.py --batch-dir /path/to/folder --no-push
# Review results, then push manually:
git -C /path/to/reference push
```

---

## Auto-Classification Rules

When no manifest is provided, files are classified by filename patterns:

| Pattern in filename | Guessed type |
|--------------------|-------------|
| dbir, breach, ponemon, ibm_cost | `breach-report` |
| cisa, nist, dhs, fbi, wwta, ata-20 | `government` |
| wef, global_risk, enisa | `research` |
| framework, csf, cis_control, cmmc | `framework` |
| sp_800, sp800, fips | `standard` |
| checklist, playbook, template | `tool-template` |
| everything else | `threat-intel` |

Organizations auto-detected: Verizon, Proofpoint, Cisco, CrowdStrike, Mandiant, Symantec, Accenture, CISA, NIST, WEF, ENISA, Microsoft, Palo Alto/Unit42, SANS, and more.

Review the group confirmation step to catch any misclassifications before they're written.

---

## After Batch Ingest

1. Check `CATALOG.csv` — scan for any `organization=Unknown` or `year=unknown` entries worth fixing
2. For important docs, add proper frontmatter by running `/ingest` on them individually to get the full interactive experience
3. For key reports worth converting to MD, run: `python scripts/convert.py --file path/to/file.pdf`
