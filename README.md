# Cybersecurity Reference Library

A curated collection of cybersecurity threat intelligence reports, breach analyses, government advisories, and frameworks. Organized for both human browsing and machine consumption via a structured catalog.

**[CATALOG.csv](CATALOG.csv)** — machine-readable index of all documents
**[INDEX.md](INDEX.md)** — human-readable index by content type and organization

---

## Collection Structure

| Folder | Contents |
|--------|----------|
| `breach-reports/` | DBIR, Ponemon/IBM Cost of Breach, incident summaries |
| `threat-intel/` | Annual threat reports, vendor intelligence (Cisco, Proofpoint, Symantec, etc.) |
| `government/` | CISA advisories, US Annual Threat Assessments (ATA/WWTA), regulatory guidance |
| `research/` | WEF Global Risks Report, academic and think-tank research |
| `frameworks/` | NIST CSF, CIS Controls, CMMC |
| `standards/` | NIST SPs, FIPS, ISO standards |
| `tools-templates/` | Checklists, cheatsheets, playbooks, password guidance |
| `z_misc/` | Overflow and uncategorized |
| `scripts/` | Ingestion tooling (convert, catalog, ingest, update) |

Multi-topic documents live in their primary bucket and are tagged for cross-referencing in `INDEX.md`.

---

## Organizations Represented

Verizon · IBM/Ponemon · Proofpoint · Cisco · Accenture · Symantec · Coveware · SecurityScorecard · Webroot · CISA · US Intelligence Community · World Economic Forum · US Government

---

## Ingesting New Documents

This repo uses an ingest pipeline powered by [markitdown](https://github.com/microsoft/markitdown) and a Claude Code `/ingest` skill.

**Quick start:**
```bash
pip install -r scripts/requirements.txt

# Ingest from URL
python scripts/ingest.py "https://example.com/report.pdf"

# Ingest local file
python scripts/ingest.py path/to/report.pdf
```

From a Claude Code session:
```
/ingest https://example.com/report.pdf
```

See [`.claude/skills/ingest/SKILL.md`](.claude/skills/ingest/SKILL.md) for full documentation.

### Semiannual Update Check

```bash
python scripts/update_routine.py
```

Reports which sources in `scripts/sources.yaml` have potentially newer editions available.

---

## Attribution & License

I claim no ownership or copyright over any reports in this collection. Each organization retains all rights to their respective materials.

**Per-document attribution** is recorded in YAML frontmatter within each converted `.md` file and in `CATALOG.csv`. Original source URLs are linked in `CATALOG.csv` and `INDEX.md`.

### Fair Use Statement

The content in this repository may contain copyrighted material reproduced without explicit authorization from the copyright owner. This material is made available for research and educational purposes, consistent with the principles of fair use under **17 U.S.C. § 107**.

This repository is non-commercial. No profit is derived from hosting or distributing these materials. If you are a copyright holder and believe your material has been used beyond fair use, please open an issue.

### Disclaimer of Liability

This collection is for general reference and educational purposes only. Do not rely on this material as the basis for business, legal, or security decisions without consulting primary sources and qualified professionals. No representations are made regarding completeness, accuracy, or currency of the information. Any reliance is at your own risk.

---

*Last updated: 2026-02-21 | Collection restructured with ingest pipeline*
