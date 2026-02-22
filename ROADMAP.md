# Reference Library Roadmap

## In Progress

### Phase A — Batch Ingestion
Ingest local PDF/XLSX collection using `batch_ingest.py`.
```bash
python scripts/batch_ingest.py --batch-dir /path/to/folder --dry-run
python scripts/batch_ingest.py --manifest my_batch.csv
```

---

## Up Next

### markitdown MCP Server
Install the markitdown MCP so Claude can convert and read document content
inline during `/ingest` sessions — enables auto-suggested metadata from actual
document content rather than filename heuristics.

```bash
claude mcp add markitdown-mcp -- uvx markitdown-mcp
```

After install: update `.claude/skills/ingest/SKILL.md` to use the MCP tool
first (convert + read inline), falling back to `convert.py` if unavailable.

---

## Backlog

### Phase C — Review & Convert
- Review `z_misc/` for items worth reclassifying
- Batch convert remaining PDFs to Markdown for AI readability
- Flag any entries in CATALOG.csv with `organization=Unknown` or `year=unknown`

### Phase D — Update Key Reports
Run `update_routine.py` to identify stale entries, then ingest newer versions:
- Verizon DBIR (annual, usually April-May)
- IBM/Ponemon Cost of Data Breach (annual)
- CrowdStrike Global Threat Report (annual)
- Cisco Talos / Proofpoint annual reports

### Phase E — Stats Page
Generate a `STATS.md` with collection summary: doc counts by type/org/year,
coverage gaps, top tags. Claude-extracted from converted MDs + CATALOG.csv.

---

## Completed

- [x] **Phase 0** — Restructured repo into content-type bucket folders
- [x] **Phase 1** — Scripts: `convert.py`, `catalog.py`, `ingest.py`, `sources.yaml`
- [x] **Phase 2** — Claude Code skills: `/ingest`, `/add-link`, `/batch-ingest`
- [x] **Phase 3** — Generated `CATALOG.csv` and `INDEX.md` (113 records)
- [x] **Phase B** — 33 external reference stubs (NIST, MITRE, CIS, cloud providers, policy-as-code, SBOM, SCRM)
- [x] **XLSX/ZIP converter** — Full multi-sheet support, per-sheet CSVs, ZIP extraction
