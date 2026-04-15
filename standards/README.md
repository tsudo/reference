## standards

NIST Special Publications, software bill of materials (SBOM) specs, and the NIST Privacy Framework.

## Contents

| Group | Items |
| --- | --- |
| NIST SP 800-series | SP 800-53r5 (full + controls CSV), SP 800-37r2 (RMF), SP 800-39 (managing InfoSec risk), SP 800-66r1 (HIPAA Security Rule), SP 800-115 (assessment tech), SP 800-171r2 + 171A + assessment methodology |
| NIST sector guides | SP 1800-5 (IT asset management), macOS Security |
| OSCAL | NIST OSCAL content reference |
| SBOM | CycloneDX Specification, SPDX Specification |
| Privacy | NIST Privacy Framework informative references (preliminary draft) |
| CSF cross-mapping | NIST CSF → SP 800-171 mapping (CSV + MD) |

## Discovery

Filter [CATALOG.csv](../CATALOG.csv) by `content_type=standard`. The `_controls.csv` files are the primary machine-readable control catalogs.

```bash
awk -F',' '$4=="standard"' ../CATALOG.csv
```

## Notes

- **SP 800-53r5** appears under two filenames (`NIST.SP.800_53r5.md` and `NIST_SP800_53r5.md`) — same content, ingestion artifact. Use the `_controls.csv` for programmatic lookup; treat the MD files as readable reference.
- **ISO 27001/27002 equivalents are not here** — licensed content, see top-level README § Hard Stops.
