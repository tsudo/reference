# Symantec_ISTR24_2019

Original format: `pdf`

ISTR

Internet Security Threat Report
Volume 24 | February 2019

THE DOCUMENT IS PROVIDED “AS IS” AND ALL EXPRESS OR IMPLIED
CONDITIONS, REPRESENTATIONS AND WARRANTIES, INCLUDING ANY IMPLIED
WARRANTY OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR
NON-INFRINGEMENT, ARE DISCLAIMED, EXCEPT TO THE EXTENT THAT SUCH
DISCLAIMERS ARE HELD TO BE LEGALLY INVALID.

SYMANTEC CORPORATION SHALL NOT BE LIABLE FOR INCIDENTAL OR
CONSEQUENTIAL DAMAGES IN CONNECTION WITH THE FURNISHING,
PERFORMANCE, OR USE OF THIS DOCUMENT. THE INFORMATION CONTAINED
IN THIS DOCUMENT IS SUBJECT TO CHANGE WITHOUT NOTICE.

INFORMATION OBTAINED FROM THIRD PARTY SOURCES IS BELIEVED TO BE
RELIABLE, BUT IS IN NO WAY GUARANTEED.

SECURITY PRODUCTS, TECHNICAL SERVICES, AND ANY OTHER TECHNICAL
DATA REFERENCED IN THIS DOCUMENT (“CONTROLLED ITEMS”) ARE SUBJECT
TO U.S. EXPORT CONTROL AND SANCTIONS LAWS, REGULATIONS AND
REQUIREMENTS, AND MAY BE SUBJECT TO EXPORT OR IMPORT REGULATIONS
IN OTHER COUNTRIES.

YOU AGREE TO COMPLY STRICTLY WITH THESE LAWS, REGULATIONS AND
REQUIREMENTS, AND ACKNOWLEDGE THAT YOU HAVE THE RESPONSIBILITY
TO OBTAIN ANY LICENSES, PERMITS OR OTHER APPROVALS  THAT MAY
BE REQUIRED IN ORDER FOR YOU TO EXPORT, RE-EXPORT,  TRANSFER IN
COUNTRY OR IMPORT SUCH CONTROLLED ITEMS.

TABLE OF
CONTENTS

1

BIG NUMBERS

2

YEAR-IN-REVIEW

Formjacking

Cryptojacking

Ransomware

Living off the land
and supply chain attacks

Targeted attacks

Cloud

IoT

Election interference

3

FACTS AND FIGURES

Messaging

Malware

Mobile

Web attacks

Targeted attacks

IoT

Underground economy

METHODOLOGY

MALICIOUS URLS

ONE IN TENURLS ARE MALICIOUS

WEB ATTACKS

56%

FORMJACKING ATTACKS

4,800 AVERAGE NUMBER OF WEBSITES COMPROMISED

WITH FORMJACKING CODE EACH MONTH

BLOCKED

FORMJACKING ATTACKS
ON ENDPOINTS

3.7M

CRYPTOJACKING

8M

$362

JAN

4X

MORE CRYPTOJACKING EVENTS
BLOCKED IN 2018 VS 2017,
BUT TRENDING DOWN

52%

DROP IN CRYPTOJACKING EVENTS
BETWEEN JAN AND DEC 2018

90%

DROP IN CRYPTOCURRENCY
VALUE (MONERO)

4M

$48

DEC

ENTERPRISE
RANSOMWARE

MOBILE
RANSOMWARE

UP

12%

20%

DOWN

OVERALL
RANSOMWARE

33%

SUPPLY CHAIN
ATTACKS

%

MALICIOUS EMAIL

POWERSHELL

48%

OF MALICIOUS EMAIL ATTACHMENTS
ARE OFFICE FILES, UP FROM 5% IN 2017

%
0
0
0
1

INCREASE IN
MALICIOUS
POWERSHELL
SCRIPTS

NUMBER OF
ATTACK GROUPS
USING DESTRUCTIVE
MALWARE

AVERAGE NUMBER
OF ORGANIZATIONS
TARGETED BY EACH
ATTACK GROUP

55%

2

CYBER CRIMINALS TARGET
PAYMENT CARD DATA.

Incidents of formjacking—the use of malicious JavaScript
code to steal credit card details and other information
from payment forms on the checkout web pages of
eCommerce sites—trended upwards in 2018.

with one another. Magecart is believed to be behind several
high-profile attacks, including those on British Airways and
Ticketmaster, as well as attacks against British electronics
retailer Kitronik and contact lens seller VisionDirect.

This increase in formjacking reflects the general growth
in supply chain attacks that we discussed in ISTR 23, with
Magecart in many cases targeting third-party services in order
to get its code onto targeted websites. In the high-profile
breach of Ticketmaster, for example, Magecart compromised a
third-party chatbot, which loaded malicious code into the web
browsers of visitors to Ticketmaster’s website, with the aim of
harvesting customers’ payment data.

Symantec data shows that 4,818 unique websites were
compromised with formjacking code every month in 2018.
With data from a single credit card being sold for up to
$45 on underground markets, just 10 credit cards stolen
from compromised websites could result in a yield of up to
$2.2 million for cyber criminals each month. The appeal of
formjacking for cyber criminals is clear.

While attacks on household names make headlines,
Symantec’s telemetry shows that it is often small and
medium sized retailers, selling goods ranging from clothing
to gardening equipment to medical supplies, that have had
formjacking code injected onto their websites. This is a global
problem with the potential to affect any business that accepts
payments from customers online.

Symantec blocked more than 3.7 million formjacking
attempts in 2018, with more than 1 million of those
blocks occurring in the last two months of the year alone.
Formjacking activity occurred throughout 2018, with an
anomalous spike in activity in May (556,000 attempts in
that month alone), followed by a general upward trend in
activity in the latter half of the year.

Much of this formjacking activity has been blamed on
actors dubbed Magecart, which is believed to be several
groups, with some, at least, operating in competition

The growth in formjacking in 2018 may be partially explained
by the drop in the value of cryptocurrencies during the year:
cyber criminals who may have used websites for cryptojacking
may now be opting for formjacking. The value of stolen credit
card details on the cyber underground is probably more
assured than the value of cryptocurrencies in the current
climate.

Back to ToC

Year-in-Review  14

ISTR 24 | February 2019TRENDING DOWN, BUT
CERTAINLY NOT OUT.

Cryptojacking—where cyber criminals surreptitiously run
coinminers on victims’ devices without their knowledge
and use their central processing unit (CPU) power to mine
cryptocurrencies—was the story of the final quarter of 2017
and continued to be one of the dominant features in the
cyber security landscape in 2018.

Cryptojacking activity peaked between December 2017 and
February 2018, with Symantec blocking around 8 million
cryptojacking events per month in that period. During 2018,
we blocked more than four times as many cryptojacking
events as in 2017—almost 69 million cryptojacking events
in the 12-month period, compared to just over 16 million in
2017. However, cryptojacking activity did fall during the year,
dropping by 52 percent between January and December
2018. Despite this downward trend, we still blocked more
than 3.5 million cryptojacking events in December 2018.

This is still significant activity, despite the fact that
cryptocurrency values—which were at record-breaking
highs at the end of 2017 and played a major role in driving
the initial growth of cryptojacking—dropped significantly in
2018. While this may have led some of the initial adopters of
cryptojacking to turn to other ways to make money, such as
formjacking, it’s clear a significant cohort of cyber criminals

still think cryptojacking is worth their time. We also saw some
cryptojacking criminals targeting enterprises in 2018, with
the WannaMine (MSH.Bluwimps) cryptojacking script, which
uses the Eternal Blue exploit made famous by WannaCry to
spread through enterprise networks, rendering some devices
unusable due to high CPU usage.

The majority of cryptojacking activity continued to originate
from browser-based coinminers in 2018. Browser-based coin
mining takes place inside a web browser and is implemented
using scripting languages. If a web page contains a coin-
mining script, the web page visitors’ computing power will be
used to mine for cryptocurrency for as long as the web page
is open. Browser-based miners allow cyber criminals to target
even fully patched devices and can also allow them to operate
stealthily without the activity being noticed by victims.

We predicted that cryptojacking activity by cyber criminals
would be largely dependent on cryptocurrency values
remaining high. As cryptocurrency values have fallen, we
have also observed a decline in the volume of cryptojacking
events. However, they haven’t fallen at the same rate as
cryptocurrency values—in 2018, the value of Monero
dropped by almost 90 percent while cryptojacking dropped
by around 52 percent. This means some cyber criminals must
still find it profitable or are biding their time until another
surge in cryptocurrency values. It also shows that there are
other elements of cryptojacking that make it attractive to
cyber criminals, such as the anonymity it offers and the low
barriers to entry. It looks like cryptojacking is an area that will
continue to have a role in the cyber crime landscape.

Back to ToC

Year-in-Review  15

ISTR 24 | February 2019For the first time since 2013, we observed a decrease in
ransomware activity during 2018, with the overall number of
ransomware infections on endpoints dropping by 20 percent.
WannaCry, copycat versions, and Petya, continued to inflate
infection figures. When these worms are stripped out from
the statistics, the drop in infection numbers is steeper: a 52
percent fall.

However, within these overall figures there was one dramatic
change. Up until 2017, consumers were the hardest hit by
ransomware, accounting for the majority of infections. In 2017,
the balance tipped towards enterprises, with the majority
of infections occurring in businesses. In 2018, that shift
accelerated and enterprises accounted for 81 percent of all
ransomware infections. While overall ransomware infections
were down, enterprise infections were up by 12 percent in
2018.

This shift in victim profile was likely due to a decline in exploit
kit activity, which was previously an important channel for
ransomware delivery. During 2018, the chief ransomware
distribution method was email campaigns. Enterprises tend to
be more affected by email-based attacks since email remains
the primary communication tool for organizations.

Alongside this, a growing number of consumers are exclusively
using mobile devices, and their essential data is often backed
up in the cloud. Since most major ransomware families still
target Windows-based computers, the chances of consumers
being exposed to ransomware is declining.

ACTIVITY BEGINS TO DROP,
BUT REMAINS A CHALLENGE
FOR ORGANIZATIONS.

Another factor behind the drop in overall ransomware
activity is Symantec’s increased efficiency at blocking
ransomware earlier in the infection process, either via email
protection or using technologies such as behavioral analysis
or machine learning. Also contributing to the decline is
the fact that some cyber crime gangs are losing interest in
ransomware. Symantec saw a number of groups previously
involved in spreading ransomware move to delivering other
malware such as banking Trojans and information stealers.

However, some groups are continuing to pose a severe
threat. In further bad news for organizations, a notable
number of highly damaging targeted ransomware attacks hit
organizations in 2018, many of which were conducted by the
SamSam group. During 2018, Symantec found evidence of
67 SamSam attacks, mostly against organizations in the U.S.
In tandem with SamSam, other targeted ransomware groups
have become more active.

Additional targeted threats have also emerged. Activity
involving Ryuk (Ransom.Hermes) increased significantly in
late 2018. This ransomware was responsible for an attack in
December where the printing and distribution of several well-
known U.S. newspapers was disrupted.

Dharma/Crysis (Ransom.Crysis) is also often used in a
targeted fashion against organizations. The number of
Dharma/Crysis infection attempts seen by Symantec
more than tripled during 2018, from an average of
1,473 per month in 2017 to 4,900 per month in 2018.

In November, two Iranian nationals were indicted in the U.S.
for their alleged involvement with SamSam. It remains to
be seen whether the indictment will have any impact on the
group’s activity.

Back to ToC

Year-in-Review  16

ISTR 24 | February 2019REMAIN A STAPLE OF THE
NEW THREAT LANDSCAPE.

In previous reports, we highlighted the trend of attackers
opting for off-the-shelf tools and operating system features
to conduct attacks. This trend of “living off the land” shows
no sign of abating—in fact, there was a significant increase
in certain activity in 2018. PowerShell usage is now a staple
of both cyber crime and targeted attacks—reflected by a
massive 1,000 percent increase in malicious PowerShell
scripts blocked in 2018 on the endpoint.

In 2018, Microsoft Office files accounted for almost half (48
percent) of all malicious email attachments, jumping up from
just 5 percent in 2017. Cyber crime groups, such as Mealybug
and Necurs, continued to use macros in Office files as their
preferred method to propagate malicious payloads in 2018,
but also experimented with malicious XML files and Office
files with DDE payloads.

Zero-day exploit usage by targeted attack groups
continued to decline in 2018. Only 23 percent of attack
groups were known to use zero days, down from 27 percent in
2017. We also began seeing attacks which rely solely on living
off the land techniques and don’t use any malicious code. The
targeted attack group Gallmaker is an example of this shift,
with the group exclusively using generally available tools to
carry out its malicious activities.

Self-propagating threats continued to create headaches for
organizations but, unlike worms of old, modern worms don’t
use remotely exploitable vulnerabilities to spread. Instead,
worms such as Emotet (Trojan.Emotet) and Qakbot (W32.
Qakbot) use simple techniques including dumping passwords
from memory or brute-forcing access to network shares to
laterally move across a network.

Supply chain attacks continued to be a feature of the threat
landscape, with attacks increasing by 78 percent in 2018.
Supply chain attacks, which exploit third-party services and
software to compromise a final target, take many forms,
including hijacking software updates and injecting malicious
code into legitimate software. Developers continued to be
exploited as a source of supply chain attacks, either through
attackers stealing credentials for version control tools, or
by attackers compromising third-party libraries that are
integrated into larger software projects.

The surge in formjacking attacks in 2018 reinforced how the
supply chain can be a weak point for online retailers and
eCommerce sites. Many of these formjacking attacks were
the result of the attackers compromising third-party services
commonly used by online retailers, such as chatbots or
customer review widgets.

Both supply chain and living off the land attacks highlight the
challenges facing organizations and individuals, with attacks
increasingly arriving through trusted channels, using fileless
attack methods or legitimate tools for malicious purposes.
While we block on average 115,000 malicious PowerShell
scripts each month, this only accounts for less than 1
percent of overall PowerShell usage. Effectively identifying
and blocking these attacks requires the use of advanced
detection methods such as analytics and machine learning.

Back to ToC

Year-in-Review  17

ISTR 24 | February 2019Targeted attack actors continued to pose a significant
threat to organizations during 2018, with new groups
emerging and existing groups continuing to refine their
tools and tactics. The larger, more active attack groups
appeared to step up their activity during 2018. The 20
most active groups tracked by Symantec targeted an
average of 55 organizations over the past three years,
up from 42 between 2015 and 2017.

One notable trend was the diversification in targets,
with a growing number of groups displaying an interest
in compromising operational computers, which could
potentially permit them to mount disruptive operations
if they chose to do so.

This tactic was pioneered by the Dragonfly espionage
group, which is known for its attacks on energy companies.
During 2018, we observed the Thrip group compromise a
satellite communications operator and infect computers
running software that monitors and controls satellites.
The attack could have given Thrip the ability to seriously
disrupt the company’s operations.

We also saw the Chafer group compromise a telecoms
services provider in the Middle East. The company sells
solutions to multiple telecoms operators in the region and
the attack may have been intended to facilitate surveillance
of end-user customers of those operators.

This interest in potentially disruptive attacks is also
reflected in the number of groups known to use destructive
malware, up by 25 percent in 2018.

During 2018, Symantec exposed four previously unknown
targeted attack groups, bringing the number of targeted
attack groups first exposed by Symantec since 2009 to 32.
While Symantec exposed four new groups in both 2017

and 2018, there was a big shift in the way these groups were
uncovered. Two out of the four new groups exposed during
2018 were uncovered through their use of living off the land
tools. Indeed, one of those two groups (Gallmaker) doesn’t use
any malware in its attacks, relying exclusively on living off the
land and publicly available hacking tools.

Living off the land has been increasingly used by targeted
attack groups in recent years because it can help attackers
maintain a low profile by hiding their activity in a mass
of legitimate processes. This trend was one of the main
motivations for Symantec to create its Targeted Attack
Analytics (TAA) solution in 2018, which leverages advanced
artificial intelligence to spot patterns of malicious activity
associated with targeted attacks. Twice during 2018 we
discovered previously unknown targeted attack groups in
investigations that began with TAA triggered by living off the
land tools. The rise in the use of living off the land tools has
been mirrored by the decline of other, older attack techniques.
The number of targeted attack groups known to use zero-day
vulnerabilities was 23 percent, down from 27 percent at the
end of 2017.

One of the most dramatic developments during 2018 was
the significant increase in indictments in the United States
against people alleged to be involved in state-sponsored
espionage. Forty-nine individuals or organizations were
indicted during 2018, up from four in 2017 and five in 2016.
While most of the headlines were devoted to the indictment
of 18 alleged Russian agents, most of whom were charged
with involvement in attacks relating to the 2016 presidential
election, the indictments were far more wide ranging.
Alongside Russian nationals, 19 Chinese individuals or
organizations were charged, along with 11 Iranians, and
one North Korean.

This sudden glare of publicity may disrupt some of the
organizations named in these indictments. It will severely
limit the ability of indicted individuals to travel internationally,
potentially hampering their ability to mount operations
against targets in other countries.

Back to ToC

Year-in-Review  18

ISTR 24 | February 2019S
T
O
R
A
G
E

SPECTRE

MELTDOWN

SECURITY CHALLENGES
EMERGE ON MULTIPLE FRONTS.

From simple misconfiguration issues to vulnerabilities in
hardware chips, in 2018 we saw the wide range of security
challenges that the cloud presents.

Poorly secured cloud databases continued to be a weak point
for organizations. In 2018, S3 buckets emerged as an Achilles
heel for organizations, with more than 70 million records
stolen or leaked as a result of poor configuration. This was
on the heels of a spate of ransomware attacks against open
databases such as MongoDB in 2017, which saw attackers
wipe their contents and seek payment in order to restore
them. Attackers didn’t stop there—also targeting container
deployment systems such Kubernetes, serverless applications
and other publicly exposed API services. There’s a common
theme across these incidents—poor configuration.

There are numerous tools widely available which allow
potential attackers to identify misconfigured cloud
resources on the internet. Unless organizations take
action to properly secure their cloud resources, such as
following the advice provided by Amazon for securing S3
buckets, they are leaving themselves open to attack.

A more insidious threat to the cloud emerged in 2018 with
the revelation of several vulnerabilities in hardware chips.
Meltdown and Spectre exploit vulnerabilities in a process
known as speculative execution. Successful exploitation
provides access to memory locations that are normally
forbidden. This is particularly problematic for cloud
services because while cloud instances have their own

virtual processors, they share pools of memory—meaning
that a successful attack on a single physical system could
result in data being leaked from several cloud instances.

Meltdown and Spectre weren’t isolated cases—several
variants of these attacks were subsequently released into the
public domain throughout the year. They were also followed
up by similar chip-level vulnerabilities such as Speculative
Store Bypass and Foreshadow, or L1 Terminal Fault. This is
likely just the start, as researchers and attackers home in on
vulnerabilities at the chip level, and indicates that there are
challenging times ahead for the cloud.

Back to ToC

Year-in-Review  19

ISTR 24 | February 2019IN THE CROSSHAIRS
OF CYBER CRIMINALS AND
TARGETED ATTACK GROUPS.

While worms and bots continued to account for the vast
majority of Internet of Things (IoT) attacks, in 2018 we saw
a new breed of threat emerge as targeted attack actors
displayed an interest in IoT as an infection vector.

The overall volume of IoT attacks remained high in 2018
and consistent (-0.2 percent) compared to 2017. Routers
and connected cameras were the most infected devices and
accounted for 75 and 15 percent of the attacks respectively.
It’s unsurprising that routers were the most targeted devices
given their accessibility from the internet. They’re also
attractive as they provide an effective jumping-off point
for attackers.

The notorious Mirai distributed denial of service (DDoS)
worm remained an active threat and, with 16 percent
of the attacks, was the third most common IoT threat in
2018. Mirai is constantly evolving and variants use up to
16 different exploits, persistently adding new exploits to
increase the success rate for infection, as devices often
remain unpatched. The worm also expanded its target

scope by going after unpatched Linux servers. Another
noticeable trend was the increase in attacks against industrial
control systems (ICS). The Thrip group went after satellites,
and Triton attacked industrial safety systems, leaving them
vulnerable to sabotage or extortion attacks. Any computing
device is a potential target.

The emergence of VPNFilter in 2018 represented an evolution
of IoT threats. VPNFilter was the first widespread persistent
IoT threat, with its ability to survive a reboot making it very
difficult to remove. With an array of potent payloads at its
disposal, such as man in the middle (MitM) attacks, data
exfiltration, credential theft, and interception of SCADA
communications, VPNFilter was a departure from traditional
IoT threat activity such as DDoS and coin mining. It also
includes a destructive capability which can “brick,” or wipe a
device at the attackers’ command, should they wish to destroy
evidence. VPNFilter is the work of a skilled and well-resourced
threat actor and demonstrates how IoT devices are now facing
attack from many fronts.

Back to ToC

Year-in-Review  20

ISTR 24 | February 2019Other efforts to combat election interference in
2018 included the United States Cyber Command
contacting Russian hackers directly to tell them they
had been identified by U.S. operatives and were being
tracked; the DHS offering free security assessments
of state election machines and processes; and the
widespread adoption of so-called Albert sensors,
hardware that helps the federal government monitor
for evidence of interference with computers used to
run elections.

In July and August 2018, multiple malicious domains
mimicking websites belonging to political organizations
were discovered and shut down by Microsoft. The cyber
espionage group APT28 (which has also been attributed
by Homeland Security and the FBI to Russia) is thought to
have set-up some of these sites as part of a spear-phishing
campaign targeting candidates in the 2018 midterms.
To combat website spoofing attacks like this, Symantec
launched Project Dolphin, a free security tool for website
owners.

Adversaries continued to focus on using social media
platforms to influence voters in 2018. While this is nothing
new, the tactics used have become more sophisticated.
Some Russia-linked accounts, for example, used third
parties to purchase social media ads for them and avoided
using Russian IP addresses or Russian currency. Fake
accounts also began to focus more on promoting events
and rallies, which are not monitored as closely as politically
targeted ads.

Social media companies and government agencies took
a more proactive role in combatting election interference
in 2018. Facebook set up a “war room” to tackle election
interference and blocked numerous accounts and pages
suspected of being linked to foreign entities engaged in
attempts to influence politics in the U.S., U.K., Middle East,
and Latin America.

Twitter removed over 10,000 bots posting messages
encouraging people not to vote and updated its rules for
identifying fake accounts and protecting the integrity
of elections. Twitter also released an archive of tweets
associated with two state-sponsored propaganda operations
that abused the platform to spread disinformation intended
to sway public opinion.

With the 2016 U.S. presidential election impacted by several
cyber attacks, such as the attack on the Democratic National
Committee (DNC), all eyes were on the 2018 midterms. And,
just one month after Election Day had passed, the National
Republican Congressional Committee (NRCC) confirmed its
email system was hacked by an unknown third party in the
run-up to the midterms. The hackers reportedly gained access
to the email accounts of four senior NRCC aides and may
have collected thousands of emails over the course of several
months.

Then, in January 2019, the DNC revealed it was targeted by an
unsuccessful spear-phishing attack shortly after the midterms
had ended. The cyber espionage group APT29, which has
been attributed by the U.S. Department of Homeland Security
(DHS) and the FBI to Russia, is thought to be responsible for
the campaign.

Back to ToC

Year-in-Review  21

ISTR 24 | February 2019MESSAGING

In 2018, employees of small organizations were more likely to be hit by email threats—including
spam, phishing, and email malware—than those in large organizations. We also found that spam
levels continued to increase in 2018, as they have done every year since 2015, with 55 percent of
emails received in 2018 being categorized as spam. Meanwhile, the email malware rate remained
stable, while phishing levels declined, dropping from 1 in 2,995 emails in 2017, to 1 in 3,207 emails
in 2018. The phishing rate has declined every year for the last four years.

We also saw fewer URLs used in malicious emails as attackers refocused on using malicious email
attachments as a primary infection vector. The use of malicious URLs in emails had jumped to
12.3 percent in 2017, but it dropped back to 7.8 percent in 2018. Symantec telemetry shows that
Microsoft Office users are the most at risk of falling victim to email-based malware, with Office
files accounting for 48 percent of malicious email attachments, jumping from 5 percent in 2017.

48%

OF MALICIOUS EMAIL
ATTACHMENTS ARE
OFFICE FILES
UP FROM 5% IN 2017

EMAIL DISGUISED AS
NOTIFICATION, SUCH AS
INVOICE OR RECEIPT

ATTACHED OFFICE
FILE CONTAINS
MALICIOUS SCRIPT

OPENING ATTACHMENT
EXECUTES SCRIPT
DOWNLOADS MALWARE

1

2

3

MALICIOUS EMAIL RATE (YEAR)

MALICIOUS EMAIL PER USER (MONTH)

2018

1 in 412

MALICIOUS EMAIL URL RATE (YEAR)

2018

7.8%

The pecentage of users hit with
malicious email trended up
during 2018

MALICIOUS EMAIL RATE (MONTH)

MALICIOUS EMAIL URL RATE (MONTH)

200

300

400

500

600

700

800

14%

12%

10%

8%

6%

4%

2%

0

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

Malicious email rate (1 in)

% of malicious email

30%

25%

20%

15%

10%

5%

0

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

Users targeted (%)

MALICIOUS EMAIL RATE BY INDUSTRY (YEAR)

INDUSTRY

Mining

Agriculture, Forestry, & Fishing

Public Administration

Manufacturing

Wholesale Trade

Construction

Nonclassifiable Establishments

Transportation & Public Utilities

Finance, Insurance, & Real Estate

Services

Retail Trade

MALICIOUS EMAIL RATE (1 IN)

258

302

302

369

372

382

450

452

491

493

516

Back to ToC

Facts and Figures  24

ISTR 24 | February 2019MALICIOUS EMAIL URL RATE BY INDUSTRY (YEAR)

MALICIOUS EMAIL PER USER BY INDUSTRY (YEAR)

MALICIOUS EMAIL URL RATE BY ORGANIZATION SIZE (YEAR)

USERS TARGETED (%)

ORGANIZATION SIZE

MALICIOUS EMAIL (%)

INDUSTRY

EMAIL MALWARE (%)

Agriculture, Forestry, & Fishing

Retail Trade

Mining

Services

Construction

Public Administration

Finance, Insurance, & Real Estate

Manufacturing

Nonclassifiable Establishments

Wholesale Trade

Transportation & Public Utilities

11.2

10.9

8.9

8.2

7.9

7.8

7.7

7.2

7.2

6.5

6.3

INDUSTRY

Mining

Wholesale Trade

Construction

Nonclassifiable Establishments

Retail Trade

Agriculture, Forestry, & Fishing

Manufacturing

Public Administration

Transportation & Public Utilities

Services

Finance, Insurance, & Real Estate

38.4

36.6

26.6

21.2

21.2

21.1

20.6

20.2

20.0

11.7

11.6

Employees of smaller organizations
were more likely to be hit by email
threats—including spam, phishing,
and email malware—than those in
large organizations.

MALICIOUS EMAIL RATE BY ORGANIZATION SIZE (YEAR)

ORGANIZATION SIZE

MALICIOUS EMAIL RATE (1 IN)

1-250

251-500

501-1000

1001-1500

1501-2500

2501+

323

356

391

823

440

556

1-250

251-500

501-1000

1001-1500

1501-2500

2501+

6.6

8.3

6.6

8.3

7.3

8.6

MALICIOUS EMAIL PER USER BY ORGANIZATION SIZE (YEAR)

ORGANIZATION SIZE

USERS TARGETED (1 IN)

1-250

251-500

501-1000

1001-1500

1501-2500

2501+

6

6

4

7

4

11

Back to ToC

Facts and Figures  25

ISTR 24 | February 2019MALICIOUS EMAIL RATE BY COUNTRY (YEAR)

COUNTRY

Saudi Arabia

Israel

Austria

South Africa

Serbia

Greece

Oman

Taiwan

Sri Lanka

UAE

Thailand

Poland

Norway

Hungary

Qatar

Singapore

Italy

Netherlands

UK

Ireland

Luxembourg

Hong Kong

China

Denmark

Malaysia

Colombia

Switzerland

Papua New Guinea

Germany

Philippines

Belgium

MALICIOUS EMAIL RATE (1 IN)

118

122

128

131

137

142

160

163

169

183

183

185

190

213

226

228

232

241

255

263

272

294

309

311

311

328

334

350

352

406

406

COUNTRY

Brazil

South Korea

Portugal

Spain

Finland

Canada

Sweden

New Zealand

USA

France

Australia

India

Mexico

Japan

MALICIOUS EMAIL RATE (1 IN)

415

418

447

510

525

525

570

660

674

725

728

772

850

905

MALICIOUS EMAIL URL RATE BY COUNTRY (YEAR)

COUNTRY

Brazil

Mexico

Norway

Sweden

Canada

New Zealand

Colombia

Australia

France

Finland

Switzerland

Spain

MALICIOUS EMAIL (%)

35.7

29.7

12.8

12.4

11.5

11.3

11.0

10.9

10.5

9.7

9.5

9.4

Qatar

USA

Portugal

India

Philippines

Singapore

Luxembourg

Italy

Austria

South Africa

Papua New Guinea

South Korea

Germany

Japan

Belgium

UK

Hungary

Saudi Arabia

Denmark

Hong Kong

Malaysia

China

Netherlands

Serbia

Taiwan

UAE

Sri Lanka

Ireland

Oman

Thailand

Greece

Poland

Israel

8.9

8.9

8.4

8.3

8.1

7.7

7.3

7.1

6.7

6.7

6.5

6.5

6.3

6.3

6.1

6.1

5.9

5.2

5.1

5.1

5.1

4.9

4.9

4.4

4.4

4.2

4.1

3.9

3.6

3.4

3.3

2.8

1.9

Back to ToC

Facts and Figures  26

ISTR 24 | February 2019TOP EMAIL THEMES (YEAR)

TOP MALICIOUS EMAIL ATTACHMENT TYPES (YEAR)

TOP BEC EMAIL KEYWORDS (YEAR)

SUBJECT TOPIC

Bill

Email delivery failure

Package delivery

Legal/law enforcement

Scanned document

TOP EMAIL KEYWORDS (YEAR)

WORDS

invoice

mail

sender

payment

important

message

new

returned

:

delivery

PERCENT

15.7

13.3

2.4

1.1

0.3

PERCENT

13.2

10.2

9.2

8.9

8.5

7.7

7.2

6.9

6.9

6.6

FILE TYPE

.doc, .dot

.exe

.rtf

.xls, .xlt, .xla

.jar

.html, htm

.docx

.vbs

.xlsx

.pdf

PERCENT

37.0

19.5

14.0

7.2

5.6

5.5

2.3

1.8

1.5

0.8

SUBJECT

urgent

request

important

payment

attention

outstanding payment

info

important update

attn

transaction

PERCENT

8.0

5.8

5.4

5.2

4.4

4.1

3.6

3.1

2.3

2.3

TOP MALICIOUS EMAIL ATTACHMENT CATEGORIES (YEAR)

EMAIL PHISHING RATE (YEAR)

FILE TYPE

Scripts

Executables

Other

PERCENT

47.5

25.7

25.1

PHISHING RATE (1 IN)

3,207

MONTHLY AVERAGE NUMBER OF ORGANIZATIONS TARGETED
BY BEC SCAMS (YEAR)

AVERAGE

5,803

AVERAGE BEC EMAILS PER ORGANIZATION (YEAR)

AVERAGE

4.5

Phishing levels declined, dropping
from 1 in 2,995 emails in 2017,
to 1 in 3,207 emails in 2018.

Back to ToC

Facts and Figures  27

ISTR 24 | February 2019EMAIL PHISHING RATE (MONTH)

EMAIL PHISHING RATE BY INDUSTRY (YEAR)

EMAIL PHISHING RATE BY ORGANIZATION SIZE (YEAR)

INDUSTRY

PHISHING RATE (1 IN)

ORGANIZATION SIZE

PHISHING RATE (1 IN)

2,000

2,500

3,000

3,500

4,000

4,500

5,000

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

Phishing rate (1 in)

EMAIL PHISHING RATE PER USER (MONTH)

Agriculture, Forestry, & Fishing

Finance, Insurance, & Real Estate

Mining

Wholesale Trade

Public Administration

Services

Construction

Retail Trade

Manufacturing

Nonclassifiable Establishments

Transportation & Public Utilities

1,769

2,628

2,973

3,042

3,473

3,679

3,960

3,971

3,986

5,047

5,590

30

40

50

60

70

80

EMAIL PHISHING RATE PER USER BY INDUSTRY (YEAR)

INDUSTRY

Wholesale Trade

Agriculture, Forestry, & Fishing

Mining

Retail Trade

Construction

Finance, Insurance, & Real Estate

Manufacturing

Nonclassifiable Establishments

Public Administration

Transportation & Public Utilities

Services

USERS TARGETED (1 IN)

22

28

30

36

39

46

52

53

57

62

64

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

Users targeted (1 in)

1-250

251-500

501-1000

1001-1500

1501-2500

2501+

2,696

3,193

3,203

6,543

3,835

4,286

EMAIL PHISHING RATE PER USER BY ORGANIZATION SIZE
(YEAR)

ORGANIZATION SIZE

USERS TARGETED (1 IN)

1-250

251-500

501-1000

1001-1500

1501-2500

2501+

52

57

30

56

36

82

Back to ToC

Facts and Figures  28

ISTR 24 | February 2019

EMAIL PHISHING RATE BY COUNTRY (YEAR)

EMAIL SPAM RATE (MONTH)

COUNTRY

Saudi Arabia

Norway

Netherlands

Austria

South Africa

Hungary

Thailand

Taiwan

Brazil

UAE

New Zealand

Hong Kong

Singapore

Luxembourg

Italy

Qatar

China

USA

Ireland

Belgium

Sweden

Australia

Switzerland

Spain

UK

Oman

Papua New Guinea

Sri Lanka

Portugal

Philippines

Canada

PHISHING RATE (1 IN)

675

860

877

1,306

1,318

1,339

1,381

1,712

1,873

2,312

2,446

2,549

2,857

2,860

3,048

3,170

3,208

3,231

3,321

3,322

3,417

3,471

3,627

3,680

3,722

3,963

4,011

4,062

4,091

4,241

4,308

COUNTRY

Greece

Israel

Colombia

Malaysia

Germany

Denmark

Mexico

France

India

Serbia

Finland

Japan

South Korea

Poland

PHISHING RATE (1 IN)

4,311

4,472

4,619

4,687

5,223

5,312

5,389

5,598

5,707

6,376

6,617

7,652

8,523

9,653

EMAIL SPAM RATE (YEAR)

EMAIL SPAM RATE (%)

55

56.0%

55.5%

55.0%

54.5%

54.0%

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

Email spam rate (%)

EMAIL SPAM PER USER (MONTH)

85

80

75

70

65

60

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

Spam per user

Back to ToC

Facts and Figures  29

ISTR 24 | February 2019EMAIL SPAM RATE BY INDUSTRY (YEAR)

EMAIL SPAM RATE BY ORGANIZATION SIZE (YEAR)

INDUSTRY

Mining

Finance, Insurance, & Real Estate

Manufacturing

Public Administration

Agriculture, Forestry, & Fishing

Transportation & Public Utilities

Nonclassifiable Establishments

Services

Retail Trade

Construction

Wholesale Trade

EMAIL SPAM RATE (%)

ORGANIZATION SIZE

EMAIL SPAM RATE (%)

58.3

56.7

55.1

54.9

54.6

54.6

54.2

54.1

53.7

53.6

52.6

1-250

251-500

501-1000

1001-1500

1501-2500

2501+

55.9

53.6

54.5

56.9

53.7

54.9

EMAIL SPAM PER USER BY ORGANIZATION SIZE (YEAR)

ORGANIZATION SIZE

SPAM PER USER

EMAIL SPAM PER USER BY INDUSTRY (YEAR)

INDUSTRY

Wholesale Trade

Retail Trade

Mining

Construction

Nonclassifiable Establishments

Transportation & Public Utilities

Manufacturing

Agriculture, Forestry, & Fishing

Public Administration

Finance, Insurance, & Real Estate

Services

SPAM PER USER

135

111

109

103

97

93

79

66

63

61

59

1-250

251-500

501-1000

1001-1500

1501-2500

2501+

EMAIL SPAM RATE BY COUNTRY (YEAR)

COUNTRY

Saudi Arabia

China

Brazil

Sri Lanka

Norway

Oman

Sweden

Mexico

UAE

USA

Colombia

55

57

109

125

107

55

EMAIL SPAM RATE (%)

66.8

62.2

60.8

60.6

59.1

58.6

58.3

58.1

58.1

57.5

56.8

Belgium

Serbia

Singapore

UK

Germany

Taiwan

Austria

Finland

Hungary

Greece

Israel

Denmark

France

Netherlands

Australia

New Zealand

Canada

Italy

Poland

Spain

Qatar

South Korea

Portugal

Luxembourg

Malaysia

Thailand

Ireland

India

South Africa

Switzerland

Hong Kong

Papua New Guinea

Philippines

Japan

56.2

55.8

55.4

54.8

54.8

54.5

54.4

54.4

54.4

54.2

54.1

54.1

54

53.9

53.9

53.4

53.4

53.4

53.2

52.9

52.6

52.4

52.1

51.4

51.4

51.1

51

50.9

50.8

50.8

50.5

50

49.5

48.7

Back to ToC

Facts and Figures  30

ISTR 24 | February 2019MALWARE

Emotet continued to aggressively expand its market share in 2018, accounting
for 16 percent of financial Trojans, up from 4 percent in 2017. Emotet was also
being used to spread Qakbot, which was in 7th place in the financial Trojans
list, accounting for 1.8 percent of detections. Both of these threats present
further serious challenges for organizations due to their self-propagating
functionality.

Use of malicious PowerShell scripts increased by 1,000 percent in 2018, as
attackers continued the movement towards living off the land techniques. A
common attack scenario uses Office macros to call a PowerShell script, which
in turn downloads the malicious payload. Office macro downloaders accounted
for the majority of downloader detections, while VBS.Downloader and
JS.Downloader threats declined.

In 2018, we also blocked 69 million cryptojacking events—four times as many
events as we blocked in 2017. However, cryptojacking activity declined by 52
percent between January and December 2018. This mirrored the decline in
cryptocurrency values, albeit at a slower rate. For the first time since 2013,
the overall number of ransomware infections fell, dropping by more than
20 percent year-on-year. However, enterprise detections bucked the trend,
increasing by 12 percent, demonstrating that ransomware continues to be a
problem for enterprises. Fewer new ransomware families emerged in 2018,
indicating that ransomware may hold less appeal for cyber criminals than it
previously did.

SELF-PROPAGATING
EMOTET JUMPS UP TO

FROM 4% in 2017

8,000,000
$450

$400

7,000,000

$350

$300

6,000,000

$250

$200

5,000,000

$150

$100

4,000,000

$50

0
3,000,000

TOTAL CRYPTOJACKING EVENTS BY MONTH

VALUE OF MONERO

NEW MALWARE VARIANTS (YEAR)

TOP NEW MALWARE VARIANTS (MONTH)

YEAR

2016

2017

2018

NEW VARIANTS

PERCENT CHANGE

357,019,453

669,947,865

246,002,762

0.5

87.7

-63.3

Emotet continued to aggressively
expand its market share in
2018, accounting for 16 percent
of financial Trojans, up from 4
percent in 2017.

35M

30M

25M

20M

15M

10M

5M

0

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

XM.Mailcab@mm

W32.Ramnit!html

Trojan.Kotver!gm2

Heur.AdvML.C

WS.Reputation.1

W32.Almanahe.B!inf

PUA.WASMcoinminer

Heur.AdvML.B

W32.Sality.AE

JS.Webcoinminer

Back to ToC

Facts and Figures  32

ISTR 24 | February 2019TOP MALWARE (YEAR)

TOP MALWARE (MONTH)

THREAT NAME

Heur.AdvML.C

Heur.AdvML.B

BloodHound.SymVT.FP

JS.Webcoinminer

Heur.AdvML.S.N

W97M.Downloader

Packed.Dromedan!lnk

Hacktool

Hacktool.Kms

Trojan.Mdropper

ATTACKS BLOCKED

43,999,373

PERCENT

52.1

8,373,445

3,193,779

2,380,725

2,300,919

1,233,551

1,215,196

846,292

763,557

679,248

9.9

3.8

2.8

2.7

1.5

1.4

1.0

0.9

0.8

Cyber crime groups, such as
Mealybug and Necurs, continued to
use macros in Office files as their
preferred method to propagate
malicious payloads in 2018.

15M

12M

9M

6M

3M

0

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

BloodHound.SymVT.FP

Heur.AdvML.B

Heur.AdvML.S.N

Trojan.Mdropper

Hacktool

Heur.AdvML.Cf

JS.Webcoinminer

W97M.Downloader

Hacktool.Kms

Packed.Dromedan!lnk

Back to ToC

Facts and Figures  33

ISTR 24 | February 2019TOTAL MALWARE (MONTH)

OFFICE MACRO DOWNLOADERS (MONTH)

JAVASCRIPT DOWNLOADERS (MONTH)

25M

20M

15M

10M

5M

0

300K

250K

200K

150K

100K

50K

0

150K

120K

90K

60K

30K

0

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

Attacks blocked

Downloaders blocked

Downloaders blocked

TOTAL DOWNLOADERS (MONTH)

VBSCRIPT DOWNLOADERS (MONTH)

350K

300K

250K

200K

150K

100K

50K

0

While VBS.Downloader and
JS.Downloader threats trended
downwards in 2018, Office macro
downloaders trended upwards
towards the end of the year.

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

Downloaders blocked

100K

80K

60K

40K

20K

0

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

Downloaders blocked

Back to ToC

Facts and Figures  34

ISTR 24 | February 2019TOTAL MALWARE BY OPERATING SYSTEM (YEAR)

TOP NEW MAC MALWARE VARIANTS (MONTH)

YEAR

2016

2017

2018

OPERATING SYSTEM

ATTACKS BLOCKED

PERCENT

Windows

Mac

Windows

Mac

Windows

Mac

161,708,289

2,445,414

165,639,264

4,011,252

144,338,341

4,206,986

98.5

1.5

97.6

2.4

97.2

2.8

TOTAL MAC MALWARE (MONTH)

500K

400K

300K

200K

100K

0

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

Attacks blocked

500K

400K

300K

200K

100K

0

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

NEW MAC MALWARE VARIANTS (YEAR)

Wasm.Webcoinminer

PUA.WASMcoinminer

Miner.Jswebcoin

Heur.AdvML.B

YEAR

2016

2017

2018

VARIANTS

772,018

1,390,261

1,398,419

PERCENT CHANGE

W97M.Downloader

OSX.Shlayer

JS.Webcoinminer

Bloodhound.Unknown

80.1

0.6

SMG.Heur!gen

JS.Nemucod

Back to ToC

Facts and Figures  35

ISTR 24 | February 2019TOP MAC MALWARE (YEAR)

TOP MAC MALWARE (MONTH)

THREAT NAME

OSX.MacKeeper

OSX.Malcol

W97M.Downloader

OSX.Malcol.2

Heur.AdvML.B

JS.Webcoinminer

Trojan.Mdropper

OSX.Shlayer

OSX.AMCleaner!g1

JS.Downloader

ATTACKS BLOCKED

PERCENT

452,858

338,806

262,704

205,378

166,572

122,870

77,800

59,197

49,517

40,543

19.6

14.7

11.4

8.9

7.2

5.3

3.4

2.6

2.1

1.8

In 2018, Symantec blocked 69
million cryptojacking events—four
times as many events as 2017.

250K

200K

150K

100K

50K

0

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

W97M.Downloader

OSX.Malcol.2

OSX.MacKeeper!gen1

JS.Webcoinminer

Trojan.Mdropper

OSX.Malcol

OSX.MacKeeper

Heur.AdvML.B

OSX.Shlayer

OSX.AMCleaner!g1

Back to ToC

Facts and Figures  36

ISTR 24 | February 2019PERCENTAGE SSL-ENABLED MALWARE (YEAR)

RANSOMWARE BY COUNTRY (MONTH)

YEAR

2017

2018

PERCENTAGE OF MALWARE THAT USES SSL

TOTAL RANSOMWARE (YEAR)

YEAR

2018

RANSOMWARE BY MARKET (YEAR)

MARKET

Consumer

Enterprise

TOP RANSOMWARE BY COUNTRY (YEAR)

COUNTRY

China

India

USA

Brazil

Portugal

Mexico

Indonesia

Japan

South Africa

Chile

4.5

3.9

TOTAL

545,231

TOTAL

100,907

444,259

PERCENT

16.9

14.3

13.0

5.0

3.9

3.5

2.6

2.1

2.1

1.8

40K

35K

30K

25K

20K

15K

10K

5K

0

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

USA

South Africa

Portugal

Mexico

Japan

Indonesia

India

China

Chile

Brazil

Back to ToC

Facts and Figures  37

ISTR 24 | February 2019TOTAL RANSOMWARE (MONTH)

RANSOMWARE BY MARKET (MONTH)

MALWARE: TOP COINMINER VARIANTS (MONTH)

60K

50K

40K

30K

20K

10K

0

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

Jan

Feb

Mar

Apr

may

Jun

Jul

Aug

Sep

Oct

Nov

Dec

Ransomware

NEW RANSOMWARE VARIANTS (MONTH)

Enterprise

Consumer

25K

20K

15K

10K

5K

0

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

New variants

NEW RANSOMWARE VARIANTS (YEAR)

YEAR

2018

TOTAL

186,972

NEW RANSOMWARE FAMILIES (YEAR)

98

30

28

2015

2016

2017

Ransomware families

10

2018

50K

40K

30K

20K

10K

0

120

100

80

60

40

20

0

8M

7M

6M

5M

4M

3M

2M

1M

0
Dec

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Zcashminer

WASM.Webcoinminer

Linux.Coinminer

CPUMiner

Xiaobaminer

Shminer

JS.Webcoinminer

Bitcoinminer

XMRigminer

Coinminer

The overall number of ransomware
infections fell, dropping by more
than 20 percent year-on-year.
However, enterprise detections
bucked the trend, increasing by
12 percent, demonstrating that
ransomware continues to be a
problem for enterprises.

Back to ToC

Facts and Figures  38

ISTR 24 | February 2019TOTAL CRYPTOJACKING (MONTH)

TOP COINMINERS (YEAR)

COINMINER BY MARKET (MONTH)

8M

7M

6M

5M

4M

3M

2M

1M

0

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

Cryptojacking

THREAT NAME

ATTACKS BLOCKED

PERCENT

JS.Webcoinminer

WASM.Webcoinminer

Bitcoinminer

Bluwimps

XMRigminer

Coinminer

Zcashminer

Gyplyraminer

CPUMiner

Linux.Coinminer

2,768,721

2,201,789

414,297

58,601

58,301

38,655

13,389

5,221

3,807

3,324

49.7

39.5

7.4

1.1

1.0

0.7

0.2

0.1

0.1

0.1

TOP COINMINERS (MONTH)

TOP MAC COINMINERS (MONTH)

2.5M

2.0M

1.5M

1.0M

0.5M

0

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

Enterprise

Consumer

TOTAL FINANCIAL TROJANS (MONTH)

150K

120K

90K

60K

30K

0

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

Zcashminer

Linux.Coinminer

Gyplyraminer

Bluwimps

Zcashminer

OSX.Coinminer

Linux.Coinminer

CPUMiner

XMRigminer

JS.Webcoinminer

Coinminer

Bitcoinminer

XMRigminer

Neoscryptminer

JS.Webcoinminer

Bitcoinminer

WASM.Webcoinminer

CPUMiner

WASM.Webcoinminer

Coinminer

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

Attacks blocked

1.5M

1.2M

900K

600K

300K

0

7K

6K

5K

4K

3K

2K

1K

0

Back to ToC

Facts and Figures  39

ISTR 24 | February 2019TOP FINANCIAL TROJANS (MONTH)

POWERSHELL DETECTIONS (MONTH)

Use of malicious PowerShell
scripts increased by 1,000 percent
in 2018, as attackers continued the
movement towards living off the
land techniques.

80K

70K

60K

50K

40K

30K

20K

10K

0
Dec

VIRTUAL-MACHINE-AWARE MALWARE (YEAR)

20%

18%

16%

15%

2015

2016

2017

2018

Virtual-machine-aware malware

DATE

PERCENTAGE MALICIOUS POWERSHELL SCRIPTS

RATIO

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

0.1

0.5

2.5

0.4

1.3

0.9

1.4

0.8

1.0

1.0

0.7

0.7

1 in 1,000

1 in 200

1 in 40

1 in 250

1 in 77

1 in 111

1 in 71

1 in 125

1 in 100

1 in 100

1 in 143

1 in 143

POWERSHELL DETECTIONS (YEAR)

YEAR

2017

2018

PERCENT OF TOTAL
WHICH IS MALICIOUS

0.9

0.9

RATIO

1 in 111

1 in 111

PERCENT INCREASE
OF MALICIOUS
SCRIPTS

998.9

25%

20%

15%

10%

5%

0

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Zbot

Trickybot

Shylock

Ramnit

Qakbot

Emotet

Cridex

Cidox/Rovnix

Carberp

Bebloh

TOP FINANCIAL TROJANS (YEAR)

FINANCIAL TROJAN

ATTACKS BLOCKED

PERCENT

Ramnit

Zbot

Emotet

Cridex

Carberp

Trickybot

Qakbot

Shylock

Bebloh

Cidox/Rovnix

271,930

100,821

92,039

31,539

22,690

14,887

10,592

7,354

5,592

3,889

47.4

17.6

16.0

5.5

4.0

2.6

1.8

1.3

1.0

0.7

Back to ToC

Facts and Figures  40

ISTR 24 | February 2019MOBILE

While the overall number of mobile malware infections fell during
2018, there was a rapid increase in the number of ransomware
infections on mobile devices, up by a third when compared to 2017.
The U.S. was the worst affected by mobile ransomware, accounting
for 63 percent of infections. It was followed by China (13 percent)
and Germany (10 percent).

Managing mobile device security continues to present a challenge
for organizations. During 2018, one in 36 devices used in
organizations were classed as high risk. This included devices
that were rooted or jailbroken, along with devices that had a high
degree of certainty that malware had been installed.

33%

ONE IN

MOBILE
DEVICES
HAD HIGH
RISK APPS
INSTALLED

MOBILE
RANSOMWARE
INFECTIONS
INCREASED
FROM 2017

NEW MOBILE MALWARE VARIANTS (YEAR)

NEW MOBILE MALWARE FAMILIES (YEAR)

6,705

5,932

68

50

8K

7K

6K

5K

4K

3K

2K

1K

0

2,328

80

70

60

50

40

30

20

10

0

23

During 2018, Symantec blocked an
average of 10,573 malicious mobile
apps per day. Tools (39%), Lifestyle
(15%), and Entertainment (7%)
were the most frequently seen
categories of malicious apps.

2016

2017

2018

2016

2017

2018

New variants added

New families added

NUMBER OF BLOCKED MOBILE APPS (YEAR)

MONTHLY AVERAGE NUMBER OF MOBILE RANSOMWARE
(YEAR)

PER DAY

10,573

PER MONTH

4,675

TOP MALICIOUS MOBILE APP CATEGORIES (YEAR)

TOP MOBILE MALWARE (YEAR)

CATEGORY

Tools

LifeStyle

Entertainment

Social & Communication

Music & Audio

Brain & Puzzle Games

Photo & Video

Arcade & Action Games

Books & Reference

Education

PERCENT

39.1

14.9

7.3

6.2

4.3

4.2

4.2

4.1

3.2

2.6

THREAT NAME

Malapp

Fakeapp

MalDownloader

FakeInst

Mobilespy

HiddenAds

Premiumtext

MobileSpy

HiddenApp

Opfake

PERCENT

29.7

9.1

8.9

6.6

6.3

4.7

4.4

2.8

2.5

2.0

Back to ToC

Facts and Figures  42

ISTR 24 | February 2019TOP COUNTRIES FOR MOBILE MALWARE (YEAR)

LENGTH OF EXPOSURE TO NETWORK THREATS FOR MOBILE
DEVICES (YEAR)

DEVICES RUNNING NEWEST ANDROID VERSION (YEAR)

Other 31.3%

USA 24.7%

India 23.6%

Germany 3.9%

China 3%

Japan 2.8%

Russia 2.6%

Brazil 2.3%

Netherlands 2.1%

Australia 1.9%

Indonesia 1.8%

DEVICES EXPOSED TO NETWORK ATTACKS

PERCENT

After 1 month
(out of devices created 1-4 months ago)

After 2 months
(out of devices created 2-5 months ago)

After 3 months
(out of devices created 3-6 months ago)

After 4 months
(out of devices created 4-7 months ago)

15.1

21.8

27.4

32.2

DEVICES THAT DO NOT HAVE ENCRYPTION ENABLED (YEAR)

All new
Android versions
23.7%

Newest
major version
18.6%

Newest
minor version
5.1%

Other 76.3%

Percent of malware

JAILBROKEN OR ROOTED MOBILE DEVICE RATE (YEAR)

SEGMENT

Consumer

Enterprise

SEGMENT

Android Consumer

Android Enterprise

iOS Consumer

iOS Enterprise

RATIO

1 in 23

1 in 3,890

1 in 828

1 in 4,951

DEVICES RISK LEVELS (YEAR)

DEVICE RISK LEVEL

Minimal

Low

Medium

PASSWORD PROTECTED MOBILE DEVICES BY MARKET
(YEAR)

High (including rooted/jailbroken/have
high-certainty-malware apps installed)

PERCENT

13.4

10.5

RATIO

1 in 2

1 in 4

1 in 4

1 in 36

SEGMENT

Consumer

Enterprise

PERCENT

97.9

98.4

DEVICES RUNNING NEWEST IOS VERSION (YEAR)

Other
21.7%

Newest minor
version 29.7%

Newest major
version 48.6%

All new iOS versions 78.3%

Back to ToC

Facts and Figures  43

ISTR 24 | February 2019The percentage of mobile apps
that employ invasive advertising
techniques dropped. Having stood
at 30% in 2017, it fell to 26%
in 2018.

RATIO OF APPS THAT ACCESS HIGH RISK DATA (YEAR)

RATIO OF APPS THAT ACCESS HEALTH DATA (YEAR)

YEAR

2016

2017

2018

APPS ACCESSING HIGH-
RISK DATA (%)

7.2

8.9

6.9

RATIO

1 in 13.9

1 in 11.3

1 in 14.5

CHANGE (PP)

1.7

-2

YEAR

2016

2017

2018

APPS ACCESSING
HEALTH DATA (%)

0.2

1.7

2.2

RATIO

1 in 427.3

1 in 57.6

1 in 46.3

CHANGE (PP)

1.5

0.5

RATIO OF APPS THAT CONTAIN HARD CODED CREDENTIALS
(YEAR)

RATIO OF APPS THAT USE INVASIVE ADVERTISING (YEAR)

YEAR

2016

2017

2018

APPS CONTAINING HARD-CODED
CREDENTIALS (%)

0.8

1.1

1.0

RATIO

1 in 124.5

1 in 91.0

1 in 99.1

CHANGE (PP)

0.3

-0.1

YEAR

2016

2017

2018

PERCENTAGE OF
APPS USING INVASIVE
ADVERTISING

19.4

30.5

26.4

RATIO

1 in 5.2

1 in 3.3

1 in 3.8

CHANGE (PP)

11.1

-4.1

RATIO OF APPS THAT USE HOT PATCHING (YEAR)

PERCENTAGE OF ORGANIZATIONS AFFECTED BY APPS THAT
ACCESS HEALTH DATA (YEAR)

YEAR

2016

2017

2018

APPS USING HOT-
PATCHING RISK (%)

0.7

0.35

0.01

RATIO

1 in 142.1

1 in 285.1

1 in 7,146.0

CHANGE (PP)

-0.35

-0.34

YEAR

2016

2017

2018

ORGANIZATIONS WITH
1+ APPS: HEALTH DATA
(%)

27.6

44.9

39.0

RATIO

1 in 3.6

1 in 2.2

1 in 2.6

CHANGE (PP)

17.3

-5.9

Back to ToC

Facts and Figures  44

ISTR 24 | February 2019PERCENTAGE OF ORGANIZATIONS AFFECTED BY APPS THAT
ACCESS HIGH RISK DATA (YEAR)

PERCENTAGE OF ORGANIZATIONS AFFECTED BY APPS THAT
USE INVASIVE ADVERTISING (YEAR)

PERCENTAGE OF
ORGANIZATIONS FOUND
WITH APPS THAT ACCESS
HIGH-RISK DATA

63

54.6

46

YEAR

2016

2017

2018

RATIO

1 in 1.6

1 in 1.8

1 in 2.2

CHANGE (PP)

-8.4

-8.6

PERCENTAGE OF
ORGANIZATIONS
FOUND WITH APPS
THAT USE INVASIVE
ADVERTISING

19.4

30.5

26.4

YEAR

2016

2017

2018

RATIO

1 in 5.2

1 in 3.3

1 in 3.8

CHANGE (PP)

11.1

-4.1

There was a marked increase in the
number of ransomware infections
on mobile devices during 2018, up
by a third when compared to 2017.

PERCENTAGE OF ORGANIZATIONS AFFECTED BY APPS THAT
CONTAIN HARD CODED CREDENTIALS (YEAR)

PERCENTAGE OF
ORGANIZATIONS FOUND
WITH APPS THAT
HAVE HARD-CODED
CREDENTIALS

47.3

42.9

34.3

YEAR

2016

2017

2018

RATIO

1 in 2.1

1 in 2.3

1 in 2.9

CHANGE (PP)

-4.4

-8.6

PERCENTAGE OF ORGANIZATIONS AFFECTED BY APPS THAT
USE HOT PATCHING (YEAR)

PERCENTAGE OF
ORGANIZATIONS FOUND
WITH APPS THAT USE
HOT-PATCHING

31.3

11.7

6.8

YEAR

2016

2017

2018

RATIO

1 in 3.2

1 in 8.5

1 in 14.7

CHANGE (PP)

-19.6

-4.9

TOP COUNTRIES FOR MOBILE RANSOMWARE (YEAR)

TOP MOBILE RANSOMWARE (YEAR)

Germany
10.4%

China 13.4%

USA 63.2%

Japan 3.4%

India 2.4%

Canada 1.5%

UK 0.8%

Norway 0.6%

Netherlands 0.6%

Austria  0.6%

Other 3.1%

THREAT NAME

Simplocker

Lockdroid.E

LockScreen

Simplocker.B

Ransomware

Ransomeware

Lockdroid.F

Android.WannaLocker

WannaLocker

Lockdroid.G

PERCENT

59.3

26.2

7.1

2.8

2.7

1.0

0.7

<0.1

<0.1

<0.1

Back to ToC

Facts and Figures  45

ISTR 24 | February 2019NUMBER OF MOBILE MALWARE BLOCKED (MONTH)

NUMBER OF MOBILE RANSOMWARE BLOCKED (MONTH)

12K

10K

8K

6K

4K

2K

0

400

350

300

250

200

150

100

50

0

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

Malware per month

Ransomware per day

While the annual total of mobile malware infections
fell in 2018, infection numbers began to climb upwards
again during the fourth quarter of the year.

Back to ToC

Facts and Figures  46

ISTR 24 | February 2019WEB ATTACKS

In 2018, 1 in 10 URLs analyzed were identified as being malicious, up from 1 in 16 in
2017. Additionally, despite a drop off in exploit kit activity, overall web attacks on
endpoints increased by 56 percent in 2018. By December, Symantec was blocking
more than 1.3 million unique web attacks on endpoint machines every day.

Formjacking was one of the biggest cyber security trends of the year, with an
average of 4,800 websites compromised with formjacking code every month in 2018.
Formjacking is the use of malicious JavaScript code to steal payment card details
and other information from payment
forms on the checkout web pages of
eCommerce sites, and in total Symantec
blocked 3.7 million formjacking attempts
on endpoint devices in 2018. More than
a third of formjacking activity took place
in the last quarter of 2018, with 1.36
million formjacking attempts blocked in
that period alone.

1,122,229
2nd QTR

697,187
1st QTR

FORMJACKING BY QTR

FORMJACKING BY MONTH

FORMJACKING ACTIVITY
More than a third of the formjacking activity
took place in the last quarter of 2018.

1,362,990
4th QTR

1,400,000

1,200,000

1,000,000

800,000

600,000

400,000

200,000

551,117
3rd QTR

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

WEB ATTACKS (YEAR)

TOP COMPROMISED WEBSITE CATEGORIES (YEAR)

PHISHING URLS (YEAR)

TOTAL WEB ATTACKS BLOCKED

AVERAGE WEB ATTACKS BLOCKED PER DAY

348,136,985

953,800

DOMAIN CATEGORIES

2017 (%)

2018 (%)

PERCENTAGE POINT
DIFFERENCE

WEB ATTACKS (MONTH)

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

Web attacks per month

WEB ATTACKS (DAY)

50M

40M

30M

20M

10M

0

1.5M

1.2M

900K

600K

300K

0

Dynamic DNS

Gambling

Hosting

Technology

Shopping

Business

Pornography

Health

Educational

Content Delivery
Network

15.7

7.9

8.2

13.6

4.6

9.0

3.2

5.7

3.7

2.1

MALICIOUS URLS (YEAR)

16.6

16.3

8.7

8.1

8.1

7.2

5.2

4.5

3.9

2.6

0.8

8.4

0.5

-5.5

3.6

-1.7

2.1

-1.2

0.2

0.6

YEAR

2017

2018

PERCENT OF TOTAL

6.4

9.9

RATIO

1 in 16

1 in 10

PERCENTAGE POINT
CHANGE

3.4

YEAR

2017

2018

PERCENT OF
ALL URLS

0.4

0.6

RATIO

1 in 235

1 in 170

PERCENT OF
MALICIOUS
URLS

6.6

5.9

RATIO

1 in 15

1 in 17

PERCENTAGE
CHANGE

PERCENTAGE
POINT CHANGE

38.1

0.2

FORMJACKING ATTACKS (YEAR)

YEAR

2018

FORMJACKING ATTACKS

3,733,523

FORMJACKING ATTACKS (MONTH)

600K

500K

400K

300K

200K

100K

0

BOTNET URLS (YEAR)

YEAR

2017

2018

PERCENT OF
ALL URLS

1.2

1.8

RATIO

1 in 85

1 in 54

PERCENT OF
MALICIOUS
URLS

18.2

18.7

RATIO

1 in 5

1 in 5

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

PERCENTAGE
CHANGE

PERCENTAGE
POINT CHANGE

Formjacking attacks

57.6

0.7

AVERAGE FORMJACKING WEBSITES (MONTH)

Jan

Feb

Mar

Apr

May

Jun

Jul

Aug

Sep

Oct

Nov

Dec

Web attacks per day

YEAR

2018

AVERAGE WEBSITES EACH MONTH

4,818

Back to ToC

Facts and Figures  48

ISTR 24 | February 20192015-2017: AVG 42 ORGS TARGETED PER GROUP
(20 MOST ACTIVE GROUPS)

ESPIONAGE INDICTMENTS BY U.S. AUTHORITIES

TARGETED ATTACKS

While the overall number of targeted attacks was down somewhat last year, the most
active groups stepped up their activity, attacking an average of 55 organizations
over the past three years, up from 42 between 2015 and 2017. Spear-phishing emails
remained the most popular avenue for attack and were used by 65 percent of all
known groups. The most likely reason for an organization to experience a targeted
attack was intelligence gathering, which is the motive for 96 percent of groups.

Alongside the rise in popularity of living off the land tactics, the use of zero-day
vulnerabilities declined in 2018, with only 23 percent of groups known to have
exploited zero days, down from 27 percent in 2017. While still a niche area, the use
of destructive malware continued to grow. Eight percent of groups were known to
use destructive tools, a 25 percent increase over 2017.

SPEAR PHISHING

INTELLIGENCE GATHERING

2016-2018: AVG 55 ORGS TARGETED PER GROUP
(20 MOST ACTIVE GROUPS)

65%

of groups used spear
phishing as the primary
infection vector

96%

of groups’ primary
motivation continues to be
intelligence gathering

5

2016

23%
Groups using
zero-day
vulnerabilities

8%
Groups using
destructive
malware

4

2017

49

19

CHINA

18

RUSSIA

11

IRAN

1
NORTH KOREA

2018

TARGETED ATTACK GROUPS KNOWN (YEAR)

TARGETED ATTACK GROUP MOTIVES (ALL TIME)

137

155

116

200

150

100

50

0

6%

10%

96%

100%

80%

60%

40%

20%

0

The most likely reason for an
organization to experience a
targeted attack was intelligence
gathering, which is the motive for
96 percent of groups.

2016

2017

2018

Financial

Disruption

Intelligence

Total known groups

Percentage of groups

TARGETED ATTACK GROUPS EXPOSED BY SYMANTEC (YEAR)
8

MOTIVES PER TARGETED ATTACK GROUP (ALL TIME)

89%

100%

7

6

5

4

3

2

1

0

1%

3

Motives per group

10%

2

1

80%

60%

40%

20%

0

2009

2010

2011

2012

2013

2014

2015

2016

2017

2018

Number of groups

Back to ToC

Facts and Figures  50

ISTR 24 | February 2019Spear-phishing emails remained
the most popular avenue for attack
and were used by 65 percent of all
known groups.

TARGETED ATTACK GROUP INFECTION VECTORS (ALL TIME)

65%

23%

1%

2%

5%

Data storage
devices

Web server
exploits

Trojanized software
updates

Watering hole
websites

Spear phishing
emails

Percentage of groups

INFECTION VECTORS PER TARGETED ATTACK GROUP
(ALL TIME)

54%

27%

15%

4%

80%

70%

60%

50%

40%

30%

20%

10%

0

60%

50%

40%

30%

20%

10%

0

TOP COUNTRIES AFFECTED BY TARGETED ATTACK GROUPS
(2016-2018)

COUNTRY

USA

India

Japan

China

Turkey

Saudi Arabia

South Korea

Taiwan

UAE

Pakistan

ATTACKS

255

128

69

44

43

42

40

37

30

28

NUMBER OF ORGANIZATIONS AFFECTED BY TARGETED
ATTACKS (YEAR)

582

455

388

2016

2017

2018

600

500

400

300

200

100

0

No known vector(s)

One vector

Two vectors

Three vectors

Organizations

Percentage of groups

Back to ToC

Facts and Figures  51

ISTR 24 | February 2019NUMBER OF TOOLS USED BY THE 20 MOST ACTIVE GROUPS
(2016-2018)

PERCENTAGE OF GROUPS KNOWN TO USE ZERO-DAY
VULNERABILITIES (ALL TIME)

TOTAL INDICTMENTS BY U.S. AUTHORITIES (YEAR)

MINIMUM

1

MAXIMUM

18

AVERAGE

5

23%

77%

AVERAGE NUMBER OF ORGANIZATIONS TARGETED BY THE 20
MOST ACTIVE GROUPS (2016-2018)

2016-2018

55

No

Yes

49

2018

5

2016

Number Indicted

4

2017

60

50

40

30

20

10

0

While still a niche area, the use of
destructive malware continued to
grow. Eight percent of groups were
known to use destructive tools, up
from 6 percent at the end of 2017.

PERCENTAGE OF GROUPS KNOWN TO USE DESTRUCTIVE
MALWARE (ALL TIME)

INDICTMENTS BY U.S. AUTHORITIES BY COUNTRY (YEAR)

8%

92%

50

40

30

20

10

0

No

Yes

2016

2017

2018

Russia

Syria

Iran

China

North Korea

Back to ToC

Facts and Figures  52

ISTR 24 | February 2019IOT

After a massive increase in Internet of Things (IoT)
attacks in 2017, attack numbers stabilized in 2018,
when the number of attacks averaged 5,200 per
month against Symantec’s IoT honeypot. Routers
and connected cameras were by far the main source
of IoT attacks, accounting for over 90 percent of all
attacks on the honeypot. The proportion of infected
cameras used in attacks increased considerably
during 2018. Connected cameras accounted for 15
percent of attacks, up from 3.5 percent in 2017.
Attackers were also increasingly focused on Telnet
as an avenue for attack. Telnet accounted for over 90
percent of attempted attacks in 2018, a jump from
50 percent in 2017.

ATTACKS INVOLVING CONNECTED CAMERAS UP FROM 3.5% IN 2017 TO 15% IN 2018
ROUTERS AND CONNECTED CAMERAS
WERE THE MAIN SOURCE OF IOT ATTACKS
ACCOUNTING FOR OVER
90 PERCENT

OF ACTIVITY.

IOT DEVICES EXPERIENCE AN AVERAGE OF 5,200 ATTACKS PER MONTH

The notorious Mirai distributed
denial of service (DDoS) worm
remained an active threat and,
with 16 percent of the attacks, was
the third most common IoT threat
in 2018.

TOP SOURCE COUNTRIES FOR IOT ATTACKS (YEAR)

TOP PASSWORDS USED IN IOT ATTACKS (YEAR)

COUNTRY

China

USA

Brazil

Russia

Mexico

Japan

Vietnam

South Korea

Turkey

Italy

PERCENT

24.0

10.1

9.8

5.7

4.0

3.7

3.5

3.2

2.6

1.9

PASSWORDS

123456

[BLANK]

system

sh

shell

admin

1234

password

enable

12345

TOP USER NAMES USED IN IOT ATTACKS (YEAR)

TOP IOT THREATS (YEAR)

USER NAME

root

admin

enable

shell

sh

[BLANK]

system

enable

>/var/tmp/.ptmx && cd /var/tmp/

>/var/.ptmx && cd /var/

PERCENT

38.1

22.8

4.5

4.2

1.9

1.7

1.1

0.9

0.9

0.9

THREAT NAME

Linux.Lightaidra

Linux.Kaiten

Linux.Mirai

Trojan.Gen.2

Downloader.Trojan

Trojan.Gen.NPE

Linux.Mirai!g1

Linux.Gafgyt

Linux.Amnesiark

Trojan.Gen.NPE.2

PERCENT

24.6

17.0

4.3

4.0

1.9

1.3

1.0

1.0

1.0

0.9

PERCENT

31.3

31.0

15.9

8.5

3.2

2.8

1.9

1.7

1.1

0.8

Back to ToC

Facts and Figures  54

ISTR 24 | February 2019Routers and connected cameras
were the most infected devices and
accounted for 75 and 15 percent of
the attacks respectively.

TOP PROTOCOLS ATTACKED BY IOT THREATS (YEAR)

TOP DEVICE TYPES PERFORMING IOT ATTACKS (YEAR)

TARGETED SERVICE

telnet

http

https

smb

ssh

ftp

snmp

cwmp

upnp

modbus

PERCENT

90.9

6.6

1.0

0.8

0.6

<0.1

<0.1

<0.1

<0.1

<0.1

DEVICE TYPE

Router

Connected Camera

Multi Media Device

Firewall

PBX Phone System

NAS (Network Attached Storage)

VoIP phone

Printer

Alarm System

VoIP Adapter

PERCENT

75.2

15.2

5.4

2.1

0.6

0.6

0.2

0.2

0.2

0.1

TOP PORTS ATTACKED BY IOT THREATS (YEAR)

ATTACKS AGAINST IOT DEVICES (YEAR)

TCP PORT NUMBER

23

80

2323

443

445

22

8080

2223

2222

21

DESCRIPTION

Telnet

World Wide Web HTTP

Telnet (alternate)

HTTP over TLS/SSL

Microsoft Directory Services

Secure Shell (SSH) Protocol

HTTP (alternate)

Rockwell CSP2

Secure Shell (SSH) Protocol (alternate)

File Transfer Protocol [Control]

PERCENT

85.0

6.5

5.8

1.0

0.8

0.6

0.1

<0.1

<0.1

<0.1

YEAR

2017

2018

TOTAL ATTACKS

PERCENT CHANGE

57,691

57,553

-0.2

AVERAGE ATTACKS AGAINST IOT DEVICES (MONTH)

PER MONTH

5,233

Back to ToC

Facts and Figures  55

ISTR 24 | February 2019UNDERGROUND ECONOMY

ACCOUNTS

Restaurant gift cards

15–40% of value

Online retailer gift cards

15–50% of value

Online banking accounts (depending on value & verification)

0.5%–10% of value

Socks proxy account

$0.10–2

Video and music streaming accounts

$0.10–10

Cloud service account

$5–10

Gaming platform account

$0.50–12

Hacked email accounts (2,500)

VPN services

$1–15

$1–20

Hotel loyalty (reward program accounts with 100,000 points)

$10–20

Various services (more than 120+ different accounts)

$0.50–25

RDP login credentials

$3–30

Retail shopping account

$0.50–99

Online payment accounts (depending on value & verification)

$1–100

IDENTITIES

Stolen or fake identity (name, SSN, and DOB)

$0.10–1.50

Medical notes and prescriptions

Mobile phone online account

$15–20

$15–25

Stolen medical records

$0.10–35

ID/passport scans or templates

$1–35

Scanned documents (utility bill, etc.)

$0.50–45

Full ID packages (name, address, phone, SSN, email, bank account, etc.)

$30–100

0

10

20

30

40

50

60

70

80

90

100

110

120

UNDERGROUND ECONOMY

IDENTITIES (CONT.)

Fake health care ID cards

Parcel drop off box for deliveries

$50–220

$70–240

Fake ID, driver license, passport, etc.

$25–5,000

MONEY TRANSFER SERVICES

Cash redirector service for bank accounts

.1–15% of value

Cash redirector service for online payment system

1–5% of value

Pay $100 in Bitcoin and get a money transfer of $1000

$100

Cash redirector service

5–20% of value

MALWARE

Office macro downloader generator

$5–10

DDoS bot software

$1–15

Spyware

Cryptocurrency stealer malware

$3–50

$4–60

Cryptocurrency miner (e.g. Monero)

$10–200

Ransomware toolkit

$0–250

Common banking Trojans toolkit with support

$10–1,500

0

0

10

100

20

200

30

300

40

1000

50

1500

60

2000

70

2500

80

3000

90

3500

100

4000

110

4500

120

5000

UNDERGROUND ECONOMY

SERVICES

Airline ticket and hotel bookings

10% of value

Money laundering service (into cash or cryptocurrencies)

4–40%

Cash out service (bank account, ATM card, and fake ID)

$350

Hacker for hire

$100+

Custom phishing page service

DDoS service, short duration <1 hour (medium protected targets)

$3–12

$5–20

DDoS service, duration >24h (medium and strong protected targets)

$10–1,000

PAYMENT CARDS

Single credit card

$0.50–20

Single credit card with full details (fullz)

$1–45

Dump of magnetic strip track 1/2 data (e.g. from skimming)

$5–60

SOCIAL MEDIA

100 likes on social media platforms

$0.10–3

500 social media followers

$2–6

100,000 social media video views

$200–250

These prices are taken from publicly accessible underground forums
and dark web TOR sites. Closed, private forums tend to have even
lower prices. We cannot verify if the goods are genuinely sold for the
asked price, some of them might be fake offers.

0

0

10

100

20

200

30

300

40

1000

50

1500

60

2000

70

2500

80

3000

90

3500

100

4000

110

4500

120

5000

Symantec has established the largest civilian threat collection
network in the world, and one of the most comprehensive
collections of cyber security threat intelligence, through the
Symantec Global Intelligence Network (GIN).

The Symantec GIN comprises more than 123 million attack
sensors, recording thousands of threat events per second,
and contains over 9 petabytes of security threat data. This
network also monitors threat activities for over 300,000
businesses and organizations worldwide that depend on
Symantec for protection. Telemetry from across Symantec’s
threat protection portfolio helps our 3,800 cyber security
researchers and engineers identify the top trends shaping the
threat landscape.

Analyses of spam, phishing, and email malware trends
are gathered from a variety of Symantec email security
technologies processing more than 2.4 billion emails each day,
including: Symantec Messaging Gateway for Service Providers,
Symantec Email Security.cloud, Symantec Advanced Threat
Protection for Email, Symantec’s CloudSOC™ Service, and the
Symantec Probe Network. Symantec also gathers phishing
information through an extensive anti-fraud community of
enterprises, security vendors, and partners.

Filtering more than 322 million emails, and over 1.5 billion
web requests each day, Symantec’s proprietary Skeptic™
technology underlies the Symantec Email and Web Security.
cloud™ services, utilizing advanced machine learning,
network traffic analysis, and behavior analysis to detect
even the most stealthy and persistent threats. Additionally,
Symantec’s Advanced Threat Protection for Email uncovers
advanced email attacks by adding cloud-based sandboxing,
additional spear-phishing protection, and unique targeted
attack identification capabilities.

Billions of URLs are processed and analyzed each month
by Symantec’s Secure Web Gateway solutions, including
ProxySG™, Advanced Secure Gateway (ASG), and Web
Security Solution (WSS), all powered by our real-time
WebPulse Collaborative Defense technology and Content
Analysis System, identifying and protecting against malicious
payloads and controlling sensitive web-based content.

Mobile threat intelligence, provided by Symantec Endpoint
Protection Mobile (SEPM), is used to predict, detect, and
protect against the broadest range of existing and unknown
threats. SEPM’s predictive technology uses a layered
approach that leverages massive crowdsourced threat
intelligence, in addition to both device-based and server-
based analysis, to proactively protect mobile devices from
malware, network threats, and app and OS vulnerability
exploits. Additionally, mobile technology from Appthority,
coupled with SEPM, offers the ability to analyze mobile apps
for both malicious capabilities and unsafe and unwanted
behaviors, such as vulnerabilities, risk of sensitive data loss,
and privacy-invasive actions.

These resources give Symantec analysts unrivaled sources
of data with which to identify, analyze, and provide informed
commentary on emerging trends in cyber attacks, malicious
code activity, phishing, and spam. The result is the annual
Symantec Internet Security Threat Report™, which gives
enterprises, small businesses, and consumers essential
information to help secure their systems effectively now
and into the future.

Back to ToC

Mehodology  59

ISTR 24 | February 2019CREDITS

Team

Brigid O’Gorman

Candid Wueest

Dick O’Brien

Gillian Cleary

Hon Lau

John-Paul Power

Mayee Corpin

Orla Cox

Paul Wood

Scott Wallace

Contributors

Alan Neville

Alex Shehk

Brian Duckering

Chris Larsen

Christian Tripputi

Dennis Tan

Gavin O’Gorman

Parveen Vashishtha

Pierre-Antoine Vervier

Pravin Bange

Robert Keith

Sean Kiernan

Sebastian Zatorski

Seth Hardy

Shashank Srivastava

Shaun Aimoto

Siddhesh Chandrayan

Tor Skaar

Tyler Anderson

Yun Shen

Symantec Corporation
World Headquarters
350 Ellis Street
Mountain View, CA 94043
United Stated of America

For specific country offices
and contact numbers, please
visit our website. For product
information in the U.S., call
toll-free 1 (800) 745 6054.

+1 650 527– 8000
+1 800 721–3934

Symantec.com

Copyright © 2019
Symantec Corporation.

All rights reserved.
Symantec, the Symantec
Logo, and the Checkmark
Logo are trademarks or
registered trademarks of
Symantec Corporation or
its affiliates in the U.S. and
other countries. Other names
may be trademarks of their
respective owners.

02/19


