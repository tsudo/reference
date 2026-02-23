# Chinese-Cyber-Activity-Targeting-Managed-Service-Providers

Original format: `pdf`

C I S A   |   C Y B E R S E C U R I T Y   A N D   I N F R A S T R U C T U R E   S E C U R I T Y   A G E N C Y

TLP:WHITE

AWARENESS BRIEFING:
CHINESE CYBER ACTIVITY
TARGETING MANAGED
SERVICE PROVIDERS

1

TLP:WHITE

Disclaimer

This report is provided “as is” for informational purposes only. The Department
of Homeland Security (DHS) does not provide any warranties of any kind
regarding any information contained within. The DHS does not endorse any
commercial product or service, referenced in this bulletin or otherwise. This
document is marked TLP:WHITE. Subject to standard copyright rules.
TLP:WHITE information may be distributed without restriction. Sources may
use TLP:WHITE when information carries minimal or no foreseeable risk of
misuse, in accordance with applicable rules and procedures for public release.

For more information on the Traffic Light Protocol,
see https://www.us-cert.gov/tlp.

2

Welcome and
Introductions

Bradford Willke

Stakeholder Engagement

TLP:WHITE

3

Introductory
Remarks

Christopher C. Krebs

Director, Cybersecurity and
Infrastructure Security Agency

TLP:WHITE

4

C I S A   |   C Y B E R S E C U R I T Y   A N D   I N F R A S T R U C T U R E   S E C U R I T Y   A G E N C Y

TLP:WHITE

CISA
OVERVIEW

5

TLP:WHITE

6

7

Our
objective
with this
webinar
Enable you to
identify and reduce
your exposure to
this threat

TLP:WHITE

Underlying
message

You can outsource
your operations,
but you cannot
outsource your risk

8

TLP:WHITE

Target
Audience

Managed Service
Providers (MSP)

Clients

9

Housekeeping

• Submit questions and feedback in the

Questions box.

• Troubleshooting: Chat with support
staff in the Technical Support box.

Please complete the short
survey following the webinar.
We appreciate your feedback.

TLP:WHITE

10

Agenda

Threat Overview

Mitigation & Detection

Q&A

CISA Offerings

TLP:WHITE

11

C I S A   |   C Y B E R S E C U R I T Y   A N D   I N F R A S T R U C T U R E   S E C U R I T Y   A G E N C Y

TLP:WHITE

THREAT
OVERVIEW

12

Cyber is
the top
threat to
national
security

TLP:WHITE

13

China wants what we have

TLP:WHITE

14

China needs
cyber
espionage

TLP:WHITE

15

Threat
Actor:
APT 10

TLP:WHITE

Background

• Affiliated with the Ministry of State

Security (December 2018 indictment)

• Active since at least 2006

• Becoming increasingly sophisticated and

capable

Intent

• Most likely to support commercial and

economic espionage

o Made in China 2025, Five Year Plan

• Could also target PII

• Targets of opportunity

16

TLP:WHITE

Campaign:
CLOUD HOPPER

MSPs as Targets

• Provide unique opportunities for
access and collection against
large numbers of targets

• Fits a pattern of threat actors
increasingly targeting supply
chains and trusted relationships

CLOUD HOPPER
• Begins in 2014, picks up in

2016, on-going through 2018
despite public disclosure in 2017

• Targets MSPs and MSP

customers on every continent
targeted (finance and banking,
telecommunications,
biotechnology, consulting,
automotive…)

17

Campaign:
CLOUD HOPPER

TLP:WHITE

TTPs:

•

Initial compromise may be phishing or
spearphishing

• Use of common and custom malware
(PlugX, RedLeaves, QuasarRAT)

• Living-off-the-Land, stolen credentials,

lateral movement

• Encryption of exfiltrated data from target

through MSP networks

• Appears to adjust to public disclosure

18

Key
Takeaways

TLP:WHITE

1. This is a serious actor with
1

resources and they require a
firm resolve by the defenders.

2. This actor sweeps up collateral
2

targets of opportunity, in addition
to their primary targets of
interest.

3. This actor lives off the land, and
3
they may use commonplace
tools found in your network
environments and turn them
against you.

19

C I S A   |   C Y B E R S E C U R I T Y   A N D   I N F R A S T R U C T U R E   S E C U R I T Y   A G E N C Y

TLP:WHITE

MITIGATION
& DETECTION

20

Manage Supply
Chain Risks

• Understand the
supply chain
risks associated
with their MSP to
include
determining
network security
expectations

• Manage risk

equally across
their security,
legal, and
procurement
groups.

Manage
Architecture Risks

• Review and
verify all
connections
between
customer
systems, service
provider
systems, and
other client
enclaves

• Restrict Virtual

Private Network
(VPN) traffic to
and from MSP
using a
dedicated VPN
connection

TLP:WHITE

General
Mitigation
Guidance

Mitigation Strategies for
Managed Service Provider
(MSP) Customers

General
Mitigation
Guidance

Mitigation Strategies for Managed Service Provider
(MSP) Customers

Implement Strong Operational Controls

• Create baseline for system and network behavior;

continuously monitor network devices SIEM
appliance alerts

• Regularly update software and operating systems

22

TLP:WHITE

Manage
Authentication,
Authorization, and
Accounting
Procedures

• Adhere to best
practices for
password and
permission
management

• Ensure MSP

accounts are not
assigned to
administrator groups
and restrict those
accounts to only
systems they
manage

General Mitigation
Guidance

Mitigation Strategies
for Managed Service
Providers (MSP)

Apply the principle of
least privilege to their
environment

TLP:WHITE

Ensure that log
information is aggregated
and correlated to enable
maximum detection
capabilities

Ensure they have fully
implemented all
mitigation actions
available to protect
against this threat

Implement robust
network and host-based
monitoring solutions

Work with their
customers to ensure
hosted infrastructure is
monitored and maintained

23

Specific
Mitigation
Guidance

Mitigation Strategies for
known TTPs

TLP:WHITE

DLL Search Order
High jacking

Enable Safe DLL
Search Mode

• Disallow loading
of remote DLLs

• Forces the use
of restricted
directories

Implement tools for
detecting search
order hijacking
opportunities

Utilize application
whitelisting to block
unknown DLLs

24

Monitoring for
DLL Search
Order Hijacking

• Monitor file system for created, moved,

renamed DLL’s

• Changes in system DLL’s not associated with updates/patches

are suspicious

• Monitor DLL’s loaded by processes (legitimate names,

abnormal path)

TLP:WHITE

25

Logging

Enable and audit
advanced PowerShell
logging

User account activity
(focus on administrator
level accounts)

TLP:WHITE

26

Network
Activity

TLP:WHITE

Monitor processes for
outbound network activity
(against baseline)

Monitor connections
to MSP infrastructure

27

Key
Takeaways

TLP:WHITE

1. Good credentials management
1

goes a long way.

2. Foreclosing the doors this
2

actor uses to move, hide, and
attack can be done through
good cyber hygiene.

3. Recognizing normal versus
3

abnormal system and network
behavior is still the longest
yard to make.

28

Q&A

How do we learn about
these types of malicious
activities?

TLP:WHITE

29

Q&A

What are the benefits of
reporting this information?

TLP:WHITE

30

TLP:WHITE

CISA
Offerings

CISA offers a collection of
resources and tools to
support identification of and
defense against Chinese
malicious activity
• A comprehensive list of mitigation

strategies for IT service providers can be
found at https://www.us-cert.gov/china

Organizations that determine
their risk to be elevated
should conduct a dedicated
investigation to identify any
Chinese related activity
• Contact CISA NCCIC

ncciccustomerservice@hq.dhs.gov
888-282-0870

• Report unauthorized network access

to your local FBI Cyber Division
cywatch@fbi.gov
855-292-3937

31

TLP:WHITE

We
Need
You

Engage with us,
share with us.

One entity’s detection
is another’s prevention.

We’re all in this together.

D E F E N D   T O D A Y .   S E C U R E   T O M O R R O W .

32

TLP:WHITE

For more information:
cisa.gov

For media inquiries, contact
nppdmedia@hq.dhs.gov

Report incidents
Email:
ncciccustomerservice@hq.dhs.gov
Phone: 1-888-282-0870

33


