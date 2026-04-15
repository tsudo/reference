## research

Academic, industry research, and methodology-grade content — things that explain *how to think*, not *what to do*.

## Contents

| Group | Items |
| --- | --- |
| Risk quantification | FAIR-CAM (FAIR Controls Analytics Model) introduction, Minimum Viable Information Risk Management Program |
| WEF Global Risks | 2019, 2021, 2024 reports; Cybersecurity Outlook |
| Threat landscape | ENISA Threat Landscape, ransomware history |
| Academic | WEIS 2019 paper |
| Illustrative / examples | AICPA cybersecurity risk management illustrative report, "Do No Harm" 2.0 (healthcare) |
| Vendor research | Wiz Security Research |

## Discovery

Filter [CATALOG.csv](../CATALOG.csv) by `content_type=research`.

```bash
awk -F',' '$4=="research"' ../CATALOG.csv
```

## Notes

- **FAIR / FAIR-CAM coverage is currently thin** — a recognized gap. Flagged for expansion as part of the Security-GRC Skill Pack "pro mode" prerequisite work.
- WEF reports are cross-domain (geopolitical, environmental, technological) — filter for cyber-relevant sections; not every page is on topic.
