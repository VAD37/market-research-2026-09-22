# SEC EDGAR full-text search — GEO / AEO / AI-visibility / AI-search terms in 2026 filings, filer lists; opened exhibits from multi-location filers (The Joint Corp, Hyatt, IHG, Yelp, 1-800-Flowers, Yext); headcounts and location counts from 10-Ks (The Joint Corp, Choice Hotels, Walgreens Boots Alliance, Yext, Hyatt)

```yaml
source:          SEC EDGAR full-text search API (efts.sec.gov), hit lists as returned; filing documents from sec.gov/Archives; filer metadata from data.sec.gov/submissions
url_or_doc_id:   https://efts.sec.gov/LATEST/search-index?q=<phrase>&dateRange=custom&startdt=2026-01-01&enddt=2026-09-23&forms=10-K,10-Q,8-K,20-F,6-K ; documents listed per section below
published:       filing dates as listed
pull_date:       2026-09-23
pull_method:     fetch (python urllib, User-Agent "market-research-bot contact: research@example.invalid"); document text stripped of HTML by script; excerpts located by regex on engine and category terms
pull_purpose:    evidence about a number
tier:            2
tier_reason:     filed — 8-K exhibits, 10-K, 6-K text as filed; the FTS hit lists are EDGAR's own index (tier 2 on existence of the phrase in the filing); the Corporate Ink survey figures quoted inside the Yext exhibit are a vendor relay, tier 5
source_label:    filed
lane:            F
sub_market:      organic recommendation (agentic commerce where the excerpt says so)
engine:          as named per excerpt
metric_kind:     none
supersedes:      none — extends docs/raw/e-edgar-fulltext-repull-2026-09-23.md and f-edgar-fts-budget-line-queries-2026-09-23.md with the local / multi-location cut
captured:        FTS hit lists (up to 40 rows per query); regex-located excerpts (±220–480 characters) from opened documents; headcount and location sentences
verbatim:        full for hit-list fields and excerpts; excerpt boundaries are the extraction window, marked "…"
```

## FTS hit lists — `forms=10-K,10-Q,8-K,20-F,6-K`, 2026-01-01 to 2026-09-23

### `"generative engine optimization"` — total 20

| file_date | form | display_names | _id |
|---|---|---|---|
| 2026-07-21 | 8-K | Change Agents Corporation. (ALBT) (CIK 0001630212) | 0001213900-26-079830:ea029857301ex99-1.htm |
| 2026-08-12 | 8-K | Direct Digital Holdings, Inc. (DRCT) (CIK 0001880613) | 0001880613-26-000095:drct-earningsreleaseq226xe.htm |
| 2026-05-07 | 8-K | TechTarget, Inc. (TTGT) (CIK 0002018064) | 0001193125-26-211953:ttgt-ex99_1.htm |
| 2026-08-14 | 10-Q | Change Agents Corporation. (CHGA) (CIK 0001630212) | 0001213900-26-090229:ea0301266-10q_change.htm |
| 2026-03-31 | 10-K | Onfolio Holdings, Inc (ONFO, ONFOP, ONFOW) (CIK 0001825452) | 0001654954-26-003083:onfo_10k.htm |
| 2026-09-22 | 10-Q | ADOBE INC. (ADBE) (CIK 0000796343) | 0000796343-26-000156:adbe-20260828.htm |
| 2026-06-15 | 10-Q | ADOBE INC. (ADBE) (CIK 0000796343) | 0000796343-26-000112:adbe-20260529.htm |
| 2026-04-27 | 10-K | Glidelogic Corp. (GDLG) (CIK 0001848672) | 0001096906-26-000615:gdlg-20260131_10k.htm |
| 2026-03-02 | 10-K | SEMrush Holdings, Inc. (SEMR) (CIK 0001831840) | 0001628280-26-013259:semr-20251231.htm |
| 2026-03-17 | 10-K | INTELLIGENT PROTECTION MANAGEMENT CORP. (IPM) (CIK 0001355839) | 0001213900-26-029095:ea0277611-10k_intelligent.htm |
| 2026-03-03 | 10-K | Upland Software, Inc. (UPLD) (CIK 0001505155) | 0001505155-26-000007:upld-20251231.htm |
| 2026-01-15 | 10-K | ADOBE INC. (ADBE) (CIK 0000796343) | 0000796343-26-000003:adbe-20251128.htm |
| 2026-04-03 | 10-K | OOMA INC (OOMA) (CIK 0001327688) | 0001327688-26-000009:ooma-20260131.htm |
| 2026-02-25 | 10-K | Zeta Global Holdings Corp. (ZETA) (CIK 0001851003) | 0001193125-26-068598:zeta-20251231.htm |
| 2026-03-11 | 10-K | TechTarget, Inc. (TTGT) (CIK 0002018064) | 0001193125-26-102183:ttgt-20251231.htm |
| 2026-09-09 | 10-K | INTUIT INC. (INTU) (CIK 0000896878) | 0000896878-26-000037:intu-20260731.htm |
| 2026-02-25 | 10-K | Fastly, Inc. (FSLY) (CIK 0001517413) | 0001517413-26-000053:fsly-20251231.htm |
| 2026-02-27 | 10-K | Primerica, Inc. (PRI) (CIK 0001475922) | 0001193125-26-082233:pri-20251231.htm |
| 2026-03-12 | 20-F | Fiverr International Ltd. (FVRR) (CIK 0001762301) | 0001178913-26-000858:zk2634486.htm |
| 2026-08-20 | 10-K | COTY INC. (COTY) (CIK 0001024305) | 0001024305-26-000048:coty-20260630.htm |

### `"answer engine optimization"` — total 9

| file_date | form | display_names | _id |
|---|---|---|---|
| 2026-06-05 | 6-K | REZOLVE AI PLC (RZLV, RZLVW) (CIK 0001920294) | 0001193125-26-259945:rzlv-ex99_1.htm |
| 2026-07-01 | 6-K | Locafy Ltd (LCFY, LCFYW) (CIK 0001875547) | 0001493152-26-031582:ex99-1.htm |
| 2026-04-14 | 8-K | Rent the Runway, Inc. (RENT) (CIK 0001468327) | 0001468327-26-000018:fy2025earningsrelease.htm |
| 2026-06-02 | 8-K | Yext, Inc. (YEXT) (CIK 0001614178) | 0001628280-26-039786:ex992q1fy27shareholderlett.htm |
| 2026-02-11 | 10-K | HUBSPOT INC (HUBS) (CIK 0001404655) | 0001193125-26-046646:hubs-20251231.htm |
| 2026-03-20 | 10-K | DULUTH HOLDINGS INC. (DLTH) (CIK 0001649744) | 0001193125-26-117508:dlth-20260201.htm |
| 2026-04-14 | 10-K | Rent the Runway, Inc. (RENT) (CIK 0001468327) | 0001468327-26-000020:wdq-20260131.htm |
| 2026-03-02 | 10-K | SEMrush Holdings, Inc. (SEMR) (CIK 0001831840) | 0001628280-26-013259:semr-20251231.htm |
| 2026-03-02 | 20-F | SIMILARWEB LTD. (SMWB) (CIK 0001842731) | 0001842731-26-000018:smwb-20251231.htm |

### `"AI visibility"` — total 21

| file_date | form | display_names | _id |
|---|---|---|---|
| 2026-09-01 | 8-K | Yext, Inc. (YEXT) (CIK 0001614178) | 0001628280-26-059706:ex993q2fy27productupdatepr.htm |
| 2026-08-06 | 8-K | TechTarget, Inc. (TTGT) (CIK 0002018064) | 0001193125-26-338041:ttgt-ex99_1.htm |
| 2026-06-05 | 6-K | REZOLVE AI PLC (RZLV, RZLVW) (CIK 0001920294) | 0001193125-26-259945:rzlv-ex99_1.htm |
| 2026-05-07 | 8-K | JOINT Corp (JYNT) (CIK 0001612630) | 0001612630-26-000048:jyntq12026resultsdeck-fi.htm |
| 2026-08-06 | 8-K | JOINT Corp (JYNT) (CIK 0001612630) | 0001612630-26-000063:a8-05x26q22026resultsdec.htm |
| 2026-09-01 | 8-K | Yext, Inc. (YEXT) (CIK 0001614178) | 0001628280-26-059706:ex992q2fy27shareholderlett.htm |
| 2026-03-11 | 8-K | Netskope Inc (NTSK) (CIK 0002063196) | 0001193125-26-102142:ck0002063196-ex99_1.htm |
| 2026-05-07 | 8-K | TechTarget, Inc. (TTGT) (CIK 0002018064) | 0001193125-26-211953:ttgt-ex99_1.htm |
| 2026-08-10 | 8-K | N-able, Inc. (NABL) (CIK 0001834488) | 0001834488-26-000044:nabl-20260630x8kxex991.htm |
| 2026-02-19 | 10-K | Amplitude, Inc. (AMPL) (CIK 0001866692) | 0001193125-26-057847:ampl-20251231.htm |
| 2026-06-02 | 8-K | Yext, Inc. (YEXT) (CIK 0001614178) | 0001628280-26-039786:ex992q1fy27shareholderlett.htm |
| 2026-03-09 | 8-K | Yext, Inc. (YEXT) (CIK 0001614178) | 0001628280-26-016005:ex992q4fy26shareholderlett.htm |
| 2026-05-07 | 10-Q | Amplitude, Inc. (AMPL) (CIK 0001866692) | 0001193125-26-209631:ampl-20260331.htm |
| 2026-08-06 | 10-Q | Amplitude, Inc. (AMPL) (CIK 0001866692) | 0001193125-26-335706:ampl-20260630.htm |
| 2026-03-02 | 10-K | SEMrush Holdings, Inc. (SEMR) (CIK 0001831840) | 0001628280-26-013259:semr-20251231.htm |
| 2026-08-14 | 10-Q | Change Agents Corporation. (CHGA) (CIK 0001630212) | 0001213900-26-090229:ea0301266-10q_change.htm |
| 2026-07-30 | 10-Q | Fortinet, Inc. (FTNT) (CIK 0001262039) | 0001262039-26-000021:ftnt-20260630.htm |
| 2026-03-31 | 10-K | Onfolio Holdings, Inc (ONFO, ONFOP, ONFOW) (CIK 0001825452) | 0001654954-26-003083:onfo_10k.htm |
| 2026-03-26 | 10-K | COMSCORE, INC. (SCOR) (CIK 0001158172) | 0001158172-26-000009:scor-20251231.htm |
| 2026-03-31 | 10-K | Netskope Inc (NTSK) (CIK 0002063196) | 0001193125-26-135011:ck0002063196-20260131.htm |
| 2026-03-02 | 20-F | SIMILARWEB LTD. (SMWB) (CIK 0001842731) | 0001842731-26-000018:smwb-20251231.htm |

### `"AI search" franchise` — total 18 (word match, not phrase-adjacent)

VisitIQ Corp. 10-K 2026-05-20; INTERCONTINENTAL HOTELS GROUP PLC 6-K 2026-08-11 (0001654954-26-007436:a0528q.htm) and 6-K 2026-02-17; DiamondRock Hospitality Co 10-K 2026-02-27; 1 800 FLOWERS COM INC 10-K 2026-09-11 (0001084869-26-000029:flws-20260628.htm); HOST HOTELS & RESORTS 10-K 2026-02-25; Athena Technology Acquisition Corp. II 10-K 2026-03-11; URBAN ONE 10-K 2026-03-20; Elastic N.V. 10-K 2026-06-08; Upland Software 10-K 2026-03-03; Walmart Inc. 10-K 2026-03-13; NatWest Group plc 20-F 2026-02-17 and 6-K 2026-02-13; YELP INC 10-K 2026-02-27 (0001345016-26-000019:yelp-20251231.htm); RENTOKIL INITIAL PLC 20-F 2026-03-25 and 6-K 2026-03-25; Trump Media & Technology Group 10-K 2026-02-27; MakeMyTrip Ltd 20-F 2026-07-27.

### `"AI search" restaurants` — HTTP 500 from efts.sec.gov (one attempt, not retried).

### `"ChatGPT" franchisees` — total 4

Hyatt Hotels Corp 8-K 2026-05-28 (0001104659-26-067209:tm2615108d1_ex99-1.htm); Hyatt Hotels Corp 10-K 2026-02-13 (0001468174-26-000007:h-20251231.htm); WW INTERNATIONAL, INC. 8-K 2026-03-16; PVH CORP. 10-K 2026-03-31.

## Opened documents — excerpts

### The Joint Corp (NASDAQ: JYNT), 8-K exhibit, Q1 2026 results deck, filed 2026-05-07 — https://www.sec.gov/Archives/edgar/data/1612630/000161263026000048/jyntq12026resultsdeck-fi.htm

> "…nd helping patients get back to what they love to do • National Marketing: began high-impact media program in November 2025 which is helping drive monthly sequential improvement in active member growth • Ongoing SEO and AI visibility optimization • New Sales Initiatives • Minimum term commitment on plans changed from 2 to 3 months • New flexible plans • B2B partnership program • Began nationwide rollout of Care Credit Program • Rolled out enhanced pricing structure in approximately 300 clinics w…"

### The Joint Corp, 8-K exhibit, Q2 2026 results deck, filed 2026-08-06 — https://www.sec.gov/Archives/edgar/data/1612630/000161263026000063/a8-05x26q22026resultsdec.htm

> "…practic care for pain relief, and helping patients get back to what they love to do • Sequential improvement in active member growth each month this year • Increasing focus on our MVPs (most valuable patients) • SEO and AI visibility optimization driving organic traffic and lead quality • Positive trends in traffic and high-intent actions on local clinic microsites • New and expanded flexible membership plan options • Rolled out optimized pricing in over 500 clinics 9NASDAQ: JYNT | © 2026 The Jo…"

[note: no engine named in either deck; no dollar figure attached to "AI visibility optimization".]

### The Joint Corp, 10-K FY2025, filed 2026-03-13 — https://www.sec.gov/Archives/edgar/data/1612630/000161263026000022/jynt-20251231.htm

> "Workforce As of December 31, 2025, we and our consolidated VIEs employed approximately 202 persons on a full-time basis and approximately 128 persons on a part-time basis."
> "As of December 31, 2025, our franchisees owned or managed 885 clinics, and we owned or managed 75 clinics."
> "We are the largest chiropractic franchisor in the United States with over 960 clinics operating across the United States."
> "We are focused on growing our franchise business through the strategic divestitures of all of our company-owned or managed clinics."

### Hyatt Hotels Corp, 10-K FY2025, filed 2026-02-13 — https://www.sec.gov/Archives/edgar/data/1468174/000146817426000007/h-20251231.htm

> "…t-term rental of homes and apartments from their owners, thereby providing an alternative to hotel rooms, such as Airbnb and Vrbo. Companies or websites that provide generative AI services and recommendations, including large language models ("LLMs") like ChatGPT, Claude, Gemini, Grok, and others, represent an additional source of competition because they may currently or in the future serve as alternative distribution channels. The hospitality industry has experienced significant consolidation,…"
> "… digital platforms, loss of development opportunities, or reduced colleague retention and increased recruiting difficulties. In addition, the increasing prevalence and adoption of generative AI tools and LLMs, including ChatGPT, Claude, Gemini, Grok, and others, means that information about Hyatt, our brands, and our properties can be accessed quickly and easily. The manner in which these AI tools decide what information to provide in response to a given user query may also result in our propert…"
> "Employees At December 31, 2025, we had approximately 242,000 colleagues working at our corporate and regional offices, our managed,"

### Hyatt Hotels Corp, 8-K exhibit 99.1, Investor Day 2026 deck, filed 2026-05-28 — https://www.sec.gov/Archives/edgar/data/1468174/000110465926067209/tm2615108d1_ex99-1.htm

> "…H ENGINE Scaled Through Technology Augments and accelerates performance and growth 3 47 INVESTOR DAY 2026 TECHNOLOGY AS A GROWTH MULTIPLIER Smarter Decisions Hotel Heartbeat Deeper Guest Engagement Intent-based search & ChatGPT AI RFP Tool Scalable Platform Core Technology – CRS, RMS, PMS INVESTOR DAY 2026 48…"

### InterContinental Hotels Group PLC, 6-K half-year results, filed 2026-08-11 — https://www.sec.gov/Archives/edgar/data/858446/000165495426007436/a0528q.htm

> "…l IHG booking websites, making it easier and faster for hotel owners to create and update compelling content to showcase their properties using AI. This includes machine translation into multiple languages and optimised AI search of structured content, new media types such as video, 360 images, floor plans and virtual tours, and enriched information on the properties and nearby attractions. o A new Customer Relationship Management (CRM) platform is also in development this year to help deepen lo…"
> "…o In July we launched conversational search across our websites and app to allow travellers to describe in their own words what they are looking for. Similarly, our ChatGPT plug-in recommends IHG hotels based on travellers' preferences, surfacing real-time availability, pricing, interactive maps and amenities, helping guests move naturally from discovery to comparison and onward to IHG's direct booking channels. IHG is also participating in Google's Agentic AI booking pilot which allows guests to book hotels within Google's AI Mode experience (which are still…"
> "IFRS results: Total revenue $2,659m $2,519m +6% Operating profit $671m $623m +8%"
> "Global estate of 1,049k rooms (7,109 hotels)"; "This drove net system growth of 5% and expanded our global estate to 7,100 hotels."

### Yelp Inc, 10-K FY2025, filed 2026-02-27 — https://www.sec.gov/Archives/edgar/data/1345016/000134501626000019/yelp-20251231.htm

> "…nt that helps consumers make informed spending decisions and confidently transact with local businesses. This collection of high-quality, human-generated content is also the type of proprietary data that is essential to AI search providers, thereby providing a valuable monetizable asset.…"
> "…• if consumers use AI-powered features of search engines, such as Google's AI Overviews and AI Mode, AI chatbots or other AI platforms instead of traditional search engines, as these tools often present their results in a format that de-emphasizes links to our platform;…"
> "As of December 31, 2025, we had 5,168 employees (including employees on leave) globally"

### 1-800-Flowers.com, 10-K FY2026 (fiscal year ended 2026-06-28), filed 2026-09-11 — https://www.sec.gov/Archives/edgar/data/1084869/000108486926000029/flws-20260628.htm

> "…ch and paid listing algorithms, the addition of artificial intelligence ("AI") summaries to online search engine results, and the introduction of new AI assistant platforms. Consumers may increasingly rely on generative AI search, shopping assistants, social commerce, marketplace recommendations, or other intermediated discovery tools that reduce traffic to our owned websites and mobile applications or change how and whether our brands and products are described or ranked. These tools may displa…"

### Yext, Inc., 8-K exhibit 99.3, product update press release, 2026-09-01 — https://www.sec.gov/Archives/edgar/data/1614178/000162828026059706/ex993q2fy27productupdatepr.htm

> "Yext expands agentic capabilities to grow AI visibility for enterprise brands and small businesses — Yext adds brand-level AI visibility and AEO optimization to Scout and launches a new product purpose-built for SMBs — NEW YORK -- (BUSINESS WIRE) — September 1, 2026 — Yext (NYSE: YEXT) today announced that it has expanded its agentic marketing platform to optimize more sources that AI cites and also launched an early version of a new SMB product: Corvo AI is a proactive agent purpose-built for small business owners. The announcements accompany Yext's results for its second quarter of fiscal 2027, issued today, and will also be featured at Envision, its customer conference on September 30, 2026."
> ""The surfaces where brands need to be discoverable keep multiplying, and the marketing landscape has never been more competitive, from the largest enterprises to the smallest local businesses," said Michael Walrath, chairman and CEO of Yext. Many businesses are still observing the problem of AI visibility without a proven path to improve their visibility across these new AI answer surfaces. According to a Corporate Ink survey, 88% of CMOs and VP-level marketers are being asked by leadership or their board about AI visibility. Yet, only 34% of all marketers surveyed say they have a defined AI visibility strategy. Scout is Yext's comprehensive answer to this problem for enterprises. Scout has proven to help multi-location brands increase AI visibility at the local-level by increasing citations by 186% for one hearing care provider. Now, Yext is expanding to offer brand and location-level AI visibility optimization across more sources that AI cites to capture intent at critical times in the consideration process. In early use, the new capabilities have been shown to double inbound leads for a programmatic advertising platform. Yext used its own product to grow its AI visibility by 147% and win share of voice against two leading competitors in only two weeks. Yext is currently piloting it with a small number of enterprise customers ahead of broader availability on September 30."
> "Corvo AI is Yext's new small business agent harness, built for business owners who have limited time to manage their marketing and are always on the move. Corvo AI proactively texts business owners specific recommendations for improving local marketing, so they can outrank the competition nearby."

[note: no engine named in the exhibit (0 matches for ChatGPT, Gemini, Perplexity, Copilot, Claude, AI Overviews, AI Mode, Grok). The Corporate Ink survey has no n, date or method in the exhibit.]

### Headcounts from 10-Ks (for buyer-size banding)

| Filer | Statement, verbatim | Filing |
|---|---|---|
| Yext | "As of January 31, 2026, we had approximately 1,120 full-time employees, approximately 27% of whom are based in our New York headquarters." | 10-K filed 2026-03-10, https://www.sec.gov/Archives/edgar/data/1614178/000162828026016402/yext-20260131.htm |
| Choice Hotels International | "As of December 31, 2025, the Company had 1,562 U.S. and 192 international associates, excluding employees at our 13 managed hotels." | 10-K filed 2026-02-19, https://www.sec.gov/Archives/edgar/data/1046311/000104631126000008/chh-20251231.htm |
| Walgreens Boots Alliance | "Walgreens Boots Alliance has a presence in 8 countries and employs approximately 312,000 people." | 10-K FY2024 filed 2024-10-15 (latest 10-K in the submissions index), https://www.sec.gov/Archives/edgar/data/1618921/000161892124000084/wba-20240831.htm |
| The Joint Corp | as above: ~202 full-time, ~128 part-time; over 960 clinics, 885 franchised | 10-K filed 2026-03-13 |
| Hyatt | as above: ~242,000 colleagues | 10-K filed 2026-02-13 |
| IHG | no headcount sentence captured; total revenue $2,659m, half-year | 6-K filed 2026-08-11 |

## Pull notes — mechanical only

- efts.sec.gov answered all queries except `"AI search" restaurants` (HTTP 500 once). Hit lists truncated at 40 rows per query by the script; totals are the API's `hits.total.value`.
- Document fetches from sec.gov/Archives all HTTP 200; data.sec.gov submissions JSON HTTP 200 for CIKs 1614178, 1046311, 1618921, 1612630.
- Excerpts located by regex on `AI visibility|AI search|ChatGPT|generative engine|answer engine|AI Overviews|Perplexity|large language model`; windows of ~220 characters before and ~280–480 after; at most six per document shown; sec.gov exhibits from decks are slide text run together.
- Walgreens: the submissions index's latest 10-K is FY2024 (filed 2024-10-15); no FY2025 10-K listed.
- Choice Hotels: no "employees" sentence matched the first pattern; the "associates" sentence was found on a second pass.
