# Cybersecurity Reference Library

A curated collection of cybersecurity threat intelligence reports, breach analyses, government advisories, frameworks, standards, and templates, organized for human browsing and machine consumption.

**[CATALOG.csv](CATALOG.csv)** — machine-readable index of documents
**[INDEX.md](INDEX.md)** — human-readable index by content type and organization

---

## Machine-Readable Access

Agents and downstream tooling should start here.

| Artifact | Purpose |
| --- | --- |
| [CATALOG.csv](CATALOG.csv) | Primary discovery surface. One row per document. Columns: `filename, folder, organization, content_type, title, year, tags, source_url, format, md_available, date_ingested, doc_path`. `format=LINK` entries are external-reference stubs — follow `source_url`. `format=MD/PDF/XLSX` entries are stored in-repo at `doc_path`. |
| [INDEX.md](INDEX.md) | Human-oriented grouping of the same content by content_type and organization. Useful for browsing; not the canonical parse target. |
| [scripts/sources.yaml](scripts/sources.yaml) | Upstream source registry — maps logical source names to live URLs and update frequency. Consume this to know where canonical versions live. |

**Consumption pattern for agents:** filter CATALOG.csv by `content_type` and/or `tags`, resolve `doc_path` for local files or `source_url` for LINK entries, cross-reference `scripts/sources.yaml` for freshness.

**Bucket taxonomy (content_type values):** `breach-report`, `threat-intel`, `government`, `research`, `framework`, `standard`, `tool-template`, `misc`.

---

## Collection Structure

| Folder | Contents |
| --- | --- |
| [breach-reports/](breach-reports/) | DBIR, Ponemon/IBM Cost of Breach, named-incident records |
| [threat-intel/](threat-intel/) | Annual and quarterly vendor threat reports |
| [government/](government/) | CISA advisories, ATA/WWTA reports, FFIEC, HHS/HIPAA |
| [research/](research/) | FAIR-CAM, WEF Global Risks, academic and methodology content |
| [frameworks/](frameworks/) | CIS Controls, NIST CSF, SOC/VSA mappings, cloud benchmarks |
| [standards/](standards/) | NIST SPs (53r5, 37, 39, 171), OSCAL, SBOM specs, Privacy Framework |
| [tools-templates/](tools-templates/) | Assessment tools, playbooks, IaC scanners, policy scaffolds |
| [z_Misc/](z_Misc/) | Overflow and uncategorized references |

Each bucket has a `README.md` explaining its scope, contents, and how to filter CATALOG.csv.

---

## Automated Conversion and AI Notice

Documents in this repository may have been converted, transformed, classified, or summarized using automated tooling and AI-assisted workflows (for example OCR, format conversion, spreadsheet extraction, and markdown generation).

Conversion artifacts can contain extraction errors, omissions, formatting defects, or misinterpretations. Converted files are provided as convenience derivatives only.

**Verification responsibility is on downstream users.** Anyone using this repository must independently validate content against the original authoritative source before relying on it for legal, regulatory, security, operational, or business decisions.

The maintainer does not accept responsibility for decisions made from unverified converted content.

---

## Attribution and License

I claim no ownership or copyright over third-party reports in this collection. Each organization retains rights to its materials.

Per-document attribution is recorded in file metadata where available and in `CATALOG.csv`.

### Fair Use Statement

This repository may contain copyrighted material reproduced without explicit authorization from the copyright owner for research and educational purposes, consistent with fair use principles under **17 U.S.C. § 107**.

This repository is non-commercial. If you are a copyright holder and believe material has been used beyond fair use, open an issue.

### General Liability Disclaimer

This collection is for reference and educational purposes only. No representation is made regarding completeness, accuracy, fitness, or currency. Use at your own risk.

---

*Last updated: 2026-02-23*
