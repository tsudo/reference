---
title: "SOC System Type Diagram"
organization: "AICPA"
content_type: tool-template
year: 2018
tags: ["soc2;system-diagram;operations"]
source_url: ""
license: "© AICPA. Reproduced for research and educational purposes per 17 U.S.C. § 107 (fair use)."
date_ingested: 2026-02-22
original_format: pdf
---

Boards

Types

SubTypes

Incident

Any unplanned
interruption.
(Problem)

Hardware
(HW)

Software
(SW)

Network
(NET)

Security
(SEC)

Change

Installs, modifications,
additions, changes,
removals

Event

Warning or Failure
notification from RMM,
threshold crossed

Broad to Narrow

Hardware

Software

Server OS
Server App
Desktop OS
Microsoft Office
Desktop App
Misc

Network

Switching
Routing
Wireless
WAN
LAN
VPN
Misc

Server
Desktop
Laptop
Appliance
Printer
Peripheral
Misc

Security

AntiVIrus
AntiMalware
Web Filter
Spam Filter
GW Security
IDS/IPS
Restricted Access
Misc

??

??

Alert

Is it CRITICAL?

NO

T1

YES

Oncall and Dispatch
Communicate to
determine BEST
resource

T2

Oncall

T1

T2

RESOLVED

Change INScope

Can the work be
done remotely?

No

Is it less than 4hrs?

Yes

Yes

No

T2

T1 or T2

HandOff to Project
Team

RESOLVED

Change INScope

Can the work be
done remotely?

No

Is it less than 4hrs?

Yes

Yes

No

T2

T1 or T2

HandOff to Project
Team

RESOLVED

Change OUTScope

HandOff to Sales
Team

Scoping
Design
Work Order if
needed

