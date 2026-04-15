## breach-reports

Annual breach and incident cost reports from industry analysts and named-incident postmortems. Primary sources: Verizon DBIR (every year since 2015), Ponemon/IBM Cost of a Data Breach Report, and incident-specific records (Anthem, Equifax).

## Contents

| Group | Organizations / series |
| --- | --- |
| Annual industry reports | Verizon DBIR 2015–present, Ponemon/IBM Cost of a Data Breach 2018–2023 |
| Named-incident records | Anthem (2016), Equifax (GAO 2018, Senate 2019, SEC filing) |
| Resilience / posture surveys | Ponemon Cyber Resilient Organization, State of SMB Cybersecurity, State of Endpoint Security |

## Discovery

Filter [CATALOG.csv](../CATALOG.csv) by `content_type=breach-report`. Organizations covered: `Verizon`, `IBM`, `Ponemon`, `Anthem`, `Equifax`, `GAO`.

```bash
awk -F',' '$4=="breach-report"' ../CATALOG.csv
```

## Notes

- All documents are derivative Markdown conversions — verify against original PDFs (source_url in frontmatter) for anything relied on operationally.
- Multi-year series are useful for trend analysis; DBIR methodology changes are documented in each year's introduction.
