## government

US government and regulator publications — advisories, threat assessments, sector-specific guidance, and compliance source material.

## Contents

| Group | Items |
| --- | --- |
| CISA | KEV catalog (machine-readable feed), advisories, MS-ISAC ransomware guide, fact sheets |
| Intelligence community | Annual Threat Assessment (ATA) 2018–2023, Worldwide Threat Assessment |
| Financial sector | FFIEC CAT (Cybersecurity Assessment Tool) — inherent risk profile, maturity, NIST CSF mapping, glossary |
| Healthcare | HHS/HIPAA guidance, 42 CFR Part 2 consent |
| Cloud / FedRAMP | Authorization boundary guidance, CSP-A templates |
| Specific threat advisories | China APT (MSP targeting), OT ransomware, sector alerts |

## Discovery

Filter [CATALOG.csv](../CATALOG.csv) by `content_type=government`. Organizations: `CISA`, `FFIEC`, `HHS`, `FBI`, `DHS`, `GAO`, `DoD`.

```bash
awk -F',' '$4=="government"' ../CATALOG.csv
```

## Notes

- **CISA KEV** (`CISA_KEV.md`) tracks known-exploited vulnerabilities — the authoritative upstream is the CSV feed linked in the document's frontmatter; treat the local copy as a point-in-time snapshot.
- ATA reports (Worldwide Threat / Annual Threat Assessment) are released yearly; check the public repo for the most recent year.
