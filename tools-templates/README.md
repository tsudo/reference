## tools-templates

Operational artifacts — checklists, playbooks, assessment tools, policy scaffolds, IaC scanners, and control self-assessment spreadsheets.

## Contents

| Group | Items |
| --- | --- |
| CIS assessment tools | CIS-CAT Pro Assessor, CIS-CAT Centralized Reporting, AuditScripts Critical Security Control assessment tools (executive, manual, mappings) |
| Active Directory | AD Design Recommendations, AD Design Guide |
| AWS | AWS Security Samples, AWS Security Services Best Practices |
| Cloud / IaC | Checkov IaC Scanner, Cloud Custodian, Cloudflare Docs + Terraform Provider, Azure Policy Definitions |
| Playbooks | CRI Ransomware Playbook, CISO Mindmap (SANS) |
| Financial sector | Financial Services Sector Cybersecurity Profile (assessment + user guide + mappings) |

## Discovery

Filter [CATALOG.csv](../CATALOG.csv) by `content_type=tool-template`.

```bash
awk -F',' '$4=="tool-template"' ../CATALOG.csv
```

## Notes

- Many items here are **link stubs** (`format=LINK` in CATALOG.csv) pointing to upstream tool docs — follow `source_url` for the canonical version.
- AuditScripts CSVs are directly parseable control assessment tables — useful for automated gap analysis.
