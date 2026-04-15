## frameworks

Control frameworks, cross-framework mappings, and cloud-platform control catalogs. The largest bucket in the library.

## Contents

| Group | Items |
| --- | --- |
| CIS Controls | Versions 7, 7.1, 8 — full text, CSV catalogs, implementation-group mappings, cloud companion guide |
| NIST CSF | 2.0 Implementation Examples (CSV + MD) |
| AICPA | SOC for Cybersecurity brochure, Description Criteria |
| Cloud | AWS CIS Foundations Benchmark, C5 (German cloud compliance catalogue) |
| Cross-framework mappings | HIPAA master mapping, CSF↔SP 800-171 mapping (see also `standards/`) |

## Discovery

Filter [CATALOG.csv](../CATALOG.csv) by `content_type=framework`. CSV catalogs (`.csv` files here) are machine-readable control tables — parse directly for programmatic cross-mapping.

```bash
awk -F',' '$4=="framework"' ../CATALOG.csv
```

## Notes

- **Licensed content excluded:** ISO 27001/27002/27018/27701/22301, HITRUST CSF, and full PCI DSS v4.0.1 text are not in this library (license restrictions). Control catalog summaries and mappings referencing these frameworks may appear in `research/` or `standards/` where fair-use applies.
- CSV files are the primary machine-readable surface here — prefer them over the Markdown equivalents for automated control lookup.
