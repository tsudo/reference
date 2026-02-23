# Symantec_ISTR20_2015

Original format: `pdf`

APRIL 2015
VOLUME 20

INTERNET SECURITY THREAT REPORT

MOBILE & IOT     WEB THREATS     SCAMS & SOCIAL MEDIA     TARGETED ATTACKS

2

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

4

5

9

 Introduction

 Executive Summary

2014 IN NUMBERS

18  MOBILE DEVICES

& THE INTERNET OF THINGS

19
23

25

26
26
27
27
28
29

 Mobile Malware

 SMS and the Interconnected
Threat to Mobile Devices
  Mobile Apps and Privacy

 Internet of Things
  Wearable Devices

Internet-Connected Everything
 Automotive Security

  The Network As the Target

 Medical Devices – Safety First, Security Second

31  WEB THREATS

32
32
32
33
34
35
35

 Vulnerabilities
  Heartbleed
  ShellShock and Poodle
  High-Profile Vulnerabilities and Time to Patch

 The Vulnerability Rises

  SSL and TLS Certificates Are Still Vital to Security
  Vulnerabilities as a Whole

41

 Compromised Sites

42

 Web Attack Toolkits

43
43

 Malvertising
  Malvertising at Large

44

 Denial of Service

45  SOCIAL MEDIA & SCAMS

46
46
48

50
51
53
54
54

54
56

 Social Media
  Facebook, Twitter, and Pinterest
 Affiliate Programs: The Fuel That
Drives Social Media Scams
Instagram

  Messaging Platforms
  Dating Scams
  Malcode in Social Media
  The Rise of “Antisocial Networking”

 Phishing

 Phishing in Countries You Might Not Expect

58

 Email Scams and Spam

60  TARGETED ATTACKS

61

 Cyberespionage

62
63

 Industrial Cybersecurity

 Securing Industrial Control Systems

65

 Reconnaissance Attacks

66
69

 Watering Hole Attacks

 Shifting Targets and Techniques

70

 Threat Intelligence

70

 Techniques Used In Targeted Attacks

77  DATA BREACHES & PRIVACY

83

 Retailers Under Attack

84
85

 Privacy and the Importance of Data Security
 Data Breaches in the Healthcare Industry

87  E-CRIME & MALWARE

88

 The Underground Economy

90
93
93
95
97

 Malware
  Ransomware
  Crypto-Ransomware

 Digital Extortion: A Short History of Ransomware

  Bots and Botnets

98
100

 OSX as a Target
  Malware on Virtualized Systems

101  APPENDIX

102

 Looking Ahead

104

 Best Practice Guidelines for Businesses

107

 20 Critical Security Controls

108

 Critical Control Protection Priorities

111

 Best Practice Guidelines for Consumers

112

 Best Practice Guidelines for Website Owners

114

 Footnotes

117

 Credits

118

 About Symantec

118

 More Information

2015 Internet Security Threat Report

MOBILE & IOT     WEB THREATS     SCAMS & SOCIAL MEDIA     TARGETED ATTACKS

3

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

CHARTS & TABLES

9

2014 IN NUMBERS

18  MOBILE DEVICES

& THE INTERNET OF THINGS
 New Android Mobile Malware Families

 Cumulative Android Mobile Malware Families

 New Android Variants per Family

 App Analysis by Symantec’s Norton Mobile Insight

 New Mobile Vulnerabilities

 Mobile Vulnerabilities by Operating System

 Mobile Threat Classifications

19
20
20
21
21
22
22

 Heartbleed and ShellShock Attacks

 New Vulnerabilities

31  WEB THREATS
33
35
36
36
37
37

 Browser Vulnerabilities

 Total Number of Vulnerabilities

 Plug-In Vulnerabilities by Month

 Top 10 Vulnerabilities Found Unpatched
on Scanned Webservers

38

38
39
39
40
40
42
42
44

 Scanned Websites with Vulnerabilities
Percentage of Which Were Critical

 Websites Found with Malware

 Classification of Most Frequently Exploited Websites

 Web Attacks Blocked per Month

 New Unique Malicious Web Domains

 Web Attacks Blocked per Day

 Top 5 Web Attack Toolkits

 Timeline of Web Attack Toolkit Use

 DDoS Attack Traffic

 Email Phishing Rate (Not Spear-Phishing)

 Number of Phishing URLs on Social Media

 Social Media

 Phishing Rate

45  SOCIAL MEDIA & SCAMS
47
55
57
57
58
58
59

 Global Spam Volume per Day

 Overall Email Spam Rate

 Estimated Global Email Spam Volume per Day

 Vulnerabilities Disclosed in ICS Including SCADA Systems

 Top 5 Zero-Day Vulnerabilities, Time of Exposure & Days to Patch

 Zero-Day Vulnerabilities, Annual Total

 Distribution of Spear-Phishing Attacks by Organization Size

 Risk Ratio of Spear-Phishing Attacks by Organization Size

 Zero-Day Vulnerabilities

60  TARGETED ATTACKS
62
66
67
68
70
71
71
72

 Top 10 Industries Targeted in Spear-Phishing Attacks

 Risk Ratio of Organizations in an Industry Impacted
by Targeted Attack Sent by Spear-Phishing Email

72
73
73
74
74
75
75
76

 Risk Ratio of Spear-Phishing Attacks by Industry

 Spear-Phishing Emails per Day

 Spear-Phishing Email Campaigns

 Spear-Phishing Email Word Cloud

 Risk Ratio of Spear-Phishing Attacks by Job Role

 Risk Ratio of Spear-Phishing Attacks by Job Level

 Average Number of Spear-Phishing Attacks per Day

 Analysis of Spear-Phishing Emails Used in Targeted Attacks

 Breaches with More Than 10 Million Identities Exposed

 Average Identities Exposed per Breach

 Median Identities Exposed per Breach

 Total Breaches

 Top Causes of Data Breach

77  DATA BREACHES & PRIVACY
78
78
79
79
80
80
81
82
82
83

 Timeline of Data Breaches

 Total Identities Exposed

 Top-Ten Types of Information Exposed

 Top 10 Sectors Breached by Number of Incidents

 Top 10 Sectors Breached by Number of Identities Exposed

 Value of Information Sold on Black Market

 Email Malware Rate (Overall)

 Email Malware as URL vs. Attachment

 Percent of Email Malware as URL vs. Attachment by Month

 Proportion of Email Traffic in Which Malware Was Detected

 New Malware Variants

87  E-CRIME & MALWARE
89
90
90
91
91
92
92
93
94
97
97
98
99

 Ransomware Over Time

 Crypto-Ransomware

 Ransomware Total

 Number of Bots

 Malicious Activity by Source: Bots

 Top 10 Spam-Sending Botnets

 Top 10 Mac OSX Malware Blocked on OSX Endpoints

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SCAMS & SOCIAL MEDIA     TARGETED ATTACKS

4

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Introduction

Symantec has established the most comprehensive source of Internet threat
data in the world through the Symantec™ Global Intelligence Network, which
is made up of more than 57.6 million attack sensors and records thousands of
events per second. This network monitors threat activity in over 157 countries
and territories through a combination of Symantec products and services such
as Symantec DeepSight™ Intelligence, Symantec™ Managed Security Services,
Norton™ consumer products, and other third-party data sources.

In addition, Symantec maintains one of the world’s most comprehensive vulnerability

databases, currently consisting of more than 66,400 recorded vulnerabilities (spanning more

than two decades) from over 21,300 vendors representing over 62,300 products.

Spam, phishing, and malware data is captured through a variety of sources including the

Symantec Probe Network, a system of more than 5 million decoy accounts, Symantec.cloud,

and a number of other Symantec security technologies. Skeptic™, the Symantec.cloud propri-

etary heuristic technology, is able to detect new and sophisticated targeted threats before

they reach customers’ networks. Over 8.4 billion email messages are processed each month

and more than 1.8 billion web requests filtered each day across 14 data centers. Symantec

also gathers phishing information through an extensive anti-fraud community of enterprises,

security vendors, and more than 50 million consumers.

Symantec Trust Services secures more than one million web servers worldwide with 100

percent availability since 2004. The validation infrastructure processes over 6 billion Online

Certificate Status Protocol (OCSP) look-ups per day, which are used for obtaining the revo-

cation status of X.509 digital certificates around the world. The Norton™ Secured Seal is

SHARE
THIS

displayed almost one billion times per day on websites in 170 countries and in search results

on enabled browsers.

These resources give Symantec analysts unparalleled sources of data with which to identify,

analyze, and provide informed commentary on emerging trends in attacks, malicious code

activity, phishing, and spam. The result is the annual Symantec Internet Security Threat

Report, which gives enterprises, small businesses, and consumers essential information to

secure their systems effectively now and into the future.

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SCAMS & SOCIAL MEDIA     TARGETED ATTACKS

5

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Executive Summary

If there is one thing that can be said about the threat landscape, and Internet
security as a whole, it is that the only constant is change. This can clearly be
seen in 2014: a year with far-reaching vulnerabilities, faster attacks, files held
for ransom, and far more malicious code than in previous years.

While 2013 was seen as the Year of the Mega Breach, 2014 had high-profile
vulnerabilities grabbing the headlines. Data breaches are still a significant
issue, since the number of breaches increased 23 percent and attackers were
responsible for the majority of these breaches. However, attention shifted
during the year from what was being exfiltrated to the way attackers could
gain access.

Vulnerabilities have always been a big part of the security picture, where
operating system and browser-related patches have been critical in keeping
systems secure. However, the discovery of vulnerabilities such as Heartbleed,
ShellShock, and Poodle, and their wide-spread prevalence across a number of
operating systems, brought the topic front and center. The conversation has
shifted from discussing “threat X that exploits a vulnerability” to detailing
how “vulnerability Y is used by these threats and in these attacks.”

This is one of many constants that changed in 2014. Based on the data
collected by the Symantec Intelligence network and the analysis of our
security experts, here are other trends of note in 2014.

Attackers Are Moving Faster, Defenses Are Not

Within four hours of the Heartbleed vulnerability becoming public, Symantec saw a surge of

attackers stepping up to exploit it. Reaction time has not increased at an equivalent pace.

Advanced attackers continue to favor zero-day vulnerabilities to silently sneak onto victims’

computers, and 2014 had an all-time high of 24 discovered zero-day vulnerabilities. As we

observed with Heartbleed, attackers moved in to exploit these vulnerabilities much faster

than vendors could create and roll out patches. In 2014, it took 204 days, 22 days, and 53

days, for vendors to provide a patch for the top three most exploited zero-day vulnerabilities.

By comparison, the average time for a patch to be issued in 2013 was only four days. The

most frightening part, however, is that the top five zero-days of 2014 were actively used by

attackers for a combined 295 days before patches were available.

SHARE
THIS

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SCAMS & SOCIAL MEDIA     TARGETED ATTACKS

6

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Attackers Are Streamlining and Upgrading Their Techniques,

While Companies Struggle to Fight Old Tactics

In 2014, attackers continued to breach networks with highly targeted spear-phishing attacks,

which increased eight percent overall. They notably used less effort than the previous year,

deploying 14 percent less email towards 20 percent fewer targets.

Attackers also perfected watering hole attacks, making each attack more selective by infecting

legitimate websites, monitoring site visitors and targeting only the companies they wanted to

attack.

Further complicating companies’ ability to defend themselves was the appearance of

“Trojanized” software updates. Attackers identified common software programs used by target

organizations, hid their malware inside software updates for those programs, and then waited

patiently for their targets to download and install that software—in effect, leading companies

to infect themselves.

Last year, 60 percent of all targeted attacks struck small- and medium-sized organizations.

SHARE
THIS

These organizations often have fewer resources to invest in security, and many are still not

adopting basic best practices like blocking executable files and screensaver email attachments.

This puts not only the businesses, but also their business partners, at higher risk.

Cyberattackers Are Leapfrogging Defenses in Ways Companies Lack Insight to Anticipate

As organizations look to discover attackers using stolen employee credentials and identify signs

of suspicious behavior throughout their networks, savvy attackers are using increased levels of

deception and, in some cases, hijacking companies’ own infrastructure and turning it against

them.

In 2014, Symantec observed advanced attackers:

•   Deploying legitimate software onto compromised computers to continue their attacks

without risking discovery by anti-malware tools.

•   Leveraging a company’s management tools to move stolen IP around the corporate network.

•   Using commonly available crimeware tools to disguise themselves and their true intention if

discovered.

•   Building custom attack software inside their victim’s network, on the victim’s own servers.

•   Using stolen email accounts from one corporate victim to spear-phish their next corporate

victim.

•   Hiding inside software vendors’ updates, in essence “Trojanizing” updates, to trick targeted

companies into infecting themselves.

Given all of this stealthy activity, it’s not surprising that Symantec Incident Response teams

brought in to investigate one known breach to an organization discovered additional breaches

still in progress.

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SCAMS & SOCIAL MEDIA     TARGETED ATTACKS

7

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Almost no company, whether large or small, is immune. Five out of

every six large companies (2,500+ employees) were targeted with

SHARE
THIS

spear-phishing attacks in 2014, a 40 percent increase over the previous year. Small- and

medium-sized businesses also saw an uptick, with attacks increasing 26 percent and 30

percent, respectively.

Malware Used In Mass Attacks Increases and Adapts

Non-targeted attacks still make up the majority of malware, which increased by 26 percent

in 2014. In fact, there were more than 317 million new pieces of

malware created last year, meaning nearly one million new threats
were released into the wild each day. Some of this malware may not be a direct risk to

SHARE
THIS

organizations and is instead designed to extort end-users. Beyond the annoyance factor to

IT, however, it impacts employee productivity and diverts IT resources that could be better

spent on high-level security issues.

Malware authors have various tricks to avoid detection; one is to spot security researchers

by testing for virtual machines before executing their code. In 2014, up to 28 percent of

all malware was “virtual machine aware.” This should serve as a wake-up call to security

researchers who are dependent on virtual sandboxing to observe and detect malware. It

also makes clear that virtual environments do not provide any level of protection. Certain

malware like W32.Crisis, upon detecting a virtual machine, will search for other virtual

machine images and infect them.

Digital Extortion on the Rise: 45 Times More People Had Their Devices Held Hostage in 2014

While most people associate “extortion” with Hollywood films and mafia bosses, cybercrim-

inals have used ransomware to turn extortion into a profitable enterprise, attacking big and

small targets alike.

Ransomware attacks grew 113 percent in 2014, driven by more than

a 4,000 percent increase in crypto-ransomware attacks. Instead of

SHARE
THIS

pretending to be law enforcement seeking a fine for stolen content, as we’ve seen with tradi-

tional ransomware, crypto-ransomware holds a victim’s files, photos and other digital media

hostage without masking the attacker’s intention. The victim will be offered a key to decrypt

their files, but only after paying a ransom that can range from $300-$500—and that’s no

guarantee their files will be freed.

In 2013, crypto-ransomware accounted for a negligible percentage of all ransomware attacks

(0.2 percent, or 1 in 500 instances). However, in 2014, crypto-ransomare was seen 45 times

more frequently. While crypto-ransomware predominately attacks devices running Windows,

Symantec has seen an increase in versions developed for other operating systems. Notably,

the first piece of crypto-ransomware on mobile devices was observed on Android last year.

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SCAMS & SOCIAL MEDIA     TARGETED ATTACKS

8

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Cybercriminals Are Leveraging Social Networks and Apps to Do Their Dirty Work

Email remains a significant attack vector for cybercriminals, but there is a clear movement

toward social media platforms. In 2014, Symantec observed that 70 percent of social media

scams were manually shared. These scams spread rapidly and are lucrative for cybercrimi-

nals because people are more likely to click something posted by a friend.

Mobile was also ripe for attack, as many people only associate cyber threats with their

PCs and neglect even basic security precautions on their smartphones. In 2014, Symantec

found that 17 percent of all Android apps (nearly one million total) were actually malware in

disguise. Additionally, grayware apps, which aren’t malicious by design but do annoying and
inadvertently harmful things like track user behavior, accounted for 36 percent of all mobile

apps.

Internet of Things Is Not a New Problem, But an Ongoing One

Symantec continued to see attacks against Point of Sales systems, ATMs, and home routers

in 2014. These are all network-connected devices with an embedded operating system,

though they’re not often considered part of the Internet of Things (IoT). Whether officially

part of the IoT or not, attacks on these devices further demonstrate that it’s no longer only

our PCs at risk. And the potential for cyberattacks against cars and medical equipment

should be a concern to all of us.

Risks to many IoT devices are exacerbated by the use of smartphones as a point of control.

Symantec discovered that 52 percent of health apps—many of which connect to wearable

devices—did not have so much as a privacy policy in place, and 20 percent sent personal

information, logins, and passwords over the wire in clear text.

Some of this may reflect the attitudes of end users. In a Norton survey, one in four admitted they

did not know what they agreed to give access to on their phone when downloading an application.

And 68 percent were willing to trade their privacy for nothing more than a free app.

SHARE
THIS

2015 Internet Security Threat Report
MOBILE & IOT     WEB THREATS     SCAMS & SOCIAL MEDIA     TARGETED ATTACKS

9

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

2
0
1
4
I

N
N
U
M
B
E
R
S

2015 Internet Security Threat Report

MOBILE & IOT     WEB THREATS     SCAMS & SOCIAL MEDIA     TARGETED ATTACKS

10

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

46
2014

57
2013

277
2014

231
2013

New Android Mobile
Malware Families

Cumulative Android
Mobile Malware
Families

48
2014

57
2013

9,839
2014

7,612
2013

New Android
Variants per Family

Cumulative Android
Mobile Malware
Variants

168
2014

127
2013

New Mobile Vulnerabilities

Grayware apps, which aren’t
malicious by design but do annoying
and inadvertently harmful things like
track user behaviour, accounted for
36 percent of all mobile apps.

6.3 M
2014

6.1 M
2013

1 M
2014

.7 M
2013

2.3 M
2014

2.2 M
2013

Total Apps
Analyzed

Total Apps
Classified
as Malware

Total Apps
Classified
as Grayware

App Analysis by Symantec’s
Norton Mobile Insight

SHARE
THIS

Symantec found that 17 percent of all
Android apps (nearly one million total)
were actually malware in disguise.

MOBILE
DEVICES

2015 Internet Security Threat Report

MOBILE & IOT     WEB THREATS     SCAMS & SOCIAL MEDIA     TARGETED ATTACKS

11

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

76+ 77

76%
2014

77%
2013

20+ 16+

20%
2014

16%
2013

Scanned Websites
with Vulnerabilities

Percentage of
Which Were Critical

496,657
2014

568,734
2013

Web Attacks Blocked per Day

1 in 1,126
2014

1 in 566
2013

Websites Found with Malware
Inverse Graph: Smaller Number = Greater Risk

1

2

3

4

5

SSL/TLS Poodle Vulnerability

Cross-Site Scripting

SSL v2 support detected

SSL Weak Cipher Suites Supported

Invalid SSL certificate chain

Top 5 Vulnerabilities Found Unpatched on
Scanned Web Servers

6,549
2014

6,787
2013

New Vulnerabilities

Within four hours of the Heartbleed
vulnerability becoming public, Symantec
saw a surge of attackers stepping up
to exploit it.

SHARE
THIS

WEB
THREATS

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SCAMS & SOCIAL MEDIA     TARGETED ATTACKS

12

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

60+ 66+

60%
2014

66%
2013

1 in 965
2014

1 in 392
2013

Overall Email
Spam Rate

Email Phishing Rate
Inverse Graph: Smaller Number = Greater Risk

23+ 81+

23%
2014

81%
2013

70+ 2+

70%
2014

2%
2013

In 2014, Symantec
observed that 70
percent of social
media scams were
manually shared.

Fake Offering
Social Media Scams

Manually Shared
Social Media Scams

SHARE
THIS

3,829
2014

6,993
2013

Average Number of Phishing URLs
on Social Media

28
Billion
2014

29
Billion
2013

Estimated Global
Spam Volume
per Day

SCAMS &
SOCIAL MEDIA

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SCAMS & SOCIAL MEDIA     TARGETED ATTACKS

13

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

841

779

18

23

25

29

Campaigns

Recipients per
Campaign

Average
Number of
Attacks per
Campaign

9
Days

8
Days

Average
Duration of a
Campaign

Spear Phishing Email Campaigns

   2014

   2013

SHARE
THIS

Industry

Mining

Wholesale

Manufacturing

Risk Ratio

   2014

   2013

1 in 2.3  44%
1 in 2.7  37%

1 in 2.9  34%
1 in 3.4  29%

1 in 3.0  33%
1 in 3.2  31%

Transportation,
Communications, Electric,
Gas & Sanitary Services

1 in 3.4  29%
1 in 3.9  26%

Public Administration
(Government)

1 in 3.4  29%
1 in 3.1  32%

Risk Ratio of Spear-Phishing Attacks by Industry

73
2014

83
2013

Spear Phishing
Emails per Day

Industry

   2014

   2013

Manufacturing

Services—
Nontraditional

Finance, Insurance
& Real Estate

Services—
Professional

Wholesale

20%
13%

20%
14%

18%
13%

11%
15%

10%
5%

Top 10 Industries Targeted in
Spear-Phishing Attacks

TARGETED
ATTACKS

2015 Internet Security Threat Report

MOBILE & IOT     WEB THREATS     SCAMS & SOCIAL MEDIA     TARGETED ATTACKS

14

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Individual Contributor

1 in 3.7  27%

Manager

Intern

Director

Support

1 in 3.8  26%

1 in 3.9  26%

1 in 5.4  19%

1 in 7.6  13%

Top 5 Risk Ratio of Spear-Phishing Attacks
by Job Level

Sales/Marketing

1 in 2.9  35%

Finance

Operations

R&D

IT

1 in 3.3  30%

1 in 3.8  27%

1 in 4.4  23%

1 in 5.4  19%

Top 5 Risk Ratio of Spear-Phishing Attacks
by Job Role

.doc

.exe

.scr

.au3

.jpg

39%

23%

9%

8%

5%

Spear-Phishing Emails Used
in Targeted Attacks

Last year, 60
percent of all
targeted attacks
struck small- and
medium-sized
organizations.

SHARE
THIS

34%
2014

30%
2013

25%
2014

31%
2013

41%
2014

39%
2013

Distribution of Spear-Phishing
Attacks by Organization Size

Small
Businesses
(SMBs)
1 to 250
Employees

Medium-Size
Businesses
251 to 2,500
Employees

Large
Enterprises
2,500+
Employees

Risk Ratio of Spear-Phishing
Attacks by Organization Size

45%
1 in 2.2

19%
1 in 5.2

63%
1 in 1.6

33%
1 in 3.5

83%
1 in 1.2

43%
1 in 2.3

2015 Internet Security Threat Report

MOBILE & IOT     WEB THREATS     SCAMS & SOCIAL MEDIA     TARGETED ATTACKS

15

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

In total, the top five zero-days of 2014 were
actively exploited by attackers for a combined
295 days before patches were available.

SHARE
THIS

4

19

2013

2014

59

Average Days to Patch by Vendor for Top 5 Zero-Days

Total Days of Exposure for Top 5 Zero-Days

295

81%  Microsoft ActiveX Control

10%  Microsoft Internet Explorer

7%  Adobe Flash Player

2%  Adobe Flash Player

<1%  Microsoft Windows

81%
Microsoft ActiveX
Control

25

20

15

10

5

)
S
D
N
A
S
U
O
H
T
(

d
e
t
c
e
t
e
D
s
k
c
a
t
t
A
f
o
r
e
b
m
u
N

0

25

50

75

100

125

150

175

200

225

250

275

300

Number of Days After Vulnerability Publication

Top 5 Zero-Day Vulnerabilities – Days of Exposure and Days to Patch
Source: Symantec

24
2014

23
2013

Zero-Day Vulnerabilities

2015 Internet Security Threat Report

MOBILE & IOT     WEB THREATS     SCAMS & SOCIAL MEDIA     TARGETED ATTACKS

16

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

312
2014

253
2013

348 M
2014

552 M
2013

1.1 M
2014

2.2 M
2013

7,000
2014

6,777
2013

Total Breaches

Total Identities
Exposed

Average Identities
Exposed per Breach

Median Identities
Exposed per Breach

The number of breaches increased 23 percent
in 2014. Attackers were responsible for the
majority of these breaches.

SHARE
THIS

4
2014

8
2013

Breaches with More Than 10 Million
Identities Exposed

Retail

205M

  59%

Financial

80M

  23%

Computer
Software

 35M

  10%

Healthcare

 7M   2%

Gov. & Public

7M   2%

Top 5 Sectors Breached
by Number of Identities Exposed

Healthcare

116

  37%

Retail

Education

Gov. & Public

Financial

34

31

26

19

  11%

  10%

  8%

  6%

Top 5 Sectors Breached by Number of Incidents

Real Names

Gov. ID Numbers
(e.g, SSN)

Home Addresses

Financial
Information

Birth Dates

  69%

  45%

  43%

  36%

  35%

Top 10 Types of Information Exposed

DATA
BREACHES

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SCAMS & SOCIAL MEDIA     TARGETED ATTACKS

17

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

317M
2014

252M
2013

1 in 244
2014

1 in 196
2013

New Malware Variants (Added Each Year)

Email Malware Rate
Inverse Graph: Smaller Number = Greater Risk

24 K
Per Day

11 K
Per Day

8.8 Million
2014

4.1 Million
2013

Ransomware Total

Ransomware attacks grew 113
percent in 2014, along with 45 times
more crypto-ransomware attacks.

In 2014, up to 28 percent of
all malware was “virtual
machine aware.”

SHARE
THIS

Item

2014 Cost

1,000 Stolen
Email Addresses

$0.50 to $10

Credit Card Details

$0.50 to $20

Scans of Real
Passports

Stolen Gaming
Accounts

$1 to $2

$10 to $15

Custom Malware

$12 to $3500

1,000 Social Network
Followers

$2 to $12

Stolen Cloud Accounts

$7 to $8

1 Million Verified
Email Spam Mail-outs

$70 to $150

Registered and
Activated Russian
Mobile Phone SIM
Card

$100

Value of Information
Sold on Black Market

1.9M
2014

2.3M
2013

Number of Bots

12 25

12%
2014

25%
2013

Email Malware as URL
vs. Attachment

E-CRIME
& MALWARE

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

18

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

M
O
B
I
L
E
D
E
V
I
C
E
S

&
T
H
E
I

N
T
E
R
N
E
T
O
F
T
H
N
G
S

I

2015 Internet Security Threat Report

MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

19

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Mobile Devices and the Internet of Things

With billions of smartphones and potentially many billions of Internet-connected devices of all
kinds, the focus of Internet security is shifting from the desktop and the data center to the home,
the pocket, the purse, and, ultimately, the infrastructure of the Internet itself.

At a Glance

 There are now more than

1 million malicious apps in
existence.

 Proof-of-concept attacks on

the Internet of Things are here,
including wearables, Internet
infrastructure, and even cars.

 Devices on the cusp of the
Internet of Things, such as
routers, network-attached
storage devices, and embedded
Linux devices, are already
under attack.

The falling number
of families doesn’t
indicate that
this problem is
going away but
just that the rate
of innovation
is slowing.

Mobile Malware

The tenth anniversary of mobile malware occurred in 2014. In 2004, researchers discovered
SymbOS.Cabir,1 a worm that spread through Bluetooth and targeted the Symbian OS, the most
popular mobile operating system at the time.2

Today many apps contain malware. As of 2014, Symantec has identified more than 1 million
apps that are classified as malware. This includes 46 new families of Android malware in 2014.
In addition, there are perhaps as many as 2.3 million “grayware” apps that, while not technically
malware, display undesirable behavior, such as bombarding the user with advertising.3

2014

2013

2012

46
–19%

57
-45%

103

16

New Android Mobile Malware Families
Source: Symantec

The falling number of families doesn’t indicate that this problem is going away but just that the
rate of innovation is slowing. This may be because existing malware is effective enough and there
is less demand for new software. In addition, the overall trend masks significant fluctuations
from month to month. The drop also suggests that developers are maximizing the number of
variants per family, for example, by repackaging well-known games and apps with malware.

Symantec expects the growth in mobile malware to continue in 2015, becoming more aggres-
sive in targeting a user’s money. Already 51 percent of U.S. adults bank online and 35 percent
use mobile phones to do so.4 This creates an incentive for malware writers to target phones
to capture bank details.5 Today, Android malware can intercept text
messages with authentication codes from your bank and forward them
to attackers. Fake versions of legitimate banks’ mobile applications also
exist, hoping to trick users into giving up account details.

SHARE
THIS

1  http://www.symantec.com/security_response/writeup.

jsp?docid=2004-061419-4412-99

2  http://www.symantec.com/connect/blogs/tenth-

anniversary-mobile-malware

3  http://www.symantec.com/connect/blogs/grayware-

casting-shadow-over-mobile-software-marketplace

4  http://www.pewinternet.org/2013/08/07/51-of-u-s-

adults-bank-online/

5  http://www.symantec.com/connect/blogs/future-

mobile-malware

2015 Internet Security Threat Report  New Android Mobile Malware FamiliesMOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

20

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

277

 In 2014 there were 46 new
mobile malware families
discovered.

300

250

200

150

100

50

71

231

174

2011

2012

2013

2014

16B

Cumulative Android Mobile Malware Families, 2011–2014
Source: Symantec

2014

2013

2012

17

New Android Variants per Family

Source: Symantec

 There was a 16 percent drop in
the number of Android variants
per family in 2014.

48
-16%

57
+50%

38

2015 Internet Security Threat Report  Cumulative Android Mobile Malware FamiliesNew Android Variants per Family MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

21

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

Millions

  6.3

  6.1

BACK TO TABLE OF CONTENTS

 Of the 6.3 million apps analyzed
in 2014, one million of these
were classified as malware, while
2.3 million were classified as
grayware.

 A further 1.3 million apps within
the grayware category were
classified as madware.

SHARE
THIS

2013
88

2012
50

   2014

   2013

   2012

  2.7

  2.3
  2.2

Total Apps Analyzed

Total Apps Classified
as Malware

  1

  .7

  .2

Total Apps Classified
as Grayware

Total Grayware Further
Classified as Madware

Known Ad Libraries

  1.4

  1.3
  1.2

2014
93

  .6

Malware Definition

Programs and files that are created to do harm.
Malware includes computer viruses, worms, and Trojan horses.

Grayware Definition

Programs that do not contain viruses and that are not obviously malicious
but that can be annoying or even harmful to the user (for example, hack
tools, accessware, spyware, adware, dialers, and joke programs).

Madware Definition

Aggressive techniques to place advertising in your mobile device’s photo
albums and calendar entries and to push messages to your notification bar.
Madware can even go so far as to replace a ringtone with an ad.

64

App Analysis by Symantec’s Norton Mobile Insight
Source: Symantec

2014

2013

2012

15

New Mobile Vulnerabilities

Source: Symantec

 There were 168 mobile

vulnerabilities disclosed in 2014,
a 32 percent increase compared
to 2013.

168
+32%

127
-69%

416

2015 Internet Security Threat Report  App Analysis by Symantec’s Norton Mobile InsightNew Mobile Vulnerabilities MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

22

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

2013

2014

 84% of mobile vulnerabilities
related to Apple iOS in 2014,
compared with 11% for Android,
4% for BlackBerry and 1% for
Nokia.

SHARE
THIS

82% 84%

13% 11%

1%

4%

0%

1%

iOS

Android

Blackberry OS

Windows
Phone

100%

80

60

40

20

63

Mobile Vulnerabilities by Operating System, 2013–2014
Source: Symantec

 Traditional threats increased 6

percentage points between 2013
and 2014, while threats that
steal information from the device
or track users declined in 2014.

2012

2013

2014

32

28

30

21

22

15

25

26

20

35%

30

25

20

15

10

5

13

11

8

9

8

7

13

10

8

Send
Content

Adware
Annoyance

Reconfigure
Device

Traditional
Threats

Steal
Information

Track
User

Send Content – Threats that send premium SMS, Spam and SEO Poisoning threats.

Adware/Annoyance – Threats that cause advertisement popups and unwanted information.

Reconfigure Device – Threats that modify user settings, and elevates privileges.

Traditional Threats – Threats like Backdoor Trojans, Downloaders, DDoS utility, Hacktool and Security Alerts.

Steal Information – Threats that steal device data, media files and any user credentials. Eg., Banking Trojan.

Track User – Threats that spy on users, tracks user location.

62

Mobile Threat Classifications, 2012–2014
Source: Symantec

2015 Internet Security Threat Report  Mobile Vulnerabilities by Operating SystemMobile Threat ClassificationsMOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

23

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

SMS and the Interconnected
Threat to Mobile Devices

by Lamine Aouad, Slawomir Grzonkowski,
Alejandro Mosquera, and Dylan Morss

The threat landscape is continually evolving, and with
the emergence of cheaper and readily available technol-
ogies and communication channels, it naturally attracts
malicious activity of all sorts. The shift from desktop PCs
to mobile devices as primary computing devices is a perfect
example of this. As more users rely on their mobile devices,
more spam, scams, and threats are tailored to these devices.

We suspect that the interconnectedness of apps on
smartphones has played a big part in this increase. This
interconnectedness has enabled a malicious source to send
an SMS that will open in a mobile browser by default, which
can be readily utilized to exploit the user.

SMS is far from a new technology; it’s older than the
smartphone itself. However, we’ve seen significant growth
in this area of the mobile landscape when it comes to how
scammers and attackers carry out their campaigns. SMS
and other mobile messaging technologies are readily being
used as a means to deliver all kinds of scam campaigns,
such as adult content, rogue pharmacy, phishing and
banking scams, payday loan spam, fake gifts, etc.

An important trend in 2014 was the proliferation of scam
campaigns. Although this category was not the most
prevalent, it certainly was one of the most dangerous
threats using SMS messages as its vector of attack. These
are targeted campaigns, of a range of scams and frauds,
addressed to selected potential victims, mainly scraped off

classified ad websites. Scammers send automated inquiries
about the advert via SMS. They also offer fictitious items
for sale, such as jobs and houses for rent, and interact with
potential victims by SMS, and then they switch to email for
communication. They typically use fake checks or spoofed
payment notifications to make victims ship their items or
to take victims’ deposits. Naturally victims never hear back
from them.

Another variant leads online dating users to fake age
verification websites that charge for a premium adult
subscription. For these adult scams, spammers initially
targeted mobile dating apps users and moved to SMS
afterward. These apps and social media sites were the main
sources that dating scammers used in 2014.

Most SMS scammers are posing as U.S. or Canadian
citizens or businesses running from other countries (many
were traced back to Nigeria). They abuse VoIP and cloud-
based mobile carriers and messaging services (the top two
services, namely Enflick and Integra5, accounted for more
than 90 percent of their traffic). They also abuse all sorts
of hosting, email, listing, and online payment and money
transfer services. These scams are not new and have been
running on email for quite some time; however, new mobile
platforms and technologies make it easier for scammers to
take advantage of the unsuspecting, especially when they
are using a relatively trusted medium like SMS. Online

buyers and sellers, as
well as those looking for
a job, apartment, or any
other service, should pay
close attention to the
details of each commu-
nication and be aware
that these scammers are
constantly improving
their fraudulent tactics.

Adult Content

Payday Loan

Bank / Account Phishing

Rogue Pharmacy

Scam

Others

38%

24%

11%

10%

9% 8%

0

100%

Top Categories of Observed SMS Spam, 2014
Source: Symantec

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

24

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

01 A typical Craigslist or PayPal11 scam, for
instance, would start with a message like

the following sent to hundreds of people scraped
off Craigslist:

02 The scammers have further discussions with
the victim via email and follow up with a text
message stating that they will be paying for the item
and shipping via PayPal:

11  PayPal has a Buyer and Seller Protection Program to

help protect against scams like this. For more information,

see the following link. https://www.paypal.com/webapps/

mpp/paypal-safety-and-security

03 The scammers send a confirmation email to
the victim’s PayPal account, from a fake
PayPal email address, claiming the funds have been
deducted from his or her account and will be
released to the victim once he or she ships the item:

04 If this is successful, the scammers can then track the
items to their doorstep and the victim never receives

any compensation for his or her items.

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

25

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Users should also be aware of the continually evolving
malware landscape. SMS has been seen as an infection
and propagation vector for many Trojans, worms, and SMS
agents. There are instances of malicious apps’ propagating
via SMS to infect new victims, which typically would be the
contact list. These are very short messages that look legit
but include links to malicious apps. Typical examples would
look like the following text messages to the right. These
malicious apps are monetized in different ways, mainly via
premium services and SMS subscriptions. They also leak
personal information and show affiliate ads.

The fact that an older technology, such as SMS, has become
such a popular propagation technique for scams and other
malicious activity highlights an important issue in the
mobile threat landscape: communication is becoming
more unified through new applications and services. In the
future, the underlying delivery technology will be irrele-
vant, regardless if it’s SMS, email, IM, or something new.
As different apps and technologies are becoming more and
more integrated, users will need to be aware that threats
can be delivered across a variety of areas.

Mobile malware will become harder to remove, for example, by using PCs as a way to infect attached phones
and by using bootkits to infiltrate a phone’s operating system.6 Like some rootkits for PCs, bootkits infect the
master boot record of a device so that the malware runs before the operating system is even loaded. The first
crypto-ransomware for Android devices appeared in 2014, giving criminals another way to earn money by
infecting phones and tablets—extortion.7

There are also wider privacy issues at stake. Not only can apps gain access to users’ private information,
but the phones themselves can also be used to invade people’s privacy. For example, this year researchers at
Stanford University were able to pick up audio and identify who was speaking by using the gyroscope in a
mobile phone.8

Mobile Apps and Privacy

An alarming percentage of apps collect and send personally identifiable information (PII) to app developers. A
survey carried out by Symantec, and published in December 2014,9 indicates that most consumers worry about
app security and privacy risks. However, the findings also suggest consumers are their own worst enemies when
it comes to mobile privacy.

Many consumers worry about device and data security, but, ironically, most are still willing to allow apps access
to their personal information. In fact, according to the survey, 68 percent of people will willingly trade their
privacy for a free app.

App users think they understand what they are agreeing to when downloading apps, but, in reality, they have
little understanding of common app permission practices and behaviors. For instance, over half of respondents
were unaware that apps could track their physical location (22 percent of the apps
scanned by Norton Mobile Insight track this information).

SHARE
THIS

6  http://www.symantec.com/connect/blogs/future-

mobile-malware

7  http://www.symantec.com/connect/blogs/simplocker-

first-confirmed-file-encrypting-ransomware-android

8  https://www.usenix.org/system/files/conference/

usenixsecurity14/sec14-paper-michalevsky.pdf

9  http://www.slideshare.net/symantec/norton-mobile-

apps-survey-report

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

26

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Internet of Things

The first Internet-connected appliance was a Coke machine at Carnegie
Mellon University back in 1982. It reported on stock levels and whether
newly loaded drinks were chilled.10 It was the snowflake that started an avalanche.

SHARE
THIS

The Internet of Things (IoT), embedded computing devices with Internet connectivity, embraces
a wide range of devices, including digital home thermostats, smart TVs, car systems (such as
navigation, entertainment, and engine management computers), networking devices, smart
watches, and activity trackers.

The diversity of threats mirrors the diversity of devices. In the past year, there has been a
growing number of probing and experimental attacks on a range of devices, as well as a few
serious attacks.

As the market for IoT devices has developed, it has become fragmented with a rich diversity in
low-cost hardware platforms and operating systems. Some attacks are already capable of exploit-
ing vulnerabilities in Linux-based IoT systems and routers; however, as market leaders emerge
and their ecosystems grow stronger, attacks against some devices will undoubtedly escalate. This
is likely to follow a path similar to the way that attacks against the Android platform reflected
the growth in its popularity in recent years.

Wearable Devices

Wearable fitness and personal health devices will be a $5 billion market by 201612 according
to analysts at Gartner. There are devices and apps already available for measuring our steps,
blood pressure, heart rate, and other intimate medical data, which can be stored online or on our
phones.

With countless Internet-connected wearable devices on the market and more coming, including
the highly anticipated Apple Watch, there is an obvious security and privacy threat.

Already, there have been proof-of-concept attacks on Fitbit devices13 and Symantec researchers
revealed significant vulnerabilities in many devices and applications in this area.14 In a review of
the 100 health apps in the App Store, 20 percent transmitted user credentials without encrypting
them, more than half (52 percent) did not have any privacy policies, and, on average, each app
contacted five Internet domains (typically a mix of advertising and analytics services).

The potential exposure of personal data from health-monitoring devices could have serious conse-
quences for individuals, for example, if insurance companies started to use the data to adjust
premiums, if people used hacked location data to track other people without their knowledge. In a
fast-moving and early-stage industry, developers have a strong incentive to offer new functional-
ity and features, but data protection and privacy policies seem to be of lesser priority.

10  https://www.cs.cmu.edu/~coke/history_long.txt

12  Garter, Market Trends: Enter the Wearable Electronics

Market With Products for the Quantified Self, Angela

McIntyre and Jessica Ekholm, 01 July 2013

As the market for
IoT devices has
developed, it has
become fragmented
with a rich diversity
in low-cost hardware
platforms and
operating systems.

13  https://securityledger.com/2013/05/fitbitten-

researchers-exploit-health-monitor-to-earn-workout-

rewards/

14  http://www.symantec.com/connect/blogs/how-safe-

your-quantified-self-tracking-monitoring-and-wearable-

tech

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

27

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Internet-Connected Everything

Computing and connectivity have enhanced our lives. Phones now play videos. Cars now have
navigation and entertainment systems. In our homes, lighting, heating, and cooling can be
controlled from an app. The possibilities are exciting, but there is also a dark side.

For example, in May 2014, the FBI and police in 19 countries arrested more than 90 people in
connection with “creepware”—using Internet-connected webcams to spy on people.15,16 Similarly,
as cars get “smarter” (meaning more digital and more connected), they are also at greater risk.
Researchers found that many cars are vulnerable to cyberattacks.17 Researchers were even able to
use a laptop to control a standard car.18

Automotive Security

by Shankar Somasundaram

The automotive industry is undergoing a number of big
changes. Cars are already powerful networks on wheels,
processing large quantities of data. In many cases, smart-
phones have already been integrated into car infotainment
systems. Auto manufacturers are also integrating Internet
connectivity into cars. This connectivity offers a variety of
useful features to the cars, ranging from predictive main-
tenance to downloading new features on an on-demand
basis. Standards around vehicle-to-vehicle (V2V) and vehi-
cle-to-infrastructure (V2I) communications are also being
developed, with initial trials already underway. A number
of players have also engaged in research on driverless cars,
which is progressing rapidly, adding further computing
power to the driving experience.

These developments have brought security and privacy
issues in the automotive industry to the forefront. Attacks
have already been demonstrated on different car manufac-
turers over the last couple of years.19,20

One attack surface is the websites and mobile apps provided
by the car manufacturer, which could be used to configure
or remotely control an Internet-enabled car. Symantec
internal research has found that a number of these car
manufacturers’ websites are not very well authenticated.
Another issue is that some of these websites and apps rely
upon the car’s unique vehicle identification number (VIN)
to identify it. A car can be easily controlled by spoofing
VINs through these websites and apps, by sending messages
to the targeted cars. If this seems farfetched, keep in mind
that in many cases a car’s VIN can be located near the base
of the windshield.

The most common attack surface is the OBD-II port, a diag-
nostic port that is kept in easily accessible locations within
most cars, as per regulations for maintenance and software
updates. The OBD-II port can be used to inject packets into
the car’s computer system, allowing control of the brakes,
ignition control unit, etc. Technically speaking, an attacker
could control any component within the car, even prevent-
ing the driver from accessing them via a denial-of-service
attack. The general argument against the validity of such
attacks has been that they require a physical connection
to the auto. However, with insurance providers’ and other
players’ providing wireless aftermarket units that can
connect to the OBD-II port, such physical connectivity is no
longer required.

If the back-end systems of companies providing devices
that connect to a car’s OBD-II port are compromised, then
remote attacks on the car can be launched through these
systems. In fact, compromised back-end systems, such as
servers collecting and storing data from the devices, could
become launch pads for attacks through multiple vendors,
ranging from repair shops to the auto manufacturers them-
selves.

A compromised smartphone or malicious application on a
phone is also a potential medium for attacking a car. For
example, if a compromised device is charged via a vehicle’s
USB port, the vehicle is susceptible to being attacked. The
increasing popularity of 4G, picocells,21 and Home Node Bs22
has also created a way to connect to and launch attacks over
a cellular interface.

15  http://www.cnn.com/2014/05/19/justice/us-global-

hacker-crackdown/

who-s-watching-you

16  http://www.symantec.com/connect/blogs/creepware-

17  http://www.wired.com/2014/08/car-hacking-chart/

18  http://www.bbc.co.uk/news/technology-23443215

19  http://www.forbes.com/sites/

andygreenberg/2013/07/24/hackers-reveal-nasty-new-

car-attacks-with-me-behind-the-wheel-video/

20  http://www.cbsnews.com/news/car-hacked-on-60-

minutes/

21  http://en.wikipedia.org/wiki/Picocell

22  http://en.wikipedia.org/wiki/Home_Node_B

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

28

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Another big threat vector is the infotainment unit, which
controls the USB port, CD player, and other popular devices.
Researchers at University of Washington and University
of California, San Diego,23 have demonstrated how attacks
on a car can be carried out by compromising CD-ROMs
or Bluetooth interfaces. Once the infotainment system is
compromised, other units in the car can be attacked as well.

Another interesting, albeit less effective, threat has been
tire pressure sensors. Attackers have demonstrated how
wireless signals at the right frequency can be used to send
conflicting signals to the tire pressure controller, possibly
causing warning lights on the dashboard to turn on or, even
worse, crash the controllers that connect to the tire pressure
sensors, risking loss of control of the vehicle. However, such
attacks need to be done at short range and require wireless
expertise, in addition to particular hacking skills, making
them more difficult to carry out.

While the above scenarios are critical from a security
perspective, there are also issues around privacy. With the
amount of data being generated by the car, as well as the
user details that the car stores, questions like “Who owns the
data?” and “How is the data being secured?” become critical
issues. Privacy issues will start to get more severe as V2V and
V2I technologies become more popular. In scenarios where
user anonymity and privacy must be maintained, authentica-
tion will need to be carried out on an extremely large scale.

Symantec is conducting extensive research in this field,
working directly with automobile manufacturers to perform
vulnerability analysis of different features and components
and providing aftermarket assessment. While auto manu-
facturers are separating out the critical and noncritical
components of the car to ensure security, much more needs
to be done. Symantec advocates end-to-end security to help
address the problem. These solutions range from authenti-
cation, ensuring only signed code is executed, securing the
infotainment and telematics units and applications that
run on them, and then monitor them by using analytics
to monitor abnormal activity, and ensuring the car’s
software can be updated remotely as needed. Some of these
approaches must be incorporated during the design phase
itself. How these solutions are implemented is equally
important, since improper implementation could be just as
ineffective as no security at all.

The future of Internet-enabled cars is bright and full of
potential. The next phase of V2V communication, as well as
driverless cars, will bring in a lot more connectivity. It will
also increase the attack surface, as cars will autonomously
communicate with each other and the infrastructure around
them. It is all the more important that we understand and
take action on the security issues now, before the challenges
become too big to surmount.

23  http://www.autosec.org/pubs/cars-usenixsec2011.pdf

The Network As the Target

The Internet is made up of hubs, switches, and routers that move information from place to place.
These devices, from retail home routers to form-factor network-attached storage devices, are at the
very least close cousins in the emerging IoT device space. They have processing, storage, and Internet
connectivity and in many ways function just like more strictly defined IoT devices.

These types of devices are already under attack and can be seen as harbingers of what is to come in the
larger IoT space.

For example, in August 2014 some Synology network-attached storage devices were infected by
ransomware.24 At the end of 2013, Symantec researchers discovered a new Linux worm called Darlloz25
that targeted small Internet-enabled devices such as home routers, set-top boxes, and security
cameras.26 By March 2014, Symantec identified 31,716 devices that were infected with this malware.27
Attackers can use freely available tools, such as the Shodan search engine, to search for Internet-en-
abled devices such as security cameras, heating control systems in buildings, and more.28

Symantec expects to see further malware development and attacks on the Internet of Things as
criminals find new ways to make money from doing so. For example, some attackers have used Darlloz
to mine for crypto-currencies similar to bitcoins. Other attackers have leveraged hacked routers to
carry out distributed denial-of-service attacks.29 Experience with PCs and, more recently, with mobile
malware suggests that where there is opportunity created by technical exploits and motivation, such as
greed, vindictiveness, or revenge, there will be cyberattacks.

24  https://www.synology.com/en-us/company/news/

article/Synology_Encourages_Users_to_Update_as_

SynoLocker_Ransomware_Affects_Older_DSM_Versions/

Synology%C2%AE%20Encourages%20Users%20to%20

Update%20as%20SynoLocker%20Ransomware%20

Affects%20Older%20DSM%20Versions

25  http://www.symantec.com/security_response/writeup.

jsp?docid=2013-112710-1612-99

26  http://www.symantec.com/connect/blogs/

linux-worm-targeting-hidden-devices

27  http://www.symantec.com/connect/blogs/iot-worm-

used-mine-cryptocurrency

28  http://www.symantec.com/connect/blogs/internet-

things-new-threats-emerge-connected-world

29  http://krebsonsecurity.com/2015/01/lizard-stresser-

runs-on-hacked-home-routers/

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

29

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Medical Devices – Safety First, Security Second

by Axel Wirth

Medical devices are notoriously insecure and easy to hack,
as has been demonstrated for pacemakers and30 insulin
pumps,31 as well as surgical and anesthesia devices, venti-
lators, infusion pumps, defibrillators,
patient monitors, and laboratory
equipment.32

SHARE
THIS

The concerns voiced by security researchers, government
regulators, and healthcare providers are well founded as any
medical device cybersecurity incident could seriously harm
patients. Because medical devices are so closely tied in with
the care process any compromise may also adversely affect
care delivery and hospital operations.

It is also a topic in the public eye, as we have seen through
the press coverage of former Vice President Dick Cheney,
who had the remote features of his pacemaker turned off.33
These types of incidents were even dramatized in TV crime
series like “Homeland” (Showtime) and “Person of Interest”
(CBS).

2014 can be considered the year when medical device
security became a mainstream topic and change started to
happen. The US Department of Homeland Security,34 the
FBI,35 and the FDA,36 as well as international regulators
issued warnings and expressed their concerns about the
need to improve the cybersecurity of our medical device
ecosystem.

There are reasons why medical devices are highly
vulnerable:

 Medical devices have a long, useful life.

 The design, manufacturing, and sale of medical devices
are highly regulated. Although regulations typically do
not prevent manufacturers from including or updating
device cybersecurity, they do mandate a time-consuming
release process and test cycle, which can delay availabili-
ty of security patches.

 Medical devices are used 24x7 and may be difficult
to find time for upgrades, especially since groups of
devices need to be upgraded together to maintain opera-
tional compatibility.

 Since medical devices are periodically on and off the
hospital network as patient come and go, removal of
malware from compromised devices may be operation-
ally difficult. Given some malware’s ability to reinfect
cleaned devices, all vulnerable devices may need to
be cleaned at once, requiring all impacted patients to
come to the hospital at one time: a scheduling challenge
in-and-of itself.

The most important risk scenarios to be aware of are
those that target medical devices with the goal to harm a
patient. Life-sustaining devices like pacemakers or insulin
pumps can be hacked. Fortunately, to-date no such case has
been reported outside proof-of-concept security research;
however, the potential impact remains high.

Another situation that many healthcare providers struggle
with are poorly patched devices, often running end-of-life
operating systems. These highly vulnerable devices are a
problem not because they are targeted, but because of their
susceptibility to common malware. The impact is mainly
operational, but cases have been reported where emergency
patients have had to be rerouted to other hospitals due to
malware infections of diagnostic equipment.37

Medical device vulnerabilities could also be used for an
attack on a hospital. Attackers could exploit a device and
use it as an entry point for a larger targeted attack, with
the goal of damaging the reputation of a healthcare facility
or instilling fear in the population as part of a hacktivist,
cybervandalism, or even a cyberterrorism attack.

For practical and regulatory reasons, the responsibility
for securing the actual device itself lies mainly with the
manufacturers. However, hospitals also need to assure that
their biomedical engineers are trained to work with their
IT department to build secure networks for medical devices
and include cybersecurity considerations in their buying
decisions. Solutions to secure their devices and device
networks do exist, and can be applied by manufacturers or
healthcare providers.

30 “A Heart Device Is Found Vulnerable to Hacker

Attacks”; New York Times; Mar. 2008; http://www.nytimes.

com/2008/03/12/business/12heart-web.html?_r=0

31 https://www.gartner.com/doc/2537715/market-

trends-enter-wearable-electronics

32  U.S. Department of Homeland Security, Industrial

Control System Cyber Emergency Response Team, (ICS-

CERT); ALERT-13-164-01; https://ics-cert.us-cert.gov/

alerts/ICS-ALERT-13-164-01

33  U.S. “Yes, terrorists could have hacked Dick Cheney’s

heart”; The Washington Post; Oct. 21, 2013; http://www.

washingtonpost.com/blogs/the-switch/wp/2013/10/21/

yes-terrorists-could-have-hacked-dick-cheneys-heart/

34 “Feds Probe Cybersecurity Dangers in Medical

Devices”; IEEE Spectrum; Oct. 27, 2014; http://spectrum.

ieee.org/tech-talk/biomedical/devices/feds-probe-

cybersecurity-dangers-in-medical-devices

37 “Medical-device security isn’t tracked well, research

shows”; Network World; July 19, 2012; http://www.

networkworld.com/article/2189998/data-center/medical-

device-security-isn-t-tracked-well--research-shows.html

35 “Health Care Systems and Medical Devices at Risk

for Increased Cyber Intrusions for Financial Gain”; U.S.

Federal Bureau of Investigation (FBI) Cyber Division,

Private Industry Notice #140408-009; April 8, 2014

36 “Content of Premarket Submissions for Management

of Cybersecurity in Medical Devices: Guidance for

Industry and Food and Drug Administration Staff”;

U.S. Food and Drug Administration, Center for Devices

and Radiological Health (FDA CDRH); October 2, 2014;

http://www.fda.gov/downloads/MedicalDevices/

DeviceRegulationandGuidance/GuidanceDocuments/

UCM356190.pdf

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

30

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

 Asset management and risk analysis are critical

to minimize the security risks of medical devices.
Automated tools to support these activities do exist and
standards and best practices are being put forward, for
example the IEC 80001 series on risk management of
medical device networks.

 Host Intrusion Detection and Prevention (HIDS/HIPS)
is a security technology installed on the device itself
that effectively excludes any undesired programs or an
unauthorized user.

 Encryption can be used to protect patient data, but also
to prevent data from being manipulated with the goal to
change system settings.

 Device and software certificates can be used to control
use of devices and deployment of device software and
upgrades, minimizing the risk of unauthorized code
being installed.

 Network-based security technologies, like Firewalls and
Security Gateways, can be used to detect an external
attack, but also to identify any devices that may be
compromised by detecting connections to malicious
external sources.

Medical device security is not only a challenge of today’s
healthcare ecosystem. Under the evolving umbrella of
mobile health, or mHealth, new care delivery models
will move devices into the patient’s home. This will place
medical devices on public networks, provide medical apps
through consumer devices such as smartphones, and
interlace personal data with clinical information.

With the evolving concept of “care is everywhere” we need
to deal with cybersecurity, but also privacy concerns. The
device will not only provide clinical information, but also
information about patient behavior and location. Once
again, it seems that regulations will have to catch up with
technology. We will need new guidelines to address the new
risks of information use, data ownership, and consent.

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

31

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

W
E
B
T
H
R
E
A
T
S

2015 Internet Security Threat Report
MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

32

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Web Threats

Web threats got bigger and much more aggressive in 2014 as holes in commonly used tools
and encryption protocols were exposed and criminals made it harder to escape their malicious
clutches.

At a Glance

 The Heartbleed vulnerability
left approximately half a
million trusted websites at risk
of significant data breaches in
April.38

SHARE
THIS

 The Heartbleed scare caused

many more people to take note
and improve standards in SSL
and TLS implementation.

 Criminals are taking advantage

of the technology and
infrastructure that legitimate
ad networks have created to
distribute malicious attacks
and scams.

 A big jump to 5 percent of total
infected websites has bumped
anonymizer sites into the top
10 types of infected sites for
2014.

 The total number of sites found
with malware has virtually
halved since 2013.

38 http://www.symantec.com/connect/blogs/freak-

vulnerability-can-leave-encrypted-communications-open-

attack

39  http://www.symantec.com/connect/blogs/freak-

vulnerability-can-leave-encrypted-communications-open-

attack

40  http://www.symantec.com/connect/blogs/heartbleed-

bug-poses-serious-threat-unpatched-servers

41  http://news.netcraft.com/archives/2014/04/08/

half-a-million-widely-trusted-websites-vulnerable-to-

heartbleed-bug.html

42  http://www.symantec.com/connect/blogs/heartbleed-

reports-field

The web presented an incredibly threatening landscape in 2014, a trend set to continue in 2015.
Vulnerabilities and new variants of malware underlined that website security deserves full-time,
business-critical attention.

Vulnerabilities

Vulnerabilities grabbed the headlines in 2014, and they continue to do so. At the time of writing,
a new SSL/TLS vulnerability dubbed “FREAK” had been identified by several security research-
ers.39 FREAK allows man-in-the-middle attacks on encrypted communications between a website
visitor and website, which ultimately could allow attackers to intercept and decrypt communi-
cations between affected clients and servers. Once the encryption is broken by the attackers,
they can steal passwords and other personal information and potentially launch further attacks
against the affected website.

Looking back at 2014, three vulnerabilities disclosed in particular grabbed the news headlines.

Heartbleed

Heartbleed hit the headlines in April 2014, when it emerged that a vulnerability in the OpenSSL
cryptographic software library meant attackers could access the data stored in a web server’s
memory during an encrypted session. This session data could include credit card details,
passwords, or even private keys that could unlock an entire encrypted exchange.40

At the time, it was estimated that Heartbleed affected 17 percent of SSL web servers, which use
SSL and TLS certificates issued by trusted certificate authorities.41 This had a massive impact on
businesses and individuals.

Not only was a great deal of sensitive data at risk, but the public also had to be educated about
the vulnerability so they knew when to update their passwords. Website owners had to first
update their servers to the patched version of OpenSSL, then install new SSL certificates, and
finally revoke the old ones. Only then would a password change be effective against the threat,
and communicating that to the general public posed a real challenge.

Fortunately, the response was swift and within five days none of the websites included in
Alexa’s top 1,000 were vulnerable to Heartbleed and only 1.8 percent of the top 50,000 remained
vulnerable.42

ShellShock and Poodle

Heartbleed wasn’t the only vulnerability to come to light in the online ecosystem in 2014. In
September a vulnerability known as “Bash Bug” or “ShellShock,” which affected most versions of
Linux and Unix as well as Mac OS X, was discovered. ShellShock was a particularly good example
that highlighted how quickly the security landscape could change for website owners; one day
their servers are securely patched and up to date, and then, very suddenly, they are not and many
of the initial patches are incomplete and must be patched again.

The easiest route of attack was through web servers, as attackers could use Common Gateway
Interface (CGI), the widely used system for generating dynamic web content, to add a malicious

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

33

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

43  For those unfamiliar with UNIX terminology, a shell

is a command line user interface for interacting with the

operating system. In this case, Bash is one of the most

widely used shells in all of the UNIX and Linux worlds.

BACK TO TABLE OF CONTENTS

Heartbleed and
ShellShock could be
viewed as a different
class of vulnerability
altogether.

44  http://www.symantec.com/connect/blogs/shellshock-

all-you-need-know-about-bash-bug-vulnerability

45 http://www.symantec.com/connect/blogs/poodle-

vulnerability-old-version-ssl-represents-new-threat

command to an environmental variable. The Bourne Again Shell (Bash),43 the server
component containing the vulnerability, would then interpret the variable and run it.44

Numerous threats took advantage of ShellShock, exposing servers and the networks to which
they were connected, to malware that could infect and spy on multiple devices.

Attention then turned back to encryption in October 2014, when Google discovered a vulner-
ability known as Poodle. Potentially, this vulnerability allowed criminals to exploit servers
that supported an older SSL protocol known as SSL 3.0. It interfered with the “handshake”
process that verified the server’s protocol forcing it to use SSL 3.0—even if a newer protocol was
supported.45

A successful exploit allows attackers to carry out man-in-the-middle attacks to decrypt secure
HTTP cookies, which then lets them steal information or take control of victims’ online accounts.
Fortunately, this was not as serious as Heartbleed. To take advantage of the Poodle vulnerabil-
ity, the attacker would need to have access to the network between the client and server—for
instance, through a public Wi-Fi hotspot.

High-Profile Vulnerabilities and Time to Patch

The attacks that quickly followed the announcement of these vulnerabilities were big news in
and of themselves, albeit in a different manner than attention-grabbing zero-day vulnerabili-
ties. Heartbleed and ShellShock could be viewed as a different class of vulnerability altogether,
because they were used to compromise servers instead of end points. The key factor with these
high-profile vulnerabilities was the prevalence of the software they affected, found in so many
systems and devices. Given the software’s widespread existence, these vulnerabilities instantly
became hot targets for attackers, and both were exploited within hours of disclosure.

Heartbleed Attacks

ShellShock Attacks

April 7 2014:
“Heartbleed”
Vulnerability
Reported
(CVE-2014-0160)

Sep 24 2014:
“ShellShock”
Vulnerability
Reported
(CVE-2014-6271)

 The large spikes seen in the chart
demonstrate that while Symantec
signatures were in place to
detect and block attacks almost
immediately after disclosure,
there were already a large
number of attacks underway.
Attackers were able to exploit the
Heartbleed vulnerability within
four hours of it becoming public.

S
D
N
A
S
U
O
H
T

35

30

25

20

15

10

5

M

J

J

A

S

O

N

70

Heartbleed and ShellShock Attacks, April–November, 2014
Source: Symantec

2015 Internet Security Threat Report  Heartbleed and ShellShock AttacksMOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

34

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

The Vulnerability Rises

By Tim Gallo

Over the past few years the idea of vulnerability manage-
ment has been frequently talked about but was often seen
as an annoyance or a process that, while interesting, isn’t
as important as breach response or adversary tracking.
However, 2014 gave vivid examples of the importance of
addressing vulnerabilities. Three major vulnerabilities were
in the news—and not just security industry news—including
coverage by major media news outlets. They were colloqui-
ally known as Poodle, ShellShock, and Heartbleed.

 The Heartbleed vulnerability

even got its own logo.

Each of these vulnerabilities was discovered in areas tradi-
tionally not covered by most vulnerability management
processes at the time. These processes have, as of late, been
focused on laptops and servers, thanks to the regularity of
publicized vulnerabilities by Adobe and Microsoft and these
companies’ speed in releasing patches. While we have seen,
and will continue to see, new vulnerabilities in these appli-
cations, solid processes have been established here in patch
deployment, vulnerability disclosure, and overall patch
management processes.

SHARE
THIS

It is this automation of patch
deployment by operating system
and application vendors that has forced attackers to shift
their tactics somewhat. Attackers have moved to new
methods of exploitation—or perhaps more accurately, they
have moved back into the vulnerability research game. This
shift back to combing through applications more thorough-
ly on the attacker’s part has resulted in vulnerabilities being
discovered in areas previously thought to be secure.

Let’s take one of these vulnerabilities, ShellShock, as an
example of what we will likely see in the coming years.
ShellShock was, at best, a flawed feature and, at worst, a
design flaw, in the Bourne Again Shell (Bash) that went

overlooked for over 25 years before it was discovered to be
exploitable, and subsequently disclosed publicly. ShellShock
has been a part of the fabric of the Internet for most of
the Internet’s existence. In fact, the targets of ShellShock
weren’t just routers or Linux web servers but also email
servers and even DDoS bots that utilize the shell—anything
Unix-based that makes use of Bash.

We will likely continue to see vulnerabilities like this as the
new normal for the coming years, for a few reasons. For
starters, it is now apparent that the attackers are not going
to rely on reusing the same old methods and the same old
exploits. They are instead investing in researching new
vulnerabilities in frequently used, older infrastructure that
provides a broad attack surface.

These three high-profile vulnerabilities were also inter-
esting because not only did they expose flaws in major
components of Internet infrastructure, but they highlighted
one of the dirty secrets of application development as well:
code reuse. Code reuse is when a developer copies sections
of code from existing applications for use in development of
new applications. It is this practice, which has been around
for as long as coding has existed, that can lead to vulnera-
bilities’ being present in systems that may be completely
unrelated.

When looking at the situation that led up to the Heartbleed
discovery, legitimate uses of the OpenSSL library were a
perfect example of code reuse. This code had long been seen
as reliable and often went untested, as it was considered “a
solved problem.” However, new vulnerabilities in the library
were discovered and developers around the globe had to
scramble to determine if their code reuse implementations
were vulnerable.

Additionally, we have seen a rise in bug bounty programs,
and we no longer see governments threatening vulnerability
researchers with jail time as in years past.46 Therefore, the
incentive to research vulnerabilities has increased and the
repercussions of irresponsible disclosure, or even outright
mercenary behavior, are no longer something researchers
fear.

46  http://www.wired.com/2013/03/att-hacker-gets-3-

years

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

35

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

However, what we will also hopefully see is that remediation
and better security practices will become more prevalent.
It takes the average IT professional only a few weeks of
all-nighters to decide that planning ahead is far more
advantageous. Better enforcement of configuration, policy,
and patching across entire infrastructures will help. The
moving of infrastructure to the cloud will help an over-
worked IT professional manage these issues as well.

As we look at the “detect and remediate” cycle of security,
the return of vulnerabilities is a key point in understanding
the threat landscape. To become more effective security
professionals, we need to additionally think about how we

“protect and respond” and “inform and assess” as well.
That means we need to become better planners and testers,
look to intelligence to help keep us informed, and know
our environment well enough to understand whether that
intelligence is actionable.

We need to better understand that the fabric of the Internet
is likely still riddled with holes, and it is our responsibility
to maintain vigilance in order to be prepared to deal with
new vulnerabilities as they are disclosed in a process-ori-
ented and programmatic manner. To not do so would be
detrimental to our future.

SSL and TLS Certificates Are Still Vital to Security

It’s important to note that while online security was shaken in 2014, SSL certificates and their
more modern counterparts, TLS certificates, still work and are still essential. In fact, the Heart-
bleed incident demonstrated just how quickly the online security community could respond to
these types of threats.

Industry standards are also constantly improving thanks to the hard work and vigilance of
organizations like the CA/Browser Forum, of which Symantec is a member. In other words, the
foundations of Internet security, which keep your site and visitors safe, are still strong and are
only getting stronger.

Vulnerabilities as a Whole

2014

2013

2012

27

New Vulnerabilities
Source: Symantec

 The overall number of

vulnerabilities declined
3.5 percent in 2014.

6,549
-3.5%

6,787
+28%

5,291

2015 Internet Security Threat Report  New VulnerabilitiesMOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

36

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

 While reported vulnerabilities

represent a general risk, zero-day
vulnerabilities are potentially
much more serious. These
are vulnerabilities that are
discovered only after they are
exploited by attackers. See the
chapter on Targeted Attacks for
further coverage on zero-day
vulnerabilities.

6,253

5,562

4,842

4,644

4,814

5,291

4,989

6,787

6,549

8,000

7,000

6,000

5,000

4,000

3,000

2,000

1,000

2006

2007

2008

2009

2010

2011

2012

2013

2014

52

Total Number of Vulnerabilities, 2006–2014
Source: Symantec

891

591

639

Opera

Mozilla Firefox

Microsoft Internet
Explorer

Google Chrome

Apple Safari

 There was a 8 percent increase

in the number of browser
vulnerabilities reported in 2014.

 Microsoft Internet Explorer
reported the largest number
of vulnerabilities, followed by
Google Chrome.

SHARE
THIS

1,000

800

600

400

351

200

2011

2012

2013

2014

54

Browser Vulnerabilities, 2011–2014
Source: Symantec

2015 Internet Security Threat Report  Total Number of VulnerabilitiesBrowser VulnerabilitiesMOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

37

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Java

Apple

Adobe

ActiveX

 With a total of 336

vulnerabilities, there was a 10
percent decrease in the number
of plug-in vulnerabilities reported
in 2014.

 Adobe, with its Acrobat and
Flash plugins, disclosed the
largest number of vulnerabilities,
followed by Oracle and its Java
plug-in.

 As was the case in 2013, SSL and
TLS vulnerabilities were most
commonly exploited in 2014.

SHARE
THIS

80

70

60

50

40

30

20

10

J
2013

JMAMF

DNOSAJ

J
2014

JMAMF

DNOSAJ

55

Plug-in Vulnerabilities by Month, 2013–2014
Source: Symantec

Rank

Name

1

2

3

4

5

6

7

8

9

SSL/TLS Poodle Vulnerability

Cross-Site Scripting

SSL v2 support detected

SSL Weak Cipher Suites Supported

Invalid SSL certificate chain

Missing Secure Attribute in an Encrypted Session (SSL) Cookie

SSL and TLS protocols renegotiation vulnerability

PHP 'strrchr()' Function Information Disclosure vulnerability

http TRACE XSS attack

10

OpenSSL 'bn_wexpend()' Error Handling Unspecified Vulnerability

Top 10 Vulnerabilities Found Unpatched on Scanned Web Servers

28B

Source: Symantec

2015 Internet Security Threat Report  Plug-In Vulnerabilities by MonthTop 10 Vulnerabilities Found Unpatched  on Scanned WebserversMOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

38

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

 In 2014, 20 percent (1 in 5) of
all vulnerabilities discovered
on legitimate websites were
considered critical, meaning they
could allow attackers to access
sensitive data, alter the website’s
content, or compromise visitors’
computers.

SHARE
THIS

 The number of websites found
with malware decreased by
nearly half in 2014.

76

76%
-1%

2014

77

77%
+25% pts

2013

Scanned Websites with Vulnerabilities

20

20%
+4%

2014

16

16%
-8% pts

2013

28

Percentage of Which Were Critical
Source: Symantec

2014

2013

2012

55

55%

2012

24

24%

2012

1 in 1,126

1 in 566

1 in 532

30

Websites Found with Malware
Source: Symantec

Inverse Graph: Smaller Number = Greater Risk

2015 Internet Security Threat Report  Scanned Websites with Vulnerabilities Percentage of Which Were CriticalWebsites Found with MalwareMOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

39

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

 In terms of the type of websites
most frequently exploited, it’s
interesting to note the inclusion
of anonymizer websites in the
top 10 this year. This is perhaps
another case of criminals
following the crowds as more
people look to evade tracking
by ISPs and others and increase
their browsing privacy.

Rank

2014 Top 10 Most
Frequently Exploited
Categories of Websites

2014 Percentage
of Total Number of
Infected Websites

2013
Top 10

2013
Percentage

Technology

21.5%

Technology

1

2

3

4

5

6

7

8

9

Hosting

Blogging

Business

Anonymizer

Entertainment

Shopping

Illegal

Placeholder

7.3%

7.1%

6.0%

5.0%

2.6%

2.5%

2.4%

2.2%

1.8%

Business

Hosting

Blogging

Illegal

Shopping

Entertainment

Automotive

Educational

9.9%

6.7%

5.3%

5.0%

3.8%

3.3%

2.9%

1.8%

1.7%

10

Virtual Community

Virtual Community

1.7%

51

Classification of Most Frequently Exploited Websites, 2013–2014
Source: Symantec

2013

2014

TREND

 For the most part, the bulk of
the 12.7% drop in the average
number of daily attacks blocked
occurred in the latter half of
2013. The decline in attacks
throughout 2014 has been much
more shallow than in 2013.

800

700

600

500

400

300

200

100

S
D
N
A
S
U
O
H
T

J

F

M

A

M

J

J

A

S

O

N

D

50B

Web Attacks Blocked per Month, 2013–2014
Source: Symantec

2015 Internet Security Threat Report  Classification of Most Frequently Exploited WebsitesWeb Attacks Blocked per MonthMOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

40

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

 A 47 percent drop in unique

malicious web domains in 2014
could indicate an increase in the
use of cloud-based SaaS-type
toolkits.

 The number of web attacks
blocked per day dropped 13
percent in 2014.

29,927
-47%

56,158
-24%

74,001
+34%

55,000

496,657
-13%

568,734
+23%

464,100

2014

2013

2012

2011

19

New Unique Malicious Web Domains
Source: Symantec

2014

2013

2012

20

Web Attacks Blocked per Day

Source: Symantec

2015 Internet Security Threat Report  New Unique Malicious Web Domains  Web Attacks Blocked per Day  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

41

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

With minor fluctuations from year to year, the trend in the number of vulnerabilities continues
upward. Remedies, workarounds, or patches are available for the majority of reported vulner-
abilities. However, malware authors know that many people do not apply these updates and
so they can exploit well-documented vulnerabilities in their attacks. In many cases, a special-
ist “dropper” scans for a number of known vulnerabilities and uses any unpatched security
weakness as a back door to install malware. This, of course, underlines the crucial importance
of applying updates.

This is how web exploit toolkits, such as Sakura and Blackhole, have made it easier for attackers
to exploit an unpatched vulnerability published months or even years previously. Several
exploits may be created for each vulnerability, and a web attack toolkit will perform a vulnerabil-
ity scan on the browser to identify any potentially vulnerable plug-ins and the best attack that
can be applied. Many toolkits won’t utilize the latest exploits for new vulnerabilities if old ones
will suffice. Exploits against zero-day vulnerabilities are uncommon and highly sought after by
attackers, especially for use in watering-hole-style targeted attacks.

Compromised Sites

Three-quarters of the websites Symantec scanned for vulnerabilities in 2014 were found to have
issues—about the same as last year. The percentage of those vulnerabilities classified as critical,
however, increased from 16 to 20 percent.

In contrast, the number of websites actually found with malware was much lower than last year,
down from 1 in 566 to 1 in 1,126. This seems to have had a knock-on effect on the number of
web attacks blocked per day, which has also declined, though only by 12.7 percent, suggesting
infected websites were, on average, responsible for more attacks in 2014. This is due to the fact
that some web attack toolkits are designed to be used in the cloud, as software as a service (SaaS).
For example, a compromised website may use an HTML iframe tag, or some obfuscated JavaS-
cript, in order to inject malicious code from the SaaS-based exploit toolkit rather than launch
the malicious attack directly from exploit code hosted on the compromised website. This growth
in SaaS-based exploit toolkits is also evidenced in the decline in the number of new malicious
domains used to host malware, which fell by 47 percent, from 56,158 in 2013 to 29,927 in 2014.

Web attack toolkits perform scans on the victims’ computers, looking for vulnerable plug-ins
in order to launch the most effective attack. Moreover, these SaaS toolkits are often located on
bulletproof hosting services, with IP addresses that can change quickly and domain names that
may be dynamically generated, making it more difficult to locate the malicious SaaS infrastruc-
ture and shut it down. Attackers are also able to control how the exploits are administered such
as enabling the attacks only if a cookie has been set by the initial compromised website thereby
preserving the malicious code from the prying eyes of search engines and security researchers.

With the majority of websites still accommodating vulnerabilities, it is apparent that many
website owners are not keeping on top of vulnerability scans, although they may be paying more
attention to malware scans that can potentially reveal malicious software. However, malware is
often planted following previous exploitations of vulnerabilities, and prevention is always better
than cure.

With so many potentially vulnerable websites, criminals in 2014 were achieving considerable
success exploiting them, and many were also quick to take advantage of the SSL and TLS vulnera-
bilities. Moreover, the greater prevalence of social media scams and malvertising in 2014 suggests
criminals are already turning to them as alternative methods of malware distribution.

These SaaS toolkits
are often located on
bulletproof hosting
services, with IP
addresses that can
change quickly and
domain names that
may be dynamically
generated.

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

42

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

 With half of active web attack
toolkits falling into the “other”
category, overall toolkit usage
was much more fragmented in
2014 than in previous years.

 After the arrest of the alleged
creator in late 2013, the
Blackhole toolkit has dropped
14 percentage points in 2014,
comprising only five percent of
all web attack toolkit activity. At
its peak, Blackhole make up 41
percent of all toolkit activity.

Web Attack Toolkits

Blackhole

Sakura

Phoenix RedKit

Nuclear

2012

41%

22%

10% 7% 3 Other  17%

0

G01 Pack

Blackhole

Sakura

Styx

CoolKit

2013

23%

19%

14%

10% 8%

Other  26%

0

Sakura

Nuclear Styx OrangeKit

Blackhole

2014

23%

10% 7% 5% 5%

Other  50%

0

48

Top 5 Web Attack Toolkits, 2012–2014
Source: Symantec

100%

100%

100%

100%

L
A
T
O
T
F
O
E
G
A
T
N
E
C
R
E
P

0

Others

Blackhole

OrangeKit

Styx

Nuclear

Sakura

J

F

M

A

M

J

J

A

S

O

N

D

49

Timeline of Web Attack Toolkit Use, Top 5, 2014
Source: Symantec

2015 Internet Security Threat Report  Top 5 Web Attack ToolkitsTimeline of Web Attack Toolkit Use

MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

43

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

47  http://www.symantec.com/connect/blogs/

massive-malvertising-campaign-leads-browser-locking-

ransomware

 Example of a Browlock webpage demanding a fine for surfing pornography illegally.47

Malvertising

As we moved into 2014, we saw ransomware and malvertising cross paths, with the number of
victims getting redirected to Browlock websites hitting new heights.

Browlock itself is one of the less aggressive variants of ransomware. Rather than malicious code
that runs on the victim’s computer, it’s simply a webpage that uses JavaScript tricks to prevent
the victim from closing the browser tab. The site determines where the victim is and presents a
location-specific webpage, which claims the victim has broken the law by accessing pornography
websites and demands that they pay a fine to the local police.

The Browlock attackers appear to be purchasing advertising from legitimate networks to drive
traffic to their sites. The advertisement is directed to an adult webpage, which then redirects
to the Browlock website. The traffic that the Browlock attackers purchased comes from several
sources, but primarily from adult advertising networks.48

To escape, victims merely need to close their browser. However, the large financial investment
criminals are making to direct traffic to their site suggests people are just paying up instead.
Perhaps this is because the victim has clicked on an advert for a pornographic site before ending
up on the Browlock webpage: guilt can be a powerful motivator.

Malvertising at Large

It’s not just ransomware that is spread through malvertising: malicious advertisements also
redirect to sites that install Trojans. Some malicious advertisements even use drive-by attacks to
infect a victim’s device without the user clicking on the advertisements.

The appeal for criminals is that malvertising can hit major, legitimate websites drawing in high
volumes of traffic. Ad networks also tend to be highly localized in their targeting, meaning

As we moved into
2014, we saw
ransomware and
malvertising cross
paths, with the
number of victims
getting redirected to
Browlock websites
hitting new heights.

48  Ibid

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

44

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

criminals can tailor their scams to specific victims—for example, people searching for financial
services. Legitimate ad networks sometimes inadvertently do all the work for the criminals.

Criminals also switch tactics to avoid detection. For example, they’ll run a legitimate ad for a few
weeks, to appear aboveboard, and then convert it to a malicious ad. In response, ad networks need to
run scans regularly rather than just when a new ad is uploaded.

For website owners, it’s hard to prevent malvertising, as they have no direct control over the ad
networks and their customers. However, site managers can reduce risk by choosing networks that
restrict ad functionality so advertisers can’t embed malicious code in their promotions. And of
course, when selecting an ad network, due diligence goes a long way.

Denial of Service

Denial-of-service attacks give attackers another way to target individual organizations. By over-
loading critical systems, such as websites or email, with Internet traffic as a way to block access,
denial-of-service attacks can wreak financial havoc and disrupt normal operations. Distributed
denial-of-service (DDoS) attacks are not new, but they are growing in intensity and frequency.49
For example, Symantec saw a 183 percent increase in DNS amplification attacks between January
and August 2014.50 According to a survey by Neustar, 60 percent of companies were impacted by
a DDoS attack in 2013 and 87 percent were hit more than once.51 Motives include extortion for
money, diversion of attention away from other forms of attack, hacktivism, and revenge. Increasing-
ly, would-be deniers of service can rent attacks of a specified duration and intensity for as little as
$10–$20 in the online black market.

49  http://www.symantec.com/connect/blogs/denial-

service-attacks-short-strong

50  http://www.symantec.com/connect/blogs/denial-

service-attacks-short-strong

 DDoS traffic saw peaks in April

of-ddos-attacks.pdf

51  http://www.symantec.com/content/en/us/enterprise/

media/security_response/whitepapers/the-continued-rise-

DDoS Total

TREND

DNS Amplification
Attack

Generic ICMP
Flood Attack

Generic TCP SYN Flood
Denial-of-Service Attack

and July of 2014.

 There was a 183 percent

increase in DNS amplification
attacks between January and
August 2014.

S
N
O
I
L
L
I
M

8

7

6

5

4

3

2

1

J

F

M

A

M

J

J

A

S

O

N

D

69

DDoS Attack Traffic Seen by Symantec’s Global Intelligence Network, 2014
Source: Symantec

2015 Internet Security Threat Report  DDoS Attack TrafficMOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

45

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

S
O
C
I
A
L
M
E
D
A
&
S
C
A
M
S

I

2015 Internet Security Threat Report

MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

46

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

Social Media and Scams

In 2014 criminals hijacked the power of “social proof”—the idea that we attribute more value to
something if it’s shared or approved by others. The classic example is of two restaurants: one
with a big queue, the other empty. People would rather wait in the queue because popularity
suggests quality.

Criminals exploited this theory by hacking real accounts on platforms like Snapchat so that
when you saw an endorsement for a scam product or link, you’d trust it because it seemed to
come from someone you actually knew.

The public also undervalued their data in 2014, freely giving away email addresses and login
credentials without checking that they were on a legitimate website.

While scammers certainly evolved their tactics and ventured onto new platforms in 2014, a lot
of their success continued to come from people’s willingness to fall for predictable and easily
avoided scams.

Social Media

Criminals will go wherever there are people to be scammed. There are large numbers of people
using well-established social media platforms, and, as such, they play host to plenty of scams.
The rise in popularity of messaging and dating apps means scammers have taken note and taken
advantage, and a variety of scams are being seen on these platforms.

Facebook, Twitter, and Pinterest

The big shift in social media scams this year has been the uptick in manual sharing scams. This
is where people voluntarily and unwittingly share enticing videos, stories, pictures, and offers
that actually include links to malicious or affiliate sites.

BACK TO TABLE OF CONTENTS

At a Glance

 Social media scammers go
after payouts from affiliate
programs by offering false
promises of weight loss,
money, and sex to drive clicks
and sign-ups.

 Many people use the same
password on multiple
networks, meaning criminals
have been able to spam
multiple accounts thanks to a
single hack.

 Scammers take advantage of
the power of social proof by
relying on real people rather
than bot networks to share
their scams.

SHARE
THIS

 Many phishing scams play

on either fears generated by
hacking and health-scare
stories or intrigue piqued by
scandalous celebrity stories,
both real and fake.

In 2014 criminals
hijacked the power
of “social proof”—
the idea that we
attribute more
value to something
if it’s shared or
approved by others.

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

47

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

100%

80

60

40

20

2012

2013

2014

 In 2014, 70 percent of social

media threats required end users
to propagate them, compared
with only 2 percent in 2013.

81

70

56

18

2

Manual
Sharing

23

Fake
Offering

10

7

5

Likejacking

3

2

1

0

0

1

Fake
Apps

Comment
Jacking

Manual Sharing – These rely on victims to actually do the work of sharing
the scam by presenting them with intriguing videos, fake offers or messages that they share
with their friends.

Fake Offering – These scams invite social network users to join a fake event or group
with incentives such as free gift cards. Joining often requires the user to share
credentials with the attacker or send a text to a premium rate number.

Likejacking – Using fake “Like” buttons, attackers trick users into clicking website
buttons that install malware and may post updates on a user’s newsfeed, spreading the attack.

Fake Apps – Users are invited to subscribe to an application that appears to be
integrated for use with a social network, but is not as described and may be used to steal
credentials or harvest other personal data.

Comment Jacking – This attack is similar to the "Like" jacking where the attacker tricks the
user into submitting a comment about a link or site, which will then be posted to his/her wall.

59

Social Media, 2012–2014
Source: Symantec

2015 Internet Security Threat Report  Social MediaMOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

48

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Affiliate Programs: The Fuel That Drives Social Media Scams

By Satnam Narang

If you have used a social network in the past decade,
chances are you’ve seen one of the following offers appear
in your news feeds and timelines:

 Free smartphones, airline tickets, or gift cards

 Unbelievable news about celebrities (sex tapes, death)

 Unbelievable world news (specifically, natural disasters)

 Proposals to get naked on a webcam or propositions

from alleged sex workers

Affiliates participate in an affiliate program by appending a
special ID to the URLs that are used when a customer clicks
an advertisement. The unique ID helps keep track of where
the click comes from. This affiliate ID enables merchants
to track the contributions from affiliates and thus pay out
commissions.

It has become clear that as any social networking platform
becomes popular, scammers are never far behind. While
each platform may be different and each scam slightly
varied, the constant is that affiliate networks are the driving
force behind them.

Affiliate marketing is a popular way for companies to
increase their business on the Internet. A business uses
affiliates to help market and sell their products. For
instance, an affiliate could feature a book on their webpage
and provide a link directly to a vendor that sells that book.
And for every sale, the affiliate receives a small commission.

While legitimate vendors use affiliates, so do illegitimate
ones. And in some cases the vendor is legitimate, but some
of their affiliates are willing to use unscrupulous methods
to profit from an affiliate program.

Scammers monetize on social media by leveraging
affiliate networks. When a user is asked to fill out a
survey or sign up for a premium offer to a service, he
or she becomes the referral for an affiliate program. By
tricking users into participating in a survey and/or signing
up for a premium service, the scammer makes money.

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

49

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Details on these semi-legitimate affiliates and their
payouts are murky. Many won’t share details, making it
hard to estimate just how much money an affiliate can
make. However, most affiliate networks put up bids from
merchants, which state clearly what action is required for
a conversion. In the example above, a $1,500 Visa gift card
advertisement will convert when the referrer submits his
or her email address. This particular merchant values each
email conversion at $1.40 when paying affiliates.

On the popular dating application Tinder, we found affiliate
links to adult dating services and webcam sites. These sites
promote their affiliate payouts directly. One site pays affili-
ates up to $6 for every user who signs up for an account and
up to $60 if a user signs up for a premium service, which
typically involves paying for a subscription using a credit
card.

Based on the pricing structure, convincing users to sign
up for the premium service could be highly profitable.
However, scammers drive so much traffic to these sites
that sign-ups for an account, at only $6 each, are enough
to create a handsome profit. The users who do sign up for a
premium service are just the icing on the cake.

Legitimate merchants, and some affiliate networks, have
tried to tackle scams on their platforms, but as long as there
is money to be made from these shady affiliate programs,
they will persist. As a merchant, it is important to know the
affiliates you work with and ensure they are being transpar-
ent with you about their practices.

End users should be mindful when using any social
network, keeping an eye out for free offers for gadgets, gift
cards, and airline tickets or for invitations from attractive
women to join adult dating and webcam sites. If you are
asked to fill out a survey or sign up for a service using a
credit card, you are most likely being scammed. As the old
adage goes, if it sounds too good to be true, it probably is.

SHARE
THIS

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

50

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

 Facebook share dialog with fake comments and shares.

 Scam site asks users to install fake Facebook media plug-in.

For example, scammers took advantage of the death of Robin Williams by sharing what was
supposed to be his goodbye video. Users were told they had to share the video with their friends
before they could view it, and were instructed to fill out surveys, download software, or were redi-
rected to a fake news website. There was no video.52

With manual sharing there’s no hacking or jacking necessary—people and their networks do all
the work for the criminals. Other social media scams require a bit more work on the part of the
criminal. Likejacking and comment jacking, for example, ask victims to click what appears to be a
“continue” or “verification” button to access some enticing content but actually masks the fact the
victim is liking or commenting on the post to increase its popularity and reach.

Instagram

Instagram, the picture-sharing platform, now has more monthly active users than Twitter, and
legitimate brands use it as a marketing channel.53,54 Among the scams seen on Instagram in 2014
were those where criminals tried to monetize prepopulated accounts and mimic offers employed by
legitimate corporate users.

In one scam, fake accounts are created, purporting to be lottery winners who are sharing their
winnings with anyone who will become a follower. In another scam, scammers pretend to be well-
known brands giving away gift cards. Instagram users are told to follow the fake accounts and add
their personal information, like email addresses, in the comments to receive incentives.

Once a fake
account has enough
followers, the
criminals change
the name, picture,
and bio, so when
the incentive fails
to materialize,
people can’t locate
the account to
mark it as spam.

52  http://www.symantec.com/connect/blogs/robin-

williams-goodbye-video-used-lure-social-media-scams

53  http://blog.instagram.com/

post/104847837897/141210-300million

54  https://investor.twitterinc.com/releasedetail.

cfm?ReleaseID=878170

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

51

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Victims often think nothing of giving away their details. According to our Norton Mobile Apps
Survey Report, 68 percent of people surveyed will willingly trade in various types of private infor-
mation for a free app.55  In fact, some even send $0.99 to the scammers in order to cover the return
postage for the so-called offer. (The offer never arrives, of course.) It’s such a small amount, so
people don’t worry, but they’re giving away more details, and scammers are getting an extra cash
bonus.56

This is particularly prevalent on Instagram, partly because there is no verified check for legitimate
accounts. And as soon as one person falls for the scam, that person’s friends who follow his or her
stream will see the posted picture and often jump on board too.

Once a fake account has enough followers, the criminals change the name, picture, and bio,
so when the incentive fails to materialize, people can’t locate the account to mark it as spam.
Criminals then sell this altered account with all its followers to the highest bidder.

Shortly afterward a new account usually pops up in the guise of the original fake profile, claiming
the old account was hacked, and the process starts all over again.

Messaging Platforms

This year Snapchat, the social app that allows people to send images and videos that self-destruct
within 10 seconds of the recipient’s opening the message, was hit particularly hard.

In October 2014, several Snapchat accounts were hacked and people reported receiving messages
from their friends with a live link promoting diet pills. Snapchat claims these accounts were
compromised because certain users reused the same password on multiple websites, one of which
had been breached.57

 Instagram accounts impersonating real-life lottery winners.58

55  http://www.slideshare.net/symantec/norton-mobile-

apps-survey-report

56  http://www.symantec.com/connect/blogs/instagram-

scam-lottery-winners-impersonated-offer-money-followers

57  http://www.symantec.com/connect/blogs/hacked-

snapchat-accounts-use-native-chat-feature-spread-diet-

pill-spam

58  Image from http://www.symantec.com/connect/blogs/

instagram-scam-lottery-winners-impersonated-offer-

money-followers

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

52

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

 An example of a legitimate user account being compromised to send spam to the victim’s circle of friends.

The legitimate owner of the compromised account was quickly notified by Snapchat.

URL shortening services are popular among spammers and
social networking users alike because they provide a
shortened link. For spammers, they have an added benefit:
they obfuscate the domain name of the spam website behind
them. Additionally, by appending “+” to the end of a Bitlink,
spammers and their affiliates now have easy access to
click-through statistics and other demographics.

Short URLs are frequently seen not only in email spam but
also in SMS spam and some of the newer forms of spam
spread through social networks.

In October 2014 Symantec also saw an incident, referred to
online as “The Snappening,” when supposedly destroyed
Snapchat images began appearing online. This originated
from an unapproved third-party app that some people used
to archive their Snapchat photos.

Often, the security and privacy policies of emerging social

 Example of click-through rates
for the URL included in the
Snapchat spam example above.

media platforms aren’t as strong as they could or should be, and users don’t help the situation by
replicating their passwords across multiple platforms and using unverified third-party apps to
enhance their experience.

Unless users begin to think about the risk they’re exposing themselves to, we’re likely to see
similar account hijacking stories in 2015 on whatever the next big platforms turn out to be.

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

53

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

 Historical overview of fake prostitution profiles on Tinder.59

Dating Scams

Sexual content has always gone hand in hand with cybercrime,
and 2014 was no different.

In 2014, adult-themed scams embraced popular dating apps, with
examples appearing on Tinder and on messaging services, such as
Snapchat and Kik Messenger. The goal is to get people to click through
and sign up for external websites, at which point scammers earn a
commission as part of an affiliate program.60

 Examples of spam “cam girl”-type messages
appearing as new chats on Kik Messenger.

60  http://www.symantec.com/connect/blogs/adult-

webcam-spam-all-roads-lead-kik-messenger

Some affiliate programs will pay out for every victim who clicks
through, and others will pay out only if a victim signs up and hands
over credit card details. Some sites pay $6 per lead for a successful
sign-up and up to $60 if a lead becomes a premium member.61 These
schemes can be, in other words, a profitable monetization strategy for
online criminals. (See “Affiliate Programs: The Fuel That Drives Social Media Scams”
for more on affiliate marketing.)

The scam usually starts with the profile of an attractive young girl offering adult webcam time,
sexting, or hookups. In Tinder there have also been cases of profile pictures overlaid with text
offering prostitution services. Scammers put the text within the image in an attempt to beat spam
filters.

The recipient then clicks through to or manually visits an affiliate website if he or she wants to
continue the encounter. In reality these “hot chicks” are nothing more than scripted bots with sexy
profile pictures, and there’s no one waiting on the other side.

These promises of sexual content prove popular with the public: one particular campaign, associ-
ated with a site called blamcams, resulted in nearly half a million clicks across seven URLs in less
than four months.62 For scammers tied to affiliate programs or who use links to fake webcam sites
to phish for credit card details, that’s a good source of income.

59  Taken from: http://www.symantec.com/connect/blogs/

tinder-spam-year-later-spammers-still-flirting-mobile-

dating-app

61  http://www.symantec.com/connect/blogs/tinder-

spam-year-later-spammers-still-flirting-mobile-dating-app

62  http://www.symantec.com/connect/blogs/tinder-

spam-year-later-spammers-still-flirting-mobile-dating-app

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

54

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Malcode in Social Media

It’s worth noting that while most sharing scams are concerned with gaining clicks and sign-ups
for affiliate programs, there was a case in 2014 where a Facebook scam redirected to the Nuclear
exploit kit. When successful, this scam gives attackers control of a victim’s computer and allows
them to send out spam email and malicious files.63

People need to be wary of links posted by friends that seem unusually sensational and, rather than
clicking on the link, should go directly to a trusted news source and search for the story there.

Some argue that
secrecy is the key
to the next phase of
social networking.

The Rise of “Antisocial Networking”

Privacy concerns—both about government surveillance and oversharing with service providers—
have triggered the launch of new social networks that prioritize secrecy, privacy, and/or anonymity,
such as Secret, Cloaq, Whisper, ind.ie, and PostSecret. These types of applications are havens for
gossip, confessions, and, sometimes, the darker side of human nature. Some argue that secrecy
is the key to the next phase of social networking.64,65 Critics say that anonymous forums, such
as 4chan, create safe havens for trolls, bullies, and criminals.66 Existing social networks, such as
Twitter and Facebook, have responded to these concerns with greater disclosure and by sharpening
up their privacy policies. For example, Facebook now publishes its number of government data
requests,67 Twitter is considering a “whisper mode,”68 and Google has enhanced encryption on its
Gmail email service.69

While the desire to remain anonymous may be very attractive for some individuals, there is always
a downside that we must keep in mind. Some organizations have very strict guidelines and policies
that govern how their employees must conduct themselves online, but many are still adapting
to these new environments where people can potentially say whatever they like with impunity.
Businesses should ensure their electronic communication policies address these concerns and
technologies are in place for monitoring potential breaches of the rules. While it may not be appro-
priate to block access, it may prove invaluable to be able to monitor such activities.

Phishing

There was a dip between June and September, but the overall phishing rate in 2014 was 1 in 965,
compared with 1 in 392 in 2013. Phishing attacks toward the end of the year were boosted by
the surge in Apple ID phishing schemes that emerged after the headline-grabbing hack that saw
several nude pictures of celebrities stolen and published. Apple IDs have always been a target for
phishers, but this news story meant people were particularly receptive to messages purporting to
be about the security of their iCloud accounts.

The Kelihos botnet looked to exploit the public’s fear by sending messages that claimed a purchase
had been made on the victim’s iCloud account from an unusual device and IP address. The victim
was encouraged to urgently check his or her Apple ID by clicking an accompanying link, which led
to a phishing page. Masquerading as an Apple website, the site asked the user to submit his or her
Apple ID and password, which was then harvested by criminals for exploit or resale.70

Most phishing scams are distributed through phishing emails or URLs on
social media sites. On social media there’s often a news hook, like the Ebola
outbreak or some kind of celebrity scandal, that encourages people to click on links that require
them to “log in” before they can see the details or video promised.

SHARE
THIS

Email distribution involves news hooks but is used to phish for professional account logins such
as banking details, LinkedIn accounts, cloud file storage, or email accounts.71 Some emails pose as
security updates or unusual activity warnings that require you to fill in your details on a phishing
site, which then immediately sends your details to the criminals.

63  http://www.symantec.com/connect/blogs/facebook-

scam-leads-nuclear-exploit-kit

64  http://www.wired.com/2014/02/can-anonymous-

apps-give-rise-authentic-internet/

65  http://www.technologyreview.com/review/531211/

confessional-in-the-palm-of-your-hand/

66  See many issues highlighted on See many issues

highlighted on http://en.wikipedia.org/wiki/4chan

67  https://www.facebook.com/about/government_

requests

68  http://thenextweb.com/twitter/2014/04/30/twitter-

ceo-dick-costolo-whisper-mode-encourage-friends-

privately-discuss-public-conversations/

69  http://techcrunch.com/2014/03/20/gmail-traffic-

between-google-servers-now-encrypted-to-thwart-nsa-

snooping/

70  http://www.symantec.com/connect/blogs/apple-ids-

targeted-kelihos-botnet-phishing-campaign

71  LinkedIn: http://www.symantec.com/connect/blogs/

linkedin-alert-scammers-use-security-update-phish-

credentials

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

55

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

 Sample of phishing email sent to

victims.72

 Variations on this theme

appeared throughout 2014, with
criminals aiming to acquire social
media, banking and email login
details.

72  Image from http://www.symantec.com/connect/blogs/

apple-ids-targeted-kelihos-botnet-phishing-campaign

2014

2013

2012

 The email phishing rate dropped
to 1 in 965 emails in 2014. In
2013 this rate was 1 in 392
emails.

1 in 965

1 in 392

1 in 414

13

Email Phishing Rate (Not Spear-Phishing)
Source: Symantec

Inverse Graph: Smaller Number = Greater Risk

2015 Internet Security Threat Report  Email Phishing Rate (Not Spear-Phishing) MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

56

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Phishing in Countries You Might Not Expect

By Nicholas Johnston

Symantec sees a significant proportion of global email
traffic, and recently we were surprised to see phishing
attacks targeting institutions in rather unexpected
locations.

Angola and Mozambique are two southern African
countries, on opposite sides of the vast continent. These
countries aren’t the first places that spring to mind when
you think of phishing, where the goal is to gather sensitive
information in order to make money. Mozambique is still
a developing country, and despite having an abundance of
natural resources, remains heavily dependent on foreign
aid. Its per-capita GDP is around $600. Angola fares better
than Mozambique; its per-capita GDP is just under $6,000.
These are statistically poor countries. (For comparison,
global average per-capita GDP figure stands at $10,400, and
the U.S. GDP stands around $52,800.)

Both of these countries have recently been subjected to
phishing campaigns. For instance, one recent phishing
campaign was targeted at a major African financial institu-
tion, appearing to come from a Mozambique bank, with the
email subject, “Mensagens & alertas: 1 nova mensagem!”
(Messages & alerts: 1 new message!) A URL contained
within the body lead to a fake version of the bank’s Web
site, asking the target to enter a number of banking details
that would allow the attacker to take over the account.

Why are financial institutions in these countries being
targeted? It’s impossible to be sure, but one of the main
dangers of phishing is the ease at which attackers can set
up phishing sites. Over the year we’ve found many “phish

kits”--zip files containing phishing sites, ready to be
unzipped on a freshly-compromised web server. Addition-
ally, since Angola and Mozambique both speak Portuguese,
campaigns from one country can easily be used in the other
with only minor changes to the content within them.

From an attacker’s perspective, phishing has very low
barriers to entry. By targeting smaller or more niche insti-
tutions, phishers can avoid competition with their peers.
Phishing awareness in developing countries is likely to be
lower than in the US or Europe for example.

In all likelihood, the phishing scams targeting Angola and
Mozambique probably originate from those countries or
neighboring ones. Phishers who target people in developed
countries won’t be interested in the comparatively low
potential profits from phishing accounts in Angola or
Mozambique—but those low (by Western standards) profits
can still be attractive to someone living in Angola, Mozam-
bique or nearby countries with similar living standards.
It might also be easier for phishers based in Angola or
Mozambique to use stolen credentials locally rather than
selling them on.

As people increasingly interact with companies and services
online, we expect phishing to increase—there are more
targets and barriers of entry that will continue to get lower.
Even institutions in the very small and relatively isolated
east Himalayan Kingdom of Bhutan have been targeted in
phishing attacks. This only demonstrates that nowhere is
safe from phishing.

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

57

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

DNOSAJJMAMFJ

DNOSAJJMAMFJ

DNOSAJJMAMFJ

2012

2013

2014

 There was a significant drop in

the phishing rate during the late
summer, early autumn of 2014.

N

I

1

200

400

600

800

1,000

1,200

1,400

1,600

1,800

2,000

2,200

65

Phishing Rate, 2012–2014     Inverse Graph: Smaller Number = Greater Risk
Source: Symantec

 The number of phishing URLs
on social media remained
low throughout 2014 when
compared to 2013 and the peak
year of 2012.

60

50

40

30

20

10

S
D
N
A
S
U
O
H
T

2010

2011

2012

2013

2014

66

Number of Phishing URLs in Social Media, 2009–2014
Source: Symantec

2015 Internet Security Threat Report  0Phishing RateNumber of Phishing URLs on Social Media
MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

58

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

The shift away
from email isn’t
happening with just
phishing attacks;
the global spam
rate is declining too.

 The overall email spam rate
further declined in 2014,
dropping six percentage points
to 60 percent.

 The global spam volume per day
dropped three percent for the
second year in a row.

The origins of these phishing sites are often obscured to prevent security warnings when victims
open their browsers, and this year saw a new leap forward for the criminals with the use of AES
(Advanced Encryption Standard).

This encryption is designed to make the analysis of phishing sites more difficult, and a casual
analysis of the page will not reveal any phishing-related content, as it is contained in the unread-
able encrypted text. Browser and security software warnings are therefore less likely to appear.

Email Scams and Spam

The shift away from email isn’t happening with just phishing attacks; the global spam rate is
declining too. The result is more victims are likely to fall for the scam, and it’s harder to track.73

60

60%
-6% pts

2014

66

66%
-3% pts

2013

9

Overall Email Spam Rate
Source: Symantec

2014

2013

2012

10

Estimated Global Email Spam Volume per Day
Source: Symantec

69

69%

2012

28 Billion
-3%

29 Billion
-3%

30 Billion

73   http://www.symantec.com/connect/blogs/fresh-

phish-served-helping-aes

2015 Internet Security Threat Report  Overall Email Spam RateEstimated Global Email Spam Volume per Day
MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

59

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

 Over the last three years, the

overall spam rate has dropped
from 69 percent in 2012, to 66
percent in 2013 and 60 percent
in 2014. While this is good news
overall, there are still a lot of
scams out there being sent by
email, and criminals are still
making money.

35

30

25

20

15

10

5

S
N
O
I
L
L
I
B

JAN

FEB

MAR

APR

MAY

JUN

JUL

AUG

SEP

OCT

NOV

DEC

67

Global Spam Volume per Day, 2014
Source: Symantec

In October 2014, Symantec reported an increase in a particular scam where emails were sent, often
to a recipient working in the finance department of a company, requesting payment by credit card
or the completion of a wire transfer. The sender details were sometimes faked or made to look like
they had come from the CEO or another high-ranking member of the victim’s company. Money
transfer details were either sent in an attachment, or required the victim to email back and request
them.74

The rise in this type of scam is likely because scams based on malicious attachments can be more
easily filtered by corporate security systems, but many organizations are still not undertaking this
simple action despite the majority of malicious emails relying on potentially harmful attachments.

In contrast, a sharp rise in malicious URLs versus attachments at the end of the year was related to
a change in tactics and a surge in socially engineered spam emails.

74  http://www.symantec.com/connect/blogs/scammers-

pose-company-execs-wire-transfer-spam-campaign

2015 Internet Security Threat Report  0Global Spam Volume per DayMOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

60

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

T
A
R
G
E
T
E
D
A
T
T
A
C
K
S

2015 Internet Security Threat Report
MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

61

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Targeted Attacks

In 2014, Symantec analyzed several cyberespionage attacks and gathered data on the tactics used
to infiltrate thousands of well-defended organizations around the world. This research shows a
worrying increase in sophistication.

At a Glance

Imagine you’re the CISO for an Eastern European diplomatic corps. In 2014, You suspect that
computers in your embassies across Europe have been infected with a back door Trojan. You
call in a security firm to investigate and they confirm your worst suspicions. Upon investigation
you find that a carefully targeted spear-phishing campaign sent emails to staff members with
a stealthy Trojan payload that infected the computers. The use of zero-day exploits, carefully
crafted emails, and cunning watering hole website attacks meant that the attacks evaded
detection long enough to compromise more than 4,500 computers in more than 100 countries.75
It’s a worrying scenario but not a hypothetical one. This is a description of the Waterbug attack.

It’s similar to other targeted attacks such as Turla and Regin, and due to the targets chosen and
the sophistication of the attack methods, Symantec believes that a state-sponsored group is
behind Waterbug.76

In view of the growing sophistication of these attacks, good IT security is essential and broad
cybersecurity practices should be the norm. Well-funded state actors are not the only threat.
Patriotic hackers, hacktivists, criminal extortionists, data thieves, and other attackers use similar
techniques but with fewer resources and perhaps less sophistication.

Email-based attacks continue much as before. Web-based attacks are growing increasingly
sophisticated. Espionage attacks use more exploit kits, bundling together
exploits rather than using just one attack. Exploit kits have been used in
e-crime for many years, but cyberespionage attackers are now using them too.

SHARE
THIS

Cyberespionage

In 2014, Symantec security experts spent nearly eight months dissecting one of the most sophis-
ticated pieces of cyberespionage malware ever seen. Known as Regin, it gave its owners powerful
tools for spying on governments, infrastructure operators, businesses, researchers, and private
individuals. Attacks on telecom companies appeared to be designed to gain access to calls being
routed through their infrastructure.77

Regin is complex, with five stealth stages of installation. It also has a modular design that allows
for different capabilities to be added and removed from the malware. Both multistage loading
and modularity have been seen before, but Regin displays a high level of engineering capability
and professional development. For example, it has dozens of modules with capabilities such as
remote access, screenshot capture, password theft, network traffic monitoring, and deleted file
recovery.78

It took months, if not years, to develop Regin, implying a significant investment of resources.
It is highly suited to persistent long-term surveillance operations, and its level of sophistication
implies that a nation state created it.

Symantec saw a similar level of commitment in another cyberespionage campaign known as
Turla.79 The attackers used spear-phishing and watering hole attacks (see below) to target the
governments and embassies of former Eastern Bloc countries. Once installed, it gave attackers
remote access to infected computers, allowing them to copy files, delete files, and connect
to servers, among other things. Because of the targets chosen and the sophistication of the
malware, Symantec believes that a state-sponsored group was behind these attacks too.80

 More state-sponsored

cyberespionage came to light
in 2014.

 Attackers are using
increasingly well-
crafted malware that
displays sophisticated
software engineering and
professionalism.

 Campaigns such as Dragonfly,
Waterbug, and Turla infiltrated
industrial systems, embassies,
and other sensitive targets.

 The number of spear-phishing
campaigns increased by 8
percent in 2014, while the
number of daily attacks
decreased as attackers become
more patient, lying in wait
and crafting more subtle
attacks boosted by longer-term
reconnaissance.

In view of
the growing
sophistication
of these attacks,
good IT security
is essential and
broad cybersecurity
practices should
be the norm.

75  http://www.symantec.com/content/en/us/enterprise/

media/security_response/whitepapers/waterbug-attack-

group.pdf

76  Ibid

77  http://www.symantec.com/content/en/us/enterprise/

media/security_response/whitepapers/regin-analysis.pdf

78  http://www.symantec.com/en/uk/outbreak/?id=regin

79  http://www.symantec.com/connect/blogs/turla-

spying-tool-targets-governments-and-diplomats

80  http://www.symantec.com/connect/blogs/turla-

spying-tool-targets-governments-and-diplomats

2015 Internet Security Threat Report  81  http://www.symantec.com/connect/blogs/equation-

advanced-cyberespionage-group-has-all-tricks-book-and-

more

MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

62

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

More recently, a highly resourced attack group dubbed the “Equation Group” was
exposed,81 revealing that espionage attacks in previous years, including 2014, had probably
employed highly specialized techniques. Moreover, as espionage attack groups continue to
improve their methods, they can also take advantage of the black market in exploits, zero-day
attacks, and custom code. The exposé of the Equation Group further highlights the profession-
alism behind the development of these specialized attacks, as espionage attack groups benefit
from the same traditional software development practices as legitimate software companies.

Industrial Cybersecurity

As more devices are being connected to the Internet, new avenues of attack and, potentially,
sabotage open up. This is especially true for industrial devices known as industrial control
systems (ICSs), commonly used in areas of industrial production and utility services throughout
the world. Many of these devices are Internet enabled, allowing for
easier monitoring and control of the devices.

SHARE
THIS

Vulnerabilities

Unique Vendors

 The chart shows the number of
disclosed vulnerabilities that
were associated with ICS and
supervisory control and data
acquisition (SCADA) systems,
including the number of vendors
involved each year.

75

13

80

70

60

50

40

30

20

10

52A

9

35

39

7

16

14

12

10

8

6

4

2

2012

2013

2014

Vulnerabilities Disclosed in ICS Including SCADA Systems
Source: Symantec

2015 Internet Security Threat Report  Vulnerabilities Disclosed in ICS Including SCADA SystemsMOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

63

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Securing Industrial Control Systems

By Preeti Agarwal

Targeted attacks have evolved from novice intrusion
attempts to become an essential weapon in cyberespionage.
Industrial control systems (ICS) are prime targets for these
attackers, with motives for executing attacks at a national
security level. These trends are leading countries to
reinforce their investment and build strategies to improve
ICS security.

The term “industrial control system” refers to devices that
control, monitor, and manage critical infrastructure in
industrial sectors, such as electric, water and wastewater,
oil and natural gas, transportation, etc. Various types of
ICSs include supervisory control and data acquisition
(SCADA), programmable logic controllers (PLC), distributed
control systems (DCS), to name a few.

Attacks targeting ICSs have become a common occurrence
and can potentially have serious social and economic
impacts. But these attacks often go undisclosed, limiting the
PR fallout for the victim, and underreporting the extent of
the problem.

There have been numerous attacks, with intentions ranging
from cyberespionage to damaging the utilities in ICSs. In
2010 Stuxnet was discovered, a threat designed to attack
specific SCADA systems and damaged the physical facilities
of Iran’s nuclear system. Since then a myriad of weapon-
ized malware has been seen in the threat landscape, and
2014 was no exception. The attackers behind Dragonfly, a
cyberespionage campaign against a range of targets, mainly
in the energy sector, managed to compromise a number of
strategically important ICSs within these organizations
and could have caused damage or disruption to the energy
supply in the affected countries, had they used the sabotage
capabilities open to them.

More recently, Sandworm launched a sophisticated and
targeted malware campaign compromising the human-ma-
chine interface (HMI) of several well-known ICS vendors.
Attackers used the internet connected HMIs to exploit
vulnerabilities in the ICS software. Such intrusions could
have been reconnaissance for another attack.

The most recent addition to emerge in 2014 was an incident
where a blast furnace at a German steel mill suffered massive
damage following a cyber-attack on the plant’s network.82

Attacks against ICSs have matured and become more
frequent, making the security of these systems essential
and a pressing issue.

Many ICSs are installed and operate for many years.
This often leads to security policies rooted in a securi-
ty-through-obscurity approach, using physical isolation,
proprietary protocols, and specialized hardware in the
hopes that this will keep them secure. Many of these
systems were developed before Internet-based technologies
were used in businesses and were designed with a focus on
reliability, maintainability and availability aspects, with
little-or-no emphasis on security. However, compelling
needs for remote accessibility and corporate connectivity
have changed the attack surface dramatically, exposing new
vulnerabilities in these systems to attacks.

The primary entry point for these attacks today is poorly
protected Internet-accessible, critical infrastructure
devices. In order to provide remote accessibility, elements
of SCADA systems, used to monitor and control the plants
and equipment, are connected to the Internet through
corporate networks. These SCADA elements expose the
control network and pose a risk of attacks like scanning,
probing, brute force attempts, and unauthorized access of
these devices.

One way to leverage these devices in an attack is through
the HMI, often accessible from the corporate network. An
attacker can compromise the corporate hosts by exploit-
ing any existing day-zero vulnerability, discover any hosts
that have access into the control network, and attempt to
leverage this information as a way into the ICSs.

Another way to leverage ICSs is through an HMI connected
directly to Internet. These Internet-facing devices can be
easily discovered over the Internet using common search
engines. Once a control device is identified it can be
compromised by exploiting vulnerabilities or through an
improper configuration. The level of knowledge required for
launching these attacks is fairly low.

Apart from these entry points, ICSs and their software have
several inherent vulnerabilities, opening doors for adver-
saries. Many of the proprietary web applications available
have security vulnerabilities that allow buffer overflows,

82  https://www.bsi.bund.de/SharedDocs/Downloads/DE/

BSI/Publikationen/Lageberichte/Lagebericht2014.pdf

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

64

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

SQL injection, or cross-site scripting attacks. Poor authen-
tication and authorization techniques can lead the attacker
to gain access to critical ICS functionalities. Weak authenti-
cation in ICS protocols allows for man-in-the-middle attacks
like packet replay and spoofing. An attacker can end up
sending rogue commands to PLCs or fake statuses to HMIs.

ty solutions designed for IT computer systems. Given these
challenges there is no silver bullet solution for ICS security.
Rather security has to be implemented end-to-end at each
layer, including the network perimeter, access points to the
corporate and external network, the network level, the host-
based level, and the application level.

Ladder logic used to program the PLCs is a critical asset in
ICS environments. Compromises to an engineering work
station used for developing and uploading this PLC ladder
logic can lead to reverse engineering, which can be used to
craft attacks.

Securing ICS environments requires a comprehensive
security plan that would help an organization define its
security goals in terms of standards, regulatory compliance,
potential risk factors, business impacts, and required miti-
gation steps. Building a secure ICS environment requires
integrating security into each phase of the industrial
processes starting from planning to the day-to-day opera-
tions.

Network-level segregation between the control network and
corporate network should be an absolute requirement as
it greatly reduces the chances of attacks originating from
within corporate networks. However practical consider-
ations require ICS connectivity from the corporate network.
In such cases the access points should be limited, protected
by a firewall, and should make use of trusted communica-
tion channels like a VPN.

ICS environments are evolving, with vendors extending
support for security software on the control devices for
general purpose SCADA servers and engineering work-
stations. However systems like PLCs and DCSes still use
vendor-specific customized operating systems. These
control systems, once installed, have zero tolerance for
downtime, limited resources and time-dependent code. This
limits opportunities to deploy traditional enterprise-securi-

In addition, the control devices themselves should also
be secure by design. Manufacturers are responsible to
ensure that security is built into the control devices before
shipping.

Looking ahead we will likely see a trend towards an increase
in the use of mobile technology allowing remote HMI access
and control options. While the solution is very compelling
from administrative efficiency perspective, it will launch a
new attack surface associated with the mobile usage model.

It’s also possible that we will see the development of gener-
alized techniques for attacking ICSs. As a result we may see
a rise in freely available ICS exploit kits. This trend would
no doubt increase ICS attack numbers.

As we saw with Stuxnet, which reincarnated itself with
multiple variants, ICS-focused threats that followed had
similarities in attack vectors and artifacts, making use of
common ICS protocols and general-purpose Trojans. It
is highly likely that there are threats out there on ICSs,
installed stealthily, that have not yet been detected, sitting
passively at the moment. Attackers may find a reason to
make these passive attacks active at any point in time. It’s
entirely possible that we will see an onset of more critical
infrastructure vulnerabilities being utilized, to dangerous
ends.

2015 Internet Security Threat Report  83  http://www.symantec.com/content/en/us/enterprise/

media/security_response/whitepapers/Dragonfly_Threat_

Against_Western_Energy_Suppliers.pdf

84  http://en.wikipedia.org/wiki/OLE_for_Process_Control

MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

65

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Symantec saw more attacks against industrial control systems in 2014.
For example, the Dragonfly cyberespionage campaign attacked a range of
targets, including energy grid operators, electricity generators, petroleum pipeline operators, and
industrial equipment manufacturers.83 The majority of victims were located in the United States,
Spain, France, Italy, Germany, Turkey, and Poland.

SHARE
THIS

By attacking industrial control systems Dragonfly is following in the footsteps of Stuxnet, which
targeted the Iranian nuclear program. However, Dragonfly appears to have less destructive goals.
Initially it appeared to focus on espionage and persistent access rather than the ultimate goal of
sabotage. However, it gives the well-resourced group that created it insight into important industri-
al systems and— hypothetically—the ability to deliver a more destructive attack if required.

Using custom-written malware and malware bought “off the shelf” from Russian-language forums,
Dragonfly was spread using a combination of email-based spear-phishing and web-based watering
hole attacks that targeted its principal victims through smaller, less well-protected companies in
their supply chain.

It can be difficult for companies to protect legacy systems when they can’t afford any downtime
for patching or when they use proprietary or poorly protected technology. For example, OLE for
Process Control84 (OPC) is a widely used protocol in industrial automation systems. It is a well-docu-
mented open standard, but there is little provision for encryption, authentication, or other security
measures, making it vulnerable to rogue software. One of the goals of Dragonfly was to collect
information about OPC systems in target companies.

By specifically exploiting the ICS vendors’ software update servers, the Dragonfly attacks intro-
duced a new dimension to the watering hole attack method. Watering hole-based attacks exploit
vulnerabilities in third-party websites that the real target of the attack will visit, through which the
attacker may inject malware into the targeted organization. With Dragonfly, the attackers compro-
mised the supply chain by exploiting the software update servers for the ICS software employed by
its victims, marking a new milestone in new watering hole-style attacks.

Reconnaissance Attacks

Besides attacks using spear-phishing campaigns and watering holes—attacks that require the
human element of social engineering to succeed—attackers continue to attack targeted organiza-
tions from other angles in order to gain a foothold in their network. They can do this by attacking
the perimeter of the network, looking for holes in their defenses and exploiting them.

Now more than ever, reconnaissance plays a big part in an attacker gaining access to a targeted
organization’s network. This is generally the first step in the hacking process: gaining information
about the systems and looking for any weaknesses that can be exploited.

The popularity of reconnaissance is clear when looking at the top zero-day exploits in 2014. Far
and away, the most commonly used zero-day vulnerability was CVE-2013-7331. This wasn’t a
run-of-the-mill “exploit and gain access to a vulnerable system” exploit either. It only supports the
attacker gathering intelligence on the targeted network. However, it is quite useful for planning
further attacks. Armed with information such as the targeted internal network’s host names, IP
addresses, and various internal path names, an attacker could easily figure out his or her plan of
attack.

This zero-day exploit was also left unpatched for a significant period of time. Not only was the
CVE for this vulnerability allocated in 2013, only to be disclosed in February 2014, but the patch
to mitigate it wasn’t released until September 2014. This left a huge window of 204 days between
public disclosure and the patch’s release for the attackers to exploit vulnerable systems.

Now more than ever,
reconnaissance
plays a big part in
an attacker gaining
access to a targeted
organization’s
network.

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

66

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Attackers were able
to take advantage
of the vulnerability
and the information
it gained them about
targeted networks,
indirectly helping
them in their
malicious goals.

The best explanation for this extended period of exposure is the perceived severity of the threat.
Since this particular exploit did not allow an attacker to directly take control of a vulnerable
computer, perhaps it was not considered as important to address as other vulnerabilities. Attackers
clearly noticed this and were able to take advantage of the vulnerability and the information it
gained them about targeted networks, indirectly helping them in their malicious goals.

This is a portion of the threat landscape that may be deserving of more attention across the
security industry. While a vulnerability that simply returns information about the network,
computer, or device may not be considered as severe as one that allows privilege escalation, it
can still be just as dangerous if it points attackers toward vulnerable systems they wouldn’t have
discovered without it.

Watering Hole Attacks

The professional hackers-for-hire group known as Hidden Lynx, first uncovered in September
2013, continued their operations in 2014. This group took advantage of a significant zero-day
vulnerability (CVE-2014-0332)85 through a watering hole-style attack. The attack ultimately opened
a back door on any computer that visited the compromised site while the watering hole was active,
through which subsequent attacks and exfiltration could take place.

This vulnerability was also discovered in watering hole attacks against organizations involved with
the French aerospace industry and a variety of Japanese websites. However, it is likely that these
attacks are separate from the Hidden Lynx group and other actors were involved in their use.86

Another significant watering hole attack took advantage of a zero-day vulnerability in Adobe Flash
(CVE-2014-0515) and coupled it with a specific piece of software produced by a legitimate vendor.
This particular attack appears to have been highly targeted, as the target organization would have
needed both pieces of software installed in order for the attack to be successful.

2014

2013

2012

31

Zero-Day Vulnerabilities
Source: Symantec

 There was a four percent

increase in the number of zero-
day vulnerabilities discovered in
2014.

SHARE
THIS

24
+4%

23
+64%

14

85  http://www.symantec.com/connect/blogs/emerging-

threat-ms-ie-10-zero-day-cve-2014-0322-use-after-free-

remote-code-execution-vulnerabi

86  http://www.symantec.com/connect/blogs/zero-day-

internet-vulnerability-let-loose-wild

2015 Internet Security Threat Report  Zero-Day VulnerabilitiesBN31 Zero-day VulnerabilitiesMOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

67

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

4

19

2013

2014

59

Average Days to Patch by Vendor for Top 5 Zero-Days

Total Days of Exposure for Top 5 Zero-Days

295

25

20

15

10

5

)
s
d
n
a
s
u
o
h
T
(

d
e
t
c
e
t
e
D
s
k
c
a
t
t
A
f
o
r
e
b
m
u
N

81%  Microsoft ActiveX Control

CVE-2013-7331

10%  Microsoft Internet Explorer

CVE-2014-0322

7%

2%

Adobe Flash Player
CVE-2014-0515

Adobe Flash Player
CVE-2014-0497

<1%  Microsoft Windows

CVE-2014-4114 OLE

81%
Microsoft ActiveX
Control

0

25

50

75

100

125

150

175

200

225

250

275

300

Number of Days After Vulnerability Publication

Top 5 Zero-Day Vulnerabilities – Days of Exposure and Days to Patch
Source: Symantec

31B

 The total number of days between the vendor’s publication date and the

subsequent patch date for the top five most frequently exploited zero-day
vulnerabilities grew from 19 days in 2013 to 295 days in 2014. Fifty-seven
percent of the attacks exploiting these top five zero-day vulnerabilities were
blocked by Symantec Endpoint technology in the first 90 days, often before
a patch was made available.

SHARE
THIS

2015 Internet Security Threat Report  Top 5 Zero-Day Vulnerabilities, Time of Exposure & Days to Patch

87 http://www.symantec.com/connect/blogs/sandworm-

windows-zero-day-vulnerability-being-actively-exploited-

targeted-attacks

88  http://www.symantec.com/connect/blogs/how-

elderwood-platform-fueling-2014-s-zero-day-attacks

MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

68

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

In a different case, a previously undiscovered vulnerability in Microsoft Windows allowed the
Sandworm cyberespionage group to install malware on targeted organizations,87 including NATO,
as well as several Ukrainian and Western European government organizations, energy companies,
and telecommunications companies.

The Elderwood platform was first identified in 2012 but continues to be maintained. At the start
of 2014, for example, it exploited three new zero-day vulnerabilities to attack its victims.88 Twen-
ty-four zero-day vulnerabilities were discovered in 2014, just one more than the all-time high of
2013, indicating a new norm in zero-day vulnerabilities being discovered and exploited. There may
be many more that remain undiscovered and attackers are keeping to themselves for now.

The value and importance of an exploit for a zero-day vulnerability for an attacker comes in two
ways. First, any unpublished vulnerability has enormous value if it can be exploited by an attacker
to gain remote access or perform reconnaissance. Second, an exploit can reap enormous reward by
taking advantage of the delay between a vendor’s becoming aware of the vulnerability and the time
taken to provide a patch. It can take several days, weeks, or even months for a patch to be available
and even longer before it is widely deployed.

For the top five most frequently exploited zero-day vulnerabilities published in 2014, the total
number of days between the vendor publication date and the patch date grew to 295 days, up from
19 in 2013. The average time taken between publication and patch also grew, to 59 days, up from
4 in 2013. The most frequently exploited zero-day in 2014, CVE-2013-7331, was first identified
in 2013, hence its classification; however, its existence was not disclosed to the public until the
following year. It was a further 204 days before the vendor was able to publish a patch. The number
two and three most frequent zero-day exploits also had long time-to-patch windows of 22 and 53
days, respectively. Both of these windows are larger than the average seen in 2013.

 Twenty-four zero-days were

discovered in 2014, consistent
with the all-time high of 2013.

SHARE
THIS

23

24

30

25

20

15

10

5

15

13

14

14

12

9

8

2006

2007

2008

2009

2010

2011

2012

2013

2014

40

Zero-Day Vulnerabilities, Annual Total, 2006–2014
Source: Symantec

2015 Internet Security Threat Report  Zero-Day Vulnerabilities, Annual TotalMOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

69

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Shifting Targets and Techniques

By the Symantec Managed Adversary
& Threat Intelligence team

As Symantec has worked to protect our customers over the
years, we have noted that our cyber adversaries demon-
strate considerable agility and adaptability. This is enabling
a proliferation of targeted attacks by actors other than
governments, who were previously believed to have had a
monopoly on this capability and intent. This remains the
case in 2014. Symantec follows and reports on adversar-
ies—those actors conducting malicious attacks—as well as
their tools, techniques, and activities through its DeepSight
Adversary Intelligence service.89 Two of the changes we
observed in 2014 relate to shifting techniques and targets.

Cybercriminals are increasingly combining malicious
activity with benign behavior to target networks globally.
One technique that actors use when targeting environments
is to limit the use of malware and detectable attack tools in
order to avoid detection and subsequent security improve-
ments made by defenders. While intrusions involving
spear-phishing emails containing malware and second-
stage-attack malware to maintain network access remain
prevalent, the use of privileged user accounts with tools
that generate legitimate network activity, such as network
administration tools, has become common. Symantec
has discovered and exposed such network intrusions
and methods of maintaining persistence within enter-
prise customers in the retail sector this year, and expects
increasing adoption of this technique across the adversary
community.

To mitigate the risk of these types of attacks, defenders,
in addition to relying on signature-based detection, should
identify and minimize risks from legitimate but unnec-

essary services running on their networks that could be
utilized by attackers for lateral movement, privilege esca-
lation and exfiltration. They should also address risks from
asymmetric attack vectors such as network connectivity
with less well-defended parties, such as vendors.

While attacks against financial and other high-profile
industries continue unabated, a number of cyber espionage
campaigns discovered in 2014 targeted key sectors—such
as energy and manufacturing—that use industrial control
system (ICS) technologies to automate physical processes.
Over the last year, Symantec detected multiple campaigns
against ICS technologies such as actors using BlackEnergy
malware to exploit specialized ICS software programs, and
the Dragonfly group using Trojanized ICS software bundles
that distribute Backdoor.Oldrea90 (a.k.a. Havex, and used
by the Dragonfly group) to perform reconnaissance on ICS
network protocols and ports. Given the potential impact
such attacks can have on targeted enterprises and nations,
it is reasonable to expect certain categories of adversaries
will continue to enhance their capabilities to exploit ICS
weaknesses.

Defenders of ICS technologies should not rely on the
limited connectivity and unique architectures of these
environments for protection. Given the sensitivity of the
assets, strong security controls should be implemented and
the deterministic nature of the environment leveraged to
identify abnormal behavior through security monitoring.

89  http://www.symantec.com/deepsight-products/

90  http://www.symantec.com/security_response/writeup.

jsp?docid=2013-052817-2105-99

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

70

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

It is this weakness—the window of vulnerability—that the espionage attack groups depend on for
their success. For example, a website already compromised to host a watering hole exploit may stop
using a zero-day exploit once the software vendor publishes information about the vulnerability’s
existence, even though a patch may not yet be available. The attackers may then switch over to
using another as-of-yet undiscovered exploit, a further example of the enormous resources at their
disposal.

Threat Intelligence

Threat intelligence is now a vital component for any organization to understand regarding the
potential threats against their networks. Investing in great technology solves only part of the
problem, and a combination of threat intelligence, risk management, and the best technical
solutions will help not only reveal who is being targeted but also how and why. Understanding
the threats is critical, as businesses should now expect to be attacked. The question is not “if” but
“when.”

Advanced attackers use exploit toolkits against not only older vulnerabilities but also new zero-day
ones, and being good at defense means being harder to breach. Threat intelligence can provide
a prioritized list of suspicious incidents by correlating all available information from across the
enterprise. A continual assessment of not only the people and their skills but also the processes
will ensure the best response is followed and that processes are continually updated and skills are
maintained. If businesses can become harder to breach, the attackers will have to work harder;
don’t be the weakest link in the supply chain.

Techniques Used In Targeted Attacks

100%

50%

50%

39%

41%

31%

25%

19%

31%

30%

34%

32%

18%

0

2011

2012

2013

2014

Large
Enterprises
2,500+
Employees

Medium-Size
Businesses
251 to 2,500
Employees

Small
Businesses (SMBs)
1 to 250
Employees

21A

Distribution of Spear-Phishing Attacks by Organization Size
Source: Symantec

 Forty-one percent of spear-

phishing emails were directed
at large enterprises in 2014.
As in 2013, spear-phishing
attacks on small- and medium-
size businesses in 2014 show
that being small and relatively
anonymous is no protection. In
fact, attacks in 2014 confirm
that determined attackers often
attack a target company’s supply
chain as a way of outflanking its
security.

SHARE
THIS

2015 Internet Security Threat Report  Distribution of Spear-Phishing Attacks by Organization Size MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

71

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

 In 2014, 83 percent of large
enterprises were targeted in
spear-phishing campaigns,
compared with 43 percent in
2013.

SHARE
THIS

 Overall in 2014, the

manufacturing sector was
targeted with the greatest volume
of spear-phishing attacks, as 1 in
5 (20 percent) were directed at
manufacturing organizations.

SHARE
THIS

Organization Size

Risk Ratio

   2014

   2013

100%

Large Enterprises
2,500+ Employees

Medium-Size Businesses
251–2,500 Employees

Small Businesses (SMBs)
1–250 Employees

1 in 1.2  83%

1 in 2.3  43%

1 in 1.6  63%

1 in 3.5  33%

1 in 2.2  45%

1 in 5.2  19%

21B

Risk Ratio of Spear-Phishing Attacks by Organization Size
Source: Symantec

Manufacturing

Services—Nontraditional

Finance, Insurance
& Real Estate

Services—Professional

Wholesale

Transportation, Gas,
Communications, Electric

Public Administration (Gov.)

Retail

Mining

Construction

2014

2013

 13

 14

 20%

 20

 18

 13

 11

 15

 10

 16

 5

 5

 7
 6

 3

 2

 1
 1

 1
 1

34

Top 10 Industries Targeted in Spear-Phishing Attacks, 2013–2014
Source: Symantec

5

10

15

20

25%

2015 Internet Security Threat Report  Risk Ratio of Spear-Phishing Attacks by Organization SizeTop 10 Industries Targeted in Spear-Phishing Attacks
MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

72

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

 The mining industry was the

most heavily targeted in 2014,
with 43 percent (1 in 2.3) of
mining organizations being
targeted at least once during the
year. The mining classification
includes energy extraction
organizations, as well as those
mining metals and quarrying
minerals.

SHARE
THIS

Industry

Mining

Wholesale

Manufacturing

Transportation,
Communications, Electric,
Gas & Sanitary Services

Public Administration
(Government)

Finance, Insurance
& Real Estate

Risk Ratio

   2014

   2013

100%

1 in 2.3  44%

1 in 2.7  37%

1 in 2.9  34%

1 in 3.4  29%

1 in 3.0  33%

1 in 3.2  31%

1 in 3.4  29%

1 in 3.9  26%

1 in 3.4  29%

1 in 3.1  32%

1 in 4.8  21%

Retail

1 in 4.8  21%

Services—Non Traditional

1 in 6.5  15%

Services—Professional

1 in 6.9  15%

37

Risk Ratio of Spear-Phishing Attacks by Industry
Source: Symantec

2015 Internet Security Threat Report  Risk Ratio of Organizations in an Industry Impacted  by Targeted Attack Sent by Spear-Phishing EmailRisk Ratio of Spear-Phishing Attacks by IndustryMOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

73

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

2014

2013

2012

24

Spear-Phishing Emails per Day
Source: Symantec

73
-12%

83
-28%

116

2014

Change

2013

Change

2012

Campaigns

841

+8%

779

+91%

408

Recipients per
Campaign

Average Number of
Email Attacks per
Campaign

18

25

-22%

-14%

23

29

-80%

111

-76%

122

Average Duration
of a Campaign

9 Days

+13%

8 Days

+32%

3 Days

25

Spear-Phishing Email Campaigns, 2012–2014

Source: Symantec

SHARE
THIS

BACK TO TABLE OF CONTENTS

 The number of spear-phishing
emails detected by Symantec
fell slightly, but there are no
signs that the intensity of
targeted attacks is also falling.
The number of overall email
campaigns has increased, and
spear-phishing emails have
become subtler, using custom-
written malware and carefully
crafted, socially engineered
messages in order to bypass
security.

 In 2014, there was an 8 percent
increase in targeted attacks
via spear-phishing campaigns,
despite an overall decline by
12 percent in the number of
spear-phishing emails sent
daily. Spear-phishing attacks in
2014 were less spam-like, with
fewer high-volume recipients.
Attackers have taken more
time to plan and coordinate
attacks before launching them,
paying particular attention
to reconnaissance. Symantec
has also observed several
“distributed targeted attacks”
being coordinated between
groups of attackers seemingly
working together. These
attacks have been planned and
distributed in such a way that
even if they were of relatively
high volume, they wouldn’t have
qualified as spam.

2015 Internet Security Threat Report  Spear-Phishing Emails per DaySpear-Phishing Email CampaignsMOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

74

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

26

Spear-Phishing Email Word Cloud
Most commonly used words in spear-phishing attacks

Job Role

Risk Ratio

   2014

100%

Sales/Marketing

1 in 2.9

  35%

Finance

1 in 3.3

  30%

Operations

1 in 3.8

  27%

R&D

IT

1 in 4.4

  23%

1 in 5.4

  19%

Engineering

1 in 6.4

  16%

HR & Recruitment

1 in 7.2

  14%

Other

1 in 9.3

  11%

36

Risk Ratio of Spear-Phishing Attacks by Job Role
Source: Symantec

 Individuals in sales/marketing

job roles were the most targeted
in 2014, with 1 in 2.9 of them
being targeted at least once; this
is equivalent to 35 percent of
sales/marketing personnel.

SHARE
THIS

2015 Internet Security Threat Report  Spear-Phishing Email Word CloudRisk Ratio of Spear-Phishing Attacks by Job RoleMOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

75

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

 Individual contributors were the
most frequently targeted level
of seniority in 2014, with 1 in
3.7 of them being targeted at
least once; this is equivalent to
27 percent of individuals at that
level.

SHARE
THIS

 The average number of spear-
phishing attacks per day
continued to decline in 2014.

Job Level

Risk Ratio

   2014

100%

Individual Contributor

1 in 3.7

  27%

Manager

1 in 3.8

  26%

Intern

Director

Support

Other

1 in 3.9

  26%

1 in 5.4

  19%

1 in 7.6

  13%

1 in 9.3

  11%

36A

Risk Ratio of Spear-Phishing Attacks by Job Level
Source: Symantec

250

225

200

175

150

125

100

75

50

25

DNOSAJJMAMFJ

DNOSAJJMAMFJ

DNOSAJJMAMFJ

2012

2013

2014

32

Average Number of Spear-Phishing Attacks per Day, 2012–2014
Source: Symantec

2015 Internet Security Threat Report  Risk Ratio of Spear-Phishing Attacks by Job LevelAverage Number of Spear-Phishing Attacks per DayMOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

76

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

Rank

Attachment
Type

2014 Overall
Percentage

Attachment
Type

2013 Overall
Percentage

1

2

3

4

5

6

7

8

9

10

.doc

.exe

.scr

.au3

.jpg

.class

.pdf

.bin

.txt

.dmp

38.7%

22.6%

9.2%

8.2%

4.6%

3.4%

3.1%

1.9%

1.4%

1.0%

.exe

.scr

.doc

.pdf

.class

.jpg

.dmp

.dll

.au3

.xls

31.3%

18.4%

7.9%

5.3%

4.7%

3.8%

2.7%

1.8%

1.7%

1.2%

39

Analysis of Spear-Phishing Emails Used in Targeted Attacks, 2013–2014
Source: Symantec

BACK TO TABLE OF CONTENTS

 Microsoft Office document
file attachments overtook
executable files to become the
most frequently used type of
attachments used in spear-
phishing attacks. They were used
in 39 percent of attacks during
2014. Malicious document
attachments could also be
rendered safe before reaching
the email gateway through
the use of strong cloud-based
filtering that can identify and
eliminate spear-phishing attacks
before they reach the corporate
network.

SHARE
THIS

 At least 32 percent of spear-
phishing attacks could be
prevented if companies blocked
executable-type file attachments
and screensavers at the email
gateway.

SHARE
THIS

2015 Internet Security Threat Report  Analysis of Spear-Phishing Emails Used in Targeted AttacksMOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

77

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

D
A
T
A
B
R
E
A
C
H
E
S
&
P
R
I
V
A
C
Y

2015 Internet Security Threat Report

MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

78

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Data Breaches

In 2014, cybercriminals continued to steal private information on an epic scale, by direct attack
on institutions such as banks and retailers’ point-of-sale systems.

At a Glance

While there were fewer “mega breaches” in 2014, data breaches are still a significant issue.
The number of breaches increased 23 percent and attackers were responsible for the majority
of these breaches.

Fewer identities were reported exposed in 2014, in part due to fewer companies reporting this
metric when disclosing that a breach took place. This could indicate that many breaches—
perhaps the majority—go unreported or undetected.91,92

2014

2013

2012

3

Total Breaches
Source: Symantec

2014

2013

2012

1

Breaches with More Than 10 Million Identities Exposed
Source: Symantec

312
+23%

253
+62%

156

4

8

1

 There were fewer mega

breaches (with more than 10
million identities disclosed) in
2014 than 2013.

 The overall number of data

breaches increased.

 Attackers are responsible for
the majority—49 percent—of
breaches.

SHARE
THIS

 Attacks on point-of-sale

systems have grown in scale
and sophistication.

 According to a survey carried

out by Symantec, 57 percent of
respondents are worried their
data is not safe.

 While 2014 had fewer mega

breaches (greater than 10 million
identities exposed per breach),
the total number of breaches
increased 23 percent, suggesting
breach activity continues to rise.

91  http://www.insurancejournal.com/news/

west/2014/03/07/322748.htm

92  http://www.ponemon.org/news-2/7

2015 Internet Security Threat Report  Total BreachesBreaches with More Than 10 Million Identities ExposedMOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

79

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

The release of nearly 200 celebrity photographs on the website 4chan in August 2014 received
wide media coverage and increased consumer anxiety about privacy. According to Apple, the
images were obtained using highly tailored targeted attacks on individual accounts rather than
general weaknesses in the company’s security.93

People’s personal and financial information continues to command high prices on the black
market, and that means cybercriminals will continue to target major institutions for large scores
and small companies for small, easy ones. Many breaches are preventable with the right security
measures, including elements such as data loss prevention, encryption, and intrusion detection
systems, as well as with effective security policies and training.

93  https://www.apple.com/uk/pr/

library/2014/09/02Apple-Media-Advisory.html

Cause

Attackers

Accidentally
Made Public

Theft or Loss
of Computer
or Drive

Insider Theft

Number of
Incidents

153

87

67

72

66

69

26

15

Percent

   2014

   2013

100%

49%

34%

22%

29%

21%

27%

8%

6%

42

Top Causes of Data Breach, 2013–2014
Source: Symantec

2014

2013

2012

1.1 Million
-49%

2.2 Million
+261%

605 Thousand

Average Identities Exposed per Breach
Source: Symantec

5

 At 49 percent, the majority
of breaches were caused by
attackers, up from 34 percent
in 2013. However, a further
22 percent of breaches were
classified as “accidentally made
public,” and 21 percent were due
to theft or loss of a computer
or drive. These latter types of
data exposure are preventable
if data is encrypted, effectively
eliminating the impact of the
data’s falling into the wrong
hands. The good news is that this
is down from 56 percent in 2013.

 The average number of identities
exposed per breach declined
in 2014 due to fewer mega
breaches compared to 2013.

SHARE
THIS

2015 Internet Security Threat Report  Top Causes of Data BreachAverage Identities Exposed per BreachMOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

80

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

 The median number of identities
exposed has increased three
percent in 2014.

7,000
+3%

6,777
-19%

8,350

2014

2013

2012

6

Median Identities Exposed per Breach
Source: Symantec

)
S
N
O
I
L
L
I
M

(

D
E
S
O
P
X
E
S
E
I
T
I
T
N
E
D

I

180

160

140

120

100

24

80

60

40

20

43

J
2013

159

37

130

33

34

147

31

113

29

27

27

27

26

26

25

22

22

22

24

78

59

23

14

19

17

15 15
53

15

17

23

12

3

8

6

.3 .8

8

3

2

MAMF

J

J

A

S

O

N

D

MAMF

J
2014

32

10

1

J

J

A

S

6.5

.4

N

D

1

O

45

40

35

30

25

20

15

10

5

S
T
N
E
D
C
N

I

I

43

Timeline of Data Breaches, 2013–2014
Source: Symantec

Identities Exposed (Millions)

Incidents

2015 Internet Security Threat Report  Median Identities Exposed per BreachTimeline of Data Breaches

MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

81

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

 One significant downturn in

2014 is the number of identities
exposed as the result of a data
breach. In 2013 we reported that
there were 552 million identities
exposed. In 2014 this is down
significantly, to 348 million
identities.

SHARE
THIS

348 Million
-37%

552 Million
+493%

93 Million

2014

2013

2012

4

Total Identities Exposed
Source: Symantec

On the surface it appears that there were far fewer identities exposed in 2014. The fact that
there were fewer breaches reported containing more than 10 million identities plays a part in
this drop, if anything for sheer volume. It is also possible that large organizations sat up and
took notice of the major breaches that occurred toward the end of 2013, implementing security
policies that reduced the risk of a data breach, such as rolling out a data loss prevention (DLP)
solution that prevents most data from being exfiltrated, even if attackers succeed in penetrating
the network.

While these items no doubt played a part, our numbers point to another possibility: the number
of organizations that are withholding information on the number of identities exposed is
increasing. In 2013, 34 out of 253 breaches, or 13 percent, did not report the number of identities
exposed. In comparison, 61 out of 312, or 20 percent, of breaches disclosed in 2014 didn’t include
this information. This equates to 1 in 5 breaches not reporting on the breadth of data exposed.

It’s difficult to definitively explain why this information is not being shared publicly. In some
cases it’s possible the organizations find it too challenging to determine the number of identities
exposed. In others, this information likely remains undisclosed to help save face in what clearly
has a negative impact on an organization’s public reputation.

What is most concerning, however, is this trend could point to a situation where a large number
of breaches are not being disclosed to the public at all. While there are many industries, such as
healthcare and some government organizations where a breach must legally be reported, most
industries do not have such laws. As a result, some organizations may decide to withhold infor-
mation about a breach to protect their reputations, and they do not face penalties as a result.
This may change in the coming years, as many governing agencies around the world are already
looking at bringing in regulation surrounding the proper disclosure of data breaches.

2015 Internet Security Threat Report  Total Identities ExposedMOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

82

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Rank

Sector

1

2

3

4

5

6

7

8

9

Healthcare

Retail

Education

Gov. & Public Sector

Financial

Computer Software

Hospitality

Insurance

Transportation

10

Arts and Media

Number
of Incidents

116

Percentage of Incidents

100%

  37%

 For the fourth year in a row, the
healthcare sector reported the
largest number of data breaches.

SHARE
THIS

34

31

26

19

13

12

11

9

6

  11%

  10%

  8%

  6%

  4%

  4%

  4%

  3%

  2%

6B

Top 10 Sectors Breached by Number of Incidents
Source: Symantec

Rank

Sector

Retail

Financial

Number of
Identities
Exposed

 205,446,276

 79,465,597

Percentage of Identities Exposed

100%

 The retail sector was responsible
for 59 percent of all identities
exposed in 2014, followed by the
financial sector, with 23 percent.

  59%

SHARE
THIS

  23%

1

2

3

4

5

6

7

8

9

Computer Software

 35,068,405

  10%

Healthcare

 7,230,517

Gov. & Public Sector

 7,127,263

Social Networking

 4,600,000

Telecom

Hospitality

Education

 2,124,021

 1,818,600

 1,359,190

10

Arts and Media

 1,082,690

  2%

  2%

  1%

  .6%

  .5%

  .4%

  .3%

6A

Top 10 Sectors Breached by Number of Identities Exposed
Source: Symantec

2015 Internet Security Threat Report  Top 10 Sectors Breached by Number of IncidentsTop 10 Sectors Breached by Number of Identities Exposed

MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

83

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Retailers Under Attack

Attackers clearly have retailers in their cross hairs, if the increase in data breaches containing
financial information is any indication. The retail industry again has the dubious distinction of
being the industry liable for the largest number of identities exposed, accounting for almost 60
percent of all identities reported exposed, up from 30 percent in 2013. Financial information has
moved to the fourth most common type of information exposed in a breach. In 2013, 17.8 percent
of breaches contained financial information, but in 2014 this number jumped to 35.5 percent.

This financial information can range from bank account details to tax-related documents, but, in
most cases, this information is credit or debit card details. Online retailers play a significant part,
but so do attacks on point-of-sale systems: the credit card swipe machines that have become so
ubiquitous in our retail lives.

Although the first attacks on retail point-of-sale systems date back to 2005, Symantec saw an
upsurge in attacks in 2014. It is now one of the biggest sources of stolen payment card data94
and is at the root of 2013’s and 2014’s biggest data breaches.

Type of Information

Percentage

   2014

   2013

100%

Real Names

Gov. ID Numbers
(e.g, SSN)

Home Addresses

Financial Information

Birth Dates

Medical Records

Phone Numbers

Email Addresses

User Names & Passwords

Insurance

69%
72%

45%
40%

43%
38%

36%
18%

35%
43%

34%
34%

21%
19%

20%
15%

13%
12%

11%
6%

2

Top 10 Types of Information Exposed
Source: Symantec

94  http://securityresponse.symantec.com/content/en/

us/enterprise/media/security_response/whitepapers/

attacks_on_point_of_sale_systems.pdf

 Real names, government ID

numbers, and home addresses
were the top three types of
information breached in 2014.
The exposure of financial
information grew from 17.8
percent to 35.5 percent in 2014,
the largest increase within the
top 10 list of information types
exposed.

SHARE
THIS

2015 Internet Security Threat Report  Top-Ten Types of Information ExposedMOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

84

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Point-of-sale systems are vulnerable because of widespread lack of security, including poor or
nonexistent encryption of data, software vulnerabilities, reliance on out-of-date software such
as Microsoft Windows XP (which Microsoft stopped supporting in 2014), and the slow adoption
of chip-and-PIN technology outside Europe. With new ways to pay, such as Apple Pay, and chip-
and-PIN cards finally being adopted in the United States, point-of-sale data should become more
secure over the next few years.

Nonetheless, point-of-sale systems are likely to remain a top target for attacks in the near term.
Credit card companies are quick to spot anomalous spending patterns, as are observant card
owners. This means that criminals need a steady supply of “fresh” card numbers, and the online
economy provides a ready market of buyers and sellers. 95

Privacy and the Importance of Data Security

The prevalence of data breaches over the past number of years has certainly had an impact on
consumers’ views concerning their private information. Symantec carried out a survey on the
topic of privacy within the European Union, publishing some interesting findings in the “State of
Privacy Report 2015.” 96

For instance, 59 percent of respondents have experienced a data protection issue in the past.
These issues include not only being notified of a data breach by a company that they use but also
having an email or social media account hacked, having bank details stolen, being a victim of
online identify theft, getting a computer virus, or responding to an online scam or fake email.

Overall, 57 percent of respondents are worried their data is not safe. This is no small matter,
as data security is very important to consumers, considering that 88 percent say this is an
important factor when choosing a company to do business with—more important than the
quality of the product (86 percent) or the customer service experience (82 percent).

On top of that, only 14 percent of respondents were happy to share their data with third parties,
with 47 percent being unhappy to share any data and 35 percent requiring some form of check
on exactly what data would be shared.

Those surveyed also indicated that they are actively adopting a self-moderation approach
to their personal data and taking the matter into their own hands. According to Symantec’s
research, over half of those surveyed (57 percent) are now avoiding posting personal details
online. Another popular approach to self-moderation could also have chilling repercussions for
business, as 1 in 3 consumers admitted they provide false information in order to protect their
privacy.

On another note, attackers have become more patient, breaching organizations’ defenses and
lying in wait, building up knowledge of behavior patterns from activity on the network and
learning who does what and how. In this way, attackers are better able to target consumers while
impersonating and exploiting them. Attackers often use legitimate, stolen credentials and use
patience in conducting such attacks, as opposed to springing attacks immediately following a
breach. By carefully monitoring these cycles of behavior for a long time, cybercriminals make
sure their attacks appear like normal patterns of behavior.

The traditional perimeter for an organization is no longer as clear as it once was—the boundaries
are blurred—and mobile devices make this even more difficult to manage. Data is increasingly
stored not only on mobile devices but also in the cloud. Mobile devices have become the key to
accessing this data since passwords are more likely to be cached on mobile devices, which are
less likely to be encrypted than a stolen laptop.

95  http://www.symantec.com/connect/blogs/

demystifying-point-sale-malware-and-attacks

96  http://www.symantec.com/content/en/us/about/

presskits/b-state-of-privacy-report-2015.pdf

1 in 3 consumers
admitted they
provide false
information in order
to protect their
privacy.

SHARE
THIS

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

85

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Data Breaches in the Healthcare Industry

By Axel Wirth and David Finn

Driven by market forces and the desire to improve health
delivery, reduce costs, and comply with government
mandates, healthcare providers are adopting electronic
records and digital clinical systems in record numbers. In
addition, an aging population requiring management of
chronic diseases, new diagnostic methodologies delivering
higher-quality results, and an increasing number of covered
patients are leading to rapidly growing data volumes. This
all results in a more complex IT infrastructure, increasing
needs for integration and exchange of information, new care
delivery and reimbursement models, and the accumulation
of data. These combined trends are making the healthcare
industry more attractive to attackers and have put providers
at an increasing risk of data breaches, both intentional and
accidental.

SHARE
THIS

Symantec saw a 25 percent increase
in the number of healthcare data
breaches in 2014, two percentage points higher than the
rate across all industries. Unlike data breaches as a whole,
human error and device theft—related or unrelated to the
data present—still make up the majority of these incidents.
Lost or stolen devices are accountable for the largest
portion of breaches in the healthcare industry. According
to the Norton Cybercrime Index, 44 percent of healthcare
breaches were the result of lost or stolen devices, a 10
percent increase over the previous year. The number of
identities being accidentally exposed publicly as the result
of error was also up approximately 11 percent in 2014.

However, targeting patient medical information for
purposes of medical identity theft, financial fraud, or health
insurance fraud has become an increasing problem. Specif-
ically interested in personally identifiable information (PII)
or protected health information (PHI), thieves appear to
have more incentive to either hack into healthcare organiza-
tions or attempt to hire insiders to obtain electronic copies
or printouts of patient records. In fact, the number of data
breaches in the healthcare industry that were the result of
insider theft nearly doubled in 2014. Data breaches that
were the result of attacks were up 82 percent in 2014.

More advanced attacks may target larger volumes of
electronic records for identity theft, such as in the retail

sector. There are also other criminal activities, including
extortion, blackmail, or celebrity snooping. However, an
unprecedented number of cases have been reported around
the globe and across all types of healthcare organizations,
from large academic medical centers to small community
hospitals, when compared with any other industry. Neither
location nor size provides any protection, as in the case of a
22-bed rural community hospital in Southern Illinois, which
received stolen patient data in an email with the request to
pay a ransom or the information would be made public.97

A number of hospitals have mature cybersecurity programs
in place, but many are still struggling with basic goals like
implementing encryption to protect data on lost or stolen
mobile devices, laptops, or data carriers. Too many health-
care organizations are still underinvesting in cybersecurity,
making them an easy target for cybercriminals’ increasingly
sophisticated and targeted attacks.

Unfortunately, for the most part, the healthcare industry is
not prepared to face today’s cybersecurity risks, no matter
if they are hospitals, pharmaceutical or biotech companies,
medical device manufacturers, health insurers, national
health agencies, or employers.

Many organizations, such as the SANS Institute, U.S.
Department of Homeland Security, FBI, and FDA, have all
issued dire warnings about the cybersecurity risks to the
healthcare industry. And this is not just a U.S.-centric issue,
as breaches have been reported in many other countries.
There is a thriving underground market for medical infor-
mation, and criminals are monetizing it in many ways and
for many reasons.

First, medical data sets tend to be more complete when
compared to what can be obtained elsewhere. They include
demographics, government ID numbers, bank and credit
card accounts, insurance plan credentials, disease statuses,
and physical descriptors. This data can be used for identify
theft, financial fraud, prescription fraud, obtaining medical
services, or reselling the data on the black market. Physical
characteristics of patients could be misused to obtain
passports, visas, or other identity cards.98 In short, it is
enticing for malicious agents due to the breadth and depth
of the data.

97  “Illinois hospital reports data blackmail”; PC World;

Dec. 15, 2014; http://www.pcworld.com/article/2859952/

illinois-hospital-reports-data-blackmail.html

98  “Medical identity theft proves lucrative in myriad

ways”; Fierce Health IT; Oct. 21, 2014; http://www.

fiercehealthit.com/story/medical-identify-theft-

proves-lucrative-myriad-ways/2014-10-21?utm_

medium=nl&utm_source=internal

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

86

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Medical identity theft has been shown to be much more
costly to the victims in ways other than just financial.
Incorrect data in your medical records could lead to
incorrect or delayed diagnoses or treatments, could affect
job prospects, and could be difficult to correct. Unlike
financial fraud, where consumers have limited liability,
there is little protection against healthcare fraud and the
long-term consequences.99

Where credit card numbers may fetch $0.50 to $1 in the
underground economy, basic identity and insurance infor-
mation can be valued up to $10100 or even as high as $50101
based on its completeness, which may even include ready-
made insurance membership cards, driver’s licenses, and
credit cards.

SHARE
THIS

Breach numbers in healthcare are high and they are
trending up. Traditionally, device loss or theft has been
the predominant challenge for healthcare organizations,
but we are now seeing an increase in targeted attacks on
healthcare organizations, resulting in breaches with a
significant impact on healthcare providers and patients.
Overall, unintentional causes, such as losing devices or
accidentally exposing data, are still the most common, but
breaches caused by malicious actors, such as attackers or
insider thieves, are increasing far more rapidly. This trend
highlights the need for healthcare organizations to ensure
there are processes in place to handle theft or loss, as well
as policies to protect against outside agencies attempting to
gain access to lucrative data.

99  “The Growing Threat of Medical Identity Fraud:

A Call to Action”; Medical Identity Fraud Alliance

(MIFA); July 2013; http://medidfraud.org/wp-content/

uploads/2013/07/MIFA-Growing-Threat-07232013.pdf

100  “Your medical record is worth more to hackers

than your credit card”; Reuters; Sept. 24, 2014; http://

www.reuters.com/article/2014/09/24/us-cybersecurity-

hospitals-idUSKCN0HJ21I20140924

101  “Stolen EHR Charts Sell for $50 Each on Black

Market”; MedScape; April 18, 2014; http://www.

medscape.com/viewarticle/824192

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

87

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

I

E
-
C
R
M
E
&
M
A
L
W
A
R
E

2015 Internet Security Threat Report

MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

88

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

At a Glance

 Prices are holding steady in
the underground economy,
suggesting continuing high
levels of demand for stolen
identities, malware, and
e-crime services.

 The number of vulnerabilities
is down relative to 2013,
but the general trend is still
upward.

 The number of new malware

variants grew by 317,256,956
in 2014—a 26 percent
increase compared with 2013.

 Ransomware is getting nastier
and increasing in volume. The
amount of crypto-ransomware
has also grown over 45 times
larger than in 2013.

 The number of bots declined

by 18 percent in 2014.

Cybercriminals rely
on an underground
online economy to
buy and sell services
and malware.

SHARE
THIS

102  http://www.symantec.com/connect/blogs/

underground-black-market-thriving-trade-stolen-data-

malware-and-attack-services

103  http://www.symantec.com/connect/blogs/

underground-black-market-thriving-trade-stolen-data-

malware-and-attack-services

E-Crime and Malware

Every day, personal banking details are phished by fake emails and websites. Computers
infected with malware are used to send out spam or contribute to distributed denial-of-service
(DDoS) attacks. Perhaps the most unlucky see all their files encrypted and their computer made
unusable by ransomware.

Email continues to be an effective delivery vehicle for spam, phishing, and malware, and overall,
the proportion of emails that include malware is rising. Cybercriminals rely on an underground
online economy to buy and sell services and malware and to fence stolen credit cards and
botnets.

Working with security firms, including Symantec, law enforcement has continued to disrupt
botnets and make arrests. This has produced noticeable, if temporary, improvements on the
overall levels of cybercrime.

The Underground Economy

The underground black market is thriving. In the darker corners of the Internet, there’s a huge
trade in stolen data, malware, and attack services.102 Criminals are moving their illegal market-
places further from public gaze, including using the anonymous Tor network and limiting access
to an invitation-only basis.103 Price changes give some indication of supply and demand. Overall,
email prices have dropped considerably, credit card information has declined a little, and online
bank account details have remained stable.

 Underground economy prices for credit cards in various countries.

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

89

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Cybercriminals can also buy malware, attack kits, and vulnerability
information off the shelf. They can even buy “crimeware as a service,”
which comes with the entire infrastructure to run online scams.

SHARE
THIS

These markets allow a division of labor. Some people specialize in writing Trojans and viruses,
and others in malware distribution, botnets, or monetizing stolen credit card details. Some of
these markets have existed for at least 10 years, but Symantec sees increasing professionaliza-
tion of all the elements. Any product or service directly linked to monetary profit for the buyer
retains a solid market price.104

A drive-by download web toolkit, which includes updates and 24/7 support, can be rented
for between $100 and $700 per week. The online banking malware SpyEye (detected as
Trojan.Spyeye) is offered from $150 to $1,250 on a six-month lease, and DDoS attacks can be
ordered from $10 to $1,000 per day.105

Item

2014 Cost

Uses

1,000 Stolen Email Addresses

$0.50 to $10

Spam, Phishing

Credit Card Details

$0.50 to $20

Fraudulent Purchases

Scans of Real Passports

$1 to $2

Identity Theft

Stolen Gaming Accounts

$10 to $15

Attaining Valuable Virtual Items

Custom Malware

$12 to $3500

Payment Diversions, Bitcoin Stealing

1,000 Social Network Followers

$2 to $12

Generating Viewer Interest

Stolen Cloud Accounts

$7 to $8

Hosting a Command-and-Control
(C&C) Server

1 Million Verified Email
Spam Mail-outs

$70 to $150

Spam, Phishing

Registered and Activated Russian
Mobile Phone SIM Card

$100

Fraud

2b

Value of Information Sold on Black Market

Source: Symantec

104  http://www.symantec.com/connect/blogs/

underground-black-market-thriving-trade-stolen-data-

malware-and-attack-services

105  http://www.symantec.com/connect/blogs/

underground-black-market-thriving-trade-stolen-data-

malware-and-attack-services

2015 Internet Security Threat Report  Value of Information Sold on Black MarketMOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

90

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Malware

At the end of 2013, Russian authorities arrested “Paunch,” the alleged author of the Blackhole
exploit kit, which was responsible for a large number of infections worldwide.106,107 It was a small
victory in a long war against malware in all its forms.

Inevitably, other attack kits have come up to fill the void. Malware designed to steal bank details
continues to be prevalent. Malware targeting new “markets” appeared in 2014, with the Snifula
banking Trojan attacking Japanese financial institutions108 and an indigenous group of attacks
emerging in the Middle East using malware called njRAT. 109

2014

2013

317 Million
+26%

252 Million

 With more than 317 million new
pieces of malware created in
2014, or close to 1 million new
pieces of unique malware each
day, the overall total number of
malware is now 1.7 billion.

106  http://en.wikipedia.org/wiki/Blackhole_exploit_kit

107  http://krebsonsecurity.com/2013/12/meet-paunch-

the-accused-author-of-the-blackhole-exploit-kit/

108  http://www.symantec.com/connect/blogs/snifula-

banking-trojan-back-target-japanese-regional-financial-

institutions

109  http://www.symantec.com/connect/blogs/simple-

njrat-fuels-nascent-middle-east-cybercrime-scene

12b

New Malware Variants  (Added in Each Year)
Source: Symantec

2014

2013

2012

 The email malware rate dropped
to 1 in 244 emails in 2014. While
lower than 2013, this is still
higher than the rate of 1 in 291
emails seen in 2012.

1 in 244

1 in 196

1 in 291

12

Email Malware Rate  (Overall)  Inverse Graph: Smaller Number = Greater Risk

Source: Symantec

2015 Internet Security Threat Report  New Malware VariantsEmail Malware Rate (Overall)MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

91

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

 Twelve percent of email-
borne malware in 2014
contained a malicious link
rather than being attached
to an email, compared with
25 percent in 2013.

 In November 2014, the percent
of email malware that contains
a URL jumped to 41 percent, the
highest seen since August 2013.

 The sudden increase, and
subsequent decline, was
attributed to the activity of
the Cutwail botnet.

12

12%
-13% pts

2014

25

25%
+2% pts

2013

23

23%

2012

11

Email Malware as URL vs. Attachment
Source: Symantec

In October 2014, only seven percent of malicious spam emails contained URL links. That number
jumped to 41 percent in November and continued to climb in early December, thanks to a surge
in social engineering–themed messages, including malicious fax and voice mail notification
emails.

The links in these emails use hijacked domains and have a URL path that leads to a PHP landing
page. If the user clicks on the links, they are led to a malicious file. In particular, we have seen
Downloader.Ponik and Downloader.Upatre being used in these emails. These are well-known
Trojans that are used for downloading additional malware onto compromised computers,
including information stealers like Trojan.Zbot (also known as Zeus).110

Overall, the number of emails distributing malware has declined in 2014, after appearing to have
peaked in 2013.

100%

90

80

70

60

50

40

30

20

10

DNOSAJJMAMFJ

DNOSAJJMAMFJ

DNOSAJJMAMFJ

2012

2013

2014

57

Percent of Email Malware as URL vs. Attachment by Month, 2012–2014
Source: Symantec

110  http://www.symantec.com/connect/blogs/malicious-

links-spammers-change-malware-delivery-tactics

2015 Internet Security Threat Report  Email Malware as URL vs. AttachmentPercent of Email Malware as URL vs. Attachment by MonthMOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

92

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

 There was a significant drop in
the email malware rate during
the late summer, early autumn
of 2014.

 On average there were 729,167
ransomware attacks per month
in 2014.

DNOSAJJMAMFJ

DNOSAJJMAMFJ

DNOSAJJMAMFJ

2012

2013

2014

N

I

1

100

150

200

250

300

350

400

56

Proportion of Email Traffic in Which Malware Was Detected, 2012–2014
Source: Symantec

Inverse Graph: Smaller Number = Greater Risk

1,000

900

800

700

600

500

400

300

200

100

S
D
N
A
S
U
O
H
T

J
2013

JMAMF

J

DNOSA

J
2014

JMAMF

J

DNOSA

46

Ransomware Over Time, 2013–2014
Source: Symantec

2015 Internet Security Threat Report  Proportion of Email Traffic in Which Malware Was Detected0Ransomware Over Time
MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

93

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Ransomware

Ransomware attacks more than doubled in 2014, from 4.1 million in
2103, up to 8.8 million. More concerning is the growth of file-encrypting
ransomware (what Symantec refers to as “crypto-ransomware”), which expanded from 8,274 in
2013 to 373,342 in 2014. This is 45 times more crypto-ransomware in the threat landscape within
a one-year span. In 2013, crypto-ransomware accounted for 0.2 percent (1 in 500) of ransomware
and was fairly uncommon; however, by the end of 2014 it accounted for 4 percent (1 in 25) of all
ransomware.

SHARE
THIS

On a human level, ransomware is one of the nastiest forms of attack for victims. Criminals use
malware to encrypt the data on victims’ hard drives—family pictures, homework, music, that unfin-
ished novel—and demand payment to unlock the files. The best, and pretty much only, defense is to
keep a separate backup of your files, preferably offline, to restore from.

There are many ransomware variants, and no operating system guarantees immunity.111 And while
the advice remains the same—do not pay the criminals—many businesses and individuals simply
want or need their files back. So they pay, and thus the scam remains profitable.

Criminals use
malware to encrypt
the data on victims’
hard drives—
family pictures,
homework, music,
that unfinished
novel—and
demand payment
to unlock the files.

2014

2013

24 K
Per Day

11 K
Per Day

8.8 Million
+113%

4.1 Million

14A

Ransomware Total
Source: Symantec

Crypto-Ransomware

The bad news is that, while ransomware has doubled, between 2013 and 2014 Symantec saw the
amount of crypto-ransomware in the threat landscape grow to be over 45 times larger.112

There are several different crypto-ransomware families, such as Cryptolocker,113 Cryptodefense,114
and Cryptowall,115 but their method of exploitation is the same. Rather than locking your desktop
behind a ransom wall, crypto-ransomware encrypts your personal files and holds the private keys
to their decryption for ransom at a remote site. This is a much more vicious attack than traditional
ransomware.

Methods of infection vary, but commonly it’s via a malicious email attachment purporting to be
an invoice, energy bill, or image. The delivery often forms part of a service actually provided by
different criminals from those executing the crypto-ransomware. This is just one of the darker sides
of the underground economy, where criminals offer services such as “I can infect X computers for a
fixed price of Y.”

111  http://www.symantec.com/connect/blogs/windows-

8-not-immune-ransomware-0

112  http://www.symantec.com/connect/blogs/

australians-increasingly-hit-global-tide-cryptomalware

113  http://www.symantec.com/security_response/

writeup.jsp?docid=2013-091122-3112-99

114 http://www.symantec.com/security_response/

writeup.jsp?docid=2014-032622-1552-99

115  http://www.symantec.com/security_response/

writeup.jsp?docid=2014-061923-2824-99

2015 Internet Security Threat Report  Ransomware TotalMOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

94

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

116  Tor is a combination of software and an open network

that protects users against traffic analysis and helps to

preserve their anonymity and privacy online. While not

inherently criminal, it also helps to protect the anonymity

of criminals in this case.

 In 2013, crypto-ransomware
accounted for approximately
0.2 percent of all ransomware
attacks. By the end of 2014 this
figure grew to 4 percent.118

117  http://www.symantec.com/connect/blogs/

cryptodefense-cryptolocker-imitator-makes-over-34000-

one-month

118  http://www.symantec.com/connect/blogs/

international-takedown-wounds-gameover-zeus-

cybercrime-network

CryptoDefense, brought to light back in March, is a perfect example of just how serious cryp-
to-ransomware is and how hard the criminals behind it are to track. It’s delivered via malicious
email attachments and encrypts a victim’s files with public-key cryptography using strong RSA
2048 encryption.

In order to pay the ransom, the victim has to visit a webpage on the Tor network.116 The payment
is then requested in bitcoins. These are typical moves of a crypto-ransomware criminal, making
it incredibly difficult to track and shut down such scams.

And then we get to the crux of the entire scam: the profit. Symantec
estimated that the cybercriminals behind CryptoDefense earned over
$34,000 in just one month.117 It’s no wonder crypto-ransomware is considered
to be the most effective cybercrime operation out there at the moment.

SHARE
THIS

80

70

60

50

40

30

20

10

S
D
N
A
S
U
O
H
T

0.2% Overall for 2013

J
2013

JMAMF

J

A

DNOS

J
2014

JMAMF

J

A

DNOS

46A

Crypto-Ransomware, 2013–2014
Source: Symantec

2015 Internet Security Threat Report  0Crypto-RansomwareMOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

95

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Digital Extortion: A Short History of Ransomware

By Peter Coogan

In 2014, crypto-ransomware was rarely out of the news. The
latest and deadliest trend in the ongoing ransomware saga,
crypto-ransomware differs from its standard ransomware
siblings, which simply lock the device, in that it encrypts
data files on the compromised device and, in most cases,
leaves victims with no way to rescue their data. Both
crypto-ransomware and ransomware, however, are in the
business of extorting ransom from victims for the removal
of the infection.

These types of malware have been around for over a decade
but have grown in prevalence over the past few years. This
growth is the result of cybercriminals’ shifting from the
creation of fake antivirus software to the more lucrative
ransomware. While we can trace an evolution from fake
antivirus, to ransomware, and then on to crypto-ransom-
ware, malware authors rarely rest on their laurels. We can
clearly see new areas of the threat landscape where these
digital extortionists are heading.

Fake antivirus (a.k.a. FakeAV or rogue security software)
is a misleading application that fraudulently deceives or
misleads a user into paying for the removal of malware.
While this software has been around for quite some time
now— its prevalence peaked around 2009, a Symantec
report at that time observed 43 million rogue security
software installation attempts from over 250 distinct
programs, at a cost of $30 to $100 for anyone who
purchased the software.119

Ransomware is malicious software that locks and restricts
access to infected computers. The malicious software then
displays an extortion message using a social engineering
theme that demands a ransom payment to remove the
restriction. In 2012 Symantec reported on the growing
menace of ransomware, with fraudsters charging in the
range of €50 to €100 in Europe or up to $200 in the U.S. for
the removal of restrictions.120

Now, after the emergence and perceived success of the
now-infamous Trojan.Cryptolocker121 in 2013, malware
authors have been turning their attention to writing new
crypto-ransomware-style threats. This has led to a surge in
new crypto-ransomware families seen in 2014 that incor-
porate new innovations, platforms, and evasion tactics

alongside both old and new tricks in an attempt to extort
money from victims.

One of the more prolific new crypto-ransomware threats in
2014 was Trojan.Cryptodefense122 (a.k.a. Cryptowall). This
threat appeared in late February 2014 and was initially
marketed as Cryptodefense. It employed techniques such as
the use of Tor and bitcoins for anonymity, strong RSA-2048
encryption of data, and pressure tactics to scare victims into
payment. With an initial ransom demand of $500/€500,
it soon increased to $1,000/€1,000 if payment was not
forthcoming. However, following analysis, it was found that
the malware author’s poor implementation of the cryp-
tographic functionality had left hostages with the key to
their own escape, in the form of the private encryption key
being left on the system. After this information was made
public, the issue was fixed by the malware authors and it
was rebranded as Cryptowall. Since then, Cryptowall has
continued to evolve by weaponizing itself further, with an
elevation of privilege exploit, anti-analysis checks, and the
use of Invisible Internet Project (I2P) for communication
anonymization. The known earnings of Cryptowall were at
least $34,000 in its first month, 123 with researchers deter-
mining that it made in excess of $1 million over a six-month
period.124

The Windows PC landscape has been a lucrative area for
ransomware authors, and this will likely continue to be the
case. However, in 2014 the attackers behind these digital
extortion tools began to tackle new platforms. We saw
the Reveton gang release Android ransomware known as
Android.Lockdroid.G125 (a.k.a. Koler). Through their use
of a Traffic Distribution System (TDS), the Reveton gang
performed a three-pronged ransomware attack. Depending
on certain conditions, such as the browser being used to
view a website controlled by the gang, traffic would be redi-
rected to a fitting ransomware.

Ransomware had suddenly become platform independent.
Android users would be redirected to download Android.
Lockdroid.G. Internet Explorer users were redirected to the
Angler Exploit kit, delivering a payload of Trojan.Ransom-
lock.G.126 and other browsers used on Windows, Linux,
or Mac to Browlock,127 another form of ransomware that

119  http://eval.symantec.com/mktginfo/enterprise/

white_papers/b-symc_report_on_rogue_security_software_

exec_summary_20326021.en-us.pdf

120  http://www.symantec.com/content/en/us/enterprise/

media/security_response/whitepapers/ransomware-a-

growing-menace.pdf

121  http://www.symantec.com/security_response/

writeup.jsp?docid=2013-091122-3112-99

122  http://www.symantec.com/security_response/

writeup.jsp?docid=2014-032622-1552-99

123  http://www.symantec.com/connect/blogs/

cryptodefense-cryptolocker-imitator-makes-over-34000-

one-month

124  http://www.secureworks.com/cyber-threat-

intelligence/threats/cryptowall-ransomware/

125  http://www.symantec.com/security_response/

writeup.jsp?docid=2014-050610-2450-99

126  http://www.symantec.com/security_response/

writeup.jsp?docid=2011-051715-1513-99

127  http://www.symantec.com/connect/blogs/

massive-malvertising-campaign-leads-browser-locking-

ransomware

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

96

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

attempts to lock the computer and extort money from users
by simply using tools in their web browser.

In June 2014, the first file-encrypting ransomware for
Android, known as Android.Simplocker,128 was discovered.
With a demand initially in Russian, by July 2014 an updated
English version (Android.Simplocker.B129) was being seen
that employed an FBI social engineering theme. October
2014 saw the emergence of Android.Lockdroid.E130 (a.k.a.
Porndroid), which once again used a fake FBI social engi-
neering theme. This threat, however, also used the device’s
camera to take a picture, which would then be displayed
alongside the ransom demand. Android.Lockdroid further
spawned new variants that included worm-like capabilities,
allowing self-replication via SMS messages sent to contacts
in the address book on an infected device, along with a
social engineering catch.

Ransomware authors even began looking past mobile
devices to see where else they could possibly extort money,
and they realized that network-attached storage (NAS)
devices, where large quantities of files are stored, could also
be targeted. Trojan.Synolocker131 (a.k.a. Synolocker) targeted
Synology NAS devices by using a previously unknown

vulnerability in Synology’s DiskStation manager software
to gain access to the devices and then encrypt all the files,
holding them for ransom. These devices have since been
patched against further attacks, but this case highlights
that ransomware attackers are continuing to look for new
areas to attack.

So why are we seeing such rapid
changes in ransomware? Ransomware
is a lucrative business for cybercriminals, with ransom
demands ranging anywhere from $100 to $500. During 2014
we also saw bitcoins become the ransom payment method
of choice by most new ransomware. Given bitcoin’s strong
anonymity, it allows cybercriminals to easily hide and
launder their ill-gotten gains.

SHARE
THIS

While we have observed a surge in new ransomware
families, Symantec has also seen an increase in the overall
growth path. Since 2013, there has been a 113 percent rise
in the occurrence of ransomware attacks. However, given
the lucrative nature of these threats and the number of new
ransomware families appearing, it is unlikely that ransom-
ware-type scams will drop off the threat landscape anytime
soon, with future growth being more likely.

 “Porndroid” Android
ransomware threat.

128  http://www.symantec.com/security_response/

writeup.jsp?docid=2014-060610-5533-99

129  http://www.symantec.com/security_response/

writeup.jsp?docid=2014-072317-1950-99

130  http://www.symantec.com/security_response/

writeup.jsp?docid=2014-103005-2209-99

131  http://www.symantec.com/security_response/

writeup.jsp?docid=2014-080708-1950-99

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

97

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Bots and Botnets

The number of bots declined by 18 percent in 2014 compared to the previous year. In large
measure, this is because the FBI, the European Cybercrime Centre (EC3) at Europol, and other
international law enforcement agencies, working with Symantec and other tech firms, have been
active in disrupting and shutting them down. Most notably, the Gameover Zeus botnet was
shut down in 2014. It was responsible for millions of infections worldwide since its arrival in
2011.132,133 This is one in a series of botnet takedowns over the past couple of years134,135 that have
seen IT firms and law enforcement working together effectively.

2014

2013

2012

14

Number of Bots
Source: Symantec

1.9 Million
-18%

2.3 Million
-33%

3.4 Million

132  http://www.symantec.com/connect/blogs/

international-takedown-wounds-gameover-zeus-

cybercrime-network

133  http://krebsonsecurity.com/2014/06/operation-

tovar-targets-gameover-zeus-botnet-cryptolocker-

scourge/

 The decline in bots in 2014 was,
in part, fueled by the disruption
of the Gameover Zeus botnet
with “Operation Tovar.” This
botnet had largely been used for
banking fraud and distribution of
the CryptoLocker ransomware.

134  http://www.computerweekly.com/

news/2240185424/Microsoft-partnership-takes-down-

1000-cybercrime-botnets

135  http://www.computerweekly.com/

news/2240215443/RSA-2014-Microsoft-and-partners-

defend-botnet-disruption

 The United States and China, two
of the most populated countries
with the greatest concentration
of Internet-connected users,
swapped the number one and
two places in 2014. This switch
can likely be attributed to the
takedown of the Gameover Zeus
botnet.

Country/Region

2014 Bots Rank

2014 Bots
Percentage

2013 Bots
Rank

2013 Bots
Percentage

China

United States

Taiwan

Italy

Hungary

Brazil

Japan

Germany

Canada

Poland

1

2

3

4

5

6

7

8

9

10

16.5%

16.1%

8.5%

5.5%

4.9%

4.3%

3.4%

3.1%

3.0%

2.8%

2

1

4

3

7

5

6

8

10

12

9.1%

20.0%

6.0%

6.0%

4.2%

5.7%

4.3%

4.2%

3.5%

3.0%

44

Malicious Activity by Source: Bots, 2013–2014
Source: Symantec

2015 Internet Security Threat Report  Number of BotsMalicious Activity by Source: BotsMOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

98

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Spam Botnet
Name

Percentage
of Botnet
Spam

Estimated
Spam
per Day

Top Sources of Spam From Botnet

                    Rank #1

          Rank #2

    Rank #3

KELIHOS

51.6%

884,044

Spain   10.5%

United States

7.6%

Argentina   7.3%

UNKNOWN/
OTHER

25.3%

432,594

United States   13.5%

Brazil

7.8%

Spain   6.4%

GAMUT

7.8%

133,573

Russia   30.1%

Vietnam   10.1%

Ukraine   8.8%

CUTWAIL

3.7%

63,015

Russia   18.0%

India

8.0%

Vietnam   6.2%

DARKMAILER5

1.7%

28,705

Russia   25.0%

Ukraine   10.3%

Kazakhstan   5.0%

DARKMAILER

0.6%

9,596

Russia   17.6%

Ukraine   15.0%

China   8.7%

SNOWSHOE

0.6%

9,432

Canada   99.9%

United States   0.02%

Japan   0.01%

ASPROX

0.2%

3,581

United States   76.0%

Canada

3.4%

United Kingdom   3.3%

DARKMAILER3

0.1%

1,349

United States   12.7%

Poland

9.6%

South Korea    9.1%

GRUM

0.03%

464

Canada   45.7%

Turkey   11.5%

Germany   8.5%

45

Top 10 Spam-Sending Botnets, 2014
Source: Symantec

OSX as a Target

Over the past few years Apple has sat up and taken notice of the threats that have been targeting
OS X, rolling out a couple of much-needed security features to the operating system. XProtect
scans downloaded files for signs of malware, warning users if they download a malicious file
known to Apple. Using code signing Gatekeeper limits what apps can be run within an OS X
computer. There are varying degrees of protection with Gatekeeper, ranging from limiting instal-
lation to apps from the official Mac App Store, developers identified as trustworthy by Apple, or
any developer that signs their apps.

However, while these security features have made it more difficult for threats to gain a foothold
in OS X, threats have nevertheless succeeded in getting past them. As with any signature-based
security solution, apps have managed to compromise computers before signatures could be put
in place to block them. Malicious apps have also appeared with legitimate developer signatures,
by either stealing legitimate credentials or creating false ones.

The most common threats seen in 2014 had similar behaviors to those found on other operating
systems. There were Trojans that arrived via browser exploits. Notorious threats such as
Flashback, which infected over 600,000 Macs in 2012, are still fairly prevalent, with variants
taking up the number three and 10 spots in 2014. Threats that modify settings, such as DNS,
browser, or search settings on the OS X computer, also rank highly.

2015 Internet Security Threat Report  Top 10 Spam-Sending Botnets MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

99

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Two notable threats highlighted a significant issue in the OS X threat landscape:
pirated OS X apps that contain malware.

OSX.Wirelurker is a dual-threat Trojan horse, impacting both Macs running OS X and any iOS devices
connected to a compromised computer. This threat gained major attention when it was discovered
within 467 OS X applications hosted on a third-party OS X app store in China. These malicious apps
were downloaded more than 356,000 times before Apple stepped in and blocked them to prevent them
from running.

Rank

Malware Name

Percentage of
Mac Threats 2014

Malware
Name

Percentage of Mac
Threats 2013

 Two notable threats highlighted
a significant issue in the OS X
threat landscape: pirated OS X
apps that contain malware.

1

2

3

4

5

6

7

8

9

OSX.RSPlug.A

OSX.Okaz

OSX.Flashback.K

OSX.Keylogger

OSX.Stealbit.B

OSX.Klog.A

OSX.Crisis

OSX.Sabpab

OSX.Netweird

10

OSX.Flashback

21.2%

12.1%

8.6%

7.7%

6.0%

4.4%

4.3%

3.2%

3.1%

3.0%

OSX.RSPlug.A

35.2%

OSX.Flashback.K

10.1%

OSX.Flashback

OSX.HellRTS

OSX.Crisis

OSX.Keylogger

OSX.MacControl

OSX.FakeCodec

OSX.Iservice.B

OSX.Inqtana.A

9.0%

5.9%

3.3%

3.0%

2.9%

2.3%

2.2%

2.1%

58

Top 10 Mac OS X Malware Blocked on OS X Endpoints, 2013–2014
Source: Symantec

 Third-party app store, Maiyadi,
which was found to be hosting
apps with OS X malware in 2014.

2015 Internet Security Threat Report  Top 10 Mac OSX Malware Blocked on OSX Endpoints MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

100

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

OSX.Luaddit (a.k.a. iWorm) is a threat that added compromised computers to an OS X botnet.
This threat was found bundled with pirated copies of commercial products like Adobe Photoshop,
Microsoft Office, and Parallels.136 These apps were posted to torrent sites and were downloaded
thousands of times.

136  http://www.thesafemac.com/iworm-method-of-

infection-found/

137  http://www.symantec.com/connect/blogs/does-

malware-still-detect-virtual-machines

139  http://www.symantec.com/content/en/us/enterprise/

media/security_response/whitepapers/threats_to_virtual_

environments.pdf

Virtualization
is no protection
against malware.
Increasingly,
malware can detect
whether it is running
on a virtual machine
and, instead of
quitting, it can
change its behavior
to reduce the risk of
detection.

138  Ibid

140  Ibid

 Examples of OS X torrents that contain malware.

In terms of other notable OS X threats, OSX.Stealbit.A and OSX.Stealbit.B are bitcoin-stealing
threats that monitor browsing traffic, looking for login credentials to major bitcoin websites.
The latter was one of the top five OS X threats seen in 2014.

OSX.Slordu is a back door Trojan horse that appears to be used for gathering information about
the compromised computer. What is interesting about this threat is it appears to be an OS X port
of a popular Windows back door.

OSX.Ventir is a modular threat, equipped with option components that can open a back door, log
keystrokes, or contain spyware capabilities. Depending on what the attacker wishes to gain from
the compromised computer, different modules could be downloaded and installed in OS X.

OSX.Stealbit.A is a bitcoin-stealing threat that monitors browsing traffic, looking for login
credentials to major bitcoin websites.

Malware on Virtualized Systems

Virtualization is no protection against malware. Increasingly, malware
can detect whether it is running on a virtual machine and, instead of
quitting, it can change its behavior to reduce the risk of detection.137 Historically the proportion
of malware that detected whether or not it was running on VMware hovered around 18 percent
but spiked at the beginning of 2014 to 28 percent.138

SHARE
THIS

But this type of functionality is not being used just to avoid security researchers. Once installed
on a virtual machine, malware can hop to other virtual machines on the same hardware or infect
the hypervisor, massively increasing the risk and the difficulty of removal.139 This behavior has
already been seen in the wild: the W32.Crisis malware tries to infect virtual machine images
stored on a host computer.140

For IT managers, this kind of attack poses special risks. It is unlikely to be detected by perimeter
security, such as intrusion detection systems or firewalls that use virtual machines for detecting
threats in virtual “sandboxes.” Virtual machines may not have the same level of protection
as traditional clients or servers because of the (false) assumption that malware doesn’t attack
virtual machines. Organizations need to consider technology such as network hardware, hypervi-
sors, and software-defined networks in their security plans and patch cycles.

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

101

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

A
P
P
E
N
D
I
X

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

102

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Looking Ahead

Threat Intelligence and Unified Security

Today’s attackers are skilled enough and sufficiently resourced to have the persistence and patience
to carry out their espionage activities over a period of months or even years. They have only to be
successful once in order to breach their targets’ defenses; however, those targets must be able to
resist each and every one of those assaults, every second of every day. Threat intelligence is a vital
component in understanding these potential threats, uncovering new attacks, and better protecting
critical company assets. Threat intelligence can provide a prioritized list of suspicious incidents by
correlating all available information from across the enterprise.

Advanced attackers use exploit toolkits against not only older vulnerabilities but also new, zero-day
ones, and being good at defense means being harder to breach. The battle is an asymmetric one, and
attackers already understand the defenses and their weaknesses. A unified security model is not just
about investing in great technology. It also takes a holistic approach that combines threat intelligence,
risk management, and the very best technical solutions. A unified approach will not only help reveal
who is being targeted but also how and why. Understanding the new threats is critical, and businesses
should now expect to be attacked—the question is not “if” but “when” and “how.”

Unified security can leverage the combined visibility and threat intelligence gathered across the
enterprise to block, detect, and remediate attacks. It can help guide how to better protect confidential
information and reduce risk, supporting the continual assessment of not only people and their skills
but also processes and technology to ensure the best response is followed. Processes are continually
updated and skills maintained. Ultimately, by becoming harder to breach, attackers must work harder;
no one wants to be the weakest link in the supply chain. This, we believe, is the future of security.

Security Gamification

As the 15th-century security consultant Niccolo Machiavelli observed, “Men are so simple and yield so
readily to the desires of the moment that he who will trick will always find another who will suffer to
be tricked.”

Internet security relies on the human element as much as it does on technology. If people were more
skillful, they could help reduce the risks they faced. This is as true of consumers’ avoiding scams as it
is of government employees’ avoiding the social engineering in targeted attacks.

In this context, gamification can be used to turn “the desires of the moment” into lasting changes
of behavior by using the psychological rewards and instant gratification of simple computer games.
Gamification could be used, for example, to train people to be wary of phishing emails or to generate,
remember, and use strong passwords.

Symantec sees a big market opportunity and a great need for this kind of training in the coming years.

Security Simulation

Companies can prepare for security breaches and understand their defenses better using simulations
and security “war games.” By extending conventional penetration testing into a simulated response and
remediation phase, companies can train their people and improve their readiness. This message is not
lost on governments. In January 2015, UK Prime Minister David Cameron and U.S. President Barack
Obama agreed to carry out “war game” cyberattacks on each other. Companies should follow their
example in 2015.

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

103

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Determined Attackers Will Likely Succeed

In the battle between attackers and corporate IT security, the bad guys have to be lucky only
once. The IT department has to be lucky all the time. With this in mind, IT managers (and indeed
consumers) need to plan for the worst. There is no magic-bullet technology that will guarantee
immunity from Internet crime or determined, targeted attacks. So assume you’ve been hacked
or you’re about to be hacked. Switch from a binary “safe”/“not safe” view to a nuanced, almost
medical approach to trends, symptoms, behavioral prevention, diagnostics, and treatment.

On a technical level, it means ensuring you have effective data loss prevention software on each
endpoint, gateway, and email server to prevent data exfiltration. It also means that backup and
disaster recovery become much more important, as do detection and response planning. This is
not a counsel of despair—we should never make it easy for attackers by giving up on prevention—
but it is better to be wise before the event than sad after it.

Data Sharing Between Companies Is Essential

Data sharing between companies is essential to security. Historically, companies have been
afraid to share too much information with other companies, so they’ve effectively fought individ-
ual battles against the bad guys and depended on their own internal resources. We believe they
need to pool their threat intelligence and their experience to combat the criminals. Tools that
allow them to do this while retaining some IP protection will become increasingly important. For
example, security electronic data exchanges could share hashes, binary attributes, symptoms,
and so on, without revealing corporate secrets or information that could be useful in an attack.

Insecure Operating Systems

A quarter of PC users were running Windows XP and Office 2003 in July 2014141 even as their
software went out of support and Microsoft stopped updating it. A lot of people are still in denial
about this change. This leaves them unpatched as new threats emerge. Over the next year,
this presents a significant security risk. For embedded devices running out-of-date operating
systems, companies will need to find new ways of protecting them until they can be replaced or
upgraded.

Internet of Things

As consumers buy more smart watches, activity trackers, holographic headsets, and whatever
new wearable devices are dreamed up in Silicon Valley and Shenzhen, the need for improved
security on these devices will become more pressing. It’s a fast-moving environment where inno-
vation trumps privacy. Short of government regulation, a media-friendly scare story, or greater
consumer awareness of the dangers, it is unlikely that security and privacy will get the attention
they deserve. The market for Internet of Things–ready devices is growing but is still very frag-
mented, with a rich diversity in low-cost hardware platforms and operating systems. As market
leaders emerge and certain ecosystems grow, the attacks against these devices will undoubtedly
escalate, as has already happened with attacks against the Android platform in the mobile arena
in recent years.

141  http://www.informationweek.com/software/

operating-systems/windows-xp-stayin-alive/d/d-

id/1279065

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

104

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Best Practice Guidelines for Businesses

Employ defense-in-depth strategies

Emphasize multiple, overlapping, and mutually supportive
defensive systems to guard against single-point failures in any
specific technology or protection method. This should include
the deployment of regularly updated firewalls as well as gateway
antivirus, intrusion detection or protection systems (IPS),
website vulnerability with malware protection, and web security
gateway solutions throughout the network.

Monitor for network incursion attempts,
vulnerabilities, and brand abuse

Receive alerts for new vulnerabilities and threats across vendor
platforms for proactive remediation. Track brand abuse via
domain alerting and fictitious website reporting.

Antivirus on endpoints is not enough

On endpoints, it is important to have the latest versions of
antivirus software installed. Deploy and use a comprehensive
endpoint security product that includes additional layers of
protection including:

 Endpoint intrusion prevention that protects unpatched

vulnerabilities from being exploited, protects against social
engineering attacks, and stops malware from reaching
endpoints;

 Browser protection for avoiding obfuscated web-based

attacks;

 File and web-based reputation solutions that provide a

risk-and-reputation rating of any application and website to
prevent rapidly mutating and polymorphic malware;

 Behavioral prevention capabilities that look at the behavior

of applications and prevent malware;

 Application control settings that can prevent applications
and browser plug-ins from downloading unauthorized
malicious content;

 Device control settings that prevent and limit the types of

USB devices to be used.

Secure your websites against MITM
attacks and malware infection

Avoid compromising your trusted relationship with your
customers by:

 Implementing Always On SSL (SSL protection on your

website from logon to logoff);

 Scanning your website daily for malware;

 Setting the secure flag for all session cookies;

 Regularly assessing your website for any vulnerabilities (in

2013 1 in 8 websites scanned by Symantec was found to have
vulnerabilities);

 Choosing SSL Certificates with Extended Validation to
display the green browser address bar to website users;

 Displaying recognized trust marks in highly visible locations
on your website to show customers your commitment to
their security.

Protect your private keys

Make sure to get your digital certificates from an established,
trustworthy certificate authority that demonstrates excellent
security practices. Symantec recommends that organizations:

 Use separate Test Signing and Release Signing infrastruc-

tures;

 Secure keys in secure, tamper-proof, cryptographic hardware

devices;

 Implement physical security to protect your assets from

theft.

Use encryption to protect sensitive data

Implement and enforce a security policy whereby any sensitive
data is encrypted. Access to sensitive information should be
restricted. This should include a Data Loss Protection (DLP)
solution. Ensure that customer data is encrypted as well. This
not only serves to prevent data breaches, but can also help
mitigate the damage of potential data leaks from within an
organization. Use Data Loss Prevention to help prevent data
breaches: Implement a DLP solution that can discover where
sensitive data resides, monitor its use, and protect it from loss.
Data loss prevention should be implemented to monitor the flow
of information as it leaves the organization over the network,
and monitor traffic to external devices or websites.

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

105

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Best Practice Guidelines for Businesses

 DLP should be configured to identify and block suspicious

Ensure regular backups are available

copying or downloading of sensitive data;

 DLP should also be used to identify confidential or sensitive

data assets on network file systems and computers.

Ensure all devices allowed on company
networks have adequate security protections

If a bring your own device (BYOD) policy is in place, ensure a
minimal security profile is established for any devices that are
allowed access to the network.

Implement a removable media policy

Where practical, restrict unauthorized devices such as external
portable hard-drives and other removable media. Such devices
can both introduce malware and facilitate intellectual property
breaches, whether intentional or unintentional. If external
media devices are permitted, automatically scan them for
viruses upon connection to the network and use a DLP solution
to monitor and restrict copying confidential data to unencrypted
external storage devices.

Be aggressive in your updating and patching

Update, patch, and migrate from outdated and insecure
browsers, applications, and browser plug-ins. This also applies
to operating systems, not just across computers, but mobile,
ICS, and IoT devices as well. Keep virus and intrusion preven-
tion definitions at the latest available versions using vendors’
automatic update mechanisms. Most software vendors work dili-
gently to patch exploited software vulnerabilities; however, such
patches can only be effective if adopted in the field. Wherever
possible, automate patch deployments to maintain protection
against vulnerabilities across the organization.

Enforce an effective password policy

Ensure passwords are strong; at least 8-10 characters long and
include a mixture of letters and numbers. Encourage users
to avoid re-using the same passwords on multiple websites
and sharing of passwords with others should be forbidden.
Passwords should be changed regularly, at least every 90 days.

Create and maintain regular backups of critical systems, as
well as endpoints. In the event of a security or data emergency,
backups should be easily accessible to minimize downtime of
services and employee productivity.

Restrict email attachments

Configure mail servers to block or remove email that contains
file attachments that are commonly used to spread viruses,
such as .VBS, .BAT, .EXE, .PIF, and .SCR files. Enterprises should
investigate policies for .PDFs that are allowed to be included
as email attachments. Ensure that mail servers are adequately
protected by security software and that email is thoroughly
scanned.

Ensure that you have infection and incident response
procedures in place

 Keep your security vendor contact information handy, know
who you will call, and what steps you will take if you have
one or more infected systems;

 Ensure that a backup-and-restore solution is in place in order
to restore lost or compromised data in the event of successful
attack or catastrophic data loss;

 Make use of post-infection detection capabilities from web

gateway, endpoint security solutions and firewalls to identify
infected systems;

 Isolate infected computers to prevent the risk of further

infection within the organization, and restore using trusted
backup media;

 If network services are exploited by malicious code or some
other threat, disable or block access to those services until a
patch is applied.

Educate users on basic security protocols

 Do not open attachments unless they are expected and

come from a known and trusted source, and do not execute
software that is downloaded from the Internet (if such
actions are permitted) unless the download has been scanned
for viruses;

 Be cautious when clicking on URLs in emails or social media
programs, even when coming from trusted sources and
friends;

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

106

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

 Deploy web browser URL reputation plug-in solutions that

display the reputation of websites from searches;

 Only download software (if allowed) from corporate shares or

directly from the vendor website;

 If Windows users see a warning indicating that they are

“infected” after clicking on a URL or using a search engine
(fake antivirus infections), educate users to close or quit the
browser using Alt-F4, CTRL+W or the task manager.

Building Security into devices

 The diverse nature of ICS and IoT platforms make host-

based IDS and IPS, with customizable rulesets and policies
that are unique to a platform and application, suitable
solutions. However, manufacturers of ICS and IoT devices
are largely responsible for ensuring that security is built into
the devices before shipping. Building security directly into
the software and applications that run on the ICS and IoT
devices would prevent many attacks that manage to side-step
defenses at the upper layers. Manufacturers should adopt
and integrate such principles into their software develop-
ment process.

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

107

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

20 Critical Security Controls

Overview

The Council on Cybersecurity 20 Critical Security Controls is a
prioritized list designed to provide maximum benefits toward
improving risk posture against real-world threats. This list of
20 control areas grew out of an international consortium of U.S.
and international agencies and experts, sharing from actual
incidents and helping to keep it current against evolving global
cybersecurity threats.

Many organizations face the challenges and increasing threats
to their cybersecurity by strategically choosing a security
controls framework as a reference for initiating, implementing,
measuring and evaluating their security posture, and managing
risk. Over the years, many security control frameworks have
been developed (e.g. NIST), with the common goal of offering
combined knowledge and proven guidance for protecting critical

assets, infrastructure and information. Based on the informa-
tion we have today about attacks and threats, what are the most
important steps that enterprises should take now, to secure
systems and data?

The Critical Security Controls are designed to provide organi-
zations the information necessary to increase their security
posture in a consistent and ongoing fashion. The Controls
are a relatively small number of prioritized, well-vetted, and
supported set of security actions that organizations can take to
assess and improve their current security state.

To implement the Controls you must understand what is critical
to your business, data, systems, networks, and infrastructures,
and you must consider the adversary actions that could impact
your ability to be successful in the business or operations.

Top 5 Priorities

We emphasize the use of the first five
Controls for every organization. This
helps establish a foundation of security
and has the most immediate impact on
preventing attacks. From this foun-
dation organizations can apply other
Controls as they meet the business need
of the organization.

In the following pages you will see a
table that outlines the areas identified
in the ISTR and ties them to Critical
Security Controls:

01
Inventory of Authorized and
Unauthorized Devices
Reduce the ability of attackers to find and
exploit unauthorized and unprotected
systems: Use active monitoring and
configuration management to maintain
an up-to-date inventory of devices
connected to the enterprise network,
including servers, workstations,
laptops, and remote devices.

02
Inventory of Authorized and
Unauthorized Software
Identify vulnerable or malicious software
to mitigate or root out attacks: Devise
a list of authorized software for each
type of system, and deploy tools to
track software installed (including type,
version, and patches) and monitor for
unauthorized or unnecessary software.

04
Continuous Vulnerability
Assessment and Remediation
Proactively identify and repair software
vulnerabilities reported by security
researchers or vendors: Regularly run
automated vulnerability scanning
tools against all systems and quickly
remediate any vulnerabilities, with
critical problems fixed within 48 hours.

03
Secure Configurations for
Hardware & Software on Laptops,
Workstations, and Servers
Prevent attackers from exploiting
services and settings that allow
easy access through networks and
browsers: Build a secure image that
is used for all new systems deployed
to the enterprise, host these standard
images on secure storage servers,
regularly validate and update these
configurations, and track system images
in a configuration management system.

05
Malware Defense
Block malicious code from tampering
with system settings or content, capturing
sensitive data, or from spreading:
Use automated antivirus and anti-
spyware software to continuously monitor
and protect workstations, servers,
and mobile devices. Automatically
update such anti-malware tools on
all machines on a daily basis.

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

108

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Critical Control Protection Priorities

INTERNET OF THINGS

HARDEN
DEFENSES

ENHANCE
DETECTION

REDUCE
IMPACT

04 05 06 07

01

09 10 11 14

12 13 17 19

18

MOBILE THREATS

02

03 04 05 06

01 10

08 17

07

PROTECT WEB SERVERS

02

03

04 05 06

01 14 16 18 20

08 12 17 13

10

11

WEB-BASED ATTACKS

02 03 04 05 06

01 14 16

12 13 15 17

SPAM & PHISHING

TARGETED ATTACKS

02 05

01 09 20

12 13

02

03 04 05 06

01 14 16 18 20

12 13 15 17

11

DATA BREACHES

02

03

04

05 06

01

14 16 09 18

08

12 17 13 15

10

11

07

20

19

MALWARE THREATS

BOTS

02 03 04 05

01

14 16 09 18

08 12 17 13

20

02 03 04 05

01 14 18

17 13 19

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

109

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Critical Controls

01
Inventory of Authorized and
Unauthorized Devices
Reduce the ability of attackers to find and
exploit unauthorized and unprotected
systems: Use active monitoring and
configuration management to maintain
an up-to-date inventory of devices
connected to the enterprise network,
including servers, workstations,
laptops, and remote devices.

02
Inventory of Authorized and
Unauthorized Software
Identify vulnerable or malicious software
to mitigate or root out attacks: Devise
a list of authorized software for each
type of system, and deploy tools to
track software installed (including type,
version, and patches) and monitor for
unauthorized or unnecessary software.

03
Secure Configurations for
Hardware & Software on Laptops,
Workstations, and Servers
Prevent attackers from exploiting
services and settings that allow
easy access through networks and
browsers: Build a secure image that
is used for all new systems deployed
to the enterprise, host these standard
images on secure storage servers,
regularly validate and update these
configurations, and track system images
in a configuration management system.

04
Continuous Vulnerability
Assessment and Remediation
Proactively identify and repair software
vulnerabilities reported by security
researchers or vendors: Regularly run
automated vulnerability scanning
tools against all systems and quickly
remediate any vulnerabilities, with
critical problems fixed within 48 hours.

05
Malware Defense
Block malicious code from tampering
with system settings or content, capturing
sensitive data, or from spreading:
Use automated antivirus and anti-
spyware software to continuously monitor
and protect workstations, servers,
and mobile devices. Automatically
update such anti-malware tools on
all machines on a daily basis.
Prevent network devices from using auto-
run programs to access removable media.

06

Application Software Security
Neutralize vulnerabilities in web-
based and other application software:
Carefully test internally-developed and
third-party application software for
security flaws, including coding errors
and malware. Deploy web application
firewalls that inspect all traffic, and
explicitly check for errors in all user
input (including by size and data type).

07

Wireless Device Control
Protect the security perimeter
against unauthorized wireless access:
Allow wireless devices to connect to
the network only if they match an
authorized configuration and security
profile and have a documented
owner and defined business need.
Ensure that all wireless access points
are manageable using enterprise
management tools. Configure scanning
tools to detect wireless access points.

08

Data Recovery Capability
Minimize the damage from an attack:
Implement a trustworthy plan for
removing all traces of an attack.
Automatically back up all information
required to fully restore each system,
including the operating system,
application software, and data. Back
up all systems at least weekly; back up
sensitive systems more frequently.
Regularly test the restoration process.

09

Security Skills Assessment
and Appropriate Training
to Fill Gaps
Find knowledge gaps, and eradicate
them with exercises and training:
Develop a security skills assessment
program, map training against the
skills required for each job, and use the
results to allocate resources effectively
to improve security practices.

10

Secure Configurations for
Network Devices such as
Firewalls, Routers, and Switches
Preclude electronic holes from forming
at connection points with the Internet,
other organizations, and internal
network segments: Compare firewall,
router, and switch configurations against
standards for each type of network
device. Ensure that any deviations
from the standard configurations are
documented and approved and that
any temporary deviations are undone
when the business need abates.

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

110

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Critical Controls

11

14

17

Limitation and Control of
Network Ports, Protocols, and
Services
Allow remote access only to legitimate
users and services: Apply host-based
firewalls, port-filtering, and scanning
tools to block traffic that is not explicitly
allowed. Properly configure web servers,
mail servers, file and print services,
and domain name system (DNS)
servers to limit remote access. Disable
automatic installation of unnecessary
software components. Move servers
inside the firewall unless remote access
is required for business purposes.

12

Controlled Use of
Administrative Privileges
Protect and validate administrative
accounts on desktops, laptops, and servers
to prevent two common types of attack: (1)
enticing users to open a malicious email,
attachment, or file, or to visit a malicious
website; and (2) cracking an administrative
password and thereby gaining access to
a target machine. Use robust passwords
that follow Federal Desktop Core
Configuration (FDCC) standards.

13

Boundary Defense
Control the flow of traffic through
network borders, and police content
by looking for attacks and evidence of
compromised machines: Establish a
multi-layered boundary defense by relying
on firewalls, proxies, demilitarized zone
(DMZ) perimeter networks, and other
network-based tools. Filter inbound and
outbound traffic, including through
business partner networks (“extranets”).

Maintenance, Monitoring, and
Analysis of Security Audit Logs
Use detailed logs to identify and uncover
the details of an attack, including the
location, malicious software deployed,
and activity on victim machines: Generate
standardized logs for each hardware
device and the software installed on
it, including date, time stamp, source
addresses, destination addresses, and
other information about each packet and/
or transaction. Store logs on dedicated
servers, and run bi-weekly reports to
identify and document anomalies.

15

Controlled Access Based
on the Need to Know
Prevent attackers from gaining access
to highly sensitive data: Carefully
identify and separate critical data from
information that is readily available
to internal network users. Establish a
multilevel data classification scheme
based on the impact of any data exposure,
and ensure that only authenticated users
have access to nonpublic data and files.

16

Account Monitoring and Control
Keep attackers from impersonating
legitimate users: Review all system
accounts and disable any that are not
associated with a business process and
owner. Immediately revoke system access
for terminated employees or contractors.
Disable dormant accounts and encrypt
and isolate any files associated with
such accounts. Use robust passwords
that conform to FDCC standards.

Data Loss Prevention
Stop unauthorized transfer of
sensitive data through network
attacks and physical theft: Scrutinize
the movement of data across network
boundaries, both electronically and
physically, to minimize exposure to
attackers. Monitor people, processes,
and systems, using a centralized
management framework.

18

Incident Response
Management
Protect the organization’s reputation,
as well as its information: Develop an
incident response plan with clearly
delineated roles and responsibilities
for quickly discovering an attack
and then effectively containing the
damage, eradicating the attacker’s
presence, and restoring the integrity
of the network and systems.

19

Secure Network Engineering
Keep poor network design from enabling
attackers: Use a robust, secure network
engineering process to prevent security
controls from being circumvented. Deploy
a network architecture with at least three
tiers: DMZ, middleware, private network.
Allow rapid deployment of new access
controls to quickly deflect attacks.

20

Penetration Tests and
Red Team Exercises
Use simulated attacks to improve
organizational readiness: Conduct
regular internal and external penetration
tests that mimic an attack to identify
vulnerabilities and gauge the potential
damage. Use periodic red team exercises—
all-out attempts to gain access to
critical data and systems to test existing
defense and response capabilities.

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

111

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Best Practice Guidelines for Consumers

Protect Yourself

Think Before You Click

Use a modern Internet security solution that includes the
following capabilities for maximum protection against malicious
code and other threats:

 Antivirus (file- and heuristic-based) and behavioral malware
prevention can prevent unknown malicious threats from
executing;

 Bi-directional firewalls will block malware from exploiting

potentially vulnerable applications and services running on
your computer;

 Browser protection to protect against obfuscated web-based

attacks;

 Use reputation-based tools that check the reputation and
trust of a file and website before downloading, and that
check URL reputations and provide safety ratings for
websites found through search engines;

 Consider options for implementing cross-platform parental

controls, such as Norton Online Family.142

Update Regularly

Keep your system, program, and virus definitions up-to-date
– always accept updates requested by the vendor. Running
out-of-date versions can put you at risk from being exploited by
web-based attacks. Only download updates from vendor sites
directly. Select automatic updates wherever possible.

Be Wary of Scareware Tactics

Versions of software that claim to be free, cracked or pirated
can expose you to malware, or social engineering attacks that
attempt to trick you into thinking your computer is infected and
getting you to pay money to have it removed.

Use an Effective Password Policy

Ensure that passwords are a mix of letters and numbers, and
change them often. Passwords should not consist of words from
the dictionary. Do not use the same password for multiple appli-
cations or websites. Use complex passwords (upper/lowercase
and punctuation) or passphrases.

Never view, open, or copy email attachments to your desktop or
execute any email attachment unless you expect it and trust the
sender. Even when receiving email attachments from trusted
users, be suspicious.

 Be cautious when clicking on URLs in emails or social media
communications, even when coming from trusted sources
and friends. Do not blindly click on shortened URLs without
expanding them first using a preview tool or plug-in.

 Use a web browser plug-in or URL reputation site that shows
the reputation and safety rating of websites before visiting.
Be suspicious of search engine results; only click through
to trusted sources when conducting searches, especially on
topics that are hot in the media.

 Be suspicious of warnings that pop up asking you to install

media players, document viewers and security updates. Only
download software directly from the vendor’s website.

 Be aware of files you make available for sharing on public
sites, including gaming, bitTorrent, and any other peer-to-
peer (P2P)exchanges. Keep Dropbox, Evernote, and other
usages to a minimum for pertinent information only.

Guard Your Personal Data

Limit the amount of personal information you make publicly
available on the Internet (in particular via social networks). This
includes personal and financial information, such as bank logins
or birth dates.

 Review your bank, credit card, and credit information

frequently for irregular activity. Avoid banking or shopping
online from public computers (such as libraries, Internet
cafes, and similar establishments) or from unencrypted
Wi-Fi connections.

 Use HTTPS when connecting via Wi-Fi networks to your

email, social media and sharing websites. Check the settings
and preferences of the applications and websites you are
using.

 Look for the green browser address bar, HTTPS, and recog-

nizable trust marks when you visit websites where you log in
or share any personal information.

 Configure your home Wi-Fi network for strong authentica-
tion and always require a unique password for access to it.

142  For more information about Norton Online Family,

please visit https://onlinefamily.norton.com/

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

112

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Best Practice Guidelines for Website Owners

Despite this year’s vulnerabilities, when it comes to protecting
your website visitors and the information they share with you,
SSL and TLS remain the gold standard.

In fact, due to the publicity that Heartbleed received, more
companies than ever have started hiring SSL developers to
work on fixes and code. This has focused more eyes on the SSL
libraries and common good practices in implementation.

Get Stronger SSL

SSL certificate algorithms become stronger than ever in 2014.
Symantec, along with several other CAs, has moved to SHA-2
as default and is winding down support for 1024-bit roots.143
Microsoft and Google announced SHA-1 deprecation plans that
may affect websites with SHA-1 certificates expiring as early as
January 1, 2016.144   In other words, if you haven’t migrated to
SHA-2, visitors using Chrome to access your site will likely see a
security warning and as of January 1, 2017, your certificates just
won’t work for visitors using Internet Explorer.

Symantec is also advancing the use of the ECC algorithm—a
much stronger alternative to RSA. All major browsers, even
mobile, support ECC certificates on all the latest platforms,
and there are three main benefits to using it:

1. Improved Security

Compared to an industry-standard RSA-2048 key, ECC-256 keys
are 10,000 times harder to crack.145  In other words, it would take
a lot more computing power and a lot longer for a brute-force
attack to crack this algorithm.

2. Better Performance

Website owners used to worry that implementing SSL certif-
icates would slow their sites. This led to many sites’ having
only partial-on SSL, which creates serious vulnerabilities. ECC
requires much less processing power on the website than does
RSA and can handle more users and more connections simulta-
neously. This makes the implementation of always-on SSL not
only sensible but viable too.

3. Perfect Forward Secrecy (PFS)

Although PFS is an option with RSA-based and ECC-based
certificates, performance is much better with ECC-based certif-
icates. Why does that matter? Without PFS, if hackers got hold
of your private keys, they could retrospectively decrypt any and
all data they captured. Considering the Heartbleed vulnerability

made this a very real possibility for so many websites, this is a
problem. With PFS, however, if hackers crack or get hold of your
SSL certificate private keys, they can decrypt only information
protected with those keys—not historical data—from that point
on.

Use SSL Correctly. As we realized in 2014, SSL is only as good as
its implementation and maintenance. So be sure to:

Implement Always-On SSL. Use SSL certificates to protect
every page of your website so that every interaction a visitor has
with your site is authenticated and encrypted.

Keep Servers Up to Date. This applies beyond server SSL
libraries: any patches or updates should be installed as soon as
possible. They’re released for a reason: to reduce or eliminate a
vulnerability.

Display Recognized Trust Marks. (such as the Norton Secured
Seal) in highly visible locations on your website to show
customers your commitment to their security.

Scan Regularly. Keep an eye on your web servers and watch for
vulnerabilities or malware.

Keep Server Configuration Up to Date. Make sure that old,
unsecure versions of the SSL protocol (SSL2 and SSL3) are
disabled, and newer versions of the TLS protocol (TLS1.1 and
TLS1.2) are enabled and prioritized. Use tools like Symantec’s
SSL Toolbox to verify proper server configuration.146

Educate Employees

Basic common sense and the introduction of some good security
habits can go a long way toward keeping sites and servers safe
this year:

 Ensure employees don’t open attachments from senders they

don’t know.

 Educate them on safe social media conduct: offers that look

too good probably aren’t legitimate; hot topics are prime bait
for scams; not all links lead to real login pages.

 Encourage them to adopt two-step authentication on any

website or app that offers it.

 Ensure they have different passwords for every email

account, application, and login—especially for work-related
sites and services.

 Remind then to use common sense—having antivirus

software doesn’t mean it’s OK to go on malicious or question-
able websites.

143  http://www.symantec.com/page.jsp?id=1024-bit-

certificate-support

144  http://www.symantec.com/en/uk/page.jsp?id=sha2-

transition

145  http://www.symantec.com/connect/blogs/

introducing-algorithm-agility-ecc-and-dsa

146  https://ssltools.websecurity.symantec.com/checker/

views/certCheck.jsp

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

113

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Get Safe or Get Shamed

Attackers have become more aggressive, more sophisticated,
and more ruthless than ever in their attempts to exploit the
Internet for ill gains. There is, however, plenty that individuals
and organizations can do to limit attackers’ impact.

SSL and website security are now in the public consciousness,
and if you’re not doing your part you could find yourself being
publicly shamed on HTTP Shaming, a site set up by software
engineer Tony Webster.147

When it comes to businesses and their websites, good security
processes and implementations are all that stand in the way of
total financial and reputational ruin. So get secure in 2015 with
Symantec.

147  http://arstechnica.com/security/2014/08/new-

website-aims-to-shame-apps-with-lax-security/

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

114

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Footnotes

01  http://www.symantec.com/security_response/writeup.

28  http://www.symantec.com/connect/blogs/internet-things-new-threats-

jsp?docid=2004-061419-4412-99

emerge-connected-world

02  http://www.symantec.com/connect/blogs/tenth-anniversary-mobile-

29  http://krebsonsecurity.com/2015/01/lizard-stresser-runs-on-hacked-

malware

home-routers/

03  http://www.symantec.com/connect/blogs/grayware-casting-shadow-

30

over-mobile-software-marketplace

04  http://www.pewinternet.org/2013/08/07/51-of-u-s-adults-bank-

“A Heart Device Is Found Vulnerable to Hacker Attacks”; New
York Times; Mar. 2008; http://www.nytimes.com/2008/03/12/
business/12heart-web.html?_r=0

online/

05  http://www.symantec.com/connect/blogs/future-mobile-malware

06

Ibid

07  http://www.symantec.com/connect/blogs/simplocker-first-confirmed-

file-encrypting-ransomware-android

08  https://www.usenix.org/system/files/conference/usenixsecurity14/

sec14-paper-michalevsky.pdf

09  http://www.slideshare.net/symantec/norton-mobile-apps-survey-report

10  https://www.cs.cmu.edu/~coke/history_long.txt

11  PayPal has a Buyer and Seller Protection Program to help protect

against scams like this. For more information, see the following link.
https://www.paypal.com/webapps/mpp/paypal-safety-and-security

12  Garter, Market Trends: Enter the Wearable Electronics Market With

Products for the Quantified Self, Angela McIntyre and Jessica Ekholm,
01 July 2013

13  https://securityledger.com/2013/05/fitbitten-researchers-exploit-

health-monitor-to-earn-workout-rewards/

14  http://www.symantec.com/connect/blogs/how-safe-your-quantified-

self-tracking-monitoring-and-wearable-tech

15  http://www.cnn.com/2014/05/19/justice/us-global-hacker-crackdown/

16  http://www.symantec.com/connect/blogs/creepware-who-s-watching-

you

17  http://www.wired.com/2014/08/car-hacking-chart/

18  http://www.bbc.co.uk/news/technology-23443215

19  http://www.forbes.com/sites/andygreenberg/2013/07/24/hackers-
reveal-nasty-new-car-attacks-with-me-behind-the-wheel-video/

31  https://www.gartner.com/doc/2537715/market-trends-enter-

wearable-electronics

32  U.S. Department of Homeland Security, Industrial Control System
Cyber Emergency Response Team, (ICS-CERT); ALERT-13-164-01;
https://ics-cert.us-cert.gov/alerts/ICS-ALERT-13-164-01

33  U.S. “Yes, terrorists could have hacked Dick Cheney’s heart”; The

Washington Post; Oct. 21, 2013; http://www.washingtonpost.com/
blogs/the-switch/wp/2013/10/21/yes-terrorists-could-have-hacked-
dick-cheneys-heart/

34

35

36

“Feds Probe Cybersecurity Dangers in Medical Devices”; IEEE
Spectrum; Oct. 27, 2014; http://spectrum.ieee.org/tech-talk/
biomedical/devices/feds-probe-cybersecurity-dangers-in-medical-
devices

“Health Care Systems and Medical Devices at Risk for Increased Cyber
Intrusions for Financial Gain”; U.S. Federal Bureau of Investigation (FBI)
Cyber Division, Private Industry Notice #140408-009; April 8, 2014

 “Content of Premarket Submissions for Management of
Cybersecurity in Medical Devices: Guidance for Industry and Food
and Drug Administration Staff”; U.S. Food and Drug Administration,
Center for Devices and Radiological Health (FDA CDRH); October
2, 2014; http://www.fda.gov/downloads/MedicalDevices/
DeviceRegulationandGuidance/GuidanceDocuments/UCM356190.pdf

37

“Medical-device security isn’t tracked well, research shows”; Network
World; July 19, 2012; http://www.networkworld.com/article/2189998/
data-center/medical-device-security-isn-t-tracked-well--research-
shows.html

38  http://www.symantec.com/connect/blogs/freak-vulnerability-can-

leave-encrypted-communications-open-attack

39

Ibid

20  http://www.cbsnews.com/news/car-hacked-on-60-minutes/

40  http://www.symantec.com/connect/blogs/heartbleed-bug-poses-

21  http://en.wikipedia.org/wiki/Picocell

22  http://en.wikipedia.org/wiki/Home_Node_B

23  http://www.autosec.org/pubs/cars-usenixsec2011.pdf

24  https://www.synology.com/en-us/company/news/article/Synology_

Encourages_Users_to_Update_as_SynoLocker_Ransomware_Affects_
Older_DSM_Versions/Synology%C2%AE%20Encourages%20
Users%20to%20Update%20as%20SynoLocker%20Ransomware%20
Affects%20Older%20DSM%20Versions

25  http://www.symantec.com/security_response/writeup.

jsp?docid=2013-112710-1612-99

26  http://www.symantec.com/connect/blogs/linux-worm-targeting-

hidden-devices

27  http://www.symantec.com/connect/blogs/iot-worm-used-mine-

cryptocurrency

serious-threat-unpatched-servers

41  http://news.netcraft.com/archives/2014/04/08/half-a-million-widely-

trusted-websites-vulnerable-to-heartbleed-bug.html

42  http://www.symantec.com/connect/blogs/heartbleed-reports-field

43  For those unfamiliar with UNIX terminology, a shell is a command line

user interface for interacting with the operating system. In this case,
Bash is one of the most widely used shells in all of the UNIX and Linux
worlds.

44  http://www.symantec.com/connect/blogs/shellshock-all-you-need-

know-about-bash-bug-vulnerability

45  http://www.symantec.com/connect/blogs/poodle-vulnerability-old-

version-ssl-represents-new-threat

46  http://www.wired.com/2013/03/att-hacker-gets-3-years

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

115

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

47  http://www.symantec.com/connect/blogs/massive-malvertising-

75  http://www.symantec.com/content/en/us/enterprise/media/security_

campaign-leads-browser-locking-ransomware

response/whitepapers/waterbug-attack-group.pdf

48

Ibid

76

Ibid

49  http://www.symantec.com/connect/blogs/denial-service-attacks-short-

77  http://www.symantec.com/content/en/us/enterprise/media/security_

strong

50

Ibid

response/whitepapers/regin-analysis.pdf

78  http://www.symantec.com/en/uk/outbreak/?id=regin

51  http://www.symantec.com/content/en/us/enterprise/media/security_
response/whitepapers/the-continued-rise-of-ddos-attacks.pdf

79  http://www.symantec.com/connect/blogs/turla-spying-tool-targets-

governments-and-diplomats

52  http://www.symantec.com/connect/blogs/robin-williams-goodbye-

80

Ibid

video-used-lure-social-media-scams

81  http://www.symantec.com/connect/blogs/equation-advanced-

53  http://blog.instagram.com/post/104847837897/141210-300million

cyberespionage-group-has-all-tricks-book-and-more

54  https://investor.twitterinc.com/releasedetail.cfm?ReleaseID=878170

82  https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/

55  http://www.slideshare.net/symantec/norton-mobile-apps-survey-

report

56  http://www.symantec.com/connect/blogs/instagram-scam-lottery-

winners-impersonated-offer-money-followers

57  http://www.symantec.com/connect/blogs/hacked-snapchat-accounts-

use-native-chat-feature-spread-diet-pill-spam

58  http://www.symantec.com/connect/blogs/instagram-scam-lottery-

winners-impersonated-offer-money-followers

59  http://www.symantec.com/connect/blogs/tinder-spam-year-later-

spammers-still-flirting-mobile-dating-app

60  http://www.symantec.com/connect/blogs/adult-webcam-spam-all-

roads-lead-kik-messenger

61  http://www.symantec.com/connect/blogs/tinder-spam-year-later-

spammers-still-flirting-mobile-dating-app

62

Ibid

63  http://www.symantec.com/connect/blogs/facebook-scam-leads-

nuclear-exploit-kit

64  http://www.wired.com/2014/02/can-anonymous-apps-give-rise-

authentic-internet/

65  http://www.technologyreview.com/review/531211/confessional-in-the-

Publikationen/Lageberichte/Lagebericht2014.pdf

83  http://www.symantec.com/content/en/us/enterprise/media/security_

response/whitepapers/Dragonfly_Threat_Against_Western_Energy_
Suppliers.pdf

84  http://en.wikipedia.org/wiki/OLE_for_Process_Control

85  http://www.symantec.com/connect/blogs/emerging-threat-ms-ie-

10-zero-day-cve-2014-0322-use-after-free-remote-code-execution-
vulnerabi

86  http://www.symantec.com/connect/blogs/zero-day-internet-

vulnerability-let-loose-wild

87  http://www.symantec.com/connect/blogs/sandworm-windows-zero-

day-vulnerability-being-actively-exploited-targeted-attacks

88  http://www.symantec.com/connect/blogs/how-elderwood-platform-

fueling-2014-s-zero-day-attacks

89  http://www.symantec.com/deepsight-products/

90  http://www.symantec.com/security_response/writeup.

jsp?docid=2013-052817-2105-99

91  http://www.insurancejournal.com/news/west/2014/03/07/322748.

htm

92  http://www.ponemon.org/news-2/7

palm-of-your-hand/

93  https://www.apple.com/uk/pr/library/2014/09/02Apple-Media-

66  See many issues highlighted on See many issues highlighted on http://

Advisory.html

en.wikipedia.org/wiki/4chan

67  https://www.facebook.com/about/government_requests

68  http://thenextweb.com/twitter/2014/04/30/twitter-ceo-dick-

costolo-whisper-mode-encourage-friends-privately-discuss-public-
conversations/

69  http://techcrunch.com/2014/03/20/gmail-traffic-between-google-

servers-now-encrypted-to-thwart-nsa-snooping/

70  http://www.symantec.com/connect/blogs/apple-ids-targeted-kelihos-

botnet-phishing-campaign

71  http://www.symantec.com/connect/blogs/linkedin-alert-scammers-

use-security-update-phish-credentials

72  http://www.symantec.com/connect/blogs/apple-ids-targeted-kelihos-

botnet-phishing-campaign

73  http://www.symantec.com/connect/blogs/fresh-phish-served-helping-

aes

74  http://www.symantec.com/connect/blogs/scammers-pose-company-

execs-wire-transfer-spam-campaign

94  http://securityresponse.symantec.com/content/en/us/enterprise/
media/security_response/whitepapers/attacks_on_point_of_sale_
systems.pdf

95  http://www.symantec.com/connect/blogs/demystifying-point-sale-

malware-and-attacks

96  http://www.symantec.com/content/en/us/about/presskits/b-state-of-

privacy-report-2015.pdf

97

98

99

“Illinois hospital reports data blackmail”; PC World; Dec. 15, 2014;
http://www.pcworld.com/article/2859952/illinois-hospital-reports-
data-blackmail.html

“Medical identity theft proves lucrative in myriad ways”; Fierce Health
IT; Oct. 21, 2014; http://www.fiercehealthit.com/story/medical-
identify-theft-proves-lucrative-myriad-ways/2014-10-21?utm_
medium=nl&utm_source=internal

“The Growing Threat of Medical Identity Fraud: A Call to Action”;
Medical Identity Fraud Alliance (MIFA); July 2013; http://medidfraud.
org/wp-content/uploads/2013/07/MIFA-Growing-Threat-07232013.pdf

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

116

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

100  “Your medical record is worth more to hackers than your credit card”;
Reuters; Sept. 24, 2014; http://www.reuters.com/article/2014/09/24/
us-cybersecurity-hospitals-idUSKCN0HJ21I20140924

101  “Stolen EHR Charts Sell for $50 Each on Black Market”; MedScape;
April 18, 2014; http://www.medscape.com/viewarticle/824192

126  http://www.symantec.com/security_response/writeup.

jsp?docid=2011-051715-1513-99

127  http://www.symantec.com/connect/blogs/massive-malvertising-

campaign-leads-browser-locking-ransomware

128  http://www.symantec.com/security_response/writeup.

102  http://www.symantec.com/connect/blogs/underground-black-market-

jsp?docid=2014-060610-5533-99

thriving-trade-stolen-data-malware-and-attack-services

103  Ibid

104  Ibid

105  Ibid

106  http://en.wikipedia.org/wiki/Blackhole_exploit_kit

107  http://krebsonsecurity.com/2013/12/meet-paunch-the-accused-

author-of-the-blackhole-exploit-kit/

108  http://www.symantec.com/connect/blogs/snifula-banking-trojan-back-

target-japanese-regional-financial-institutions

109  http://www.symantec.com/connect/blogs/simple-njrat-fuels-nascent-

middle-east-cybercrime-scene

110  http://www.symantec.com/connect/blogs/malicious-links-spammers-

change-malware-delivery-tactics

111  http://www.symantec.com/connect/blogs/windows-8-not-immune-

ransomware-0

112  http://www.symantec.com/connect/blogs/australians-increasingly-hit-

global-tide-cryptomalware

113  http://www.symantec.com/security_response/writeup.

jsp?docid=2013-091122-3112-99

114  http://www.symantec.com/security_response/writeup.

jsp?docid=2014-032622-1552-99

129  http://www.symantec.com/security_response/writeup.

jsp?docid=2014-072317-1950-99

130  http://www.symantec.com/security_response/writeup.

jsp?docid=2014-103005-2209-99

131  http://www.symantec.com/security_response/writeup.

jsp?docid=2014-080708-1950-99

132  http://www.symantec.com/connect/blogs/international-takedown-

wounds-gameover-zeus-cybercrime-network

133  http://krebsonsecurity.com/2014/06/operation-tovar-targets-

gameover-zeus-botnet-cryptolocker-scourge/

134  http://www.computerweekly.com/news/2240185424/Microsoft-

partnership-takes-down-1000-cybercrime-botnets

135  http://www.computerweekly.com/news/2240215443/RSA-2014-

Microsoft-and-partners-defend-botnet-disruption

136  http://www.thesafemac.com/iworm-method-of-infection-found/

137  http://www.symantec.com/connect/blogs/does-malware-still-detect-

virtual-machines

138  Ibid

139  http://www.symantec.com/content/en/us/enterprise/media/security_

response/whitepapers/threats_to_virtual_environments.pdf

140  Ibid

115  http://www.symantec.com/security_response/writeup.

141  http://www.informationweek.com/software/operating-systems/

jsp?docid=2014-061923-2824-99

windows-xp-stayin-alive/d/d-id/1279065

116  Tor is a combination of software and an open network that protects

142  For more information about Norton Online Family, please visit https://

onlinefamily.norton.com/

143  http://www.symantec.com/page.jsp?id=1024-bit-certificate-support

144  http://www.symantec.com/en/uk/page.jsp?id=sha2-transition

145  http://www.symantec.com/connect/blogs/introducing-algorithm-

agility-ecc-and-dsa

146  https://ssltools.websecurity.symantec.com/checker/views/certCheck.

jsp

147  http://arstechnica.com/security/2014/08/new-website-aims-to-shame-

apps-with-lax-security/

users against traffic analysis and helps to preserve their anonymity and
privacy online. While not inherently criminal, it also helps to protect the
anonymity of criminals in this case.

117  http://www.symantec.com/connect/blogs/cryptodefense-cryptolocker-

imitator-makes-over-34000-one-month

118  http://www.symantec.com/connect/blogs/international-takedown-

wounds-gameover-zeus-cybercrime-network

119  http://eval.symantec.com/mktginfo/enterprise/white_papers/b-

symc_report_on_rogue_security_software_exec_summary_20326021.
en-us.pdf

120  http://www.symantec.com/content/en/us/enterprise/media/security_

response/whitepapers/ransomware-a-growing-menace.pdf

121  http://www.symantec.com/security_response/writeup.

jsp?docid=2013-091122-3112-99

122  http://www.symantec.com/security_response/writeup.

jsp?docid=2014-032622-1552-99

123  http://www.symantec.com/connect/blogs/cryptodefense-cryptolocker-

imitator-makes-over-34000-one-month

124  http://www.secureworks.com/cyber-threat-intelligence/threats/

cryptowall-ransomware/

125  http://www.symantec.com/security_response/writeup.

jsp?docid=2014-050610-2450-99

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

117

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

Credits

Paul Wood, Executive Editor

Ben Nahorney, Editorial Content

Kavitha Chandrasekar, Analyst

Scott Wallace, Graphics & Design

Kevin Haley, Technical Advisor

Contributors

Alejandro Mosquera

Anand Kashyap

Axel Wirth

Bartlomiej Uscilowski

Candid Wueest

David Finn

Dylan Morss

Efrain Ortiz

Gavin O’Gorman

Kent McMullen

Lamine Aouad

Michael Klieman

Nicholas Johnston

Peter Coogan

Pierre-Antoine Vervier

Pravin Bange

Preeti Agarwal

Satnam Narang

Shankar Somasundaram

Slawomir Grzonkowski

Stephen Doherty

Tim Gallo

Vaughn Eisler

With Support From

Albert Cooley

Eric Chien

Gary Krall

Himanshu Dubey

Jason Theodorson

Kevin Thompson

Marianne Davis

Rick Andrews

William Wright

Special Thanks To

Alejandro Borgia

Anna Sampson

Camille Van Duyn

Charlie Treadwell

Cheryl Elliman

Darbi Booher

David Gantman

Fred Unterberger

Gerritt Hoekman

Gina Fiorentino

Jasmin Kohan

Jeff Scheel

Jennifer Duffourg

Jim Kunkle

Linda Smith Munyan

Mara Mort

Mary Verducci

Melissa Orr

Nisha Ramachandran

Piero DePaoli

Solange Deschatres

2015 Internet Security Threat Report  MOBILE & IOT     WEB THREATS     SOCIAL MEDIA & SCAMS     TARGETED ATTACKS

118

DATA BREACHES & PRIVACY     E-CRIME & MALWARE     APPENDIX

BACK TO TABLE OF CONTENTS

About Symantec

Symantec Corporation (NASDAQ: SYMC) is an information protection expert that helps people,
businesses and governments seeking the freedom to unlock the opportunities technology brings
– anytime, anywhere. Founded in April 1982, Symantec, a Fortune 500 company, operating one of
the largest global data-intelligence networks, has provided leading security, backup and availability
solutions for where vital information is stored, accessed and shared. The company’s more than 20,000
employees reside in more than 50 countries. Ninety-nine percent of Fortune 500 companies are
Symantec customers. In fiscal 2014, it recorded revenues of $6.7 billion. To learn more go to
www.symantec.com or connect with Symantec at: go.symantec.com/socialmedia.

More Information

 Symantec Worldwide: http://www.symantec.com/

 ISTR and Symantec Intelligence Resources: http://www.symantec.com/threatreport/

 Symantec Security Response: http://www.symantec.com/security_response/

 Norton Threat Explorer: http://us.norton.com/security_response/threatexplorer/

 Norton Cybercrime Index: http://us.norton.com/cybercrimeindex/

2015 Internet Security Threat Report  Symantec Corporation World Headquarters

350 Ellis Street

Mountain View, CA 94043 USA

+1 (650) 527 8000

1 (800) 721 3934

www.symantec.com

For specific country offices

and contact numbers,

please visit our website.

For product information in the U.S.,

call toll-free 1 (800) 745 6054.

Copyright © 2015 Symantec Corporation.
All rights reserved. Symantec, the Symantec Logo,
and the Checkmark Logo are trademarks or registered
trademarks of Symantec Corporation or its affiliates in
the U.S. and other countries. Other names may
be trademarks of their respective owners

04/15  21,500-21347932


