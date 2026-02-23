---
title: "Active Directory Design Guide"
organization: "Microsoft"
content_type: tool-template
year: 2012
tags: ["active-directory;ad;design;microsoft"]
source_url: ""
license: "© Microsoft. Reproduced for research and educational purposes per 17 U.S.C. § 107 (fair use)."
date_ingested: 2026-02-22
original_format: pdf
---

Active Directory
Design Guide

Thursday, 25 February 2010

Version 2.0.0.0 Baseline

Prepared by

Microsoft

Prepared by Microsoft

Copyright

This document and/or software (“this Content”) has been created in partnership with the National Health Service (NHS) in England. Intellectual Property
Rights to this Content are jointly owned by Microsoft and the NHS in England, although both Microsoft and the NHS are entitled to independently exercise
their rights of ownership. Microsoft acknowledges the contribution of the NHS in England through their Common User Interface programme to this Content.
Readers are referred to www.cui.nhs.uk for further information on the NHS CUI Programme.

All trademarks are the property of their respective companies. Microsoft and Windows are either registered trademarks or trademarks of Microsoft
Corporation in the United States and/or other countries.

© Microsoft Corporation 2010. All rights reserved.

Disclaimer

At the time of writing this document, Web sites are referenced using active hyperlinks to the correct Web page. Due to the dynamic nature of Web sites, in
time, these links may become invalid. Microsoft is not responsible for the content of external Internet sites.

Page ii

Active Directory – Design Guide
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010

Prepared by Microsoft

TABLE OF CONTENTS

1  Executive Summary ....................................................................................................................... 1

2

Introduction .................................................................................................................................... 2
2.1  Value Proposition ...................................................................................................................... 2
2.2  Knowledge Prerequisites .......................................................................................................... 2
2.2.1  Skills and Knowledge .......................................................................................................... 2
2.2.2  Training and Assessment .................................................................................................... 3
Infrastructure Prerequisites ....................................................................................................... 3
2.3
2.4  Audience ................................................................................................................................... 4
2.5  Assumptions .............................................................................................................................. 4

3  Using This Document .................................................................................................................... 5
3.1  Document Structure .................................................................................................................. 5

4.2

4  Envision .......................................................................................................................................... 8
4.1  Directory Services and AD DS .................................................................................................. 8
4.1.1  Overview of Directory Services ........................................................................................... 8
4.1.2  AD DS Overview .................................................................................................................. 9
Initial State Environment ......................................................................................................... 10
4.2.1  Public Domain AD DS Guidance ....................................................................................... 11
4.2.2  Microsoft Healthcare AD DS Guidance ............................................................................. 11
4.3  End State Environment ........................................................................................................... 12
4.4  Scenarios ................................................................................................................................ 12
Infrastructure Environment Scenarios ............................................................................... 12
4.4.1
4.4.2  Technology Scenarios ....................................................................................................... 14

5  Plan ................................................................................................................................................ 16
5.1  Review Planning an AD DS Deployment Project .................................................................... 16
5.1.1  Review the AD DS Deployment Project Cycle .................................................................. 17
5.1.2  Review AD DS Terms and Definitions ............................................................................... 18
5.2  Determine the AD DS Design, Test and Deployment Strategy .............................................. 18
5.2.1  AD DS Design Requirements ............................................................................................ 18
5.2.2  AD DS Testing Requirements ........................................................................................... 20
5.2.3  AD DS Deployment Requirements .................................................................................... 20

6  Develop ......................................................................................................................................... 21
6.1  Design the AD DS Logical Structure ....................................................................................... 22
6.1.1
Identify the Deployment Project Participants ..................................................................... 23
6.1.2  Create a Forest Design ..................................................................................................... 24
6.1.3  Create a Domain Design for Each Forest ......................................................................... 26
6.1.4  Design the OU Structure for Each Domain ....................................................................... 28

Active Directory – Design Guide
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010

Page iii

Prepared by Microsoft

6.1.5  Prepare to Enable Advanced Features via Functional Level ............................................ 28
6.1.6  AD DS Trust Design .......................................................................................................... 29
6.1.7  Active Directory Naming Standards .................................................................................. 31
6.2  Design an AD DS Physical Structure ...................................................................................... 39
6.2.1  Collect Network Information .............................................................................................. 39
6.2.2  Domain Controller Placement............................................................................................ 39
6.2.3  Operations Master Role Placement .................................................................................. 43
6.2.4  Create a Site Design ......................................................................................................... 47
6.2.5  Create a Site Link Design .................................................................................................. 49
6.2.6  Create a Site Link Bridge Design ...................................................................................... 50
6.2.7  Domain Controller Hardware Availability and Scalability Requirements ........................... 51
6.3  Design for AD DS Security ...................................................................................................... 53
6.3.1  Plan a Secure AD DS Environment ................................................................................... 53
6.3.2  Design an Authentication Strategy .................................................................................... 55
6.3.3  Design a Resource Authorisation Strategy ....................................................................... 58
6.3.4  Design a Public Key Infrastructure .................................................................................... 59
6.4  Design Network Services to Support AD DS .......................................................................... 60
6.4.1  DNS Infrastructure to Support AD DS ............................................................................... 61
6.4.2  WINS Infrastructure to Support AD DS ............................................................................. 65
6.4.3  Additional Network Services .............................................................................................. 66

7  Stabilise ......................................................................................................................................... 67
7.1  Design a Test Environment ..................................................................................................... 67
7.1.1  Overview of a Test Environment ....................................................................................... 67
7.1.2  Create a Test Plan ............................................................................................................. 68
7.1.3  Plan a Test Lab ................................................................................................................. 68
7.1.4  Design the Test Lab .......................................................................................................... 69
7.1.5  Develop the Test Lab ........................................................................................................ 69
7.1.6  Design the Test Cases ...................................................................................................... 70
7.1.7  Conduct the Tests ............................................................................................................. 71
7.1.8  Use the Test Lab After Deployment .................................................................................. 72
7.2  Design a Pilot Project .............................................................................................................. 72
7.2.1  Overview of a Pilot Project ................................................................................................ 72
7.2.2  Create a Pilot Plan ............................................................................................................. 74
7.2.3  Prepare for the Pilot ........................................................................................................... 74
7.2.4  Deploy and Test the Pilot .................................................................................................. 75
7.2.5  Evaluate the Pilot ............................................................................................................... 75
7.3  Prepare for Production Deployment ....................................................................................... 75

8  Deploy ........................................................................................................................................... 76
8.1  AD DS Deployment Prerequisites ........................................................................................... 77
8.2  AD DS Deployment Strategy .................................................................................................. 78
8.2.1  AD DS Forest Root Domain Deployment .......................................................................... 78

Active Directory – Design Guide
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010

Page iv

Prepared by Microsoft

8.2.2  Raise the Functional Level ................................................................................................ 80
8.2.3  Deploy Windows Server 2003 Regional Domains (Optional) ............................................ 80
8.3  Deploy a Domain Controller .................................................................................................... 80
8.3.1  AD DS Installation Wizard ................................................................................................. 81
8.3.2  Automated Scripted Installations for Domain Controllers .................................................. 81
Install an Additional Domain Controller Through Backup Media ....................................... 83
8.3.3
8.4  Test the Installation of AD DS ................................................................................................. 83
8.5  Configure AD DS..................................................................................................................... 84

9  Operate .......................................................................................................................................... 85
9.1  Ensure a Managed AD DS Infrastructure ............................................................................... 86
9.1.1  People and Process .......................................................................................................... 86
9.1.2  Automated Change and Configuration Management ........................................................ 86
9.1.3  Processes and Procedures for Improving Service Management ...................................... 87
9.2  Ensure an Operational AD DS Infrastructure .......................................................................... 88
9.2.1  Manual Operational Activities ............................................................................................ 88
9.2.2  Methods to Automate Manual Operational Activities......................................................... 89
9.2.3  Products that Automate Operational Activities .................................................................. 90
9.3  AD DS Administrative Tools .................................................................................................... 90

APPENDIX A  Skills and Training Resources ................................................................................. 92
PART I  Microsoft Active Directory .................................................................................................. 92
Group Policy, both Domain and Local ........................................................................... 92
PART II
PART III  Network Services ........................................................................................................... 93

APPENDIX B  Windows Server 2003 Active Directory Design Complexity ................................. 94

APPENDIX C  AD DS Functionality Features .................................................................................. 95

APPENDIX D  Background Information for Planning Domain Controller Capacity .................... 99

APPENDIX E  AD DS Tests ............................................................................................................. 101

APPENDIX F  Document Information ............................................................................................ 103
PART I  Terms and Abbreviations ................................................................................................. 103
References .................................................................................................................. 106
PART II

Active Directory – Design Guide
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010

Page v

Prepared by Microsoft

1

UMMARY
EXECUTIVE SUMMARY

Design Guide will help accelerate the design and deployment of Microsoft®
The Active Directory® Design Guide will help accelerate the design and deployment of Microsoft
Design Guide will help accelerate the design and deployment of Microsoft
Windows Server® 2008 R2 Active Directory
, and bring about a reduction in diversity of its implementation.
organisation, and bring about a reduction in diversity of its implementation.

2008 R2 Active Directory® Domain Services (AD DS) within a healthcare
a healthcare

this guidance will:
Implementation of this guidance will:

(cid:1)  Provide consistent and secure Active Directory

increase efficiency
Provide consistent and secure Active Directory Domain Services that increase efficiency

(cid:1)  Provide a flexible framework for the organisation and management of resources, including
Provide a flexible framework for the organisation and management of resources, including
Provide a flexible framework for the organisation and management of resources, including
vers, and printers
the network authorisation of, users, client computers, servers, and printers
the network authorisation

The guidance given in this document is based on existing public guidance within the Infrastructure
The guidance given in this document is based on existing public guidance within the
The guidance given in this document is based on existing public guidance within the
DS Design Guide2,
Planning and Design series1 (IPD) documents, the
Windows Server 2008 and Windows Server 2008 R2 Technet Library3. This guidance has
. This guidance has
and the Windows Server 2008 and Windows Server 2
healthcare industry.
also been overlaid with current best practice recommendations specific to the healthcare industry
also been overlaid with current best practice recommendations specific to the

(IPD) documents, the Windows Server 2008 AD DS

1 Infrastructure Planning and Design {
gb/library/cc196387.aspx
http://technet.microsoft.com/en-gb/library/cc196387.aspx

{R1}:

2 Windows Server 2008 AD DS Design
Windows Server 2008 AD DS Design  {R2}:
us/library/cc754678(WS.10).aspx
http://technet.microsoft.com/en-us/library/cc754678(WS.10).aspx

3 Windows Server 2008 and Windows Server 2008 R2
Windows Server 2008 and Windows Server 2008 R2  {R3}:
us/library/dd349801(WS.10).aspx
http://technet.microsoft.com/en-us/library/dd349801(WS.10).aspx

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 1

Prepared by Microsoft

2

NTRODUCTION
INTRODUCTION

This document is a component of the strategic Microsoft infrastructure guidance being provided
This document is a component of the strategic Microsoft infrastructure guidance being provided to
This document is a component of the strategic Microsoft infrastructure guidance being provided
practice guidance, samples and specific design
. It provides current best-practice guidance, samples and specific design
the healthcare industry. It provides current best
that is envision, plan, develop, stabilise, deploy and operate) of
that is envision, plan, develop, stabilise, deploy and operate
decisions for the full lifecycle (that is envision, plan, develop, stabilise, deploy and operate
ork services, such as Domain
Microsoft Windows Server 2008 R2 AD DS and its principal network services, such as Domain
Microsoft Windows Server 2008 R2
Name System (DNS). The provision of a standard
centric approach to designing and
Name System (DNS). The provision of a standard healthcare-centric approach to designing and
deploying a directory authentication and authorisation service will reduce the time required to plan,
deploying a directory authentication and authorisation service will reduce the time required to plan,
deploying a directory authentication and authorisation service will reduce the time required to plan,
hereby enabling the Total Cost of Ownership (TCO) savings that
deploy and operate the service, thereby enabling the Total Cost of Ownership (TCO) savings that
deploy and operate the service, t
achieved by decreasing diversity.
can be achieved by decreasing diversity.

Value Proposition
2.1  Value Proposition

This document provides guidance on designing and implementing a simplified, cost-effective,
This document provides guidance on designing and implementing a simplified, cost
This document provides guidance on designing and implementing a simplified, cost
. The offering is
reliable, and robust directory service infrastructure for healthcare organisations. The offering is
reliable, and robust directory service inf
designed to:

(cid:1)  Help identify potential design and deployment risks
Help identify potential design and deployment risks

(cid:1)  Provide rapid knowledge transfer to reduce the learning curve of designing
Provide rapid knowledge transfer to reduce the learning curve of designing AD DS
Provide rapid knowledge transfer to reduce the learning curve of designing

(cid:1)  Establish some preliminary design decisions before

moving ahead with the implementation
Establish some preliminary design decisions before moving ahead with the implementation

(cid:1)  Provide a consolidation of relevant publically available

best practice guidance
Provide a consolidation of relevant publically available AD DS best practice guidance

Knowledge Prerequisites
2.2  Knowledge Prerequisites

This section outlines the required knowledge and skills, and provides suggested training and skill
This section outlines the required knowledge and skills, and provides suggested training and skill
This section outlines the required knowledge and skills, and provides suggested training and skill
resources to make the most of this guidance. The necessary infrastructure
assessment resources to make the most of this guidance. The necessary infrastructure
resources to make the most of this guidance. The necessary infrastructure
prerequisites are detailed in section 2.3.
prerequisites are detailed in section

made throughout this document, a number of
To implement effectively the recommendations made throughout this document, a number of
To implement effectively the recommendations
based and environmental infrastructure prerequisites should be in place.
knowledge-based and environmental infrastructure prerequisites should be in place.
based and environmental infrastructure prerequisites should be in place.

2.2.1

Skills and Knowledge
Skills and Knowledge

The technical knowledge and minimum skills required to use this guidance are:
The technical knowledge and minimum skills required to use this guidance are:
The technical knowledge and minimum skills required to use this guidance are:

(cid:1)  Microsoft Windows Server 2008 R

Microsoft Windows Server 2008 R2 AD DS

(cid:2)  AD DS design, including DNS design
design, including DNS design

(cid:2)  Domain Controller Capacity Planning, site design and Domain Controller Placement
Domain Controller Capacity Planning, site design and Domain Controller Placement
Domain Controller Capacity Planning, site design and Domain Controller Placement

(cid:2)  Operations Master roles: placement of role holders, troubleshooting role holders and
Operations Master roles: placement of role holders, troubleshooting role holders and
Operations Master roles: placement of role holders, troubleshooting role holders and
management

(cid:2)  Organisation Unit (OU) design
Organisation Unit (OU) design

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 2

Prepared by Microsoft

(cid:1)  Group Policy, both Domain and Local
Policy, both Domain and Local

(cid:2)  Controlling operating system

operating system configuration and security

(cid:2)  Design and implementation for application deployment
Design and implementation for application deployment

(cid:2)  Management using Microsoft Group Policy Management Console (GPMC): scripting,
Management using Microsoft Group Policy Management Console (GPMC): scripting,
Management using Microsoft Group Policy Management Console (GPMC): scripting,
policy export and import, backup and re
policy export and import, backup and restore

(cid:2)

Implement within an Active Directory OU hierarchy, using security groups to further
Implement within an Active Directory OU hierarchy, using security groups to further
Implement within an Active Directory OU hierarchy, using security groups to further
control scope

(cid:1)  Network Services

(cid:2)  DNS, particularly what
requires from DNS, and how it can be integrated with
DNS, particularly what AD DS requires from DNS, and how it can be integrated with
party systems
third-party systems

(cid:2)  Dynamic Host Configuration Protoc

ol (DHCP): creating scopes, defining scope and
Dynamic Host Configuration Protocol (DHCP): creating scopes, defining scope and
server properties, lease configuration, reserving addresses, trouble shooting,
server properties, lease configuration, reserving addresses, trouble shooting,
server properties, lease configuration, reserving addresses, trouble shooting,
configuration to support
configuration to support Remote Installation Services (RIS), integration with
ver 2008 R2 (preferred)
using Microsoft DHCP service on Windows Server 2008 R2 (preferred)
using Microsoft DHCP service on Windows Ser

(RIS), integration with AD DS if

(cid:2)  Windows Internet Name Service (WINS): service placement, integration with Microsoft
Windows Internet Name Service (WINS): service placement, integration with Microsoft
Windows Internet Name Service (WINS): service placement, integration with Microsoft
, replication design, troubleshooting and integration with DNS
DNS and AD DS, replication design, troubleshooting and integration with DNS
, replication design, troubleshooting and integration with DNS

(cid:2)  Local area networks (LAN) and networking devices such as switches, modem
ocal area networks (LAN) and networking devices such as switches, modems, and
ocal area networks (LAN) and networking devices such as switches, modem

wireless access points
wireless access points

2.2.2

Training and Assessment
Training and Assessment

Guidelines on the basic skill sets that are required in order to make best use of this Deliverable are
Guidelines on the basic skill sets that are required in order to make best use of this Deliverable are
Guidelines on the basic skill sets that are required in order to make best use of this Deliverable are
detailed in APPENDIX A. These represent the training courses and other resources available.
. These represent the training courses and other resources available. All
. These represent the training courses and other resources available.
courses mentioned are optional and can be provided by a variety of certified training partners.
courses mentioned are optional and can be provided by a variety of certified training partners.
courses mentioned are optional and can be provided by a variety of certified training partners.

2.3

Infrastructure Prerequisites
Infrastructure Prerequisites

The following are prerequisites for implementing Windows Server 2008 R2 AD
The following are prerequisites for impl
organisation:

DS in a healthcare

(cid:1)  A Windows® XP, Windows Vista

XP, Windows Vista® and/or Windows® 7 client infrastructure that requires
7 client infrastructure that requires

authentication and management by AD DS
authentication and management by

(cid:1)  A Windows Server® 200

server infrastructure that requires authentication and
2000 or later server infrastructure that requires authentication and

management

(cid:1)  A Windows Server 2008 R2 server build that is detailed in the document
A Windows Server 2008 R2 server build that is detailed in the document Automated Build
A Windows Server 2008 R2 server build that is detailed in the document
Healthcare Desktop and Server Guide

Desktop and Server Guide {R4}

(cid:1)  An Internet Protocol (IP) addressing scheme for the network, utilising an automated system
An Internet Protocol (IP) addressing scheme for the network, utilising an automated system
An Internet Protocol (IP) addressing scheme for the network, utilising an automated system
such as that provided by DHCP
such as that provided by DHCP

(cid:1)  Hostname and Network Basic Input Output System (NetBIOS) name resolution systems,
Hostname and Network Basic Input Output System (NetBIOS) name resolution systems,
Hostname and Network Basic Input Output System (NetBIOS) name resolution systems,
by DNS and WINS
such as that provided by DNS and WINS

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 3

Prepared by Microsoft

2.4  Audience

The guidance contained in this document is targeted at a variety of roles within a healthcare IT
The guidance contained in this document is targeted at a variety of roles within
The guidance contained in this document is targeted at a variety of roles within
ide for this document, illustrating the roles and the
provides a reading guide for this document, illustrating the roles and the
organisation. Table 1 provides a reading gu
sections of the document that are likely to be of most interest. The structure of the sections referred
sections of the document that are likely to be of most interest. The structure of the sections referred
sections of the document that are likely to be of most interest. The structure of the sections referred
to are described in section 3.1

3.1.

Role

Document Usage
Document Usage

IT Manager

IT Architect

Review of the entire document to understand
Review of the entire document to understand
the justification and drivers, and to develop an
the justification and drivers, and to develop an
understanding of the implementation
understanding of the implementation
requirements

Review the relevant areas within the document
Review the relevant areas within the document
against local architecture strategy and
against local architecture strategy and
implementation plans
implementation plans

e
v
i
t
u
c
e
x
E

y
r
a
m
m
u
S
(cid:1)

n
o
i
s
i
v
n
E
(cid:1)

p
o
l
e
v
e
D

e
s
i
l
i

b
a
t
S

l

y
o
p
e
D

e
t
a
r
e
p
O

n
a
l
P

(cid:1)

(cid:1)

(cid:1)

(cid:1)

IT Professional/
Administrator

Detailed review and implementation of the
Detailed review and implementation of the
guidance to meet local requirements
guidance to meet local

(cid:1)

(cid:1)

(cid:1)

(cid:1)

(cid:1)

(cid:1)

(cid:1)

Table 1: Document Audience

2.5  Assumptions

that healthcare organisations will implement their own production
It is anticipated that healthcare organisations
infrastructure in order to use a Microsoft authentication service. However, if multiple healthcare
infrastructure in order to use a Microsoft authentication service. However, if multiple
infrastructure in order to use a Microsoft authentication service. However, if multiple
organisations collaborate closely, it would be advantageous to implement an
collaborate closely, it would be advantageous to implement an AD
ility for users to roam using a single
infrastructure across this larger cohesive unit, thus aiding the ability for users to roam using a single
infrastructure across this larger cohesive unit, thus aiding the ab
logon, and access services and resources within these organisations.
logon, and access services and resources within these

own production AD DS

AD DS forest

healthcare organisations that want to share
The guidance provided in this document assumes that
The guidance provided in this document assumes that healthcare organisations
itable IP Addressing schemes in place to
services and resources between sites already have suitable IP Addressing schemes in place to
services and resources between sites already have su
site communication; that is, unique IP Addressing schemes assigned to
enable successful site-to-site communication; that is, unique IP Addressing schemes assigned to
site communication; that is, unique IP Addressing schemes assigned to
, and the underlying DNS, requires the use
organisation with no overlap. AD DS, and the underlying DNS, requires the use
each participating organisation
of unique IP Addressing schemes at adjoining sites in order for cross
site communication to
g schemes at adjoining sites in order for cross-site communication to
function successfully. The use of Network Address Translation (NAT) within an AD DS environment
function successfully. The use of Network Address Translation (NAT) within an
function successfully. The use of Network Address Translation (NAT) within an
is neither recommended nor supported by Microsoft.
is neither recommended nor supported by Microsoft.

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 4

3  USING THIS D

DOCUMENT

Prepared by Microsoft

and IT administrators who are
tended for use by healthcare organisations and IT administrators who are

This document is intended for use by
responsible for designing AD DS
making process, rather than a detailed procedural
guidance focuses on the decision-making process, rather than a detailed procedural
guidance focuses on the decision
implementation.

, including deployment and operations practices. As a result, the
DS, including deployment and operations practices. As a result, the

The design of a directory service requires a significant
The design of a directory service requires a significant undertaking because it impacts
aspects of infrastructure design and deployment.
aspects of infrastructure design and deployment.

undertaking because it impacts many

This Active Directory Design Guide

Guide aims to:

(cid:1)  Collate the numerous public technical resources available for designing
Collate the numerous public technical resources available for designing AD DS, into a
Collate the numerous public technical resources available for designing
consolidated healthcare

healthcare-specific document

(cid:1)  Provide the order for designing

through a sequenced checklist of design and
Provide the order for designing AD DS through a sequenced checklist of design and
deployment steps

(cid:1)  Identify the Microsoft curren

Identify the Microsoft current recommended practices for designing AD
industry experience, to minimise design time and reduce risk
industry experience, to minimise design time and reduce risk

 DS, based on

(cid:1)  Identify key design decisions pertinent to the

, and provide design
Identify key design decisions pertinent to the healthcare industry, and provide design
multiple implementations
solutions which reduce configuration diversity across multiple implementations
solutions which reduce configuration diversity across

(cid:1)  Provide a standardised design and configuration approach to reduce the administration and
Provide a standardised design and configuration approach to reduce the administration and
Provide a standardised design and configuration approach to reduce the administration and
management overheads of the system, thereby reducing overall support costs
management overheads of the system, thereby reducing overall support costs
management overheads of the system, thereby reducing overall support costs

(cid:1)  Provide a consistent and reliable directory service to users as th

ey move around their
Provide a consistent and reliable directory service to users as they move around their
, thereby increasing their utilisation and service quality perception of
healthcare organisation, thereby increasing their utilisation and service quality perception of
healthcare organisation
the infrastructure

Document Structure
3.1  Document Structure

This document contains six sections that deal with the project lifecycle, as illustrated in Figure 1
This document contains six sections that deal with the project lifecycle, as illustrated in
This document contains six sections that deal with the project lifecycle, as illustrated in
and in the list below:

(cid:1)  Envision

(cid:1)  Plan

(cid:1)  Develop

(cid:1)  Stabilise

(cid:1)  Deploy

(cid:1)  Operate

Each section is based on the Microsoft IT Project Lifecycle as defined in the Microsoft Solutions
Each section is based on the Microsoft IT Project Lifecycle as defined in the Microsoft Solutions
Each section is based on the Microsoft IT Project Lifecycle as defined in the Microsoft Solutions
Framework (MSF) Process Model, and the Microsoft Operations Framework (MOF). The IT Project
Framework (MSF) Process Model, and the Microsoft Operations Framework (MOF). The IT Project
Framework (MSF) Process Model, and the Microsoft Operations Framework (MOF). The IT Project
ramework Core White Papers4 and
Lifecycle is described in more detail in the Microsoft Solutions Framework Core White Paper
Lifecycle is described in more detail in the
5. The MSF Process Model and MOF describe a high
the MOF Executive Overview5
. The MSF Process Model and MOF describe a high-level sequence
of activities for building, deploying and managing IT solutions. Rather than prescribing a specific
of activities for building, deploying and managing IT solutions. Rather than prescribing a specific
of activities for building, deploying and managing IT solutions. Rather than prescribing a specific
xible enough to accommodate a broad range of IT projects.
series of procedures, they are flexible enough to accommodate a broad range of IT projects.
series of procedures, they are fle

Microsoft Solutions Framework Core White Papers:

4 Microsoft Solutions Framework Core White
fc886956790e&DisplayLang=en
http://www.microsoft.com/downloads/details.aspx?FamilyID=e481cb0b-ac05-42a6-bab8-fc886956790e&DisplayLang=en
http://www.microsoft.com/downloads/details.aspx?FamilyID=e481cb0b

5 MOF Executive Overview:
http://www.microsoft.com/technet/solutionaccelerators/cits/mo/mof/mofeo.mspx
http://www.microsoft.com/technet/solutionaccelerators/cits/mo/mof/mofeo.mspx

Page 5

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

The following diagram illustrates the different sections of this guide:
The following diagram illustrates the different sections of this guide:

Prepared by Microsoft

Microsoft Solutions Framework Process Model Phases and Document Structure
Figure 1: Microsoft Solutions Framework Process Model Phases and Document Structure

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 6

Prepared by Microsoft

solution are listed below. Where
documentation resources for developing an AD DS solution are listed below. Where
The key public documentation resources for developing an
appropriate, specific chapters or sections from these documents have been referenced throughout
appropriate, specific chapters or sections from these documents have been referenced throughout
appropriate, specific chapters or sections from these documents have been referenced throughout
this guidance.

(cid:1)  Infrastructure Planning and Design
, in the Directory Services, Directory Service
Infrastructure Planning and Design {R1}, in the Directory Services, Directory Service
level architectural overview of major concepts
Planning Guide section, for high-level architectural overview of major concepts
Planning Guide section, for high

(cid:1)  Windows Server Technologies: Networking

Windows Server Technologies: Networking 6, for high-level architectural overview of major
architectural overview of major
concepts

(cid:1)  Active Directory Services

Active Directory Services7, for detailed technical review of components aimed at IT
, for detailed technical review of components aimed at IT
Professionals

(cid:1)  Windows Server 2008 and Windows Server 2008 R2

for detailed technical analysis of
Windows Server 2008 and Windows Server 2008 R2 {R3} for detailed technical analysis of
more specialised components aimed at IT Professionals
more specialised components aimed at IT Professionals

6 Windows Server Technologies: Networking
Windows Server Technologies: Networking {R6}:
us/library/cc753940(WS.10).aspx
http://technet.microsoft.com/en-us/library/cc753940(WS.10).aspx

7 Designing and Deploying Directory and Security Services
Designing and Deploying Directory and Security Services {R5}:
us/library/dd578336(WS.10).aspx
http://technet.microsoft.com/en-us/library/dd578336(WS.10).aspx

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 7

Prepared by Microsoft

4

ENVISION

The Envision phase addresses one of the most fundamental requirements for success in any
The Envision phase addresses one of the most fundamental requirements for success in any
The Envision phase addresses one of the most fundamental requirements for success in any
ehind a common vision. There must be a clear vision of
project unification of the project team behind a common vision. There must be a clear vision of
project unification of the project team b
what is to be accomplished such that it can be stated in clear terms. Envisioning, by creating a
what is to be accomplished such that it can be stated in clear terms. Envisioning, by creating a
what is to be accomplished such that it can be stated in clear terms. Envisioning, by creating a
high-level view of the overall goals and constraints, will serve as an early form of planning. It sets
level view of the overall goals and constraints, will serve as an early form of planning. It sets
level view of the overall goals and constraints, will serve as an early form of planning. It sets
he stage for the more formal planning process that will take place during the planning phase.
he stage for the more formal planning process that will take place during the planning phase.
the stage for the more formal planning process that will take place during the planning phase.

ents that should be
level checklist, illustrating the sequence of events that should be
Figure 2 acts as a high-level checklist, illustrating the sequence of ev
a directory service within a healthcare organisation:
a directory service within a healthcare organisation
undertaken when envisioning a directory service within a healthcare organisation

: Sequence for Defining a Directory Service Design
Figure 2: Sequence for Defining a Directory Service Design

4.1  Directory Services and

Directory Services and AD DS

The persistent drive to reduce the complexity and diversity of the network infrastructure and drive
The persistent drive to reduce the complexity and diversity of the network infrastructure and drive
The persistent drive to reduce the complexity and diversity of the network infrastructure and drive
down costs makes it paramount that IT delivers new value back to the business with the least
down costs makes it paramount that IT delivers new value back to the business with the least
down costs makes it paramount that IT delivers new value back to the business with the least
ous process that will assist in
amount of investment and effort. This guidance provides a rigor
amount of investment and effort. This guidance provides a rigorous process that will assist in
are designed and developed to
ensuring that directory services within a healthcare organisation are designed and developed to
ensuring that directory services within
provide maximum business value.
provide maximum business value.

Overview of Directory Services
4.1.1  Overview of Directory Services

ut networked devices and services,
A directory service provides the ability to store information about networked devices and services,
A directory service provides the ability to store information abo
and the people who use them, in a central location within a distributed environment. A directory
and the people who use them, in a central location within a distributed environment. A directory
and the people who use them, in a central location within a distributed environment. A directory
service also implements the services that make this information available to users, computers, and
service also implements the services that make this information available to users, computers, and
service also implements the services that make this information available to users, computers, and
applications. Therefore, a directory service is both a directory (the store of this information) and a
directory service is both a directory (the store of this information) and a
directory service is both a directory (the store of this information) and a
set of services that provide the means to securely add, modify, delete, and locate data in the
set of services that provide the means to securely add, modify, delete, and locate data in the
set of services that provide the means to securely add, modify, delete, and locate data in the
directory store.

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 8

Prepared by Microsoft

Overview
4.1.2  AD DS Overview

is the network focused directory service included in the Windows 2000, Windows Server
uded in the Windows 2000, Windows Server
AD DS is the network focused directory service incl
2003 and Windows Server 2008 family of operating systems.
delivers an extensible and
2003 and Windows Server 2008 family of operating systems. AD DS delivers an extensible and
scalable service that provides network authentication, administration and management of directory
scalable service that provides network authentication, administration and management of
scalable service that provides network authentication, administration and management of
services to an organisation running a Windows

n running a Windows-based network infrastructure.

and how it acts as the focal point of the Windows
illustrates the benefits of AD DS and how it acts as the focal point of the Windows
Figure 3 illustrates the benefits of
2008 R2 network, demonstrating how it can be used to manage identities and broker
Server 2008 R2 network, demonstrating how it can be used to manage identities and broker
2008 R2 network, demonstrating how it can be used to manage identities and broker
relationships between distributed resources.
relationships between distributed resources.

on a Windows Server 2008 R2 Network
Figure 3: AD DS on a Windows Server 2008 R2 Network

AD DS provides:

(cid:1)  A central location for network adm

inistration and the delegation of administrative
A central location for network administration and the delegation of administrative
authority

AD DS acts as a repository for objects representing all network users, devices, and
acts as a repository for objects representing all network users, devices, and
acts as a repository for objects representing all network users, devices, and
resources, and provides the ability to group objects for ease of management and
resources, and provides the ability to group objects for ease of management and the
resources, and provides the ability to group objects for ease of management and
application of security and Group Policy. Group Policy refers to applying policy
application of security and Group Policy. Group Policy refers to applying policy
application of security and Group Policy. Group Policy refers to applying policy
(configuration settings) to groups of computers and/or users contained in AD DS.
(configuration settings) to groups of computers and/or users contained in
(configuration settings) to groups of computers and/or users contained in

(cid:1)  Information security and single sign

on for user access to local network resources
Information security and single sign-on for user access to local network resources

Tight integration with security eliminates costly tracking of accounts for authentication and
integration with security eliminates costly tracking of accounts for authentication and
integration with security eliminates costly tracking of accounts for authentication and
authorisation between systems. A single user name and password (or smartcard)
authorisation between systems. A single user name and password (or smartcard)
authorisation between systems. A single user name and password (or smartcard)
combination can identify each network user, and this identity follows the user throughout
combination can identify each network user, and this identity follows the user throughout
combination can identify each network user, and this identity follows the user throughout
the local network.

Page 9

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Prepared by Microsoft

(cid:1)  Scalability

AD DS can be designed and implemented in numerous configurations to achieve scalability
can be designed and implemented in numerous configurations to achieve scalability
can be designed and implemented in numerous configurations to achieve scalability
large-scale site to meet
from a single site with a
with a small number of users, to a highly complex large
any current and future network authentication requirements.
any current and future network authenticati

(cid:1)  Easy and flexible searching of the Active Directory
Easy and flexible searching of the Active Directory

Users and administrators can use Windows XP, Windows Vista or Windows 7 desktop tools
Users and administrators can use Windows XP, Windows Vista or Windows 7 desktop tools
Users and administrators can use Windows XP, Windows Vista or Windows 7 desktop tools
to search the entire Active Directory.
to search the entire Active Directory

(cid:1)  Storage for application data
Storage for application data

to store data that is shared between applications, and
provides a central location to store data that is shared between applications, and

AD DS provides a central location
with applications that need to distribute their data across entire Windows networks.
with applications that need to distribute their data across entire Windows networks
with applications that need to distribute their data across entire Windows networks

(cid:1)  Efficient synchronisation of directory updates
Efficient synchronisation of directory updates

Updates are distributed throughout the network through secure and co
Updates are distributed throughout the network through secure and cost
between domain controllers.
between domain controllers

st-efficient replication

(cid:1)  Remote administration
Remote administration

It is possible, providing the user has been granted appropriate permissions, to connect to
It is possible, providing the user has been granted appropriate permissions, to connect to
It is possible, providing the user has been granted appropriate permissions, to connect to
any domain controller remotely from any Windows
Server administrative tools installed

based computer that has Windows
remotely from any Windows-based computer that has Windows

ministrative tools installed.

(cid:1)  Single, modifiable, and extensible schema
Single, modifiable, and extensible schema

The schema is the definition of the objects and their attributes that can be created in
The schema is the definition of the objects and their attributes that can be created in
The schema is the definition of the objects and their attributes that can be created in
. It is possible to modify the schema to create new attributes that can be used to
AD DS. It is possible to modify the schema to create new attributes that can be used to
. It is possible to modify the schema to create new attributes that can be used to
nt new types of objects or to extend existing objects. For example, attributes of the
implement new types of objects or to extend existing objects. For example, attributes of the
nt new types of objects or to extend existing objects. For example, attributes of the
user object store information, such as username, password, and telephone number
user object store information, such as username,

password, and telephone number.

(cid:1)  Integration of service names with DNS, the Internet standard name resolution service
Integration of service names with DNS, the Internet standard name resolution service
Integration of service names with DNS, the Internet standard name resolution service

relies on DNS to implement an IP-based naming system so that

based naming system so that the Active Directory

AD DS relies on DNS to implement an IP
and domain controllers

domain controllers are locatable over standard IP, both on intranets and the Internet

are locatable over standard IP, both on intranets and the Internet.

(cid:1)  Lightweight Directory Access Protocol (LDAP) support
Lightweight Directory Access Protocol (LDAP) support

LDAP is the industry standar
LDAP is the industry standard directory access protocol, making AD DS
to management and query applications. AD DS supports LDAP version 2 and version 3
to management and query applications.

supports LDAP version 2 and version 3.

DS widely accessible

A detailed view of all the components involved in an AD DS design is illustrated in
A detailed view of all the components involved in an

design is illustrated in APPENDIX B.

4.2

Initial State Environment
Initial State Environment

design can be a complex undertaking and there are many different possible approaches to
AD DS design can be a complex undertaking and there are many different possible approaches to
design can be a complex undertaking and there are many different possible approaches to
designing and implementing an
solution. The provision of a standardised design approach,
designing and implementing an AD DS solution. The provision of a standardised design approach,
including key design recommendations, will reduce the time and effort required to design and
including key design recommendations, will reduce the time and effort required to design and
including key design recommendations, will reduce the time and effort required to design and
deploy a directory service within a healthcare organisation.
deploy a directory service within

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 10

Prepared by Microsoft

xamples of the potential diversity of a directory services design within
Figure 4 illustrates examples of the potential diversity of a directory services design within
xamples of the potential diversity of a directory services design within
that could be derived if using purely public information sources without
healthcare organisations that could be derived if using purely public information sources without
that could be derived if using purely public information sources without
specific healthcare guidance.

Note

The following diagram provides examples, and is not intended to provide specific design
The following diagram provides examples, and is not intended to provide specific design
The following diagram provides examples, and is not intended to provide specific design
recommendations.

Designs without Guidance
Figure 4: Potential Diversity of AD DS Designs without Guidance

4.2.1

Public Domain AD DS Guidance
Public Domain

eb sites, documents and guidance which provide assistance in designing
The Internet hosts many web sites, documents and guidance which provide assistance in designing
eb sites, documents and guidance which provide assistance in designing
. This information can be hard to navigate, and often contains inaccuracies or out-of-date
. This information can be hard to navigate, and often contains inaccuracies or out
AD DS. This information can be hard to navigate, and often contains inaccuracies or out
date current best practice
information. This document seeks to provide accurate and up-to-date current best practice
information. This document seeks to provide accurate and up
guidance, much of which is based upon four publicly available sources of in
guidance, much of which is based upon four publicly available sources of information for
which range in technical depth. These sources are:
which range in technical depth. These sources are:

formation for AD DS,

(cid:1)  Windows Server 2008 R2 Product Help
Windows Server 2008 R2 Product Help {R7}, which provides a thorough product
and generic deployment guidance
and generic deployment guidance

which provides a thorough product overview

(cid:1)  Infrastructure Planning and Design

level design guidance
Infrastructure Planning and Design {R1}, which provides architectural-level design guidance
for an IT infrastructure

(cid:1)  Active Directory Services

which provides technical guidelines, tools, and the
Active Directory Services {R5}, which provides technical guidelines, tools, and the
recommended process for designing and deploying Windows Server 200
recommended process for designing and deploying Windo
technologies to meet generic business needs and IT goals
Security services technologies to meet generic business needs and IT goals
technologies to meet generic business needs and IT goals

2008 R2 Directory and

(cid:1)  The Microsoft Technet collection

Windows Server 2008 and Windows
Technet collection of documentation: Windows Server 2008 and Windows

Server 2008 R2 {R3}, which contains
Server 2008 R2 topics, such as
Security

technical guidance on specific Windows
, which contains in-depth technical guidance on specific Windows
, Networking and  Windows
topics, such as AD DS, Core Operating system, Networking and  Windows

4.2.2  Microsoft Healthcare AD

Microsoft Healthcare AD DS Guidance

The guidance provided within this document is predominantly based upon two Microsoft public
The guidance provided within this document is predominantly based upon two Microsoft public
The guidance provided within this document is predominantly based upon two Microsoft public
resources, the Infrastructure Planning and Design series
Infrastructure Planning and Design series {R1} and the Active Directory
. The specific books, chapters and sections from these resources that relate to this
collection {R5}. The specific books, chapters and sections from these resources that relate to this
. The specific books, chapters and sections from these resources that relate to this
AD DS guidance will be identified where

guidance will be identified where appropriate.

tive Directory Services

healthcare organisations will each have unique requirements that cannot be
have unique requirements that cannot be
It is appreciated that healthcare organisations
step guidance will do.
met by architecture guidance alone. Sometimes, only prescriptive, step-by-step guidance will do.
met by architecture guidance alone. Sometimes, only prescriptive, step

Page 11

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Prepared by Microsoft

Active Directory Services collection {R5} have

Infrastructure Planning and Design {R1} and the Active Directory Services collection
The Infrastructure Planning and Design
organisation IT
designed and developed with the knowledge that, when adopted, organisation IT
been designed and developed with the knowledge that, when adopted,
will require further customisation to match the unique business and technology
infrastructure will require further customisation to match the unique business and technology
will require further customisation to match the unique business and technology
requirements of individual healthcare organisations
, but rather a set of design choices and
to be a universal solution for all healthcare organisations, but rather a set of design choices and
to be a universal solution for all
the local directory services solution, understand what
best practices that can be used to jump start the local directory services solution, understand what
best practices that can be used to
is made in a given scenario, and how to implement that
decisions are available, why a decision is made in a given scenario, and how to implement that
decisions are available, why a decision
decision.

healthcare organisations. The referenced documentation i

. The referenced documentation is not intended

guidance endeavours not to repeat content from public documentation, but to provide a
This AD DS guidance endeavours not to repeat content from public documentation, but to provide a
guidance endeavours not to repeat content from public documentation, but to provide a
consolidated, organised and structured reference list to these documents. Where appropriate,
consolidated, organised and structured reference list to these documents.
includes recommendations where
default installation configurations or Windows Server 2008 R2 configuration.
default installation configurations or Windows Server 2008 R2 configuration.

should deviate from the current
recommendations where a typical healthcare organisation should deviate from the current

Where appropriate, it

End State Environment
4.3  End State Environment

ll help lead a healthcare
The Directory Services guidance provided within this document will help lead a healthcare
The Directory Services guidance provided within this docu
through the process of making inherently complex design and implementation
organisation through the process of making inherently complex design and implementation
through the process of making inherently complex design and implementation
infrastructure.
decisions for an AD DS infrastructure.

all’, this document enables a healthcare
design guidance can be a ‘one size fits all’, this document enables a healthcare

Whilst no AD DS design guidance can be a ‘one size fits
to simplify the design process, whilst allowing them to take local requirements into
organisation to simplify the design process, whilst allowing them to take local requirements into
to simplify the design process, whilst allowing them to take local requirements into
account. This will result in a reduction in diversity in
This will result in a reduction in diversity in AD DS design across the healthcare industry
thus aiding the supportability of the directory service
s through the standardisation and regulation of
thus aiding the supportability of the directory services through the standardisation and regulation of
implementations. In the future, it may be possible to further enhance these benefits through
implementations. In the future, it may be possible to further enhance these benefits through
implementations. In the future, it may be possible to further enhance these benefits through
will be able to establish
collaboration of services and service provision. Healthcare organisations will be able to establish
collaboration of services and service provision.
approaches to training and support of administration tasks required to maintain
common practice approaches to training and support of administration tasks required to maintain
approaches to training and support of administration tasks required to maintain
these directories.

healthcare industry,

healthcare organisation will implement a single domain

It is anticipated that each healthcare organisation
forest in the production environment. Additional single domain Active Directory
forest in the production environment. Additional single
production and test environments. For more information on Active
isolated networks as pre-production and test environments. For more information on Active
production and test environments. For more information on Active
Directory forests, see section 6.1.2

will implement a single domain Active Directory
 forests will exist on

6.1.2.

4.4  Scenarios

This section describes the following scenarios that are recommended as appropriate for the
This section describes the following scenarios that are recommended as appropriate for the
This section describes the following scenarios that are recommended as appropriate for the
application of this guidance:

(cid:1)  The infrastructure environment scenarios
The infrastructure environment scenarios

(cid:1)  The technology scenarios
The technology scenarios

4.4.1

Infrastructure Environment Scenarios
Infrastructure Environment

This section describes the key levels which are recommended as appropriate for the deployment of
This section describes the key levels which are recommended as appropriate for the deployment of
This section describes the key levels which are recommended as appropriate for the deployment of
and its associated network services.
AD DS and its associated network services.

Whilst Microsoft strongly recommends starting with a simple single forest Windows Server 2008 R2
Whilst Microsoft strongly recommends starting with a simple single forest Windows Server 2008 R2
Whilst Microsoft strongly recommends starting with a simple single forest Windows Server 2008 R2
it is not always possible due to the business requirements the directory structure
Active Directory it is not always possible due to the business requirements the directory structure
it is not always possible due to the business requirements the directory structure
needs to address.

In general, the reason why Microsoft recommends a simple single forest is to help ensure the
In general, the reason why Microsoft recommends a simple single forest is to help ensure the
In general, the reason why Microsoft recommends a simple single forest is to help ensure the
maximum return on investment and to minimise the long
term TCO of the service. In some cases
maximum return on investment and to minimise the long term TCO of the service.
where a number of individual healthcare organisations are part of a larger controlling body, there
where a number of individual healthcare organisations are part of a larger controlling body, there
where a number of individual healthcare organisations are part of a larger controlling body, there
would be an advantage in implementing a single Active Directory forest for the entire body.
would be an advantage in implementing a single Active Directory forest for the entire body.
would be an advantage in implementing a single Active Directory forest for the entire body.
However, while this may ultimately
that the individual healthcare organisations are sufficiently autonomous that operational and
that the individual healthcare organisations are sufficiently autonomous that operational and
that the individual healthcare organisations are sufficiently autonomous that operational and
political constraints render this unachievable.
political constraints render this unachievable.

ltimately be the most cost and management-effective goal,

effective goal, it could be

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 12

Prepared by Microsoft

(which forms the most cohesive
he current and most appropriate level at which to deploy AD DS (which forms the most cohesive
The current and most appropriate level at which to deploy
level. A single domain
financial, administrative and security unit) is at the healthcare organisation level. A single domain
financial, administrative and security unit) is at the
healthcare organisation level ensures that the forest acts as the local
ensures that the forest acts as the local
Active Directory forest at the healthcare organisation
authentication and authorisation directory security boundary for that entire
healthcare organisation.
authentication and authorisation directory security boundary for that entire healthcare organisation
This infrastructure enables clinicians and administrators to move around within their organisation,
This infrastructure enables clinicians and administrators to move around within their
This infrastructure enables clinicians and administrators to move around within their
etwork resources to deliver the care required, wherever it is needed.
utilising network resources to deliver the care required, wherever it is needed.

Healthcare organisations can range in size and functionality.

range in size and functionality. For example:

(cid:1)  A single site with a small number of users (up to 50)
ingle site with a small number of users (up to 50)

(cid:1)  An organisation spread over m

umber of users
An organisation spread over multiple locations with any number of users

(cid:1)  An organisation controlling

between one to three hospitals, each with approximately 2000
organisation controlling between one to three hospitals, each with approximately 2000

users, potentially a total of 6000 users across a few physical sites
users, potentially a total of 6000 users across a few physical sites

(cid:1)  An organisation controlling

An organisation controlling multiple General Practice clinics, each with, for examp
users at each of the multiple different physical sites, with a total of approximately 500 users
users at each of the multiple different physical sites, with a total of approximately 500 users
users at each of the multiple different physical sites, with a total of approximately 500 users
across these sites

, each with, for example, 20

(cid:1)  A central organisation which

A central organisation which provides IT services to multiple healthcare organisations
multiple healthcare organisations,
General Practice
normally within a defined geographical area, including hospitals and General Practice
normally within a defined geographical area
, as well as a number of administrative office locations
clinics, as well as a number of administrative office locations

The IT infrastructure and IT administration for these examples could be either a centralised or
The IT infrastructure and IT administration for these examples could be either a centralised or
The IT infrastructure and IT administration for these examples could be either a centralised or
distributed implementation scenario. The first, second a
nd third examples above would be classed
distributed implementation scenario. The first, second and third examples above would be classed
as centralised deployments of servers and administration. The fourth and fifth examples would be
as centralised deployments of servers and administration. The fourth and fifth examples would be
as centralised deployments of servers and administration. The fourth and fifth examples would be
classed as a distributed deployment, potentially hosting a server locally in a General Practice clinic
General Practice clinic
classed as a distributed deployment, potentially hosting a server locally in a
IT staff, whilst core control would be
certain levels of administration to the local non-IT staff, whilst core control would be
and delegating certain levels of administration to the local non
maintained by a central IT team.
maintained by a central IT team.

regardless of its size:
The following points are assumed for a healthcare organisation regardless of its size:
The following points are assumed for

(cid:1)  The organisation has the power to mandate IT so

lutions and the money to implement these
the power to mandate IT solutions and the money to implement these

solutions

(cid:1)  Each healthcare organisation

healthcare organisation has a single IT service provider who will own AD

rvice provider who will own AD DS

(cid:1)  Levels of network connection can potentially be controlled, such as ensuring that there is no
Levels of network connection can potentially be controlled, such as ensuring that there is no
Levels of network connection can potentially be controlled, such as ensuring that there is no
NAT8 in place within the organ
where it connects to external networks, such as the Internet)
where it connects to external networks, such as the Internet)

isation (NAT may exist at the boundaries of the network,
within the organisation (NAT may exist at the boundaries of the network,

8 For further information regarding the use of NAT, see section

For further information regarding the use of NAT, see section 2.5.

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 13

level, rather than
It is acknowledged that implementing AD DS at a healthcare organisation level, rather than
It is acknowledged that implementing
tory forest across a number of loosely affiliated
attempting to implement a single Active Directory forest across a number of loosely affiliated
attempting to implement a single Active Direc
introduce some limitations into the Directory Services design:
organisations, may introduce some limitations into the Directory Services design:
introduce some limitations into the Directory Services design:

Prepared by Microsoft

(cid:1)  There is no default Kerberos

authentication between forests if multiple healthcare

There is no default Kerberos9 authentication between forests if multiple
user roaming and resource sharing.
want to provide cross-organisation user roaming and resource sharing.
organisations want to provide cross
However, this is technically achievable with additional configuration and/or Microsoft
However, this is technically achievable with additional configuration and/or Microsoft
However, this is technically achievable with additional configuration and/or Microsoft
products such as Windows Server 2003 Active Directory Cross Forest Trust, and Windows
products such as Windows Server 2003 Active Directory Cross Forest Trust, and Windows
products such as Windows Server 2003 Active Directory Cross Forest Trust, and Windows
Server 2003 Active Directory Federation Services (AD FS)
Server 2003 Active Directory Feder

(cid:1)  A single global catalog (GC)

A single global catalog (GC)10 of objects (that is user accounts and their attributes, such as
of objects (that is user accounts and their attributes, such as
employee ID) would not exist within the healthcare organisation. However, this is technically
. However, this is technically
employee ID) would not exist within the
achievable with additional Microsoft products
, such as the Microsoft Identity and Integration
achievable with additional Microsoft products, such as the Microsoft Identity and Integration
Feature Pack (IIFP) and Microsoft Identity and Integration Server (MIIS)
Feature Pack (IIFP) and Microsoft Identity and Integration Server (MIIS)
Feature Pack (IIFP) and Microsoft Identity and Integration Server (MIIS)

(cid:1)  Healthcare organisation

boundaries may change in the future, requiring further technical
Healthcare organisation boundaries may change in the future, requiring further technical
effort to join, consolidate or divest AD DS
effort to join, consolidate or divest

in mind, it is important that each healthcare organisation assess

assesses the criteria
With these points in mind, it is important that each
design phases. It may be deemed more
within this guidance document during the initial AD DS design phases. It may be deemed more
within this guidance document during the initial
beneficial, from both a cost and technical perspective, to collaborate with other
beneficial, from both a cost and technical perspective,
organisations and thereby avoid
services and increasing the benefits of

the TCO for directory
avoid these constraints, ultimately reducing the TCO for directory

and increasing the benefits of AD DS.

rate with other healthcare

Up to this point, guidance has only been provided for implementing a single domain forest
Up to this point, guidance has only been provided for implementing a single domain forest within
Up to this point, guidance has only been provided for implementing a single domain forest
the production environment. It is expected that, in addition to the single production forest for each
the production environment. It is expected that, in addition to the single production forest for each
the production environment. It is expected that, in addition to the single production forest for each
an additional forest is implemented as a pre-production test environment
production test environment
healthcare organisation, an additional forest is implemented as a pre
ntation. Microsoft strongly recommends the use of
that is representative of the production implementation. Microsoft strongly recommends the use of
that is representative of the production impleme
a pre-production environment on an isolated network which mirrors the hardware and software
production environment on an isolated network which mirrors the hardware and software
production environment on an isolated network which mirrors the hardware and software
configuration of the live environment as far as possible. This should be used for final testing of
configuration of the live environment as far as possible. This should be used for final testing of
configuration of the live environment as far as possible. This should be used for final testing of
d patches before release to production. In addition, Microsoft recommends a
applications and patches before release to production. In addition, Microsoft recommends a
d patches before release to production. In addition, Microsoft recommends a
‘sandbox’ style test environment, either physically implemented or in a virtualised environment. This
‘sandbox’ style test environment, either physically implemented or in a virtualised environment. This
‘sandbox’ style test environment, either physically implemented or in a virtualised environment. This
should be used to perform tasks such as basic design proving and application t
should be used to perform tasks such as basic design proving and application testing, and should
should be used to perform tasks such as basic design proving and application t
be rebuilt as and when required. The remainder of this guidance focuses on the Active Directory
be rebuilt as and when required. The remainder of this guidance focuses on the Active Directory
be rebuilt as and when required. The remainder of this guidance focuses on the Active Directory
forest requirements for the production environment.
forest requirements for the production environment.

4.4.2

Technology Scenarios
Technology Scenarios

The core technology required by this guidance is Windows Server 2008
R2. Many of the features
The core technology required by this guidance is Windows Server 2008 R2. Many of the features
discussed in this guidance were also available in Windows Server 2008 which itself extended the
discussed in this guidance were also available in Windows Server 2008 which itself extended the
discussed in this guidance were also available in Windows Server 2008 which itself extended the
Where appropriate, Windows Server 2008 R2
technology provided by Windows Server 2003. Where appropriate, Windows Server 2008 R2
technology provided by Windows Server 2003
components will be discussed.
components will be discussed.

nts included as part of the Windows Server 2008 R2 installation DVD that are
Additional components included as part of the Windows Server 2008 R2 installation DVD that are
nts included as part of the Windows Server 2008 R2 installation DVD that are
required include:

(cid:1)  DNS service

(cid:1)  WINS

(cid:1)  Remote Server Administrative Tools (RSAT)
Remote Server Administrative Tools (RSAT)

(cid:1)  Security Configuration Wizard
Security Configuration Wizard

ation to services or databases; it
a security system that authenticates users. Kerberos does not provide authorisation to services or databases; it

9 Kerberos – a security system that authenticates user
establishes identity at logon, which is used throughout the session. The Kerberos protocol is the primary authentication
establishes identity at logon, which is used throughout the session. The Kerberos protocol is the primary authentication
establishes identity at logon, which is used throughout the session. The Kerberos protocol is the primary authentication
mechanism in the Windows 2000 and above

and above operating systems.

10 The global catalog contains a partial replica of every Windows Server 2003 domain in the Active Directory. This lets users
e global catalog contains a partial replica of every Windows Server 2003 domain in the Active Directory. This lets users
e global catalog contains a partial replica of every Windows Server 2003 domain in the Active Directory. This lets users
and applications find objects in an Active Directory domain tree, given one or more attributes of the target object without
and applications find objects in an Active Directory domain tree, given one or more attributes of the target object without
and applications find objects in an Active Directory domain tree, given one or more attributes of the target object without
ch domain holds them, and without requiring a contiguous extended namespace in the environment.
knowing which domain holds them, and without requiring a contiguous extended namespace in the environment.
ch domain holds them, and without requiring a contiguous extended namespace in the environment.

Page 14

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Prepared by Microsoft

In the past it was recommended to install the Windows Server support tools and Resource kit tools
In the past it was recommended to install the Windows Server support tools and Resource kit tools
In the past it was recommended to install the Windows Server support tools and Resource kit tools
but a strategic change incorporated into Windows Server 2008 was to eliminate these resources
but a strategic change incorporated into Windows Server 2008 was to eliminate these resources
but a strategic change incorporated into Windows Server 2008 was to eliminate these resources
itself. Additional Microsoft software
and to include all of the tools as part of the
and to include all of the tools as part of the Operating system itself. Additional Microsoft software
that is required and available for free download from the Internet includes:
that is required and available for free download from the Internet includes:

(cid:1)  Active Directory Management Pack

Management Pack11, if using Microsoft System Center Operations
, if using Microsoft System Center Operations

Manager

The hardware requirements are stated in the Windows Server 2008 R2 Build {R4
The hardware requirements are stated in the

R4}.

Note

Services mentioned within this section will not be available between
Services mentioned within this section will not be available between parts of a healthcare organisation
have identical IP Address schemes. The use of NAT as a workaround between such
have identical IP Address schemes
organisation within an AD DS

uch parts of the
nvironment is neither recommended nor supported by Microsoft.
DS environment is neither recommended nor supported by Microsoft.

parts of a healthcare organisation that

, and the Microsoft
For further information please read the Assumptions statement in section 2.5, and the Microsoft
For further information please read the Assumptions statement in section
whitepaper Active Directory in Networks Segmented by Firewalls

Active Directory in Networks Segmented by Firewalls12.

Active Directory Management Pack for Operations Manager 2007 {R8}:

11 Active Directory Management Pack for Operations Manager 2007
http://www.microsoft.com/downloads/details.aspx
http://www.microsoft.com/downloads/details.aspx?FamilyId=008F58A6-DC67-4E59-95C6-
D7C7C34A1447&amp;displaylang=en&displaylang=en
D7C7C34A1447&amp;displaylang=en&displaylang=en

Active Directory in Networks Segmented by Firewalls {R10}:

12 Active Directory in Networks Segmented by Firewalls
a9166368434e&DisplayLang=en
http://www.microsoft.com/downloads/details.aspx?FamilyID=c2ef3846-43f0-4caf-9767-a9166368434e&DisplayLang=en
http://www.microsoft.com/downloads/deta

Page 15

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Prepared by Microsoft

5

PLAN

The Plan phase is where the bulk of the implementation planning is completed. During this phase,
The Plan phase is where the bulk of the implementation planning is completed. During this phase,
The Plan phase is where the bulk of the implementation planning is completed. During this phase,
the areas for further analysis are identified and a design process commences.
the areas for further analysis are identified a

level checklist, illustrating the sequence of events that the IT Manager and
Figure 5 acts as a high-level checklist, illustrating the sequence of events that the IT Manager and
level checklist, illustrating the sequence of events that the IT Manager and
IT Architect need to perform when planning for deployment of
organisation:

ithin a healthcare
when planning for deployment of AD DS within a healthcare

Design
Figure 5: Sequence for Planning an AD DS Design

design, all IT
It is vital that, before embarking on the Windows Server 2008 R2 AD DS design, all IT
It is vital that, before embarking on the Windows Server 2008 R2
have a thorough understanding, at architectural level, of how AD DS can be
have a thorough understanding, at architectural level, of how
Professionals involved have a thorough understanding, at architectural level, of how
used to provide a directory services solution specifically for their healthcare organisation
used to provide a directory services solution specifically for their

healthcare organisation.

best practices and architectural
eb site for up to date product information, guidance on best practices and architectural

guidance in this document, it is important to frequently visit the Microsoft
guidance in this document, it is important to frequently visi
In addition to the AD DS guidance in this document, it is important to frequently visi
web site for up to date product information, guidance
, where features and technology have not changed since the
information. It should be noted that, where features and technology have not changed since the
information. It should be noted that
Windows Server 2003 release, the documentation has not been updated.
Windows Server 2003 release, the documentation has not

(cid:1)  Active Directory Best practices

Active Directory Best practices13 (Windows Server 2003)

(cid:1)  DNS best practices14 (Windows Server 2003)
Windows Server 2003)

15
(cid:1)  WINS Best Practices15

5.1  Review Planning an

Review Planning an AD DS Deployment Project

, it is important to become familiar
Before beginning to plan the Windows Server 2008 R2 AD DS, it is important to become familiar
Before beginning to plan the Windows Server 2008 R2
related terms that are required during
deployment project cycle, as well as AD DS related terms that are required during
with the AD DS deployment project cycle, as well as
the project process.

13 Active Directory Best practices {R11
a61e733579301033.mspx?mfr=true
http://technet2.microsoft.com/WindowsServer/en/library/5712b108-176a-4592-bcde-a61e733579301033.mspx?mfr=true
 http://technet2.microsoft.com/WindowsServer/en/library/5712b108

R11}:

14 DNS best practices {R12}:
c73db47398a21033.mspx
http://technet2.microsoft.com/windowsserver/en/library/59d7a747-48dc-42cc-8986-c73db47398a21033.mspx
 http://technet2.microsoft.com/windowsserver/en/library/59d7a747

15 WINS Best Practices {R13}:
a2fc52886ed71033.mspx
http://technet2.microsoft.com/windowsserver/en/library/ed9beba0-f998-47d2-8137-a2fc52886ed71033.mspx
 http://technet2.microsoft.com/windowsserver/en/library/ed9beba0

Page 16

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Prepared by Microsoft

5.1.1  Review the AD

 DS Deployment Project Cycle

An AD DS deployment project involves six key phases.
the phases of the project cycle, relative to the lifetime of the deployment project.
the phases of the project cycle, relative to the lifetime of the deployment project.
the phases of the project cycle, relative to the lifetime of the deployment project.

shows the relationship between
deployment project involves six key phases. Figure 6 shows the relationship between

nderstand the interaction between the subsequent
During the Planning phase, it is important to understand the interaction between the subsequent
During the Planning phase, it is important to u
phases for project planning purposes. In the Developing phase, a design for Active Directory that
phases for project planning purposes. In the Developing phase, a design for Active Directory that
phases for project planning purposes. In the Developing phase, a design for Active Directory that
that will be using the directory service should
healthcare organisation that will be using the directory service should
best meets the needs of the healthcare organisation
be created. After the design is approved, the design should be stabilised by testing it in a lab
d. After the design is approved, the design should be stabilised by testing it in a lab
d. After the design is approved, the design should be stabilised by testing it in a lab
environment and then implementing the final design in the production environment.
environment and then implementing the final design in the production environment.
environment and then implementing the final design in the production environment.

As testing is typically performed by those that would deploy the Active Directory, and
As testing is typically performed by those that would deploy the Active Directory, and it could
As testing is typically performed by those that would deploy the Active Directory, and
potentially affect the designing phase, it is an interim activity that overlaps both design and
potentially affect the designing phase, it is an interim activity that overlaps both design and
potentially affect the designing phase, it is an interim activity that overlaps both design and
deployment. When the deployment is complete, the Active Directory service becomes the
deployment. When the deployment is complete, the Active Directory service becomes the
deployment. When the deployment is complete, the Active Directory service becomes the
responsibility of those that will carry out the day
ities of maintaining it. Lab testing and
responsibility of those that will carry out the day-to-day activities of maintaining it. Lab testing and
the implementation of a pilot program should continue throughout the lifetime of the deployment.
the implementation of a pilot program should continue throughout the lifetime of the deployment.
the implementation of a pilot program should continue throughout the lifetime of the deployment.

Figure 6: AD DS Deployment Project Phases

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 17

Prepared by Microsoft

Terms and Definitions
5.1.2  Review AD DS Terms and Definitions

t to ensure that certain terms and definitions referred to in this guidance are
It is important to ensure that certain terms and definitions referred to in this guidance are
t to ensure that certain terms and definitions referred to in this guidance are
understood when designing an AD DS deployment process. Table 2 details the most import
understood when designing an
these.

details the most important of

Term

Definition

AD DS domain(Active Directory
domain)

An administrative unit in a computer network which groups capabilities together for
An administrative unit in a computer network which groups capabilities together for
wide user identity, authentication, trust
management convenience, such as network-wide user identity, authentication, trust
relationships, policy administration and replication.

AD DS forest (Active Directory forest)

A collection of one or more Active Directory domains that share the same directory schema
A collection of one or more Active Directory domains that share the same directory schema
and a common logical configuration structure. It also includes automatic transitive trust
and a common logical configuration structure. It also includes automatic transitive trust
relationships between domains in the forest so that any object in one domain can be granted
relationships between domains in the forest so that any object in one domain
access to resources in any domain in the forest. The forest is also the security boundary for
access to resources in any domain in the forest. The forest is also the security boundary for
an AD DS instance.

AD DS functional level (Active
Directory functional level)

feature which can be enabled through a
An advanced domain-wide or forest-wide AD DS feature which can be e
. Typically the functional levels enable specific
setting in Windows Server 2008 R2 AD DS. Typically the functional levels enable specific
operating system version.
features that rely on all domain controllers being at a minimum operating system

Migration

The process of moving an object from a source domain to a target domain. This process
domain to a target domain. This process
involves either preserving or modifying properties of the object to ensure it is accessible in the
involves either preserving or modifying properties of the object to ensure it is accessible in the
target domain.

Domain restructure

A migration process that involves changing the domain structure of a forest.
A migration process that involves changing the domain structure of a forest.

Domain consolidation

A restructuring process which involves merging the contents of one domain with another
A restructuring process which involves merging the contents of one domain with another
domain in order to reduce the overall number of domains in use.

Domain upgrade

The process of upgrading the directory service of a domain to a later version.
The process of upgrading the directory service of a domain to a later

In-place domain upgrade

This process involves an upgrade of the operating system on all domain controller
domain objects remain in place.

domain controllers while all

Regional domain

A child domain that is created based on a geographic region in order to optimise replication
A child domain that is created based on a geographic region in order to optimise
traffic.

Important Terms and Definitions
Table 2: Windows Server 2008 R2 AD DS Important Terms and Definitions

5.2  Determine the AD

Design, Test and Deployment Strategy
AD DS Design, Test and Deployment Strategy

strategy required will vary according to the healthcare organis
The level of AD DS strategy required will vary according to the
network configuration. The guidance presented within this document is focused on the components
network configuration. The guidance presented within this document is focused on the components
network configuration. The guidance presented within this document is focused on the components
, rather than looking at upgrading or restructuring an existing
required for a new AD DS, rather than looking at upgrading or restructuring an existing
, rather than looking at upgrading or restructuring an existing
owever some of these concepts overlap.
implementation. However some of these concepts overlap.

healthcare organisation’s existing

Note

Microsoft has produced the Active Directory Migration Guide
. This guidance can be used in conjunction with this
migration to Windows Server 2003 Active Directory
Windows Server 2003 Active Directory. This guidance can be used in conjuncti
estigating the restructuring of an existing implementation.
document to aid a healthcare organisation investigating the restructuring of an existing implementation.
document to aid a healthcare organisation

Deliverable which provides guidance on the
Active Directory Migration Guide Deliverable which provides guidance on the

The AD DS design and testing requirements are expanded further in sections
technical references and relevant healthcare organisation design decisions where app
technical references and relevant

design and testing requirements are expanded further in sections 6

6 and 7 detailed
design decisions where appropriate.

Design Requirements
5.2.1  AD DS Design Requirements

identifies the most important aspects which require understanding and

and planning when

for a more detailed breakdown of
a healthcare organisation. See section 6 for a more detailed breakdown of

Table 3 identifies the most important aspe
designing AD DS for a healthcare organi
these components.

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 18

AD DS Design Component

Logical Structure
Designing an AD DS Logical Structure

Identify the Deployment Project Participants
Identify the Deployment Project Participants

Create a Forest Design

Create a Domain Design for Each Forest
Create a Domain Design for Each Forest

Design the OU Structure for Each Domain
Design the OU Structure for Each Domain

Prepare to Enable Advanced Features via Functional Levels
Prepare to Enable Advanced Features via Functional Levels

Active Directory Trust Design

AD DS Naming Standards

Design an AD DS Physical Structure

Collect Network Information

Domain Controller Placement

Operations Master Role Placement
Operations Master Role Placement

Create a Site Design

Create a Site Link Design

Create a Site Link Bridge Design
Create a Site Link Bridge Design

Hardware Availability and Scalability Requirements
Domain Controller Hardware Availability and Scalability Requirements

Designing for AD DS Security

Environment
Plan a Secure AD DS Environment

Design an Authentication Strategy
Design an Authentication Strategy

Design a Resource Authorisation Strategy
Design a Resource Authorisation Strategy

Design a Public Key Infrastructure (PKI)
Design a Public Key Infrastructure (PKI)

Designing Network Services to Support AD DS
Designing Network Services to Support

DNS Infrastructure to Support AD DS
DNS Infrastructure to Support

WINS Infrastructure to Support AD DS
WINS Infrastructure to Support

Additional Network Services

Table 3: AD DS Design Components

Prepared by Microsoft

Section Number for Further Detail
Section Number for Further Detail

6.1

6.1.1

6.1.2

6.1.3

6.1.4

6.1.5

6.1.6

6.1.7

6.2

6.2.1

6.2.2

6.2.3

6.2.4

6.2.5

6.2.6

6.2.7

6.3

6.3.1

6.3.2

6.3.3

6.3.4

6.4

6.4.1

6.4.2

6.4.3

design components are planned for whilst scoping the project, such
It is important that the AD DS design components are planned for whilst scoping the project, such
design components are planned for whilst scoping the project, such
design is essential to
that they are included in the Build phase. Thoroughly planning the AD DS design is essential to
that they are included in the Build phase. Thoroughly planning the
ensure a secure, stable and cost-effective deployment.
ensure a secure, stable and cost

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 19

Testing Requirements
5.2.2  AD DS Testing Requirements

Prepared by Microsoft

identifies the most important aspects that require understanding and planning

planning when testing
a more detailed breakdown of
for a healthcare organisation. See section 7 for a more detailed breakdown of

Table 4 identifies the most important aspects
and verifying AD DS for a healthcare organisation
these components.

AD DS Testing Component

Design a Test Environment

Create a Test Plan

Develop the Test Lab

Design the Test Cases

Conduct the Tests

Design a Pilot Environment

Create a Pilot Plan

Deploy and Test the Pilot

Evaluate the Pilot

Prepare for Production Deployment

Table 4: AD DS Testing Components

Deployment Requirements
5.2.3  AD DS Deployment Requirements

Section Number for Further Detail
Section Number for Further Detail

7.1

7.1.2

7.1.5

7.1.6

7.1.7

7.2

7.2.2

7.2.4

7.2.5

7.3

identifies the most important aspects which require understanding and planning

Table 5 identifies the most important aspects which require understanding
deploying AD DS for a healthcare organisation
these components.

for a more detailed breakdown of
a healthcare organisation. See section 8 for a more detailed breakdown of

and planning when

Deployment Component
AD DS Deployment Component

Section Number for Further Detail
Section Number for Further Detail

AD DS Deployment Prerequisites

AD DS Deployment Strategy

Active Directory Forest Root Domain Deployment
Active Directory Forest Root Domain Deployment

Raise the Functional Level

Deploy a Domain Controller

Test the Installation of AD DS

Configure AD DS

Table 5: AD DS Deployment Components

8.1

8.2

8.2.1

8.2.2

8.3

8.4

8.5

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 20

Prepared by Microsoft

6  DEVELOP

During the Develop phase the solution components are built based on the planning and designs
During the Develop phase the solution components are built based on the planning and designs
During the Develop phase the solution components are built based on the planning and designs
phases. Further refinement of these components will continue into the
completed during the earlier phases. Further refinement of these components will continue into the
phases. Further refinement of these components will continue into the
stabilisation phase.

The Develop phase has been structured into four major components, for which design decisions
The Develop phase has been structured into four major components, for which design decisions
The Develop phase has been structured into four major components, for which design decisions
are required for an Active Directory service.
are required for an Active Directory service.

evel checklist, illustrating the sequence of these components that the IT
Figure 7 acts as a high-level checklist, illustrating the sequence of these components that the IT
evel checklist, illustrating the sequence of these components that the IT
Manager and IT Architect need to determine when planning for AD DS deployment within
Manager and IT Architect need to determine when planning for
healthcare organisation:

deployment within a

irectory Design
Figure 7: Sequence for Building an Active Directory Design

The aim of the Develop phase is to provide a structured synopsis of these major components, with
The aim of the Develop phase is to provide a structured synopsis of these major components, with
The aim of the Develop phase is to provide a structured synopsis of these major components, with
each component being broken down into why it is important, determine what its critical aspects are,
each component being broken down into why it is important, determine what its critical aspects are,
each component being broken down into why it is important, determine what its critical aspects are,
and also identify for these what key design decisions are required for the healthcare organisation
and also identify for these what key design

the healthcare organisation.

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 21

Prepared by Microsoft

components, job aids are available in the Windows Server 2003
 components, job aids are available in the Windows Server 2003

For many of the major AD DS
Deployment Kit, comprising of worksheets that can help an IT professional document design
Deployment Kit, comprising of worksheets that can help an IT professional document design
Deployment Kit, comprising of worksheets that can help an IT professional document design
decisions and create subsequent deployment plans. There are currently no such similar job aids for
e subsequent deployment plans. There are currently no such similar job aids for
e subsequent deployment plans. There are currently no such similar job aids for
Windows Server 2008 R2 although the Windows Server 2003 Deployment kit aids could be used in
Windows Server 2008 R2 although the Windows Server 2003 Deployment kit aids could be used in
Windows Server 2008 R2 although the Windows Server 2003 Deployment kit aids could be used in
conjunction with the documented Windows Server 2008 AD DS Deployment Guide
conjunction with the documented Windows Server 2008
specific job aid filenames have been referenced in the relevant sections of this guidance and can
specific job aid filenames have been referenced in the relevant sections of this guidance and can
specific job aid filenames have been referenced in the relevant sections of this guidance and can
be downloaded from the Microsoft Download Center16.
be downloaded from the Microsoft Download

Deployment Guide {R33}. The

Information

In section 4.4.1, various implementation scenarios and infrastructure environments were identified. Where
, various implementation scenarios and infrastructure environments were identified. Where
, various implementation scenarios and infrastructure environments were identified. Where
possible, throughout this section, the recommended design decisions will be identified, allowing
possible, throughout this section, the recommended design decisions will be identified, allowing
possible, throughout this section, the recommended design decisions will be identified, allowing
healthcare organisations to map these to their environment, and therefore reduce the amount of time
to map these to their environment, and therefore reduce the amount of time
to map these to their environment, and therefore reduce the amount of time
design. It is recommended that these are used in conjunction with the
DS design. It is recommended that these are used in conjunction with the
required to produce the AD DS
Windows Server 2003 Deployment Kit job aids.
Windows Server 2003 Deployment Kit job aids

6.1  Design the AD DS

DS Logical Structure

logical structure involves defining the structure of, and relationships between,
Designing an AD DS logical structure involves defining the structure of, and relationships between,
logical structure involves defining the structure of, and relationships between,
the forests, domains, and OUs that require deployment.
the forests, domains, and OUs that require deployment.

Careful designing of the AD DS

logical structure provides the following benefits:
DS logical structure provides the following benefits:

(cid:1)  Ensures that the time and effort required to implement

in the live environment is
Ensures that the time and effort required to implement AD DS in the live environment is
minimised

(cid:1)  Allows an efficient structure to be designed that best meets the

health organisation’s
Allows an efficient structure to be designed that best meets the health organisation’s
administrative requirements
administrative requirements

(cid:2)  Simplifies the management of the Windows ne
tworks that may contain large numbers of
Simplifies the management of the Windows networks that may contain large numbers of
objects, such as users, computers and groups
objects, such as users, computers and groups

(cid:2)  Consolidates the domain structure and

administration costs
Consolidates the domain structure and reduces administration costs

(cid:2)  Provides the ability to delegate administrative control over resources, as appropriate
Provides the ability to delegate administrative control over resources, as appropriate
Provides the ability to delegate administrative control over resources, as appropriate

(cid:1)  Reduces impact on network bandwidth
n network bandwidth

(cid:1)  Simplifies resource sharing
Simplifies resource sharing

(cid:1)  Optimises search performance
Optimises search performance

(cid:1)  Lowers TCO

logical structure facilitates the efficient integration of features such as
A well-designed AD DS logical structure facilitates the efficient integration of features such as
logical structure facilitates the efficient integration of features such as
Group Policy, enabling desktop lockdown, software distribution, and th
e administration of users,
Group Policy, enabling desktop lockdown, software distribution, and the administration of users,
groups, workstations, and servers, into the infrastructure environment. In addition, a carefully
groups, workstations, and servers, into the infrastructure environment. In addition, a carefully
groups, workstations, and servers, into the infrastructure environment. In addition, a carefully
designed logical structure facilitates the integration of other services, such as PKI for added
designed logical structure facilitates the integration of other services, such as PKI for added
designed logical structure facilitates the integration of other services, such as PKI for added
security, and domain-based Distribut

ed File System (DFS) for file collaboration.
based Distributed File System (DFS) for file collaboration.

Job Aids for Windows Server 2003 Deployment Kit {R14}:

16 Job Aids for Windows Server 2003 Deployment Kit
607a58fc81f0&DisplayLang=en
http://www.microsoft.com/downloads/details.aspx?FamilyID=edabb894-4290-406c-87d1-607a58fc81f0&DisplayLang=en
http://www.microsoft.com/downloads/details.aspx?FamilyID=edabb894

Page 22

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Prepared by Microsoft

6.1.1

Identify the Deployment Project Participants
Identify the Deployment Project Participants

6.1.1.1

Determine Project Specific Roles
Determine Project Specific Roles

Specific roles during an AD DS
Sponsor, IT Architect, IT Manager and IT Professionals.
Sponsor, IT Architect, IT Manager and IT

DS design should be identified. The key roles17 include Executive
include Executive

, the number of individuals that need to take
Depending upon the size of the healthcare organisation, the number of individuals that need to take
Depending upon the size of the
may require several individuals to get
part in the project will vary; large healthcare organisations may require several individuals to get
part in the project will vary; large
involved, whilst smaller healthcare org
multiple project roles, such as the IT Architect and the IT Manager. The roles of the IT
multiple project roles, such as the IT Architect and the IT Manager. The roles of the IT
multiple project roles, such as the IT Architect and the IT Manager. The roles of the IT
Professionals design team and the deployment team may also overlap depending upon the size of
Professionals design team and the deployment team may also overlap depending upon the size of
Professionals design team and the deployment team may also overlap depending upon the size of
nd number of resources available.
the organisation and number of resources available.

may only require a couple of resources with
healthcare organisations may only require a couple of resources with

The established design team that is required to begin the forest planning and deployment process
The established design team that is required to begin the forest planning and deployment process
The established design team that is required to begin the forest planning and deployment process
should include IT professionals who are familiar with the existing network, the potential forest
should include IT professionals who are familiar with the existing network, the potential forest
should include IT professionals who are familiar with the existing network, the potential forest
manage the corporate namespace, and the owners and administrators
owners, the individuals who manage the corporate namespace, and the owners and administrators
manage the corporate namespace, and the owners and administrators
AD DS after the deployment project is complete.
who will be responsible for AD

6.1.1.2

Establish Owners and Administrators
Establish Owners and Administrators

are established for the following roles in
Ensure that service owners and administrators {R15} are established for the following roles in
Ensure that service owners and administrators
AD DS:

(cid:1)  Service and Data owners for

Service and Data owners for AD DS

The service owners are those who are responsible for planning and managing AD DS,
The service owners are those who are responsible for planning and managing
The service owners are those who are responsible for planning and managing
cture and ensuring the service availability. The data owners are
defining the forest structure and ensuring the service availability. The data owners are
cture and ensuring the service availability. The data owners are
those who are responsible for the data stored in AD DS. For example, IT Manager roles
. For example, IT Manager roles
those who are responsible for the data stored in
DNS owner, the site topology owner, and the
which include the forest owner, the AD DS DNS owner, the site topology owner, and the
which include the forest owner, the
OU owner.

(cid:1)  Service and Data Administrators for

nd Data Administrators for AD DS

The service administrators are those who have been delegated the privilege to implement
The service administrators are those who have been delegated the privilege to implement
The service administrators are those who have been delegated the privilege to implement
decisions or design changes defined by the service owners and who are trusted to manage
decisions or design changes defined by the service owners and who are trusted to manage
decisions or design changes defined by the service owners and who are trusted to manage
s are those who have been delegated the
day basis. Data administrators are those who have been delegated the
AD DS on a day-to-day basis. Data administrator
permissions to update, create or delete specific data stored within
to update, create or delete specific data stored within AD DS
modifying the properties of user objects. For example, IT Administrators responsible for
modifying the properties of user objects. For example, IT Administrators responsible for
modifying the properties of user objects. For example, IT Administrators responsible for
ofessionals responsible for the data
retaining service control of AD DS, and IT Professionals responsible for the data
retaining service control of
DS objects such as users and groups.
administration of AD DS

DS such as

As with the project specific roles, the owners and administrators in larger healthcare organisations
healthcare organisations
As with the project specific roles, the owners and administrators in larger
ay be responsible for
may be different individuals, whereas in smaller organisations, individuals may be responsible for
may be different individuals, whereas in smaller
multiple roles.

6.1.1.3

Document the Project Teams
Document the Project Teams

Once the participants of the project have been defined, the names and roles should be
Once the participants of the project have been defined, the names and roles should be
Once the participants of the project have been defined, the names and roles should be
documented. It is advised that this is done using the Design and Deployment Team Informa
documented. It is advised that this is done using the
aid document, named DSSLOGI_1.doc

DSSLOGI_1.doc {R14}.

Design and Deployment Team Information job

Identifying the deployment Project Participants {R15}:

17 Identifying the deployment Project Participants
us/library/cc732532(WS.10).aspx
http://technet.microsoft.com/en-us/library/cc732532(WS.10).aspx

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 23

Prepared by Microsoft

Recommendation

The use of the job aids available in the Windows Server 2003 Deployment Kit
The use of the job aids available in the Windows Server 2003 Deployment Kit {R14}
recommended as they can aid a healthcare organisation in quickly documenting the design decisions
in quickly documenting the design decisions
recommended as they can aid a
rticularly if the IT professionals involved are not experienced in
made throughout the AD DS design, pa
design, particularly if the IT professionals involved are not experienced in
creating complex detailed design documents.
creating complex detailed design documents.

} is highly

Create a Forest Design
6.1.2  Create a Forest Design

Creating a forest design involves identifying the groups within the healthcare organisation
Creating a forest design involves identifying the groups within the
the resources available to host an
and then determining the number of forests required in order to meet these requirements.
and then determining the number of forests required in order to meet these requirements.
and then determining the number of forests required in order to meet these requirements.

forest, defining the forest design requirements,
ble to host an Active Directory forest, defining the forest design requirements,

healthcare organisation that have

6.1.2.1

Identify Groups able to Host an Active Directory Forest
Identify Groups able to Host an Active Directory Forest
Identify Groups able to Host an Active Directory Forest

Prior to understanding whether
a multiple forest design within a single organisation is required, it
Prior to understanding whether a multiple forest design within a single organisation is required, it
must be first ascertained whether the various groups within the organisation that will host and
must be first ascertained whether the various groups within the organisation that will host and
must be first ascertained whether the various groups within the organisation that will host and
administer an Active Directory forest have the financial and human resources available to do so. If
administer an Active Directory forest have the financial and human resources available to
administer an Active Directory forest have the financial and human resources available to
a group does not have these resources available, it will not be possible to implement a multiple
a group does not have these resources available, it will not be possible to implement a multiple
a group does not have these resources available, it will not be possible to implement a multiple
forest design.

6.1.2.2

Identify the Forest Design Requirements
Identify the Forest Design Requirements

Whilst Microsoft strongly recommends in public documentation to start with a simple single forest
Whilst Microsoft strongly recommends in public documentation to start with a simple single fo
Whilst Microsoft strongly recommends in public documentation to start with a simple single fo
Windows Server 2008 R2 AD DS
be required. This section highlights some of these key factors and the resultant
be required. This section highlights some of these key factors and the r
organisation will be required. This section highlights some of these key factors and the r
recommendations for a healthcare organisation.
recommendations for a healthcare organisation

multiple forest designs within a single
DS, there are situations where multiple forest designs within a single

Recommendation

It is recommended that where possible a single Active Directory forest is implemented at the healthcare
It is recommended that where possible a single Active Directory forest is implemented at the
It is recommended that where possible a single Active Directory forest is implemented at the
level for the production environment, therefore following the organisational forest model18.
level for the production environment, therefore following the organisational forest model
organisation level for the production environment, therefore following the organisational forest model

at the directory structure needs to accommodate involves
Identifying the business requirements that the directory structure needs to accommodate involves
Identifying the business requirements th
need to manage their
determining how much autonomy the groups in the healthcare organisation need to manage their
determining how much autonomy the groups in the
network resources, and whether each group needs to isolate their resources on the network from
network resources, and whether each group needs to isolate their resources on the network from
network resources, and whether each group needs to isolate their resources on the network from
other groups.

investigating to help identify
The three critical types of business requirements that need thoroughly investigating to help identify
The three critical types of business requirements that need
forest design requirements are:
the Active Directory forest design requirements are:

(cid:1)  Organisational structure requirements
Organisational structure requirements

(cid:1)  Operational requirements
Operational requirements

(cid:1)  Legal requirements

identifying the forest design requirements19 involves identifying the degree to which groups
involves identifying the degree to which groups
can trust the potential forest owners and their service administrators,
 can trust the potential forest owners and their service administrators,

Part of identifying the forest design requirements
in the healthcare organisation
healthcare
and identifying the autonomy and isolation requirements for each group in the healthcare
and identifying the autonomy and isolation requirements for e
organisation.

18 Forest Design Models {R16}:
us/library/cc770439(WS.10).aspx
http://technet.microsoft.com/en-us/library/cc770439(WS.10).aspx

Identifying Forest Design Requirements {R17}:

19 Identifying Forest Design Requirements
http://technet.microsoft.com/en-us/library/cc730924(WS.10).aspx

us/library/cc730924(WS.10).aspx

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 24

Prepared by Microsoft

During the forest design process, it is important to identify who are the AD DS administrators
During the forest design process, it is important to identify who are the
what their scope of authority will be, as this will help determine forest security boundaries.
what their scope of authority will be, as this will help determine forest security boundaries.
what their scope of authority will be, as this will help determine forest security boundaries.

administrators20 and

Recommendations
(cid:1)  There should be a strict division of service and data administration within
DS
ere should be a strict division of service and data administration within AD DS
(cid:1)  There should be as few ‘service’ administrators as possible, all of whom are highly trusted
There should be as few ‘service’ administrators as possible, all of whom are highly trusted
There should be as few ‘service’ administrators as possible, all of whom are highly trusted
(cid:1)  All other AD DS tasks should be related to ‘data’ based administration, and delegated out
tasks should be related to ‘data’ based administration, and delegated out
tasks should be related to ‘data’ based administration, and delegated out
appropriately on the principle of ‘Least Privilege’, thus helping to maximise security
appropriately on the principle of ‘Least Privilege’, thus helping to maximise security
appropriately on the principle of ‘Least Privilege’, thus helping to maximise security

(cid:1)  Additional forests should only be considered if there is a requirement to isolate or provide c
Additional forests should only be considered if there is a requirement to isolate or provide complete
Additional forests should only be considered if there is a requirement to isolate or provide c
autonomy for the service owners or system administrators of a particular section in a directory service
autonomy for the service owners or system administrators of a particular section in a directory service
autonomy for the service owners or system administrators of a particular section in a directory service

Once the forest design requirements regarding data, service, autonomy and isolation
Once the forest design requirements regarding data, service, autonomy and isolation
Once the forest design requirements regarding data, service, autonomy and isolation
It is advised that this is done using
considerations have been defined, they should be documented. It is advised that this is done using
considerations have been defined, they should be documented.
R14}.
the Forest Design Requirements

Forest Design Requirements job aid document, named DSSLOGI_2.doc {R14

Note

entified additional requirements, a simple single forest design
If no groups within the organisation have identified additional requirements, a simple single forest design
If no groups within the organisation have id
will be suitable for the healthcare organisation

healthcare organisation.

6.1.2.3

Determine the Number of Forests
Determine the Number of Forests

If a simple single forest design is not suitable due to the identification of additional requirements, it
If a simple single forest design is not suitable due to the identification of additional requirements, it
If a simple single forest design is not suitable due to the identification of additional requirements, it
ecessary to determine the forest design model and the number of forests needed. Current best
ecessary to determine the forest design model and the number of forests needed. Current best
is necessary to determine the forest design model and the number of forests needed. Current best
practice forest design models21

21 that can be identified include:

(cid:1)  Organisational forest model
Organisational forest model

User accounts and resources are contained in the forest and managed independently.
User accounts and resources are contained in the forest and managed inde
User accounts and resources are contained in the forest and managed inde

(cid:1)  Resource forest model
Resource forest model

A separate forest is used to manage resources.
A separate forest is used to manage resources

(cid:1)  Restricted access forest model
estricted access forest model

A separate forest is created to contain user accounts and data that must be isolated from
A separate forest is created to contain user accounts and data that must be isolated from
A separate forest is created to contain user accounts and data that must be isolated from
healthcare organisation.
the rest of the healthcare organisation.

(cid:1)  Impending divestiture
divestiture

A separate forest is recommended to accommodate users and services for the elements of
services for the elements of
A separate forest is recommended to accommodate users and
that will be separated out into a separate organisation in the near
a healthcare organisation
healthcare organisation that will be separated out into a separate organisation in the near
future. Although this creates extra work it makes the separatio
n much easier as the forest
future. Although this creates extra work it makes the separation much easier as the forest
can be separated and there is no need to perform a migration of the affected users and
can be separated and there is no need to perform a migration of the affected users and
can be separated and there is no need to perform a migration of the affected users and
applications out of the health organisation’s AD DS.
applications out of the

Once the number of forests has been defined, it should be documented. It is advised that this is
Once the number of forests has been defined, it should be documented. It is advised that this is
Once the number of forests has been defined, it should be documented. It is advised that this is
done using the Forest Design job aid document, named
an example of a simple record of the design decisions made, taking into account the
an example of a simple record of the design decisions made, taking into account the
an example of a simple record of the design decisions made, taking into account the
recommendation of a single forest for a

 job aid document, named DSSLOGI_3.doc {R14}

of a single forest for a healthcare organisation.

}. Table 6 provides

Service Administrator Scope of Authority {R18}:

20 Service Administrator Scope of Authority
us/library/cc772268(WS.10).aspx
http://technet.microsoft.com/en-us/library/cc772268(WS.10).aspx

21 Forest Design Models {R19}:
us/library/cc770439(WS.10).aspx
http://technet.microsoft.com/en-us/library/cc770439(WS.10).aspx

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 25

Prepared by Microsoft

Group Name

Contact
Contact

Forest Type

Requirements
Requirements

Health Organisation Group IT

IT Architect Name
IT Architect Name

Organisational

Email

Phone

A single forest created for the
A single forest created for the
entire
entire organisation. All groups
within the organisation will use
within the organisation will use
this forest.
this forest.

: Example Completed Job Aid for Forest Design
Table 6: Example Completed Job Aid for Forest Design

Create a Domain Design for Each Forest
6.1.3  Create a Domain Design for Each Forest

The forest owner is responsible for creating a domain design for the forest. Creating a domain
The forest owner is responsible for creating a domain design for the forest. Creating a domain
The forest owner is responsible for creating a domain design for the forest. Creating a domain
design involves examining the replication requirements and the existing capacity of the network
s and the existing capacity of the network
design involves examining the replication requirement
to function in the most
infrastructure, and then building a domain structure that enables AD DS to function in the most
infrastructure, and then building a domain structure that enables
efficient way.

6.1.3.1

Review the Domain Models
Review the Domain Models

design should start with a single domain and forest design in the
It is advised that any AD DS design should start with a single domain and forest design in the
design should start with a single domain and forest design in the
production environment to maintain management simplicity and ensure lowest possible TCO. In a
production environment to maintain management simplicity and ensure lowest possible TCO. In a
production environment to maintain management simplicity and ensure lowest possible TCO. In a
single domain design, all information is replicated to all of the
single domain design, all information is replicated to all of the domain controllers
Windows Server 2008 R2 has further reduced the reasons for needing separate domains in a forest
Windows Server 2008 R2 has further reduced the reasons for needing separate domains in a forest
Windows Server 2008 R2 has further reduced the reasons for needing separate domains in a forest
leaving a small set of specific reasons for multiple domains.
leaving a small set of specific reasons for multiple domains.

domain controllers. The release of

There are justifiable reasons for having multiple domain model designs within a forest. The
There are justifiable reasons for having multiple domain model designs within a forest. The
There are justifiable reasons for having multiple domain model designs within a forest. The
following factors will impact this decision:
following factors will impact this decision:

(cid:1)  The amount of available bandwidth capacity on the network that is able to be allocated to
The amount of available bandwidth capacity on the network that is able to be allocated to
The amount of available bandwidth capacity on the network that is able to be allocated to
AD DS

(cid:1)  The number of users in the

The number of users in the healthcare organisation

(cid:1)  The number of domain controllers that would be needed to support

The number of domain controllers that would be needed to support the
organisation

the healthcare

6.1.3.2

Determine the Number of Domains Required
Determine the Number of Domains Required

It is best to minimise the number of domains that are deployed in the forest as this reduces the
It is best to minimise the number of domains that are deployed in the forest as this reduces the
It is best to minimise the number of domains that are deployed in the forest as this reduces the
overall complexity of the deployment and, as a result, further reduces TCO.
overall complexity of the deployment and, as a result, further reduces TCO.

Recommendations

level, forming the simplest
A single domain forest should be implemented at the healthcare organisation level, forming the simplest
A single domain forest should be implemented at the
possible domain design within this cohesive unit. This enables reduced administrative complexity by
possible domain design within this cohesive unit. This enables reduced administrative complexity by
possible domain design within this cohesive unit. This enables reduced administrative complexity by
providing the following advantages:
providing the following advantages:
(cid:1)  Any domain controller can authenticate any user in the forest
can authenticate any user in the forest
(cid:1)  All domain controllers can be GC servers
can be GC servers
(cid:1)  A reduced number of domain controllers
A reduced number of domain controllers

The following information can be used in circumstances where a single domain forest is not
The following information can be used in circumstances where a single domain forest is not
The following information can be used in circumstances where a single domain forest is not
suitable for the healthcare organi

healthcare organisation.

, the following table shows the
Taking into account the factors listed in section 6.1.3.1, the following table shows the
Taking into account the factors listed in section
ion with the slowest link
recommended maximum number of users in a single domain in conjunction with the slowest link
recommended maximum number of users in a single domain in conjunct
Table 7 can aid in
available and the percentage of bandwidth available to
available and the percentage of bandwidth available to AD DS replication. Table
determining the number of domains required in this situation.
determining the number of domain

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 26

Slowest Link
Connecting a Domain
Controller (Kbps)

Maximum Number of
Maximum Number of
Users if 1% Bandwidth
Users if 1% Bandwidth
Available
Available

Maximum Number of
Users if 5% Bandwidth
Available

Maximum Number of
Maximum Number of
Users if 10% Bandwidth
Users if 10% Bandwidth
Available
Available

Prepared by Microsoft

28.8

32

56

64

128

256

512

1500

10,000
10,000

10,000
10,000

10,000
10,000

10,000
10,000

25,000
25,000

50,000
50,000

80,000
80,000

100,000
100,000

25,000

25,000

50,000

50,000

100,000

100,000

100,000

100,000

40,000
40,000

50,000
50,000

100,000
100,000

100,000
100,000

100,000
100,000

100,000
100,000

100,000
100,000

100,000
100,000

Number of Users in a Single Domain
Table 7: Recommended Maximum Number of Users in a Single Domain

Note

are based upon the following environment conditions:
7 are based upon the following environment conditions:

20 percent new user accounts created per year

The figures quoted in Table 7
(cid:1)  20 percent new user accounts
(cid:1)  15 percent user accounts removed per year
15 percent user accounts removed per year
(cid:1)  Each user account is a member of five global groups and five universal groups
Each user account is a member of five global groups and five universal groups
(cid:1)  For every one user there is one computer
For every one user there is one computer
(cid:1)  The DNS solution in use is
(cid:1)  DNS scavenging is enabled
DNS scavenging is enabled

The DNS solution in use is AD DS Integrated DNS

this basis, if a healthcare organisation has only one percent of bandwidth available to

On this basis, if a healthcare organisation
replication, using a 28.8 Kbps link between locations where
replication, using a 28.8 Kbps link between locations where domain controllers
support up to 10,000 users in a single domain.
support up to 10,000 users in a single domain.

has only one percent of bandwidth available to AD DS
 reside, it can still

It is recommended that, once the number of domains has been defined, it should be documented
ed that, once the number of domains has been defined, it should be documented
ed that, once the number of domains has been defined, it should be documented
using the Indentifying Regions
R14}.Table 8 provides
an example of a simple record of the design decisions made, taking into account the
an example of a simple record of the design decisions made, taking into account the
an example of a simple record of the design decisions made, taking into account the
recommendation of a single domain forest for a healthcare organisa

Indentifying Regions job aid document, named DSSLOGI_4.doc {R14

of a single domain forest for a healthcare organisation.

Name of Region

Slow Link
Slow Link

Healthcare Organisation

56 Kbps
56 Kbps

# of Users

5,000

Comment
Comment

A single forest with a single
A single forest with a single
domain and 5% bandwidth
domain and 5% bandwidth
allocation for AD DS
allocation for

: Example Completed Job Aid for the Number of Domains
Table 8: Example Completed Job Aid for the Number of Domains

6.1.3.3

Determine Whether to Upgrade Existing or Deploy New Domains
Determine Whether to Upgrade Existing or Deploy New Domains
Determine Whether to Upgrade Existing or Deploy New Domains

This AD DS guidance is focused on providing guidance for new installations. Specific guidance on
guidance is focused on providing guidance for new installations. Specific guidance on
guidance is focused on providing guidance for new installations. Specific guidance on
upgrading Windows NT 4.0 and Windows 2000 domains, as well as migrating from Novell
upgrading Windows NT 4.0 and Windows 2000 domains, as well as migrating from Novell
upgrading Windows NT 4.0 and Windows 2000 domains, as well as migrating from Novell
NetWare, is provided in the Active Directory Migration Guide

and includes the following scenarios:
Active Directory Migration Guide, and includes the following scenarios:

(cid:1)  Migrating from Windows NT

Migrating from Windows NT 4.0 domains

(cid:1)  Migrating from Windows 2000 domains
ating from Windows 2000 domains

(cid:1)  Migrating from Novell NetWare
Migrating from Novell NetWare

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 27

6.1.3.4

Assign Domain Names
Assign Domain Names

Prepared by Microsoft

and NetBIOS names for each domain must be determined and assigned. It is recommended
DNS and NetBIOS names for each domain must be determined and assigned. It is recommended
and NetBIOS names for each domain must be determined and assigned. It is recommended
that this is done using the Domain Planning

Domain Planning job aid, named DSSLOGI_5.doc {R14

R14}.

Recommendations

should be followed when
The recommended naming standards guidance shown in section 6.1.7 should be followed when
The recommended naming standards guidance shown in section
determining any domain names.
determining any domain names.

tive Directory domain name follows the naming convention of the healthcare
tive Directory domain name follows the naming convention of the
It is advised that the Active Directory domain name follows the naming convention of the
scale for which it is being deployed and is prefixed with the letters ‘AD’ to easily identify the
organisation scale for which it is being deployed and is prefixed with the letters ‘AD’ to easily identify the
scale for which it is being deployed and is prefixed with the letters ‘AD’ to easily identify the
name as being associated with the AD DS implementation.
name as being associated with the

6.1.3.5

Forest Root Domain
Select the Forest Root Domain

Once the domain model has been determined, it is necessary to select the domain which will act as
Once the domain model has been determined, it is necessary to select the domain which will act as
Once the domain model has been determined, it is necessary to select the domain which will act as
domains in the domain
the forest root domain. This involves determining whether one of the
the forest root domain. This involves determining whether one of the AD DS domains in the domain
ain, or whether it is necessary to deploy a dedicated
design can function as the forest root domain, or whether it is necessary to deploy a dedicated
design can function as the forest root dom
forest root domain.

Recommendation

A single domain forest for the production environment should be implemented at the healthcare
A single domain forest for the production environment should be implemented at the
A single domain forest for the production environment should be implemented at the
organisation level, forming the simplest design, whereby the single domai

n acts as the forest root domain.
level, forming the simplest design, whereby the single domain acts as the forest root domain.

The forest root domain name is also the name of the forest. The forest root name is a DNS name
The forest root domain name is also the name of the forest. The forest root name is a DNS name
The forest root domain name is also the name of the forest. The forest root name is a DNS name
. Creating a new namespace for
that consists of a prefix and a suffix, in the form of prefix.suffix. Creating a new namespace for
that consists of a prefix and a suffix, in the form of
ing DNS infrastructure does not need to be modified to accommodate
AD DS ensures that any existing DNS infrastructure does not need to be modified to accommodate
ing DNS infrastructure does not need to be modified to accommodate
AD DS.

Recommendation

should be followed when
The recommended naming standards guidance given in section 6.1.7 should be followed when
The recommended naming standards guidance given in section
determining any domain names.
determining any domain names.

Design the OU Structure for Each Domain
6.1.4  Design the OU Structure for Each Domain

Forest owners are responsible for creating OU designs for each domain. Creating an OU design
Forest owners are responsible for creating OU designs for each domain. Creating an OU design
Forest owners are responsible for creating OU designs for each domain. Creating an OU design
involves designing the OU structure, assigning the OU owner ro
le, and creating account and
involves designing the OU structure, assigning the OU owner role, and creating account and
resource OUs. For further information on the best practice methods around OU design, refer to the
resource OUs. For further information on the best practice methods around OU design, refer to the
resource OUs. For further information on the best practice methods around OU design, refer to the
Group Policy for Healthcare Desktop Management {R20}.
guidance document, Group Policy for

6.1.5

Prepare to Enable Advanced Features via Functional Level
Prepare to Enable Advanced Features via Functional Level
Prepare to Enable Advanced Features via Functional Level

In order to utilise the advanced features in Windows Server 2008 R2, the domain and/or forest
In order to utilise the advanced features in Windows Server 2008 R2, the domain and/or forest
In order to utilise the advanced features in Windows Server 2008 R2, the domain and/or forest
must be raised to the appropriate functional level. This not only enables new features to be used,
tional level. This not only enables new features to be used,
must be raised to the appropriate func
in the environment.
but also limits the versions of Windows that can be run on
but also limits the versions of Windows that can be run on domain controllers in the environment.
The following are references for the advanced features available:
The following are references for the advanced features available:

(cid:1)  Table 23 (APPENDIX C

features that are available by default on
APPENDIX C) summarises the AD DS features that are available by default on

any domain controller running Windows Server

running Windows Server 2008 R2

(cid:1)  Table 24 (APPENDIX C

) lists the Windows Server 2008 R2 domain functional levels, the
APPENDIX C) lists the Windows Server 2008 R2 domain functional levels, the
operating systems that they support, and the Windows Server 2008 R2 features that are
operating systems that they support, and the Windows Server 2008 R2 features that are
operating systems that they support, and the Windows Server 2008 R2 features that are
available at each domain functional level
available at each domain functional level

(cid:1)  Table 25 (APPENDIX C

) lists the Windows Server 2008 R2 forest functional levels, the
APPENDIX C) lists the Windows Server 2008 R2 forest functional levels, the

operating systems that they support, and the Windows Server 2008 R2 features that are
operating systems that they support, and the Windows Server 2008 R2 features that are
operating systems that they support, and the Windows Server 2008 R2 features that are
available at each forest functional level
available at each forest functional level

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 28

Prepared by Microsoft

6.1.5.1

Prepare to Enable Functional Levels
Prepare to Enable Functional Levels

In order to determine what preparation is required to enable domain and/or forest functional level
In order to determine what preparation is required to enable domain and/or forest functional level
In order to determine what preparation is required to enable domain and/or forest functional level
changes, the following should be identified:
changes, the following should be identified:

(cid:1)  Assess the current environment requirements. It is recommended that this is
Assess the current environment requirements. It is recommended that this is done using the
Assess the current environment requirements. It is recommended that this is
Domain Controller Assessment
Domain Controller Assessment job aid document, named DSSPFL_1.doc

DSSPFL_1.doc {R14}

(cid:1)  Identify the functional level scenario, for example, a Windows NT
4.0 environment, a
Identify the functional level scenario, for example, a Windows NT 4.0 environment, a
mode environment, a
mode environment, a Windows 2000 native-mode environment, a
Windows 2000 mixed-mode environment, a Windows 2000 native
Windows Server 2003 environment or a new Windows Server 2008 R2 forest
Windows Server 2003 environment or a new Windows Server 2008 R2 forest
Windows Server 2003 environment or a new Windows Server 2008 R2 forest

(cid:1)  Identify any applications that cannot support the desired functional level and assess
Identify any applications that cannot support the desired functional level and assess which
Identify any applications that cannot support the desired functional level and assess
is the maximum functional level they can support. This is typically a scenario around the
is the maximum functional level they can support. This is typically a scenario around the
is the maximum functional level they can support. This is typically a scenario around the
ystem which offers new functional levels in
release of a new version of the operating system which offers new functional levels in
release of a new version of the
AD DS. For the majority of applications it is not necessarily the functio
nal level that is
. For the majority of applications it is not necessarily the functional level that is
unsupported but rather what it means in terms of domain controllers. Some applications in
unsupported but rather what it means in terms of domain controllers. Some applications in
unsupported but rather what it means in terms of domain controllers. Some applications in
the past have failed to work in an environment where all domain controllers are running the
the past have failed to work in an environment where all domain controllers are running the
the past have failed to work in an environment where all domain controllers are running the
latest Windows Server operating system version
latest Windows Server

Once the current environment has been assessed and the functional level requirements are
current environment has been assessed and the functional level requirements are
current environment has been assessed and the functional level requirements are
gathered, the appropriate domain and/or forest functional level can be enabled during the
gathered, the appropriate domain and/or forest functional level can be enabled during the
gathered, the appropriate domain and/or forest functional level can be enabled during the
deployment phase.

Recommendation

tilise advanced features, the forest functional level
healthcare organisations to be able to utilise advanced features, the forest functional level
In order for healthcare organisations
mode as soon as possible after forest creation.
should be raised to Windows Server 2008 R2 native-mode as soon as possible after forest creation.
should be raised to Windows Server 2008 R2 native
Raising the forest functional level automatically raises the domain functional level.
Raising the forest functional level automatically raises the domain functional level.

Information

(cid:1)  It is not possible to lower t

not possible to lower the functional level of a domain or forest after it has be

after it has been raised without a

restore
full domain or forest restore

(cid:1)  Only members of the Domain Admins group can raise the domain functional level
Only members of the Domain Admins group can raise the domain functional level
Only members of the Domain Admins group can raise the domain functional level
(cid:1)  Only members of the Enterprise Admins group can
(cid:1)  The Primary Domain Controller (PDC) emulator operations master

raise the forest functional level
Only members of the Enterprise Admins group can raise the forest functional level

is the domain controller that should
Primary Domain Controller (PDC) emulator operations master is the domain controller that should

be used to raise the domain functional level
be used to raise the domain functional level

(cid:1)  The schema operations master is the domain controller that should be used to

raise the forest
The schema operations master is the domain controller that should be used to raise the forest
functional level

Trust Design
6.1.6  AD DS Trust Design

domain can be authenticated and authorised for
By default, all users in a specific Active Directory domain can be authenticated and authorised for
By default, all users in a specific
resources contained within that domain. In this way, users can be provided with secured access to
resources contained within that domain. In this way, users can be provided with secured access to
resources contained within that domain. In this way, users can be provided with secured access to
all resources in that domain. To expand that access to include resources beyond the boundaries of
all resources in that domain. To expand that access to include resources beyond the boundaries of
all resources in that domain. To expand that access to include resources beyond the boundaries of
a single domain, trust relationships are required. Trust relationships provide a mechanism for one
ain, trust relationships are required. Trust relationships provide a mechanism for one
ain, trust relationships are required. Trust relationships provide a mechanism for one
domain to allow access to resources, from user accounts that have been authenticated in another
domain to allow access to resources, from user accounts that have been authenticated in another
domain to allow access to resources, from user accounts that have been authenticated in another
domain.

Transitive trust relationships allow
Active Directory forest. However, in order for controlled users to have authentication and resource
. However, in order for controlled users to have authentication and resource
. However, in order for controlled users to have authentication and resource
access, it is necessary to manually design for, and deploy, trusts to external domains and forests.
access, it is necessary to manually design for, and deploy, trusts to external domains and forests.
access, it is necessary to manually design for, and deploy, trusts to external domains and forests.

allow full forest wide authentication and resource access

ion and resource access within an

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 29

Prepared by Microsoft

The trust technologies22 in Windows Server 2008 R2 can provide a starting point to help
in Windows Server 2008 R2 can provide a starting point to help healthcare
in Windows Server 2008 R2 can provide a starting point to help
address these business requirements, and enhance their ability to offer and maintain
organisations address these business requirements, and enhance their ability to offer and maintain
address these business requirements, and enhance their ability to offer and maintain
Single Sign-On (SSO) and Reduced Sign

On (SSO) and Reduced Sign-On (RSO).

-in features of the
Applications integrated with Windows Server 2008 R2 and AD DS use the built-
Applications integrated with Wind
operating system to establish and maintain trust for a wide variety of business requirements and
operating system to establish and maintain trust for a wide variety of business requirements and
operating system to establish and maintain trust for a wide variety of business requirements and
scenarios, including domain trusts, cross
scenarios, including domain trusts, cross-forest trusts and external trusts.

R2 fully audits trust configuration at a detailed level. Auditable events
Windows Server 2008 R2 fully audits trust configuration at a detailed level. Auditable events
R2 fully audits trust configuration at a detailed level. Auditable events
include the creation, deletion and modification of trusts.
include the creation, deletion and modification of trusts.

Recommendations

level, therefore no additional
A single domain forest should be implemented at healthcare organisation level, therefore no additional
A single domain forest should be implemented at
rnal trusts will be required in the forest unless:
internal trusts will be required in the forest unless:
(cid:1)  It is necessary to have an external trust relationship with another

It is necessary to have an external trust relationship with another healthcare organisation
Directory forest in order to allow roaming users and the collaboration of resources
Directory forest in order to allow roaming users and the collaboration of resources
Directory forest in order to allow roaming users and the collaboration of resources

healthcare organisation Active

(cid:1)  Cater for third-party IT service provision requirements
IT service provision requirements

Ideally, in a design requiring collaboration between multiple forests, each forest should
Ideally, in a design requiring collaboration between multiple forests, each forest should be, at a minimum,
Ideally, in a design requiring collaboration between multiple forests, each forest should
configured with Windows Server 2003 forest functional level and cross forest trusts should be
configured with Windows Server 2003 forest functional level and cross forest trusts should be
configured with Windows Server 2003 forest functional level and cross forest trusts should be
g that Kerberos is used between forests, and allowing for a greater degree of
implemented, ensuring that Kerberos is used between forests, and allowing for a greater degree of
g that Kerberos is used between forests, and allowing for a greater degree of
configuration with regards to security.
configuration with regards to security.

Should additional trusts be required, the Multiple Forest Considerations in Windows 2000 and
Should additional trusts be required, the Multiple Forest Considerations in Windows 2000 and
Should additional trusts be required, the Multiple Forest Considerations in Windows 2000 and
Windows Server 200323 whitepaper should be reviewed in conjunction with this section. However, if
whitepaper should be reviewed in conjunction with this section. However, if
whitepaper should be reviewed in conjunction with this section. However, if
it is determined that no additional trusts are required, section 6.1.6.1 can be skippe
it is determined that no additional trusts are required, section

can be skipped.

22 Trust Technologies {R21}:
http://technet2.microsoft.com/windowsserver/en/library/9d688a18-15c7-4d4e-9d34-7a763baa50a11033.mspx
http://technet2.microsoft.com/windowsserver/
us/library/cc770299.aspx
http://technet.microsoft.com/en-us/library/cc770299.aspx

7a763baa50a11033.mspx  and

Multiple Forest Considerations in Windows 2000 and Windows Server 2003 {R22}:

23 Multiple Forest Considerations in Windows 2000 and Windows
http://technet2.microsoft.com/windowsserver/en/library/bda0d769

2.microsoft.com/windowsserver/en/library/bda0d769-a663-42f4-879f-f548b19a8c7e1033.mspx

f548b19a8c7e1033.mspx

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 30

Prepared by Microsoft

6.1.6.1

Identify and Design for Trust Model Required
Identify and Design for Trust Model Required

trust requirements have been determined, if required, the trust model
Once the AD DS trust requirements have been determined, if required, the trust model
trust requirements have been determined, if required, the trust model
relationships should be designed and documented.
relationships should be designed and documented.

Administrators can use a number of methods24 to configure and manage trust relationships in
relationships in
Administrators can use a number of methods
environments, including the following:
AD DS environments, including the following:

(cid:1)  Trust tools built into the Windows Server

Trust tools built into the Windows Server Operating system

(cid:1)  Trust Windows Management Instrumentation (WMI) classes
Trust Windows Management Instrumentation (WMI) classes

(cid:1)  Script based solution using classes and APIs provided in the

operating system
Script based solution using classes and APIs provided in the operating system

Configuring Trust relationships also requires cooperation with the network security team to ensure
nfiguring Trust relationships also requires cooperation with the network security team to ensure
nfiguring Trust relationships also requires cooperation with the network security team to ensure
that the required network ports are configured to support the trust and its associated traffic.
that the required network ports are configured to support the trust and its associated traffic.
that the required network ports are configured to support the trust and its associated traffic.

Before designing and deploying trust relationships between two
forests (also known as interforest
Before designing and deploying trust relationships between two forests (also known as interforest
trusts, including both external and forest trusts), ensure that all possible security threat scenarios
trusts, including both external and forest trusts), ensure that all possible security threat scenarios
trusts, including both external and forest trusts), ensure that all possible security threat scenarios
are reviewed25.

Active Directory Naming Standards
6.1.7  Active Directory Naming Standards

Every object in AD DS is an instance of a class defined in the schema
that ensure:

. Each class has attributes
is an instance of a class defined in the schema. Each class has attributes

(cid:1)  Unique identification of each object (instance of a class) in a directory data store
Unique identification of each object (instance of a class) in a directory data store
Unique identification of each object (instance of a class) in a directory data store

(cid:1)  Backward compatibility with Security Identifiers (SIDs) used in Windows NT 4.0 and earlier
Backward compatibility with Security Identifiers (SIDs) used in Windows NT 4.0 and earlier
Backward compatibility with Security Identifiers (SIDs) used in Windows NT 4.0 and earlier
for security principals

(cid:1)  Compatibility with LDAP standards for directory object names
ith LDAP standards for directory object names

creates a relative
can be referenced by several different names. AD DS creates a relative

Each object in AD DS can be referenced by several different names.
distinguished name (RDN), and a canonical name (CN), for each object based upon information
distinguished name (RDN), and a canonical name (CN), for each object based upon information
distinguished name (RDN), and a canonical name (CN), for each object based upon information
that was provided when the object was created or modified. Each object can also be referenced by
object was created or modified. Each object can also be referenced by
object was created or modified. Each object can also be referenced by
its distinguished name (DN), which is derived from the relative distinguished name of the object and
its distinguished name (DN), which is derived from the relative distinguished name of the object and
its distinguished name (DN), which is derived from the relative distinguished name of the object and
all of its parent container objects.
all of its parent container objects.

Recommendation

Windows Server 2008 R2 does not
Windows Server 2008 R2 does not provide any software based policy for enforcing a
naming policy should be established and communicated to all
Therefore, a healthcare organisation naming policy should be established and communicated to all
Therefore, a healthcare organisation
employees who have been delegated the right to create objects in AD DS.
employees who have been delegated the right to create objects in

provide any software based policy for enforcing a naming standard.

ons contain the guidelines and guidance for the naming standards of the most
The following sections contain the guidelines and guidance for the naming standards of the most
ons contain the guidelines and guidance for the naming standards of the most
common Active Directory objects.
common Active Directory objects.

6.1.7.1

Forest and Domain Naming Requirements
AD DS Forest and Domain Naming Requirements

name of the domain. However, for backward
domain names are usually the full DNS name of the domain. However, for backward
AD DS domain names are usually the full DNS
Windows 2000 name for use by computers running pre-
compatibility, each domain also has a pre-Windows 2000 name for use by computers running pre
compatibility, each domain also has a pre
Windows 2000 operating systems.
Windows 2000 operating systems.

Domain and Forest Trust Tools and Settings {R23}:

24 Domain and Forest Trust Tools and Settings
6adbc1ebceca1033.mspx. Windows
http://technet2.microsoft.com/windowsserver/en/library/108124dd
http://technet2.microsoft.com/windowsserver/en/library/108124dd-31b1-4c2c-9421-6adbc1ebceca1033.mspx
e individual chapters documented in the Active Directory Domains
Server 2008 R2 specific content is embedded within the individual chapters documented in the Active Directory Domains
Server 2008 R2 specific content is embedded within th
and Trusts section  http://technet.microsoft.com/en

http://technet.microsoft.com/en-us/library/cc770299.aspx

25 Security Considerations for Trusts {
http://technet2.microsoft.com/windowsserver/en/library/1f33e9a1-c3c5-431c-a5cc-c3c2bd579ff11033.mspx
http://technet2.microsoft.com/windowsserv
Windows Server 2008 R2 content related to the separate Trust types is contained in the Active Directory Domains and
Windows Server 2008 R2 content related to the separate Trust types is contained in the Active Directory Domains and
Windows Server 2008 R2 content related to the separate Trust types is contained in the Active Directory Domains and
Trusts section  http://technet.microsoft.com/en

http://technet.microsoft.com/en-us/library/cc770299.aspx

c3c2bd579ff11033.mspx and specific

{R24}:

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 31

Prepared by Microsoft

Windows 2000 domain name can be used to log on to a Windows Server 2008 R2 domain
Windows 2000 domain name can be used to log on to a Windows Server 2008 R2 doma
The pre-Windows 2000 domain name can be used to log on to a Windows Server 2008 R2 doma
Windows 2000, Windows 2000, Windows XP, or servers running
from computers running pre-Windows 2000, Windows 2000, Windows XP, or servers running
Windows 2000, Windows 2000, Windows XP, or servers running
format. Users can also log on to
Windows Server 2003 using the DomainName\UserName format. Users can also log on to
Windows Server 2003 using the
computers running any Windows
computers running any Windows operating system from Windows 2000 onwards using the
Principal Name (UPN) associated with their user account.
Principal Name (UPN) associated with their user account.

ystem from Windows 2000 onwards using the User

Recommendations

The following recommended naming standards should be adhered to when determining any DNS or pre-
The following recommended naming standards should be adhered to when determining any DNS or pre
The following recommended naming standards should be adhered to when determining any DNS or pre
Windows 2000 (NetBIOS) domain names:
Windows 2000 (NetBIOS) domain names:
(cid:1)  Use a prefix that is not likely to become out
(cid:1)  Use a prefix that includes Internet standard characters only, which include A

Use a prefix that includes Internet standard characters only, which include A-Z, a
are not entirely numeric

Use a prefix that is not likely to become outdated

Z, a-z, 0-9 and (-), but

(cid:1)  Ensure that DNS naming policy is identifiable with, and relevant to, the

Ensure that DNS naming policy is identifiable with, and relevant to, the healthcare organisation
AD DS is representing

healthcare organisation that

(cid:1)  Ensure that it is clear and meaningful
Ensure that it is clear and meaningful
(cid:1)  Keep DNS naming intuitive, using 15 characters or fewer in the prefix, and as such allowing the
Keep DNS naming intuitive, using 15 characters or fewer in the prefix, and as such allowing the
Keep DNS naming intuitive, using 15 characters or fewer in the prefix, and as such allowing the
NetBIOS name to be the same as the prefix
NetBIOS name to be the same as the prefix

(cid:1)  The chosen name should avoid generic words such as AD, Corp and root. Any nam
The chosen name should avoid generic words such as AD, Corp and root. Any name that looks as
The chosen name should avoid generic words such as AD, Corp and root. Any nam
though it could easily clash with another organisation should be avoided, something quite likely with
though it could easily clash with another organisation should be avoided, something quite likely with
though it could easily clash with another organisation should be avoided, something quite likely with
generic words

(cid:1)  Domain and forest names cannot be comprised solely of numbers. Neither the domain name
Domain and forest names cannot be comprised solely of numbers. Neither the domain name nor the
Domain and forest names cannot be comprised solely of numbers. Neither the domain name
forest name can commence with
forest name can commence with a period (.)or a hyphen (-)

(cid:1)  Avoid the use of any of the words listed in the table of reserved words documented in Microsoft
Avoid the use of any of the words listed in the table of reserved words documented in Microsoft
Avoid the use of any of the words listed in the table of reserved words documented in Microsoft
Knowledge Base article 90926426
Knowledge Base article 909264

(cid:1)  The Active Directory DNS domain name should be the

The Active Directory DNS domain name should be the healthcare organisation’s
the letters ‘AD’; for example, AD

for more information
tters ‘AD’; for example, ADHealthOrg. See section 6.1.7.2 for more information

healthcare organisation’s name preceded by

(cid:1)  The Active Directory NetBIOS domain name should be an abridged versi

The Active Directory NetBIOS domain name should be an abridged version of the
name preceded by the letters ‘AD’ so that it is not longer than 15 characters in total
name preceded by the letters ‘AD’ so that it is not longer than 15 characters in total
name preceded by the letters ‘AD’ so that it is not longer than 15 characters in total

on of the organisation’s

(cid:1)  UPNs should be used for user account log on. See section

UPNs should be used for user account log on. See section 6.1.7.3 for more information on
Security Principal Object Naming Requirements
Security Principal Object Naming Requirements

for more information on AD DS

6.1.7.2

DNS Naming Requirements
DNS Naming Requirements

The DNS and NetBIOS names for each domain will be determined in section 6.1.3
The DNS and NetBIOS names for each domain will be determined in section
. It is recommended that this is documented using the Domain Planning
. It is recommended that this is documented using the
guidelines in section 6.1.7.1. It is recommended that this is documented using the
job aid, named DSSLOGI_5.doc
provides an example of a simple record of the
DSSLOGI_5.doc {R14}. Table 9 provides an example of a simple record of the
design decisions made, taking into account the recommendations made for DNS and NetBIOS
design decisions made, taking into account the recommendations made for DNS and NetBIOS
design decisions made, taking into account the recommendations made for DNS and NetBIOS
names.

6.1.3, based on the

Region

Origin

DNS Prefix

NetBIOS Name

Health
Organisation

(cid:2) New domain
(cid:3) Upgrade
From:

IT Administrator
Owner: IT Administrator

ADHealthOrg.healthorg.com

ADHealthOrg

: Example Completed Job Aid for DNS and NetBIOS Names
Table 9: Example Completed Job Aid for DNS and NetBIOS Names

Naming conventions in Active Directory for computers, domains, sites, and OUs: {R25}

26 Naming conventions in Active Directory for computers, domains, sites, and OUs
http://support.microsoft.com/kb/909264
http://support.microsoft.com/kb/909264

Justification /
Notes

The ADHealthOrg
domain is a sub-domain
of the organisation’s
externally registered
domain, this is also the
Forest Root Domain

Page 32

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Prepared by Microsoft

The DNS and NetBIOS names should be incorporated into the DNS infrastructure, and a forest
The DNS and NetBIOS names should be incorporated into the DNS infrastructure, and a forest
The DNS and NetBIOS names should be incorporated into the DNS infrastructure, and a forest
DNS name identified.

Recommendations

The DNS namespace should not be a single label DNS name, as detailed in Microsoft Knowledge Base
The DNS namespace should not be a single label DNS name, as detailed in Microsoft Knowledge Base
The DNS namespace should not be a single label DNS name, as detailed in Microsoft Knowledge Base
label DNS names {R26}.
Information about configuring Windows for domains with single-label DNS
article 300684: Information about configuring Windows for domains with single

external DNS registration, and
The DNS name should be registered as a sub-domain of the organisation’s external DNS registration, and
The DNS name should be registered as a sub
should follow their suffix standards, for example,
This reduces administration, whilst
should follow their suffix standards, for example, healthorg.org.com. This reduces administration, whilst
maintaining simplicity and flexibility in working towards an integrated collaborative infrastructure for the
maintaining simplicity and flexibility in working towards an integrated collaborative infrastructure for the
maintaining simplicity and flexibility in working towards an integrated collaborative infrastructure for the
healthcare organisation.

The DNS name should be as short as possible while still remaining meaningful and unique. This reduces
The DNS name should be as short as possible while still remaining meaningful and uniq
The DNS name should be as short as possible while still remaining meaningful and uniq
the risk of any file system issues with very long domain names.
the risk of any file system issues with very long domain names.

lists the character sets that are supported by DNS and NetBIOS.
Table 10 lists the character sets that are supported by DNS and NetBIOS.

Character
Restriction

Standard Domain Name
Standard Domain Name
System (Including
System (Including
Windows NT4.0)

Characters
permitted

Supports Request for Comments
Supports Request for Comments
(RFC) 1123, which permits: A to Z,
(RFC) 1123, which permits: A to Z,
a to z, 0 to 9, and the hyphen (-).
a to z, 0 to 9, and the hyphen (

Maximum host
name and Fully
Qualified
Domain Name
(FQDN) length.

63 bytes for each name and 255
63 bytes for each name and 255
bytes for the complete FQDN (254
bytes for the complete FQDN (254
bytes for the FQDN plus one byte
bytes for the FQDN plus one byte
for the terminating dot).

Microsoft Domain Name System
(Windows 2000,  Windows Server
2003, Windows Server 2008 and
Windows Server 2008 R2)

Supports RFC 1123 and Universal
Transformation Format-8 (UTF-8). Windows
2000 Server onwards DNS server can be
configured to allow or disallow the use of
UTF-8 characters.

The same as standard DNS with the
addition of UTF-8 support. Some UTF-8
characters exceed one byte in length.

NetBIOS
NetBIOS

Not allowed: Unicode characters,
Not allowed: Unicode characters,
numbers, white space, and the
numbers, white space, and the
symbols: / \ [ ] : | < > + = ; , ? and
symbols: /
*).

15 bytes in length.
15 bytes in length.

Table 10: Domain Name System and NetBIOS

: Domain Name System and NetBIOS Naming Character Set Restrictions

6.1.7.3

Security Principal Object Naming Requirements
AD DS Security Principal Object Naming Requirements
Security Principal Object Naming Requirements

Security principal objects are AD
the network, as well as being granted access to domain resources. An adm
inistrator needs to
the network, as well as being granted access to domain resources. An administrator needs to
provide names for security principal objects (user accounts, computer accounts, and groups) that
provide names for security principal objects (user accounts, computer accounts, and groups) that
provide names for security principal objects (user accounts, computer accounts, and groups) that
are unique within a domain.

objects that are assigned SIDs, and can be used to log on to
AD DS objects that are assigned SIDs, and can be used to log on to

objects helps to ensure that
wide naming convention for AD DS objects helps to ensure that

Establishing an organisation-wide naming convention for
secure access control within any Active Directory forest is not compromised. Without a universal
l within any Active Directory forest is not compromised. Without a universal
l within any Active Directory forest is not compromised. Without a universal
naming convention, the potential for user error when adding, modifying or removing AD DS security
naming convention, the potential for user error when adding, modifying or removing
naming convention, the potential for user error when adding, modifying or removing
round the
principal objects increases substantially, especially if IT Administrators move around the
principal objects increases substantially, especially if IT Administrators move a
infrastructure.

Recommendation

When establishing an AD DS
organisation, ensure that it
provides for the inclusion of information about the object’s scope and purpose in its name, and also its
provides for the inclusion of information about the object’s scope and purpose in its name, and also its
provides for the inclusion of information about the object’s scope and purpose in its name, and also its
ts description. This helps to differentiate each object from similar objects.
owner in its description. This helps to differentiate each object from similar objects.

DS object naming convention for the healthcare organisation

The names of security principal objects can contain all Unicode characters except the special
The names of security principal objects can contain all Unicode characters except the special
The names of security principal objects can contain all Unicode characters except the special
LDAP characters defined in RFC 2253. This list of special characters includes: a leading space, a
LDAP characters defined in RFC 2253. This list of special characters includes: a lea
LDAP characters defined in RFC 2253. This list of special characters includes: a lea
trailing space and any of the following characters: # , + " \ < > and ;
trailing space and any of the following characters: # , + "

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 33

Prepared by Microsoft

displays the security principal object names and the guidelines that they must conform to:
Table 11 displays the security principal object names and the guidelines that they must conform to:
displays the security principal object names and the guidelines that they must conform to:

Type of Account
Name

User account

Maximum Size
Maximum Size

Special Limitations
Special Limitations

Computers running Windows Server 2003 and
Computers running Windows Server
Windows 2000 can use a UPN for a user account.
Windows 2000 can use a UPN for a user account.
Computers running Windows NT 4.0 and earlier are
Computers running Windows NT 4.0 and earlier are
limited to 20 characters or 20 bytes, depending upon
limited to 20 characters or 20 bytes, depending upon
the character set. Individual characters may require
the character set. Individual characters may require
more than one byte.
more than one byte.

A user account cannot consist solely of periods (.)
A user account cannot co
or spaces, or end in a period. Any leading periods
or spaces, or end in a period. Any leading periods
or spaces are cropped. Use of the @ symbol is
or spaces are cropped. Use of the @ symbol is
not supported with the logon format for Windows
not supported with the logon format for Windows
NT 4.0 and earlier, which is
NT 4.0 and earlier, which is
UserName. Windows 2000 logon
DomainName\UserName
names are unique to the domain and Windows
ue to the domain and Windows
Server 2003 logon names are unique within the
Server 2003 logon names are unique within the
forest.

Computer account

NetBIOS = 15 characters or 15 bytes, depending upon
NetBIOS = 15 characters or 15 bytes, depending upon
the character set. Individual characters may require
the character set. Individual characters may require
more than one byte.
more than one byte.

A computer account cannot consist solely of
A computer account cannot consist solely of
numbers, periods (.), or spaces. Any leading
numbers, periods (.), or spaces. Any leading
are cropped.
periods or spaces are cropped.

= 63 characters or 63 bytes, depending upon the
DNS = 63 characters or 63 bytes, depending upon the
character set, and 255 characters for a FQDN.
character set, and 255 characters for a FQDN.
Individual characters may require more than one byte.
Individual characters may require more than one byte.

Group account

63 characters or 63 bytes, depending upon the
63 characters or 63 bytes, depending upon the
character set. Individual characters may require more
character set. Individual characters may require more
than one byte.
than one byte.

A group account cannot consist solely of numbers,
A group account cannot consist solely of numbers,
periods (.), or spaces. Any leading periods or
periods (.), or spaces. Any leading periods or
spaces are cropped.

: Guidelines for Security Principal Names
Table 11: Guidelines for Security Principal Names

Note

If the administrator changes the default security settings, then it is possible to use computer names
If the administrator changes the default security settings, then it is possible to use computer names
If the administrator changes the default security settings, then it is possible to use computer names
containing more than 15 characters.
containing more than 15 characters.

6.1.7.3.1

User Account Names
User Account Names

each user account has:
In AD DS, each user account has:

(cid:1)  A user logon name

(cid:1)  A pre-Windows 2000 user logon name (Security Account Manager (SAM) account name)
Windows 2000 user logon name (Security Account Manager (SAM) account name)
Windows 2000 user logon name (Security Account Manager (SAM) account name)

(cid:1)  A UPN suffix

The administrator enters the user logon name and selects the UPN suffix when creating the user
The administrator enters the user logon name and selects the UPN suffix when creating the user
The administrator enters the user logon name and selects the UPN suffix when creating the user
account. AD DS suggests a pre
Windows 2000 logon name at any time.
logon name. Administrators can change the pre-Windows 2000 logon name at any time.
logon name. Administrators can change the pre

Windows 2000 user logon name using the first 20 bytes of the user
pre-Windows 2000 user logon name using the first 20 bytes of the user

, each user account has a UPN based on Internet Engineering Task Force (IETF) RFC
In AD DS, each user account has a UPN based on Internet Engineering Task Force (IETF) RFC
, each user account has a UPN based on Internet Engineering Task Force (IETF) RFC
822: Standard for the Format of ARPA Internet Text Messages
logon name and the UPN suffix joined by the @ sign.
logon name and the UPN suffix joined by the @ sign.

for the Format of ARPA Internet Text Messages27. The UPN is composed of the user
. The UPN is composed of the user

Important

automatically adds it when it
Do not add the @ sign to the user logon name or the UPN suffix as AD DS automatically adds it when it
Do not add the @ sign to the user logon name or the UPN suffix as
UPN. A UPN that contains more than one @ sign is invalid.
creates the UPN. A UPN that contains more than one @ sign is invalid.

Windows NT4.0 and earlier domains allowed the use of a period (.) at the end of a user logon name as
Windows NT4.0 and earlier domains allowed the use of a period (.) at the end of a user logon name as
Windows NT4.0 and earlier domains allowed the use of a period (.) at the end of a user logon name as
long as the user logon name did not consist solely of period characters. Windows Server 2008 R2
long as the user logon name did not consist solely of period characters. Windows Server 2008 R2
long as the user logon name did not consist solely of period characters. Windows Server 2008 R2
domains do NOT allow the use of a period or multiple periods at the end of a user logon name.
domains do NOT allow the use of a period or multiple periods at the end of a user logon name.
domains do NOT allow the use of a period or multiple periods at the end of a user logon name.

Standard for the Format of ARPA Internet Text Messages {R27}:

27Standard for the Format of ARPA Internet Text Messages
http://www.ietf.org/rfc/rfc2822.txt

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 34

Prepared by Microsoft

The second part of the UPN, the UPN suffix, identifies the domain in which the user account is
The second part of the UPN, the UPN suffix, identifies the domain in which the user account is
The second part of the UPN, the UPN suffix, identifies the domain in which the user account is
located. This UPN suffix can be the DNS domain name, the DNS name o
f any domain in the forest,
located. This UPN suffix can be the DNS domain name, the DNS name of any domain in the forest,
or it can be an alternative name created by an administrator and used just for log on purposes. This
or it can be an alternative name created by an administrator and used just for log on purposes. This
or it can be an alternative name created by an administrator and used just for log on purposes. This
alternative UPN suffix does not need to be a valid DNS name.
alternative UPN suffix does not need to be a valid DNS name.

which the user account was
, the default UPN suffix is the DNS name of the domain in which the user account was

In AD DS, the default UPN suffix is the DNS name of the domain in
created. In most cases, this is the domain name registered as the enterprise domain on the
created. In most cases, this is the domain name registered as the enterprise domain on the
created. In most cases, this is the domain name registered as the enterprise domain on the
Internet. Using alternative domain names as the UPN suffix can provide additional logon security
Internet. Using alternative domain names as the UPN suffix can provide additional logon security
Internet. Using alternative domain names as the UPN suffix can provide additional logon security
and simplify the names used to log on to another domain in the forest.
and simplify the names used to log on to

User account names should follow the format of firstname.lastname

Recommendations
(cid:1)  User account names should follow the format of
(cid:1)  Duplicate names should be handled by including the middle initials in the user name such as
Duplicate names should be handled by including the middle initials in the user name such as
Duplicate names should be handled by including the middle initials in the user name such as
firstname.initial.lastname
(cid:1)  UPN suffixes should be us

ed for user log on. For more information see the Microsoft Knowledge Base
UPN suffixes should be used for user log on. For more information see the Microsoft Knowledge Base
article: Users Can Log On Using User Name or User Principal Name

Users Can Log On Using User Name or User Principal Name28

(cid:1)  Whilst users log on to the

Microsoft Management Console (MMC) should be named such
and Computers Microsoft Management Console (MMC) should be named such

using UPN names, the common name (CN) displayed within the
Whilst users log on to the AD DS using UPN names, the common name (CN) displayed within the
Active Directory Users and Computer
that different user accounts are easily identified, for example administrator account names are
that different user accounts are easily identified, for example administrator account names are
that different user accounts are easily identified, for example administrator account names are
preceded with ‘adm_’, service accounts preceded with ‘svc_’ and temporary staff account names
preceded with ‘adm_’, service accounts preceded with ‘svc_’ and temporary staff account na
preceded with ‘adm_’, service accounts preceded with ‘svc_’ and temporary staff account na
could be preceded with ‘tmp_’
could be preceded with ‘tmp_’
(cid:1)  Staff with administrative responsibilities should have at least two accounts: A regular user account
Staff with administrative responsibilities should have at least two accounts: A regular user account
Staff with administrative responsibilities should have at least two accounts: A regular user account
with which they perform their normal, day to day activities such as email and document creation and a
with which they perform their normal, day to day activities such as email and document creation and a
with which they perform their normal, day to day activities such as email and document creation and a
separate account used purely for administrative tasks. The administrative account should not have
ed purely for administrative tasks. The administrative account should not have
ed purely for administrative tasks. The administrative account should not have
access to email and should be named the same as the regular user account but with a prefix of
access to email and should be named the same as the regular user account but with a prefix of
access to email and should be named the same as the regular user account but with a prefix of
‘adm_’. This allows administrative actions to be audited and a clear association between the
‘adm_’. This allows administrative actions to be audited and a clear association be
‘adm_’. This allows administrative actions to be audited and a clear association be
trative activities and the user
administrative activities and the user

For enhanced security, the local Administrator user account should be renamed from Administrator
For enhanced security, the local Administrator user account should be renamed from
For enhanced security, the local Administrator user account should be renamed from
to make it harder to guess and attack29.
to make it harder to guess and attack

Recommendation
(cid:1)  It is recommended that the built in Administrator user

account is renamed to blend in with the chosen
It is recommended that the built in Administrator user account is renamed to blend in with the chosen
naming scheme, as well as delete the default comment on this account, and therefore aid security
naming scheme, as well as delete the default comment on this account, and therefore aid security
naming scheme, as well as delete the default comment on this account, and therefore aid security
(cid:1)  A dummy user account should be created with the name ‘Administrator’ to act as a decoy account,
A dummy user account should be created with the name ‘Administrator’ to act as a decoy account,
A dummy user account should be created with the name ‘Administrator’ to act as a decoy account,
uld then be disabled
this account should then be disabled

6.1.7.3.2

Group Account Names
Group Account Names

It is possible to apply any group naming strategy that works for the
organisation, as long as group
It is possible to apply any group naming strategy that works for the organisation
names provide enough information to distinguish them from other groups. A common approach is
names provide enough information to distinguish them from other groups. A common approach is
names provide enough information to distinguish them from other groups. A common approach is
roup naming standard that organises groups according to business structure.
roup naming standard that organises groups according to business structure.
to create a security group naming standard that organises groups according to business structure.
In this way, group names are composed of labels that represent the organisational structure, such
In this way, group names are composed of labels that represent the organisational structure, such
In this way, group names are composed of labels that represent the organisational structure, such
as department, team, and task.
as department, team, and task.

e confusing group names. Adding more descriptive
Without descriptive labels, it is possible to create confusing group names. Adding more descriptive
Without descriptive labels, it is possible to creat
labels takes time and planning, but user group searches and rights assignments are more accurate
labels takes time and planning, but user group searches and rights assignments are more accurate
labels takes time and planning, but user group searches and rights assignments are more accurate
as a result.

An organised system for naming groups makes it easy to locate the correct security group, and
An organised system for naming groups makes it easy to locate the correct security group, and
An organised system for naming groups makes it easy to locate the correct security group, and
lps protect against duplicate naming.
helps protect against duplicate naming.

User Can Log on Using User Name or User Principal Name {R28}:

28 User Can Log on Using User Name or User Principal Name
http://support.microsoft.com/kb/243280
http://support.microsoft.com/kb/243280

The Administrator Accounts Security Planning Guide {R29}:

29 The Administrator Accounts Security Planning Guide
http://www.microsoft.com/technet/security/topics/serversecurity/administratoraccounts/default.mspx
http://www.microsoft.com/technet/security/topics

/serversecurity/administratoraccounts/default.mspx

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 35

Prepared by Microsoft

In addition, following should be considered when creating group names and descriptions:
In addition, following should be considered when creating group names and descriptions:
In addition, following should be considered when creating group names and descriptions:

(cid:1)  Both the name and description of an object can include up to 256 characters
Both the name and description of an object can include up to 256 characters
Both the name and description of an object can include up to 256 characters

(cid:1)  The naming standard should be able to distinguish between security and distribution groups
The naming standard should be able to distinguish between security and distribution groups
The naming standard should be able to distinguish between security and distribution groups
as well as group scope and purpose. For example security groups could be prefixed with
as well as group scope and purpose. For example security groups could be prefixed with
as well as group scope and purpose. For example security groups could be prefixed with
SEC and distribution groups prefixed with a DIST. The scope of the group could
SEC and distribution groups prefixed with a DIST. The scope of the group could be
SEC and distribution groups prefixed with a DIST. The scope of the group could
identified with the use of GLO (for Global security groups), DLG (for Domain Local Groups)
identified with the use of GLO (for Global security groups), DLG (for Domain Local Groups)
identified with the use of GLO (for Global security groups), DLG (for Domain Local Groups)
and UNI (Universal Security Groups). A typical naming scheme for group names is <type>-
and UNI (Universal Security Groups). A typical naming scheme for group names is <type>
and UNI (Universal Security Groups). A typical naming scheme for group names is <type>
<scope>-<description>

<description> for example, SEC-GLO-InternetAccessAllowed

(cid:1)  The first 20 characters of the name are usually visible in a list without resizing columns and
20 characters of the name are usually visible in a list without resizing columns and
20 characters of the name are usually visible in a list without resizing columns and
scrolling. When viewing the Properties dialog box of the object, about 50 characters of the
scrolling. When viewing the Properties dialog box of the object, about 50 characters of the
scrolling. When viewing the Properties dialog box of the object, about 50 characters of the
viate any organisational labels used
name are viewable. It is current best practice to abbreviate any organisationa
name are viewable. It is current best practice to abbre
in the object name to ensure that the distinguishing portion of the object name can be
in the object name to ensure that the distinguishing portion of the object name can be
in the object name to ensure that the distinguishing portion of the object name can be
viewed in these environments
viewed in these environments

6.1.7.3.3

Workstation Computer Account Names
Workstation Computer Account Names

Each computer account created in AD DS has the following names:
Each computer account created in

(cid:1)  A relative distinguished na

A relative distinguished name

(cid:1)  A pre-Windows 2000 computer name (Security Account Manager (SAM) account name)
Windows 2000 computer name (Security Account Manager (SAM) account name)
Windows 2000 computer name (Security Account Manager (SAM) account name)

(cid:1)  A primary DNS suffix

(cid:1)  A DNS host name

(cid:1)  A Service Principal Name (SPN)
A Service Principal Name (SPN)

The administrator enters the computer name when creating the computer account. This computer
The administrator enters the computer name when creating the computer account. This computer
The administrator enters the computer name when creating the computer account. This computer
as the LDAP relative distinguished name.
name is used as the LDAP relative distinguished name.

Windows 2000 name is used, including the first 15 bytes of the relative
AD DS suggests the pre-Windows 2000 name is used, including the first 15 bytes of the relative
Windows 2000 name is used, including the first 15 bytes of the relative
Windows 2000 name at any time.
distinguished name. The administrator can change the pre-Windows 2000 name at any time.
distinguished name. The administrator can change the pre

The DNS name for a host, also th
e full computer name, is a DNS fully qualified domain name
The DNS name for a host, also the full computer name, is a DNS fully qualified domain name
(FQDN). The full computer name is a concatenation of the computer name (the first 15 bytes of the
(FQDN). The full computer name is a concatenation of the computer name (the first 15 bytes of the
(FQDN). The full computer name is a concatenation of the computer name (the first 15 bytes of the
SAM account name of the computer account without the "$" character) and the primary DNS suffix
SAM account name of the computer account without the "$" character) and the primary DNS suffix
SAM account name of the computer account without the "$" character) and the primary DNS suffix
DNS domain name of the domain in which the computer account exists). It is listed on the
DNS domain name of the domain in which the computer account exists). It is listed on the
(the DNS domain name of the domain in which the computer account exists). It is listed on the
tab in System Properties in the Control Panel.
Computer Name tab in System Properties in the Control Panel.

When creating a workstation build, it is important to have a consistent workstation naming
When creating a workstation build, it is important to have a consistent workstation naming
When creating a workstation build, it is important to have a consistent workstation naming
convention to ease support and to avoid duplicate network names, see the
guidance document for more information.
Healthcare Desktop and Server Guide {R4} guidance document for more information.
Healthcare Desktop and Server Guide

Automated Build
ease support and to avoid duplicate network names, see the Automated Build

Recommendations

wide computer naming standard should be implemented that allows for, and conforms to,
An organisation-wide computer naming standard should be implemented that allows for, and conforms to,
wide computer naming standard should be implemented that allows for, and conforms to,
the following criteria:
(cid:1)  Workstation names should be easy for users to remember
ion names should be easy for users to remember
(cid:1)  Workstation names identify the location of the workstation
Workstation names identify the location of the workstation
(cid:1)  Select names that describe the type of workstation
Select names that describe the type of workstation
(cid:1)  Use unique names for all computers in the

. Do not assign the same computer name to
Use unique names for all computers in the organisation. Do not assign the same computer name to
ferent computers in different DNS domains
different computers in different DNS domains

(cid:1)  Do not use the character case to convey the owner or purpose of a computer, because DNS is not
Do not use the character case to convey the owner or purpose of a computer, because DNS is not
Do not use the character case to convey the owner or purpose of a computer, because DNS is not
case-sensitive

An example of a workstation naming standard could be of the form illustrated in Table 12, where
An example of a workstation naming standard could be of the form illustrated in
An example of a workstation naming standard could be of the form illustrated in
the workstation name is DTRHW00001

DTRHW00001:

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 36

Prepared by Microsoft

Machine Number or Asset Number
Machine Number or Asset Number

00001 OR A567B

Example Use

Laptop

Desktop

Tablet

Pocket PC

LT

DT

TP

PP

BERKSHIRE NHS FOUNDATION TRUST)
RHW (ROYAL BERKSHIRE NHS FOUNDATION TRUST)

Machine number could be a sequential number, such as
Machine number could be a sequential number, such as 00001,
whereas Asset Number is the official Asset Tag, such as A567B
whereas Asset Number is the official Asset Tag, such as

Computer Type

DT

Location
Location

RHW
RHW

Workstation Naming Standard
Table 12: Example Workstation Naming Standard

Where the following is the case:
Where the following is the case:

Component

Computer Type

A two character code indicating the machine type
A two character code indicating the machine type

Location

A three character site code

Machine Number or Asset Number

Table 13: Recommended Workstation Naming

Recommended Workstation Naming Convention

Recommendation

It is recommended that the healthcare organisation
detailed in Table 13.

use an asset number and machine type scheme, as
healthcare organisation use an asset number and machine type scheme, as

6.1.7.3.4

Server Computer Account Names
Server Computer Account Names

The naming convention for servers should follow a similar standard to that of the workstations. The
The naming convention for servers should follow a similar standard to that of the workstations. The
The naming convention for servers should follow a similar standard to that of the workstations. The
te the server role rather than the
difference would be that the two-character code would indicate the server role rather than the
difference would be that the two
machine type.

character codes that could be used to identify
provides examples of server roles and two-character codes that could be used to identify
Table 14 provides examples of server roles and two
em. Only the most common server roles have been given, therefore the table is not exhaustive.
them. Only the most common server roles have been given, therefore the table is not exhaustive.
em. Only the most common server roles have been given, therefore the table is not exhaustive.

Server Role

Domain Controller

File Server

Print Server

SQL Server

WSUS Server

Anti-Virus Server

Web Server

Application Server (not fitting into another named role)
Application Server (not fitting into another named role)

Two-Character Codes

DC

FS

PR

SQ

WU

AV

WW

AP

Multi-role server (for example, File/Print/WSUS/Custom Application)

role server (for example, File/Print/WSUS/Custom Application)  MR

Proxy Server

PX

: Example Server Role Naming Standards
Table 14: Example Server Role Naming Standards

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 37

Prepared by Microsoft

6.1.7.3.5

Organisational Unit Names
Organisational Unit Names

OU structure is not intended to be visible to end users. The OU structure is an
The AD DS OU structure is not intended to be visible to end users. The OU structure is an
OU structure is not intended to be visible to end users. The OU structure is an
administrative tool for Service and Data Administrators.
administrative tool for Service and Data Administrators.

Recommendation

should reflect the objects contained within the
The names used to represent the OU object within AD DS should reflect the objects contained within the
The names used to represent the OU object within
organisation and the administrative and policy
the best practice recommendations for the OU structure, see the Group Policy for Healthcare
the best practice recommendations for the OU structure, see the
guidance document.
Management {R20} guidance document.

and the administrative and policy-based structure for the OUs. For detailed information on
based structure for the OUs. For detailed information on
Healthcare Desktop

6.1.7.3.6

Site and Site Link Names
Site and Site Link Names

by site and subnet objects. The replication path
Sites and subnets are represented in AD DS by site and subnet objects. The replication path
Sites and subnets are represented in
between sites is designated to AD DS by use of site link objects.
between sites is designated to

Important

It is recommended to use legal DNS names when creating new site names, otherwise the site will only be
It is recommended to use legal DNS names when creating new site names, otherwise the site will only be
It is recommended to use legal DNS names when creating new site names, otherwise the site will only be
accessible where a Microsoft DNS server is used. The primary reason for this is that site names are
accessible where a Microsoft DNS server is used. The primary reason for this is that site names are
accessible where a Microsoft DNS server is used. The primary reason for this is that site names are
st therefore adhere to DNS naming rules. It is also advisable that site names
published in DNS and must therefore adhere to DNS naming rules. It is also advisable that site names
st therefore adhere to DNS naming rules. It is also advisable that site names
should not consist entirely of numbers.
should not consist entirely of numbers.

Sites should have easily identifiable and standardised national codes associated with them to aid
Sites should have easily identifiable and standardised national codes associated with them to aid
Sites should have easily identifiable and standardised national codes associated with them to aid
administrators with locating sites and site links.
administrators with locating sites and

Recommendation

should only use Internet standard characters
The name for the site object that will be created in AD DS should only use Internet standard characters
The name for the site object that will be created in
and should contain the name of the organisation, as well as the Site code for the location of the site to aid
, as well as the Site code for the location of the site to aid
and should contain the name of the
code>< Site Code><number>.
IT Administration, such that, the format will be, <Healthcare Organisation code>< Site Code><number>
IT Administration, such that, the format will be,

For example, a North London Hospital in
site name CONNLH3901. Table
for this example:

Hospital in a healthcare organisation called Contoso
Table 15 provides a breakdown of the meaning of the si

a healthcare organisation called Contoso would have the
provides a breakdown of the meaning of the site object name

Characters

Identifier

Value

Example

1-3

4-8

9-10

Healthcare Organisation Code
Healthcare Organisation

3 character combination of letters or letters and numbers  CON
3 character combination of letters or letters and numbers

Site Code

5 character combination of letters or letters and numbers  NLH39
5 character combination of letters or letters and numbers

Sequential number

01-99

01

Table 15: Site Object Naming Convention

Site link objects require a straightforward
link for ease of administration.

naming structure that easily identifies both ends of the
straightforward naming structure that easily identifies both ends of the

Recommendation

ed, separated by a hyphen
Site Link object names can be generated from two sites which are interconnected, separated by a hyphen
Site Link object names can be generated from two sites which are interconnect
(-). For example, linking the North London
would give a site link object name of:
Contoso would give a site link object name of:

North London Hospital in Contoso with the Manchester

 Hospital in the

0101
CONNLH3901-CONMAH0101

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 38

6.2  Design an AD DS

DS Physical Structure

Prepared by Microsoft

The AD DS physical structure incorporates the following components of

physical structure incorporates the following components of AD DS

DS:

(cid:1)  Site topology

(cid:1)  Domain controller placement
placement

(cid:1)  Operations Master role placement
role placement

(cid:1)  Hardware availability and scalability requirements
Hardware availability and scalability requirements

The site topology is a logical representation of the physical
The site topology is a logical representation of the physical network. Designing an
topology involves planning for
placement and designing sites, subnets, site links
topology involves planning for domain controller placement and designing sites, subnets, site links
and site link bridges, to ensure efficient routing of authentication, query and replication traffic.
and site link bridges, to ensure efficient routing of authentication, query and replication traffic.
and site link bridges, to ensure efficient routing of authentication, query and replication traffic.

network. Designing an AD DS site

Planning domain controller placement and capacity helps determine the appropriate number of
placement and capacity helps determine the appropriate number of
placement and capacity helps determine the appropriate number of
domain controllers to place in each domain that is represented in a site. Capacity planning also
to place in each domain that is represented in a site. Capacity planning also
to place in each domain that is represented in a site. Capacity planning also
so that cost can be
assists in estimating the hardware requirements for each
assists in estimating the hardware requirements for each domain controller so that cost c
minimised and an effective service level is maintained for the users.
minimised and an effective service level

Before beginning to design the site topology, it is important that the following components of AD DS
Before beginning to design the site topology, it is important that the following components of
Before beginning to design the site topology, it is important that the following components of
have been designed and reviewed:
have been designed and reviewed:

(cid:1)  AD DS logical structure, including the adminis

trative hierarchy, forest plan, and domain plan
logical structure, including the administrative hierarchy, forest plan, and domain plan

for each forest (see section 6.1)
for each forest (see section

(cid:1)  DNS infrastructure design for

DNS infrastructure design for AD DS (see section 6.4.1)

Collect Network Information
6.2.1  Collect Network Information

physical components, it is important to understand the
Before beginning to design the AD DS physical components, it is important to understand the
Before beginning to design the
d devices. The following components should be identified and
existing physical network structure and devices. The following components should be identified and
existing physical network structure an
documented:

(cid:1)  A location map that represents the physical network infrastructure of the
A location map that represents the physical network infrastructure of the healthcare
A location map that represents the physical network infrastructure of the
organisation

(cid:1)  List communication links and available bandwidth. It is advised that this is document
List communication links and available bandwidth. It is advised that this is documented
List communication links and available bandwidth. It is advised that this is document
job aid, named
Geographic Locations and Communication Links job aid, named
using the Geographic Locations and Communication Links
DSSTOPO_1.doc {R14

R14}

(cid:1)  List IP subnets within each location. It is advised that this is documented using the
List IP subnets within each location. It is advised that this is documented using the
List IP subnets within each location. It is advised that this is documented using the
Locations and Subnets job aid, named DSSTOPO_1.doc {R14}
Locations and Subnets

(cid:1)  List domains and number of users for each location. It is advised that this is documented
List domains and number of users for each location. It is advised that this is documented
List domains and number of users for each location. It is advised that this is documented
DSSTOPO_1.doc {R14}
using the Domains and Users in Each Location

Domains and Users in Each Location job aid, named DSSTOPO_1.doc

Domain Controller Placement
6.2.2  Domain Controller Placement

After gathering all of the network information that will be used to design the site topology, planning
After gathering all of the network information that will be used to design the site topology
After gathering all of the network information that will be used to design the site topology
in controllers should take
where to place domain controllers
place.

domain controllers including regional and forest root domain controllers

Note

This process does not include the identification of the proper number of domain controllers
This process does not include the identification of the proper number of
hardware requirements for each domain represented in each site. This is covered in
domain controller hardware requirements for each domain represented in each site. This is covered in
hardware requirements for each domain represented in each site. This is covered in
section 6.2.7.

domain controllers and the

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 39

6.2.2.1

Plan Forest Root Domain Controller Placement
Plan Forest Root Domain Controller Placement

Prepared by Microsoft

Forest root domain controllers
clients that need to access resources in domains other than their own, and for hosting the
clients that need to access resources in domains other than their own, and for hosting the
clients that need to access resources in domains other than their own, and for hosting the
These are covered in section 6.2.3.
Operations Master Roles. These are covered in section

 are needed to establish the forest, create AD DS

DS trust paths for

Recommendations
(cid:1)  As a single domain forest is being recommended, this production domain is also the forest root
As a single domain forest is being recommended, this production domain is also the forest root
As a single domain forest is being recommended, this production domain is also the forest root
domain

(cid:1)  For both centralised and distributed implementation scenarios, there should be at least two
For both centralised and distributed implementation scenarios, there should be at least two domain
For both centralised and distributed implementation scenarios, there should be at least two
yed to assume forest root functions and provide a basic level of resilience for the
controllers deployed to assume forest root functions and provide a basic level of resilience for the
yed to assume forest root functions and provide a basic level of resilience for the
authentication service
AD DS authentication service

(cid:1)  The domain controllers covering forest root functions should, where possible, be hosted within a
covering forest root functions should, where possible, be hosted within a
covering forest root functions should, where possible, be hosted within a

ere is only a single central data centre, the two forest root
centralised hub or data centre location. If th
centralised hub or data centre location. If there is only a single central data centre
located in different physical locations to provide a degree of resilience.
domain controllers should be located in different physical locations to provide a degree of resilience.
domain controllers should be

ontroller placement design decisions are
It is recommended that the forest root domain controller placement design decisions are
It is recommended that the forest root
documented using the Domain Controller Placement

Domain Controller Placement job aid, named DSSTOPO_4.doc

DSSTOPO_4.doc {R14}.

6.2.2.2

Plan Additional Domain Controller Placement
Plan Additional Domain Controller Placement

as possible outside of the
For cost efficiency, plan to place as few regional domain controllers as possible outside of the
For cost efficiency, plan to place as
is required locally,
centralised hub or data centre. Evaluate whether a regional domain controller is required locally,
centralised hub or data centre. Evaluate whether a regional
based on centralised hub and distributed satellite locations within the healthcare organisation
based on centralised hub and distributed satellite locations within the

healthcare organisation.

When planning domain controller
consider the following points:

placement, regardless of which domain it is for, it is critical to
domain controller placement, regardless of which domain it is for, it is critical to

(cid:1)  Domain controller physical security
physical security

(cid:1)  Remote management strategy
Remote management strategy

(cid:1)  WAN link availability

(cid:1)  Authentication availability
Authentication availability

(cid:1)  Logon performance over WAN link
performance over WAN link

(cid:1)  Remote applications and services that depend on directory services
Remote applications and services that depend on directory services

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 40

at a satellite location, see the decision tree
To help determine whether to place a domain controller at a satellite location, see the decision tree
To help determine whether to place a
in Figure 8:

Prepared by Microsoft

: Determining Whether to Place Domain Controllers at Satellite Locations
Figure 8: Determining Whether to Place Domain Controllers at Satellite Locations

Recommendations

domain controller.
It is possible, in small sites, to have multiple services running on a single domain controller.
It is possible, in small sites, to have multiple services running on a single

Typically, these services include: AD DS-integrated DNS, WINS and DHCP. However, it is not current
integrated DNS, WINS and DHCP. However, it is not current
Typically, these services include:
best practice for full read / write
ovide additional services to the network due to
best practice for full read / write domain controllers to provide additional services to the network due to
potential security risks. It is therefore current best practice to minimise the number of service
potential security risks. It is therefore current best practice to minimise the number of service
potential security risks. It is therefore current best practice to minimise the number of service
administrators, applications and services that are installed on read / write domain controllers
administrators, applications and services that are installed on read / write
minimise these risks.

domain controllers to help

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 41

Prepared by Microsoft

hosted application and
virtual instance on the server) should be taken in configuring the co-hosted application and

prohibitive, additional measures (such as running each application
Where this is not appropriate or is cost-prohibitive, additional measures (such as running each application
Where this is not appropriate or is cost
in its own virtual instance on the server
operating system security policies, to mitigate the associated risk. Windows Server 2008 R2 also offers
olicies, to mitigate the associated risk. Windows Server 2008 R2 also offers
olicies, to mitigate the associated risk. Windows Server 2008 R2 also offers
the option of deploying a Read Only Domain Controller (RODC) to further enhance the security of the
the option of deploying a Read Only Domain Controller (RODC) to further enhance the security of the
the option of deploying a Read Only Domain Controller (RODC) to further enhance the security of the
on a shared physical server
domain information making the decision to host domain controller functionality on a shared physical server
domain information making the decision to host domain controller functionality
with other services such as DHCP and DNS. To ensure the security database integrity
with other services such as DHCP and DNS
should be located in a physically secure server room with audited access control, and
should be located in a physically secure server room with audited access control
domain controllers should be located in a physically secure server room with audited access control
net with access restricted to the IT Administrators.
kept in a locked cabinet with access restricted to the IT Administrators.

o ensure the security database integrity, Active Directory

infrastructure environments may consider the implementation
Healthcare organisation infrastructure environments may consider the implementation

domain controllers after careful review of the performance requirements within the n

Large or distributed Healthcare organisation
of additional domain controllers
For example:
(cid:1)  The user population exceeds 50 in a remote location and where they are authenticating over a low
The user population exceeds 50 in a remote location and where they are authenticating over a low
The user population exceeds 50 in a remote location and where they are authenticating over a low
bandwidth WAN link to the hub site
bandwidth WAN link to the hub site

after careful review of the performance requirements within the network.

(cid:1)  If the users are performing network intensive transactions across a WAN link
If the users are performing network intensive transactions across a WAN link
(cid:1)  Running applications that

require frequent access to a domain controller or a GC
Running applications that require frequent access to a domain controller or a GC

domain controller
Windows Server 2008 introduces a new option to consider when planning domain controller
Windows Server 2008 introduce
placement, namely Read Only Domain Controllers (RODCs). The advantage of an RODC is that it
placement, namely Read Only Domain Controllers (RODCs). The advantage of an RODC is that it
placement, namely Read Only Domain Controllers (RODCs). The advantage of an RODC is that it
performs the major functions of a domain controller by authenticating users. However, it also
unctions of a domain controller by authenticating users. However, it also
unctions of a domain controller by authenticating users. However, it also
addresses many of the security concerns of businesses when placing domain controllers in remote
addresses many of the security concerns of businesses when placing domain controllers in remote
addresses many of the security concerns of businesses when placing domain controllers in remote
locations through some specific capabilities and restrictions:
locations through some specific capabilities and restrictions:

(cid:1)  Read Only: As the name suggests these are domain controllers that only provide read
: As the name suggests these are domain controllers that only provide read
: As the name suggests these are domain controllers that only provide read

(cid:1)  Unidirectional replication

an RODC. Therefore RODCs will only
, there is no need to support replication from an RODC. Therefore RODCs will only

. This means that it is not possible to make changes to AD DS on a RODC
. This means that it is not possible to make changes to
access to AD DS. This means that it is not possible to make changes to
and have them replicate around the rest of the domain or forest
and have them replicate around the rest of the domain or forest
cause RODCs will not be used to initiate any changes to
Unidirectional replication: Because RODCs will not be used to initiate any changes to
AD DS, there is no need to support replication
replicate in one direction, from a read / write domain controller. This not only applies to
replicate in one direction, from a read / write domain controller. This not only applies to
replicate in one direction, from a read / write domain controller. This not only applies to
to the supporting services such as SYSVOL and DNS. This also helps
to the supporting services such as SYSVOL and DNS. This also helps
AD DS itself but also to the supporting services such as SYSVOL and DNS. This also helps
to reduce the replication load on Bridgehead servers in the data centre as they can support
to reduce the replication load on Bridgehead servers in the data centre as they can support
to reduce the replication load on Bridgehead servers in the data centre as they can support
more outbound replication partners or reduce the amount of time spent replicating
more outbound replication partners or reduce the amount of time spent replicating
more outbound replication partners or reduce the amount of time spent replicating
ication is a parallel activity for a domain controller whereas inbound
ication is a parallel activity for a domain controller whereas inbound
(outbound replication is a parallel activity for a domain controller whereas inbound
replication is serial)

(cid:1)  Filtered Attribute Set: Although an RODC is a fully functional domain controller it does not
: Although an RODC is a fully functional domain controller it does not
: Although an RODC is a fully functional domain controller it does not
automatically replicate all information. To enhance the security adva
ntages of an RODC
automatically replicate all information. To enhance the security advantages of an RODC
there is a set of attributes and objects that are not replicated to an RODC. These rules are
there is a set of attributes and objects that are not replicated to an RODC. These rules are
there is a set of attributes and objects that are not replicated to an RODC. These rules are
managed via the Filtered Attribute Set property of an RODC. Examples of information that
managed via the Filtered Attribute Set property of an RODC. Examples of information that
managed via the Filtered Attribute Set property of an RODC. Examples of information that
is not replicated includes PKI Account credentials, BitL
ocker recovery information and the
is not replicated includes PKI Account credentials, BitLocker recovery information and the
passwords of the built in privileged accounts such as Administrator. The RODC will cache
passwords of the built in privileged accounts such as Administrator. The RODC will cache
passwords of the built in privileged accounts such as Administrator. The RODC will cache
user credentials as and when they authenticate against it thus reducing the number of
user credentials as and when they authenticate against it thus reducing the number of
user credentials as and when they authenticate against it thus reducing the number of
olen or compromised. It is possible to pre-
users who will be at risk should an RODC be stolen or compromised. It is possible to pre
users who will be at risk should an RODC be st
load the RODC cache to improve performance
load the RODC cache to improve performance

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 42

Prepared by Microsoft

(cid:1)  Administrative Role Separation:

The design of a RODC allows for separation of
Administrative Role Separation: The design of a RODC allows for separation of
administrative roles by using a separate Kerberos Key Distribution Centre (KDC) account to
by using a separate Kerberos Key Distribution Centre (KDC) account to
by using a separate Kerberos Key Distribution Centre (KDC) account to
the one used by the read / write domain controllers. This also makes it possible to support
he one used by the read / write domain controllers. This also makes it possible to support
he one used by the read / write domain controllers. This also makes it possible to support
delegating administrative privileges to non
domain administrators for the management and
delegating administrative privileges to non-domain administrators for the management and
maintenance of the RODC without compromising the security of the domain. This makes it
maintenance of the RODC without compromising the security of the domain. Thi
maintenance of the RODC without compromising the security of the domain. Thi
easier to support multiple applications and services running on a domain controller as there
easier to support multiple applications and services running on a domain controller as there
easier to support multiple applications and services running on a domain controller as there
is no longer the same security risk
is no longer the same security risk

(cid:1)  Security: This is addressed in a number of ways by RODCs. Firstly they do not cache or
This is addressed in a number of ways by RODCs. Firstly they do not cache or
This is addressed in a number of ways by RODCs. Firstly they do not cache or
maintained in the domain.
replicate privileged account information or significant ‘secrets’ maintained in the domain.
replicate privileged account
by default only the users that authenticate
Secondly they will only cache a subset of users – by default only the users that authenticate
Secondly they will only cache a subset of users
that an RODC is stolen or compromised there is an
against the RODC. Thirdly, in the event that an RODC is stolen or compromised there is an
against the RODC. Thirdly, in the even
reset the password of all the user accounts whose credentials have been cached
option to reset the password of all the user accounts whose credentials have been cached
reset the password of all the user accounts whose credentials have been cached
by the RODC

administrators to provide
The capabilities introduced by RODCs add another option for AD DS administrators to provide
The capabilities introduced by RODCs add another option for
the directory. Because
authentication services locally to users while ensuring the security of the directory. Because
authentication services locally to users while ensuring the security of
opens the possibility of hosting
RODCs provide the separation of administration capabilities, it re-opens the possibility of hosting
RODCs provide the separation of administration capabilities, it re
multiple services on a single server.
multiple services on a single server.

ontroller placement design decisions are
It is recommended that the additional domain controller placement design decisions are
It is recommended that the additional
documented using the Domain Controller Placement

Domain Controller Placement job aid, named DSSTOPO_4.doc

DSSTOPO_4.doc {R14}.

6.2.2.3

Branch Office Infrastructure Solution
Branch Office Infrastructure Solution

The Branch Office Infrastructure Solution (BOIS) version 3 for Microsoft Windows Server 2008 is a
The Branch Office Infrastructure Solution (BOIS) version 3 for Microsoft Windows Server 2008 is a
The Branch Office Infrastructure Solution (BOIS) version 3 for Microsoft Windows Server 2008 is a
design information for situations where the
set of publicly available guidance, providing further design information for situations where the
set of publicly available guidance, providing further
consideration of satellite locations needs to be taken into account. The aim of BOIS is to help in the
consideration of satellite locations needs to be taken into account. The aim of BOIS is to help in the
consideration of satellite locations needs to be taken into account. The aim of BOIS is to help in the
following areas:

(cid:1)  More efficient use of hardware and software
More efficient use of hardware and software

(cid:1)  More efficient systems administration and

More efficient systems administration and management

(cid:1)  Faster and more complete recovery of data in the event of a disaster
and more complete recovery of data in the event of a disaster

(cid:1)  Higher degree of standardisation
Higher degree of standardisation

could benefit from using the BOIS guides, in conjunction with this
A healthcare organisation could benefit from using the BOIS guides, in conjunction with this
could benefit from using the BOIS guides, in conjunction with this
guidance document, to help plan for remote satellite locations which require multiple server roles to
te locations which require multiple server roles to
guidance document, to help plan for remote satelli
service users. BOIS can be viewed online at the Branch Office TechCenter30 or can be downloaded
or can be downloaded
service users. BOIS can be viewed online
from the Microsoft Download Center31.
from the Microsoft Download Center

Operations Master Role Placement
6.2.3  Operations Master Role Placement

used to design the site topology, plan where to locate the
Using the gathered network information used to design the site topology, plan where to locate the
Using the gathered network information
that will host the operations master roles and GCs.
domain controllers that will host the operations master roles and GCs.

6.2.3.1

Determine Global Catalog Placement
Determine Global Catalog Placement

Assuming the healthcare organisation
forest, all domain controllers can

can (and should) act as GCs.

healthcare organisation follow the recommended guidance of having a single dom

follow the recommended guidance of having a single domain

30 Branch Office TechCenter {R32}:
us/branchoffice/default.aspx
http://technet.microsoft.com/en-us/branchoffice/default.aspx

31 Branch Office Infrastructure Solution for Windows Server 2008
Branch Office Infrastructure Solution for Windows Server 2008
E0232B5C59E3&displaylang=en
http://www.microsoft.com/downloads/details.aspx?familyid=02057405-49AF-4867-BF1D-E0232B5C59E3&displaylang=en
http://www.microsoft.com/downloads/details.aspx?familyid=02057405

Page 43

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Recommendation

Prepared by Microsoft

For a single domain forest, configure all
database content of a domain controller
lookups across GC servers within the single domain forest, ensure that all domain controllers
lookups across GC servers within the single domain forest, ensure that all
configured as GCs.

configure all domain controllers as GC servers. In a single domain forest, the
as GC servers. In a single domain forest, the
Therefore, to load-balance client

domain controller and a GC server are the same. Therefore, to load

domain controllers are

design should vary from the single domain forest, it is necessary to determine GC
If the AD DS design should vary from the single domain forest, it is necessary to determine GC
design should vary from the single domain forest, it is necessary to determine GC
based on the following points:
placement based on the following points:

(cid:1)  GC-aware application presence
aware application presence

(cid:1)  The number of users at the location
The number of users at the location

(cid:1)  Whether the WAN link is 100 percent available
Whether the WAN link is 100 percent available

(cid:1)  Whether roaming users work at the location
Whether roaming users work at the location

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 44

displays a decision tree that may be used to determine the placement of the GC servers:
Figure 9 displays a decision tree that may be used to determine the placement of the GC servers:
displays a decision tree that may be used to determine the placement of the GC servers:

Prepared by Microsoft

: Determining the Placement of Global Catalog Servers
Figure 9: Determining the Placement of Global Catalog Servers

Recommendation

If a multiple domain forest has been deployed, the provision of GC should be further investigated32 based
If a multiple domain forest has been deployed, the provision of GC should be further investigated
If a multiple domain forest has been deployed, the provision of GC should be further investigated
on the information provided in Figure 9 to determine the requirements.
on the information provided in

Windows Server 2008 R2 AD DS  Deployment Guide Web page {R33}:

32 Windows Server 2008 R2 AD DS  Deployment Guide Web page
us/library/cc732877(WS.10).aspx
 http://technet.microsoft.com/en-us/library/cc732877(WS.10).aspx

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 45

Prepared by Microsoft

For all of the scenarios that dictate placing a GC at a location there is the further question of
For all of the scenarios that dictate placing a GC at a location there is the further question of
For all of the scenarios that dictate placing a GC at a location there is the further question of
whether to place a full read / write domain controller or an R
ODC. For any situations where there is
whether to place a full read / write domain controller or an RODC. For any situations where there is
any doubt about the physical security of the domain controller or whether there is a need to provide
any doubt about the physical security of the domain controller or whether there is a need to provide
any doubt about the physical security of the domain controller or whether there is a need to provide
local administration access to the server, a RODC should be considered instead of a full read /
local administration access to the server, a RODC should be considered instead of a full read /
local administration access to the server, a RODC should be considered instead of a full read /
write domain controller.

It is recommended that the GC server placement design decisions are documented using the
It is recommended that the GC server placement design decisions are documented using the
It is recommended that the GC server placement design decisions are documented using the
Domain Controller Placement job aid, named

 job aid, named DSSTOPO_4.doc {R14}.

6.2.3.2

Determine Placement of the

Role Holders
mine Placement of the Operations Master Role Holders

There are five Operations Master

provides details on their roles.
Operations Master roles within a forest. Table 16 provides details on their roles.

Operations Master Role

Role Type
Role Type

Description

PDC Emulator

Domain level role
Domain level role

RID Master

Domain level role
Domain level role

Performs a number of tasks including processing all replication requests
Performs a number of tasks including processing all replication requests
from Microsoft Windows NT 4.0 Backup Domain Controllers (BDCs) and
from Microsoft Windows NT 4.0 Backup Domain Controllers (BDCs) and
processing all password updates for clients that are not running AD DS
processing all password updates for clients that are not running
client software

Allocates relative identifiers (RID) to all domain controllers to ensure that
Allocates relative identifiers (RID) to all domain controllers to ensure that
all security principals have a unique identifier

Infrastructure Master

Domain level role
Domain level role

Maintains a list of the security principals from other domains that are
Maintains a list of the security principals from other domains that are
members of groups within its domain

Schema Master

Forest level role
Forest level role

Governs changes to the schema

Domain Naming Master

Forest level role
Forest level role

Adds and removes Naming Contexts (such as domains), to and from the
Adds and removes Naming Contexts (such as domains), to and from the
forest

Table 16: Operations Master Roles

Recommendations

single domain forest covering a healthcare organisation, it is recommended that the

For a single domain forest covering a healthcare organisation
Master roles are left on the first

roles are left on the first domain controller commissioned.

, it is recommended that the Operations

is high and causing any performance
Operations Master role holder domain controller is high and causing any performance

If the load on an Operations Master
problems, then it may be necessary to relocate individual roles to separate
problems, then it may be necessary to relocate individual roles to separate domain controllers
FSMO (Flexible Single Master Operations)
guidance in the Microsoft Knowledge Base article 223346: FSMO (Flexible Single Master Operations)
guidance in the Microsoft Knowledge Base article 223346:
placement and optimization on

ptimization on Active Directory domain controllers33.

domain controllers as per the

FSMO placement and optimization on Active Directory domain controllers {R34}:

33 FSMO placement and optimization on
http://support.microsoft.com/kb/223346
 http://support.microsoft.com/kb/223346

Page 46

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Prepared by Microsoft

Should a single domain forest implementation not be suitable, it is necessary to carefully plan the
Should a single domain forest implementation not be suitable, it is necessary to carefully plan the
Should a single domain forest implementation not be suitable, it is necessary to carefully plan the
placement of the Operations Master
determined by the identification of the following components and their effect on an Operations
determined by the identification of the following components and their effect on an
determined by the identification of the following components and their effect on an
Master:

Operations Master role holders34. The Operations Master role loads

role loads can be

(cid:1)  Legacy clients, such as Windows NT

Legacy clients, such as Windows NT® 4.0

(cid:1)  Password change forwarding and logon forwarding requests with mismatched passwords
Password change forwarding and logon forwarding requests with mismatched passwords
Password change forwarding and logon forwarding requests with mismatched passwords
and service accounts
for users, computers, and service accounts

(cid:1)  RID and PDC emulator load/communication
RID and PDC emulator load/communication

(cid:1)  Group Policy updates

(cid:1)  The initial update of DFS
The initial update of DFS

role placement are
It is recommended that the design decisions for the Operations Master role placement are
It is recommended that the design decisions for the
DSSTOPO_4.doc {R14}.
documented using the Domain Controller Placement

Domain Controller Placement job aid, named DSSTOPO_4.doc

Create a Site Design
6.2.4  Create a Site Design

Creating a site design involves deciding which locations will become sites, creating site objects,
Creating a site design involves deciding which locations will become sites, creating site objects,
Creating a site design involves deciding which locations will become sites, creating site objects,
g subnet objects, and associating the subnets with sites.
creating subnet objects, and associating the subnets with sites.

replication traffic. A well-
Designing a site topology helps efficiently route client queries and AD DS replication traffic. A well
Designing a site topology helps efficiently route client queries and
achieve the following benefits:
designed site topology will help the healthcare organisation achieve the following benefits:
designed site topology will help the

(cid:1)  Minimise the cost of replicating

data, for example, bandwidth, time, and effort
inimise the cost of replicating AD DS data, for example, bandwidth, time, and effort

(cid:1)  Minimise administrative efforts that are required to maintain the site topology
Minimise administrative efforts that are required to maintain the site topology
Minimise administrative efforts that are required to maintain the site topology

(cid:1)  Schedule replication that enables locations with slow or dial
-peak hours

up network links to replicate
Schedule replication that enables locations with slow or dial-up network links to replicate
AD DS data during off-

(cid:1)  Optimise the ability of client computers to locate the nearest resources, such as
Optimise the ability of client computers to locate the nearest resources, such as domain
Optimise the ability of client computers to locate the nearest resources, such as
and DFS servers, reducing network traffic over slow WAN links, improving logon
controllers and DFS servers, reducing network traffic over slow WAN links, improving logon
and DFS servers, reducing network traffic over slow WAN links, improving logon
and logoff processes, and speeding up file download operations
and logoff processes, and speeding up file download operations

, the following
For the purposes of the site topology design within a healthcare organisation, the following
For the purposes of the site topology design within a
adhered to:
guidelines should be adhered to:

(cid:1)  Small infrastructure environments should typically have fewer than 75 seats on a single IP
Small infrastructure environments should typically have fewer than 75 seats on a single IP
Small infrastructure environments should typically have fewer than 75 seats on a single IP
Subnet on a single LAN (being determined as a network having high speed interconnects of
Subnet on a single LAN (being determined as a network having high speed interconnects of
Subnet on a single LAN (being determined as a network having high speed interconnects of
greater than 10Mb/s) with little or no server infrastructure
greater than 10Mb/s) with little or no server infrastructure

(cid:1)  Distributed infrastructure environments should have any number of seats being spread over
stributed infrastructure environments should have any number of seats being spread over
stributed infrastructure environments should have any number of seats being spread over

multiple IP Subnets or being on separate LANs interconnected by fully routed WAN
multiple IP Subnets or being on separate LANs interconnected by fully routed WAN
multiple IP Subnets or being on separate LANs interconnected by fully routed WAN
connections, with or without server infrastructure
connections, with or without server infrastructure

Operations Master Role Placement {R35}:

34 Operations Master Role Placement
us/library/cc754889(WS.10).aspx
http://technet.microsoft.com/en-us/library/cc754889(WS.10).aspx

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 47

Prepared by Microsoft

6.2.4.1

Decide Which Locations Will Become Sites
Decide Which Locations Will Become S

Determine the healthcare organisation’s
particular identify the following components:
particular identify the following components:

geographic locations and communication links, in
healthcare organisation’s geographic locations and communication links, in

(cid:1)  Healthcare organisation

hub location, for example, a centralised data centre
Healthcare organisation hub location, for example, a centralised data centre

(cid:1)  Healthcare organisation
tions, for example, a distributed office location such as
Healthcare organisation satellite locations, for example, a distributed office location such as
clinic
a General Practice clinic

(cid:1)  Connection type

(cid:1)  Available bandwidth between locations
Available bandwidth between locations

site design should be created based on the gathered information of the existing physical
An AD DS site design should be created based on the gathered information of the existing physical
site design should be created based on the gathered information of the existing physical
infrastructure. This requires the identification of the
become sites.

locations that will
requires the identification of the healthcare organisation locations that will

Figure 10 displays a decision tree that will act as an ai
become sites.

d when deciding which locations should
displays a decision tree that will act as an aid when deciding which locations should

: Deciding Which Locations Will Become Sites
Figure 10: Deciding Which Locations Will Become Sites

Recommendations
(cid:1)  Create sites for all locations in which it is planned to place
(cid:1)  Create sites for those locations that include servers, which are running applications that require a site
locations that include servers, which are running applications that require a site
locations that include servers, which are running applications that require a site

Create sites for all locations in which it is planned to place domain controllers

to be created, for example DFS
to be created, for example DFS

(cid:1)  If a site is not required for a location, add the subnet of the location to a site for which the location has
If a site is not required for a location, add the subnet of the location to a site for which the location has
If a site is not required for a location, add the subnet of the location to a site for which the location has
the maximum WAN speed and available bandwidth
the maximum WAN speed and availa

It is recommended that site locations, including their network addresses and subnet masks, are
It is recommended that site locations, including their network addresses and subnet masks, are
It is recommended that site locations, including their network addresses and subnet masks, are
DSSTOPO_4.doc {R14}.
documented using the Associating Subnets with Sites

Associating Subnets with Sites job aid, named DSSTOPO_4.doc

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 48

Prepared by Microsoft

6.2.4.2

Create a Site Object Design
Create a Site Object Design

It is recommended that each location where a site is to be created is documented using the
It is recommended that each location where a site is to be created is documented using the
It is recommended that each location where a site is to be created is documented using the
. This job aid can then be
Associating Subnets with Sites job aid, named DSSTOPO_4.doc {R14}. This job aid can then be
Associating Subnets with Sites
used to create the site objects.
used to create the site objects.

6.2.4.3

Create a Subnet Object Design
Create a Subnet Object Design

It is recommended that the IP subnets and subnet masks associated with each location are
It is recommended that the IP subnets and subnet masks associated with each location are
It is recommended that the IP subnets and subnet masks associated with each location are
documented using the Associating Subnets with Sites
This job aid can then be used to create the subnet objects. All subnets that are in use
This job aid can then be used to create the subnet objects.
healthcare organisation should be documented and created in

Associating Subnets with Sites job aid, named DSSTOPO_4.doc

DSSTOPO_4.doc {R14}.
All subnets that are in use within the

should be documented and created in AD DS.

6.2.4.4

Associate Subnets With Sites
Associate Subnets With Sites

Each subnet object should be associated with a site object. It is recommended that these are
Each subnet object should be associated with a site object. It is recommended that these are
Each subnet object should be associated with a site object. It is recommended that these are
documented using the Associating Subnets with Sites
Subnets that are not defined within AD DS will result in event log messages on domain controllers
will result in event log messages on domain controllers
Subnets that are not defined within
tion where the computer has an unrecognised IP address. This is
when users authenticate at a location where the computer has an unrecognised IP address. This is
when users authenticate at a loca
unnecessary noise in the event logs that is easy to eliminate.
unnecessary noise in the event logs that is easy to eliminate.

Associating Subnets with Sites job aid, named DSSTOPO_4.doc

DSSTOPO_4.doc {R14}.

Recommendations
(cid:1)  For a healthcare organisation

with a small centralised infrastructure environment, it is appropriate to
healthcare organisation with a small centralised infrastructure environment, it is appropriate to

t a single Active Directory site
implement a single Active Directory site

(cid:1)  For a healthcare organisation

whose infrastructure is physically distributed, Active Directory sites
healthcare organisation whose infrastructure is physically distributed, Active Directory sites
should ideally be implemented per IP subnet, where the IP subnets are configured to segregate client
should ideally be implemented per IP subnet, where the IP subnets are configured to segregate client
should ideally be implemented per IP subnet, where the IP subnets are configured to segregate client
from server traffic on a network within a LAN environment, or where there is a network distinction of
on a network within a LAN environment, or where there is a network distinction of
on a network within a LAN environment, or where there is a network distinction of
clients based on functional or geographic information that aids management of the client estate
clients based on functional or geographic information that aids management of the client estate
clients based on functional or geographic information that aids management of the client estate

(cid:1)  It is important to ensure that all defined subnets are associated with a site.

Subnets that are not
It is important to ensure that all defined subnets are associated with a site. Subnets that are not
directly associated with a physical location should be linked to the central hub site.
directly associated with a physical location should be linked to the central hub site.
directly associated with a physical location should be linked to the central hub site.

Create a Site Link Design
6.2.5  Create a Site Link Design

Site links reflect the intersite connectivity and method used to transfer replication traffic. It is
Site links reflect the intersite connectivity and method used to transfer replication traffic. It is
Site links reflect the intersite connectivity and method used to transfer replication traffic. It is
sites with site links so that domain controllers at each site can replicate
important to connect sites with site links so that
changes. Site links are used by
and the specific relationship between the individual sites.
and the specific relationship between the individual sites.

administrators to define the preferred replication topology
Site links are used by AD DS administrators to define the preferred replication topology

at each site can replicate AD DS

6.2.5.1

Connect Sites With Site Links
Connect Sites W

To connect sites with site links, the sites to connect with the site link should be identified, a site link
To connect sites with site links, the sites to connect with the site link should be identified, a site link
To connect sites with site links, the sites to connect with the site link should be identified, a site link
Site Transports’ container should be created, and the site link named.
container should be created, and the site link named.
object in the respective ‘Inter-Site Transports’
tes and associated site links should be determined and, in particular,
sites and associated site links should be determined and, in particular,
The healthcare organisation si
the following components should be identified.
the following components should be identified.

(cid:1)  Healthcare organisation

Healthcare organisation site names, following the guidance given in section

site names, following the guidance given in section 6.2.4.1

(cid:1)  Name of site link, following the guidance given in section

, and as documented in
Name of site link, following the guidance given in section 6.1.7.3.6, and as documented in
the Associating Subnets with Sites

Associating Subnets with Sites job aid, named DSSTOPO_4.doc {R14

R14}

(cid:1)  Site link type. When creating the site link object, it is created in either the IP container
ink type. When creating the site link object, it is created in either the IP container
ink type. When creating the site link object, it is created in either the IP container
(which associates the site link with the Remote Call Procedure (RPC) over IP transport) or
(which associates the site link with the Remote Call Procedure (RPC) over IP transport) or
(which associates the site link with the Remote Call Procedure (RPC) over IP transport) or
the Simple Mail Transfer Protocol (SMTP) container (which associates the site link with the
the Simple Mail Transfer Protocol (SMTP) container (which associates the site
the Simple Mail Transfer Protocol (SMTP) container (which associates the site
SMTP transport)

It is recommended that site names and associated site link names are documented using the Site
It is recommended that site names and associated site link names are documented using the
It is recommended that site names and associated site link names are documented using the
job aid, named DSSTOPO_5.doc {R14}.
and Associated Site Links job aid, named

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 49

Recommendation

Prepared by Microsoft

Site Link objects should be created in the IP container. As it is recommended that a
Site Link objects should be created in the IP containe
organisation implements a single domain forest, then RPC over IP is the only s
scale.

ite link type available at this
implements a single domain forest, then RPC over IP is the only site link type available at this

 healthcare

A site link should only contain two sites: the two sites for which the explicit relationship is being defined.
A site link should only contain two sites: the two sites for which the explicit relationship is being defined.
A site link should only contain two sites: the two sites for which the explicit relationship is being defined.
Although it is possible to have more than two sites in a site link,
Although it is possible to have more than two sites in a site link, AD DS will treat all of the sites in t
link as being equally connected and will generate replication connection objects between domain
link as being equally connected and will generate replication connection objects between domain
link as being equally connected and will generate replication connection objects between domain
installations this results in an
controllers in each of the member sites. For the majority of AD DS installations this results in an
controllers in each of the member sites. For the majority of
rollers in remote sites could be attempting to
inappropriate replication topology where domain controllers in remote sites could be attempting to
inappropriate replication topology where domain cont
replicate with each other.

will treat all of the sites in the site

6.2.5.2

Set Site Link Properties
Set Site Link Properties

Intersite replication occurs according to the properties of the connection objects. When the
Intersite replication occurs according to the properties of the connection objects. When the
Intersite replication occurs according to the properties of the connection objects. When the
Knowledge Consistency Checker (KCC) creates connection objects,
it derives the replication
Knowledge Consistency Checker (KCC) creates connection objects, it derives the replication
schedule from properties of the site link objects. Each site link object represents the WAN
schedule from properties of the site link objects. Each site link object represents the WAN
schedule from properties of the site link objects. Each site link object represents the WAN
connection between two or more sites.
connection between two or more sites.

Setting the site link object properties35 includes the following steps:
Setting the site link object properties

(cid:1)  Determining the cost that i

s associated with that replication path. The KCC uses cost to
Determining the cost that is associated with that replication path. The KCC uses cost to
determine the least expensive route for replication between two sites that replicate the
determine the least expensive route for replication between two sites that replicate the
determine the least expensive route for replication between two sites that replicate the
same directory partition
same directory partition

(cid:1)  Determining the schedule that defines the times during which intersite replicati
Determining the schedule that defines the times during which intersite replication can occur
Determining the schedule that defines the times during which intersite replicati

(cid:1)  Determining the replication interval that defines how frequently replication should occur
Determining the replication interval that defines how frequently replication should occur
Determining the replication interval that defines how frequently replication should occur
during the times when replication is allowed, as defined in the schedule
during the times when replication is allowed, as defined in the schedule
during the times when replication is allowed, as defined in the schedule

Recommendations
(cid:1)  When determining the site link cost, the cost should be calculat

ed based on the available bandwidth
When determining the site link cost, the cost should be calculated based on the available bandwidth
and not the link bandwidth of the inter-network link
and not the link bandwidth of the inter

(cid:1)  The KCC should be left on, which is the default setting. Windows Server 200

8 R2 is scalable to over
d regarding switching off the KCC
thousand sites before further design consideration is required regarding switching off the KCC

The KCC should be left on, which is the default setting. Windows Server 2008 R2
three thousand sites before further design consideration is require
and manually configuring a replication topology
and manually configuring a replication topology

Create a Site Link Bridge Design
6.2.6  Create a Site Link Bridge Design

implementations there is no
A site link bridge connects two or more site links. For most AD DS implementations there is no
A site link bridge connects two or more site links.
need for a site link bridge especially if they
are single domain forests. In cases where there are
need for a site link bridge especially if they are single domain forests. In cases where there are
multiple domains in a forest distributed across multiple physical locations where some of those
multiple domains in a forest distributed across multiple physical locations where some of those
multiple domains in a forest distributed across multiple physical locations where some of those
physical locations have only a single domain controller, it may be necessary to implement site link
physical locations have only a single domain controller, it may be necessary to implement site link
physical locations have only a single domain controller, it may be necessary to implement site link
to ensure that full replication can be achieved.
bridges to ensure that full replication can be achieved.

Recommendation

By default, all site links are transitive and it is recommended this is left enabled. However, occasionally it
By default, all site links are transitive and it is recommended this is left enabled. However, occasionally it
By default, all site links are transitive and it is recommended this is left enabled. However, occasionally it
a site link bridge design if
may be necessary to disable ‘Bridge all site links’ for replication and complete a site link bridge design if
may be necessary to disable ‘
either of the following applies:
either of the following applies:
(cid:1)  The IP network is not fully routed
The IP network is not fully routed
(cid:1)  It is necessary to control the replication flow of the changes made in
, such as controlling
It is necessary to control the replication flow of the changes made in AD DS, such as controlling
replication failover, or Active Directory replication through a firewall
replication failover, or Active Directory replication

35 Site Link Properties {R36}:
http://technet.microsoft.com/en-us/library/cc753700(WS.10).aspx

us/library/cc753700(WS.10).aspx

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 50

Prepared by Microsoft

Currently the DFS topology generation and ’next closest site’ features require that the Bridge all
Currently the DFS topology generation and ’next closest site’ features require that the Bridge all
Currently the DFS topology generation and ’next closest site’ features require that the Bridge all
Site Links option remains enabled. A new switch has been introduced to repadmin.exe to allow the
Site Links option remains enabled. A new switch has been introduced to repadmin.exe to allow the
Site Links option remains enabled. A new switch has been introduced to repadmin.exe to allow the
DFS topology generation to continue while
disabling the Active Directory replication site link
DFS topology generation to continue while disabling the Active Directory replication site link
bridging topology. If the circumstances require the DFS topology generation but not the Active
bridging topology. If the circumstances require the DFS topology generation but not the Active
bridging topology. If the circumstances require the DFS topology generation but not the Active
Directory site link bridging feature, the site link bridging option should be left enabled and the
Directory site link bridging feature, the site link bridging option should be left enabled and the
Directory site link bridging feature, the site link bridging option should be left enabled and the
g command run for each site that is affected:
following command run for each site that is affected:

repadmin /siteoptions <domain controller> /site:<site name>
C:\Windows> repadmin /siteoptions <domain controller> /site:<site name>
repadmin /siteoptions <domain controller> /site:<site name>
+W2K3_BRIDGES_REQUIRED

If required, the site link bridge requirements should be determined, based on network connectivity
If required, the site link bridge requirements should be determined, based on network connectivity
If required, the site link bridge requirements should be determined, based on network connectivity
link bridge design. For instance, the requirements would need to be identified for the
link bridge design. For instance, the requirements would need to be identified for the
and the site link bridge design. For instance, the requirements would need to be identified for the
following scenarios36:

(cid:1)  Disjointed networks

(cid:1)  Control of the AD DS replication flow
replication flow

6.2.7  Domain Controller

Hardware Availability and Scalability
Domain Controller Hardware Availability and Scalability
Requirements

Planning domain controller capacity helps determine the appropriate number of
capacity helps determine the appropriate number of domain controllers
capacity helps determine the appropriate number of
to place in each domain that is represented in a site. Capacity planning also assists in estimating
to place in each domain that is represented in a site. Capacity planning also assists in estimating
to place in each domain that is represented in a site. Capacity planning also assists in estimating
, enabling the cost to be minimised and an
the hardware requirements for each
the hardware requirements for each domain controller, enabling the cost to be m
effective service level to be maintained for the
When planning the
effective service level to be maintained for the healthcare organisation users. When planning the
domain controller hardware it is worth noting that Windows Server 2008 R2 is only available as a
domain controller hardware it is worth noting that Windows Server 2008 R2 is only available as a
domain controller hardware it is worth noting that Windows Server 2008 R2 is only available as a
omain controller requirements it may be possible to
64 bit operating system. Depending upon the domain controller requirements it may be possible to
64 bit operating system. Depending upon the d
reduce the overall number of domain controllers required as the capacity and performance of 64 bit
reduce the overall number of domain controllers required as the capacity and performance of 64 bit
reduce the overall number of domain controllers required as the capacity and performance of 64 bit
servers exceeds those of 32 bit servers.
servers exceeds those of 32 bit servers.

6.2.7.1

Determine Domain Controller Capacity
Determine Domain Controller Capacity

capacity, the Active Directory site topology design must be
troller capacity, the Active Directory site topology design must be

Before planning domain controller
complete. Part of designing site topology involves deciding which locations require domain
complete. Part of designing site topology involves deciding which locations require
complete. Part of designing site topology involves deciding which locations require
controllers and what type of domain controller
site topology, planning the domain controller
controllers that are needed in each domain for each site, and the hardware that is required for each
s that are needed in each domain for each site, and the hardware that is required for each
s that are needed in each domain for each site, and the hardware that is required for each
domain controller and, in turn,
domain controller. Various elements can affect the per
domain controller capacity37.
influence the domain controller

s are required in each location. After designing the
capacity will help to determine the number of domain

. Various elements can affect the performance of a domain controller

domain controllers are required in each location. After designing th

domain controller capacity will help to determine the number of

36 Creating a Site Link Bridge Design {
http://technet.microsoft.com/en-us/library/cc753638(WS.10).aspx

us/library/cc753638(WS.10).aspx

{R37}:

Background Information for Planning Domain Controller Capacity {R38}:

37 Background Information for Planning Domain Controller Capacity
http://technet2.microsoft.com/windowsserver/en/library/52bf61a8-9845-4878-8fa4-a85c57fe25e51033.mspx
http://technet2.microsoft.com/windowsserver/en/library/52bf61a8

a85c57fe25e51033.mspx

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 51

6.2.7.2

Determine Minimum Number of Domain Controllers Required
Determine Minimum Number of Domain Controllers Required
Determine Minimum Number of Domain Controllers Required

Prepared by Microsoft

s should be placed in
To maintain an effective service level, a sufficient number of domain controllers should be placed in
To maintain an effective service level, a sufficient number of
each domain in a site, thus allowing the number of users that are also within each domain in that
ain in a site, thus allowing the number of users that are also within each domain in that
ain in a site, thus allowing the number of users that are also within each domain in that
site to be supported. The identification of inbound and outbound replication requirements should be
site to be supported. The identification of inbound and outbound replication requirements should be
site to be supported. The identification of inbound and outbound replication requirements should be
understood, adding domain controller

domain controllers to support replication between sites if required

en sites if required38.

As each healthcare organisation
the number of domain controller
healthcare organisation to unders
number of users within a site:

healthcare organisation is different, it is not possible to place actual recommendations for
is different, it is not possible to place actual recommendations for
owing guidance may help a
domain controllers that will be required. However, the following guidance may help a

tand the hardware which may be required to support a certain
to understand the hardware which may be required to support a certain

(cid:1)  The Domain Controller Capacity Test Configurations information, as provided in the
The Domain Controller Capacity Test Configurations information, as provided in the
The Domain Controller Capacity Test Configurations information, as provided in the
Determining the Minimum Number of
Windows Server 2003 Deployment Guide article: Determining the Minimum Number of
Windows Server 2003 Deployment Guide article:
Domain Controllers Required39
Domain Controllers Required

Important

to estimate the number of
Following the guidance in this section will allow a healthcare organisation to estimate the number of
Following the guidance in this section will allow
s required with a given configuration, but this should only be used as a guideline. Any
domain controllers required with a given configuration, but this should only be used as a guideline. Any
s required with a given configuration, but this should only be used as a guideline. Any
isions regarding the hardware chosen should be tested thoroughly in an isolated environment
design decisions regarding the hardware chosen should be tested thoroughly in an isolated environment
isions regarding the hardware chosen should be tested thoroughly in an isolated environment
will be implemented.
which, as much as possible, matches the live environment where AD DS will be implemented.
which, as much as possible, matches the live environment where

6.2.7.3

Determine Disk Space and Memory Requirements
Determine Disk Space and Memory Requirements

Underestimating hardware requirements can cause poor performance and application response
requirements can cause poor performance and application response
requirements can cause poor performance and application response
time, and can prevent users from quickly logging on to the network to access resources.
time, and can prevent users from quickly logging on to the network to access resources.
time, and can prevent users from quickly logging on to the network to access resources.

should be
The required disk space and memory requirements for each domain controller should be
The required disk space and memory requirements for each
determined, taking into account that this may vary according to the following:
determined, taking into account that this may vary according to the following:

(cid:1)  GC distribution

(cid:1)  AD DS application partition requirements
application partition requirements

(cid:1)  Memory and large memory support requirements
Memory and large memory support requirements

rmine the minimum memory
The number of users per domain in a site should be used to determine the minimum memory
The number of users per domain in a site should be used to dete
provides details of the minimum
domain controller in that domain. Table 17 provides details of the minimum
requirements for each domain controller
memory requirements per domai

domain controller.

Users per Domain in a Site

Minimum Memory per Domain Controller
Minimum Memory per Domain Controller

1 – 499

500 – 999

1000 – > 10000

512 MB

1 GB

2 GB

: Minimum Memory Requirements per Domain Controller
Table 17: Minimum Memory Requirements per Domain Controller

Domain controllers require at least enough disk space for the
SYSVOL shared folder, and the operating system.
SYSVOL shared folder, and the operating system.

s require at least enough disk space for the AD DS database,

database, AD DS log files, the

38 Adding Domain Controllers to Support Replication Between Sites
http://technet2.microsoft.com/windowsserver/en/library/4a59cc62-9425-463f-89b6-95347e2ea91e1033.mspx
http://technet2.microsoft.com/windowsserver/en/library/4a59cc62

ers to Support Replication Between Sites {R39}:

95347e2ea91e1033.mspx

Determining the Minimum Number of Domain Controllers Required {R40}:

39 Determining the Minimum Number of Domain Controllers Required
http://technet2.microsoft.com/windowsserver/en/library/2619a7f0-c6ab-435a-83db-34f1425107e71033.mspx
http://technet2.microsoft.com/windowsserver/en/library/2619a7f0

34f1425107e71033.mspx.

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 52

Prepared by Microsoft

Recommendations
(cid:1)  On the drive that will contain the
database, NTDS.dit, 0.4 GB of storage for each 1,000 users
On the drive that will contain the AD DS database, NTDS.dit, 0.4 GB of storage for each 1,000 users
made available
should be made available
(cid:1)  On the drive that will contain the

transaction log files, at least 500 MB of space should be
On the drive that will contain the AD DS transaction log files, at least 500 MB of space should be
made available

(cid:1)  On the drive that will contain the SYSVOL shared folder, at least 500 MB of space should be made
On the drive that will contain the SYSVOL shared folder, at least 500 MB of space should be made
On the drive that will contain the SYSVOL shared folder, at least 500 MB of space should be made
available

(cid:1)  On the drive that will contain the Windows Server 200

ll contain the Windows Server 2008 R2 operating system files, at least

operating system files, at least 20 GB of

space should be made available
space should be made available

(cid:1)  When selecting suitable hardware for providing the
When selecting suitable hardware for providing the AD DS, consideration should be given to ensuring
, consideration should be given to ensuring
uding network interfaces, power supply units, processors,
resiliency within the server components, incl
resiliency within the server components, including network interfaces, power supply units, processors,
memory, hard drives, and the provision of out-of-band management
memory, hard drives, and the provision of out
(cid:1)  Sufficient air conditioning, power and network (where possible resilient in

band connections and out-
Sufficient air conditioning, power and network (where possible resilient in-band connections and out
of-band management network) prov
management process

isioning should be planned and implemented as part of a capacity
band management network) provisioning should be planned and implemented as part of a capacity

When configuring the hard disk space on a domain controller, the data types should be segregated
, the data types should be segregated
When configuring the hard disk space on a
to separate volumes
by operating system, security database and SYSVOL, and logs, and allocated to separate volumes
by operating system, security database and SYSVOL, and logs, and allocated
for storage.

Recommendations
(cid:1)  To prevent single disk failures, a Redundant Array of Independent Disks (RAID) should be used
To prevent single disk failures, a Redundant Array of Independent Disks (RAID) should be used
To prevent single disk failures, a Redundant Array of Independent Disks (RAID) should be used
(cid:1)  For domain controllers that are accessed by fewer than 1,000 users, all four components may be
s that are accessed by fewer than 1,000 users, all four components may be
s that are accessed by fewer than 1,000 users, all four components may be

single RAID 1 array
located on a single RAID 1 array

(cid:1)  For domain controllers that are accessed by more than 1,000 users, the log files should be placed on
s that are accessed by more than 1,000 users, the log files should be placed on
s that are accessed by more than 1,000 users, the log files should be placed on
one RAID array and the SYSVOL shared folder and the database should be kept together on a
one RAID array and the SYSVOL shared folder and the database should be kept together on a
one RAID array and the SYSVOL shared folder and the database should be kept together on a
separate RAID array, as specified in Table 27
separate RAID array, as specified in

Hardware
It is recommended that the hardware requirements are documented using the Hardware
It is recommended that the hardware requirements are documented using the
Assessment job aid, named DSSTOPO_5.doc

DSSTOPO_5.doc {R14}.

6.3  Design for AD DS

DS Security

To plan a secure environment, it is vital to have a clear and consistent strategy for addressing the
To plan a secure environment, it is vital to have a clear and consistent strategy for addressing the
To plan a secure environment, it is vital to have a clear and consistent strategy for addressing the
operating system, including
many aspects of the Microsoft Windows Server 2008 R2 operating system, including
many aspects of the Microsoft Windows Server 200
security-related issues and features. Firstly, the user
should be identified, together with the other aspects of the network that comprise a secure common
should be identified, together with the other aspects of the network that comprise a secure common
should be identified, together with the other aspects of the network that comprise a secure common
infrastructure.

related requirements that impact security
related issues and features. Firstly, the user-related requirements that impact security

6.3.1

Plan a Secure AD

AD DS Environment

The Windows Server 2008 R2
security planning process is based on a high-level view of
the security configuration options and capabilities. The security planning process is based on two
the security configuration options and capabilities. The security planning process is based on two
the security configuration options and capabilities. The security planning process is based on two
organising principles:

8 R2 AD DS security planning process is based on a high

(cid:1)  Users need access to

This access can be very basic, including only desktop
Users need access to resources – This access can be very basic, including only desktop
logon and the availability of Access Control Lists (ACLs) on resources. It may also include
logon and the availability of Access Control Lists (ACLs) on resources. It may also include
logon and the availability of Access Control Lists (ACLs) on resources. It may also include
optional services, such as remote network logons, wireless network access, and access for
optional services, such as remote network logons, wireless network access, and access for
optional services, such as remote network logons, wireless network access, and access for
l users, such as business partners or customers
external users, such as business partners or customers

(cid:1)  The network requires a secure shared IT infrastructure

This infrastructure includes
The network requires a secure shared IT infrastructure – This infrastructure includes
security boundaries, secure servers and services, secure networking, and an effective plan
security boundaries, secure servers and services, secure networking, and an effective plan
security boundaries, secure servers and services, secure networking, and an effective plan
for delegating administration
for delegating administration

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 53

Prepared by Microsoft

sed together, the two principles of network operating system security can provide the trust and
Used together, the two principles of network operating system security can provide the trust and
sed together, the two principles of network operating system security can provide the trust and
integrity needed to help secure complex operating environments. By using a security planning
integrity needed to help secure complex operating environments. By using a security planning
integrity needed to help secure complex operating environments. By using a security planning
process to analyse the security requirements of a healthcare organisation deploying
process to analyse the security re
level security framework for the Windows Server 2008 R2 deployment.
level security framework for the Windows Server 200
possible to establish a high-level security framework for the Windows Server 200

deploying AD DS, it is

Important

This security planning process is not intended to replace a detailed assessment of existing security
This security planning process is not intended to replace a detailed assessment of existing security
This security planning process is not intended to replace a detailed assessment of existing security
solutions.
systems, gaps, and solutions.

security may result in the loss of access to network resources by legitimate
A breach in AD DS security may result in the loss of access to network resources by legitimate
security may result in the loss of access to network resources by legitimate
clients, or the inappropriate disclosure of potentially sensitive information.
clients, or the inappropriate disclosure of potentially sensitive information.

The Best Practice Guide for Securing Active Directory Installations40 whitepaper provides detailed
whitepaper provides detailed
The Best Practice Guide for Securing Active Directory Installations
technical information covering the following components of AD DS security:
technical information covering the following components of

(cid:1)  Planning in-depth AD DS

DS security

(cid:1)  Establishing secure AD

AD DS boundaries

(cid:1)  Deploying secure domain

omain controllers

(cid:1)  Securing DNS

(cid:1)  Strengthening domain and domain

Strengthening domain and domain controller policy settings

(cid:1)  Establish secure administrative practices
Establish secure administrative practices

Recommendation

use highly privileged accounts. All other
based administration, and delegated out appropriately on the
tasks should be related to data-based administration, and delegated out appropriately on the

Ideally, there should be very few service administrators who use highly privileged accounts
Ideally, there should be very few service administrators who
AD DS tasks should be related to data
administration helps maximise security. For more
principle of ‘least privilege’. This model of AD DS administration helps maximise security. For more
principle of ‘least privilege’. This model of
information see the whitepaper:
information see the whitepaper: Best Practices for Delegating Active Directory Administration
notes on user accounts earlier in this document {6.1.7.3.1}.
notes on user accounts earlier in this document {

Active Directory Administration41 and the

6.3.1.1

Address User-

-Related Requirements

d requirements are essential considerations in network design. There are security
User-related requirements are essential considerations in network design. There are security
d requirements are essential considerations in network design. There are security
related design decision that needs to be made.
requirements associated with almost every user-related design decision that needs to be made.
requirements associated with almost every user

The following items are key security-related user requirements that each health
The following items are key security
must address:

healthcare organisation

(cid:1)  Keyboard logons which require an authentication strategy design (see section
Keyboard logons which require an authentication strategy design (see section 6.3.2)
Keyboard logons which require an authentication strategy design (see section

(cid:1)  Access to resources which requir

e a resource authorisation strategy design (see section
Access to resources which require a resource authorisation strategy design (see section
6.3.3)

It may be necessary for Healthcare organisation
that are not as universally applicable42, for example:
that are not as universally applicable

Healthcare organisations to implement other security-related

related requirements

(cid:1)  Remote network access
Remote network access

(cid:1)  Wireless network access
Wireless network access

Deployment Whitepaper: Best Practice Guide for Securing Active Directory Installations {R41}:

40 Deployment Whitepaper: Best Practice Guide for Securing Active Directory Installations
http://technet2.microsoft.com/windowsserver/en/library/edc08cf1-d4ba-4235-9696-c93b0313ad6e1033.mspx?mfr=true
http://technet2.microsoft.com/windowsserver/en/library/edc08cf1

c93b0313ad6e1033.mspx?mfr=true

Best Practices for Delegating Active Directory Administration {R42}:

41 Best Practices for Delegating Active Direc
http://go.microsoft.com/fwlink/?LinkID=22708
http://go.microsoft.com/fwlink/?LinkID=22708

42 Addressing User-Related Requirements
05d3fa1033.mspx
http://technet2.microsoft.com/windowsserver/en/library/a35e88e7-2504-4a60-ba78-7c9efa05d3fa1033.mspx
 http://technet2.microsoft.com/windowsserver/en/library/a35e88e7

Related Requirements {R43}:

Page 54

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Prepared by Microsoft

(cid:1)  Standard Client configurations (see the
Standard Client configurations (see the Automated Build Healthcare Desktop
Guide {R30} and the Group Policy for

Group Policy for Healthcare Desktop Management

Desktop Management {R20})

Desktop and Server

(cid:1)  Encrypting File System (EFS) (see the

Encrypting File System (EFS) (see the Healthcare EFS Tool Administration Guide

Tool Administration Guide {R44})

(cid:1)  Extranet access

6.3.1.2

Establish a Secure Shared IT Infrastructure
Establish a Secure Shared IT Infrastructure

etwork services and
related features apply directly to users. Many basic network services and

Not all security-related features apply directly to users. Many basic n
configuration decisions involve creating and defining explicit boundaries, securing network traffic,
configuration decisions involve creating and defining explicit boundaries, securing network traffic,
configuration decisions involve creating and defining explicit boundaries, securing network traffic,
and securing the servers.

It is very important to prevent unauthorised users from viewing data, even if they gain physical
It is very important to prevent unauthorised users from viewing data, even if they gain physical
It is very important to prevent unauthorised users from viewing data, even if they gain physical
e server. It is advised that the following points are identified and planned for:
access to the server. It is advised that the following points are identified and planned for:
e server. It is advised that the following points are identified and planned for:

(cid:1)  Securing domain controller

domain controllers against physical access

(cid:1)  Preventing domain controller

s from booting into alternate operating systems
domain controllers from booting into alternate operating systems

(cid:1)  Protecting domain controller

domain controllers on restart by using syskey

(cid:1)  Securing backup media against physical access
Securing backup media against physical access

(cid:1)  Enhancing the security of the network infrastructure
Enhancing the security of the network infrastructure

(cid:1)  Securing the remote restart of

Securing the remote restart of domain controllers

(cid:1)  Securing service administrator accounts
Securing service administrator accounts

(cid:1)  Securing the workstations belonging to

Securing the workstations belonging to service administrators

(cid:1)  Avoiding the delegation of security

Avoiding the delegation of security-sensitive operations

Recommendations

Active Directory domain controller
and, therefore, should be housed in a physically secure environment.
and, therefore, should be housed in a physically se

s maintain sensitive security information for all users within the forest
domain controllers maintain sensitive security information for all users within the forest

AD DS is backed up as part of System State, which includes the database, log files, registry, system boot
is backed up as part of System State, which includes the database, log files, registry, system boot
is backed up as part of System State, which includes the database, log files, registry, system boot
files, COM+ Registration Database, and System Volume (Sysvol). Therefore, it is critical that these
files, COM+ Registration Database, and System Volume (Sysvol). Therefore, it is critical that these
files, COM+ Registration Database, and System Volume (Sysvol). Therefore, it is critical that these
d as a set. Backup and restore plans help to ensure service continuity
volumes be backed up and restored as a set. Backup and restore plans help to ensure service continuity
volumes be backed up and restore
in the event of a directory issue. These backups should be stored in a physically secure location, both
in the event of a directory issue. These backups should be stored in a physically secure location, both
in the event of a directory issue. These backups should be stored in a physically secure location, both
onsite and offsite.

Design an Authentication Strategy
6.3.2  Design an Authentication Strategy

s need to support seamless access to the network for multiple types of
Most healthcare organisations need to support seamless access to the network for multiple types of
s need to support seamless access to the network for multiple types of
needs to protect the network resources from
healthcare organisation needs to protect the network resources from
users. At the same time, the healthcare organisation
designed authentication strategy can help achieve this complex balance
designed authentication strategy can help achieve this comp
potential intruders. A well-designed authentication strategy can help achieve this comp
between providing reliable access for users and strong network security.
between providing reliable access for users and strong network security.

Designing an authentication strategy involves:
Designing an authentication strategy involves:

(cid:1)  Evaluating the existing infrastructure and account creation process
Evaluating the existing infrastructure and account creation process

(cid:1)  Establishing a means of securing the authentication proc

Establishing a means of securing the authentication process

(cid:1)  Establishing standards for network authentication and time synchronisation
Establishing standards for network authentication and time synchronisation
Establishing standards for network authentication and time synchronisation

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 55

Prepared by Microsoft

6.3.2.1

Create a Foundation for Authentication
Create a Foundation for Authentication

solution, it is necessary to create a foundation for secure authentication
When designing an AD DS solution, it is necessary to create a foundation for secure authentication
solution, it is necessary to create a foundation for secure authentication
require authorisation to access resources within the
of users, computers, and services which require authorisation to access resources within the
of users, computers, and services which
level. As such, the following must be included in the design
organisation level. As such, the following must be included in the design
appropriate healthcare organisation
process43:

(cid:1)  Evaluation of the current environment
Evaluation of the current environment

(cid:1)  Creation of user accounts
Creation of user accounts

(cid:1)  Creation of a user account mana

gement plan, including creating, disabling and resetting
Creation of a user account management plan, including creating, disabling and resetting
user accounts

(cid:1)  Creation of a computer account management plan, including creating, deleting and
Creation of a computer account management plan, including creating, deleting and
Creation of a computer account management plan, including creating, deleting and
resetting computer account passwords
resetting computer account passwords

(cid:1)  Creation and security of service accounts, including the local

service and network service
Creation and security of service accounts, including the local service and network service
built in accounts

(cid:1)  Application of authentication policies to groups
Application of authentication policies to groups

Authentication Strategy
It is recommended that the design decisions are documented using the Authentication Strategy
It is recommended that the design decisions are documented using the
DSSAUT_1.doc {R14}.
Planning job aid, named DSSAUT_1.doc

6.3.2.2

Secure the Authentication Process
Secure the Authentication Process

It is important to secure the authentication process to protect the system against various security
It is important to secure the authentication process to protect the system against various security
It is important to secure the authentication process to protect the system against various security
threats, such as password cracking tools, brute
rights, impersonation of authenticated users, and replay attacks. The following areas of an
rights, impersonation of authenticated users, and replay attacks. The following areas of an
rights, impersonation of authenticated users, and replay attacks. The following areas of an
authentication process should be considered:
authentication process should be considered:

or dictionary attacks, abuse of system access
cracking tools, brute force or dictionary attacks, abuse of system access

(cid:1)  Assign logon hours

(cid:1)  Create a ticket expiration policy
Create a ticket expiration policy

(cid:1)  Establish network authentication standards
uthentication standards

(cid:1)  Set clock synchronisation tolerance to prevent replay attacks
Set clock synchronisation tolerance to prevent replay attacks

(cid:1)  Review the Default Domain

Review the Default Domain Policy GPO:

(cid:2)  Create a strong password policy for the domain
Create a strong password policy for the domain

(cid:2)  Establish an account lockout policy for the domain
Establish an account lockout policy for the domain

(cid:2)  Create a Kerberos ticket expiratio

Create a Kerberos ticket expiration policy

(cid:1)  Review the Default Domain Controller

Review the Default Domain Controllers Policy GPO:

(cid:2)  Review domain controller

domain controller audit policy settings

(cid:2)  Strengthen domain controller

domain controller user rights assignment policy settings

(cid:2)  Strengthen domain controller

domain controller security options policy settings

(cid:2)  Strengthen domain co

domain controller event log policy settings

Creating a Foundation for Authentication {R45}:

43 Creating a Foundation for Authentication
http://technet2.microsoft.com/windowsserver/en/library/2df33645-5e3e-4b79-9733-ffa2a3cf60c41033.mspx
http://technet2.microsoft.com/windowsserver/en/library/2df33645

ffa2a3cf60c41033.mspx

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 56

Recommendation

Prepared by Microsoft

The points above are the only settings that should be altered within the Default Domain Policy (DDP) and
The points above are the only settings that should be altered within the Default Domain Policy (DDP) and
The points above are the only settings that should be altered within the Default Domain Policy (DDP) and
Default Domain Controller Policy (DDCP), all other settings to be applied at these levels should be
Default Domain Controller Policy (DDCP), all other settings to be applied at these levels should be
Default Domain Controller Policy (DDCP), all other settings to be applied at these levels should be
contained within new GPOs. For further detailed information, see the
guidance document.
Management {R26} guidance document.

ontained within new GPOs. For further detailed information, see the Group Policy for

Group Policy for Healthcare Desktop

job aid, named
ign decisions can be documented using the Authentication Security job aid, named

The design decisions can be documented using the
DSSAUT_2.doc {R14}.

It is also critical to strengthen DC policy settings. This can be achieved by utilising The Microsoft
It is also critical to strengthen DC policy settings. This can be achieved by utilising The Microsoft
It is also critical to strengthen DC policy settings. This can be achieved by utilising The Microsoft
Security Configuration Wizard (SCW).
Security Configuration Wizard (SCW).

Recommendations

The SCW, supplied as part of the
configure the appropriate settings44.
configure the appropriate settings

, can be used to help
as part of the Windows Server 2008 R2 operating system, can be used to help

For baseline security policies refer to the Microsoft Security Reference Framework Toolkit which provides
For baseline security policies refer to the Microsoft Security Reference Framework Toolkit which provides
For baseline security policies refer to the Microsoft Security Reference Framework Toolkit which provides
, workstations and servers based on Microsoft
guidance on establishing a secure baseline for users, workstations and servers based on Microsoft
guidance on establishing a secure baseline for users
recommended practices.

The SCW reduces the attack surface for computers running Windows Server 200
The SCW reduces the attack surface for computers running Windows Server 2008 R2 or later. It
The SCW reduces the attack surface for computers running Windows Server 200
determines the minimum functionality required for a server's role or roles, and disables functionality
determines the minimum functionality required for a server's role or roles, and disables funct
determines the minimum functionality required for a server's role or roles, and disables funct
that is not required. Specifically, the SCW assists in authoring a security policy that:
that is not required. Specifically, the SCW assists in authoring a security policy that:
that is not required. Specifically, the SCW assists in authoring a security policy that:

(cid:1)  Disables unneeded services
Disables unneeded services

(cid:1)  Blocks unused ports

(cid:1)  Allows additional address or security restrictions for ports that are left open
Allows additional address or security restrictions for ports that are left open
Allows additional address or security restrictions for ports that are left open

(cid:1)  Reduces protocol exposure to Se

rver Message Block (SMB), LAN Manager, and
Reduces protocol exposure to Server Message Block (SMB), LAN Manager, and
Lightweight Directory Access Protocol (LDAP)
Lightweight Directory Access Protocol (LDAP)

(cid:1)  Defines a high signal-to

to-noise audit policy45

(cid:1)  Guides through the process of creating, editing, applying, or rolling back a security policy
Guides through the process of creating, editing, applying, or rolling back a security policy
Guides through the process of creating, editing, applying, or rolling back a security policy
based on the selected roles of the server
based on the selected roles of

The deployed group policy settings can be documented using the HTML reports available within the
The deployed group policy settings can be documented using the HTML reports available within the
The deployed group policy settings can be documented using the HTML reports available within the
GPMC.

It is also possible to create a GPO from the SCW settings that can be linked to the domain or an
It is also possible to create a GPO from the SCW settings that can be linked to the domain or an
It is also possible to create a GPO from the SCW settings that can be linked to the domain or an
OU to provide a centrally managed and admini
applying the configuration settings. It
OU to provide a centrally managed and administered way for applying the configuration settings. It
should be noted that the default settings for Windows Server 2008 R2 are very secure. Installation
should be noted that the default settings for Windows Server 2008 R2 are very secure. Installation
should be noted that the default settings for Windows Server 2008 R2 are very secure. Installation
of additional services or applications that are part of the operating system is through the Server
ystem is through the Server
of additional services or applications that are part of the
ager application. These new services and applications are referred to as Roles and Role
ager application. These new services and applications are referred to as Roles and
Manager application. These new services and applications are referred to as Roles and
Services in Windows Server 2008 and
ervices in Windows Server 2008 and Windows Server 2008 R2. Part of the installation of a
or role service includes adding any new firewall port rules to the server on which the
or role service includes adding any new firewall port rules to the server
ervices are installed. If a role or role service is removed these required firewall port rules are
Services are installed. If a role or role service is removed these required firewall port rules are
ervices are installed. If a role or role service is removed these required firewall port rules are
removed.

Server 2008 R2. Part of the installation of a Role
on which the Roles or Role

Deployment Guide for the Security Configuration Wizard {R46}:

44 Deployment Guide for the Security Configuration Wizard
http://technet2.microsoft.com/windowsserver/en/library/5254f8cd
http://technet2.microsoft.com/windowsserver/en/library/5254f8cd-143e-4559-a299-9c723b3669461033.mspx
us/library/cc731515(WS.10).aspx
http://technet.microsoft.com/en-us/library/cc731515(WS.10).aspx

9c723b3669461033.mspx and

45 A high signal-to-noise audit policy is one that provides useful audit informatio
retrieved with it which is not regarded as useful.
retrieved with it which is not regarded as useful.

n whilst minimising the information commonly
noise audit policy is one that provides useful audit information whilst minimising the information commonly

Page 57

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Prepared by Microsoft

6.3.2.3

Extend the Authentication Framework
Extend the Authentication Framework

If more than one Active Directory
Active Directory forest is deployed and it is determined that resource access is
forest is deployed and it is determined that resource access is
required between forests, then it is necessary to extend the authentication framework46. This can
required between forests, then it is necessary to extend the authentication framework
required between forests, then it is necessary to extend the authentication framework
be accomplished by creating trust relationships and additional accounts, as appropriate, covering
be accomplished by creating trust relationships and additional accounts, as appropriate, cover
be accomplished by creating trust relationships and additional accounts, as appropriate, cover
the following requirements:

(cid:1)  Establish inter-forest authentication
forest authentication

(cid:1)  Enable interoperability with Kerberos clients and servers running other operating systems
Enable interoperability with Kerberos clients and servers running other operating systems
Enable interoperability with Kerberos clients and servers running other operating systems

Extended
It is recommended that the design requirements are documented using the Extended
It is recommended that the design requirements are documented using the
Authentication Framework job aid, named

job aid, named DSSAUT_3.doc {R14}.

6.3.2.4

Educate Users about the Authentication Process
Educate Users about the Authentication Process

It is important that, once the authentication process has been designed,
it is communicated to
It is important that, once the authentication process has been designed, it is communicated to
users, such that they can be educated as to their own role in the authentication process. Ensuring
users, such that they can be educated as to their own role in the authentication process. Ensuring
users, such that they can be educated as to their own role in the authentication process. Ensuring
that users are aware of the guidelines in creating passwords and the reasons behind the process
that users are aware of the guidelines in creating passwords and the reasons behind the process
that users are aware of the guidelines in creating passwords and the reasons behind the process
ces of users sharing their credentials or leaving them
being implemented, can reduce the chances of users sharing their credentials or leaving them
being implemented, can reduce the chan
written down where others have access to it.
written down where others have access to it.

Design a Resource Authorisation Strategy
6.3.3  Design a Resource Authorisation Strategy

Logging on does not automatically give users access to the resources they require. Users must be
Logging on does not automatically give users access to the resources they require. Users must be
Logging on does not automatically give users access to the resources they require. Users must be
authorised to access specific resources, but only at the level of access they need. Moreover, many
access specific resources, but only at the level of access they need. Moreover, many
access specific resources, but only at the level of access they need. Moreover, many
users have identical needs for access to a network resource. For example, all users in the clerical
users have identical needs for access to a network resource. For example, all users in the clerical
users have identical needs for access to a network resource. For example, all users in the clerical
colour printer, so it is
administration department of a hospital might need access to a specific colour printer, so it is
administration department of a hospital might need access to a specific
possible to easily manage access by putting every member of the clerical administration
possible to easily manage access by putting every member of the clerical administration
possible to easily manage access by putting every member of the clerical administration
department into a security group that is authorised to access that printer.
department into a security group that is authorised to access that printer.

ey form the main component of the
Because security groups are so critical for controlling access, they form the main component of the
Because security groups are so critical for controlling access, th
authorisation strategy. Consequently, it is important to know what security group types are
authorisation strategy. Consequently, it is important to know what security group types are
authorisation strategy. Consequently, it is important to know what security group types are
available and how they should be used.
available and how they should be used.

can design a resource
By applying this information appropriately, a healthcare organisation can design a resource
By applying this information appropriately, a
authorisation strategy that is scalable, easy to maintain, and cost effective.
authorisation strategy that is scalable, easy to maintain, and cost effective.

6.3.3.1

Establish a Resource Authorisation Method
Establish a Resource Authorisation Method

, access to shared
Depending on the resource and the needs of the healthcare organisation, access to shared
Depending on the resource and the needs of the
resources should be setup by applying any or all of the following authorisation methods:
resources should be setup by applying any or

all of the following authorisation methods:

(cid:1)  Account Group/ACL (AG/ACL) method

Security groups, rather than individual user
Account Group/ACL (AG/ACL) method – Security groups, rather than individual user
accounts, are added to the resource ACL, and the group is given a set of access
accounts, are added to the resource ACL, and the group is given a set of access
accounts, are added to the resource ACL, and the group is given a set of access
permissions

(cid:1)  Account Group/Resource Group (AG/RG) m

Users with similar access
Account Group/Resource Group (AG/RG) method – Users with similar access
requirements are grouped into account groups. The account groups are then added to a
requirements are grouped into account groups. The account groups are then added to a
requirements are grouped into account groups. The account groups are then added to a
resource group that has been granted specific resource access permissions
resource group that has been granted specific resource access permissions
resource group that has been granted specific resource access permissions

(cid:1)  Role-based authorisation

based authorisation – Often uses scripts, called authorisation rules, or third

tion rules, or third-party

tools to enable users with similar roles to be authorised to perform predefined sets of tasks
tools to enable users with similar roles to be authorised to perform predefined sets of tasks
tools to enable users with similar roles to be authorised to perform predefined sets of tasks
in specific applications
in specific applications

Extending Your authentication Framework {R47}:

46 Extending Your authentication Framework
http://technet2.microsoft.com/windowsserver/en/library/1d90e7c1-37e3-4efe-bf64-1b9ffa93b1a71033.mspx
http://technet2.microsoft.com/windowsserver/en/library/1d90e7c1
supplementary information for Windows Server 2008 and Windows Server 2008 R2
supplementary information for Windows Server 2008 and
us/library/dd548350(WS.10).aspx
http://technet.microsoft.com/en-us/library/dd548350(WS.10).aspx

1b9ffa93b1a71033.mspx and

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 58

Recommendations

s it is most appropriate to use the AG/RG resource
For small, centrally managed healthcare organisations it is most appropriate to use the AG/RG resource
For small, centrally managed
local groups or domain local groups should be selected as the
authorisation model. In which case, the local groups or domain local groups should be selected as the
authorisation model. In which case, the
resource groups.

Prepared by Microsoft

For larger, distributed healthcare organisation
method using the Authorization Manager {R7}.
method using the Authorization Manager

healthcare organisations, it is more appropriate to use the role

le-based authorisation

6.3.3.2

Policies for Security Group Management
Define Policies for Security Group Management

Policies for security group management are a sign
ificant part of the resource authorisation strategy.
Policies for security group management are a significant part of the resource authorisation strategy.
It is important to establish a policy defining who can create security groups and when they should
It is important to establish a policy defining who can create security groups and when they should
It is important to establish a policy defining who can create security groups and when they should
be created. It is also important to define the following policies47:
be created. It is also important to define the following policies

(cid:1)  Security group creation policy, incl

uding which members are allowed to create new security
Security group creation policy, including which members are allowed to create new security
groups, and the process used to create them
groups, and the process used to create them

(cid:1)  Security group naming policy, using the information provided in section
Security group naming policy, using the information provided in section 6.1.7.3.2
Security group naming policy, using the information provided in section

(cid:1)  Security group retirement policy, including when security groups become obsolete as these
Security group retirement policy, including when security groups become obsolete as these
Security group retirement policy, including when security groups become obsolete as these
should be identified and retired (deleted) to minimise security risks
should be identified and retired (deleted) to minimise security risks

(cid:1)  Security group nesting policy. Security group nesting occurs wh

en one security group is
Security group nesting policy. Security group nesting occurs when one security group is
made a member of another security group, and the nested group inherits all of the
made a member of another security group, and the nested group inherits all of the
made a member of another security group, and the nested group inherits all of the
privileges and permissions that are granted to the parent
privileges and permissions that are granted to the parent

Important

contains the SIDs for
Unrestrained group nesting can result in access token size problems as the token contains the SIDs for
Unrestrained group nesting can result in access token size problems as the token
each group of which the user is a member, either directly or indirectly. The default group membership
each group of which the user is a member, either directly or indirectly. The default group membership
each group of which the user is a member, either directly or indirectly. The default group membership
limitation is 120 groups48. This can also be impacted in cases where users have been migrated into the
This can also be impacted in cases where users have been migrated into the
This can also be impacted in cases where users have been migrated into the
History. The SIDs that are migrated over as part of SID History will also be
new forest and maintained SID History. The SIDs that are migrated over as part of SID History will also be
new forest and maintained SID
included in the access token further increasing the size.
included in the access token further increasing the size.

6.3.3.3

Delegate Policies for Security Group Management
Delegate Policies for Security Group Management

perform routine membership
deployments, it is appropriate to delegate the ability to perform routine membership
In large AD DS deployments, it is appropriate to delegate the ability to
maintenance on groups, and the ability to administer the ACLs and resource groups for resources.
maintenance on groups, and the ability to administer the ACLs and resource groups for resources.
maintenance on groups, and the ability to administer the ACLs and resource groups for resources.
Policies for security group management should be defined, considering the following points:
Policies for security group management should be defined, considering the following points:
Policies for security group management should be defined, considering the following points:

(cid:1)  Identify individuals to maintain

Identify individuals to maintain security groups

(cid:1)  Delegate account group maintenance
Delegate account group maintenance

(cid:1)  Delegate resource group maintenance
Delegate resource group maintenance

Design a Public Key Infrastructure
6.3.4  Design a Public Key Infrastructure

enables a variety of secure applications and business
Microsoft Windows Server 2008 R2 enables a variety of secure applications and business
Microsoft Windows Server 200
scenarios based on the use of digital certifica
tes. Before it is possible to use digital certificates, it is
scenarios based on the use of digital certificates. Before it is possible to use digital certificates, it is
necessary to design a PKI, which involves planning configuration options for one or more
necessary to design a PKI, which involves planning configuration options for one or more
necessary to design a PKI, which involves planning configuration options for one or more
certification authorities, preparing certificates to meet the needs of the healthcare
certification authorities, preparing certificates to meet the needs of
reating a PKI management plan.
creating a PKI management plan.

healthcare organisation, and

Defining Policies for Security Group Management {R48}:

47 Defining Policies for Security Group Management
http://technet2.microsoft.com/windowsserver/en/library/033a0042-ff57-4657-8350-c7a6ebe3b8991033.mspx
http://technet2.microsoft.com/windowsserver/en/library/033a0042

c7a6ebe3b8991033.mspx

Selecting Local Groups or Domain Local Groups as Resource Groups {R49}:

48 Selecting Local Groups or Domain Local Groups as Resource Groups
http://technet2.microsoft.com/windowsserver/en/library/1b3070ce-c6b1-4849-ae47-ce17bbec17ee1033.mspx
http://technet2.microsoft.com/windowsserver/en/library/1b3070ce

ce17bbec17ee1033.mspx

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 59

Prepared by Microsoft

Certificate Services provides a means to
A PKI based on Microsoft Windows Server 2008 R2 Certificate Services provides a means to
A PKI based on Microsoft Windows Server 200
perform tasks such as:

(cid:1)  Digitally signing files, including documents and applications
Digitally signing files, including documents and applications

(cid:1)  Securing e-mail from unintended viewers
mail from unintended viewers

(cid:1)  Enabling secure connections between computers, even if they are connected over the
cure connections between computers, even if they are connected over the
cure connections between computers, even if they are connected over the

public Internet or through a wireless network
public Internet or through a wireless network

(cid:1)  Enhancing user authentication through the use of smart cards
Enhancing user authentication through the use of smart cards

It is out of the scope of this document to detail the information required to fully understand PKI, and
fully understand PKI, and
It is out of the scope of this document to detail the information required to
level review of the interdependent processes
therefore provide recommendations. However, a high
therefore provide recommendations. However, a high-level review of the interdependent processes
required to create a PKI is listed below:
required to create a PKI is listed below:

(cid:1)  Defining certificate requirements. It is recommended that these are documented using the
Defining certificate requirements. It is recommended that these are documented using the
Defining certificate requirements. It is recommended that these are documented using the
Certificate Practice Statement Outline job
Summary of User Certificate Requirements
mmary of User Certificate Requirements and Certificate Practice Statement Outline
aids named DSSPKI_1.doc and DSSPKI_2.doc respectively {R14}
aids named DSSPKI_1.doc and DSSPKI_2.doc

(cid:1)  Designing the Certificate Authority (CA) infrastructure
ificate Authority (CA) infrastructure

(cid:1)  Extending the CA infrastructure
Extending the CA infrastructure

(cid:1)  Defining certificate configuration options and documenting the certificate lifecycle plan using
Defining certificate configuration options and documenting the certificate lifecycle plan using
Defining certificate configuration options and documenting the certificate lifecycle plan using
the Windows Server 2003 Certificate Lifecycle Plan

Windows Server 2003 Certificate Lifecycle Plan job aid DSSPKI_3.doc

job aid DSSPKI_3.doc {R14}

(cid:1)  Creating a certificate management plan
Creating a certificate management plan

(cid:1)  Deploying the PKI

6.4  Design Network Services to Support

Design Network Services to Support AD DS

In an IT environment, users need to make use of resources such as file and print services,
In an IT environment, users need to make use of resources such as file and print services,
In an IT environment, users need to make use of resources such as file and print services,
authentication services, email and messaging services, and access to enterprise applications. In
authentication services, email and messaging services, and access to enterprise applications. In
authentication services, email and messaging services, and access to enterprise applications. In
her, they need to be able to
addition, for the resources of one computer or device to access another, they need to be able to
addition, for the resources of one computer or device to access anot
There are two primary name resolution services used on
identify and reference each other. There are two primary name resolution services used on
identify and reference each other.
Windows networks: DNS and WINS. DNS is essential for AD DS as all resources are registered
as all resources are registered
Windows networks: DNS and WINS. DNS is essential for
for the directory. DNS is a host name resolution
with DNS and it provides the naming standards for the directory. DNS is a host name resolution
with DNS and it provides the naming standards
service that is the standard service used across private TCP/IP networks and public networks such
service that is the standard service used across private TCP/IP networks and public networks such
service that is the standard service used across private TCP/IP networks and public networks such
will not function. Since Windows 2000 when Active Directory
AD DS will not function. Since Windows 2000 when Active Directory
as the Internet. Without DNS AD
oduced, Windows clients and servers have used DNS as the primary name resolution
was first introduced, Windows clients and servers have used DNS as the primary name resolution
oduced, Windows clients and servers have used DNS as the primary name resolution
service.

WINS (Windows Internet Name Service) is the Microsoft implementation of a NetBIOS name
WINS (Windows Internet Name Service) is the Microsoft implementation of a NetBIOS name
WINS (Windows Internet Name Service) is the Microsoft implementation of a NetBIOS name
resolution service. Historically Windows based networking used NetBIOS as the
resolution service. Historically Windows based networking used NetBIOS as the foundation for
resolution service. Historically Windows based networking used NetBIOS as the
service location and network access. WINS provides a distributed NetBIOS name resolution
service location and network access. WINS provides a distributed NetBIOS name resolution
service location and network access. WINS provides a distributed NetBIOS name resolution
service to support applications and services that rely on NetBIOS name resolution. On the whole,
service to support applications and services that rely on NetBIOS name resolution. On the whole,
service to support applications and services that rely on NetBIOS name resolution. On the whole,
Windows-based networks no longer require NetBIOS name r
esolution services as the
based networks no longer require NetBIOS name resolution services as the
dependencies on the underlying technology have been gradually removed. However, in a mixed
dependencies on the underlying technology have been gradually removed. However, in a mixed
dependencies on the underlying technology have been gradually removed. However, in a mixed
based machines, legacy applications or down level,
infrastructure where there are still Windows NT-based machines, legacy applications or down level,
infrastructure where there are still Windows NT
external trusts it is likely that there
will be a requirement for a WINS infrastructure. Because the
external trusts it is likely that there will be a requirement for a WINS infrastructure. Because the
reliance on WINS has diminished significantly the WINS infrastructure will almost certainly be
reliance on WINS has diminished significantly the WINS infrastructure will almost certainly be
reliance on WINS has diminished significantly the WINS infrastructure will almost certainly be
small, possibly consisting of a single, centralised implementation. Because there may be some
small, possibly consisting of a single, centralised implementation. Because there may be some
small, possibly consisting of a single, centralised implementation. Because there may be some
legacy clients and applications still in the environment

clients and applications still in the environment, WINS is discussed in section

is discussed in section 6.4.2.

All other network services that are not specifically related to the requirem
All other network services that are not specifically related to the requirements of
considered out of scope for this guidance.
considered out of scope for this guidance.

ents of AD DS are

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 60

Prepared by Microsoft

6.4.1  DNS Infrastructure to Support

DNS Infrastructure to Support AD DS

After creating the Active Directory
infrastructure to support the AD
to IP addresses in a distributed network environment, allowing connectivity between computers and
to IP addresses in a distributed network environment, allowing connectivity between computers and
to IP addresses in a distributed network environment, allowing connectivity between computers and
other resources using names on IP networks.
other resources using names on IP networks.

forest and domain designs, it is necessary to design a DNS
Active Directory forest and domain designs, it is necessary to design a DNS
des a mapping of computer names
AD DS logical structure. DNS provides a mapping of computer names

uses DNS for name resolution, instead of the WINS NetBIOS name
Windows Server 2008 R2 uses DNS for name resolution, instead of the WINS NetBIOS name
uses DNS for name resolution, instead of the WINS NetBIOS name
based networks. A WINS infrastructure is still required
resolution method used in Windows NT 4.0-based networks. A WINS infrastructure is still required
resolution method used in Windows NT 4.0
to support NetBIOS based applications, but AD DS specifically requires DNS.
to support NetBIOS based applications, but

igning DNS to support AD DS within a healthcare organisation

The process for designing DNS to support
a healthcare organisation will vary
according to whether or not there is an existing DNS infrastructure. This section focuses on
according to whether or not there is an existing DNS infrastructure. This section focuses on
according to whether or not there is an existing DNS infrastructure. This section focuses on
implementing a DNS service to support AD DS, and provides guidance around integrating this w
implementing a DNS service to support
an existing DNS infrastructure.
an existing DNS infrastructure.

, and provides guidance around integrating this with

will depend very much on the requirements and the
a healthcare organisation will depend very much on the requirements and the

The DNS solution for a healthcare organisation
existing infrastructure. If there is no existing DNS solution then the recommendation is to use the
existing infrastructure. If there is no existing DNS solution then the recommendation is to use the
existing infrastructure. If there is no existing DNS solution then the recommendation is to use the
as part of the Windows Server 2008 R2 Operating system. This has all the
DNS service that comes as part of the Windows Server 2008 R2 Operating system. This has all the
as part of the Windows Server 2008 R2 Operating system. This has all the
needs and can make use of all the benefits that the Windows-based service
needs and can make use of all the benefits that the Windows
features that AD DS needs and can make use of all the benefits that the Windows
healthcare organisations that
offers such as AD DS integration and secure dynamic updates. For
already have a DNS solution there are several options:
already have a DNS solution there are several options:

integration and secure dynamic updates. For healthcare organisations

(cid:1)  Use the existing DNS solution to manage DNS for

(cid:1)  Use the existing solution as it is but use Windows DNS for

: If the existing DNS solution is
Use the existing DNS solution to manage DNS for AD DS: If the existing DNS solution is
provided it supports
robust, reliable and well configured it can be used to support AD DS provided it supports
robust, reliable and well configured it can be used to support
Service Location Records (SRV). It is even better if it supports dynamic updates as this
ecords (SRV). It is even better if it supports dynamic updates as this
ecords (SRV). It is even better if it supports dynamic updates as this
makes the maintenance of the DNS information easier. If the DNS solution does not
makes the maintenance of the DNS information easier. If the DNS solution does not
makes the maintenance of the DNS information easier. If the DNS solution does not
related DNS entries are regularly
support dynamic updates it is essential that the AD DS related DNS entries are regularly
support dynamic updates it is essential that the
and accurately maintained. Each domain controller writes to a local file all of the DNS
maintained. Each domain controller writes to a local file all of the DNS
maintained. Each domain controller writes to a local file all of the DNS
entries that it expects to see in DNS. The file is netlogon.dns and is located in the
entries that it expects to see in DNS. The file is netlogon.dns and is located in the
entries that it expects to see in DNS. The file is netlogon.dns and is located in the
Config folder
Windows\System32\Config folder
 As the existing DNS
Use the existing solution as it is but use Windows DNS for AD DS:
solution is already configured for the environment and is working it can be left as it is and a
solution is already configured for the environment and is working it can be left as it is and a
solution is already configured for the environment and is working it can be left as it is and a
delegation to the Active Directory namespace created. This would then allow the healthcare
delegation to the Active Directory namespace created. This would then allow
delegation to the Active Directory namespace created. This would then allow
and to make use of all the
to use the Windows DNS service to manage AD DS and to make use of all the
organisation to use the Windows DNS service to m
Windows DNS features without impacting the existing DNS solution. The Active Directory
Windows DNS features without impacting the existing DNS solution. The Active Directory
Windows DNS features without impacting the existing DNS solution. The Active Directory
namespace can then forward to the existing, internal DNS infrastructure
namespace can then forward to the existing, internal DNS infrastructure
namespace can then forward to the existing, internal DNS infrastructure
NS solution may be old or
Use the Windows DNS service for everything: The existing DNS solution may be old or
expensive to maintain. In these cases the whole DNS infrastructure can be moved over to
expensive to maintain. In these cases the whole DNS infrastructure can be moved over to
expensive to maintain. In these cases the whole DNS infrastructure can be moved over to
the Windows DNS service. The existing zones and host records can be imported into the
the Windows DNS service. The existing zones and host records can be imported into the
the Windows DNS service. The existing zones and host records can be imported into the
Windows DNS service and it can be used for all name resolution throughout the
Windows DNS service and it can be used for all name reso
organisation

lution throughout the healthcare

(cid:1)  Use the Windows DNS service for everything

Recommendation

Active Directory namespace planning and DNS planning should be approached separately, as there may
Active Directory namespace planning and DNS planning should be approached separately, as there may
Active Directory namespace planning and DNS planning should be approached separately, as there may
be separate requirements for each. Before finalising any DNS design however, it is important to reconcile
be separate requirements for each. Before finalising any DNS design however, it is important to
be separate requirements for each. Before finalising any DNS design however, it is important to
the approaches.

Where possible use the Windows DNS service to support
for the best levels of integration and
Where possible use the Windows DNS service to support AD DS for the best levels of integration and
reporting on the state of the service as well as making the most of the Windows DNS service features and
reporting on the state of the service as well as making the most of the Windows DNS service features and
reporting on the state of the service as well as making the most of the Windows DNS service features and
capabilities.

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 61

Prepared by Microsoft

6.4.1.1

Review Domain Name System Concepts
Review Domain Name System Concepts

DNS is a critical service for the successful implementation of
, and requires careful design
DNS is a critical service for the successful implementation of AD DS, and requires careful design
and deployment. It is recommended that core DNS concepts, such as delegation and recursive
and deployment. It is recommended that core DNS concepts, such as delegation and recursive
and deployment. It is recommended that core DNS concepts, such as delegation and recursive
name resolution, are reviewed49.
name resolution, are reviewed

6.4.1.2

in Name System and Active Directory
Review Domain Name System and Active Directory

, focusing particularly on the following design
Review DNS specifically, as it relates to AD DS, focusing particularly on the following design
Review DNS specifically, as it relates to
considerations:

(cid:1)  Domain controller location
location

(cid:1)  DNS name server location
DNS name server location

(cid:1)  AD DS integrated zones
integrated zones

(cid:1)  Computer naming

Recommendations
(cid:1)  For smaller to mid size environments consider i

r smaller to mid size environments consider installing the DNS service on every

the DNS service on every domain controller

in the forest

(cid:1)  Larger environments will need to consider only deploying the Windows DNS service on a carefully
Larger environments will need to consider only deploying the Windows DNS service on a carefully
Larger environments will need to consider only deploying the Windows DNS service on a carefully
the efficiency and performance of the DNS service
chosen subset of domain controllers to maintain the efficiency and performance of the DNS service
chosen subset of domain controllers to maintain

(cid:1)  Use AD DS integrated DNS zones
integrated DNS zones
(cid:1)  Configure all DNS zones to allow dynamic updates
, preferably secure dynamic updates
Configure all DNS zones to allow dynamic updates, preferably secure dynamic updates
(cid:1)  Ensure that domain names are registered with the proper Internet authorities (see the curre
Ensure that domain names are registered with the proper Internet authorities (see the current best
Ensure that domain names are registered with the proper Internet authorities (see the curre
practice naming standards guidance in section
practice naming standards guidance in section 6.1.7 for more information)

These recommendations provide the following benefits:
These recommendations provide the following benefits:

(cid:1)  Enabling of fault tolerance across a uniform

configuration, with a centrally
fault tolerance across a uniform domain controller configuration, with a centrally

managed, yet distributed, name resolution service that will be available alongside local
managed, yet distributed, name resolution service that will be available alongside local
managed, yet distributed, name resolution service that will be available alongside local
authentication services
authentication services

(cid:1)  Integrating DNS with AD

enables DNS servers to take advantage of the security,
AD DS enables DNS servers to take advantage of the security,

performance, and fault tolerance capabilities of AD DS
performance, and fault tolerance capabilities of

(cid:1)  Microsoft DNS provides efficient name resolution and interoperability designed to fully
Microsoft DNS provides efficient name resolution and interoperability designed to fully
Microsoft DNS provides efficient name resolution and interoperability designed to fully
ecognised industry standards-
DNS requirements. It is also based on recognised industry standards
support all AD DS DNS requirements. It is also based on r
based technologies

The AD DS DNS owner is responsible for the
DNS for the forest
the deployment of AD DS DNS for the forest

DNS design and responsible for overseeing
DNS owner is responsible for the AD DS DNS design and responsible for overseeing

Recommendations
(cid:1)  Ensure that an AD DS DNS Owner role is identified and some

one is assigned to it
DNS Owner role is identified and someone is assigned to it

(cid:1)  Ensure that DNS management permissions are delegated appropriately, and that DNS management
Ensure that DNS management permissions are delegated appropriately, and that DNS management
Ensure that DNS management permissions are delegated appropriately, and that DNS management
processes are understood, documented and followed
processes are understood, documented and followed

Note

can be implemented as long as it supports Service (SRV) records50.
Any DNS server that supports AD DS can be implemented as long as it supports Service (
Any DNS server that supports
It is also strongly recommended that the DNS server supports secure Dynamic Updates51, which requires
It is also strongly recommended that the DNS server supports secure Dynamic Updates
It is also strongly recommended that the DNS server supports secure Dynamic Updates
Berkeley Internet Name Domain (BIND)

Domain (BIND) version 8.2.2, patch 7 or later52.

49 DNS Concepts {R51}:
us/library/dd197461(WS.10).aspx
http://technet.microsoft.com/en-us/library/dd197461(WS.10).aspx

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 62

Prepared by Microsoft

6.4.1.3

Identify the Domain Name System Infrastructure Requirements
Identify the Domain Name System Infrastructure Requirements
Identify the Domain Name System Infrastructure Requirements

rding and conditional forwarding pointers should be configured appropriately. This allows
DNS forwarding and conditional forwarding pointers should be configured appropriately. This allows
rding and conditional forwarding pointers should be configured appropriately. This allows
and for directing
for the required communication internally between healthcare organisations and for directing
for the required communication internally between
ch enables a DNS server to
appropriate external traffic. Conditional forwarding can also be used which enables a DNS server to
appropriate external traffic. Conditional forwarding can also be used whi
forward DNS queries based on the DNS domain name in the query.
forward DNS queries based on the DNS domain name in the query.

Recommendations
(cid:1)  All domain controllers should be configured to forward to the existing DNS infrastructure if one exists.
s should be configured to forward to the existing DNS infrastructure if one exists.
s should be configured to forward to the existing DNS infrastructure if one exists.
(cid:1)  Where possible domain controllers should not be configured to resolve names that are external to the
Where possible domain controllers should not be configured to resolve names that are external to the
Where possible domain controllers should not be configured to resolve names that are external to the
healthcare organisation

(cid:1)  The DNS root zone should be removed from the DNS hierarchy

if it has been installed. This is
The DNS root zone should be removed from the DNS hierarchy if it has been installed
This zone indicates that the server is acting
typically a feature that occurred in Windows 2000 Server. This zone indicates that the server is acting
typically a feature that occurred in W
as a root Internet server, and therefore the DNS server does not use forwarders or root hints in the
as a root Internet server, and therefore the DNS server does not use forwarders or root hints in the
as a root Internet server, and therefore the DNS server does not use forwarders or root hints in the
name-resolution process. To ensure that an internal DNS server forwards queries appropria
resolution process. To ensure that an internal DNS server forwards queries appropriately within
resolution process. To ensure that an internal DNS server forwards queries appropria
the infrastructure and to internal Internet facing DNS servers, it is important to delete the root ‘.’ (also
the infrastructure and to internal Internet facing DNS servers, it is important to delete the root ‘.’ (also
the infrastructure and to internal Internet facing DNS servers, it is important to delete the root ‘.’ (also
known as ’dot’) zone. This also allows for future integration of healthcare organisations
known as ’dot’) zone. This also allows for future integration of

healthcare organisations.

AD DS integrated DNS should utilise the appr
integrated DNS should utilise the appropriate DNS application directory partitions.
integrated DNS data. By limiting the
enable setting of the appropriate replication scope for AD DS integrated DNS data. By limiting the
enable setting of the appropriate replication scope for
in the forest, it is possible to
scope of replication traffic to a subset of the servers running AD DS in the forest, it is possible to
scope of replication traffic to a subset of the servers running
and also help to keep the Global Catalog size down in cases where there
reduce replication traffic and also help to keep the Global Catalog size down in cases where there
and also help to keep the Global Catalog size down in cases where there
are multiple domains in a forest.
are multiple domains in a forest.

opriate DNS application directory partitions. These

Recommendation

Ensure that the DNS application partitions are used for controlling the replication scope.
Ensure that the DNS application partitions are used for controlling the replication scope.
Ensure that the DNS application partitions are used for controlling the replication scope.

’s Active Directory forest is configured with more than one domain,
If the Healthcare organisation’s Active Directory forest is configured with more than one domain,
’s Active Directory forest is configured with more than one domain,
then careful planning of the _msdcs zone is required.
then careful planning of the _msdcs zone is required.

Recommendation

wide DNS application directory partition, thereby
The _msdcs zone should be hosted in the forest-wide DNS application directory partition, thereby
The _msdcs zone should be hosted in the forest
to every DNS server in the forest and enabling clients to find GC servers
replicating to every DNS server in the forest and enabling clients to find GC servers
However if a Microsoft DNS
. This configuration provides replication and security benefits. However if a Microsoft DNS
wide resources. This configuration provides replication and security benefits.
, then the _msdcs zone
or BIND infrastructure has already been deployed to support an existing AD DS, then the _msdcs zone
or BIND infrastructure has already been deployed to su
must be appropriately delegated to allow resolution throughout the forest.
must be appropriately delegated to allow resolution throughout the forest.

 and all other forest-

Ensure that the Active Directory namespace is securely configured such that it is not externally
Ensure that the Active Directory namespace is securely configured such that it is not externally
Ensure that the Active Directory namespace is securely configured such that it is not externally
visible.

50 RFC 2782 – A DNS RR for specifying the location of services (DNS SRV)

A DNS RR for specifying the location of services (DNS SRV) {R52}

51 RFC 2136 – Dynamic Updates in the Domain Name System (DNS UPDATE)

Dynamic Updates in the Domain Name System (DNS UPDATE) {R53}

Configuring BIND to work with Microsoft Active Directory {R54}:

52 Configuring BIND to work with Microsoft
http://www.microsoft.com/technet/archive/interopmigration/linux/mvc/cfgbind.mspx
http://www.microsoft.com/technet/archive/interopmigration/linux/mvc/cfgbind.mspx

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 63

Prepared by Microsoft

Recommendation

The Active Directory namespace should only be visible on the internal network with no external presence.
ectory namespace should only be visible on the internal network with no external presence.
ectory namespace should only be visible on the internal network with no external presence.
Without proper name resolution, users may not be able to locate resources on the network. It is critical
Without proper name resolution, users may not be able to locate resources on the network. It is critical
Without proper name resolution, users may not be able to locate resources on the network. It is critical
not conflict with their internal Active Directory
that the organisation’s Internet facing DNS namespace does not conflict with their internal Active Directory
that the organisation’s Internet facing DNS namespace does
namespace.

DNS servers. It occurs where an organisation gives its AD

Where possible split brain DNS installations should be avoided. This is where the same domain name is
Where possible split brain DNS installations should be avoided. This is where the same domain name is
Where possible split brain DNS installations should be avoided. This is where the same domain name is
AD DS the same name
shared between different DNS servers. It occurs where an organisation gives its
as its external DNS name, for example the external DNS name of a healthcare organisation
as its external DNS name, for example
exampleHealthOrg.org.com and the Active Directory forest name is
y avoided by ensuring the Active Directory
situation provides extra administration work and can be easily avoided by ensuring the Active Directory
situation provides extra administration work and can be easil
, for example,
name is unique such as a delegated name from the public namespace, for example,
name is unique such as a delegated name from the public namespace
HealthOrgAD.exampleHealthOrg.org.com.
HealthOrgAD.exampleHealthOrg.org.com

a healthcare organisation is
and the Active Directory forest name is exampleHealthOrg.org.com

exampleHealthOrg.org.com. This

The Secure Dynamic Updates setting allows only the computers and users specified in an ACL to
The Secure Dynamic Updates setting allows only the computers and users specified in an ACL to
The Secure Dynamic Updates setting allows only the computers and users specified in an ACL to
odify objects within a DNS zone. This enhances the consistency and security of the DNS
modify objects within a DNS zone. This enhances the consistency and security of the DNS
odify objects within a DNS zone. This enhances the consistency and security of the DNS
infrastructure, whilst maintaining the flexibility offered by dynamic update.
infrastructure, whilst maintaining the flexibility offered by dynamic update.

Recommendation

Secure dynamic updates should be enabled53 on DNS zones. By default, this allows members of the
Secure dynamic updates should be enabled
ows members of the
Active Directory forest and domain to register and update DNS records in the zone, but can be extended if
Active Directory forest and domain to register and update DNS records in the zone, but can be extended if
Active Directory forest and domain to register and update DNS records in the zone, but can be extended if
required.

up and removal of stale
DNS Ageing and Scavenging can be configured to allow automatic clean-up and removal of stale
DNS Ageing and Scavenging can be configured to allow automatic clean
resource records (RRs), which can accumulate in zone data over time.
scavenging is most effective this should be enabled on the zone before any host records are added
scavenging is most effective this should be enabled on the zone before any host records are added
scavenging is most effective this should be enabled on the zone before any host records are added
to it. To configure scavenging ensure:
to it. To configure scavenging ensure:

To ensure that the
h can accumulate in zone data over time. To ensure that the

(cid:1)  The zone is configured to scavenge stale records
configured to scavenge stale records

(cid:1)  The specific domain controllers that will perform the scavenging
Recommendation

configured
ific domain controllers that will perform the scavenging are configured

Ageing and Scavenging for DNS should be enabled on two domain controllers (running the DNS Server
(running the DNS Server
Ageing and Scavenging for DNS should be enabled on two
single domain controller, by selecting
service) per domain. Although it is only necessary to enable it on a
. Although it is only necessary to enable it on a single domain controller, by selecting
two the solution is providing for fail-over of the scavenging activity.
two the solution is providing for fail

A DNS client configuration for both the DNS servers and all of their clients should be created. It is
A DNS client configuration for both the DNS servers and all of their clients should be created. It is
A DNS client configuration for both the DNS servers and all of their clients should be created. It is
job aid, named DSSLOGI_8.doc
recommended that this is documented using the DNS Inventory job aid, named DSSLOGI_8.doc
recommended that this is documented using
{R14}.

Recommendations

The DNS client configuration for each
The DNS client configuration for each domain controller should be configured to use itself as
DNS server, and an alternative DNS server in the same site or hub site should be configured as the
DNS server, and an alternative DNS server in the same site or hub site should be configured as the
DNS server, and an alternative DNS server in the same site or hub site should be configured as the
secondary DNS server.

should be configured to use itself as the primary

All other network devices, for example member servers, and Windows XP, Windows Vista
All other network devices, for example member servers, and Windows XP
clients, use a local domain controller
configured as a domain controller

domain controller in another AD DS site preferably the nearest data centre

as their primary DNS server, and their secondary DNS server is
domain controller as their primary DNS server, and their secondary DNS server is

preferably the nearest data centre.

Windows Vista or Windows 7

DNS and NetBIOS names for each domain have been determined during section 6.1.3 and
DNS and NetBIOS names for each domain have been determined during section
DNS and NetBIOS names for each domain have been determined during section
documented using the Domain Planning
for specific guidance on DNS naming standards.
for specific guidance on DNS naming standards.

Domain Planning job aid, named DSSLOGI_5.doc {R14}

}. See section 6.1.7

53 Microsoft Knowledge Base article 816592
http://support.microsoft.com/kb/816592
http://support.microsoft.com/kb/816592

816592 – How to configure DNS dynamic updates in Windows Server 2003

How to configure DNS dynamic updates in Windows Server 2003 {R55}:

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 64

Prepared by Microsoft

6.4.1.4

Integrate AD DS
Infrastructure

into an Existing Domain Name System
DS into an Existing Domain Name System

There are three likely scenarios for DNS configuration within
There are three likely scenarios for DNS configuration within a healthcare organisation
provides recommendations for how to deal with these scenarios.
provides recommendations for how to deal with the

a healthcare organisation. Table 18

DNS Scenario

Recommendation
Recommendation

No existing DNS

(cid:2)  Host all

Host all Healthcare organisation’s local DNS requirements on the AD DS

DS integrated DNS

(cid:2)  Forward any unresolved queries to the Local Service Provider’s (LSP’s) DNS infrastructure
Forward any unresolved queries to the Local Service Provider’s (LSP’s) DNS infrastructure
Forward any unresolved queries to the Local Service Provider’s (LSP’s) DNS infrastructure

(cid:2)  Create a stub zone
DS DNS zone

Create a stub zone or delegation in the LSP DNS infrastructure for the Healthcare organisation
AD DS

Healthcare organisation’s

Existing Windows based DNS
(NT4.0, 2000 or 2003)

(cid:2)  Host only Active Directory DNS requirements on the

integrated DNS
Host only Active Directory DNS requirements on the AD DS integrated DNS

(cid:2)  Consider consolidating all DNS services to

integrated DNS on the DCs
Consider consolidating all DNS services to AD DS integrated DNS on the DCs

(cid:2)  Configure Active Directory DNS to forward all unresolved queries to either the local
Configure Active Directory DNS to forward all unresolved queries to either the local Healthcare
Configure Active Directory DNS to forward all unresolved queries to either the local
organisation
organisation DNS service if not consolidated, or the LSP DNS service if the DNS infra
been consolidated
been consolidated

DNS service if not consolidated, or the LSP DNS service if the DNS infrastructure has

(cid:2)  Create a stub zone
DS DNS zone

Create a stub zone or delegation  in the LSP DNS infrastructure for the
AD DS

in the LSP DNS infrastructure for the Healthcare organisation’s

Existing Unix based DNS

(cid:2)  Host only Active Directory DNS requirements on the

integrated DNS
Host only Active Directory DNS requirements on the AD DS integrated DNS

(cid:2)  Configure

Configure AD DS DNS to forward all unresolved queries to the Unix based DNS in the
organisation
organisation

DNS to forward all unresolved queries to the Unix based DNS in the Healthcare

(cid:2)  Create a stub zone

Create a stub zone or domain delegation in the Unix DNS for the Healthcare organisation
DNS zone
DNS zone

Healthcare organisation’s AD DS

Scenarios and Subsequent Recommendations
Table 18: Existing Domain Name System Scenarios and Subsequent Recommendations

6.4.2  WINS Infrastructure to Support

WINS Infrastructure to Support AD DS

WINS servers map IP addresses to NetBIOS computer names and NetBIOS computer names back
WINS servers map IP addresses to NetBIOS computer names and NetBIOS computer names back
WINS servers map IP addresses to NetBIOS computer names and NetBIOS computer names back
to IP addresses.

6.4.2.1  WINS and Windows Server 200

WINS and Windows Server 2008 R2 AD DS

or Windows 2000, but WINS is required for
8, Windows Server 2003 or Windows 2000, but WINS is required for

WINS54 and NetBIOS are not required in an environment where computers run only
and NetBIOS are not required in an environment where computers run only
and NetBIOS are not required in an environment where computers run only
Windows Server 2008, Windows Server 2003
, computers that are running
interoperability between Windows 2000-based domain controllers, computers that are running
interoperability between Windows
earlier versions of Windows, and applications that depend on the NetBIOS namespace. For
versions of Windows, and applications that depend on the NetBIOS namespace. For
versions of Windows, and applications that depend on the NetBIOS namespace. For
example, applications that call NetServerEnum, and other ‘Net*’ Application Programming
example, applications that call NetServerEnum, and other ‘Net*’ Application Programming
example, applications that call NetServerEnum, and other ‘Net*’ Application Programming
Interfaces (APIs), that depend on NetBIOS.
Interfaces (APIs), that depend on NetBIOS.

54 Deploying WINS {R56}:
http://technet2.microsoft.com/windowsserver/en/library/a5e0f87f-9b40-47ed-b613-3b4963bd91e61033.mspx
http://technet2.microsoft.com/windowsserver/en/library/a5e0f87f
us/library/cc771750(WS.10).aspx
http://technet.microsoft.com/en-us/library/cc771750(WS.10).aspx

3b4963bd91e61033.mspx and

Page 65

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Prepared by Microsoft

Recommendation

The use of WINS in the infrast
ructure should be assessed and minimised where possible, as products
The use of WINS in the infrastructure should be assessed and minimised where possible, as products
exist that still require NetBIOS name resolution in order to function correctly. It is advised that, during
exist that still require NetBIOS name resolution in order to function correctly. It is advised that, during
exist that still require NetBIOS name resolution in order to function correctly. It is advised that, during
upgrade phases, healthcare organisations
g systems that require
healthcare organisations remove older applications and operating systems that require
NetBIOS functionality from the environment. In the meantime, it may be necessary to provide WINS as a
NetBIOS functionality from the environment. In the meantime, it may be necessary to provide WINS as a
NetBIOS functionality from the environment. In the meantime, it may be necessary to provide WINS as a
method for NetBIOS name resolution so that clients can locate older services through a server’s NetBIOS
method for NetBIOS name resolution so that clients can locate older services through a server’s NetBIOS
method for NetBIOS name resolution so that clients can locate older services through a server’s NetBIOS
name.

If a WINS infrastructure is needed, it should be kept as simple and efficient as possible. It may be possible
ure is needed, it should be kept as simple and efficient as possible. It may be possible
ure is needed, it should be kept as simple and efficient as possible. It may be possible
that just two WINS servers in the data centre that are configured as push / pull replication partners proves
that just two WINS servers in the data centre that are configured as push / pull replication partners proves
that just two WINS servers in the data centre that are configured as push / pull replication partners proves
Healthcare organisation.
to be enough to support the entire NetBIOS name resolution requirements for the Healthcare organisation
to be enough to support the entire NetBIOS name resolution

Additional Network Services
6.4.3  Additional Network Services

In provisioning an infrastructure environment, an appreciation of the following network services is
In provisioning an infrastructure environment, an appreciation of the following network services is
In provisioning an infrastructure environment, an appreciation of the following network services is
required:

(cid:1)  Transmission Control Protocol/Internet Protocol (TCP/IP)
Transmission Control Protocol/Internet Protocol (TCP/IP)

(cid:1)  Dynamic Host Configuration Protocol (DHCP)
Configuration Protocol (DHCP)

(cid:1)  Internet Protocol Security (IPSec)
Internet Protocol Security (IPSec)

(cid:1)  Dial-up and Virtual Private Network (VPN)
up and Virtual Private Network (VPN)

(cid:1)  Wireless LAN

Guidance on these technologies can be obtained from:
Guidance on these technologies can be obtained from:

(cid:1)  Windows Server 2003 Product Documentation

Windows Server 2003 Product Documentation {R7}

(cid:1)  Windows Server Systems Reference Architecture

Windows Server Systems Reference Architecture {R1}

(cid:1)  Windows Server 2003 Deployment guide

Windows Server 2003 Deployment guide {R2}

(cid:1)  TechNet Technology Collections

TechNet Technology Collections {R3}

Note

Services mentioned within this section will not be available between healthcare organisations
Services mentioned within this section will not be availa
healthcare organisations
identical IP Address schemes. The use of NAT as a workaround between such healthcare organisations
identical IP Address schemes. The use of NAT as a workaround between such
Environment is neither recommended nor supported by Microsoft.
within an AD DS Environment is neither recommended nor supported by Microsoft.

healthcare organisations that have

read the Assumptions statement in section 2.5, and the Microsoft
For further information please read the Assumptions statement in section 2.5, and the Microsoft
For further information please
whitepaper: Active Directory in Networks Segmented by Firewalls

Active Directory in Networks Segmented by Firewalls55.

Active Directory in Networks Segmented by Firewalls {R57}:

55 Active Directory in Networks Segmented by Firewalls
http://www.microsoft.com/downloads/details.aspx?FamilyID=c2ef3846

a9166368434e&DisplayLang=en
com/downloads/details.aspx?FamilyID=c2ef3846-43f0-4caf-9767-a9166368434e&DisplayLang=en

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 66

Prepared by Microsoft

7

STABILISE

The Stabilise phase involves testing the solution components whose features are complete,
The Stabilise phase involves testing the solution components whose features are complete,
The Stabilise phase involves testing the solution components whose features are complete,
resolving and prioritising any issues that are found. Testing during this phase emphasises usage
g any issues that are found. Testing during this phase emphasises usage
g any issues that are found. Testing during this phase emphasises usage
and operation of the solution components under realistic environmental conditions.
and operation of the solution components under realistic environmental conditions.
and operation of the solution components under realistic environmental conditions.

During this phase, testing and acceptance of the Active Directory service and its associated
During this phase, testing and acceptance of the Active Directory service and its associated
During this phase, testing and acceptance of the Active Directory service and its associated
network components will take place. The aim is to minimise the impact on normal business
components will take place. The aim is to minimise the impact on normal business
components will take place. The aim is to minimise the impact on normal business
operations by testing the design assumptions and verifying the deployment process in a pilot
operations by testing the design assumptions and verifying the deployment process in a pilot
operations by testing the design assumptions and verifying the deployment process in a pilot
program. It is important that this phase of testing and verifying should begin during the Design
program. It is important that this phase of testing and verifying should begin dur
program. It is important that this phase of testing and verifying should begin dur
phase and continue through the Deployment and Operations phase.
phase and continue through the Deployment and Operations phase.

level checklist, illustrating the critical components that an IT Professional
level checklist, illustrating the critical components that an
Figure 11 acts as a high-level checklist, illustrating the critical components that an
responsible for testing and validating the design of AD DS needs to determine:
responsible for testing and validating the design of

Figure 11: Sequence for Stabilising the AD DS

DS Design

Design a Test Environment
7.1  Design a Test Environment

Overview of a Test Environment
7.1.1  Overview of a Test Environment

Before deploying AD DS, even during a pilot, it is vital to test the proposed design in an
, even during a pilot, it is vital to test the proposed design in an
, even during a pilot, it is vital to test the proposed design in an
environment that simulates and protects the existing production environment. In this test
environment that simulates and protects the existing production environment. In this test
environment that simulates and protects the existing production environment. In this test
environment, it will be possible to test hardware, operating systems, or applications designed to run
environment, it will be possible to test hardware, operating systems, or applications designed to
environment, it will be possible to test hardware, operating systems, or applications designed to
test environment consists of a
together, before introducing them into the production environment. A test environment
together, before introducing them into the production environment. A
lab, detailed plans of what will be tested, and test cases that describe how each component of the
lab, detailed plans of what will be tested, and test cases that describe how each component of the
lab, detailed plans of what will be tested, and test cases that describe how each component of the

Page 67

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

t, as a minimum, there will be a second
design and deployment will be tested. This means that, as a minimum, there will be a second
design and deployment will be tested. This means tha
Active Directory forest for each
in the dedicated test environment.
in the dedicated test environment.

, one in the production environment and one
forest for each healthcare organisation, one in the production environment and one

Prepared by Microsoft

server virtualisation (there is specific documented guidance around Micr

By using server virtualisation (there is specific documented guidance around
it is possible to install and configure
This platform is well suited for test environments enabling a rapid reinstall back to a baseline
This platform is well suited for test environments enabling a rapid reinstall back to a baseline
This platform is well suited for test environments enabling a rapid reinstall back to a baseline
configuration to repeat new tests.
configuration to repeat new tests

and configure multiple virtual domain controllers on a single physical server

on a single physical server.

Microsoft® Hyper-V56),

reate a Test Plan
7.1.2  Create a Test Plan

be created. This should define the following
It is critical to the success of the testing, that a test plan be created. This should define the following
It is critical to the success of the testing, that a
components:

(cid:1)  The testing scope and objectives of the testing effort
The testing scope and objectives of the testing effort

(cid:1)  The testing methodology that the IT test team will use to condu

ct the tests
The testing methodology that the IT test team will use to conduct the tests

(cid:1)  The required resources, such as hardware, software and tools required for testing
The required resources, such as hardware, software and tools required for testing
The required resources, such as hardware, software and tools required for testing

(cid:1)  The features and functions that will be tested
The features and functions that will be tested

(cid:1)  The risk factors that may jeopardise testing
The risk factors that may jeopardise testing

(cid:1)  A testing schedule

Recommendations

It is important to include tests that verify or address the following:
It is important to include tests
(cid:1)  The functionality of a feature is being used as the design intended
The functionality of a feature is being used as the design intended
(cid:1)  Interoperability with existing components and systems in the production environment
Interoperability with existing components and systems in the production environment
Interoperability with existing components and systems in the production environment
(cid:1)  Hardware, driver, software and application compatibility testing f
(cid:1)  Baselines and stress tests for capacity planning
Baselines and stress tests for capacity planning
(cid:1)  Procedures for deployment and back
(cid:1)  Tests for the required tools and utilities
Tests for the required tools and utilities

Hardware, driver, software and application compatibility testing for the domain controller

out plans, should any issues occur during deployment
Procedures for deployment and back-out plans, should any issues occur during deployment

domain controllers

7.1.3

Plan a Test Lab
Plan a Test Lab

signed for testing, and is isolated from the production network. The
A test lab is a network that is designed for testing, and is isolated from the production network. The
A test lab is a network that is de
test lab is used to verify that components and features work correctly together in an integrated
test lab is used to verify that components and features work correctly together in an integrated
test lab is used to verify that components and features work correctly together in an integrated
environment that simulates the target production environment.
environment that simulates the target production environment.

When establishing a test lab, it is necessary to decide how it will be set up
following options:

, it is necessary to decide how it will be set up57. This could include the
. This could include the

(cid:1)  Upgrade an existing test lab versus building a new test lab
Upgrade an existing test lab versus building a new test lab

(cid:1)  Create an ad hoc test lab versus a permanent test lab
Create an ad hoc test lab versus a permanent test lab

(cid:1)  Have the test lab centralised versus distributed
Have the test lab centralised versus distributed

56 Running Domain Controllers in Hyper
us/library/dd363553(WS.10).aspx
 http://technet.microsoft.com/en-us/library/dd363553(WS.10).aspx

Hyper-V {R58}:

57 Planning the Test Plan {R60}:
http://technet2.microsoft.com/windowsserver/en/library/05f4d318-f2b4-4544-b50a-6aef2174532a1033.mspx
http://technet2.microsoft.com/windowsserver/en/library/05f4d318

6aef2174532a1033.mspx

Page 68

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Prepared by Microsoft

Design the Test Lab
7.1.4  Design the Test Lab

The lab planning process includes documenting the proposed test lab configuration. To design a
The lab planning process includes documenting the proposed test lab configuration. To design a
The lab planning process includes documenting the proposed test lab configuration. To design a
lab that mimics the future production environment, it will also need to simulate the proposed server
lab that mimics the future production environment, it will also need to simulate the proposed server
lab that mimics the future production environment, it will also need to simulate the proposed server
and client environments as closely as possible that will utilise AD DS.
and client environments as closely as p

Designing the test lab will involve:
Designing the test lab will involve:

(cid:1)  Gathering information about the current and proposed environments
Gathering information about the current and proposed environments

(cid:1)  Documenting the test lab configuration so that it can be rebuilt as and when required
Documenting the test lab configuration so that it can be rebuilt as and when required
Documenting the test lab configuration so that it can be rebuilt as and when required

(cid:1)  Simulating the proposed server env

Simulating the proposed server environment

(cid:1)  Simulating the proposed client computer environment
Simulating the proposed client computer environment

(cid:1)  Designing domains for testing
Designing domains for testing

The documentation of the test lab should form two documents, one which details the components
The documentation of the test lab should form two documents, one which details the components
The documentation of the test lab should form two documents, one which details the components
r document that details
required, such as servers, switches/hubs, UPS, workstations, and anothe
required, such as servers, switches/hubs, UPS, workstations, and another document that details
both the logical and physical diagrams of the test lab58.
both the logical and physical diagrams of the test lab

Develop the Test Lab
7.1.5  Develop the Test Lab

Once the test lab planning process is finalised and has received management approval, it is
Once the test lab planning process is finalised and has received management approval, it is
Once the test lab planning process is finalised and has received management approval, it is
ormed to ensure smooth operation of
necessary to build the lab. The following steps should be performed to ensure smooth operation of
necessary to build the lab. The following steps should be perf
the lab:

(cid:1)  Assign a test lab manager
Assign a test lab manager

(cid:1)  Build the test lab

(cid:1)  Develop test lab guidelines and procedures
Develop test lab guidelines and procedures

Recommendations
(cid:1)  It is recommended that, when building the test lab, every change made to server and client computers
It is recommended that, when building the test lab, every change made to server and client computers
It is recommended that, when building the test lab, every change made to server and client computers
umented in chronological order. This documentation can help resolve problems that might arise
is documented in chronological order. This documentation can help resolve problems that might arise
umented in chronological order. This documentation can help resolve problems that might arise
later and help explain why a specific computer behaves as it does over time
later and help explain why a specific computer behaves as it does over time

(cid:1)  Ensure that an escalation plan
problems arise during testing
problems arise during testing

escalation plan is created which describes what the test team needs to

is created which describes what the test team needs to do when

(cid:1)  Ensure that an incident-tracking system

tracking system59 is used for recording and reporting bugs and other testing
is used for recording and reporting bugs and other testing

problems, recording how they are resolved and the test results
problems, recording how they are resolved and the test results

Note

While this document outlines the ideal approach based on the experiences of Microsoft Services with
While this document outlines the ideal approach based on the experiences of Microsoft Services with
While this document outlines the ideal approach based on the experiences of Microsoft Services with
healthcare organisations simply
large scale infrastructure deployment projects it is understood that many healthcare organisations
large scale infrastructure deployment projects it is understood that many
etwork Managers and Test Lab managers. It is likely to
do not have the staff resources to be appointing Network Managers and Test Lab managers. It is likely to
do not have the staff resources to be appointing N
be the same person in many cases. The primary principle here is that there is some accountability and an
be the same person in many cases. The primary principle here is that there is some accountability and an
be the same person in many cases. The primary principle here is that there is some accountability and an
agreement from management that the lab facilities are properly considered and implemented to allow
agreement from management that the lab facilities are properly considered and implemented to all
agreement from management that the lab facilities are properly considered and implemented to all
proper testing of the solution before they are rolled out into production.
proper testing of the solution before they are rolled out into production.

58 Documenting the Test Lab Configuration
Documenting the Test Lab Configuration {R61}:
ttp://technet2.microsoft.com/windowsserver/en/library/232b6b08-d5b7-4437-bddf-a142636091741033.mspx
http://technet2.microsoft.com/windowsserver/en/library/232b6b08

a142636091741033.mspx

59 Developing an Incident-Tracking System
http://technet2.microsoft.com/windowsserver/en/library/e213d6a5-7d4e-48cf-87b8-00eb52aae61f1033.mspx
 http://technet2.microsoft.com/windowsserver/en/library/e213d6a5

Tracking System {R62}:

00eb52aae61f1033.mspx

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 69

Design the Test Cases
7.1.6  Design the Test Cases

A test case is a detailed procedure that fully tests a feature, or an aspect of a feature. Whereas the
is a detailed procedure that fully tests a feature, or an aspect of a feature. Whereas the
is a detailed procedure that fully tests a feature, or an aspect of a feature. Whereas the
bes how to perform a particular test. A test case
test plan describes what to test, a test case descri
test plan describes what to test, a test case describes how to perform a particular test. A test case
needs developing for each test listed in the test plan.
needs developing for each test listed in the test plan.

Prepared by Microsoft

A test case includes:

(cid:1)  The purpose of the test
The purpose of the test

(cid:1)  Special hardware requirements, such as a modem
Special hardware requirements, such as a modem

(cid:1)  Special software requirements, such as a utility or tool
Special software requirements, such as a utility or tool

(cid:1)  Specific setup or configuration requirements
Specific setup or configuration requirements

(cid:1)  A description of how to perform the test
A description of how to perform the test

(cid:1)  The expected results or success criteria for the test
The expected results or success criteria for the test

Full test case instructions for testing AD DS are provided in the Appendices of the document
Full test case instructions for testing
Windows Server System Reference Architecture
convenience the test descriptions are listed within

(which is no longer publicly available) but for
System Reference Architecture, (which is no longer publicly available) but for

of this document.
the test descriptions are listed within APPENDIX E of this document.

are provided in the Appendices of the document The

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 70

duct the Tests
7.1.7  Conduct the Tests

When conducting tests, the tester must perform each test as described in the test case, evaluate
When conducting tests, the tester must perform each test as described in the test case, evaluate
When conducting tests, the tester must perform each test as described in the test case, evaluate
the test results, escalate problems that arise until they are resolved, and document the test results.
the test results, escalate problems that arise until they are resolved, and document the test results.
the test results, escalate problems that arise until they are resolved, and document the test results.
illustrates the testing process:
Figure 12 illustrates the testing process:

Prepared by Microsoft

Figure 12: The Testing Process

Recommendation

It is highly likely that the lab will change frequently as tests are run an
d new tests are begun. It is
It is highly likely that the lab will change frequently as tests are run and new tests are begun. It is
recommended that backups of baseline configurations are made so that testers can quickly restore a
recommended that backups of baseline configurations are made so that testers can quickly restore a
recommended that backups of baseline configurations are made so that testers can quickly restore a
computer to its prior state. The restore process should be tested and backup files should be documented
computer to its prior state. The restore process should be tested and backup files should be documented
computer to its prior state. The restore process should be tested and backup files should be documented
and stored in a safe, accessible place.
Virtual Server images it should be possible to create a solution where changes can be rolled back to a
Virtual Server images it should be possible to create a solution where changes can be rolled back to a
Virtual Server images it should be possible to create a solution where changes can be rolled back to a
consistent state if the testing results in a negative result. Great care st
ill needs to be taken to avoid issues
consistent state if the testing results in a negative result. Great care still needs to be taken to avoid issues
such as Update Sequence Number (USN) Rollback and selectively restoring previous images of some
such as Update Sequence Number (USN) Rollback and selectively restoring previous images of some
such as Update Sequence Number (USN) Rollback and selectively restoring previous images of some
servers and not others.

With the snapshot technology in place and the ability to save
cessible place. With the snapshot technology in place and the ability to save

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 71

Prepared by Microsoft

Use the Test Lab After Deployment
7.1.8  Use the Test Lab After Deployment

ploying Windows Server 2008 R2,
The importance of testing changes to the IT environment after de
The importance of testing changes to the IT environment after deploying Windows Server
and the latest Windows clients
cannot be overemphasised. Due to the potential effect that changes
and the latest Windows clients cannot be overemphasised. Due to the potential effect that changes
can have in the production environment, it is important to test every update and Service Pack until
can have in the production environment, it is important to test every update and
can have in the production environment, it is important to test every update and
e achieved, before they are piloted or rolled out to the production
the anticipated results are achieved, before they are piloted or rolled out to the production
e achieved, before they are piloted or rolled out to the production
environment.

Recommendation

As far as possible, the test lab should remain in place after deployment. This will enable continued testing
As far as possible, the test lab should remain in place after deployment. This will enable continued testing
As far as possible, the test lab should remain in place after deployment. This will enable continued testing
ions are made, avoiding adverse affects occurring
of the infrastructure, as and when new design decisions are made, avoiding adverse affects occurring
of the infrastructure, as and when new design decis
within the production environment.
within the production environment.

Design a Pilot Project
7.2  Design a Pilot Project

Conducting the pilot is the last major step before deployment of the Windows Server 2008 R2
Conducting the pilot is the last major step before deployment of the Windows Server 200
Conducting the pilot is the last major step before deployment of the Windows Server 200
deployment of a test environment and
. The pilot should include the creation of a plan, deployment of a test environment and
AD DS. The pilot should include the creation of a plan,
testing by designated users. The results are then evaluated to ensure the pilot was successful.
testing by designated users. The results are then evaluated to ensure the pilot was successful.
testing by designated users. The results are then evaluated to ensure the pilot was successful.

Overview of a Pilot Project
7.2.1  Overview of a Pilot Project

During the pilot, tests of the design take place in a controlled environment in which users perform
During the pilot, tests of the design take place in a controlled environment in which users per
During the pilot, tests of the design take place in a controlled environment in which users per
their normal business tasks using the new features. This demonstrates that the design works in the
their normal business tasks using the new features. This demonstrates that the design works in the
their normal business tasks using the new features. This demonstrates that the design works in the
production environment as expected, and that it meets the
production environment as expected, and that it meets the Healthcare organisation
ed back into testing and redesigned
requirements. Any encountered problems can immediately be fed back into testing and redesigned
requirements. Any encountered problems can immediately be f
as required, therefore minimising the risk to the business of issues during deployment. Figure 13
as required, therefore minimising the risk to the business of issues during deployment.
as required, therefore minimising the risk to the business of issues during deployment.
illustrates the process of planning and conducting a pilot project:
illustrates the process of planning and conducting a pilot project:

Healthcare organisation’s business

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 72

Prepared by Microsoft

Figure 13: Designing a Pilot Project

Although the pilot is conducted during the Test and Validate phase of the project cycle, planning for
Although the pilot is conducted during the Test and Validate phase of the project cycle, planning for
Although the pilot is conducted during the Test and Validate phase of the project cycle, planning for
ng the Define and Plan phases of the deployment project, and preparing for the
the pilot occurs during the Define and Plan phases of the deployment project, and preparing for the
ng the Define and Plan phases of the deployment project, and preparing for the
d in planning for and
pilot occurs during development. Figure 14 illustrates the tasks involved in planning for and
pilot occurs during development.
conducting a pilot, and shows the appropriate phase during which each of these activities might
conducting a pilot, and shows the appropriate phase during which each of these activities might
conducting a pilot, and shows the appropriate phase during which each of these activities might
occur. The timeframes are generic estimations that will obviously vary from deployment to
occur. The timeframes are generic estimations that will obviously vary from deployment to
occur. The timeframes are generic estimations that will obviously vary from deployment to
deployment.

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 73

Prepared by Microsoft

: Role of the Pilot in the Project Lifecycle
Figure 14: Role of the Pilot in the Project Lifecycle

Create a Pilot Plan
7.2.2  Create a Pilot Plan

The pilot plan60 should define:

(cid:1)  The scope and objectives of the pilot
The scope and objectives of the pilot

(cid:1)  Pilot participants and where the pilot will be conducted
Pilot participants and where the pilot will be conducted

(cid:1)  A schedule for deploying and conducting the pilot
A schedule for deploying and conducting the pilot

(cid:1)  Plans for training and communicating with pilot participants
ing and communicating with pilot participants

(cid:1)  Evaluation of the pilot

(cid:1)  Risks and contingencies
Risks and contingencies

7.2.3

Prepare for the Pilot
Prepare for the Pilot

Preparation for the pilot61 deployment begins with development, during the Build phase of the
deployment begins with development, during the Build phase of the
deployment begins with development, during the Build phase of the
project, and should consider:

(cid:1)  Preparation of the pilot sites
e pilot sites

(cid:1)  Preparation of the pilot participants
Preparation of the pilot participants

(cid:1)  Testing of the rollout process
Testing of the rollout process

60 Creating a Pilot Plan {R63}:
http://technet2.microsoft.com/windowsserver/en/library/99f07a8e-503b-4751-b108-c85e188ada951033.mspx
http://technet2.microsoft.com/windowsserver/en/library/99f07a8e

c85e188ada951033.mspx

61 Preparing for the Pilot {R64}:
http://technet2.microsoft.com/windowsserver/en/library/0a5f853e-28d2-4afe-a9db-92761a8d3ed61033.mspx
http://technet2.microsoft.com/windowsserver/en/library/0a5f853e

92761a8d3ed61033.mspx

Page 74

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Prepared by Microsoft

Deploy and Test the Pilot
7.2.4  Deploy and Test the Pilot

When deploying the pilot, the Windows Server
implementation is being tested
When deploying the pilot, the Windows Server 2008 R2 AD DS implementation is being tested
under live conditions. The pilot deployment process should be started with a trial run of the pilot to
under live conditions. The pilot deployment process should be started with a trial run of the pilot to
under live conditions. The pilot deployment process should be started with a trial run of the pilot to
identify problems with the deployment and the pilot plan. Then, when the full pilot begins, keep
identify problems with the deployment and the pilot plan. Then, when the full pilot begins, keep
identify problems with the deployment and the pilot plan. Then, when the full pilot begins, keep
t tasks have been completed so that it is possible to monitor the progress
track of which deployment tasks have been completed so that it is possible to monitor the progress
t tasks have been completed so that it is possible to monitor the progress
of the pilot.

As participants use the system, it is advised that the pilot team track the progress of the pilot and
As participants use the system, it is advised that the pilot team track the progress of the pilot and
As participants use the system, it is advised that the pilot team track the progress of the pilot and
areas of concern. All participants should be encouraged to use the incident
identify areas of concern. All participants should be encouraged
to report problems and to use the escalation plan when immediate problem resolution is not
to report problems and to use the escalation plan when immediate problem resolution is not
to report problems and to use the escalation plan when immediate problem resolution is not
possible.

to use the incident-tracking system

7.2.5

Evaluate the Pilot
Evaluate the Pilot

When the pilot is complete, feedback should be obtained from a variety of sources, including
When the pilot is complete, feedback should be obtained from a variety of sources, including
When the pilot is complete, feedback should be obtained from a variety of sources, including
pants, pilot management and support teams, and other observers, to evaluate the success of
participants, pilot management and support teams, and other observers, to evaluate the success of
pants, pilot management and support teams, and other observers, to evaluate the success of
the pilot.

Once enough pilot data has been collected, and participant feedback has been evaluated, the team
Once enough pilot data has been collected, and participant feedback has been evaluated, the team
Once enough pilot data has been collected, and participant feedback has been evaluated, the team
must decide how to proceed. Depending on how well the pil
ot meets the success criteria, there are
must decide how to proceed. Depending on how well the pilot meets the success criteria, there are
a number of strategies that can be employed at this point in the pilot deployment:
a number of strategies that can be employed at this point in the pilot deployment:
a number of strategies that can be employed at this point in the pilot deployment:

(cid:1)  Overlap the stages of the pilot when moving forward
Overlap the stages of the pilot when moving forward

(cid:1)  Roll back the pilot

(cid:1)  Suspend the pilot

(cid:1)  Update the pilot and continue
Update the pilot and continue

(cid:1)  Proceed to the production deployment phase
the production deployment phase

The pilot is not complete until the team ensures that the proposed solution is viable in the
The pilot is not complete until the team ensures that the proposed solution is viable in the
The pilot is not complete until the team ensures that the proposed solution is viable in the
production environment and that every component of the solution is ready for deployment.
production environment and that every component of the solution is ready for deployment.
production environment and that every component of the solution is ready for deployment.

Prepare for Production Deployment
7.3  Prepare for Production Deployment

Once the team has agreed that the pilot has been successfully completed and has obtained
team has agreed that the pilot has been successfully completed and has obtained
team has agreed that the pilot has been successfully completed and has obtained
management approval for proceeding, the next step is to fully deploy the system to the appropriate
management approval for proceeding, the next step is to fully deploy the system to the appropriate
management approval for proceeding, the next step is to fully deploy the system to the appropriate
Healthcare organisation level. During this phase, the release team should de
technology and site components, stabilise the deployment, transition the management of the
technology and site components, stabilise the deployment, transition the management of the
technology and site components, stabilise the deployment, transition the management of the
project to the operations and support teams, and obtains final management approval of the project.
project to the operations and support teams, and obtains final management approval of the project.
project to the operations and support teams, and obtains final management approval of the project.

ploy the core
level. During this phase, the release team should deploy the core

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 75

Prepared by Microsoft

8  DEPLOY

The Deploy phase is used to manage the deploy
ment of core solution components for widespread
The Deploy phase is used to manage the deployment of core solution components for widespread
adoption in a controlled environment. During the managed deployment, the solution is tested and
adoption in a controlled environment. During the managed deployment, the solution is tested and
adoption in a controlled environment. During the managed deployment, the solution is tested and
planned deployment of solution
validated through ongoing monitoring and evaluation. A well-planned deployment of solution
validated through ongoing monitoring and evaluation. A well
end system will enable the delivery of a quality service that meets or
components as an end-to-end system will enable the delivery of a quality service that meets or
end system will enable the delivery of a quality service that meets or
exceeds customer expectations.
exceeds customer expectations.

This section describes the build process for the Windows Server 2008 R2 AD DS
This section describes the build process for the Windows Server 200
provides additional configuration information required for the
supporting network services, such as
provides additional configuration information required for the supporting network services, such as
DNS. Once installed and configured, it is vital to test and validate the functionality of AD DS before
DNS. Once installed and configured, it is vital to test and validate the functionality of
DNS. Once installed and configured, it is vital to test and validate the functionality of
using this mission critical system. This section provides AD DS deployment information that is not
deployment information that is not
using this mission critical system. This section provides
and, as such, can be used
healthcare scenarios mentioned in section 4.4.1 and, as such, can be used
specific to each of the healthcare
in a multitude of different scenarios.
in a multitude of different scenarios.

DS forest and

Successful completion of the guidance give
n in this section requires that the IT Professionals
Successful completion of the guidance given in this section requires that the IT Professionals
concerned have a certain level of technical knowledge and deployment experience.
concerned have a certain level of technical knowledge and deployment experience.
concerned have a certain level of technical knowledge and deployment experience.

The designated forest owner is responsible for deploying the forest root domain. After the forest
The designated forest owner is responsible for deploying the forest root domain. After the forest
The designated forest owner is responsible for deploying the forest root domain. After the forest
s complete, the remainder of the Active Directory forest should be
root domain deployment is complete, the remainder of the Active Directory forest should be
s complete, the remainder of the Active Directory forest should be
deployed as specified by the AD

AD DS design (see section 6 for further details).

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 76

level checklist, illustrating the critical components that an IT Professional
Figure 15 acts as a high-level checklist, illustrating the critical components that an IT Professional
level checklist, illustrating the critical components that an IT Professional
responsible for deploying AD DS

DS needs to determine:

Prepared by Microsoft

Figure 15: Sequence for Deploying AD DS

Deployment Prerequisites
8.1  AD DS Deployment Prerequisites

Before beginning the AD DS deployment (by promoting a server to be the first
domain controller
deployment (by promoting a server to be the first domain controller
and therefore creating the forest), it is important to ensure the following prerequisites have been
and therefore creating the forest), it is important to ensure the following prerequisites have been
and therefore creating the forest), it is important to ensure the following prerequisites have been
completed:

(cid:1)  Review of the AD DS forest (logical, physical and security) and network services design,
forest (logical, physical and security) and network services design,
forest (logical, physical and security) and network services design,

utilising the job aids that have been completed during the Build phase
utilising the job aids that have been completed during

(cid:1)  The Network is operational and configured as required
The Network is operational and configured as required

(cid:1)  Windows Server 2008 R2

operating system base build is complete, as per the requirements
8 R2 operating system base build is complete, as per the requirements

of the Windows Server 200

Windows Server 2008 R2 Build {R4}

(cid:1)  The domain controller

drives have been configured as stated in the design
 drives have been configured as stated in the design

(cid:1)  The chosen Active Directory forest DNS name has been registered
The chosen Active Directory forest DNS name has been registered

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 77

Prepared by Microsoft

(cid:1)  Any existing DNS service in the

has been configured with a
Any existing DNS service in the healthcare organisation has been configured with a
delegation (optional, depending on the environment). The DNS administrator of the existing
delegation (optional, depending on the environment). The DNS administrator of the existing
delegation (optional, depending on the environment). The DNS administrator of the existing
healthcare organisation
DNS service must delegate the zone that matches the name of the
healthcare organisation DNS service must delegate the zone that matches the name of the
forest root domain to the DNS servers (DCs) that will be installed in the forest root domain
forest root domain to the DNS servers (DCs) that will be installed in the fo
forest root domain to the DNS servers (DCs) that will be installed in the fo

(cid:1)  The DNS service has been installed on the server which will become a
The DNS service has been installed on the server which will become a domain controller.
The DNS service has been installed on the server which will become a
The domain controller promotion process can configure DNS automatically if the installation
The domain controller promotion process can configure DNS automatically if the installation
The domain controller promotion process can configure DNS automatically if the installation
defaults match those that the Healthcare organisation wishes to use. If the
defaults match those that the
has separate configuration requirements these must be configured (as much
organisation has separate configuration requirements these must be configured (as much
has separate configuration requirements these must be configured (as much
as they can be) prior to promoting the server62
as they can be) prior to promoting the server

s to use. If the Healthcare

(cid:1)  Configure the Time Service on the server that is to be configured as the Active Directory
Configure the Time Service on the server that is to be configured as the Active Directory
Configure the Time Service on the server that is to be configured as the Active Directory
st PDC emulator role holder, to synchronise from a valid Network Time Protocol (NTP)
forest PDC emulator role holder, to synchronise from a valid Network Time Protocol (NTP)
st PDC emulator role holder, to synchronise from a valid Network Time Protocol (NTP)
. By default this will be the first domain controller installed in each domain
source. By default this will be the first domain controller installed in each domain
. By default this will be the first domain controller installed in each domain

(cid:1)  All necessary operations and support staff are in place to take ownership of the
All necessary operations and support staff are in place to take ownership of the AD DS
All necessary operations and support staff are in place to take ownership of the

Recommendation

It is recommended that a hardware based clock for time synchronisation is installed, such as a radio or a
It is recommended that a hardware based clock for time synchronisation is installed, such as a radio or a
It is recommended that a hardware based clock for time synchronisation is installed, such as a radio or a
GPS device, and that this is used as the source for the Windows Time Service on the PDC emulator. If
GPS device, and that this is used as the source for the Windows Time Service on the PDC emulator. If
GPS device, and that this is used as the source for the Windows Time Service on the PDC emulator. If
ernal time server should be used such as time.windows.com.
this is not possible, then an external time server should be used such as time.windows.com.
this is not possible, then an ext

Deployment Strategy
8.2  AD DS Deployment Strategy

The first domain that is created in the Active Directory forest is automatically designated as the
The first domain that is created in the Active Directory forest is automatically designated as the
The first domain that is created in the Active Directory forest is automatically designated as the
he Active Directory forest
forest root domain. The forest root domain provides the foundation for the Active Directory forest
forest root domain. The forest root domain provides the foundation for t
infrastructure.

It is possible to save time during the deployment process by automating installations and by using
It is possible to save time during the deployment process by automating installations and by using
It is possible to save time during the deployment process by automating installations and by using
Installation Wizard, rather than installing via a purely manual configuration. This is
the AD DS Installation Wizard, rather than installing via a purely manual configuration. This is
Installation Wizard, rather than installing via a purely manual configuration. This is
discussed further in section 8.3.1

8.3.1.

Forest Root Domain Deployment
8.2.1  AD DS Forest Root Domain Deployment

The first step in creating the forest root domain is deploying the first forest root
The first step in creating the forest root domain is deploying the first forest root
The forest owner is responsible for deploying the forest root domain. This is followed by the
The forest owner is responsible for deploying the forest root domain. This is followed by the
The forest owner is responsible for deploying the forest root domain. This is followed by the
deployment of the second domain controller
operations master role placement.
operations master role placement.

, DNS reconfiguration, site topology configuration and
domain controller, DNS reconfiguration, site topology configuration and

domain controller.

8.2.1.1

Deploy the First Root Domain Controller
Deploy the First Root Domain

To deploy the first domain controller

in the forest root domain, complete the following tasks:
domain controller in the forest root domain, complete the following tasks:

(cid:1)  Install Windows Server 200
Install Windows Server 2008 R2 including any available service packs and patches
on the Windows Server 200

Windows Server 2008 R2 Build {R4}

any available service packs and patches, based

(cid:1)  Install AD DS, using either a scripted install or DCPromo to start the

, using either a scripted install or DCPromo to start the AD

AD DS Installation

Wizard. (See section 8.3

8.3 for more information on this step.)

(cid:1)  Verify the AD DS installation. (See section

installation. (See section 8.4 for more information.)

(cid:1)  Verify DNS server recursive name resolution

Verify DNS server recursive name resolution63

Configuring DNS for the Forest Root Domain {R65}:

62 Configuring DNS for the Forest Root Domain
us/library/cc771849(WS.10).aspx
 http://technet.microsoft.com/en-us/library/cc771849(WS.10).aspx

Verify DNS Server Recursive Name Resolution on the First Forest Root Domain Controller {R66}

63 Verify DNS Server Recursive Name Resolution on the First Forest Root Domain Controller
us/library/cc754529(WS.10).aspx
http://technet.microsoft.com/en-us/library/cc754529(WS.10).aspx

}:

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 78

8.2.1.2

Deploy the Second Domain Controller in the Same Site
Deploy the Second Domain Controller in the Same Site
Deploy the Second Domain Controller in the Same Site

After deploying the first forest root domain controller, deploy the second forest root
After deploying the first forest root
in the same site, according to the design. To deploy the second forest root domain
in the same site, according to the design. To deploy the second forest root
controller in the same site, according to the design. To deploy the second forest root
, complete the following tasks:
controller, complete the following tasks:

, deploy the second forest root domain

Prepared by Microsoft

(cid:1)  Install Windows Server 200
Install Windows Server 2008 R2 including any available service packs and updates
on the Windows Server 200

Windows Server 2008 R2 Build {R4}

any available service packs and updates, based

(cid:1)  Install AD DS, using either a scripted install or Dcpromo to start the

, using either a scripted install or Dcpromo to start the AD

 DS Installation

Wizard (see section 8.3

8.3 for more information on this step)

(cid:1)  Install DNS Server service after

installation has finished and the computer has
Install DNS Server service after AD DS installation has finished and the computer has
restarted

(cid:1)  Verify the AD DS installation (see

installation (see section 8.4 for more information)

8.2.1.3

Reconfigure the Domain Name System Service
Reconfigure the Domain Name System Service

Reconfigure the DNS service to account for the addition of the second domain controlle
Reconfigure the DNS service to account for the addition of the second
forest root domain. It is also possible to use these procedures as additional
forest root domain. It is also possible to use these procedures as additional domain controller
deployed, which are running the DNS service.
deployed, which are running the DNS service.

domain controller in the

domain controllers are

To reconfigure the DNS service:
To reconfigure the DNS service:

(cid:1)  Enable Ageing and Scavenging for DNS on two DCs running the DNS Serv
Enable Ageing and Scavenging for DNS on two DCs running the DNS Server service per
Enable Ageing and Scavenging for DNS on two DCs running the DNS Serv
domain, to allow automatic cleanup and removal of stale RRs, which can accumulate in
domain, to allow automatic cleanup and removal of stale RRs, which can accumulate in
domain, to allow automatic cleanup and removal of stale RRs, which can accumulate in
zone data over time

(cid:1)  Configure the DNS client settings of the first and subsequent

Configure the DNS client settings of the first and subsequent domain controller

domain controllers

(cid:1)  Update the DNS delegation
Update the DNS delegation

the TechNet Web page ‘Reconfigure the DNS Service’64.
the TechNet Web page ‘Reconfigure the DNS Service’
For more detailed steps, see the TechNet Web page ‘Reconfigure the DNS Service’

8.2.1.4

Configure the Site Topology
Configure the Site Topology

The site topology owner configures the site topology for the forest. Configuring the site topology for
The site topology owner configures the site topology for the forest. Configuring the site topology for
The site topology owner configures the site topology for the forest. Configuring the site topology for
the forest involves the following tasks:
the forest involves the following tasks:

(cid:1)  Delegating AD DS site administration. The forest owner should delegate this task to a
site administration. The forest owner should delegate this task to a
site administration. The forest owner should delegate this task to a

designated site topology owner
designated site topology owner

(cid:1)  Creating required AD DS

Sites and Services MMC
DS sites using the AD DS Sites and Services MMC

(cid:1)  Creating and assigning

Sites and Services MMC
Creating and assigning AD DS subnets using the AD DS Sites and Services MMC

(cid:1)  Creating AD DS site links using the

site links using the AD DS Sites and Services MMC

8.2.1.5

Deploy Additional Domain Controllers in Other Sites (Optional)
Deploy Additional Domain Controllers in Other Sites (Optional)
Deploy Additional Domain Controllers in Other Sites (Optional)

s in other sites, they
If the design specifies deployment of additional forest root domain controllers in other sites, they
If the design specifies deployment of additional forest root
should be deployed using the procedures listed in section 8.2.1.2.
should be deployed using the procedur

64 Reconfigure the DNS service {R67}
}:
http://technet.microsoft.com/en-us/library/cc732922(WS.10).aspx

us/library/cc732922(WS.10).aspx

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 79

Prepared by Microsoft

8.2.1.6

Configure Operations Master Roles
Configure Operations Master Roles

level operations master roles for the forest root domain should be
The forest-level and domain-level operations master roles for the forest root domain should be
level operations master roles for the forest root domain should be
gured as per the design. By default, the first domain controller installed in the forest root
installed in the forest root
configured as per the design. By default, the first
. These can be further configured65 to meet the
domain is assigned all operations master roles. These can be further configured
domain is assigned all operations master roles
rred to alternative domain
requirements of the organisation if it is necessary or can be transferred to alternative domain
requirements of the organisation if it is necessary or can be transfe
controllers to balance the performance load66.
controllers to balance the performance

Raise the Functional Level
8.2.2  Raise the Functional Level

When deploying the first domain controller
at the Windows 2000 forest functional level, and the domain operates by default at the Windows
at the Windows 2000 forest functional level, and the domain operates by default at the Windows
at the Windows 2000 forest functional level, and the domain operates by default at the Windows
2000 mixed functional level.

in the forest root domain, the forest operates by default
domain controller in the forest root domain, the forest operates by default

Recommendations
(cid:1)  Raise the forest functional level to Windows Server 2003

. Provided there are no
Raise the forest functional level to Windows Server 2003 native mode. Provided there are no
application issues, raise the forest functional level to Windows Server 2008 R2
application issues, raise the forest functional level to Windows Server 2008 R2

(cid:1)  Use AD DS Domains and Trusts to enable the Windows Server

functional levels
Domains and Trusts to enable the Windows Server forest functional levels

Deploy Windows Server 2003 Regional Domains (Optional)
8.2.3  Deploy Windows Server 2003 Regional Domains (Optional)
Deploy Windows Server 2003 Regional Domains (Optional)

regional domains involves creating new geographically based
loying Windows Server 2008 R2 regional domains involves creating new geographically based
Deploying Windows Server 200
child domains under the forest root domain. This is only necessary if the Build phase has designed
child domains under the forest root domain. This is only necessary if the Build phase has designed
child domains under the forest root domain. This is only necessary if the Build phase has designed
a multiple domain Active Directory forest.
a multiple domain Active Directory forest.

n any regional domains should be deployed following the sequence
Windows Server 2008 R2 in any regional domains should be deployed following the sequence
n any regional domains should be deployed following the sequence
level steps required are listed below:
for a forest root domain. The high-level steps required are listed below:
outlined in section 8.2.2 for a forest root domain. The high

(cid:1)  Reviewing the regional domain design
Reviewing the regional domain design

(cid:1)  Delegating the DNS domain for the new regional domain
Delegating the DNS domain for the new regional domain

(cid:1)  Deploying the first domain controller

domain controller in a new regional domain

(cid:1)  Deploying additional domain controller

domain controllers in a new regional domain

(cid:1)  Reconfiguring the DNS service
Reconfiguring the DNS service

(cid:1)  Configuring operations master roles
Configuring operations master roles

Recommendation

No additional information is provided on this process as a single domain forest is recommended for each
No additional information is provided on this process as a single domain forest is recommended for each
No additional information is provided on this process as a single domain forest is recommended for each
Healthcare organisation.

Deploy a Domain Controller
8.3  Deploy a Domain Controller

The Windows Server 2008 R2
8 R2 Build {R4} requires reconfiguring into the domain controller
. This is performed by running the inbuilt DCPromo.exe tool to start the AD DS
. This is performed by running the inbuilt DCPromo.exe tool to start the
host AD DS. This is performed by running the inbuilt DCPromo.exe tool to start the
Installation Wizard. The AD DS

Installation Wizard can be used for the following three methods:
DS Installation Wizard can be used for the following three methods:

domain controller role to

Configure the Operations Master roles {R104}:

65 Configure the Operations Master roles {
us/library/cc732963(WS.10).aspx
http://technet.microsoft.com/en-us/library/cc732963(WS.10).aspx

66 Transfer operations master roles {R70
http://technet2.microsoft.com/windowsserver/en/library/5da4f9f2-7f90-417a-9d11-5ee1db75bfb61033.mspx
http://technet2.microsoft.com/windowsserver/en/library/5da4f9f2
us/library/cc816946(WS.10).aspx
http://technet.microsoft.com/en-us/library/cc816946(WS.10).aspx

5ee1db75bfb61033.mspx and:

R70}:

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 80

Prepared by Microsoft

(cid:1)  AD DS Installation Wizard from running DCPromo
the ‘Configure Your Server Wizard’ menu option
the ‘Configure Your Server Wizard’ menu option

from the command line, or by selecting
Installation Wizard from running DCPromo from the command line, or by selecting

(cid:1)  Automated install using an unattended setup script ca

lled an answer file
Automated install using an unattended setup script called an answer file

(cid:1)  Installing from media for additional

Installing from media for additional domain controllers

Recommendation

It is recommended that the use of the unattended answer file is used to deploy a domain controller
It is recommended that the use of the unattended answer file is used to deploy a
primarily for two reasons:

domain controller. This is

1.  The answer files can become

part of the design documentation which can be referenced in the future.
The answer files can become part of the design documentation which can be referenced in the future.

2.  Automating the install removes the element of human error when completing the
Automating the install removes the element of human error when completing the AD DS Installation
Automating the install removes the element of human error when completing the
Wizard manually.

Installation Wizard
8.3.1  AD DS Installation Wizard

To configure a server as a domain controller
either from a command line or by selecting ‘Configure your server wizard’ from the menu option.
either from a command line or by selecting ‘Configure your server wizard’ from the menu option.
either from a command line or by selecting ‘Configure your server wizard’ from the menu option.

on the server by running DCPromo.exe
domain controller, install AD DS on the server by running DCPromo.exe

Installation Wizard:
It is possible to create two types of domain controllers by using the AD DS Installation Wizard:
It is possible to create two types of

(cid:1)  Domain controller for a new domain
for a new domain

(cid:1)  Additional domain controller

domain controller for an existing domain

When creating a domain controller

for a new domain, the domain can be one of the following types:
domain controller for a new domain, the domain can be one of the following types:

(cid:1)  Domain in a new forest

Domain in a new forest – Select this domain type if creating the first domain in
organisation, or if wanting the new domain to be independent of any existing forests. This
organisation, or if wanting the new domain to be independent of any existing forests. This
organisation, or if wanting the new domain to be independent of any existing forests. This
first domain is the forest root domain
first domain is the forest root domain

Select this domain type if creating the first domain in the

(cid:1)  Child domain in an existing domain tree
Select this domain type if wanting the new
Child domain in an existing domain tree – Select this domain type if wanting the new
domain to be a child of an existing domain
domain to be a child of an existing d

(cid:1)  Additional domain tree in an existing forest

Select this domain type if wanting to create a
Additional domain tree in an existing forest – Select this domain type if wanting to create a
domain tree that is separate from any existing domain trees
domain tree that is separate from any existing domain trees

Automated Scripted Installations for Domain Controllers
8.3.2  Automated Scripted Installations for Domain Controllers
Automated Scripted Installations for Domain Controllers

It is possible to run the AD DS
Installation Wizard without having to be present to answer the
DS Installation Wizard without having to be present to answer the
questions by using an ‘answer file’. An answer file is a text file that can be populated with the
questions by using an ‘answer file’. An answer file is a text file that can be populated with the
questions by using an ‘answer file’. An answer file is a text file that can be populated with the
parameters that the wizard needs to install AD DS.
parameters that the wizard needs to install

An answer file can be used to install Windows Server 2008 R2, and can also include the options
, and can also include the options
An answer file can be used to install Windo
necessary to subsequently install AD DS. Alternatively, it is possible to create an answer file that
. Alternatively, it is possible to create an answer file that
necessary to subsequently install
contains only the options necessary for installing AD DS. These parameters67 include the
include the domain
contains only the options necessary for installing
controller type (additional domain controller
domain controller for a
new domain), the configuration of the domain that is being created (new forest, new tree root, or
new domain), the configuration of the domain that is being created (new forest, new tree root, or
new domain), the configuration of the domain that is being created (new forest, new tree root, or
new child) and AD DS forest and domain functional levels.
onal switches have been added
forest and domain functional levels. Additional switches have been added
through Windows Server 2008 and Windows Server 2008 R2 to support the unattended installation
through Windows Server 2008 and Windows Server 2008 R2 to support the unattended installation
through Windows Server 2008 and Windows Server 2008 R2 to support the unattended installation
of the newer services and features68.
of the newer services and features

domain controller for an existing domain or a new domain controller

Once the answer file has been created, the file name can be appended to the /answer
Once the answer file has been created, the file name can be appended to the
command from the command line. For example:
running the DCPromo command from the command line. For example:

/answer switch when

67 How to use unattended mode to install and remove Active Directory Domain Services on Windows Server 2008
How to use unattended mode to install and remove Active Directory Domain Services on Windows Server 2008-based
How to use unattended mode to install and remove Active Directory Domain Services on Windows Server 2008
domain controllers {R68}:
http://support.microsoft.com/kb/947034
http://support.microsoft.com/kb/947034

Appendix of Unattended Installation Parameters {R105}:

68 Appendix of Unattended Installation Parameters
us/library/cc732086(WS.10).aspx
http://technet.microsoft.com/en-us/library/cc732086(WS.10).aspx

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 81

C:\Windows> dcpromo /answer:dcinstall.txt

dcpromo /answer:dcinstall.txt

Prepared by Microsoft

. The answers provided in this example would install a domain controller

The following is an example content of an unattended answer file for automating the installation of
The following is an example content of an unattended answer file for automating the installation of
The following is an example content of an unattended answer file for automating the installation of
AD DS. The answers provided in this example would install a
domain controller in a new domain in
a new forest. The contents of this file would need to change appropriately for subsequent
a new forest. The contents of this file would need to change appropriately for subsequent
a new forest. The contents of this file would need to change appropriately for subsequent
installations of domain controller
ReplicaOrNewDomain parameter.
ReplicaOrNewDomain parameter.

eOrJoin and Replica for the
domain controllers, such as specifying Join for the CreateOrJoin and Replica for the

[DCInstall]

AutoConfigDNS = No

CreateOrJoin = Create

CriticalReplilcationOnly = No
CriticalReplilcationOnly = No

DatabasePath = %SYSTEMROOT%\NTDS
DatabasePath = %SYSTEMROOT%

DisableCancelForDnsInstall = Yes
DisableCancelForDnsInstall = Yes

DNSOnNetwork = Yes

DomainNetBiosName = HEALTHORG

HEALTHORG

LogPath = %SYSTEMROOT%\NTDS

NTDS

NewDomain = Forest

NewDomainDNSName = healthorg.org.com

healthorg.org.com

Password = Qw3ertyu!0P

RebootOnSuccess = Yes

ReplicaOrNewDomain = Domain
ReplicaOrNewDomain = Domain

SafeModeAdminPassword = P0!uytr3wQ
SafeModeAdminPassword = P0!uytr3wQ

SetForestVersion = Yes

SysVolPath = %SYSTEMROOT%\SYSVOL
SysVolPath = %SYSTEMROOT%

TreeOrChild = Tree

UserDomain = HEALTHORGDEMODC1

DEMODC1

UserName = Administrator

Note

The example answer file above has been given purely for demonstration purposes and is not a
The example answer file above has been given purely for demonstration purposes and is not a
The example answer file above has been given purely for demonstration purposes and is not a
recommendation of the options that should be implemented. However, the example may act as an aid
recommendation of the options that should be implemented. However, the example may act as an
recommendation of the options that should be implemented. However, the example may act as an
when structuring an answer file that will fit the requirements and design decisions of the Healthcare
when structuring an answer file that will fit the requirements and design decisions of the
when structuring an answer file that will fit the requirements and design decisions of the
. Also, the example password given in the example is purely for demonstration purposes of
organisation. Also, the example password given in the example is purely for demonstration purposes of
. Also, the example password given in the example is purely for demonstration purposes of
rly complex password should be chosen.
how a complex password should be used, a similarly complex password should be chosen.
how a complex password should be used, a simila

Important

Once the answer file has been used by the DCPromo tool, any passwords contained within the file are
Once the answer file has been used by the DCPromo tool, any passwords contained within the file are
Once the answer file has been used by the DCPromo tool, any passwords contained within the file are
removed. Therefore, during testing of the answer file, if it is necessary to run the DCPromo
removed. Therefore, during testing of the answer file, if it is necessary to run the DCPromo tool multiple
removed. Therefore, during testing of the answer file, if it is necessary to run the DCPromo
times with the same answer file, the password must be entered before it can be run, otherwise the AD DS
times with the same answer file, the password must be entered before it can be run, otherwise the
times with the same answer file, the password must be entered before it can be run, otherwise the
Installation Wizard will prompt for this information.
Installation Wizard will prompt for this information.

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 82

8.3.3

Install an Additional Domain Controller Through Backup Media
Install an Additional Domain Controller Through Backup Media
Install an Additional Domain Controller Through Backup Media

Prepared by Microsoft

on member servers using a
8 R2 family, it is possible to install AD DS on member servers using a

. This backup can be stored on any
a feature known as Install From Media (IFM). This backup can be stored on any

With the Windows Server 2008 R2
running Windows
restored backup of system state data taken from an existing domain controller running Windows
restored backup of system state data taken from an existing
Server 2008 R2 – a feature known as Install From Media (IFM)
backup media (for example, tape, CD, or DVD) or a shared network resource. By using restored
backup media (for example, tape, CD, or DVD) or a shared network resource. By using restored
backup media (for example, tape, CD, or DVD) or a shared network resource. By using restored
, it is possible to greatly reduce the network
backup files to create an additional domain controller, it is possible to greatly reduce the network
backup files to create an additional
bandwidth used when installing
needed to replicate all new objects and recent changes for existing objects to the new domain
needed to replicate all new objects and recent changes for existing objects to the new
needed to replicate all new objects and recent changes for existing objects to the new
This option is suitable for either of the following situations:
controller. This option is suitable for either of the following situations:

over a shared network resource. Network connectivity is still
ing AD DS over a shared network resource. Network connectivity is still

(cid:1)  Where there is a poor WAN link between the site where the

a poor WAN link between the site where the domain controller

domain controller is being

installed and the nearest site that hosts a domain controller which will be used for
installed and the nearest site that hosts a domain controller which will be used for
installed and the nearest site that hosts a domain controller which will be used for
performing the initial replicat

replication of the directory
(cid:1)  Where the AD DS is so large that the time taken

to promote the new domain controller will
is so large that the time taken to promote the new domain controller will

be excessive. Typically this would be a case where the existing AD DS
be excessive. Typically this would be a case where the existing

 store exceeds 24GB

It is unlikely that any healthcare organisation
leteness.
documented here for completeness.

healthcare organisation will use this method for installing AD

AD DS but it is

Recommendation

a healthcare organisation wish to use backup media to install additional domain controller

Should a healthcare organisation
recommended that the unattended answer file is still used and that the ReplicateFromMedia
recommended that the unattended answer file is still used and that the
ReplicationSourcePath parameter

parameters are specified.

ReplicateFromMedia and

domain controllers, it is

Full details on this option are available within the Microsoft Knowledge Base article: How to use the
Full details on this option are available within the Microsoft Knowledge Base article:
Full details on this option are available within the Microsoft Knowledge Base article:
based domain controllers69 which can
Install from Media feature to promote Windows Server 2003
Install from Media feature to promote Windows Server 2003-based domain controllers
008 documentation for installing domain controllers
be used to supplement the Windows Server 2008 documentation for installing domain controllers
be used to supplement the Windows Server 2
and RODCs with IFM71.
via IFM70 and RODCs with IFM

8.4  Test the Installation of

Test the Installation of AD DS

installation on the first
As a minimum, the following tests should be conducted to verify the AD DS installation on the first
As a minimum, the following tests should be conducted to verify the
root domain controller:

(cid:1)  Review the Windows Server 200

Server 2008 R2 event log and resolve any errors

(cid:1)  At the command line, run Dcdiag.exe and Netdiag.exe, and resolve any errors that are
At the command line, run Dcdiag.exe and Netdiag.exe, and resolve any errors that are
At the command line, run Dcdiag.exe and Netdiag.exe, and resolve any errors that are
reported

(cid:1)  Run Task Manager and verify that the processor and memory system resources are within
Run Task Manager and verify that the processor and memory system resources are within
Run Task Manager and verify that the processor and memory system resources are within
acceptable limits

How to use the Install from Media feature to promote Windows Server 2003-based domain controllers

69 How to use the Install from Media feature to promote Windows Server 2003
http://support.microsoft.com/kb/311078.
http://support.microsoft.com/kb/311078

based domain controllers {R69}:

Installing an Additional Domain Controller by Using IFM {R106}:

70 Installing an Additional Domain Controller by Using IFM
us/library/cc816722(WS.10).aspx
http://technet.microsoft.com/en-us/library/cc816722(WS.10).aspx
71 Installing AD DS from Media {R107
R107}:
us/library/cc770654(WS.10).aspx
http://technet.microsoft.com/en-us/library/cc770654(WS.10).aspx

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 83

Prepared by Microsoft

(cid:1)  Open the DNS snap-in, navigate to
_msdcs.forest_root_domain_name
the forest_root_domain_name
were created, where forest_root_domain_name

were created. Expand
forest_root_domain_name and forest_root_domain_name were created. Expand

forest_root_domain_name node and verify that DomainDnsZones and

and ForestDnsZones

, and verify that the zones
in, navigate to Forward Lookup Zones, and verify that the zones

is the name of the forest root
forest_root_domain_name is the name of the forest root

(cid:1)  Consideration should also be given to running the Active Directory Best Practice Analyzer
Consideration should also be given to running the Active Directory Best Practice Analyzer
Consideration should also be given to running the Active Directory Best Practice Analyzer
once the forest has been configured to verify that there are no minor configuration settings
once the forest has been configured to verify that there are no minor configuration settings
once the forest has been configured to verify that there are no minor configuration settings
either not been set or have been set sub optimally
that have either not been set or have been set sub optimally

On the second domain controller
validation check:

installed in the forest root domain perform the following additional
domain controller installed in the forest root domain perform the following additional

(cid:1)  Use the same tests as shown in the procedure for the first

Use the same tests as shown in the procedure for the first domain controller
DomainDnsZones and ForestDnsZones were created, use the
verifying that DomainDnsZones
DomainDnsZones application
command to verify that the ForestDnsZones and DomainDnsZones
/showreps command to verify that the
directory partitions have been replicated successfully.
to verify that the domain
directory partitions have been replicated successfully. Use dnscmd to verify
controller has been enlisted in the replication scope of the DNS Application Partitions. Use
controller has been enlisted in the replication scope of the DNS Application Partitions.
controller has been enlisted in the replication scope of the DNS Application Partitions.
in to verify that DNS server recursive name resolution is configured
the DNS snap-in to verify that DNS server recursive name resolution is configured
in to verify that DNS server recursive name resolution is configured
according to the method used by the Healthcare organisation.
according to the method used by the

were created, use the repadmin

domain controller, but instead of

DS
8.5  Configure AD DS

service has been installed and verified, it is necessary to review the AD DS
service has been installed and verified, it is necessary to review the
Once the AD DS service has been installed and verified, it is necessary to review the
design and configure any outstanding settings. This should include:
design and configure any outstanding settings. This should include:

(cid:1)  Configuring domain controller

domain controllers as GC Servers

(cid:1)  Creating the OU structure
Creating the OU structure

(cid:1)  Creating any remaining sites, associating sites to subnets and assigning sites to site links
remaining sites, associating sites to subnets and assigning sites to site links
remaining sites, associating sites to subnets and assigning sites to site links

(cid:1)  Applying security policies, such as the additional configuration required in the DDP and
Applying security policies, such as the additional configuration required in the DDP and
Applying security policies, such as the additional configuration required in the DDP and
DDCP

(cid:1)  Creating and deploying any new GPOs that supplement the default GPOs and are requ
Creating and deploying any new GPOs that supplement the default GPOs and are required
Creating and deploying any new GPOs that supplement the default GPOs and are requ

(cid:1)  Creating service and data administrative accounts
Creating service and data administrative accounts

(cid:1)  Delegating the appropriate administration rights to the new administrative accounts
Delegating the appropriate administration rights to the new administrative accounts
Delegating the appropriate administration rights to the new administrative accounts

(cid:1)  Applying the delegation of the administration model to the OU structure
Applying the delegation of the administration model to the OU structure

(cid:1)  Creating user accounts
Creating user accounts

(cid:1)  Creating group account

Creating group accounts

(cid:1)  Nesting groups appropriately
Nesting groups appropriately

(cid:1)  Assigning resource access permissions to groups
Assigning resource access permissions to groups

(cid:1)  Establish any required Active Directory trusts to external domains or forests
Establish any required Active Directory trusts to external domains or forests
Establish any required Active Directory trusts to external domains or forests

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 84

Prepared by Microsoft

9  OPERATE

During the Operate phase, solution components are proactively managed as an end-to-end IT
During the Operate phase, solution components are proactively managed as an end
During the Operate phase, solution components are proactively managed as an end
ervice to ensure the service provides the required levels of solution functionality, reliability,
Service to ensure the service provides the required levels of solution functionality, reliability,
ervice to ensure the service provides the required levels of solution functionality, reliability,
availability, supportability and manageability. Successfully bringing a well-designed service into a
designed service into a
availability, supportability and manageability. Successfully bringing a well
production environment takes efficient planning to balanc
e speed, cost and safety, while ensuring
production environment takes efficient planning to balance speed, cost and safety, while ensuring
minimum disruption to operations and supporting the 'business as usual' delivery of the
minimum disruption to operations and supporting the 'business as usual' delivery of the
minimum disruption to operations and supporting the 'business as usual' delivery of the
organisation's IT requirements.
organisation's IT requirements.

This section is the starting point for the operations of the Windows Server 200
This section is the starting point for the operations of the Windows Server 2008 R2
designed to provide a significant head start in formulating the necessary and appropriate product
designed to provide a significant head start in formulating the necessary and appropriate product
designed to provide a significant head start in formulating the necessary and appropriate product
specific solution operations guidance. The
operations materials for the creation of healthcare-specific solution operations guidance. The
operations materials for the creation of
will depend on the scale of the implementation within
operational infrastructure to support AD DS will depend on the scale of the implementation within
operational infrastructure to support
. Small infrastructures will benefit from the reduction of administration
. Small infrastructures will benefit from the reduction of administration
each Healthcare organisation. Small infrastructures will benefit from the reduction of administration
tools, scripting repetitive tasks and the implementation of services,
through the use of the built in tools, scripting repetitive tasks and the implementation of service
tools, scripting repetitive tasks and the implementation of service
will also benefit from
such as Group Policy and RIS. Medium and large healthcare organisations will also benefit from
such as Group Policy and RIS. Medium and large
these services, as well as receiving benefit from the implementation of enterprise software
these services, as well as receiving benefit from the implementation of enterprise software
these services, as well as receiving benefit from the implementation of enterprise software
management and operations
distribution solutions, and will need to be more aware of capacity management and operations
distribution solutions, and will need to be more aware of capacity
management.

8 R2 AD DS. It is

Through a combination of these technologies, public best practices guidance, and training
Through a combination of these technologies, public best practices guidance, and training
Through a combination of these technologies, public best practices guidance, and training
opportunities, the healthcare organisations
while lowering the TCO.

can improve service, reliability, availability, and security
healthcare organisations can improve service, reliability, availability, and security

level checklist, illustrating the critical components for which an IT
Figure 16 acts as a high-level checklist, illustrating the critical components for which an IT
level checklist, illustrating the critical components for which an IT
infrastructure:
Professional is responsible for ensuring in a managed and operational AD DS infrastructure:
Professional is responsible for ensuring in a managed

Figure 16: Sequence for Operating AD DS

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 85

Prepared by Microsoft

9.1  Ensure a Managed

Ensure a Managed AD DS Infrastructure

Being more proactive with the administration and management of the network circumvents potential
Being more proactive with the administration and management of the network circumvents potential
Being more proactive with the administration and management of the network circumvents potential
and network failure problems that impact employee productivity and potential data
security risks and network failure problems that impact employee productivity and potential data
and network failure problems that impact employee productivity and potential data
loss. Windows Server 2008 R2
administration and management, through the use of the Delegation of Control (DoC) wizard72, so
administration and management, through the use of the Delegation of Control (DoC) wizard
administration and management, through the use of the Delegation of Control (DoC) wizard
that a healthcare organisation
can assign common tasks to department managers or other
 can assign common tasks to department managers or other
personnel for functions like password resets, assigning department level security, reset print
personnel for functions like password resets, assigning department level security, reset print
personnel for functions like password resets, assigning department level security, reset print
queues, or scan for security vulnerabilities.
queues, or scan for security vulnerabilities.

provide distributed and delegated levels of
8 R2 and AD DS provide distributed and delegated levels of

ation tasks on an ‘as needed’ basis, the medium and large healthcare
ation tasks on an ‘as needed’ basis, the medium and large
By distributing administration tasks on an ‘as needed’ basis, the medium and large
can be more proactive to potential problems, and can quickly respond to system
organisations can be more proactive to potential problems, and can quickly respond to system
can be more proactive to potential problems, and can quickly respond to system
problems, whilst achieving a lower TCO.
problems, whilst achieving a lower TCO.

Recommendations

Where a healthcare organisation
outine administrative tasks such as
a healthcare organisation has enough staff to support it, routine administrative tasks such as
password resets, should be delegated to ease the burden on IT support staff, so that they are more often
password resets, should be delegated to ease the burden on IT support staff, so that they are more often
password resets, should be delegated to ease the burden on IT support staff, so that they are more often
available for proactive system monitoring.
available for proactive system monitoring.

se of the core support and administration tools to allow them to
All staff should be suitably trained in the use of the core support and administration tools to allow them to
All staff should be suitably trained in the u
effectively and competently manage AD DS.
effectively and competently manage

9.1.1

People and Process
People and Process

Public guidelines are available to help effectively design, develop, deploy, operate, and support
Public guidelines are available to help effectively design, develop, deploy, operate, and support
Public guidelines are available to help effectively design, develop, deploy, operate, and support
hnologies. These guidelines are organised into two integrated
solutions built on Microsoft technologies. These guidelines are organised into two integrated
solutions built on Microsoft tec
frameworks, the Microsoft Operations Framework (MOF)73 and Microsoft Solutions Framework
and Microsoft Solutions Framework
frameworks, the Microsoft Operations Framework (MOF)
(MSF)74, which include white papers, operations guides, assessment tools, best practices, case
, which include white papers, operations guides, assessment tools, best practices, case
, which include white papers, operations guides, assessment tools, best practices, case
templates, support tools and services.
studies, templates, support tools and services.

MOF provides the regime that addresses the people, process, technology, and management issues
MOF provides the regime that addresses the people, process, technology, and management issues
MOF provides the regime that addresses the people, process, technology, and management issues
pertaining to operating complex, distributed, heterogeneous IT environments.
pertaining to operating complex, distributed, heterogeneous IT environments.

Recommendation

opriate processes are in place to help manage the IT environment within the
It is vital to ensure that appropriate processes are in place to help manage the IT environment within the
opriate processes are in place to help manage the IT environment within the
Healthcare organisation.

Automated Change and Configuration Management
9.1.2  Automated Change and Configuration Management
Automated Change and Configuration Management

For medium to large healthcare organisations
into the environment, it is important to consider the following points with
Configuration Manager into the environment, it is important to consider the following points with
into the environment, it is important to consider the following points with
regard to an AD DS design:

healthcare organisations, looking to incorporate Microsoft System

, looking to incorporate Microsoft System Center

(cid:1)  The requirements for software distribution in

site design should be considered when
The requirements for software distribution in AD DS site design should be considered when
deciding to allocate subnets to sites
deciding to allocate subnets to sites

(cid:1)  The design of Active Directory OUs, distribution lists, and security groups need
e Directory OUs, distribution lists, and security groups need
e Directory OUs, distribution lists, and security groups need
software distribution
consideration when integrated with Configuration Manager software distribution
consideration when integrated with

Active Directory delegation tools (Windows Server 2003) {R71}:

72 Active Directory delegation tools (Windows Server 2003)
us/library/cc756087(WS.10).aspx and for Windows Server 2008
http://technet.microsoft.com/en-us/library/cc756087(WS.10).aspx
us/library/dd145344.aspx
http://technet.microsoft.com/en-us/library/dd145344.aspx

Microsoft Operations Framework 4.0 {R72}:

73 Microsoft Operations Framework 4.0
http://www.microsoft.com/technet/solutionaccelerators/cits/mo/mof/mofeo.mspx
http://www.microsoft.com/technet/solutionaccelerators/cits/mo/mof/mofeo.mspx

74 Microsoft Solutions Framework Core Whitepapers
http://www.microsoft.com/downloads/details.aspx?FamilyID=e481cb0b

Framework Core Whitepapers {R73}:

fc886956790e&DisplayLang=en
/www.microsoft.com/downloads/details.aspx?FamilyID=e481cb0b-ac05-42a6-bab8-fc886956790e&DisplayLang=en

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 86

Prepared by Microsoft

System Center Configuration Manager (SCCM) is not

ensures the manageability of
amount that the Healthcare organisation ensures the manageability of

For smaller scale deployments, where System Center Configuration Manager (SCCM)
For smaller scale deployments, where
appropriate, it is still paramount that the
system patches and security updates. In preparing for simple automated patch management
system patches and security updates. In preparing for simple automated patch management
system patches and security updates. In preparing for simple automated patch management
Update Services (WSUS)75 in conjunction with Group Policy can be used
in conjunction with Group Policy can be used
services, Windows Server Update Services (WSUS)
lp implement a more secure, robust infrastructure. The patch management process should be
to help implement a more secure, robust infrastructure. The patch management process should be
lp implement a more secure, robust infrastructure. The patch management process should be
structured to ensure regular review of vulnerability assessment across the infrastructure, thus
structured to ensure regular review of vulnerability assessment across the infrastructure, thus
structured to ensure regular review of vulnerability assessment across the infrastructure, thus
reducing the exposure of unpatched systems.
reducing the exposure of unpatched systems.

The Microsoft Baseline Security Analyser (MBSA)
detect common security misconfigurations and missing security updates on computer systems in
detect common security misconfigurations and missing security updates on computer systems in
detect common security misconfigurations and missing security updates on computer systems in
small and medium sized environments. It is designed to determine the security state
small and medium sized environments. It is designed to determine the security state of computers
small and medium sized environments. It is designed to determine the security state
in accordance with Microsoft security recommendations and offers specific remediation guidance.
in accordance with Microsoft security recommendations and offers specific remediation guidance.
in accordance with Microsoft security recommendations and offers specific remediation guidance.

urity Analyser (MBSA)76 is a free tool from Microsoft that can be used to
is a free tool from Microsoft that can be used to

Recommendation

should have the ability to centrally deploy and manage the operating
Healthcare organisation should have the ability to centrally deploy and manage the operating
Each Healthcare organisation
and updates. Ideally an audit trail of what patches are deployed
system, security and application patches and updates. Ideally an audit trail of what patches are deployed
system, security and application patches
to what machines should be maintained.
to what machines should be maintained.

9.1.3

Processes and Procedures for Improving Service Management
Processes and Procedures for Improving Service Management
Processes and Procedures for Improving Service Management

Microsoft has published product operations guides, available on the Internet, that describe
Microsoft has published product operations guides, available on the Internet, that describe the
Microsoft has published product operations guides, available on the Internet, that describe
processes and procedures required for improving the management of many of its core products.
processes and procedures required for improving the management of many of its core products.
processes and procedures required for improving the management of many of its core products.
The following list highlights the essential guidance for an AD DS infrastructure:
The following list highlights the essential guidance for an

(cid:1)  Active Directory Product Operations Guide

Active Directory Product Operations Guide77

(cid:1)  DNS Service Product Operations

DNS Service Product Operations Guide78

(cid:1)  WINS Service Product Operations Guide

WINS Service Product Operations Guide79

These guides contain tables that provide a quick reference for those product maintenance
These guides contain tables that provide a quick reference for those product maintenance
These guides contain tables that provide a quick reference for those product maintenance
processes that need to be performed on a regular basis. These tables represent a summary of the
processes that need to be performed on a regular basis. These tables represent a summary of the
processes that need to be performed on a regular basis. These tables represent a summary of the
processes, and their subordinate tasks and procedures, described in more detail in subsequent
bordinate tasks and procedures, described in more detail in subsequent
bordinate tasks and procedures, described in more detail in subsequent
chapters of the guides. They are limited to those processes required for maintaining the product.
chapters of the guides. They are limited to those processes required for maintaining the product.
chapters of the guides. They are limited to those processes required for maintaining the product.

Microsoft Windows Server Update Services {R74}:

75 Microsoft Windows Server Update Services
http://www.microsoft.com/windowsserversystem/updateservices/default.mspx
http://www.microsoft.com/windowsserversystem/updateservices/default.mspx

Microsoft Baseline Security Analyser {R75}:

76 Microsoft Baseline Security Analyser
http://www.microsoft.com/technet/security/tools/mbsahome.mspx
 http://www.microsoft.com/technet/security/tools/mbsahome.mspx

Active Directory Product Operations Guide TechNet article {R76}:

77 Active Directory Product Operations Guide TechN
solutions/cits/mo/winsrvmg/adpog/adpog1.mspx
http://www.microsoft.com/technet/itsolutions/cits/mo/winsrvmg/adpog/adpog1.mspx

DNS Product Operations Guide TechNet article {R77}:

78 DNS Product Operations Guide TechNet article
http://www.microsoft.com/technet/itsolutions/cits/mo/winsrvmg/dnspog/dnspog1.mspx
 http://www.microsoft.com/technet/itsolutions/cits/mo/winsrvmg/dnspog/dnspog1.mspx

79 WINS Service Product Operations Guide TechNet article
http://www.microsoft.com/technet/itsolutions/cits/mo/winsrvmg/winspog/winspog1.mspx
 http://www.microsoft.com/technet/itsolutions/cits/mo/winsrvmg/winspog/winspog1.mspx

Product Operations Guide TechNet article {R78}:

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 87

Prepared by Microsoft

9.2  Ensure an Operational

Ensure an Operational AD DS Infrastructure

s a key aspect of the operational manageability of each
The ability to monitor the health of AD DS is a key aspect of the operational manageability of each
The ability to monitor the health of
Healthcare organisation. Proactively monitoring the distributed
and the services that it
. Proactively monitoring the distributed AD DS and the services that it
depends on is critical to maintain consistent directory data and a consistent level of IT service
depends on is critical to maintain consistent directory data and a consistent level of IT service
depends on is critical to maintain consistent directory data and a consistent level of IT service
throughout the forest80. Monitoring
Monitoring AD DS assures administrators that:

(cid:1)  All necessary services that support

domain controller
All necessary services that support AD DS are running on each domain controller

(cid:1)  Data is consistent across all
end replication completes in
Data is consistent across all domain controller s and end-to-end replication completes in
accordance with Service Level Agreements (SLAs)
accordance with Service

(cid:1)  There are no domain controllers that are consistently failing to replicate and thus in danger
There are no domain controllers that are consistently failing to replicate and thus in danger
There are no domain controllers that are consistently failing to replicate and thus in danger
of becoming orphaned
of becoming orphaned

(cid:1)  Lightweight Directory Access Protocol (LDAP) queries respond quickly
Lightweight Directory Access Protocol (LDAP) queries respond quickly

(cid:1)  Domain controllers do not experience high Centr

al Processing Unit (CPU) usage
s do not experience high Central Processing Unit (CPU) usage

Manual Operational Activities
9.2.1  Manual Operational Activities

that have deployed AD DS with few domains and domain controller
Healthcare organisations that have deployed
that do not require a critical level of service, might only check the
healthcare organisations that do not require a critical level of service, might only check the
that do not require a critical level of service, might only check the
in tools that are provided
domain controller periodically by using the built-in tools that are provided
performance of a single domain controller
8 R2, such as Performance and Reliability Monitor81.
with Windows Server 2008 R2

domain controller s, or

Microsoft has published product operations guides, available on the Internet, that pr
Microsoft has published product operations guides, available on the Internet, that provide
Microsoft has published product operations guides, available on the Internet, that pr
appropriate administration and troubleshooting information for the following products:
appropriate administration and troubleshooting information for the following products:
appropriate administration and troubleshooting information for the following products:

(cid:1)  Windows Server 2008

 Active Directory Operations Guide82

(cid:1)  Windows Server 2008

 DNS Server Operations Guide83

(cid:1)  Windows Server 2008

84
 Group Policy Planning and Deployment  Guide84

Most of the individual routine AD
site, including:

operations tasks are well documented on the Microsoft Web
AD DS operations tasks are well documented on the Microsoft Web

(cid:1)  Routine AD DS tasks detailed

Common
tasks detailed for Windows Server 2003 in the section Common

85. These have not been updated for Windows Server 2008 or
have not been updated for Windows Server 2008 or

Administrative Tasks85
Windows Server 2008 R2. Some of the tasks listed for Server 2003 will transfer over to
Windows Server 2008 R2. Some of the tasks listed for Server 2003 will transfer over to
Windows Server 2008 R2. Some of the tasks listed for Server 2003 will transfer over to
Windows Server 2008 R2. For changes or alternative methods review the Windows Server
Windows Server 2008 R2. For changes or alternative methods review the Windows Server
Windows Server 2008 R2. For changes or alternative methods review the Windows Server
2008 R2 product documentation and the Technet documentation.
2008 R2 product documentation and t

(cid:1)  A list of step-by-step guides

step guides86

Monitoring Domain Controller Performance {R79}:

80 Monitoring Domain Controller Performance
http://technet2.microsoft.com/windowsserver/en/library/c5d72b6f-5974-4263-b29f-2eece0ab44371033.mspx
http://technet2.microsoft.com/windowsserver/en/library/c5d72b6f

2eece0ab44371033.mspx

81 Performance and Reliability Monitor overview
us/library/cc771692(WS.10).aspx
http://technet.microsoft.com/en-us/library/cc771692(WS.10).aspx

Monitor overview {R80}:

82 Active Directory Operations Guide {
us/library/cc816807(WS.10).aspx
 http://technet.microsoft.com/en-us/library/cc816807(WS.10).aspx

{R81}:

83 DNS Server Operations Guide {R82
us/library/cc816603(WS.10).aspx
http://technet.microsoft.com/en-us/library/cc816603(WS.10).aspx

R82}:

84 Group Policy Planning and Deployment
us/library/cc754948(WS.10).aspx
http://technet.microsoft.com/en-us/library/cc754948(WS.10).aspx

Planning and Deployment Guide {R83}:

85 Common Administrative Tasks {R84
ac1c4b2a3f991033.mspx
http://technet2.microsoft.com/windowsserver/en/library/f2d54234-6d65-439b-9d3b-ac1c4b2a3f991033.mspx
http://technet2.microsoft.com/windowsserver/en/library/f2d54234

R84}:

86 Active Directory Step-by-step Guides
gb/windowsserver/2008/default.aspx
http://technet.microsoft.com/en-gb/windowsserver/2008/default.aspx

step Guides {R85}:

Page 88

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Prepared by Microsoft

(cid:1)  Performance tuning for

Performance Tuning Guidelines for
Performance tuning for AD DS, detailed in the paper Performance Tuning Guidelines for
Windows Server 2008 R2
counters for AD DS avail
Reference88.This reference has not been updated yet for Windows Server 2008 or Windows
This reference has not been updated yet for Windows Server 2008 or Windows
This reference has not been updated yet for Windows Server 2008 or Windows
Server 2008 R2.

8 R287 with a comprehensive reference list of the relevant
Windows Server 2003 Performance Counters
available in the paper Windows Server 2003 Performance Counters

with a comprehensive reference list of the relevant performance

Important

is to perform a backup of the service.
The most critical daily operational task to perform on the AD DS is to perform a backup of the service.
The most critical daily operational task to perform on the
is backed up as part of System State, (which includes the database, log files, registry, system boot
AD DS is backed up as part of System State, (which includes the database, log files, registry, system boot
is backed up as part of System State, (which includes the database, log files, registry, system boot
files, and COM+ registration database), and SYSVOL89.
files, and COM+ registration database), and SYSVOL

p and restored as a set. Backup and restore plans
Therefore, it is critical that these volumes be backed up and restored as a set. Backup and restore plans
Therefore, it is critical that these volumes be backed u
help to ensure service continuity in the event of a directory issue
, and provide the facility to recover
help to ensure service continuity in the event of a directory issue, and provide the facility to recover
objects that may have been accidentally deleted. This is less of an issue in Windows Server 2008 R2 with
objects that may have been accidentally deleted. This is less of an issue in Windows Server 2008 R2 w
objects that may have been accidentally deleted. This is less of an issue in Windows Server 2008 R2 w
Recycle Bin feature but still does not undermine the importance of regular and consistent
the AD DS Recycle Bin feature but still does not undermine the importance of regular and consistent
Recycle Bin feature but still does not undermine the importance of regular and consistent
backups.

To help minimise the impact of a disaster, and ensure service continuity, it is important that the
To help minimise the impact of a disaster, and ensure service continuity, it is important that the
To help minimise the impact of a disaster, and ensure service continuity, it is important that the
test environment. This should be performed in
backup is periodically restored into a test environment. This should be performed in
AD DS backup is periodically restored into a
The following document
conjunction with applying the appropriate procedures for AD DS recovery. The following document
conjunction with applying the appropriate procedures for
seful guidance on these procedures:
provides useful guidance on these

(cid:1)  Microsoft whitepaper Windows Server 2008

tory Forest
Windows Server 2008: Planning for Active Directory Forest

Recovery90

Methods to Automate Manual Operational Activities
9.2.2  Methods to Automate Manual Operational Activities
Methods to Automate Manual Operational Activities

It is possible to script and automate many
on AD DS and reduce the TCO of the service. Scripting
and reduce the TCO of the service. Scripting AD DS tasks also reduces the ri
administrative error that can be introduced, such as typing errors. The scripts themselves should be
administrative error that can be introduced, such as typing errors. The scripts themselves should be
administrative error that can be introduced, such as typing errors. The scripts themselves should be
thoroughly tested and verified before being applied to the production environment.
thoroughly tested and verified before being applied to the production environment.
thoroughly tested and verified before being applied to the production environment.

administrative tasks in order to reduce pressure
automate many AD DS administrative tasks in order to reduce pressure

tasks also reduces the risk of

logies and references for example
The following is a list of reusable AD DS script resources, technologies and references for example
The following is a list of reusable
scripts:

(cid:1)  Microsoft Script Center

Microsoft Script Center91

(cid:1)  Sample scripts for Active Directory

Sample scripts for Active Directory92

(cid:1)  Scripts for DNS93

87 Performance Tuning Guidelines for Wind
Performance Tuning Guidelines for Windows Server 2008 R2 {R86}:
http://www.microsoft.com/whdc/system/sysperf/Perf_tun_srv-R2.mspx
http://www.microsoft.com/whdc/system/sysp

88 Windows Server 2003 Performance Counters Reference
Windows Server 2003 Performance Counters Reference {R87}:
09d5ebeb9ef21033.mspx
http://technet2.microsoft.com/WindowsServer/en/Library/3fb01419-b1ab-4f52-a9f8-09d5ebeb9ef21033.mspx
http://technet2.microsoft.com/WindowsServer/en/Library/3fb01419

Active Directory Product Operations Guide, Chapter 3 {R88}:

89 Active Directory Product Operations Guide,
http://www.microsoft.com/technet/itsolutions/cits/mo/winsrvmg/adpog/adpog3.mspx
http://www.microsoft.com/technet/itsolutions/cits/mo/winsrvmg/adpog/adpog3.mspx

Best Practices: Active Directory Forest Recovery whitepaper {R89}:

90 Best Practices: Active Directory Forest Recovery whitepaper
http://www.microsoft.com/downloads/details.aspx?displaylang=en&FamilyID=326c8a7a-dcad-4333
http://www.microsoft.com/downloads/details.aspx?displaylang=en&FamilyID=326c8a7a

4333-9050-a6303ff3155c

91 Microsoft Script Center {R90}:
http://www.microsoft.com/technet/scriptcenter/default.mspx
 http://www.microsoft.com/technet/scriptcenter/default.mspx

92 Script Repository: Active Directory {
 http://gallery.technet.microsoft.com/ScriptCenter/en
http://gallery.technet.microsoft.com/ScriptCenter/en-
us/site/search?f%5B0%5D.Type=RootCategory&f%5B0%5D.Value=activedirectory&f%5B0%5D.Text=Active%20Directory
us/site/search?f%5B0%5D.Type=RootCategory&f%5B0%5D.Value=activedirectory&f%5B0%5D.Text=Active%20Directory
us/site/search?f%5B0%5D.Type=RootCategory&f%5B0%5D.Value=activedirectory&f%5B0%5D.Text=Active%20Directory

{R91}:

93 Script Repository: DNS Server {R92
http://www.microsoft.com/technet/scriptcenter/scripts/network/dns/default.mspx
 http://www.microsoft.com/technet/scriptcenter/scripts/network/dns/default.mspx

R92}:

Page 89

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Prepared by Microsoft

Active Directory Domain Services94 Web page details how to programmatically

The Active Directory Domain Services
of the routine AD DS tasks, such as man

tasks, such as managing users, groups, backing up and restoring

Web page details how to programmatically achieve many
aging users, groups, backing up and restoring AD DS.

One of the most significant additions to Windows Server 2008 R2 is the inclusion of support for
One of the most significant additions to Windows Server 2008 R2 is the inclusion of support for
One of the most significant additions to Windows Server 2008 R2 is the inclusion of support for
administration. Powershell is the powerful new scripting and
Powershell v2.0 for AD DS administration. Powershell is the powerful new scripting and
administration. Powershell is the powerful new scripting and
work for Windows Server and Microsoft Server products going forward95.
work for Windows Server and Microsoft Server products going forward
administration framework for Windows Server and Microsoft Server products going forward
Windows Server 2008 R2 includes over 80 Powershell cmdlets dedicated to automating and
Windows Server 2008 R2 includes over 80 Powershell cmdlets dedicated to automating and
Windows Server 2008 R2 includes over 80 Powershell cmdlets dedicated to automating and
administering AD DS96.

, using both the LDAP Data Interchange Format (LDIF) utility
AD DS, using both the LDAP Data Interchange Format (LDIF) utility

For batch administration of AD
and several sample programs written using the Microsoft Visual Basic Scripting Edition
(ldifde.exe) and several sample programs written using the Microsoft Visual Basic Scripting Edition
and several sample programs written using the Microsoft Visual Basic Scripting Edition
step guide to Active Directory bulk import and
(VBScript) development system, see the Step-by-step guide to Active Directory bulk import and
(VBScript) development system, see the
export97. Note that this document was released for Windows 2000 Server and has not been
Note that this document was released for Windows 2000 Server and has not been
Note that this document was released for Windows 2000 Server and has not been
updated. As such it may contain some outdated material, but it remains a useful resource to a
updated. As such it may contain some outdated material, but it remains a useful resource to a
updated. As such it may contain some outdated material, but it remains a useful resource to a
Windows Server 2008 R2 user.
Windows Server 2008 R2 user.

9.2.3

Products that Automate Operational Activities
Products that Automate Operational Activities

Larger deployments of AD DS
and sites, or that provide a critical service and cannot afford the cost of lost productivity because of
and sites, or that provide a critical service and cannot afford the cost of lost productivity because of
and sites, or that provide a critical service and cannot afford the cost of lost productivity because of
a service outage, should use an enterprise-level monitoring solution.
a service outage, should use an enterprise

domain controllers
 within healthcare organisations that have many domain controllers

Recommendation

’s requirements should be used, but the important
The monitoring solution that best meets the organisation’s requirements should be used, but the important
The monitoring solution that best meets the
are functioning correctly. The chosen
indicators should be monitored to ensure that all aspects of AD DS are functioning correctly. The chosen
indicators should be monitored to ensure that all aspects of
on should be implemented and fully proven in a lab before deploying it in the production
monitoring solution should be implemented and fully proven in a lab before deploying it in the production
on should be implemented and fully proven in a lab before deploying it in the production
environment.

Administrative Tools
9.3  AD DS Administrative Tools

 domain and forest
Administrators can use a number of methods to configure and manage
Administrators can use a number of methods to configure and manage AD DS
contains a rich set of tools and features that can be used
environments. Windows Server 2008 R2 contains a rich set of tools and features that can be used
environments. Windows Server 200
to manage the Windows environment, including
and its associated network services.
to manage the Windows environment, including AD DS and its associated network services.
Microsoft no longer provides separate tools through mechanisms such as the Windows Server
Microsoft no longer provides separate tools through mechanisms such as the Windows Server
Microsoft no longer provides separate tools through mechanisms such as the Windows Server
upport Tools as the most relevant and practical tools have been incorporated into
Resource Kit or Support Tools as the most relevant and practical tools have been incorporated into
upport Tools as the most relevant and practical tools have been incorporated into
the Windows Server Operating system.
the Windows Server Operating system.

94 Using Active Directory Domain Services
gb/library/aa746434.aspx
http://msdn2.microsoft.com/en-gb/library/aa746434.aspx

Domain Services {R93}:

95 Microsoft Powershell {R108}:
us/library/bb978526.aspx
http://technet.microsoft.com/en-us/library/bb978526.aspx

96 Active Directory Module for Windows Powershell {
ctive Directory Module for Windows Powershell {R109}:
us/library/dd378783(WS.10).aspx
http://technet.microsoft.com/en-us/library/dd378783(WS.10).aspx

97 Step-by-Step Guide to Active Directory Bulk Import and Export
us/library/bb727091.aspx
http://technet.microsoft.com/en-us/library/bb727091.aspx

Step Guide to Active Directory Bulk Import and Export {R94}:

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 90

Prepared by Microsoft

product Help include discussions on
A number of sections in the Windows Server 2008 R2 product Help include discussions on
A number of sections in the Windows Server 200
based tools, command line tools, and scripts.
appropriate AD DS graphical user interface (GUI)
below provides references to useful information for those administering AD DS.
below provides references to useful information for those administering
Table 19 below provides references to useful information for those administering
ponding information for Windows Server 2008 R2.
Unfortunately there is no corresponding information for Windows Server 2008 R2.
Unfortunately there is no corres

graphical user interface (GUI) based tools, command line tools,

Administration Area

Internet Reference

Information about the technologies, issues, and methods to
Information about the technologies, issues, and methods to
consider when deciding which tools to use to perform
consider when deciding which tools to use to perform
management tasks.

Windows Server commands, references and tools98
Windows Server commands, references

Background information on the tools that can be installed remotely
Background information on the tools that can be installed remotely
to administer Windows Server 2008 R2.

Windows Server 2008 Remote Server Administration Tools
Windows Server 2008 Remote Server Administration Tools
(RSAT)99

Windows Server 2008 R2
For an overview of the key Windows Server 2008 R2
administration interface , providing more technical details on
providing more technical details on how it
supports and manages the various Windows Server 2008 R2 roles
supports and manages the various Windows Server 2008 R2 roles
and role

Information and a detailed reference about administering Active
Information and a detailed reference about administering Active
Directory with Windows Powershell

TechNet Library: Server Manager100

Active Directory Administration with Windows Powershell101
Active Directory Administration with Windows Powershell

technical reference that details how to use and configure
A technical reference that details how to use and configure
Windows Performance Monitor

Windows Performance Monitor102

A detailed reference of the areas covered and reported on by the
A detailed reference of the areas covered and reported on by the
Best Practices Analyzer for Active Directory Domain Services.
Best Practices Analyzer for Active Directory Domain Services

Directory Administrative Tools Internet References
Table 19: Active Directory Administrative Tools Internet References

Best Practice Analyzer for Active Directory Domain Services103
Best Practice Analyzer for Active Directory Domain Services

us/library/cc731209.aspx
Windows Server 2008 and Windows Server 2008 R2 Server Manager {R98}:

Remote Server Administration Tools {R96}:

98 Windows Server Commands, References and Tools
Windows Server Commands, References and Tools {R95}:
us/library/dd560674(WS.10).aspx
http://technet.microsoft.com/en-us/library/dd560674(WS.10).aspx
99 Remote Server Administration Tools
http://technet.microsoft.com/en-us/library/cc731209.aspx
100 Windows Server 2008 and Windows Server 2008 R2 Server M
us/library/cc770629(WS.10).aspx
http://technet.microsoft.com/en-us/library/cc770629(WS.10).aspx
101 Administration with Windows Powershell
us/library/dd378937(WS.10).aspx
http://technet.microsoft.com/en-us/library/dd378937(WS.10).aspx
102 Windows Performance Monitor {R100
us/library/cc749249.aspx
http://technet.microsoft.com/en-us/library/cc749249.aspx
103 Best Practice Analyzer for Active Directory Domain Services
us/library/dd391875(WS.10).aspx
 http://technet.microsoft.com/en-us/library/dd391875(WS.10).aspx

Administration with Windows Powershell {R99}:

R100}:

Best Practice Analyzer for Active Directory Domain Services {R101}:

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 91

Prepared by Microsoft

APPENDIX A

ESOURCES
SKILLS AND TRAINING RESOURCES
S

The tables in this Appendix provide details of the suggested training and skill assessment
The tables in this Appendix provide details of the suggested training and skill assessment
The tables in this Appendix provide details of the suggested training and skill assessment
resources available. This list is not exhaustive; there are many third
resources available. This list is not exhaustive; there are many third-party provide
The resources listed are those provided by Microsoft.
The resources listed are those provided by Microsoft.

party providers of such skills.

PART I  MICROSOFT

ICROSOFT ACTIVE DIRECTORY

http://www.microsoft.com/activedirectory
For further information on Active Directory, see http://www.microsoft.com/activedirectory
For further information on Active Directory, see

Skill or Technology
Area

Resource Location
Resource Location

Description
Description

Active Directory Design,
including DNS design

http://technet.microsoft.com/en
http://technet.microsoft.com/en-
us/library/cc732058(WS.10).aspx
us/library/cc732058(WS.10).aspx

Links to sections on designing
Links to sections on designing AD DS
components
components

DC capacity planning, site
design and DC placement

Operations Master roles:
placement of role holders,
troubleshooting role holders
and management

As above
As above

As above
As above

OU design

As above
As above

Training and Skill Assessment Resources
Table 20: Microsoft Active Directory 2008 R2 Training and Skill Assessment Resources

As above

As above

As above

PART II GROUP POLICY

OCAL
OLICY, BOTH DOMAIN AND LOCAL

For an overview of Group Policies, see http://www.microsoft.com/grouppolicy.
For an overview of Group Policies, see

Skill or Technology
Area

Controlling operating system
configuration and security

Resource Location
Resource Location

Description
Description

http://www.microsoft.com/grouppolicy
http://www.microsoft.com/grouppolicy

Follow links on the page to resources
Follow links on the page to

Design and implementation for
application deployment

As above
As above

Management using GPMC:
scripting, policy export and
import, backup and restore

Implementation within an
Active Directory OU hierarchy,
and using security groups to
control scope

As above
As above

As above
As above

: Local and Domain Group Policy Training and Skill Assessment Resources
Table 21: Local and Domain Group Policy Training and Skill Assessment Resources

As above

As above

As above

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 92

Prepared by Microsoft

PART III

NETWORK

ETWORK SERVICES

Skill or Technology
Area

Resource Location
Resource Location

Description
Description

DNS

DHCP

WINS

http://technet.microsoft.com/en
http://technet.microsoft.com/en-
us/library/cc732997(WS.10).aspx
us/library/cc732997(WS.10).aspx

http://www.microsoft.com/dns
http://www.microsoft.com/dns

http://technet.microsoft.com/en
http://technet.microsoft.com/en-
us/library/cc896553(WS.10).aspx
us/library/cc896553(WS.10).aspx

http://technet.microsoft.com/en
http://technet.microsoft.com/en-
us/library/cc771750(WS.10).aspx
us/library/cc771750(WS.10).aspx

Network Policy and Access
Technologies

http://technet.microsoft.com/en-
http://technet.microsoft.com/en
us/library/cc754521(WS.10).aspx
us/library/cc754521(WS.10).aspx

DirectAccess

http://technet.microsoft.com/en-
http://technet.microsoft.com/en
us/library/dd630627(WS.10).aspx
us/library/dd630627(WS.10).aspx

: Network Services Training and Skill Assessment Resources
Table 22: Network Services Training and Skill Assessment Resources

The Windows Server 2008 DNS
The Windows Server 200
Website

The Windows Server  DNS
The Windows Server  DNS
technology Website
technology

The Windows Server 200
The Windows Server 2008 DHCP
Technology Website
Technology Website

The Windows Server 2008 WINS
The Windows Server 2008 WINS
technology Website
technology Website

The Windows Server 2008 and
The Windows Server 2008 and
Windows Server 2008 R2 Network
Windows Server 2008 R2 Network
Policy and Access technologies such
Policy and Access technologies such
as Network Access Protection
as Network Access Pro

The Windows Server 2008 R2
The Windows Server 2008 R2
DirectAccess technology Website
DirectAccess technology Website

Active Directory – Design Guide
Active Directory
Prepared by
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010
Last modified on

Page 93

i

t
f
o
s
o
r
c
M
y
b
d
e
r
a
p
e
r
P

I

Y
T
I
X
E
L
P
M
O
C
N
N
G
G
I
I
S
S
E
E
D
Y
R
O
T
C
E
R
D
E
V
I
T
C
A
3
0
0
2
R
E
V
R
E
S
S
S
W
O
D
N
W

I

Site Links

Site A -Site B Compressed, optimized for bandwidth
Site links represent slower (e.g. WAN)
Transport RPC/TCP/IP , SMTP
 Control availability with schedules
Control topology with costs

connections

B
X
I
D
N
E
P
P
A

l

a
i
r
o
t
c
p

i

172.16.65.10
ww.contoso.com
rikam.com
Query for www.fabrikam
Query for www.

(2) Service Ticket
(1) TGT

l

u
f
e
s
u
a

i

s
e
d
v
o
r
p
p
p

l
l
l
l
l
l
i
i
i
t
t
t
s
s
s

t
t
t
u
u
u
b
b
b

2
2
2
R
R
R
8
8
8
0
0
0
0
0
0
2
2
2

r
r
r
e
e
e
v
v
v
r
r
r
e
e
e
S
S
S
s
s
s
w
w
w
o
o
o
d
d
d
n
n
n
W
W
W

i
i
i

r
r
r
o
o
o
8
8
8
0
0
0
0
0
0
2
2
2

r
r
r
e
e
e
v
v
v
r
r
r
e
e
e
S
S
S
s
s
s
w
w
w
o
o
o
d
d
d
n
n
n
W
W
W

i
i
i

r
r
r
o
o
o

f
f
f

d
d
d
e
e
e

t
t
t

a
a
a
d
d
d
p
p
p
u
u
u

n
n
n
e
e
e
e
e
e
b
b
b

t
t
t

o
o
o
n
n
n

s
s
s
a
a
a
h
h
h
t
t
t
I
I
I

.
.
.
e
e
e
c
c
c
n
n
n
e
e
e
r
r
r
e
e
e
f
f
f
e
e
e
r
r
r

r
r
r
o
o
o
f
f
f
d
d
d
e
e
e
d
d
d
u
u
u
c
c
c
n
n
n

l
l
l

i
i
i

s
s
s

i
i
i

m
m
m
a
a
a
r
r
r
g
g
g
a
a
a
d
d
d

i
i
i

i
i
i

s
s
s
h
h
h
T
T
T

.
s
t
n
e
n
o
p
m
o
c
S
D
D
A
y
e
k
e
h

t

i

f
o
w
e
v
r
e
v
o

4
9
e
g
a
P

0
0

.
.

0
0

.
.

0
0
2
2

.
.

i

n
o
s
r
e
V

,
t
f
o
s
o
r
c
M
y
b

i

d
e
r
a
p
e
r
P

0
1
0
2
y
r
a
u
r
b
e
F
6
2

n
o

d
e
i
f
i
d
o
m

t
s
a
L

i

i

e
d
u
G
n
g
s
e
D
–
y
r
o
t
c
e
r
i

D
e
v
i
t
c
A

Prepared by Microsoft

APPENDIX C

AD DS FUNCTIONALITY FEATURES

Feature

Functionality

Multiple selection of user objects

Allows modification of common attributes of multiple user objects at one time.

Drag and drop functionality

Efficient search capabilities

Saved queries

Allows moving of Active Directory objects from container to container by dragging one or
more objects to a location in the domain hierarchy. It is also possible to add objects to
group membership lists by dragging one or more objects (including other group objects)
to the target group.

Search functionality is object-oriented, and provides an efficient search that minimises
network traffic associated with browsing objects.

Allows saving of commonly used search parameters for reuse in Active Directory Users
and Computers.

Active Directory command-line tools

Allows running of new directory service commands for administration scenarios.

InetOrgPerson class

Application directory partitions

The inetOrgPerson class has been added to the base schema as a security principal
and can be used in the same manner as the user class.

Allows configuring of the replication scope for application-specific data among domain
controllers. For example, control the replication scope of DNS zone data stored in
AD DS so that only specific domain controllers in the forest participate in DNS zone
replication.

Ability to add additional domain controllers by
using backup media

Reduces the time it takes to add an additional domain controller in an existing domain by
using backup media.

Universal group membership caching

Prevents the need to locate a GC across a WAN when logging on by storing universal
group membership information on an authenticating domain controller.

Secure LDAP traffic

AD DS administrative tools sign and encrypt all LDAP traffic by default. Signing LDAP
traffic guarantees that the packaged data comes from a known source and that it has not
been tampered with.

Partial synchronisation of the GC

Provides improved replication of the GC when schema changes add attributes to the GC
partial attribute set. Only the new attributes are replicated, not the entire GC.

Active Directory quotas

Quotas can be specified in AD DS to control the number of objects a user, group, or
computer can own in a given directory partition. Members of the Domain Administrators
and Enterprise Administrators groups are exempt from quotas.

Active Directory Recycle Bin

Deleted objects have their attributes retained so that Administrators can restore
accidentally deleted objects without having to resort to the most recent AD DS backup.

Active Directory Best Practice Analyzer

Provides a summary view of where the current AD DS configuration deviates from the
recognised recommended practices for configuring and deploying AD DS.

Fine Grained Password Policies

A mechanism that allows administrators to configure different password policies for
distinct and separate groups of users.

Read Only Domain Controllers

Domain controllers that will not allow changes to be made locally to AD DS and will only
replicate changes in from a Read Write domain controller. Supports separation of
administration as well as providing a way of deploying domain controllers to remote
locations without the risks of compromising the AD DS.

Restartable Active Directory Domain Services  The capability to pause and stop AD DS on a domain controller to carry out updates or

repairs without having to stop or restart the whole server.

Directory Service Auditing

The whole auditing subsystem has been revamped to allow a more granular and
targeted approach to auditing. Introduction of audit subcategories allows for individual
elements of auditing to be enabled or disabled allowing a measured and precise
approach to auditing AD DS activities.

Table 23: Windows Server 2008 R2 AD DS Features

Active Directory – Design Guide
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010

Page 95

Windows Server
Domain Functional
Level

Supported Domain
Controller Operating
Systems

Windows 2000 native

Windows 2000

Windows Server 2003

Windows Server 2003

Windows Server 2003

Windows Server 2003 R2

Windows Server 2008

Windows Server 2008 R2

Windows Server 2008

Windows Server 2008

Windows Server 2008 R2

Prepared by Microsoft

Advanced Features Available at Each Domain Functional
Level`

All default AD DS features, all features from the Windows 2000 mixed
domain functional level and:
(cid:2)  Universal Groups are enabled for both distribution and security groups
(cid:2)  Group conversion is enabled, allowing conversion between security

and distribution groups

(cid:2)  Group nesting is available, allowing nesting of groups within other

groups

(cid:2)  Security identifier (SID) history is available, allowing the migration of

security principals from one domain to another

All default AD DS features, all features from the Windows 2000 native
domain functional level and:
(cid:2)  Supports new functionality of the netdom.exe tool to prepare domain
controllers for rename. It is recommended to rename a domain
controller by using netdom.exe to ensure that all appropriate steps are
taken

(cid:2)  Enables updates to the logon timestamp attribute. The

lastLogonTimestamp attribute is updated with the last logon time of the
user or computer. This attribute is replicated within the domain
(cid:2)  Provides the ability to set the userPassword attribute as the effective

password on inetOrgPerson and user objects

(cid:2)  Provides the ability to redirect the Users and Computers containers in
order to define a new well-known location for user and computer
accounts

(cid:2)  Allows for authorisation manager to store its authorisation policies in

AD DS

(cid:2)  Includes constrained delegation, which allows applications to take

advantage of the secure delegation of user credentials by means of the
Kerberos authentication protocol. Delegation can be configured to be
allowed only to specific destination services

(cid:2)  Supports selective authentication, by which it is possible to specify the
users and groups from a trusted forest who are allowed to authenticate
to resource servers in a trusting forest

All of the default AD DS features, all of the features from the Windows
Server 2003 domain functional level, and the following features are
available:
(cid:2)  Distributed File System (DFS) replication support for the Windows

Server 2003 System Volume (SYSVOL)

(cid:2)  DFS replication support provides more robust and detailed replication

of SYSVOL contents

(cid:2)  Advanced Encryption Standard (AES 128 and AES 256) support for

the Kerberos protocol

(cid:2)  Last Interactive Logon Information:

Last Interactive Logon Information displays the following information:
The time of the last successful interactive logon for a user
The name of the workstation from which the used logged on

(cid:2)  Fine-grained password policies:

Fine-grained password policies make it possible for you to specify
password and account lockout policies for users and global security
groups in a domain

Page 96

Active Directory – Design Guide
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010

Windows Server
Domain Functional
Level

Supported Domain
Controller Operating
Systems

Windows Server 2008 R2  Windows Server 2008 R2

Table 24: Windows Server 2008 R2 Domain Functional Levels

Prepared by Microsoft

Advanced Features Available at Each Domain Functional
Level`

All default AD DS features, all features from the Windows Server 2008
domain functional level, plus the following features:
(cid:2)  Authentication mechanism assurance, which packages information
about the type of logon method (smart card or user name/password)
that is used to authenticate domain users inside each user’s Kerberos
token. When this feature is enabled in a network environment that has
deployed a federated identity management infrastructure, such as
Active Directory Federation Services (AD FS), the information in the
token can then be extracted whenever a user attempts to access any
claims-aware application that has been developed to determine
authorization based on a user’s logon method.

Active Directory – Design Guide
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010

Page 97

Prepared by Microsoft

Windows Server
2003 Forest
Functional Level

Supported Domain
Controller Operating
Systems

Advanced Features Available at Each Forest Functional
Level

Windows 2000

Windows 2000

All default AD DS features.

Windows Server 2003

Windows Server 2008

Windows Server 2008 R2

Windows Server 2003

Windows Server 2003

Windows Server 2008

Windows Server 2008 R2

Windows Server 2008

Windows Server 2008

Windows Server 2008 R2

Windows Server 2008 R2  Windows Server 2008 R2

Table 25: Windows Server 2008 R2 Forest Functional Levels

All Active Directory features available at the Windows Server 2000
functional level and:
(cid:2)  Forest trust
(cid:2)  Domain rename
(cid:2)  Linked-value replication
(cid:2)  Linked-value replication makes it possible for you to change group
membership to store and replicate values for individual members
instead of replicating the entire membership as a single unit. Storing
and replicating the values of individual members uses less network
bandwidth and fewer processor cycles during replication, and prevents
you from losing updates when you add or remove multiple members
concurrently at different domain controllers

(cid:2)  The ability to deploy a read-only domain controller (RODC)
(cid:2)  Improved Knowledge Consistency Checker (KCC) algorithms and

scalability

(cid:2)  The intersite topology generator (ISTG) uses improved algorithms that
scale to support forests with a greater number of sites than AD DS can
support at the Windows 2000 forest functional level. The improved
ISTG election algorithm is a less-intrusive mechanism for choosing the
ISTG at the Windows 2000 forest functional level

(cid:2)  The ability to create instances of the dynamic auxiliary class named

dynamicObject in a domain directory partition

(cid:2)  The ability to convert an inetOrgPerson object instance into a User
object instance, and to complete the conversion in the opposite
direction

(cid:2)  The ability to create instances of new group types to support role-

based authorization

(cid:2)  These types are called application basic groups and LDAP query

groups

(cid:2)  Deactivation and redefinition of attributes and classes in the schema

All of the features that are available at the Windows Server 2003 forest
functional level, but no additional features are available. All domains that
are subsequently added to the forest, however, operate at the Windows
Server 2008 domain functional level by default.

All of the features that are available at the Windows Server 2003 forest
functional level, plus the following features:
(cid:2)  Active Directory Recycle Bin, which provides the ability to restore

deleted objects in their entirety while AD DS is running

(cid:2)  All domains that are subsequently added to the forest will operate at
the Windows Server 2008 R2 domain functional level by default

Active Directory – Design Guide
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010

Page 98

Prepared by Microsoft

APPENDIX D

BACKGROUND INFORMATION FOR

PLANNING DOMAIN CONTROLLER

CAPACITY

Operation/Services

Variables Affecting Performance

PDC emulator operations master

The following operations typically have a high impact on the performance of the PDC
emulator:
(cid:2)  Password change forwarding and logon forwarding requests with mismatched

passwords for users, computers, and service accounts

(cid:2)  Group Policy updates
(cid:2)  The initial update of DFS
(cid:2)  Replicating directory changes to Windows NT4.0 BDCs

AD DS replication:
(cid:2)  Replication to partner Domain

The impact varies depending on the number and type of replication partners. Replicating to
more than fifteen intersite partners can have a high impact on performance.

controllers

Workstation logon:
(cid:2)  Startup process

The impact varies based on the number of workstations.

Application directory partition hosting

The impact varies based on the use of data that is contained in the application directory
partition.

GC operations:
(cid:2)  Universal group membership lookups
(cid:2)  Forest-wide searches

If this domain controller functions as a GC server, performance varies according to the type
of programs that are used. Programs that use GC searches extensively, such as Exchange
2000, have a high impact on performance.

Other operations:
(cid:2)  File and print

Network Services:
(cid:2)  DNS
(cid:2)  WINS
(cid:2)  DHCP
(cid:2)  IPSec

Users logging on:
(cid:2)  User authentication
(cid:2)  Authorisation for resource access

requests

Look-up operations:
(cid:2)  LDAP searches

The impact varies based on the number of users who are using the domain controller as a
file and print server.

The impact varies based on the number of services that are performed by the domain
controller. For example, hosting multiple services, such as DNS, WINS, and DHCP,
typically has a high impact on performance. Hosting a single service, such as DNS,
typically has a low impact on performance. For IPSec, the impact on performance varies
according to the number of connections.

The impact varies based on the number of users.

The impact varies based on the type of searches and the number of searches that the
program performs and whether they use the newer features such as Variable List View or
paged searches, whether the searches query against indexed attributes and whether the
queries are scoped.

Infrastructure operations master

The validation of links to moved objects typically has a low impact on performance.

RID pool operations master

RID pool distribution typically has a low impact on performance.

Schema operations master

Modification to the schema typically has low impact on performance.

Domain naming operations master

The addition or deletion of domains typically has low impact on performance.

Table 26: Effect of Operations and Services on Domain Controller Performance

Active Directory – Design Guide
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010

Page 99

Prepared by Microsoft

Component

Operating system files

Active Directory log files

Operations Performed

RAID System

Read and write operations

Mostly write operations

RAID 1

RAID 1

Active Directory database and SYSVOL shared folder

Mostly read operations

RAID 1 or RAID 0+1

Table 27: RAID System Requirements

Note

If cost is a factor in planning for disk space, then the operating system and Active Directory database
should be placed on one RAID array (such as RAID 0+1), and the Active Directory log files on another
RAID array (such as RAID 1). However, it is recommended that the Active Directory database and the
SYSVOL shared folder are stored on the same drive.

Active Directory – Design Guide
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010

Page 100

Prepared by Microsoft

APPENDIX E

AD DS TESTS

The following list identifies some of the key tests which can be performed to prove the installation
and design of AD DS:

(cid:1)  Verify hardware configuration of the domain controllers

(cid:1)  Verify system information on the domain controllers

(cid:1)  Verify the TCP/IP configurations and network components on the domain controllers

(cid:1)  Verify forward and reverse name resolution on the domain controllers

(cid:1)  Verify RAID and disk drive configurations on the domain controllers

(cid:1)  Verify the time information on the domain controllers

(cid:1)  Verify that Terminal Services are installed in Remote Administration mode on the domain

controllers

(cid:1)  Verify boot.ini configurations on the domain controllers

(cid:1)  Verify connectivity for the domain controllers

(cid:1)  Verify shares on the domain controllers

(cid:1)  Verify that the event ID 13516 is logged in the event log (SYSVOL initialised)

(cid:1)  Verify that the DCPromo.log, DCPromoui.log, and netsetup.log logs are error free

(cid:1)  Run nltest to confirm domain controllers in the domain and verify that the secure channel

works

(cid:1)  Confirm all the forests (and therefore domains) are running in native mode

(cid:1)  Verify that there are multiple forests, if relevant

(cid:1)  Verify the different domains, if relevant

(cid:1)  Verify that the internal OU design for the domain is correct

(cid:1)  Verify that the internal OU design for the service owner OUs of the domain is correct

(cid:1)  Verify the placement of the GC servers

(cid:1)  Verify the placement of the Operations Master roles

(cid:1)  Verify that the site design is correct

(cid:1)  Verify that the subnet allocation is correct

(cid:1)  Verify that the site links are established between the correct sites

(cid:1)  Verify that the site link properties are correctly configured

(cid:1)  Verify that the server objects are in the correct sites

(cid:1)  Verify that the different member servers are placed in the correct OUs

(cid:1)  Verify the LDAP Policy configuration

(cid:1)  Ensure that the Active Directory user functionality is normal

(cid:1)  Confirm that dcdiag and netdiag do not report any errors

(cid:1)  Use replmon to confirm error free replication between the domain controllers

(cid:1)  Run repadmin to confirm replication partners for each domain controller server

(cid:1)  Failover internal AD DS servers under load conditions

Active Directory – Design Guide
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010

Page 101

Prepared by Microsoft

(cid:1)  Ensure that under load conditions, NIC teaming works fine on the domain controllers

(cid:1)  Verify that the DDP and DDCP are applied properly

(cid:1)  Ensure that any external or cross-forest trusts between forests are working correctly

(cid:1)  Verify the administrative groups in Admins OU

(cid:1)  Verify ports configured for the Netlogon, NTDS, and FRS services on the domain

controllers

(cid:1)  Verify that the AD DS operation under load in an integrated environment

(cid:1)  Verify that only the Domain Admins have the administrative permissions on the Active

Directory Users and Computers MMC

(cid:1)  Test that DNS is functioning as required for AD DS

(cid:1)  Test that WINS is functioning as required for AD DS

This is a list of tests that was originally published as part of the Windows Server System Reference
Architecture (WSSRA) which has subsequently been replaced with the Infrastructure Planning and
Design (IPD) series. The details of the tests were not carried forward into the IPD and so have
been lost. However the tests are noted above for reference and to provide guidance on the sort of
tests that are useful in verifying the successful implementation and deployment of AD DS.

Active Directory – Design Guide
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010

Page 102

Prepared by Microsoft

APPENDIX F DOCUMENT INFORMATION

PART I  TERMS AND ABBREVIATIONS

Abbreviation

Definition

ACL

ADFS

ADSI

AG

API

BIND

CA

CMD

CN

CPU

CUI

DC

DDCP

DDP

DFS

DHCP

DN

DNS

EFS

FQDN

FSMO

GPMC

GPO

GUI

IETF

IIFP

IFN

ILM

IIS

IM&T

IP

IPSec

Access Control List

Active Directory Federation Service

Active Directory Scripting Interface

Account Group

Application Programming Interface

Berkeley Internet Name Domain

Certificate Authority

Command

Common Name

Central Processing Unit

Common User Interface

Domain Controller

Default Domain Controller Policy

Default Domain Policy

Distributed File System

Dynamic Host Configuration Protocol

Distinguished Name

Domain Name System

Encrypted File System

Fully Qualified Domain Name

Flexible Single Master Operations

Group Policy Management Console

Group Policy Object

Graphical User Interface

Internet Engineering Task Force

Identity and Integration Feature Pack

Install From Media

Identity Lifecycle Manager

Internet Information Server

Information Management and Technology

Internet Protocol

Internet Protocol Security

Active Directory – Design Guide
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010

Page 103

Prepared by Microsoft

Abbreviation

Definition

ISA

IT

KB

KCC

LAN

LDAP

LSP

MBSA

MMC

MOF

MSDN

MSF

NAT

NC

Internet Security and Authorisation Server

Information Technology

Knowledge Base

Knowledge Consistency Checker

Local Area Network

Lightweight Directory Access Protocol

Local Service Provider

Microsoft Baseline Security Analyser

Microsoft Management Console

Microsoft Operations Framework

Microsoft Developer Network

Microsoft Solutions Framework

Network Address Translation

Naming Context

NetBIOS

Network Basic Input Output System

NTP

OU

PCT

PDC

PKI

RAID

RDN

RFC

RG

RID

RIS

RPC

RR

RSO

SAM

SCW

SDK

SID

SIG

SMB

SMTP

Network Time Protocol

Organisational Unit

Primary Care Trust

Primary Domain Controller

Public Key Infrastructure

Redundant Array of Independent Disks

Relative Distinguished Name

Request For Comments

Resource Group

Relative Identifier

Remote Installation Services

Remote Procedure Call

Resource Record

Reduced Sign On

Security Account Manager

Security Configuration Wizard

Software Development Kit

Security Identifier

Special Interest Group

Server Message Blocks

Simple Mail Transfer Protocol

Active Directory – Design Guide
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010

Page 104

Prepared by Microsoft

Abbreviation

SP

SPN

SQL

SRV

SSO

TCO

UPN

UTF-8

VPN

WAN

WINS

WMI

WSH

WSSRA

WSUS

Table 28: Terms and Abbreviations

Definition

Service Pack

Service Principal Name

Structured Query Language

Service

Single Sign On

Total Cost of Ownership

User Principal Name

Universal Transformation Format-8

Virtual Private Network

Wide Area Network

Windows Internet Name Service

Windows Management Interface

Windows Scripting Host

Windows Server System Reference Architecture

Windows Software Update Service

Active Directory – Design Guide
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010

Page 105

PART II REFERENCES

Reference  Document

Prepared by Microsoft

Version

R1.

R2.

R3.

R4.

R5.

R6.

R7.

R8.

R9.

R10.

R11.

R12.

R13.

R14.

R15.

R16.

R17.

Infrastructure Planning and Design:
http://technet.microsoft.com/en-gb/library/cc196387.aspx

Microsoft TechNet: Windows Server 2008 AD DS Design:
http://technet2.microsoft.com/windowsserver/en/library/c283b699-6124-4c3a-87ef-
865443d7ea4b1033.mspx

Microsoft TechNet Windows Server 2008 and Windows Server 2008 R2:
http://technet.microsoft.com/en-us/library/dd349801(WS.10).aspx

Automated Build Healthcare Desktop and Server Guide
http://www.microsoft.com/industry/healthcare/technology/hpo/desktop/desktop.aspx

2.0.0.0

Microsoft TechNet: Active Directory Services:
http://technet.microsoft.com/en-us/library/dd578336(WS.10).aspx

Microsoft TechNet: Windows Server Technologies: Networking:
http://technet.microsoft.com/en-us/library/cc753940(WS.10).aspx

Microsoft TechNet: Installed help for Windows Server 2008 R2:
http://technet.microsoft.com/en-us/library/dd851728.aspx

Microsoft Download Center: Active Directory (AD) Management Pack for Operations Manager 2007:
http://www.microsoft.com/downloads/details.aspx?FamilyId=008F58A6-DC67-4E59-95C6-
D7C7C34A1447&amp;displaylang=en&displaylang=en

MSDN: Windows Script Host:
http://msdn2.microsoft.com/en-us/library/9bbdkx3k

Microsoft Download Center: Active Directory in Networks Segmented by Firewalls:
http://www.microsoft.com/downloads/details.aspx?FamilyID=c2ef3846-43f0-4caf-9767-
a9166368434e&DisplayLang=en

Microsoft TechNet: Microsoft Windows Server TechCenter: Active Directory Best practices:
http://technet2.microsoft.com/WindowsServer/en/library/5712b108-176a-4592-bcde-
a61e733579301033.mspx?mfr=true

Microsoft TechNet: Microsoft Windows Server TechCenter: DNS best practices:
http://technet2.microsoft.com/windowsserver/en/library/59d7a747-48dc-42cc-8986-
c73db47398a21033.mspx

Microsoft TechNet: Microsoft Windows Server TechCenter: WINS Best Practices:
http://technet2.microsoft.com/windowsserver/en/library/ed9beba0-f998-47d2-8137-
a2fc52886ed71033.mspx

Microsoft Download Center: Job Aids for Windows Server 2003 Deployment Kit:
http://www.microsoft.com/downloads/details.aspx?FamilyID=edabb894-4290-406c-87d1-
607a58fc81f0&DisplayLang=en

Microsoft TechNet: Microsoft Windows Server TechCenter: Identifying the Deployment Project
Participants:
http://technet.microsoft.com/en-us/library/cc732532(WS.10).aspx

Microsoft TechNet: Microsoft Windows Server TechCenter: Forest Design Models:
http://technet.microsoft.com/en-us/library/cc770439(WS.10).aspx

Microsoft TechNet: Microsoft Windows Server TechCenter: Identifying Forest Design Requirements:
http://technet.microsoft.com/en-us/library/cc730924(WS.10).aspx

Active Directory – Design Guide
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010

Page 106

Reference  Document

Prepared by Microsoft

Version

R18.

R19.

R20.

R21.

R22.

R23.

R24.

R25.

R26.

R27.

R28.

R29.

R30.

R31.

R32.

R33.

R34.

R35.

Service Administrator Scope of Authority:
http://technet.microsoft.com/en-us/library/cc772268(WS.10).aspx

Forest Design Models:
http://technet.microsoft.com/en-us/library/cc770439(WS.10).aspx

Group Policy for Healthcare Desktop Management
http://www.microsoft.com/industry/healthcare/technology/hpo/desktop/grouppolicy.aspx

1.0.0.0

Microsoft TechNet: Microsoft Windows Server TechCenter: Trust Technologies:
http://technet2.microsoft.com/windowsserver/en/library/9d688a18-15c7-4d4e-9d34-
7a763baa50a11033.mspx and
http://technet.microsoft.com/en-us/library/cc770299.aspx

Microsoft TechNet: Multiple Forest Considerations in Windows 2000 and Windows Server 2003:
http://technet2.microsoft.com/windowsserver/en/library/bda0d769-a663-42f4-879f-
f548b19a8c7e1033.mspx

Microsoft TechNet: Microsoft Windows Server TechCenter: Domain and Forest Trust Tools and Settings:
http://technet2.microsoft.com/windowsserver/en/library/108124dd-31b1-4c2c-9421-
6adbc1ebceca1033.mspx and
http://technet.microsoft.com/en-us/library/cc770299.aspx

Microsoft TechNet: Microsoft Windows Server TechCenter: Security Considerations for Trusts
http://technet2.microsoft.com/windowsserver/en/library/1f33e9a1-c3c5-431c-a5cc-
c3c2bd579ff11033.mspx and
http://technet.microsoft.com/en-us/library/cc770299.aspx

Naming conventions in Active Directory for computers, domains, sites, and OUs:
http://support.microsoft.com/kb/909264

Microsoft Help and Support: Information about configuring Windows for domains with single-label DNS
names:
http://support.microsoft.com/kb/300684

IETF, The Internet Engineering Task Force: Request For Comments:
http://www.ietf.org/rfc/rfc2822.txt

Microsoft Help and Support: Users Can Log On Using User Name or User Principal Name:
http://support.microsoft.com/kb/243280

The Administrator Accounts Security Planning Guide:
http://www.microsoft.com/technet/security/topics/serversecurity/administratoraccounts/default.mspx

Automated Build Healthcare Desktop and Server Guide
http://www.microsoft.com/industry/healthcare/technology/hpo/desktop/desktop.aspx

2.0.0.0

Microsoft Technet Centre: Running Domain Controllers in Hyper-V:
http://technet.microsoft.com/en-us/library/dd363553(WS.10).aspx

Microsoft Download Center: Branch Office Infrastructure Solution for Microsoft Windows Server 2003
Release 2:
http://www.microsoft.com/technet/solutionaccelerators/branch/default.mspx

Windows Server 2008 R2 AD DS Deployment Guide Web page:
http://technet.microsoft.com/en-us/library/cc732877(WS.10).aspx

FSMO placement and optimization on Active Directory domain controllers:
http://support.microsoft.com/kb/223346

Microsoft TechNet: Microsoft Windows Server TechCenter: Planning Operations Master Role Placement:
http://technet.microsoft.com/en-us/library/cc754889(WS.10).aspx

Active Directory – Design Guide
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010

Page 107

Reference  Document

Prepared by Microsoft

Version

R36.

R37.

R38.

R39.

R40.

R41.

R42.

R43.

R44.

R45.

R46.

R47.

R48.

R49.

Site Link Properties:
http://technet.microsoft.com/en-us/library/cc753700(WS.10).aspx

Microsoft TechNet: Microsoft Windows Server TechCenter: Creating a Site Link Bridge Design:
http://technet.microsoft.com/en-us/library/cc753638(WS.10).aspx

Microsoft TechNet: Microsoft Windows Server TechCenter: Background Information for Planning Domain
Controller Capacity:
http://technet2.microsoft.com/windowsserver/en/library/52bf61a8-9845-4878-8fa4-
a85c57fe25e51033.mspx

Microsoft TechNet: Microsoft Windows Server TechCenter: Adding Domain Controllers to Support
Replication Between Sites:
http://technet2.microsoft.com/windowsserver/en/library/4a59cc62-9425-463f-89b6-
95347e2ea91e1033.mspx

Microsoft TechNet: Microsoft Windows Server TechCenter: Determining the Minimum Number of Domain
Controllers Required:
http://technet2.microsoft.com/windowsserver/en/library/2619a7f0-c6ab-435a-83db-
34f1425107e71033.mspx

Windows Server 2003: Deployment Whitepaper: Best Practice Guide for Securing Active Directory
Installations:
http://technet2.microsoft.com/windowsserver/en/library/edc08cf1-d4ba-4235-9696-
c93b0313ad6e1033.mspx?mfr=true

Microsoft Download Center: Best Practices for Delegating Active Directory Administration:
http://go.microsoft.com/fwlink/?LinkID=22708

Microsoft TechNet: Microsoft Windows Server TechCenter: Addressing User-Related Requirements:
http://technet2.microsoft.com/windowsserver/en/library/a35e88e7-2504-4a60-ba78-
7c9efa05d3fa1033.mspx

Healthcare EFS Tool Administration Guide:
http://www.microsoft.com/industry/healthcare/technology/hpo/security/EFSTool.aspx

1.0.0.0

Microsoft TechNet: Microsoft Windows Server TechCenter: Creating a Foundation for Authentication:
http://technet2.microsoft.com/windowsserver/en/library/2df33645-5e3e-4b79-9733-
ffa2a3cf60c41033.mspx

Microsoft TechNet: Microsoft Windows Server TechCenter: Deployment Guide for the Security
Configuration Wizard:
http://technet2.microsoft.com/windowsserver/en/library/5254f8cd-143e-4559-a299-
9c723b3669461033.mspx and Windows Server 2008 specific content
http://technet.microsoft.com/en-us/library/cc731515(WS.10).aspx

Microsoft TechNet: Extended Your Authentication Framework:
http://technet2.microsoft.com/windowsserver/en/library/1d90e7c1-37e3-4efe-bf64-
1b9ffa93b1a71033.mspx with supplementary information specific to Windows Server 2008 and Windows
Server 2008 R2 http://technet.microsoft.com/en-us/library/dd548350(WS.10).aspx

Microsoft TechNet: Microsoft Windows Server TechCenter: Defining Policies for Security Group
Management:
http://technet2.microsoft.com/windowsserver/en/library/033a0042-ff57-4657-8350-
c7a6ebe3b8991033.mspx

Microsoft TechNet: Microsoft Windows Server TechCenter: Selecting Local Groups or Domain Local
Groups as Resource Groups:
http://technet2.microsoft.com/windowsserver/en/library/1b3070ce-c6b1-4849-ae47-
ce17bbec17ee1033.mspx

Active Directory – Design Guide
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010

Page 108

Reference  Document

Prepared by Microsoft

Version

R50.

R51.

R52.

R53.

R54.

R55.

R56.

R57.

R58.

R59.

R60.

R61.

R62.

R63.

R64.

R65.

R66.

R67.

Microsoft TechNet: Microsoft Windows Server TechCenter: Planning a Smart Card Deployment:
http://technet2.microsoft.com/windowsserver/en/library/5229033e-232b-4f91-9f86-
0cbbd7cfc5a81033.mspx

Microsoft TechNet: Microsoft Windows Server TechCenter: DNS Concepts:
http://technet.microsoft.com/en-us/library/dd197461(WS.10).aspx

IETF, The Internet Engineering Task Force: Request For Comments: A DNS RR for specifying the
location of services (DNS SRV):
http://www.ietf.org/rfc/rfc2782.txt

IETF, The Internet Engineering Task Force: Request For Comments: Dynamic Updates in the Domain
Name System (DNS UPDATE):
http://www.ietf.org/rfc/rfc2136.txt

Configuring BIND to work with Microsoft Active Directory:
http://www.microsoft.com/technet/archive/interopmigration/linux/mvc/cfgbind.mspx

Microsoft Help and Support: How to configure DNS dynamic updates in Windows Server 2003:
http://support.microsoft.com/kb/816592

Microsoft TechNet: Microsoft Windows Server TechCenter: Deploying WINS:
http://technet2.microsoft.com/windowsserver/en/library/a5e0f87f-9b40-47ed-b613-
3b4963bd91e61033.mspx and http://technet.microsoft.com/en-us/library/cc771750(WS.10).aspx

Microsoft Download Center: Active Directory in Networks Segmented by Firewalls:
http://www.microsoft.com/downloads/details.aspx?FamilyID=c2ef3846-43f0-4caf-9767-
a9166368434e&DisplayLang=en

Microsoft Download Center: Running Domain Controllers in Hyper-V:
http://technet.microsoft.com/en-us/library/dd363553(WS.10).aspx

Microsoft Download Center: Creating a Test Plan:
http://technet2.microsoft.com/windowsserver/en/library/998c2ebb-ff0d-4bd5-82ae-
d500966250121033.mspx

Microsoft TechNet: Microsoft Windows Server TechCenter: Planning the Test Plan:
http://technet2.microsoft.com/windowsserver/en/library/05f4d318-f2b4-4544-b50a-
6aef2174532a1033.mspx

Microsoft TechNet: Microsoft Windows Server TechCenter: Documenting the Test Lab Configuration:
http://technet2.microsoft.com/windowsserver/en/library/232b6b08-d5b7-4437-bddf-
a142636091741033.mspx

Microsoft TechNet: Microsoft Windows Server TechCenter: Developing an Incident-Tracking System:
http://technet2.microsoft.com/windowsserver/en/library/e213d6a5-7d4e-48cf-87b8-
00eb52aae61f1033.mspx

Microsoft TechNet: Microsoft Windows Server TechCenter: Creating a Pilot Plan:
http://technet2.microsoft.com/windowsserver/en/library/99f07a8e-503b-4751-b108-
c85e188ada951033.mspx

Microsoft TechNet: Microsoft Windows Server TechCenter: Preparing for the Pilot
http://technet2.microsoft.com/windowsserver/en/library/0a5f853e-28d2-4afe-a9db-
92761a8d3ed61033.mspx

Configuring DNS for the Forest Root Domain:
http://technet.microsoft.com/en-us/library/cc771849(WS.10).aspx

Microsoft TechNet: Microsoft Windows Server TechCenter: Verify DNS for the Forest Root Domain:
http://technet.microsoft.com/en-us/library/cc754529(WS.10).aspx

Windows Server 2008 Deployment Guide: Reconfigure the DNS service:
http://technet.microsoft.com/en-us/library/cc732922(WS.10).aspx

Active Directory – Design Guide
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010

Page 109

Reference  Document

Prepared by Microsoft

Version

R68.

R69.

R70.

R71.

R72.

R73.

R74.

R75.

R76.

R77.

R78.

R79.

R80.

R81.

R82.

R83.

R84.

R85.

R86.

Microsoft TechNet: Microsoft Windows Server TechCenter: [DCInstall] (Unattended Installation):
http://technet2.microsoft.com/WindowsServer/en/library/9639f180-c7fe-41c6-8c3d-
92389023f0e71033.mspx

Microsoft Help and Support: How to use the Install from Media feature to promote Windows Server 2003-
based domain controllers:
http://support.microsoft.com/kb/311078.

Microsoft TechNet: Windows Server 2008: Transfer operations master roles:
http://technet.microsoft.com/en-us/library/cc816946(WS.10).aspx

Microsoft TechNet: Active Directory Delegation Tools:
http://technet.microsoft.com/en-us/library/cc756087(WS.10).aspx and for Windows Server 2008
http://technet.microsoft.com/en-us/library/dd145344.aspx

Microsoft TechNet: Microsoft Operations Framework 4.0:
http://www.microsoft.com/technet/itsolutions/cits/mo/mof/mofeo.mspx

Microsoft Download Center: Microsoft Solutions Framework Core White Papers:
http://www.microsoft.com/downloads/details.aspx?FamilyID=e481cb0b-ac05-42a6-bab8-
fc886956790e&DisplayLang=en

WSUS:
http://www.microsoft.com/windowsserversystem/updateservices/default.mspx

Baseline Security Analyser (MSBA):
http://www.microsoft.com/technet/security/tools/mbsahome.mspx

Active Directory Product Operations Guide TechNet article:
http://www.microsoft.com/technet/itsolutions/cits/mo/winsrvmg/adpog/adpog1.mspx

DNS Product Operations Guide TechNet article:
http://www.microsoft.com/technet/itsolutions/cits/mo/winsrvmg/dnspog/dnspog1.mspx

WINS Product Operations Guide TechNet article:
http://www.microsoft.com/technet/itsolutions/cits/mo/winsrvmg/winspog/winspog1.mspx

Microsoft TechNet: Microsoft Windows Server TechCenter: Monitoring Domain Controller Performance:
http://technet2.microsoft.com/windowsserver/en/library/c5d72b6f-5974-4263-b29f-
2eece0ab44371033.mspx

Microsoft TechNet: Microsoft Windows Server TechCenter: Performance and Reliability Monitor
overview:
http://technet.microsoft.com/en-us/library/cc771692(WS.10).aspx

Microsoft TechNet: Microsoft Windows Server TechCenter: Active Directory Operations Guide:
http://technet.microsoft.com/en-us/library/cc816807(WS.10).aspx

Microsoft TechNet: Microsoft Windows Server TechCenter: DNS Server Operations Guide:
http://technet.microsoft.com/en-us/library/cc816603(WS.10).aspx

Microsoft TechNet: Microsoft Windows Server TechCenter: Group Policy Planning and Deployment
Guide:
http://technet.microsoft.com/en-us/library/cc754948(WS.10).aspx

Microsoft TechNet: Windows Server 2003 Product Help: Common Administrative Tasks:
http://technet2.microsoft.com/windowsserver/en/library/f2d54234-6d65-439b-9d3b-
ac1c4b2a3f991033.mspx

Microsoft TechNet: Microsoft Windows Server TechCenter: Active Directory Step-by-step Guides:
http://technet.microsoft.com/en-gb/windowsserver/2008/default.aspx

Performance Tuning Guidelines for Windows Server 2003 whitepaper:
http://go.microsoft.com/fwlink/?LinkId=24798

Active Directory – Design Guide
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010

Page 110

Reference  Document

Prepared by Microsoft

Version

R87.

R88.

R89.

R90.

R91.

R92.

R93.

R94.

R95.

R96.

R97.

R98.

R99.

Microsoft TechNet: Microsoft Windows Server TechCenter: Windows Server 2003 Performance Counters
Reference:
http://technet2.microsoft.com/WindowsServer/en/Library/3fb01419-b1ab-4f52-a9f8-
09d5ebeb9ef21033.mspx

Microsoft TechNet: Active Directory Product Operations Guide, chapter 3:
http://www.microsoft.com/technet/itsolutions/cits/mo/winsrvmg/adpog/adpog3.mspx

Microsoft Download Center: Active Directory Forest Recovery whitepaper:
http://go.microsoft.com/fwlink/?LinkId=13079

Microsoft TechNet: Script Center:
http://www.microsoft.com/technet/scriptcenter/default.mspx

Microsoft TechNet: Script Repository: Active Directory:
http://www.microsoft.com/technet/scriptcenter/scripts/ad/default.mspx

Microsoft TechNet: Script Repository: DNS Server:
http://www.microsoft.com/technet/scriptcenter/scripts/network/dns/default.mspx

MSDN Library: Using Active Directory Domain Services:
http://msdn2.microsoft.com/en-gb/library/aa746434.aspx

Microsoft TechNet: Microsoft Windows Server TechCenter: Step-by-Step Guide to Active Directory Bulk
Import and Export:
http://www.microsoft.com/technet/prodtechnol/windowsserver2003/technologies/directory/activedirectory/
stepbystep/adbulk.mspx

Microsoft TechNet: Windows Server Commands, References and Tools:
http://technet.microsoft.com/en-us/library/dd560674(WS.10).aspx

Microsoft TechNet: Remote Server Administration Tools:
http://technet.microsoft.com/en-us/library/cc731209.aspx

Microsoft Download Center: Windows Server 2003 Service Pack 2 32-bit Support Tools:
http://www.microsoft.com/downloads/details.aspx?familyid=96A35011-FD83-419D-939B-
9A772EA2DF90&displaylang=en

Microsoft TechNet: Windows Server 2008 and Server 2008 R2 Server Manager:
http://technet.microsoft.com/en-us/library/cc770629(WS.10).aspx

Microsoft Download Center: Administration with Windows Powershell:
http://technet.microsoft.com/en-us/library/dd378937(WS.10).aspx

R100.

  Microsoft TechNet: Windows Performance Monitor:

http://technet.microsoft.com/en-us/library/cc749249.aspx

R101.

  Microsoft TechNet Best Practice Analyzer for Active Directory Domain Services:

http://technet.microsoft.com/en-us/library/dd391875(WS.10).aspx

R102.

R103.

Naming conventions in Active Directory for computers, domains, sites, and OUs:
http://support.microsoft.com/kb/909264

  Microsoft Download Center: Branch Office Infrastructure Solution for Windows Server 2008
http://www.microsoft.com/downloads/details.aspx?familyid=02057405-49AF-4867-BF1D-
E0232B5C59E3&displaylang=en

R104.

  Microsoft Technet: Configure the Operations Master roles:

http://technet.microsoft.com/en-us/library/cc732963(WS.10).aspx

R105.

  Microsoft Technet: Appendix of Unattended installation parameters:
http://technet.microsoft.com/en-us/library/cc732086(WS.10).aspx

R106.

  Microsoft Technet: Installing an additional domain controller by using IFM:

http://technet.microsoft.com/en-us/library/cc816722(WS.10).aspx

Active Directory – Design Guide
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010

Page 111

Prepared by Microsoft

Version

Reference  Document

R107.

  Microsoft Technet: Installing AD DS from media:

http://technet.microsoft.com/en-us/library/cc770654(WS.10).aspx

R108.

  Windows Powershell:

http://technet.microsoft.com/en-us/library/bb978526.aspx

R109.

  Microsoft Technet: Active Directory Module for Windows Powershell:
http://technet.microsoft.com/en-us/library/dd378783(WS.10).aspx

Table 29: References

Active Directory – Design Guide
Prepared by Microsoft, Version 2.0.0.0
Last modified on 26 February 2010

Page 112

