## threat-intel

Vendor threat reports — annual and quarterly — from security product companies and managed-service providers.

## Contents

| Group | Items |
| --- | --- |
| Annual threat reports | Symantec ISTR (2015–2018), CrowdStrike Global Threat Report, Mandiant M-Trends, Cisco Annual Cybersecurity Report |
| Quarterly / periodic | Proofpoint Quarterly Threat Report, Proofpoint Human Factor, Coveware Ransomware Report (quarterly) |
| Industry / sector | Accenture Cyber Threatscape + Cybersecurity Conundrum, SSC Healthcare Report |
| Webroot, others | Webroot Threat Report 2019, additional vendor reports |

## Discovery

Filter [CATALOG.csv](../CATALOG.csv) by `content_type=threat-intel`. Organizations: `Symantec`, `Verizon`, `Proofpoint`, `CrowdStrike`, `Mandiant`, `Accenture`, `Cisco`, `Coveware`, `SSC`, `Webroot`.

```bash
awk -F',' '$4=="threat-intel"' ../CATALOG.csv
```

## Notes

- **Vendor perspective bias applies** — each report reflects telemetry from that vendor's customer base. Cross-reference with `breach-reports/` (Verizon DBIR is the closest to cross-industry) and `government/` (CISA, ATA) for triangulation.
- Recent-year reports (2023+) are thinner than historical coverage — many vendors moved reports behind landing pages that block direct ingest; see project README § Outstanding work.
