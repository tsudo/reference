---
title: "NIST Cybersecurity Framework v1.1"
organization: "NIST"
content_type: framework
year: 2018
tags: ["nist-csf;v1.1;cybersecurity-framework"]
source_url: "https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.04162018.pdf"
license: "© NIST. Reproduced for research and educational purposes per 17 U.S.C. § 107 (fair use)."
date_ingested: 2026-02-22
original_format: pdf
---

Framework for Improving
Critical Infrastructure Cybersecurity

Version 1.1

National Institute of Standards and Technology

April 16, 2018

April 16, 2018

Cybersecurity Framework

Version 1.1

Note to Readers on the Update

Version 1.1 of this Cybersecurity Framework refines, clarifies, and enhances Version 1.0, which
was issued in February 2014. It incorporates comments received on the two drafts of Version 1.1.

Version 1.1 is intended to be implemented by first-time and current Framework users. Current
users should be able to implement Version 1.1 with minimal or no disruption; compatibility with
Version 1.0 has been an explicit objective.

The following table summarizes the changes made between Version 1.0 and Version 1.1.

Table NTR-1 - Summary of changes between Framework Version 1.0 and Version 1.1.

Update

Clarified that terms like
“compliance” can be
confusing and mean
something very different
to various Framework
stakeholders

A new section on self-
assessment

Greatly expanded
explanation of using
Framework for Cyber
Supply Chain Risk
Management purposes

Refinements to better
account for authentication,
authorization, and identity
proofing

Better explanation of the
relationship between
Implementation Tiers and
Profiles

Description of Update

Added clarity that the Framework has utility as a structure and
language for organizing and expressing compliance with an
organization’s own cybersecurity requirements.  However, the
variety of ways in which the Framework can be used by an
organization means that phrases like “compliance with the
Framework” can be confusing.

Added Section 4.0 Self-Assessing Cybersecurity Risk with the
Framework to explain how the Framework can be used by
organizations to understand and assess their cybersecurity risk,
including the use of measurements.
An expanded Section 3.3 Communicating Cybersecurity
Requirements with Stakeholders helps users better understand
Cyber Supply Chain Risk Management (SCRM), while a new
Section 3.4 Buying Decisions highlights use of the Framework
in understanding risk associated with commercial off-the-shelf
products and services. Additional Cyber SCRM criteria were
added to the Implementation Tiers. Finally, a Supply Chain Risk
Management Category, including multiple Subcategories, has
been added to the Framework Core.
The language of the Access Control Category has been refined
to better account for authentication, authorization, and identity
proofing. This included adding one Subcategory each for
Authentication and Identity Proofing. Also, the Category has
been renamed to Identity Management and Access Control
(PR.AC) to better represent the scope of the Category and
corresponding Subcategories.
Added language to Section 3.2 Establishing or Improving a
Cybersecurity Program on using Framework Tiers in
Framework implementation. Added language to Framework
Tiers to reflect integration of Framework considerations within
organizational risk management programs. The Framework Tier
concepts were also refined. Updated Figure 2.0 to include
actions from the Framework Tiers.

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

ii

April 16, 2018

Cybersecurity Framework

Version 1.1

Consideration of
Coordinated Vulnerability
Disclosure

A Subcategory related to the vulnerability disclosure lifecycle
was added.

As with Version 1.0, Version 1.1 users are encouraged to customize the Framework to maximize
individual organizational value.

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

iii

April 16, 2018

Cybersecurity Framework

Version 1.1

Acknowledgements

This publication is the result of an ongoing collaborative effort involving industry, academia, and
government. The National Institute of Standards and Technology (NIST) launched the project by
convening private- and public-sector organizations and individuals in 2013. Published in 2014
and revised during 2017 and 2018, this Framework for Improving Critical Infrastructure
Cybersecurity has relied upon eight public workshops, multiple Requests for Comment or
Information, and thousands of direct interactions with stakeholders from across all sectors of the
United States along with many sectors from around the world.

The impetus to change Version 1.0 and the changes that appear in this Version 1.1 were based
on:

  Feedback and frequently asked questions to NIST since release of Framework Version

1.0;

  105 responses to the December 2015 request for information (RFI), Views on the

Framework for Improving Critical Infrastructure Cybersecurity;

  Over 85 comments on a December 5, 2017 proposed second draft of Version 1.1;
  Over 120 comments on a January 10, 2017, proposed first draft Version 1.1; and

Input from over 1,200 attendees at the 2016 and 2017 Framework workshops.

In addition, NIST previously released Version 1.0 of the Cybersecurity Framework with a
companion document, NIST Roadmap for Improving Critical Infrastructure Cybersecurity. This
Roadmap highlighted key “areas of improvement” for further development, alignment, and
collaboration.  Through private and public-sector efforts, some areas of improvement have
advanced enough to be included in this Framework Version 1.1.

NIST acknowledges and thanks all of those who have contributed to this Framework.

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

iv

April 16, 2018

Cybersecurity Framework

Version 1.1

Executive Summary

The United States depends on the reliable functioning of critical infrastructure. Cybersecurity
threats exploit the increased complexity and connectivity of critical infrastructure systems,
placing the Nation’s security, economy, and public safety and health at risk. Similar to financial
and reputational risks, cybersecurity risk affects a company’s bottom line. It can drive up costs
and affect revenue. It can harm an organization’s ability to innovate and to gain and maintain
customers. Cybersecurity can be an important and amplifying component of an organization’s
overall risk management.
To better address these risks, the Cybersecurity Enhancement Act of 20141 (CEA) updated the
role of the National Institute of Standards and Technology (NIST) to include identifying and
developing cybersecurity risk frameworks for voluntary use by critical infrastructure owners and
operators. Through CEA, NIST must identify “a prioritized, flexible, repeatable, performance-
based, and cost-effective approach, including information security measures and controls that
may be voluntarily adopted by owners and operators of critical infrastructure to help them
identify, assess, and manage cyber risks.” This formalized NIST’s previous work developing
Framework Version 1.0 under Executive Order (EO) 13636, “Improving Critical Infrastructure
Cybersecurity” (February 2013), and provided guidance for future Framework evolution. The
Framework that was developed under EO 13636, and continues to evolve according to CEA,
uses a common language to address and manage cybersecurity risk in a cost-effective way based
on business and organizational needs without placing additional regulatory requirements on
businesses.

The Framework focuses on using business drivers to guide cybersecurity activities and
considering cybersecurity risks as part of the organization’s risk management processes. The
Framework consists of three parts: the Framework Core, the Implementation Tiers, and the
Framework Profiles. The Framework Core is a set of cybersecurity activities, outcomes, and
informative references that are common across sectors and critical infrastructure. Elements of the
Core provide detailed guidance for developing individual organizational Profiles. Through use of
Profiles, the Framework will help an organization to align and prioritize its cybersecurity
activities with its business/mission requirements, risk tolerances, and resources. The Tiers
provide a mechanism for organizations to view and understand the characteristics of their
approach to managing cybersecurity risk, which will help in prioritizing and achieving
cybersecurity objectives.

While this document was developed to improve cybersecurity risk management in critical
infrastructure, the Framework can be used by organizations in any sector or community. The
Framework enables organizations – regardless of size, degree of cybersecurity risk, or
cybersecurity sophistication – to apply the principles and best practices of risk management to
improving security and resilience.

The Framework provides a common organizing structure for multiple approaches to
cybersecurity by assembling standards, guidelines, and practices that are working effectively
today. Moreover, because it references globally recognized standards for cybersecurity, the

1See 15 U.S.C. § 272(e)(1)(A)(i).  The Cybersecurity Enhancement Act of 2014 (S.1353) became public law 113-
274 on December 18, 2014 and may be found at: https://www.congress.gov/bill/113th-congress/senate-
bill/1353/text.

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

v

April 16, 2018

Cybersecurity Framework

Version 1.1

Framework can serve as a model for international cooperation on strengthening cybersecurity in
critical infrastructure as well as other sectors and communities.

The Framework offers a flexible way to address cybersecurity, including cybersecurity’s effect
on physical, cyber, and people dimensions. It is applicable to organizations relying on
technology, whether their cybersecurity focus is primarily on information technology (IT),
industrial control systems (ICS), cyber-physical systems (CPS), or connected devices more
generally, including the Internet of Things (IoT). The Framework can assist organizations in
addressing cybersecurity as it affects the privacy of customers, employees, and other parties.
Additionally, the Framework’s outcomes serve as targets for workforce development and
evolution activities.

The Framework is not a one-size-fits-all approach to managing cybersecurity risk for critical
infrastructure. Organizations will continue to have unique risks – different threats, different
vulnerabilities, different risk tolerances. They also will vary in how they customize practices
described in the Framework. Organizations can determine activities that are important to critical
service delivery and can prioritize investments to maximize the impact of each dollar spent.
Ultimately, the Framework is aimed at reducing and better managing cybersecurity risks.

To account for the unique cybersecurity needs of organizations, there are a wide variety of ways
to use the Framework. The decision about how to apply it is left to the implementing
organization. For example, one organization may choose to use the Framework Implementation
Tiers to articulate envisioned risk management practices. Another organization may use the
Framework’s five Functions to analyze its entire risk management portfolio; that analysis may or
may not rely on more detailed companion guidance, such as controls catalogs. There sometimes
is discussion about “compliance” with the Framework, and the Framework has utility as a
structure and language for organizing and expressing compliance with an organization’s own
cybersecurity requirements. Nevertheless, the variety of ways in which the Framework can be
used by an organization means that phrases like “compliance with the Framework” can be
confusing and mean something very different to various stakeholders.

The Framework is a living document and will continue to be updated and improved as industry
provides feedback on implementation. NIST will continue coordinating with the private sector
and government agencies at all levels. As the Framework is put into greater practice, additional
lessons learned will be integrated into future versions. This will ensure the Framework is
meeting the needs of critical infrastructure owners and operators in a dynamic and challenging
environment of new threats, risks, and solutions.

Expanded and more effective use and sharing of best practices of this voluntary Framework are
the next steps to improve the cybersecurity of our Nation’s critical infrastructure – providing
evolving guidance for individual organizations while increasing the cybersecurity posture of the
Nation’s critical infrastructure and the broader economy and society.

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

vi

April 16, 2018

Cybersecurity Framework

Version 1.1

Table of Contents

Note to Readers on the Update ....................................................................................................... ii

Acknowledgements ........................................................................................................................ iv

Executive Summary .........................................................................................................................v

1.0

2.0

Framework Introduction .......................................................................................................1

Framework Basics .................................................................................................................6

3.0  How to Use the Framework ................................................................................................13

4.0

Self-Assessing Cybersecurity Risk with the Framework....................................................20

Appendix A: Framework Core .......................................................................................................22

Appendix B: Glossary ....................................................................................................................45

Appendix C: Acronyms .................................................................................................................48

List of Figures

Figure 1: Framework Core Structure .............................................................................................. 6

Figure 2: Notional Information and Decision Flows within an Organization .............................. 12

Figure 3: Cyber Supply Chain Relationships................................................................................ 17

List of Tables

Table 1: Function and Category Unique Identifiers ..................................................................... 23

Table 2: Framework Core ............................................................................................................. 24

Table 3: Framework Glossary ....................................................................................................... 45

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

vii

April 16, 2018

Cybersecurity Framework

Version 1.1

1.0  Framework Introduction

The United States depends on the reliable functioning of its critical infrastructure. Cybersecurity
threats exploit the increased complexity and connectivity of critical infrastructure systems,
placing the Nation’s security, economy, and public safety and health at risk. Similar to financial
and reputational risks, cybersecurity risk affects a company’s bottom line. It can drive up costs
and affect revenue. It can harm an organization’s ability to innovate and to gain and maintain
customers. Cybersecurity can be an important and amplifying component of an organization’s
overall risk management.
To strengthen the resilience of this infrastructure, the Cybersecurity Enhancement Act of 20142
(CEA) updated the role of the National Institute of Standards and Technology (NIST) to
“facilitate and support the development of” cybersecurity risk frameworks. Through CEA, NIST
must identify “a prioritized, flexible, repeatable, performance-based, and cost-effective approach,
including information security measures and controls that may be voluntarily adopted by owners
and operators of critical infrastructure to help them identify, assess, and manage cyber risks.”
This formalized NIST’s previous work developing Framework Version 1.0 under Executive
Order 13636, “Improving Critical Infrastructure Cybersecurity,” issued in February 20133, and
provided guidance for future Framework evolution.
Critical infrastructure4 is defined in the U.S. Patriot Act of 20015 as “systems and assets, whether
physical or virtual, so vital to the United States that the incapacity or destruction of such systems
and assets would have a debilitating impact on security, national economic security, national
public health or safety, or any combination of those matters.” Due to the increasing pressures
from external and internal threats, organizations responsible for critical infrastructure need to
have a consistent and iterative approach to identifying, assessing, and managing cybersecurity
risk. This approach is necessary regardless of an organization’s size, threat exposure, or
cybersecurity sophistication today.

The critical infrastructure community includes public and private owners and operators, and
other entities with a role in securing the Nation’s infrastructure. Members of each critical
infrastructure sector perform functions that are supported by the broad category of technology,
including information technology (IT), industrial control systems (ICS), cyber-physical systems
(CPS), and connected devices more generally, including the Internet of Things (IoT). This
reliance on technology, communication, and interconnectivity has changed and expanded the
potential vulnerabilities and increased potential risk to operations. For example, as technology
and the data it produces and processes are increasingly used to deliver critical services and
support business/mission decisions, the potential impacts of a cybersecurity incident on an

2 See 15 U.S.C. § 272(e)(1)(A)(i). The Cybersecurity Enhancement Act of 2014 (S.1353) became public law 113-

274 on December 18, 2014 and may be found at: https://www.congress.gov/bill/113th-congress/senate-
bill/1353/text.

3 Executive Order no. 13636, Improving Critical Infrastructure Cybersecurity, DCPD-201300091, February 12,

2013. https://www.gpo.gov/fdsys/pkg/CFR-2014-title3-vol1/pdf/CFR-2014-title3-vol1-eo13636.pdf

4 The Department of Homeland Security (DHS) Critical Infrastructure program provides a listing of the sectors and

their associated critical functions and value chains. http://www.dhs.gov/critical-infrastructure-sectors

5 See 42 U.S.C. § 5195c(e)).  The U.S. Patriot Act of 2001 (H.R.3162) became public law 107-56 on October 26,

2001 and may be found at: https://www.congress.gov/bill/107th-congress/house-bill/3162

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

 1

April 16, 2018

Cybersecurity Framework

Version 1.1

organization, the health and safety of individuals, the environment, communities, and the broader
economy and society should be considered.

To manage cybersecurity risks, a clear understanding of the organization’s business drivers and
security considerations specific to its use of technology is required. Because each organization’s
risks, priorities, and systems are unique, the tools and methods used to achieve the outcomes
described by the Framework will vary.

Recognizing the role that the protection of privacy and civil liberties plays in creating greater
public trust, the Framework includes a methodology to protect individual privacy and civil
liberties when critical infrastructure organizations conduct cybersecurity activities. Many
organizations already have processes for addressing privacy and civil liberties. The methodology
is designed to complement such processes and provide guidance to facilitate privacy risk
management consistent with an organization’s approach to cybersecurity risk management.
Integrating privacy and cybersecurity can benefit organizations by increasing customer
confidence, enabling more standardized sharing of information, and simplifying operations
across legal regimes.

The Framework remains effective and supports technical innovation because it is technology
neutral, while also referencing a variety of existing standards, guidelines, and practices that
evolve with technology. By relying on those global standards, guidelines, and practices
developed, managed, and updated by industry, the tools and methods available to achieve the
Framework outcomes will scale across borders, acknowledge the global nature of cybersecurity
risks, and evolve with technological advances and business requirements. The use of existing and
emerging standards will enable economies of scale and drive the development of effective
products, services, and practices that meet identified market needs. Market competition also
promotes faster diffusion of these technologies and practices and realization of many benefits by
the stakeholders in these sectors.

Building from those standards, guidelines, and practices, the Framework provides a common
taxonomy and mechanism for organizations to:

1) Describe their current cybersecurity posture;

2) Describe their target state for cybersecurity;

3) Identify and prioritize opportunities for improvement within the context of a

continuous and repeatable process;

4) Assess progress toward the target state;

5) Communicate among internal and external stakeholders about cybersecurity risk.

The Framework is not a one-size-fits-all approach to managing cybersecurity risk for critical
infrastructure. Organizations will continue to have unique risks – different threats, different
vulnerabilities, different risk tolerances. They also will vary in how they customize practices
described in the Framework. Organizations can determine activities that are important to critical
service delivery and can prioritize investments to maximize the impact of each dollar spent.
Ultimately, the Framework is aimed at reducing and better managing cybersecurity risks.

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

 2

April 16, 2018

Cybersecurity Framework

Version 1.1

To account for the unique cybersecurity needs of organizations, there are a wide variety of ways
to use the Framework. The decision about how to apply it is left to the implementing
organization. For example, one organization may choose to use the Framework Implementation
Tiers to articulate envisioned risk management practices. Another organization may use the
Framework’s five Functions to analyze its entire risk management portfolio; that analysis may or
may not rely on more detailed companion guidance, such as controls catalogs. There sometimes
is discussion about “compliance” with the Framework, and the Framework has utility as a
structure and language for organizing and expressing compliance with an organization’s own
cybersecurity requirements. Nevertheless, the variety of ways in which the Framework can be
used by an organization means that phrases like “compliance with the Framework” can be
confusing and mean something very different to various stakeholders.

The Framework complements, and does not replace, an organization’s risk management process
and cybersecurity program. The organization can use its current processes and leverage the
Framework to identify opportunities to strengthen and communicate its management of
cybersecurity risk while aligning with industry practices. Alternatively, an organization without
an existing cybersecurity program can use the Framework as a reference to establish one.

While the Framework has been developed to improve cybersecurity risk management as it relates
to critical infrastructure, it can be used by organizations in any sector of the economy or society.
It is intended to be useful to companies, government agencies, and not-for-profit organizations
regardless of their focus or size. The common taxonomy of standards, guidelines, and practices
that it provides also is not country-specific. Organizations outside the United States may also use
the Framework to strengthen their own cybersecurity efforts, and the Framework can contribute
to developing a common language for international cooperation on critical infrastructure
cybersecurity.

1.1  Overview of the Framework

The Framework is a risk-based approach to managing cybersecurity risk, and is composed of
three parts: the Framework Core, the Framework Implementation Tiers, and the Framework
Profiles. Each Framework component reinforces the connection between business/mission
drivers and cybersecurity activities. These components are explained below.

  The Framework Core is a set of cybersecurity activities, desired outcomes, and

applicable references that are common across critical infrastructure sectors. The Core
presents industry standards, guidelines, and practices in a manner that allows for
communication of cybersecurity activities and outcomes across the organization from the
executive level to the implementation/operations level. The Framework Core consists of
five concurrent and continuous Functions—Identify, Protect, Detect, Respond, Recover.
When considered together, these Functions provide a high-level, strategic view of the
lifecycle of an organization’s management of cybersecurity risk. The Framework Core
then identifies underlying key Categories and Subcategories – which are discrete
outcomes – for each Function, and matches them with example Informative References
such as existing standards, guidelines, and practices for each Subcategory.

  Framework Implementation Tiers (“Tiers”) provide context on how an organization

views cybersecurity risk and the processes in place to manage that risk. Tiers describe the
degree to which an organization’s cybersecurity risk management practices exhibit the

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

 3

April 16, 2018

Cybersecurity Framework

Version 1.1

characteristics defined in the Framework (e.g., risk and threat aware, repeatable, and
adaptive). The Tiers characterize an organization’s practices over a range, from Partial
(Tier 1) to Adaptive (Tier 4). These Tiers reflect a progression from informal, reactive
responses to approaches that are agile and risk-informed. During the Tier selection
process, an organization should consider its current risk management practices, threat
environment, legal and regulatory requirements, business/mission objectives, and
organizational constraints.

  A Framework Profile (“Profile”) represents the outcomes based on business needs that an
organization has selected from the Framework Categories and Subcategories. The Profile
can be characterized as the alignment of standards, guidelines, and practices to the
Framework Core in a particular implementation scenario. Profiles can be used to identify
opportunities for improving cybersecurity posture by comparing a “Current” Profile (the
“as is” state) with a “Target” Profile (the “to be” state). To develop a Profile, an
organization can review all of the Categories and Subcategories and, based on
business/mission drivers and a risk assessment, determine which are most important; it
can add Categories and Subcategories as needed to address the organization’s risks. The
Current Profile can then be used to support prioritization and measurement of progress
toward the Target Profile, while factoring in other business needs including cost-
effectiveness and innovation. Profiles can be used to conduct self-assessments and
communicate within an organization or between organizations.

1.2  Risk Manageme nt and the Cybersecurity Framework

Risk management is the ongoing process of identifying, assessing, and responding to risk. To
manage risk, organizations should understand the likelihood that an event will occur and the
potential resulting impacts. With this information, organizations can determine the acceptable
level of risk for achieving their organizational objectives and can express this as their risk
tolerance.

With an understanding of risk tolerance, organizations can prioritize cybersecurity activities,
enabling organizations to make informed decisions about cybersecurity expenditures.
Implementation of risk management programs offers organizations the ability to quantify and
communicate adjustments to their cybersecurity programs. Organizations may choose to handle
risk in different ways, including mitigating the risk, transferring the risk, avoiding the risk, or
accepting the risk, depending on the potential impact to the delivery of critical services. The
Framework uses risk management processes to enable organizations to inform and prioritize
decisions regarding cybersecurity. It supports recurring risk assessments and validation of
business drivers to help organizations select target states for cybersecurity activities that reflect
desired outcomes. Thus, the Framework gives organizations the ability to dynamically select and
direct improvement in cybersecurity risk management for the IT and ICS environments.

The Framework is adaptive to provide a flexible and risk-based implementation that can be used
with a broad array of cybersecurity risk management processes. Examples of cybersecurity risk
management processes include International Organization for Standardization (ISO)

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

 4

April 16, 2018

Cybersecurity Framework

Version 1.1

31000:20096, ISO/International Electrotechnical Commission (IEC) 27005:20117, NIST Special
Publication (SP) 800-398, and the Electricity Subsector Cybersecurity Risk Management Process
(RMP) guideline9.

1.3  Docume nt Overview

The remainder of this document contains the following sections and appendices:

  Section 2 describes the Framework components: the Framework Core, the Tiers, and the

Profiles.

  Section 3 presents examples of how the Framework can be used.
  Section 4 describes how to use the Framework for self-assessing and demonstrating

cybersecurity through measurements.

  Appendix A presents the Framework Core in a tabular format: the Functions, Categories,

Subcategories, and Informative References.

  Appendix B contains a glossary of selected terms.
  Appendix C lists acronyms used in this document.

6   International Organization for Standardization, Risk management – Principles and guidelines, ISO 31000:2009,

2009. http://www.iso.org/iso/home/standards/iso31000.htm

7   International Organization for Standardization/International Electrotechnical Commission, Information
technology – Security techniques – Information security risk management, ISO/IEC 27005:2011, 2011.
https://www.iso.org/standard/56742.html

8   Joint Task Force Transformation Initiative, Managing Information Security Risk: Organization, Mission, and

Information System View, NIST Special Publication 800-39, March 2011. https://doi.org/10.6028/NIST.SP.800-
39

9   U.S. Department of Energy, Electricity Subsector Cybersecurity Risk Management Process, DOE/OE-0003, May

2012. https://energy.gov/sites/prod/files/Cybersecurity Risk Management Process Guideline - Final - May
2012.pdf

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

 5

April 16, 2018

Cybersecurity Framework

Version 1.1

2.0  Framework Basics

The Framework provides a common language for understanding, managing, and expressing
cybersecurity risk to internal and external stakeholders. It can be used to help identify and
prioritize actions for reducing cybersecurity risk, and it is a tool for aligning policy, business, and
technological approaches to managing that risk. It can be used to manage cybersecurity risk
across entire organizations or it can be focused on the delivery of critical services within an
organization. Different types of entities – including sector coordinating structures, associations,
and organizations – can use the Framework for different purposes, including the creation of
common Profiles.

2.1  Framework Core

The Framework Core provides a set of activities to achieve specific cybersecurity outcomes, and
references examples of guidance to achieve those outcomes. The Core is not a checklist of
actions to perform. It presents key cybersecurity outcomes identified by stakeholders as helpful
in managing cybersecurity risk. The Core comprises four elements: Functions, Categories,
Subcategories, and Informative References, depicted in Figure 1:

The Framework Core elements work together as follows:

Figure 1: Framework Core Structure

  Functions organize basic cybersecurity activities at their highest level. These Functions

are Identify, Protect, Detect, Respond, and Recover. They aid an organization in
expressing its management of cybersecurity risk by organizing information, enabling risk
management decisions, addressing threats, and improving by learning from previous
activities. The Functions also align with existing methodologies for incident management
and help show the impact of investments in cybersecurity. For example, investments in
planning and exercises support timely response and recovery actions, resulting in reduced
impact to the delivery of services.

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

 6

April 16, 2018

Cybersecurity Framework

Version 1.1

  Categories are the subdivisions of a Function into groups of cybersecurity outcomes
closely tied to programmatic needs and particular activities. Examples of Categories
include “Asset Management,” “Identity Management and Access Control,” and
“Detection Processes.”

  Subcategories further divide a Category into specific outcomes of technical and/or
management activities. They provide a set of results that, while not exhaustive, help
support achievement of the outcomes in each Category. Examples of Subcategories
include “External information systems are catalogued,” “Data-at-rest is protected,” and
“Notifications from detection systems are investigated.”

  Informative References are specific sections of standards, guidelines, and practices
common among critical infrastructure sectors that illustrate a method to achieve the
outcomes associated with each Subcategory. The Informative References presented in the
Framework Core are illustrative and not exhaustive. They are based upon cross-sector
guidance most frequently referenced during the Framework development process.

The five Framework Core Functions are defined below. These Functions are not intended to
form a serial path or lead to a static desired end state. Rather, the Functions should be performed
concurrently and continuously to form an operational culture that addresses the dynamic
cybersecurity risk. See Appendix A for the complete Framework Core listing.

  Identify – Develop an organizational understanding to manage cybersecurity risk to

systems, people, assets, data, and capabilities.

The activities in the Identify Function are foundational for effective use of the
Framework. Understanding the business context, the resources that support critical
functions, and the related cybersecurity risks enables an organization to focus and
prioritize its efforts, consistent with its risk management strategy and business needs.
Examples of outcome Categories within this Function include: Asset Management;
Business Environment; Governance; Risk Assessment; and Risk Management Strategy.

  Protect – Develop and implement appropriate safeguards to ensure delivery of critical

services.

The Protect Function supports the ability to limit or contain the impact of a potential
cybersecurity event. Examples of outcome Categories within this Function include:
Identity Management and Access Control; Awareness and Training; Data Security;
Information Protection Processes and Procedures; Maintenance; and Protective
Technology.

  Detect – Develop and implement appropriate activities to identify the occurrence of a

cybersecurity event.

The Detect Function enables timely discovery of cybersecurity events. Examples of
outcome Categories within this Function include: Anomalies and Events; Security
Continuous Monitoring; and Detection Processes.

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

 7

April 16, 2018

Cybersecurity Framework

Version 1.1

  Respond – Develop and implement appropriate activities to take action regarding a

detected cybersecurity incident.

The Respond Function supports the ability to contain the impact of a potential
cybersecurity incident. Examples of outcome Categories within this Function include:
Response Planning; Communications; Analysis; Mitigation; and Improvements.

  Recover – Develop and implement appropriate activities to maintain plans for resilience
and to restore any capabilities or services that were impaired due to a cybersecurity
incident.

The Recover Function supports timely recovery to normal operations to reduce the
impact from a cybersecurity incident. Examples of outcome Categories within this
Function include: Recovery Planning; Improvements; and Communications.

2.2  Framework Implementation  Tiers

The Framework Implementation Tiers (“Tiers”) provide context on how an organization views
cybersecurity risk and the processes in place to manage that risk. Ranging from Partial (Tier 1) to
Adaptive (Tier 4), Tiers describe an increasing degree of rigor and sophistication in
cybersecurity risk management practices. They help determine the extent to which cybersecurity
risk management is informed by business needs and is integrated into an organization’s overall
risk management practices. Risk management considerations include many aspects of
cybersecurity, including the degree to which privacy and civil liberties considerations are
integrated into an organization’s management of cybersecurity risk and potential risk responses.

The Tier selection process considers an organization’s current risk management practices, threat
environment, legal and regulatory requirements, information sharing practices, business/mission
objectives, supply chain cybersecurity requirements, and organizational constraints.
Organizations should determine the desired Tier, ensuring that the selected level meets the
organizational goals, is feasible to implement, and reduces cybersecurity risk to critical assets
and resources to levels acceptable to the organization. Organizations should consider leveraging
external guidance obtained from Federal government departments and agencies, Information
Sharing and Analysis Centers (ISACs), Information Sharing and Analysis Organizations
(ISAOs), existing maturity models, or other sources to assist in determining their desired tier.

While organizations identified as Tier 1 (Partial) are encouraged to consider moving toward Tier
2 or greater, Tiers do not represent maturity levels. Tiers are meant to support organizational
decision making about how to manage cybersecurity risk, as well as which dimensions of the
organization are higher priority and could receive additional resources. Progression to higher
Tiers is encouraged when a cost-benefit analysis indicates a feasible and cost-effective reduction
of cybersecurity risk.

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

 8

April 16, 2018

Cybersecurity Framework

Version 1.1

Successful implementation of the Framework is based upon achieving the outcomes described in
the organization’s Target Profile(s) and not upon Tier determination. Still, Tier selection and
designation naturally affect Framework Profiles. The Tier recommendation by Business/Process
Level managers, as approved by the Senior Executive Level, will help set the overall tone for
how cybersecurity risk will be managed within the organization, and should influence
prioritization within a Target Profile and assessments of progress in addressing gaps.

The Tier definitions are as follows:

Tier 1: Partial

  Risk Management Process – Organizational cybersecurity risk management practices are

not formalized, and risk is managed in an ad hoc and sometimes reactive manner.
Prioritization of cybersecurity activities may not be directly informed by organizational
risk objectives, the threat environment, or business/mission requirements.



Integrated Risk Management Program – There is limited awareness of cybersecurity risk
at the organizational level. The organization implements cybersecurity risk management
on an irregular, case-by-case basis due to varied experience or information gained from
outside sources. The organization may not have processes that enable cybersecurity
information to be shared within the organization.

  External Participation – The organization does not understand its role in the larger

ecosystem with respect to either its dependencies or dependents. The organization does
not collaborate with or receive information (e.g., threat intelligence, best practices,
technologies) from other entities (e.g., buyers, suppliers, dependencies, dependents,
ISAOs, researchers, governments), nor does it share information. The organization is
generally unaware of the cyber supply chain risks of the products and services it provides
and that it uses.

Tier 2: Risk Informed

  Risk Management Process – Risk management practices are approved by management

but may not be established as organizational-wide policy. Prioritization of cybersecurity
activities and protection needs is directly informed by organizational risk objectives, the
threat environment, or business/mission requirements.



Integrated Risk Management Program – There is an awareness of cybersecurity risk at
the organizational level, but an organization-wide approach to managing cybersecurity
risk has not been established. Cybersecurity information is shared within the organization
on an informal basis. Consideration of cybersecurity in organizational objectives and
programs may occur at some but not all levels of the organization. Cyber risk assessment
of organizational and external assets occurs, but is not typically repeatable or reoccurring.

  External Participation – Generally, the organization understands its role in the larger

ecosystem with respect to either its own dependencies or dependents, but not both. The
organization collaborates with and receives some information from other entities and
generates some of its own information, but may not share information with others.
Additionally, the organization is aware of the cyber supply chain risks associated with
the products and services it provides and uses, but does not act consistently or formally
upon those risks.

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

 9

April 16, 2018

Cybersecurity Framework

Version 1.1

Tier 3: Repeatable

  Risk Management Process – The organization’s risk management practices are formally
approved and expressed as policy. Organizational cybersecurity practices are regularly
updated based on the application of risk management processes to changes in
business/mission requirements and a changing threat and technology landscape.



Integrated Risk Management Program – There is an organization-wide approach to
manage cybersecurity risk. Risk-informed policies, processes, and procedures are
defined, implemented as intended, and reviewed. Consistent methods are in place to
respond effectively to changes in risk. Personnel possess the knowledge and skills to
perform their appointed roles and responsibilities. The organization consistently and
accurately monitors cybersecurity risk of organizational assets. Senior cybersecurity and
non-cybersecurity executives communicate regularly regarding cybersecurity risk.
Senior executives ensure consideration of cybersecurity through all lines of operation in
the organization.

  External Participation - The organization understands its role, dependencies, and

dependents in the larger ecosystem and may contribute to the community’s broader
understanding of risks. It collaborates with and receives information from other entities
regularly that complements internally generated information, and shares information
with other entities. The organization is aware of the cyber supply chain risks associated
with the products and services it provides and that it uses. Additionally, it usually acts
formally upon those risks, including mechanisms such as written agreements to
communicate baseline requirements, governance structures (e.g., risk councils), and
policy implementation and monitoring.

Tier 4: Adaptive

  Risk Management Process – The organization adapts its cybersecurity practices based on
previous and current cybersecurity activities, including lessons learned and predictive
indicators. Through a process of continuous improvement incorporating advanced
cybersecurity technologies and practices, the organization actively adapts to a changing
threat and technology landscape and responds in a timely and effective manner to
evolving, sophisticated threats.



Integrated Risk Management Program – There is an organization-wide approach to
managing cybersecurity risk that uses risk-informed policies, processes, and procedures
to address potential cybersecurity events. The relationship between cybersecurity risk and
organizational objectives is clearly understood and considered when making decisions.
Senior executives monitor cybersecurity risk in the same context as financial risk and
other organizational risks. The organizational budget is based on an understanding of the
current and predicted risk environment and risk tolerance. Business units implement
executive vision and analyze system-level risks in the context of the organizational risk
tolerances. Cybersecurity risk management is part of the organizational culture and
evolves from an awareness of previous activities and continuous awareness of activities
on their systems and networks. The organization can quickly and efficiently account for
changes to business/mission objectives in how risk is approached and communicated.

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

 10

April 16, 2018

Cybersecurity Framework

Version 1.1

  External Participation - The organization understands its role, dependencies, and
dependents in the larger ecosystem and contributes to the community’s broader
understanding of risks. It receives, generates, and reviews prioritized information that
informs continuous analysis of its risks as the threat and technology landscapes evolve.
The organization shares that information internally and externally with other
collaborators. The organization uses real-time or near real-time information to understand
and consistently act upon cyber supply chain risks associated with the products and
services it provides and that it uses. Additionally, it communicates proactively, using
formal (e.g. agreements) and informal mechanisms to develop and maintain strong supply
chain relationships.

2.3  Framework Profile

The Framework Profile (“Profile”) is the alignment of the Functions, Categories, and
Subcategories with the business requirements, risk tolerance, and resources of the organization.
A Profile enables organizations to establish a roadmap for reducing cybersecurity risk that is well
aligned with organizational and sector goals, considers legal/regulatory requirements and
industry best practices, and reflects risk management priorities. Given the complexity of many
organizations, they may choose to have multiple profiles, aligned with particular components and
recognizing their individual needs.

Framework Profiles can be used to describe the current state or the desired target state of specific
cybersecurity activities. The Current Profile indicates the cybersecurity outcomes that are
currently being achieved. The Target Profile indicates the outcomes needed to achieve the
desired cybersecurity risk management goals. Profiles support business/mission requirements
and aid in communicating risk within and between organizations. This Framework does not
prescribe Profile templates, allowing for flexibility in implementation.

Comparison of Profiles (e.g., the Current Profile and Target Profile) may reveal gaps to be
addressed to meet cybersecurity risk management objectives. An action plan to address these
gaps to fulfill a given Category or Subcategory can contribute to the roadmap described above.
Prioritizing the mitigation of gaps is driven by the organization’s business needs and risk
management processes. This risk-based approach enables an organization to gauge the resources
needed (e.g., staffing, funding) to achieve cybersecurity goals in a cost-effective, prioritized
manner. Furthermore, the Framework is a risk-based approach where the applicability and
fulfillment of a given Subcategory is subject to the Profile’s scope.

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

 11

April 16, 2018

Cybersecurity Framework

Version 1.1

2.4  Coordi nation of F ramework Implementation

Figure 2 describes a common flow of information and decisions at the following levels within an
organization:

  Executive
  Business/Process


Implementation/Operations

The executive level communicates the mission priorities, available resources, and overall risk
tolerance to the business/process level. The business/process level uses the information as inputs
into the risk management process, and then collaborates with the implementation/operations
level to communicate business needs and create a Profile. The implementation/operations level
communicates the Profile implementation progress to the business/process level. The
business/process level uses this information to perform an impact assessment. Business/process
level management reports the outcomes of that impact assessment to the executive level to
inform the organization’s overall risk management process and to the implementation/operations
level for awareness of business impact.

Figure 2: Notional Information and Decision Flows within an Organization

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

 12

April 16, 2018

Cybersecurity Framework

Version 1.1

3.0  How to Use the Framework

An organization can use the Framework as a key part of its systematic process for identifying,
assessing, and managing cybersecurity risk. The Framework is not designed to replace existing
processes; an organization can use its current process and overlay it onto the Framework to
determine gaps in its current cybersecurity risk approach and develop a roadmap to
improvement. Using the Framework as a cybersecurity risk management tool, an organization
can determine activities that are most important to critical service delivery and prioritize
expenditures to maximize the impact of the investment.

The Framework is designed to complement existing business and cybersecurity operations. It can
serve as the foundation for a new cybersecurity program or a mechanism for improving an
existing program. The Framework provides a means of expressing cybersecurity requirements to
business partners and customers and can help identify gaps in an organization’s cybersecurity
practices. It also provides a general set of considerations and processes for considering privacy
and civil liberties implications in the context of a cybersecurity program.

The Framework can be applied throughout the life cycle phases of plan, design, build/buy,
deploy, operate, and decommission. The plan phase begins the cycle of any system and lays the
groundwork for everything that follows. Overarching cybersecurity considerations should be
declared and described as clearly as possible. The plan should recognize that those
considerations and requirements are likely to evolve during the remainder of the life cycle. The
design phase should account for cybersecurity requirements as a part of a larger multi-
disciplinary systems engineering process.10 A key milestone of the design phase is validation that
the system cybersecurity specifications match the needs and risk disposition of the organization
as captured in a Framework Profile. The desired cybersecurity outcomes prioritized in a Target
Profile should be incorporated when a) developing the system during the build phase and b)
purchasing or outsourcing the system during the buy phase. That same Target Profile serves as a
list of system cybersecurity features that should be assessed when deploying the system to verify
all features are implemented. The cybersecurity outcomes determined by using the Framework
then should serve as a basis for ongoing operation of the system. This includes occasional
reassessment, capturing results in a Current Profile, to verify that cybersecurity requirements are
still fulfilled. Typically, a complex web of dependencies (e.g., compensating and common
controls) among systems means the outcomes documented in Target Profiles of related systems
should be carefully considered as systems are decommissioned.

The following sections present different ways in which organizations can use the Framework.

3.1  Basic Review of Cybersecurity Practices

The Framework can be used to compare an organization’s current cybersecurity activities with
those outlined in the Framework Core. Through the creation of a Current Profile, organizations
can examine the extent to which they are achieving the outcomes described in the Core
Categories and Subcategories, aligned with the five high-level Functions: Identify, Protect,
Detect, Respond, and Recover. An organization may find that it is already achieving the desired

10 NIST Special Publication 800-160 Volume 1, System Security Engineering, Considerations for a
Multidisciplinary Approach in the Engineering of Trustworthy Secure Systems, Ross et al, November 2016 (updated
March 21, 2018), https://doi.org/10.6028/NIST.SP.800-160v1

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

 13

April 16, 2018

Cybersecurity Framework

Version 1.1

outcomes, thus managing cybersecurity commensurate with the known risk. Alternatively, an
organization may determine that it has opportunities to (or needs to) improve. The organization
can use that information to develop an action plan to strengthen existing cybersecurity practices
and reduce cybersecurity risk. An organization may also find that it is overinvesting to achieve
certain outcomes. The organization can use this information to reprioritize resources.

While they do not replace a risk management process, these five high-level Functions will
provide a concise way for senior executives and others to distill the fundamental concepts of
cybersecurity risk so that they can assess how identified risks are managed, and how their
organization stacks up at a high level against existing cybersecurity standards, guidelines, and
practices. The Framework can also help an organization answer fundamental questions,
including “How are we doing?” Then they can move in a more informed way to strengthen their
cybersecurity practices where and when deemed necessary.

3.2   Establishing or Improving a Cybersecurity Program

The following steps illustrate how an organization could use the Framework to create a new
cybersecurity program or improve an existing program. These steps should be repeated as
necessary to continuously improve cybersecurity.

Step 1: Prioritize and Scope. The organization identifies its business/mission objectives and
high-level organizational priorities. With this information, the organization makes strategic
decisions regarding cybersecurity implementations and determines the scope of systems and
assets that support the selected business line or process. The Framework can be adapted to
support the different business lines or processes within an organization, which may have
different business needs and associated risk tolerance. Risk tolerances may be reflected in a
target Implementation Tier.

Step 2: Orient. Once the scope of the cybersecurity program has been determined for the
business line or process, the organization identifies related systems and assets, regulatory
requirements, and overall risk approach. The organization then consults sources to identify
threats and vulnerabilities applicable to those systems and assets.

Step 3: Create a Current Profile. The organization develops a Current Profile by indicating
which Category and Subcategory outcomes from the Framework Core are currently being
achieved. If an outcome is partially achieved, noting this fact will help support subsequent steps
by providing baseline information.

Step 4: Conduct a Risk Assessment. This assessment could be guided by the organization’s
overall risk management process or previous risk assessment activities. The organization
analyzes the operational environment in order to discern the likelihood of a cybersecurity event
and the impact that the event could have on the organization. It is important that organizations
identify emerging risks and use cyber threat information from internal and external sources to
gain a better understanding of the likelihood and impact of cybersecurity events.

Step 5: Create a Target Profile. The organization creates a Target Profile that focuses on the
assessment of the Framework Categories and Subcategories describing the organization’s desired
cybersecurity outcomes. Organizations also may develop their own additional Categories and

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

 14

April 16, 2018

Cybersecurity Framework

Version 1.1

Subcategories to account for unique organizational risks. The organization may also consider
influences and requirements of external stakeholders such as sector entities, customers, and
business partners when creating a Target Profile. The Target Profile should appropriately reflect
criteria within the target Implementation Tier.

Step 6: Determine, Analyze, and Prioritize Gaps. The organization compares the Current
Profile and the Target Profile to determine gaps. Next, it creates a prioritized action plan to
address gaps – reflecting mission drivers, costs and benefits, and risks – to achieve the outcomes
in the Target Profile. The organization then determines resources, including funding and
workforce, necessary to address the gaps. Using Profiles in this manner encourages the
organization to make informed decisions about cybersecurity activities, supports risk
management, and enables the organization to perform cost-effective, targeted improvements.

Step 7: Implement Action Plan. The organization determines which actions to take to address
the gaps, if any, identified in the previous step and then adjusts its current cybersecurity practices
in order to achieve the Target Profile. For further guidance, the Framework identifies example
Informative References regarding the Categories and Subcategories, but organizations should
determine which standards, guidelines, and practices, including those that are sector specific,
work best for their needs.

An organization repeats the steps as needed to continuously assess and improve its cybersecurity.
For instance, organizations may find that more frequent repetition of the orient step improves the
quality of risk assessments. Furthermore, organizations may monitor progress through iterative
updates to the Current Profile, subsequently comparing the Current Profile to the Target Profile.
Organizations may also use this process to align their cybersecurity program with their desired
Framework Implementation Tier.

3.3  Communicating Cybersecurity Requirements with Stakeholders

The Framework provides a common language to communicate requirements among
interdependent stakeholders responsible for the delivery of essential critical infrastructure
products and services. Examples include:

  An organization may use a Target Profile to express cybersecurity risk management
requirements to an external service provider (e.g., a cloud provider to which it is
exporting data).

  An organization may express its cybersecurity state through a Current Profile to report

results or to compare with acquisition requirements.

  A critical infrastructure owner/operator, having identified an external partner on whom
that infrastructure depends, may use a Target Profile to convey required Categories and
Subcategories.

  A critical infrastructure sector may establish a Target Profile that can be used among its

constituents as an initial baseline Profile to build their tailored Target Profiles.

  An organization can better manage cybersecurity risk among stakeholders by assessing

their position in the critical infrastructure and the broader digital economy using
Implementation Tiers.

Communication is especially important among stakeholders up and down supply chains. Supply
chains are complex, globally distributed, and interconnected sets of resources and processes

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

 15

April 16, 2018

Cybersecurity Framework

Version 1.1

between multiple levels of organizations. Supply chains begin with the sourcing of products and
services and extend from the design, development, manufacturing, processing, handling, and
delivery of products and services to the end user. Given these complex and interconnected
relationships, supply chain risk management (SCRM) is a critical organizational function.11

Cyber SCRM is the set of activities necessary to manage cybersecurity risk associated with
external parties. More specifically, cyber SCRM addresses both the cybersecurity effect an
organization has on external parties and the cybersecurity effect external parties have on an
organization.

A primary objective of cyber SCRM is to identify, assess, and mitigate “products and services
that may contain potentially malicious functionality, are counterfeit, or are vulnerable due to
poor manufacturing and development practices within the cyber supply chain12.” Cyber SCRM
activities may include:

  Determining cybersecurity requirements for suppliers,
  Enacting cybersecurity requirements through formal agreement (e.g., contracts),
  Communicating to suppliers how those cybersecurity requirements will be verified

and validated,

  Verifying that cybersecurity requirements are met through a variety of assessment

methodologies, and

  Governing and managing the above activities.

As depicted in Figure 3, cyber SCRM encompasses technology suppliers and buyers, as well as
non-technology suppliers and buyers, where technology is minimally composed of information
technology (IT), industrial control systems (ICS), cyber-physical systems (CPS), and connected
devices more generally, including the Internet of Things (IoT). Figure 3 depicts an organization
at a single point in time. However, through the normal course of business operations, most
organizations will be both an upstream supplier and downstream buyer in relation to other
organizations or end users.

11 Communicating Cybersecurity Requirements (Section 3.3) and Buying Decisions (Section 3.4) address only two
uses of the Framework for cyber SCRM and are not intended to address cyber SCRM comprehensively.

12 NIST Special Publication 800-161, Supply Chain Risk Management Practices for Federal Information Systems
and Organizations, Boyens et al, April 2015, https://doi.org/10.6028/NIST.SP.800-161

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

 16

April 16, 2018

Cybersecurity Framework

Version 1.1

Figure 3: Cyber Supply Chain Relationships

The parties described in Figure 3 comprise an organization’s cybersecurity ecosystem. These
relationships highlight the crucial role of cyber SCRM in addressing cybersecurity risk in critical
infrastructure and the broader digital economy. These relationships, the products and services
they provide, and the risks they present should be identified and factored into the protective and
detective capabilities of organizations, as well as their response and recovery protocols.

In the figure above, “Buyer” refers to the downstream people or organizations that consume a
given product or service from an organization, including both for-profit and not-for-profit
organizations. “Supplier” encompasses upstream product and service providers that are used for
an organization’s internal purposes (e.g., IT infrastructure) or integrated into the products or
services provided to the Buyer.  These terms are applicable for both technology-based and non-
technology-based products and services.

Whether considering individual Subcategories of the Core or the comprehensive considerations
of a Profile, the Framework offers organizations and their partners a method to help ensure the
new product or service meets critical security outcomes. By first selecting outcomes that are
relevant to the context (e.g., transmission of Personally Identifiable Information (PII), mission
critical service delivery, data verification services, product or service integrity) the organization
then can evaluate partners against those criteria. For example, if a system is being purchased that
will monitor Operational Technology (OT) for anomalous network communication, availability
may be a particularly important cybersecurity objective to achieve and should drive a
Technology Supplier evaluation against applicable Subcategories (e.g., ID.BE-4, ID.SC-3,
ID.SC-4, ID.SC-5, PR.DS-4, PR.DS-6, PR.DS-7, PR.DS-8, PR.IP-1, DE.AE-5).

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

 17

April 16, 2018

Cybersecurity Framework

Version 1.1

3.4   Buying Decisions

Since a Framework Target Profile is a prioritized list of organizational cybersecurity
requirements, Target Profiles can be used to inform decisions about buying products and
services. This transaction varies from Communicating Cybersecurity Requirements with
Stakeholders (addressed in Section 3.3) in that it may not be possible to impose a set of
cybersecurity requirements on the supplier. The objective should be to make the best buying
decision among multiple suppliers, given a carefully determined list of cybersecurity
requirements. Often, this means some degree of trade-off, comparing multiple products or
services with known gaps to the Target Profile.

Once a product or service is purchased, the Profile also can be used to track and address residual
cybersecurity risk. For example, if the service or product purchased did not meet all the
objectives described in the Target Profile, the organization can address the residual risk through
other management actions. The Profile also provides the organization a method for assessing if
the product meets cybersecurity outcomes through periodic review and testing mechanisms.

Identifying Opportunities for New or Revised Informative

3.5
References

The Framework can be used to identify opportunities for new or revised standards, guidelines, or
practices where additional Informative References would help organizations address emerging
needs. An organization implementing a given Subcategory, or developing a new Subcategory,
might discover that there are few Informative References, if any, for a related activity. To
address that need, the organization might collaborate with technology leaders and/or standards
bodies to draft, develop, and coordinate standards, guidelines, or practices.

3.6   Methodology to Protect  Privacy and Civil Libert ies

This section describes a methodology to address individual privacy and civil liberties
implications that may result from cybersecurity. This methodology is intended to be a general set
of considerations and processes since privacy and civil liberties implications may differ by sector
or over time and organizations may address these considerations and processes with a range of
technical implementations. Nonetheless, not all activities in a cybersecurity program engender
privacy and civil liberties considerations. Technical privacy standards, guidelines, and additional
best practices may need to be developed to support improved technical implementations.

Privacy and cybersecurity have a strong connection. An organization’s cybersecurity activities
also can create risks to privacy and civil liberties when personal information is used, collected,
processed, maintained, or disclosed. Some examples include: cybersecurity activities that result
in the over-collection or over-retention of personal information; disclosure or use of personal
information unrelated to cybersecurity activities; and cybersecurity mitigation activities that
result in denial of service or other similar potentially adverse impacts, including some types of
incident detection or monitoring that may inhibit freedom of expression or association.

The government and its agents have a responsibility to protect civil liberties arising from
cybersecurity activities. As referenced in the methodology below, government or its agents that
own or operate critical infrastructure should have a process in place to support compliance of
cybersecurity activities with applicable privacy laws, regulations, and Constitutional
requirements.

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

 18

April 16, 2018

Cybersecurity Framework

Version 1.1

To address privacy implications, organizations may consider how their cybersecurity program
might incorporate privacy principles such as: data minimization in the collection, disclosure, and
retention of personal information material related to the cybersecurity incident; use limitations
outside of cybersecurity activities on any information collected specifically for cybersecurity
activities; transparency for certain cybersecurity activities; individual consent and redress for
adverse impacts arising from use of personal information in cybersecurity activities; data quality,
integrity, and security; and accountability and auditing.

As organizations assess the Framework Core in Appendix A, the following processes and
activities may be considered as a means to address the above-referenced privacy and civil
liberties implications:

Governance of cybersecurity risk

  An organization’s assessment of cybersecurity risk and potential risk responses considers



the privacy implications of its cybersecurity program.
Individuals with cybersecurity-related privacy responsibilities report to appropriate
management and are appropriately trained.

  Process is in place to support compliance of cybersecurity activities with applicable

privacy laws, regulations, and Constitutional requirements.

  Process is in place to assess implementation of the above organizational measures and

controls.

Approaches to identifying, authenticating, and authorizing individuals to access
organizational assets and systems

  Steps are taken to identify and address the privacy implications of identity management
and access control measures to the extent that they involve collection, disclosure, or use
of personal information.

Awareness and training measures

  Applicable information from organizational privacy policies is included in cybersecurity

workforce training and awareness activities.

  Service providers that provide cybersecurity-related services for the organization are

informed about the organization’s applicable privacy policies.

Anomalous activity detection and system and assets monitoring

  Process is in place to conduct a privacy review of an organization’s anomalous activity

detection and cybersecurity monitoring.

Response activities, including information sharing or other mitigation efforts

  Process is in place to assess and address whether, when, how, and the extent to which

personal information is shared outside the organization as part of cybersecurity
information sharing activities.

  Process is in place to conduct a privacy review of an organization’s cybersecurity

mitigation efforts.

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

 19

April 16, 2018

Cybersecurity Framework

Version 1.1

4.0  Self-Assessing Cybersecurity Risk with the Framework

The Cybersecurity Framework is designed to reduce risk by improving the management of
cybersecurity risk to organizational objectives. Ideally, organizations using the Framework will
be able to measure and assign values to their risk along with the cost and benefits of steps taken
to reduce risk to acceptable levels. The better an organization is able to measure its risk, costs,
and benefits of cybersecurity strategies and steps, the more rational, effective, and valuable its
cybersecurity approach and investments will be.

Over time, self-assessment and measurement should improve decision making about investment
priorities. For example, measuring – or at least robustly characterizing – aspects of an
organization’s cybersecurity state and trends over time can enable that organization to
understand and convey meaningful risk information to dependents, suppliers, buyers, and other
parties. An organization can accomplish this internally or by seeking a third-party assessment. If
done properly and with an appreciation of limitations, these measurements can provide a basis
for strong trusted relationships, both inside and outside of an organization.

To examine the effectiveness of investments, an organization must first have a clear
understanding of its organizational objectives, the relationship between those objectives and
supportive cybersecurity outcomes, and how those discrete cybersecurity outcomes are
implemented and managed. While measurements of all those items is beyond the scope of the
Framework, the cybersecurity outcomes of the Framework Core support self-assessment of
investment effectiveness and cybersecurity activities in the following ways:

  Making choices about how different portions of the cybersecurity operation should

influence the selection of Target Implementation Tiers,

  Evaluating the organization’s approach to cybersecurity risk management by determining

Current Implementation Tiers,

  Prioritizing cybersecurity outcomes by developing Target Profiles,
  Determining the degree to which specific cybersecurity steps achieve desired

cybersecurity outcomes by assessing Current Profiles, and

  Measuring the degree of implementation for controls catalogs or technical guidance listed

as Informative References.

The development of cybersecurity performance metrics is evolving. Organizations should be
thoughtful, creative, and careful about the ways in which they employ measurements to optimize
use, while avoiding reliance on artificial indicators of current state and progress in improving
cybersecurity risk management. Judging cyber risk requires discipline and should be revisited
periodically. Any time measurements are employed as part of the Framework process,
organizations are encouraged to clearly identify and know why these measurements are
important and how they will contribute to the overall management of cybersecurity risk. They
also should be clear about the limitations of measurements that are used.

For example, tracking security measures and business outcomes may provide meaningful insight
as to how changes in granular security controls affect the completion of organizational
objectives. Verifying achievement of some organizational objectives requires analyzing the data
only after that objective was to have been achieved. This type of lagging measure is more

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

 20

April 16, 2018

Cybersecurity Framework

Version 1.1

absolute.  However, it is often more valuable to predict whether a cybersecurity risk may occur,
and the impact it might have, using a leading measure.

Organizations are encouraged to innovate and customize how they incorporate measurements
into their application of the Framework with a full appreciation of their usefulness and
limitations.

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

 21

April 16, 2018

Cybersecurity Framework

Version 1.1

Appendix A: Framework Core

This appendix presents the Framework Core: a listing of Functions, Categories, Subcategories,
and Informative References that describe specific cybersecurity activities that are common
across all critical infrastructure sectors. The chosen presentation format for the Framework Core
does not suggest a specific implementation order or imply a degree of importance of the
Categories, Subcategories, and Informative References. The Framework Core presented in this
appendix represents a common set of activities for managing cybersecurity risk. While the
Framework is not exhaustive, it is extensible, allowing organizations, sectors, and other entities
to use Subcategories and Informative References that are cost-effective and efficient and that
enable them to manage their cybersecurity risk. Activities can be selected from the Framework
Core during the Profile creation process and additional Categories, Subcategories, and
Informative References may be added to the Profile. An organization’s risk management
processes, legal/regulatory requirements, business/mission objectives, and organizational
constraints guide the selection of these activities during Profile creation. Personal information is
considered a component of data or assets referenced in the Categories when assessing security
risks and protections.

While the intended outcomes identified in the Functions, Categories, and Subcategories are the
same for IT and ICS, the operational environments and considerations for IT and ICS differ. ICS
have a direct effect on the physical world, including potential risks to the health and safety of
individuals, and impact on the environment. Additionally, ICS have unique performance and
reliability requirements compared with IT, and the goals of safety and efficiency must be
considered when implementing cybersecurity measures.

For ease of use, each component of the Framework Core is given a unique identifier. Functions
and Categories each have a unique alphabetic identifier, as shown in Table 1. Subcategories
within each Category are referenced numerically; the unique identifier for each Subcategory is
included in Table 2.

Additional supporting material, including Informative References, relating to the Framework can
be found on the NIST website at http://www.nist.gov/cyberframework/.

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

 22

April 16, 2018

Cybersecurity Framework

Version 1.1

Table 1: Function and Category Unique Identifiers

Function
Unique
Identifier

Function

Category
Unique
Identifier

Category

ID

Identify

ID.AM

Asset Management

ID.BE

Business Environment

ID.GV

Governance

ID.RA

Risk Assessment

ID.RM

Risk Management Strategy

ID.SC

Supply Chain Risk Management

PR

Protect

PR.AC

Identity Management and Access Control

PR.AT

Awareness and Training

PR.DS

Data Security

PR.IP

Information Protection Processes and Procedures

PR.MA

Maintenance

PR.PT

Protective Technology

DE.AE

Anomalies and Events

DE.CM

Security Continuous Monitoring

DE.DP

Detection Processes

DE

Detect

RS

Respond

RS.RP

Response Planning

RS.CO

Communications

RS.AN

Analysis

RS.MI

Mitigation

RS.IM

Improvements

RC

Recover

RC.RP

Recovery Planning

RC.IM

Improvements

RC.CO

Communications

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

 23

April 16, 2018

Cybersecurity Framework

Version 1.1

Function

Category

Subcategory

Informative References

Table 2: Framework Core

IDENTIFY
(ID)

Asset Management (ID.AM):
The data, personnel, devices,
systems, and facilities that enable
the organization to achieve
business purposes are identified
and managed consistent with their
relative importance to
organizational objectives and the
organization’s risk strategy.

ID.AM-1: Physical devices and systems
within the organization are inventoried

ID.AM-2: Software platforms and
applications within the organization are
inventoried

ID.AM-3: Organizational communication
and data flows are mapped

CIS CSC 1
COBIT 5 BAI09.01, BAI09.02
ISA 62443-2-1:2009 4.2.3.4
ISA 62443-3-3:2013 SR 7.8
ISO/IEC 27001:2013 A.8.1.1, A.8.1.2
NIST SP 800-53 Rev. 4 CM-8, PM-5

CIS CSC 2
COBIT 5 BAI09.01, BAI09.02, BAI09.05
ISA 62443-2-1:2009 4.2.3.4
ISA 62443-3-3:2013 SR 7.8
ISO/IEC 27001:2013 A.8.1.1, A.8.1.2, A.12.5.1
NIST SP 800-53 Rev. 4 CM-8, PM-5

CIS CSC 12
COBIT 5 DSS05.02
ISA 62443-2-1:2009 4.2.3.4
ISO/IEC 27001:2013 A.13.2.1, A.13.2.2
NIST SP 800-53 Rev. 4 AC-4, CA-3, CA-9, PL-8

ID.AM-4: External information systems
are catalogued
1.
2.
3.

CIS CSC 12
COBIT 5 APO02.02, APO10.04, DSS01.02
ISO/IEC 27001:2013 A.11.2.6
NIST SP 800-53 Rev. 4 AC-20, SA-9

ID.AM-5: Resources (e.g., hardware,
devices, data, time, personnel, and
software) are prioritized based on their
classification, criticality, and business
value

ID.AM-6: Cybersecurity roles and
responsibilities for the entire workforce and

CIS CSC 13, 14
COBIT 5 APO03.03, APO03.04, APO12.01,
BAI04.02, BAI09.02
ISA 62443-2-1:2009 4.2.3.6
ISO/IEC 27001:2013 A.8.2.1
NIST SP 800-53 Rev. 4 CP-2, RA-2, SA-14, SC-6

CIS CSC 17, 19
COBIT 5 APO01.02, APO07.06, APO13.01,
DSS06.03

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

24

April 16, 2018

Cybersecurity Framework

Version 1.1

Function

Category

Subcategory

Informative References

Business Environment (ID.BE):
The organization’s mission,
objectives, stakeholders, and
activities are understood and
prioritized; this information is
used to inform cybersecurity
roles, responsibilities, and risk
management decisions.

third-party stakeholders (e.g., suppliers,
customers, partners) are established

ID.BE-1: The organization’s role in the
supply chain is identified and
communicated

ISA 62443-2-1:2009 4.3.2.3.3
ISO/IEC 27001:2013 A.6.1.1
NIST SP 800-53 Rev. 4 CP-2, PS-7, PM-11

COBIT 5 APO08.01, APO08.04, APO08.05,
APO10.03, APO10.04, APO10.05
ISO/IEC 27001:2013 A.15.1.1, A.15.1.2,
A.15.1.3, A.15.2.1, A.15.2.2
NIST SP 800-53 Rev. 4 CP-2, SA-12

ID.BE-2: The organization’s place in
critical infrastructure and its industry sector
is identified and communicated

COBIT 5 APO02.06, APO03.01
ISO/IEC 27001:2013 Clause 4.1
NIST SP 800-53 Rev. 4 PM-8

ID.BE-3: Priorities for organizational
mission, objectives, and activities are
established and communicated

ID.BE-4: Dependencies and critical
functions for delivery of critical services
are established

ID.BE-5: Resilience requirements to
support delivery of critical services are
established for all operating states (e.g.
under duress/attack, during recovery,
normal operations)

ID.GV-1: Organizational cybersecurity
policy is established and communicated

COBIT 5 APO02.01, APO02.06, APO03.01
ISA 62443-2-1:2009 4.2.2.1, 4.2.3.6
NIST SP 800-53 Rev. 4 PM-11, SA-14

COBIT 5 APO10.01, BAI04.02, BAI09.02
ISO/IEC 27001:2013 A.11.2.2, A.11.2.3, A.12.1.3
NIST SP 800-53 Rev. 4 CP-8, PE-9, PE-11, PM-8,
SA-14

COBIT 5 BAI03.02, DSS04.02
ISO/IEC 27001:2013 A.11.1.4, A.17.1.1,
A.17.1.2, A.17.2.1
NIST SP 800-53 Rev. 4 CP-2, CP-11, SA-13, SA-
14

CIS CSC 19
COBIT 5 APO01.03, APO13.01, EDM01.01,
EDM01.02
ISA 62443-2-1:2009 4.3.2.6
ISO/IEC 27001:2013 A.5.1.1
NIST SP 800-53 Rev. 4 -1 controls from all
security control families

Governance (ID.GV): The
policies, procedures, and
processes to manage and monitor
the organization’s regulatory,
legal, risk, environmental, and
operational requirements are
understood and inform the

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

25

April 16, 2018

Cybersecurity Framework

Version 1.1

Function

Category

Subcategory

Informative References

management of cybersecurity
risk.

ID.GV-2: Cybersecurity roles and
responsibilities are coordinated and aligned
with internal roles and external partners

ID.GV-3: Legal and regulatory
requirements regarding cybersecurity,
including privacy and civil liberties
obligations, are understood and managed

ID.GV-4: Governance and risk
management processes address
cybersecurity risks

ID.RA-1: Asset vulnerabilities are
identified and documented

ID.RA-2: Cyber threat intelligence is
received from information sharing forums
and sources

Risk Assessment (ID.RA): The
organization understands the
cybersecurity risk to
organizational operations
(including mission, functions,
image, or reputation),
organizational assets, and
individuals.

CIS CSC 19
COBIT 5 APO01.02, APO10.03, APO13.02,
DSS05.04
ISA 62443-2-1:2009 4.3.2.3.3
ISO/IEC 27001:2013 A.6.1.1, A.7.2.1, A.15.1.1
NIST SP 800-53 Rev. 4 PS-7, PM-1, PM-2

CIS CSC 19
COBIT 5 BAI02.01, MEA03.01, MEA03.04
ISA 62443-2-1:2009 4.4.3.7
ISO/IEC 27001:2013 A.18.1.1, A.18.1.2,
A.18.1.3, A.18.1.4, A.18.1.5
NIST SP 800-53 Rev. 4 -1 controls from all
security control families

COBIT 5 EDM03.02, APO12.02, APO12.05,
DSS04.02
ISA 62443-2-1:2009 4.2.3.1, 4.2.3.3, 4.2.3.8,
4.2.3.9, 4.2.3.11, 4.3.2.4.3, 4.3.2.6.3
ISO/IEC 27001:2013 Clause 6
NIST SP 800-53 Rev. 4 SA-2, PM-3, PM-7, PM-
9, PM-10, PM-11

CIS CSC 4
COBIT 5 APO12.01, APO12.02, APO12.03,
APO12.04, DSS05.01, DSS05.02
ISA 62443-2-1:2009 4.2.3, 4.2.3.7, 4.2.3.9,
4.2.3.12
ISO/IEC 27001:2013 A.12.6.1, A.18.2.3
NIST SP 800-53 Rev. 4 CA-2, CA-7, CA-8, RA-
3, RA-5, SA-5, SA-11, SI-2, SI-4, SI-5

CIS CSC 4
COBIT 5 BAI08.01
ISA 62443-2-1:2009 4.2.3, 4.2.3.9, 4.2.3.12
ISO/IEC 27001:2013 A.6.1.4
NIST SP 800-53 Rev. 4 SI-5, PM-15, PM-16

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

26

April 16, 2018

Cybersecurity Framework

Version 1.1

Function

Category

Subcategory

Informative References

ID.RA-3: Threats, both internal and
external, are identified and documented

ID.RA-4: Potential business impacts and
likelihoods are identified

ID.RA-5: Threats, vulnerabilities,
likelihoods, and impacts are used to
determine risk

ID.RA-6: Risk responses are identified and
prioritized

ID.RM-1: Risk management processes are
established, managed, and agreed to by
organizational stakeholders

ID.RM-2: Organizational risk tolerance is
determined and clearly expressed

CIS CSC 4
COBIT 5 APO12.01, APO12.02, APO12.03,
APO12.04
ISA 62443-2-1:2009 4.2.3, 4.2.3.9, 4.2.3.12
ISO/IEC 27001:2013 Clause 6.1.2
NIST SP 800-53 Rev. 4 RA-3, SI-5, PM-12, PM-
16

CIS CSC 4
COBIT 5 DSS04.02
ISA 62443-2-1:2009 4.2.3, 4.2.3.9, 4.2.3.12
ISO/IEC 27001:2013 A.16.1.6, Clause 6.1.2
NIST SP 800-53 Rev. 4 RA-2, RA-3, SA-14, PM-
9, PM-11

CIS CSC 4
COBIT 5 APO12.02
ISO/IEC 27001:2013 A.12.6.1
NIST SP 800-53 Rev. 4 RA-2, RA-3, PM-16

CIS CSC 4
COBIT 5 APO12.05, APO13.02
ISO/IEC 27001:2013 Clause 6.1.3
NIST SP 800-53 Rev. 4 PM-4, PM-9

CIS CSC 4
COBIT 5 APO12.04, APO12.05, APO13.02,
BAI02.03, BAI04.02
ISA 62443-2-1:2009 4.3.4.2
ISO/IEC 27001:2013 Clause 6.1.3, Clause 8.3,
Clause 9.3
NIST SP 800-53 Rev. 4 PM-9
COBIT 5 APO12.06
ISA 62443-2-1:2009 4.3.2.6.5
ISO/IEC 27001:2013 Clause 6.1.3, Clause 8.3
NIST SP 800-53 Rev. 4 PM-9

Risk Management Strategy
(ID.RM): The organization’s
priorities, constraints, risk
tolerances, and assumptions are
established and used to support
operational risk decisions.

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

27

April 16, 2018

Cybersecurity Framework

Version 1.1

Function

Category

Subcategory

Informative References

ID.RM-3: The organization’s
determination of risk tolerance is informed
by its role in critical infrastructure and
sector specific risk analysis

COBIT 5 APO12.02
ISO/IEC 27001:2013 Clause 6.1.3, Clause 8.3
NIST SP 800-53 Rev. 4 SA-14, PM-8, PM-9, PM-
11

Supply Chain Risk
Management (ID.SC):
The organization’s priorities,
constraints, risk tolerances, and
assumptions are established and
used to support risk decisions
associated with managing supply
chain risk. The organization has
established and implemented the
processes to identify, assess and
manage supply chain risks.

ID.SC-1: Cyber supply chain risk
management processes are identified,
established, assessed, managed, and agreed
to by organizational stakeholders

ID.SC-2: Suppliers and third party partners
of information systems, components, and
services are identified, prioritized, and
assessed using a cyber supply chain risk
assessment process

ID.SC-3: Contracts with suppliers and
third-party partners are used to implement
appropriate measures designed to meet the
objectives of an organization’s
cybersecurity program and Cyber Supply
Chain Risk Management Plan.

ID.SC-4: Suppliers and third-party partners
are routinely assessed using audits, test
results, or other forms of evaluations to
confirm they are meeting their contractual
obligations.

CIS CSC 4
COBIT 5 APO10.01, APO10.04, APO12.04,
APO12.05, APO13.02, BAI01.03, BAI02.03,
BAI04.02
ISA 62443-2-1:2009 4.3.4.2
ISO/IEC 27001:2013 A.15.1.1, A.15.1.2,
A.15.1.3, A.15.2.1, A.15.2.2
NIST SP 800-53 Rev. 4 SA-9, SA-12, PM-9

COBIT 5 APO10.01, APO10.02, APO10.04,
APO10.05, APO12.01, APO12.02, APO12.03,
APO12.04, APO12.05, APO12.06, APO13.02,
BAI02.03
ISA 62443-2-1:2009 4.2.3.1, 4.2.3.2, 4.2.3.3,
4.2.3.4, 4.2.3.6, 4.2.3.8, 4.2.3.9, 4.2.3.10, 4.2.3.12,
4.2.3.13, 4.2.3.14
ISO/IEC 27001:2013 A.15.2.1, A.15.2.2
NIST SP 800-53 Rev. 4 RA-2, RA-3, SA-12, SA-
14, SA-15, PM-9

COBIT 5 APO10.01, APO10.02, APO10.03,
APO10.04, APO10.05
ISA 62443-2-1:2009 4.3.2.6.4, 4.3.2.6.7
ISO/IEC 27001:2013 A.15.1.1, A.15.1.2, A.15.1.3
NIST SP 800-53 Rev. 4 SA-9, SA-11, SA-12, PM-
9

COBIT 5 APO10.01, APO10.03, APO10.04,
APO10.05, MEA01.01, MEA01.02, MEA01.03,
MEA01.04, MEA01.05
ISA 62443-2-1:2009 4.3.2.6.7
ISA 62443-3-3:2013 SR 6.1
ISO/IEC 27001:2013 A.15.2.1, A.15.2.2

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

28

April 16, 2018

Cybersecurity Framework

Version 1.1

Function

Category

Subcategory

Informative References

PROTECT (PR)

Identity Management,
Authentication and Access
Control (PR.AC): Access to
physical and logical assets and
associated facilities is limited to
authorized users, processes, and
devices, and is managed
consistent with the assessed risk
of unauthorized access to
authorized activities and
transactions.

ID.SC-5: Response and recovery planning
and testing are conducted with suppliers
and third-party providers

PR.AC-1: Identities and credentials are
issued, managed, verified, revoked, and
audited for authorized devices, users and
processes

PR.AC-2: Physical access to assets is
managed and protected

PR.AC-3: Remote access is managed

NIST SP 800-53 Rev. 4 AU-2, AU-6, AU-12, AU-
16, PS-7, SA-9, SA-12

CIS CSC 19, 20
COBIT 5 DSS04.04
ISA 62443-2-1:2009 4.3.2.5.7, 4.3.4.5.11
ISA 62443-3-3:2013 SR 2.8, SR 3.3, SR.6.1, SR
7.3, SR 7.4
ISO/IEC 27001:2013 A.17.1.3
NIST SP 800-53 Rev. 4 CP-2, CP-4, IR-3, IR-4,
IR-6, IR-8, IR-9

CIS CSC 1, 5, 15, 16
COBIT 5 DSS05.04, DSS06.03
ISA 62443-2-1:2009 4.3.3.5.1
ISA 62443-3-3:2013 SR 1.1, SR 1.2, SR 1.3, SR
1.4, SR 1.5, SR 1.7, SR 1.8, SR 1.9
ISO/IEC 27001:2013 A.9.2.1, A.9.2.2, A.9.2.3,
A.9.2.4, A.9.2.6, A.9.3.1, A.9.4.2, A.9.4.3
NIST SP 800-53 Rev. 4 AC-1, AC-2, IA-1, IA-2,
IA-3, IA-4, IA-5, IA-6, IA-7, IA-8, IA-9, IA-10,
IA-11

COBIT 5 DSS01.04, DSS05.05
ISA 62443-2-1:2009 4.3.3.3.2, 4.3.3.3.8
ISO/IEC 27001:2013 A.11.1.1, A.11.1.2,
A.11.1.3, A.11.1.4, A.11.1.5, A.11.1.6, A.11.2.1,
A.11.2.3, A.11.2.5, A.11.2.6, A.11.2.7, A.11.2.8
NIST SP 800-53 Rev. 4 PE-2, PE-3, PE-4, PE-5,
PE-6, PE-8

CIS CSC 12
COBIT 5 APO13.01, DSS01.04, DSS05.03
ISA 62443-2-1:2009 4.3.3.6.6
ISA 62443-3-3:2013 SR 1.13, SR 2.6
ISO/IEC 27001:2013 A.6.2.1, A.6.2.2, A.11.2.6,
A.13.1.1, A.13.2.1

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

29

April 16, 2018

Cybersecurity Framework

Version 1.1

Function

Category

Subcategory

Informative References

PR.AC-4: Access permissions and
authorizations are managed, incorporating
the principles of least privilege and
separation of duties

PR.AC-5: Network integrity is protected
(e.g., network segregation, network
segmentation)

PR.AC-6: Identities are proofed and bound
to credentials and asserted in interactions

PR.AC-7: Users, devices, and other assets
are authenticated (e.g., single-factor, multi-
factor) commensurate with the risk of the
transaction (e.g., individuals’ security and
privacy risks and other organizational
risks)

NIST SP 800-53 Rev. 4 AC-1, AC-17, AC-19,
AC-20, SC-15

CIS CSC 3, 5, 12, 14, 15, 16, 18
COBIT 5 DSS05.04
ISA 62443-2-1:2009 4.3.3.7.3
ISA 62443-3-3:2013 SR 2.1
ISO/IEC 27001:2013 A.6.1.2, A.9.1.2, A.9.2.3,
A.9.4.1, A.9.4.4, A.9.4.5
NIST SP 800-53 Rev. 4 AC-1, AC-2, AC-3, AC-
5, AC-6, AC-14, AC-16, AC-24

CIS CSC 9, 14, 15, 18
COBIT 5 DSS01.05, DSS05.02
ISA 62443-2-1:2009 4.3.3.4
ISA 62443-3-3:2013 SR 3.1, SR 3.8
ISO/IEC 27001:2013 A.13.1.1, A.13.1.3,
A.13.2.1, A.14.1.2, A.14.1.3
NIST SP 800-53 Rev. 4 AC-4, AC-10, SC-7

CIS CSC, 16
COBIT 5 DSS05.04, DSS05.05, DSS05.07,
DSS06.03
ISA 62443-2-1:2009 4.3.3.2.2, 4.3.3.5.2, 4.3.3.7.2,
4.3.3.7.4
ISA 62443-3-3:2013 SR 1.1, SR 1.2, SR 1.4, SR
1.5, SR 1.9, SR 2.1
ISO/IEC 27001:2013, A.7.1.1, A.9.2.1
NIST SP 800-53 Rev. 4 AC-1, AC-2, AC-3,  AC-
16, AC-19, AC-24, IA-1, IA-2, IA-4, IA-5, IA-8,
PE-2, PS-3

CIS CSC 1, 12, 15, 16
COBIT 5 DSS05.04, DSS05.10, DSS06.10
ISA 62443-2-1:2009 4.3.3.6.1, 4.3.3.6.2, 4.3.3.6.3,
4.3.3.6.4, 4.3.3.6.5, 4.3.3.6.6, 4.3.3.6.7, 4.3.3.6.8,
4.3.3.6.9

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

30

April 16, 2018

Cybersecurity Framework

Version 1.1

Function

Category

Subcategory

Informative References

Awareness and Training
(PR.AT): The organization’s
personnel and partners are
provided cybersecurity awareness
education and are trained to
perform their cybersecurity-
related duties and responsibilities
consistent with related policies,
procedures, and agreements.

ISA 62443-3-3:2013 SR 1.1, SR 1.2, SR 1.5, SR
1.7, SR 1.8, SR 1.9, SR 1.10
ISO/IEC 27001:2013 A.9.2.1, A.9.2.4, A.9.3.1,
A.9.4.2, A.9.4.3, A.18.1.4
NIST SP 800-53 Rev. 4 AC-7, AC-8, AC-9, AC-
11, AC-12, AC-14, IA-1, IA-2, IA-3, IA-4, IA-5,
IA-8, IA-9, IA-10, IA-11

CIS CSC 17, 18
COBIT 5 APO07.03, BAI05.07
ISA 62443-2-1:2009 4.3.2.4.2
ISO/IEC 27001:2013 A.7.2.2, A.12.2.1
NIST SP 800-53 Rev. 4 AT-2, PM-13

CIS CSC 5, 17, 18
COBIT 5 APO07.02, DSS05.04, DSS06.03
ISA 62443-2-1:2009 4.3.2.4.2, 4.3.2.4.3
ISO/IEC 27001:2013 A.6.1.1, A.7.2.2
NIST SP 800-53 Rev. 4 AT-3, PM-13

CIS CSC 17
COBIT 5 APO07.03, APO07.06, APO10.04,
APO10.05
ISA 62443-2-1:2009 4.3.2.4.2
ISO/IEC 27001:2013 A.6.1.1, A.7.2.1, A.7.2.2
NIST SP 800-53 Rev. 4 PS-7, SA-9, SA-16

CIS CSC 17, 19
COBIT 5 EDM01.01, APO01.02, APO07.03
ISA 62443-2-1:2009 4.3.2.4.2
ISO/IEC 27001:2013 A.6.1.1, A.7.2.2
NIST SP 800-53 Rev. 4 AT-3, PM-13

CIS CSC 17
COBIT 5 APO07.03
ISA 62443-2-1:2009 4.3.2.4.2
ISO/IEC 27001:2013 A.6.1.1, A.7.2.2

PR.AT-1: All users are informed and
trained

PR.AT-2: Privileged users understand their
roles and responsibilities

PR.AT-3: Third-party stakeholders (e.g.,
suppliers, customers, partners) understand
their roles and responsibilities

PR.AT-4: Senior executives understand
their roles and responsibilities

PR.AT-5: Physical and cybersecurity
personnel understand their roles and
responsibilities

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

31

April 16, 2018

Cybersecurity Framework

Version 1.1

Function

Category

Subcategory

Informative References

PR.DS-1: Data-at-rest is protected

Data Security (PR.DS):
Information and records (data) are
managed consistent with the
organization’s risk strategy to
protect the confidentiality,
integrity, and availability of
information.

PR.DS-2: Data-in-transit is protected

PR.DS-3: Assets are formally managed
throughout removal, transfers, and
disposition

PR.DS-4: Adequate capacity to ensure
availability is maintained

PR.DS-5: Protections against data leaks
are implemented

NIST SP 800-53 Rev. 4 AT-3, IR-2, PM-13

CIS CSC 13, 14
COBIT 5 APO01.06, BAI02.01, BAI06.01,
DSS04.07, DSS05.03, DSS06.06
ISA 62443-3-3:2013 SR 3.4, SR 4.1
ISO/IEC 27001:2013 A.8.2.3
NIST SP 800-53 Rev. 4 MP-8, SC-12, SC-28

CIS CSC 13, 14
COBIT 5 APO01.06, DSS05.02, DSS06.06
ISA 62443-3-3:2013 SR 3.1, SR 3.8, SR 4.1, SR
4.2
ISO/IEC 27001:2013 A.8.2.3, A.13.1.1, A.13.2.1,
A.13.2.3, A.14.1.2, A.14.1.3
NIST SP 800-53 Rev. 4 SC-8, SC-11, SC-12

CIS CSC 1
COBIT 5 BAI09.03
ISA 62443-2-1:2009 4.3.3.3.9, 4.3.4.4.1
ISA 62443-3-3:2013 SR 4.2
ISO/IEC 27001:2013 A.8.2.3, A.8.3.1, A.8.3.2,
A.8.3.3, A.11.2.5, A.11.2.7
NIST SP 800-53 Rev. 4 CM-8, MP-6, PE-16

CIS CSC 1, 2, 13
COBIT 5 APO13.01, BAI04.04
ISA 62443-3-3:2013 SR 7.1, SR 7.2
ISO/IEC 27001:2013 A.12.1.3, A.17.2.1
NIST SP 800-53 Rev. 4 AU-4, CP-2, SC-5

CIS CSC 13
COBIT 5 APO01.06, DSS05.04, DSS05.07,
DSS06.02
ISA 62443-3-3:2013 SR 5.2
ISO/IEC 27001:2013 A.6.1.2, A.7.1.1, A.7.1.2,
A.7.3.1, A.8.2.2, A.8.2.3, A.9.1.1, A.9.1.2, A.9.2.3,
A.9.4.1, A.9.4.4, A.9.4.5, A.10.1.1, A.11.1.4,

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

32

April 16, 2018

Cybersecurity Framework

Version 1.1

Function

Category

Subcategory

Informative References

PR.DS-6: Integrity checking mechanisms
are used to verify software, firmware, and
information integrity

PR.DS-7: The development and testing
environment(s) are separate from the
production environment

PR.DS-8: Integrity checking mechanisms
are used to verify hardware integrity

PR.IP-1: A baseline configuration of
information technology/industrial control
systems is created and maintained
incorporating security principles (e.g.
concept of least functionality)

PR.IP-2: A System Development Life
Cycle to manage systems is implemented

A.11.1.5, A.11.2.1, A.13.1.1, A.13.1.3, A.13.2.1,
A.13.2.3, A.13.2.4, A.14.1.2, A.14.1.3
NIST SP 800-53 Rev. 4 AC-4, AC-5, AC-6, PE-
19, PS-3, PS-6, SC-7, SC-8, SC-13, SC-31, SI-4

CIS CSC 2, 3
COBIT 5 APO01.06, BAI06.01, DSS06.02
ISA 62443-3-3:2013 SR 3.1, SR 3.3, SR 3.4, SR
3.8
ISO/IEC 27001:2013 A.12.2.1, A.12.5.1,
A.14.1.2, A.14.1.3, A.14.2.4
NIST SP 800-53 Rev. 4 SC-16, SI-7

CIS CSC 18, 20
COBIT 5 BAI03.08, BAI07.04
ISO/IEC 27001:2013 A.12.1.4
NIST SP 800-53 Rev. 4 CM-2

COBIT 5 BAI03.05
ISA 62443-2-1:2009 4.3.4.4.4
ISO/IEC 27001:2013 A.11.2.4
NIST SP 800-53 Rev. 4 SA-10, SI-7

CIS CSC 3, 9, 11
COBIT 5 BAI10.01, BAI10.02, BAI10.03,
BAI10.05
ISA 62443-2-1:2009 4.3.4.3.2, 4.3.4.3.3
ISA 62443-3-3:2013 SR 7.6
ISO/IEC 27001:2013 A.12.1.2, A.12.5.1,
A.12.6.2, A.14.2.2, A.14.2.3, A.14.2.4
NIST SP 800-53 Rev. 4 CM-2, CM-3, CM-4, CM-
5, CM-6, CM-7, CM-9, SA-10

CIS CSC 18
COBIT 5 APO13.01, BAI03.01, BAI03.02,
BAI03.03
ISA 62443-2-1:2009 4.3.4.3.3

Information Protection
Processes and Procedures
(PR.IP): Security policies (that
address purpose, scope, roles,
responsibilities, management
commitment, and coordination
among organizational entities),
processes, and procedures are
maintained and used to manage
protection of information systems
and assets.

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

33

April 16, 2018

Cybersecurity Framework

Version 1.1

Function

Category

Subcategory

Informative References

PR.IP-3: Configuration change control
processes are in place

PR.IP-4: Backups of information are
conducted, maintained, and tested

PR.IP-5: Policy and regulations regarding
the physical operating environment for
organizational assets are met

PR.IP-6: Data is destroyed according to
policy

ISO/IEC 27001:2013 A.6.1.5, A.14.1.1, A.14.2.1,
A.14.2.5
NIST SP 800-53 Rev. 4 PL-8, SA-3, SA-4, SA-8,
SA-10, SA-11, SA-12, SA-15, SA-17, SI-12, SI-
13, SI-14, SI-16, SI-17

CIS CSC 3, 11
COBIT 5 BAI01.06, BAI06.01
ISA 62443-2-1:2009 4.3.4.3.2, 4.3.4.3.3
ISA 62443-3-3:2013 SR 7.6
ISO/IEC 27001:2013 A.12.1.2, A.12.5.1,
A.12.6.2, A.14.2.2, A.14.2.3, A.14.2.4
NIST SP 800-53 Rev. 4 CM-3, CM-4, SA-10

CIS CSC 10
COBIT 5 APO13.01, DSS01.01, DSS04.07
ISA 62443-2-1:2009 4.3.4.3.9
ISA 62443-3-3:2013 SR 7.3, SR 7.4
ISO/IEC 27001:2013 A.12.3.1, A.17.1.2,
A.17.1.3, A.18.1.3
NIST SP 800-53 Rev. 4 CP-4, CP-6, CP-9

COBIT 5 DSS01.04, DSS05.05
ISA 62443-2-1:2009 4.3.3.3.1 4.3.3.3.2, 4.3.3.3.3,
4.3.3.3.5, 4.3.3.3.6
ISO/IEC 27001:2013 A.11.1.4, A.11.2.1,
A.11.2.2, A.11.2.3
NIST SP 800-53 Rev. 4 PE-10, PE-12, PE-13, PE-
14, PE-15, PE-18

COBIT 5 BAI09.03, DSS05.06
ISA 62443-2-1:2009 4.3.4.4.4
ISA 62443-3-3:2013 SR 4.2
ISO/IEC 27001:2013 A.8.2.3, A.8.3.1, A.8.3.2,
A.11.2.7
NIST SP 800-53 Rev. 4 MP-6

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

34

April 16, 2018

Cybersecurity Framework

Version 1.1

Function

Category

Subcategory

Informative References

PR.IP-7: Protection processes are
improved

PR.IP-8: Effectiveness of protection
technologies is shared

PR.IP-9: Response plans (Incident
Response and Business Continuity) and
recovery plans (Incident Recovery and
Disaster Recovery) are in place and
managed

PR.IP-10: Response and recovery plans
are tested

PR.IP-11: Cybersecurity is included in
human resources practices (e.g.,
deprovisioning, personnel screening)

COBIT 5 APO11.06, APO12.06, DSS04.05
ISA 62443-2-1:2009 4.4.3.1, 4.4.3.2, 4.4.3.3,
4.4.3.4, 4.4.3.5, 4.4.3.6, 4.4.3.7, 4.4.3.8
ISO/IEC 27001:2013 A.16.1.6, Clause 9, Clause
10
NIST SP 800-53 Rev. 4 CA-2, CA-7, CP-2, IR-8,
PL-2, PM-6
COBIT 5 BAI08.04, DSS03.04
ISO/IEC 27001:2013 A.16.1.6
NIST SP 800-53 Rev. 4 AC-21, CA-7, SI-4

CIS CSC 19
COBIT 5 APO12.06, DSS04.03
ISA 62443-2-1:2009 4.3.2.5.3, 4.3.4.5.1
ISO/IEC 27001:2013 A.16.1.1, A.17.1.1,
A.17.1.2, A.17.1.3
NIST SP 800-53 Rev. 4 CP-2, CP-7, CP-12, CP-
13, IR-7, IR-8, IR-9, PE-17

CIS CSC 19, 20
COBIT 5 DSS04.04
ISA 62443-2-1:2009 4.3.2.5.7, 4.3.4.5.11
ISA 62443-3-3:2013 SR 3.3
ISO/IEC 27001:2013 A.17.1.3
NIST SP 800-53 Rev. 4 CP-4, IR-3, PM-14

CIS CSC 5, 16
COBIT 5 APO07.01, APO07.02, APO07.03,
APO07.04, APO07.05
ISA 62443-2-1:2009 4.3.3.2.1, 4.3.3.2.2, 4.3.3.2.3
ISO/IEC 27001:2013 A.7.1.1, A.7.1.2, A.7.2.1,
A.7.2.2, A.7.2.3, A.7.3.1, A.8.1.4
NIST SP 800-53 Rev. 4 PS-1, PS-2, PS-3, PS-4,
PS-5, PS-6, PS-7, PS-8, SA-21

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

35

April 16, 2018

Cybersecurity Framework

Version 1.1

Function

Category

Subcategory

Informative References

PR.IP-12: A vulnerability management
plan is developed and implemented

Maintenance (PR.MA):
Maintenance and repairs of
industrial control and information
system components are performed
consistent with policies and
procedures.

PR.MA-1: Maintenance and repair of
organizational assets are performed and
logged, with approved and controlled tools

Protective Technology (PR.PT):
Technical security solutions are
managed to ensure the security
and resilience of systems and
assets, consistent with related
policies, procedures, and
agreements.

PR.MA-2: Remote maintenance of
organizational assets is approved, logged,
and performed in a manner that prevents
unauthorized access

PR.PT-1: Audit/log records are
determined, documented, implemented,
and reviewed in accordance with policy

PR.PT-2: Removable media is protected
and its use restricted according to policy

CIS CSC 4, 18, 20
COBIT 5 BAI03.10, DSS05.01, DSS05.02
ISO/IEC 27001:2013 A.12.6.1, A.14.2.3,
A.16.1.3, A.18.2.2, A.18.2.3
NIST SP 800-53 Rev. 4 RA-3, RA-5, SI-2

COBIT 5 BAI03.10, BAI09.02, BAI09.03,
DSS01.05
ISA 62443-2-1:2009 4.3.3.3.7
ISO/IEC 27001:2013 A.11.1.2, A.11.2.4,
A.11.2.5, A.11.2.6
NIST SP 800-53 Rev. 4 MA-2, MA-3, MA-5,
MA-6

CIS CSC 3, 5
COBIT 5 DSS05.04
ISA 62443-2-1:2009 4.3.3.6.5, 4.3.3.6.6, 4.3.3.6.7,
4.3.3.6.8
ISO/IEC 27001:2013 A.11.2.4, A.15.1.1, A.15.2.1
NIST SP 800-53 Rev. 4 MA-4

CIS CSC 1, 3, 5, 6, 14, 15, 16
COBIT 5 APO11.04, BAI03.05, DSS05.04,
DSS05.07, MEA02.01
ISA 62443-2-1:2009 4.3.3.3.9, 4.3.3.5.8, 4.3.4.4.7,
4.4.2.1, 4.4.2.2, 4.4.2.4
ISA 62443-3-3:2013 SR 2.8, SR 2.9, SR 2.10, SR
2.11, SR 2.12
ISO/IEC 27001:2013 A.12.4.1, A.12.4.2,
A.12.4.3, A.12.4.4, A.12.7.1
NIST SP 800-53 Rev. 4 AU Family

CIS CSC 8, 13
COBIT 5 APO13.01, DSS05.02, DSS05.06
ISA 62443-3-3:2013 SR 2.3
ISO/IEC 27001:2013 A.8.2.1, A.8.2.2, A.8.2.3,
A.8.3.1, A.8.3.3, A.11.2.9

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

36

April 16, 2018

Cybersecurity Framework

Version 1.1

Function

Category

Subcategory

Informative References

PR.PT-3: The principle of least
functionality is incorporated by configuring
systems to provide only essential
capabilities

PR.PT-4: Communications and control
networks are protected

PR.PT-5: Mechanisms (e.g., failsafe, load
balancing, hot swap) are implemented to
achieve resilience requirements in normal
and adverse situations

DETECT (DE)

Anomalies and Events (DE.AE):
Anomalous activity is detected

DE.AE-1: A baseline of network
operations and expected data flows for

NIST SP 800-53 Rev. 4 MP-2, MP-3, MP-4, MP-
5, MP-7, MP-8

CIS CSC 3, 11, 14
COBIT 5 DSS05.02, DSS05.05, DSS06.06
ISA 62443-2-1:2009 4.3.3.5.1, 4.3.3.5.2, 4.3.3.5.3,
4.3.3.5.4, 4.3.3.5.5, 4.3.3.5.6, 4.3.3.5.7, 4.3.3.5.8,
4.3.3.6.1, 4.3.3.6.2, 4.3.3.6.3, 4.3.3.6.4, 4.3.3.6.5,
4.3.3.6.6, 4.3.3.6.7, 4.3.3.6.8, 4.3.3.6.9, 4.3.3.7.1,
4.3.3.7.2, 4.3.3.7.3, 4.3.3.7.4
ISA 62443-3-3:2013 SR 1.1, SR 1.2, SR 1.3, SR
1.4, SR 1.5, SR 1.6, SR 1.7, SR 1.8, SR 1.9, SR
1.10, SR 1.11, SR 1.12, SR 1.13, SR 2.1, SR 2.2,
SR 2.3, SR 2.4, SR 2.5, SR 2.6, SR 2.7
ISO/IEC 27001:2013 A.9.1.2
NIST SP 800-53 Rev. 4 AC-3, CM-7

CIS CSC 8, 12, 15
COBIT 5 DSS05.02, APO13.01
ISA 62443-3-3:2013 SR 3.1, SR 3.5, SR 3.8, SR
4.1, SR 4.3, SR 5.1, SR 5.2, SR 5.3, SR 7.1, SR 7.6
ISO/IEC 27001:2013 A.13.1.1, A.13.2.1, A.14.1.3
NIST SP 800-53 Rev. 4 AC-4, AC-17, AC-18,
CP-8, SC-7, SC-19, SC-20, SC-21, SC-22, SC-23,
SC-24, SC-25, SC-29, SC-32, SC-36, SC-37, SC-
38, SC-39, SC-40, SC-41, SC-43

COBIT 5 BAI04.01, BAI04.02, BAI04.03,
BAI04.04, BAI04.05, DSS01.05
ISA 62443-2-1:2009 4.3.2.5.2
ISA 62443-3-3:2013 SR 7.1, SR 7.2
ISO/IEC 27001:2013 A.17.1.2, A.17.2.1
NIST SP 800-53 Rev. 4 CP-7, CP-8, CP-11, CP-
13, PL-8, SA-14, SC-6

CIS CSC 1, 4, 6, 12, 13, 15, 16
COBIT 5 DSS03.01
ISA 62443-2-1:2009 4.4.3.3

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

37

April 16, 2018

Cybersecurity Framework

Version 1.1

Function

Category

Subcategory

Informative References

and the potential impact of events
is understood.

users and systems is established and
managed

DE.AE-2: Detected events are analyzed to
understand attack targets and methods

DE.AE-3: Event data are collected and
correlated from multiple sources and
sensors

DE.AE-4: Impact of events is determined

DE.AE-5: Incident alert thresholds are
established

Security Continuous
Monitoring (DE.CM): The
information system and assets are
monitored to identify
cybersecurity events and verify

DE.CM-1: The network is monitored to
detect potential cybersecurity events

ISO/IEC 27001:2013 A.12.1.1, A.12.1.2,
A.13.1.1, A.13.1.2
NIST SP 800-53 Rev. 4 AC-4, CA-3, CM-2, SI-4

CIS CSC 3, 6, 13, 15
COBIT 5 DSS05.07
ISA 62443-2-1:2009 4.3.4.5.6, 4.3.4.5.7, 4.3.4.5.8
ISA 62443-3-3:2013 SR 2.8, SR 2.9, SR 2.10, SR
2.11, SR 2.12, SR 3.9, SR 6.1, SR 6.2
ISO/IEC 27001:2013 A.12.4.1, A.16.1.1, A.16.1.4
NIST SP 800-53 Rev. 4 AU-6, CA-7, IR-4, SI-4

CIS CSC 1, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16
COBIT 5 BAI08.02
ISA 62443-3-3:2013 SR 6.1
ISO/IEC 27001:2013 A.12.4.1, A.16.1.7
NIST SP 800-53 Rev. 4 AU-6, CA-7, IR-4, IR-5,
IR-8, SI-4

CIS CSC 4, 6
COBIT 5 APO12.06, DSS03.01
ISO/IEC 27001:2013 A.16.1.4
NIST SP 800-53 Rev. 4 CP-2, IR-4, RA-3, SI-4

CIS CSC 6, 19
COBIT 5 APO12.06, DSS03.01
ISA 62443-2-1:2009 4.2.3.10
ISO/IEC 27001:2013 A.16.1.4
NIST SP 800-53 Rev. 4 IR-4, IR-5, IR-8

CIS CSC 1, 7, 8, 12, 13, 15, 16
COBIT 5 DSS01.03, DSS03.05, DSS05.07
ISA 62443-3-3:2013 SR 6.2
NIST SP 800-53 Rev. 4 AC-2, AU-12, CA-7, CM-
3, SC-5, SC-7, SI-4

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

38

April 16, 2018

Cybersecurity Framework

Version 1.1

Function

Category

Subcategory

Informative References

the effectiveness of protective
measures.

DE.CM-2: The physical environment is
monitored to detect potential cybersecurity
events

DE.CM-3: Personnel activity is monitored
to detect potential cybersecurity events

DE.CM-4: Malicious code is detected

DE.CM-5: Unauthorized mobile code is
detected

DE.CM-6: External service provider
activity is monitored to detect potential
cybersecurity events

DE.CM-7: Monitoring for unauthorized
personnel, connections, devices, and
software is performed

COBIT 5 DSS01.04, DSS01.05
ISA 62443-2-1:2009 4.3.3.3.8
ISO/IEC 27001:2013 A.11.1.1, A.11.1.2
NIST SP 800-53 Rev. 4 CA-7, PE-3, PE-6, PE-20

CIS CSC 5, 7, 14, 16
COBIT 5 DSS05.07
ISA 62443-3-3:2013 SR 6.2
ISO/IEC 27001:2013 A.12.4.1, A.12.4.3
NIST SP 800-53 Rev. 4 AC-2, AU-12, AU-13,
CA-7, CM-10, CM-11

CIS CSC 4, 7, 8, 12
COBIT 5 DSS05.01
ISA 62443-2-1:2009 4.3.4.3.8
ISA 62443-3-3:2013 SR 3.2
ISO/IEC 27001:2013 A.12.2.1
NIST SP 800-53 Rev. 4 SI-3, SI-8

CIS CSC 7, 8
COBIT 5 DSS05.01
ISA 62443-3-3:2013 SR 2.4
ISO/IEC 27001:2013 A.12.5.1, A.12.6.2
NIST SP 800-53 Rev. 4 SC-18, SI-4, SC-44

COBIT 5 APO07.06, APO10.05
ISO/IEC 27001:2013 A.14.2.7, A.15.2.1
NIST SP 800-53 Rev. 4 CA-7, PS-7, SA-4, SA-9,
SI-4

CIS CSC 1, 2, 3, 5, 9, 12, 13, 15, 16
COBIT 5 DSS05.02, DSS05.05
ISO/IEC 27001:2013 A.12.4.1, A.14.2.7, A.15.2.1
NIST SP 800-53 Rev. 4 AU-12, CA-7, CM-3,
CM-8, PE-3, PE-6, PE-20, SI-4

DE.CM-8: Vulnerability scans are
performed

CIS CSC 4, 20

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

39

April 16, 2018

Cybersecurity Framework

Version 1.1

Function

Category

Subcategory

Informative References

Detection Processes (DE.DP):
Detection processes and
procedures are maintained and
tested to ensure awareness of
anomalous events.

DE.DP-1: Roles and responsibilities for
detection are well defined to ensure
accountability

DE.DP-2: Detection activities comply with
all applicable requirements

DE.DP-3: Detection processes are tested

DE.DP-4: Event detection information is
communicated

DE.DP-5: Detection processes are
continuously improved

COBIT 5 BAI03.10, DSS05.01
ISA 62443-2-1:2009 4.2.3.1, 4.2.3.7
ISO/IEC 27001:2013 A.12.6.1
NIST SP 800-53 Rev. 4 RA-5

CIS CSC 19
COBIT 5 APO01.02, DSS05.01, DSS06.03
ISA 62443-2-1:2009 4.4.3.1
ISO/IEC 27001:2013 A.6.1.1, A.7.2.2
NIST SP 800-53 Rev. 4 CA-2, CA-7, PM-14

COBIT 5 DSS06.01, MEA03.03, MEA03.04
ISA 62443-2-1:2009 4.4.3.2
ISO/IEC 27001:2013 A.18.1.4, A.18.2.2, A.18.2.3
NIST SP 800-53 Rev. 4 AC-25, CA-2, CA-7, SA-
18, SI-4, PM-14

COBIT 5 APO13.02, DSS05.02
ISA 62443-2-1:2009 4.4.3.2
ISA 62443-3-3:2013 SR 3.3
ISO/IEC 27001:2013 A.14.2.8
NIST SP 800-53 Rev. 4 CA-2, CA-7, PE-3, SI-3,
SI-4, PM-14

CIS CSC 19
COBIT 5 APO08.04, APO12.06, DSS02.05
ISA 62443-2-1:2009 4.3.4.5.9
ISA 62443-3-3:2013 SR 6.1
ISO/IEC 27001:2013 A.16.1.2, A.16.1.3
NIST SP 800-53 Rev. 4 AU-6, CA-2, CA-7,  RA-
5, SI-4

COBIT 5 APO11.06, APO12.06, DSS04.05
ISA 62443-2-1:2009 4.4.3.4
ISO/IEC 27001:2013 A.16.1.6
NIST SP 800-53 Rev. 4, CA-2, CA-7, PL-2, RA-
5, SI-4, PM-14

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

40

April 16, 2018

Cybersecurity Framework

Version 1.1

Function

Category

Subcategory

Informative References

RESPOND (RS)

Response Planning (RS.RP):
Response processes and
procedures are executed and
maintained, to ensure response to
detected cybersecurity incidents.

Communications (RS.CO):
Response activities are
coordinated with internal and
external stakeholders (e.g.
external support from law
enforcement agencies).

RS.RP-1: Response plan is executed
during or after an incident

RS.CO-1: Personnel know their roles and
order of operations when a response is
needed

RS.CO-2: Incidents are reported consistent
with established criteria

RS.CO-3: Information is shared consistent
with response plans

RS.CO-4: Coordination with stakeholders
occurs consistent with response plans

RS.CO-5: Voluntary information sharing
occurs with external stakeholders to
achieve broader cybersecurity situational
awareness

CIS CSC 19
COBIT 5 APO12.06, BAI01.10
ISA 62443-2-1:2009 4.3.4.5.1
ISO/IEC 27001:2013 A.16.1.5
NIST SP 800-53 Rev. 4 CP-2, CP-10, IR-4, IR-8

CIS CSC 19
COBIT 5 EDM03.02, APO01.02, APO12.03
ISA 62443-2-1:2009 4.3.4.5.2, 4.3.4.5.3, 4.3.4.5.4
ISO/IEC 27001:2013 A.6.1.1, A.7.2.2, A.16.1.1
NIST SP 800-53 Rev. 4 CP-2, CP-3, IR-3, IR-8
CIS CSC 19
COBIT 5 DSS01.03
ISA 62443-2-1:2009 4.3.4.5.5
ISO/IEC 27001:2013 A.6.1.3, A.16.1.2
NIST SP 800-53 Rev. 4 AU-6, IR-6, IR-8

CIS CSC 19
COBIT 5 DSS03.04
ISA 62443-2-1:2009 4.3.4.5.2
ISO/IEC 27001:2013 A.16.1.2, Clause 7.4, Clause
16.1.2
NIST SP 800-53 Rev. 4 CA-2, CA-7, CP-2, IR-4,
IR-8, PE-6, RA-5, SI-4

CIS CSC 19
COBIT 5 DSS03.04
ISA 62443-2-1:2009 4.3.4.5.5
ISO/IEC 27001:2013 Clause 7.4
NIST SP 800-53 Rev. 4 CP-2, IR-4, IR-8

CIS CSC 19
COBIT 5 BAI08.04
ISO/IEC 27001:2013 A.6.1.4
NIST SP 800-53 Rev. 4 SI-5, PM-15

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

41

April 16, 2018

Cybersecurity Framework

Version 1.1

Function

Category

Subcategory

Informative References

Analysis (RS.AN): Analysis is
conducted to ensure effective
response and support recovery
activities.

RS.AN-1: Notifications from detection
systems are investigated

RS.AN-2: The impact of the incident is
understood

RS.AN-3: Forensics are performed

RS.AN-4: Incidents are categorized
consistent with response plans

RS.AN-5: Processes are established to
receive, analyze and respond to
vulnerabilities disclosed to the organization
from internal and external sources (e.g.
internal testing, security bulletins, or
security researchers)

RS.MI-1: Incidents are contained

Mitigation (RS.MI): Activities
are performed to prevent
expansion of an event, mitigate its
effects, and resolve the incident.

CIS CSC 4, 6, 8, 19
COBIT 5 DSS02.04, DSS02.07
ISA 62443-2-1:2009 4.3.4.5.6, 4.3.4.5.7, 4.3.4.5.8
ISA 62443-3-3:2013 SR 6.1
ISO/IEC 27001:2013 A.12.4.1, A.12.4.3, A.16.1.5
NIST SP 800-53 Rev. 4 AU-6, CA-7, IR-4, IR-5,
PE-6, SI-4

COBIT 5 DSS02.02
ISA 62443-2-1:2009 4.3.4.5.6, 4.3.4.5.7, 4.3.4.5.8
ISO/IEC 27001:2013 A.16.1.4, A.16.1.6
NIST SP 800-53 Rev. 4 CP-2, IR-4

COBIT 5 APO12.06, DSS03.02, DSS05.07
ISA 62443-3-3:2013 SR 2.8, SR 2.9, SR 2.10, SR
2.11, SR 2.12, SR 3.9, SR 6.1
ISO/IEC 27001:2013 A.16.1.7
NIST SP 800-53 Rev. 4 AU-7, IR-4

CIS CSC 19
COBIT 5 DSS02.02
ISA 62443-2-1:2009 4.3.4.5.6
ISO/IEC 27001:2013 A.16.1.4
NIST SP 800-53 Rev. 4 CP-2, IR-4, IR-5, IR-8

CIS CSC 4, 19
COBIT 5 EDM03.02, DSS05.07
NIST SP 800-53 Rev. 4 SI-5, PM-15

CIS CSC 19
COBIT 5 APO12.06
ISA 62443-2-1:2009 4.3.4.5.6
ISA 62443-3-3:2013 SR 5.1, SR 5.2, SR 5.4
ISO/IEC 27001:2013 A.12.2.1, A.16.1.5

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

42

April 16, 2018

Cybersecurity Framework

Version 1.1

Function

Category

Subcategory

Informative References

RS.MI-2: Incidents are mitigated

RS.MI-3: Newly identified vulnerabilities
are mitigated or documented as accepted
risks

RS.IM-1: Response plans incorporate
lessons learned

RS.IM-2: Response strategies are updated

RC.RP-1: Recovery plan is executed
during or after a cybersecurity incident

RC.IM-1: Recovery plans incorporate
lessons learned

RC.IM-2: Recovery strategies are updated

NIST SP 800-53 Rev. 4 IR-4

CIS CSC 4, 19
COBIT 5 APO12.06
ISA 62443-2-1:2009 4.3.4.5.6, 4.3.4.5.10
ISO/IEC 27001:2013 A.12.2.1, A.16.1.5
NIST SP 800-53 Rev. 4 IR-4

CIS CSC 4
COBIT 5 APO12.06
ISO/IEC 27001:2013 A.12.6.1
NIST SP 800-53 Rev. 4 CA-7, RA-3, RA-5

COBIT 5 BAI01.13
ISA 62443-2-1:2009 4.3.4.5.10, 4.4.3.4
ISO/IEC 27001:2013 A.16.1.6, Clause 10
NIST SP 800-53 Rev. 4 CP-2, IR-4, IR-8

COBIT 5 BAI01.13, DSS04.08
ISO/IEC 27001:2013 A.16.1.6, Clause 10
NIST SP 800-53 Rev. 4 CP-2, IR-4, IR-8
CIS CSC 10
COBIT 5 APO12.06, DSS02.05, DSS03.04
ISO/IEC 27001:2013 A.16.1.5
NIST SP 800-53 Rev. 4 CP-10, IR-4, IR-8

COBIT 5 APO12.06, BAI05.07, DSS04.08
ISA 62443-2-1:2009 4.4.3.4
ISO/IEC 27001:2013 A.16.1.6, Clause 10
NIST SP 800-53 Rev. 4 CP-2, IR-4, IR-8

COBIT 5 APO12.06, BAI07.08
ISO/IEC 27001:2013 A.16.1.6, Clause 10
NIST SP 800-53 Rev. 4 CP-2, IR-4, IR-8

RECOVER (RC)

Improvements (RS.IM):
Organizational response activities
are improved by incorporating
lessons learned from current and
previous detection/response
activities.

Recovery Planning (RC.RP):
Recovery processes and
procedures are executed and
maintained to ensure restoration
of systems or assets affected by
cybersecurity incidents.

Improvements (RC.IM):
Recovery planning and processes
are improved by incorporating
lessons learned into future
activities.

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

43

April 16, 2018

Cybersecurity Framework

Version 1.1

Function

Category

Subcategory

Informative References

Communications (RC.CO):
Restoration activities are
coordinated with internal and
external parties (e.g.  coordinating
centers, Internet Service
Providers, owners of attacking
systems, victims, other CSIRTs,
and vendors).

RC.CO-1: Public relations are managed

COBIT 5 EDM03.02
ISO/IEC 27001:2013 A.6.1.4, Clause 7.4

RC.CO-2: Reputation is repaired after an
incident

COBIT 5 MEA03.02
ISO/IEC 27001:2013 Clause 7.4

RC.CO-3: Recovery activities are
communicated to internal and external
stakeholders as well as executive and
management teams

COBIT 5 APO12.06
ISO/IEC 27001:2013 Clause 7.4
NIST SP 800-53 Rev. 4 CP-2, IR-4

Information regarding Informative References described in Appendix A may be found at the following locations:

  Control Objectives for Information and Related Technology (COBIT): http://www.isaca.org/COBIT/Pages/default.aspx
  CIS Critical Security Controls for Effective Cyber Defense (CIS Controls): https://www.cisecurity.org
  American National Standards Institute/International Society of Automation (ANSI/ISA)-62443-2-1 (99.02.01)-2009, Security

for Industrial Automation and Control Systems: Establishing an Industrial Automation and Control Systems Security Program:
https://www.isa.org/templates/one-column.aspx?pageid=111294&productId=116731

  ANSI/ISA-62443-3-3 (99.03.03)-2013, Security for Industrial Automation and Control Systems: System Security Requirements



and Security Levels: https://www.isa.org/templates/one-column.aspx?pageid=111294&productId=116785
ISO/IEC 27001, Information technology -- Security techniques -- Information security management systems -- Requirements:
https://www.iso.org/standard/54534.html

  NIST SP 800-53 Rev. 4 - NIST Special Publication 800-53 Revision 4, Security and Privacy Controls for Federal Information
Systems and Organizations, April 2013 (including updates as of January 22, 2015). https://doi.org/10.6028/NIST.SP.800-53r4.
Informative References are only mapped to the control level, though any control enhancement might be found useful in
achieving a subcategory outcome.

Mappings between the Framework Core Subcategories and the specified sections in the Informative References are not intended to
definitively determine whether the specified sections in the Informative References provide the desired Subcategory outcome.

Informative References are not exhaustive, in that not every element (e.g., control, requirement) of a given Informative Reference is
mapped to Framework Core Subcategories.

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

44

April 16, 2018

Cybersecurity Framework

Version 1.1

Appendix B: Glossary

This appendix defines selected terms used in the publication.

Table 3: Framework Glossary

Buyer

Category

Critical
Infrastructure

The people or organizations that consume a given product or service.

The subdivision of a Function into groups of cybersecurity outcomes,
closely tied to programmatic needs and particular activities. Examples
of Categories include “Asset Management,” “Identity Management
and Access Control,” and “Detection Processes.”

Systems and assets, whether physical or virtual, so vital to the United
States that the incapacity or destruction of such systems and assets
would have a debilitating impact on cybersecurity, national economic
security, national public health or safety, or any combination of those
matters.

Cybersecurity

The process of protecting information by preventing, detecting, and
responding to attacks.

Cybersecurity
Event

Cybersecurity
Incident

A cybersecurity change that may have an impact on organizational
operations (including mission, capabilities, or reputation).

A cybersecurity event that has been determined to have an impact on
the organization prompting the need for response and recovery.

Detect (function)

Develop and implement the appropriate activities to identify the
occurrence of a cybersecurity event.

Framework

A risk-based approach to reducing cybersecurity risk composed of
three parts: the Framework Core, the Framework Profile, and the
Framework Implementation Tiers. Also known as the “Cybersecurity
Framework.”

Framework Core  A set of cybersecurity activities and references that are common

across critical infrastructure sectors and are organized around
particular outcomes. The Framework Core comprises four types of
elements: Functions, Categories, Subcategories, and Informative
References.

Framework
Implementation
Tier

A lens through which to view the characteristics of an organization’s
approach to risk—how an organization views cybersecurity risk and
the processes in place to manage that risk.

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

45

April 16, 2018

Cybersecurity Framework

Version 1.1

Framework
Profile

Function

A representation of the outcomes that a particular system or
organization has selected from the Framework Categories and
Subcategories.

One of the main components of the Framework. Functions provide the
highest level of structure for organizing basic cybersecurity activities
into Categories and Subcategories. The five functions are Identify,
Protect, Detect, Respond, and Recover.

Identify (function)  Develop the organizational understanding to manage cybersecurity
risk to systems, assets, data, and capabilities.

Informative
Reference

A specific section of standards, guidelines, and practices common
among critical infrastructure sectors that illustrates a method to
achieve the outcomes associated with each Subcategory. An example
of an Informative Reference is ISO/IEC 27001 Control A.10.8.3,
which supports the “Data-in-transit is protected” Subcategory of the
“Data Security” Category in the “Protect” function.

Mobile Code

A program (e.g., script, macro, or other portable instruction) that can
be shipped unchanged to a heterogeneous collection of platforms and
executed with identical semantics.

Protect (function)  Develop and implement the appropriate safeguards to ensure delivery

of critical infrastructure services.

Privileged User

A user that is authorized (and, therefore, trusted) to perform security-
relevant functions that ordinary users are not authorized to perform.

Recover (function)  Develop and implement the appropriate activities to maintain plans for
resilience and to restore any capabilities or services that were impaired
due to a cybersecurity event.

Respond
(function)

Risk

Develop and implement the appropriate activities to take action
regarding a detected cybersecurity event.

A measure of the extent to which an entity is threatened by a potential
circumstance or event, and typically a function of: (i) the adverse
impacts that would arise if the circumstance or event occurs; and (ii)
the likelihood of occurrence.

Risk Management  The process of identifying, assessing, and responding to risk.

Subcategory

The subdivision of a Category into specific outcomes of technical
and/or management activities. Examples of Subcategories include
“External information systems are catalogued,” “Data-at-rest is
protected,” and “Notifications from detection systems are
investigated.”

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

46

April 16, 2018

Cybersecurity Framework

Version 1.1

Supplier

Product and service providers used for an organization’s internal
purposes (e.g., IT infrastructure) or integrated into the products of
services provided to that organization’s Buyers.

Taxonomy

A scheme of classification.

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

47

April 16, 2018

Cybersecurity Framework

Version 1.1

Appendix C: Acronyms

This appendix defines selected acronyms used in the publication.

ANSI
CEA
CIS
COBIT
CPS
CSC
DHS
EO
ICS
IEC
IoT
IR
ISA
ISAC
ISAO
ISO
IT
NIST
OT
PII
RFI
RMP
SCRM
SP

American National Standards Institute
Cybersecurity Enhancement Act of 2014
Center for Internet Security
Control Objectives for Information and Related Technology
Cyber-Physical Systems
Critical Security Control
Department of Homeland Security
Executive Order
Industrial Control Systems
International Electrotechnical Commission
Internet of Things
Interagency Report
International Society of Automation
Information Sharing and Analysis Center
Information Sharing and Analysis Organization
International Organization for Standardization
Information Technology
National Institute of Standards and Technology
Operational Technology
Personally Identifiable Information
Request for Information
Risk Management Process
Supply Chain Risk Management
Special Publication

This publication is available free of charge from: https://doi.org/10.6028/NIST.CSWP.04162018

48

