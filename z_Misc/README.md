## z_Misc

Overflow bucket — items that don't cleanly fit the other buckets or are awaiting reclassification. Named `z_Misc` to sort last in directory listings.

## Contents

| Group | Items |
| --- | --- |
| SMB-focused reports | BBB State of Cybersecurity SMB, Switchfast SMB Cybersecurity Report, NCSA SMB Toolkit |
| Single-vendor / one-offs | Checkpoint Cyber Security Report, NTT Security GTIR Key Findings, Malwarebytes Healthcare |
| Government one-offs | FBI Flash APT10 (TLP:WHITE), US Fed Worldwide Threat Assessment, UK DCMS Cybersecurity Breaches Survey |
| Niche / educational | CSIS Significant Cyber Events List, Damage Control Cyber Insurance ebook, Pedagogic Cybersecurity Framework, Phishing Tournament Benchmark |
| `stats.md` | Repo-level statistics |

## Discovery

Filter [CATALOG.csv](../CATALOG.csv) by `content_type=misc`.

```bash
awk -F',' '$4=="misc"' ../CATALOG.csv
```

## Notes

- **Reclassification is welcome** — items in this bucket may belong under `threat-intel/`, `government/`, or `research/` but haven't been moved yet. Open an issue or PR with a content_type suggestion.
- Items here are lower-priority for verification and update cadence than the primary buckets.
