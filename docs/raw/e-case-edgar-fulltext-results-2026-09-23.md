# SEC EDGAR full-text search — P4-r extension: result-stating filings on AI visibility, 2025-01-01 to 2026-09-23

```yaml
source:          U.S. Securities and Exchange Commission — EDGAR full-text search (efts.sec.gov) and EDGAR Archives (www.sec.gov/Archives)
url_or_doc_id:   https://efts.sec.gov/LATEST/search-index?q=<query>&dateRange=custom&startdt=2025-01-01&enddt=2026-09-23&forms=10-K,10-Q,8-K,S-1,20-F,6-K,F-1,424B4 ; per-CIK queries with &ciks=<CIK>; documents at the Archives URLs listed below
published:       per row — filing dates 2025-01 to 2026-09-22
pull_date:       2026-09-23
pull_method:     fetch (Python urllib, curl-equivalent) with User-Agent 'research contact vadprimary@gmail.com'; hit lists paginated to 500 per query; every hit document fetched and tag-stripped; sentences kept where an AI-engine term and an outcome term co-occur with a number or direction word
pull_purpose:    evidence about a number (filings stating an AI-visibility or AI-referral result)
tier:            2
tier_reason:     table default — filed documents; sentence selection is mechanical (regex), stated in pull notes
source_label:    filed
lane:            E
sub_market:      organic recommendation | paid placement | agentic commerce
engine:          per sentence
metric_kind:     per sentence — traffic, visibility, sales, none
supersedes:      none — extends raw/e-edgar-fulltext-repull-2026-09-23.md (R-BLOCKED: four phrases, forms 10-K/10-Q/8-K); that file's hits are not re-listed except where a sentence is re-quoted with context
captured:        query totals; filtered sentences; context windows for result- or action-stating filings; full hit list (company, form, date, URL, queries)
verbatim:        partial — sentences as extracted
```

## Verbatim

### Query totals (EFTS hits.total.value)

| Set | Query | Hits |
|---|---|---|
| 1 | "generative engine optimization" | 37 |
| 1 | "AI visibility" | 35 |
| 1 | "answer engine" | 22 |
| 1 | "traffic from AI" | 7 |
| 1 | "AI referrals" | 2 |
| 1 | "agentic search" | 27 |
| 1 | "generative AI" "referral traffic" | 15 |
| 1 | "ChatGPT" "referral" | 109 |
| 1 | "AI Overviews" "traffic" | 55 |
| 1 | "Perplexity" "traffic" | 44 |
| 1 | "AI search" "traffic" | 82 |
| 1 | "ChatGPT" "traffic" | 239 |
| 1 | "large language models" "organic traffic" | 44 |
| 1 | "AI Mode" "traffic" | 20 |
| 1 | "AI assistants" "traffic" | 49 |
| 1 | "AI-referred" | 13 |
| 1 | "AI-driven traffic" | 9 |
| 1 | "LLM" "referral" | 225 |
| 1 | "LLMs" "referral" | 174 |
| 1 | "AI search" "conversion" | 98 |
| 2 | "AI citations" | 4 |
| 2 | "LLM citations" | 1 |
| 2 | "answer engines" | 28 |
| 2 | "AI search engines" "increase" | 11 |
| 2 | "ChatGPT" "new members" | 32 |
| 2 | "ChatGPT" "bookings" | 62 |
| 2 | "through ChatGPT" | 1 |
| 2 | "AI discovery" | 37 |
| 2 | "AI-powered search" "traffic" | 76 |
| 2 | "AI platforms" "referrals" | 147 |

Unique documents fetched: set 1 873, set 2 366, union 1098.

### Per-CIK queries on brand-side filers — terms "AI search", "ChatGPT", "AI Overviews", "LLM", "answer engine"

| Ticker | Hits per query |
|---|---|
| FRSH | "AI search" 2; "ChatGPT" 1; "LLM" 2 |
| YEXT | "AI search" 22; "ChatGPT" 3; "answer engine" 1 |
| TTGT | "AI search" 2; "AI Overviews" 1; "LLM" 2; "answer engine" 2 |
| CHYM | "ChatGPT" 7 |
| HUBS | "ChatGPT" 1; "LLM" 1; "answer engine" 4 |
| ETSY | "ChatGPT" 3 |
| KVYO | "ChatGPT" 4 |
| LMND | "ChatGPT" 1 |
| BRZE | "ChatGPT" 2; "LLM" 3 |
| ROOT | "ChatGPT" 2 |
| TREE | "ChatGPT" 1; "AI Overviews" 1 |
| NRDS | "AI Overviews" 1 |
| DOCN | "LLM" 1 |
| SPT | "LLM" 1 |
| MAX | "LLM" 2 |

Tickers queried: CHYM, ELF, EL, ULTA, NRDS, TREE, EVER, HUBS, LMND, COTY, SLQT, MAX, QNST, ROOT, HIMS, WRBY, BRZE, DOCN, KVYO, ETSY, YEXT, TTGT, FRSH, MNDY, SPT, PGR, ALL, AXP, COF, SOFI, UPST, CURV, PRPL, OPEN; OLPX, SEMR, ZI not found in company_tickers.json. Tickers absent from the table returned zero hits on every term that did not error.

### Filtered sentences — AI term + outcome term + number or direction (set 1)

**Change Agents Corporation.  (ALBT)  (CIK** — 8-K, filed 2026-07-21 — https://www.sec.gov/Archives/edgar/data/1630212/000121390026079830/ea029857301ex99-1.htm

> As consumers increasingly rely on AI assistants for recommendations rather than using traditional search engines, Beacon is designed to improve AI discoverability, monitor brand visibility across AI platforms, and help businesses capture new customer opportunities in the emerging AI search economy.

**Onfolio Holdings, Inc  (ONFO, ONFOP, ONF** — S-1/A, filed 2026-01-28 — https://www.sec.gov/Archives/edgar/data/1825452/000165495426000655/onfo_s1a.htm

> Pace Generative helps brands increase their visibility and traffic from AI answer engines, such as Google AI overviews, ChatGPT, Perplexity, and Grok.

**Onfolio Holdings, Inc  (ONFO, ONFOP, ONF** — S-1/A, filed 2026-04-09 — https://www.sec.gov/Archives/edgar/data/1825452/000165495426003380/onfo_s1a.htm

> Pace Generative provides services including question-driven content development, AI-optimized site structure, language and topic alignment for AI models, and strategic publishing designed to increase visibility within AI-powered platforms such as ChatGPT, Google AI Overviews, and Perplexity.

**Onfolio Holdings, Inc  (ONFO, ONFOP, ONF** — 424B4, filed 2025-09-02 — https://www.sec.gov/Archives/edgar/data/1825452/000165495425010231/onfo_424b4.htm

> As Pace Generative offers services helping companies improve their AI visibility, there is risk that LLM errors or data leaks cause reputation damage to Pace or to our clients. 17 Table of Contents Eastern Standard · Economic Downturn Impact.

**SEMrush Holdings, Inc.  (SEMR)  (CIK 000** — 10-K, filed 2026-03-02 — https://www.sec.gov/Archives/edgar/data/1831840/000162828026013259/semr-20251231.htm

> Our platform enables our customers to understand trends and act upon unique insights to improve their online visibility, understand their presence in search engines and generative engines, drive high-quality traffic to their websites and social media pages, as well as online listings, distribute highly targeted content to their customers, and measure the effectiveness of their digital marketing campaigns.

**SEMrush Holdings, Inc.  (SEMR)  (CIK 000** — 8-K, filed 2025-11-05 — https://www.sec.gov/Archives/edgar/data/1831840/000162828025049628/semrush8-kexhibit991q32025.htm

> • We advanced and expanded many of our offerings and continued investments in Generative AI to provide enhanced, more efficient content creation and marketing capabilities through Semrush’s platform: ◦ Released Semrush One to unite traditional SEO and AI Search into a single offering to help brands measure and grow performance across virtually every search – from Google to AI discovery engines, including ChatGPT, Gemini, Perplexity, and other major large language models (LLMs). ◦ Announced general availability of Semrush Enterprise Site Intelligence, a site health and monitoring solution designed to keep websites technically prepared, visible and resilient in the new era of AI and search. ◦ Unveiled Semrush Enterprise AI Visibility Index, providing enterprises with a definitive benchmark to measure brand performance across ChatGPT and Google AI Mode. “We reported strong financial results

**ADOBE INC.  (ADBE)  (CIK 0000796343)** — 10-K, filed 2026-01-15 — https://www.sec.gov/Archives/edgar/data/796343/000079634326000003/adbe-20251128.htm

> Adobe LLM Optimizer Adobe LLM Optimizer is a generative engine optimization solution, helping enterprises improve brand visibility and discoverability across AI-powered search and discovery while providing actionable insights.

**TechTarget, Inc.  (TTGT)  (CIK 000201806** — 10-K, filed 2026-03-11 — https://www.sec.gov/Archives/edgar/data/2018064/000119312526102183/ttgt-20251231.htm

> Increasingly, we are leveraging AI to bolster our differentiation to both technology buyers and sellers, including growing audience referrals from AI search channels.

**TechTarget, Inc.  (TTGT)  (CIK 000201806** — 10-K, filed 2026-03-11 — https://www.sec.gov/Archives/edgar/data/2018064/000119312526102183/ttgt-20251231.htm

> Our audience development strategy is highly diversified, leveraging multiple audience acquisition and engagement tactics and channels, including daily newsletters from our Dive brands, direct web engagement for premium editorial brands like Dark Reading, BrightTALK webinar channels, social communities, and increasingly AI search engine referrals.

**TechTarget, Inc.  (TTGT)  (CIK 000201806** — 10-K, filed 2026-03-11 — https://www.sec.gov/Archives/edgar/data/2018064/000119312526102183/ttgt-20251231.htm

> We have been seeing a 2x to 3x higher membership conversion rate from answer engine and LLM citations compared to traditional organic search. 13 Table of Contents Delivering decision support content to key audiences that drive purchase behavior We deliver trusted, independent research, primary data, analysis and high-quality editorial content to technology and business professionals that drive purchase behavior in the markets it serves.

**TechTarget, Inc.  (TTGT)  (CIK 000201806** — 8-K, filed 2026-08-06 — https://www.sec.gov/Archives/edgar/data/2018064/000119312526338041/ttgt-ex99_1.htm

> • New Product launches and Partnership Momentum: BrightTALK Nurture as a Service, Netline HQL, Studio AI Visibility Audit, GEO topic planner, Demandbase for Demand Marketers and Sherpa for Partner Marketers are just some of the initiatives launched in the first half, broadening the Company's growth opportunities and value proposition;

**TechTarget, Inc.  (TTGT)  (CIK 000201806** — 8-K, filed 2026-08-06 — https://www.sec.gov/Archives/edgar/data/2018064/000119312526338041/ttgt-ex99_1.htm

> • Audience and Membership Growth: Active membership and activity of members continued to grow year on year despite traffic disruption, supported by specialist media brands, editorial relevance, and ongoing focus on distribution and AI visibility;

**TechTarget, Inc.  (TTGT)  (CIK 000201806** — 8-K, filed 2025-08-12 — https://www.sec.gov/Archives/edgar/data/2018064/000095017025106920/ttgt-ex99_1.htm

> These strategies include Search Engine Optimization (SEO) where our traditional strength translates directly to AI visibility appearing in over 50,000 AI overviews monthly and generating a substantial increase in traffic from AI overviews and with higher conversion rates , but also including the outbound email and newsletter model at Industry Dive which is seeing double-digit growth, partnership models at BrightTALK and NetLine as well as first-party data from Informa PLC.

**Fastly, Inc.  (FSLY)  (CIK 0001517413)** — 10-K, filed 2026-02-25 — https://www.sec.gov/Archives/edgar/data/1517413/000151741326000053/fsly-20251231.htm

> By surfacing relevant information with citation links directly within the control panel, AI Assistant improves the user experience and helps customers explore and configure Fastly more efficiently.

**Fiverr International Ltd.  (FVRR)  (CIK** — 20-F, filed 2026-03-12 — https://www.sec.gov/Archives/edgar/data/1762301/000117891326000858/zk2634486.htm

> Also, an increasing share of users now begins their queries with large language model (LLM) powered assistants rather than traditional web search engines, which may reduce referrals to our websites and overall traffic.

**COTY INC.  (COTY)  (CIK 0001024305)** — 10-K, filed 2026-08-20 — https://www.sec.gov/Archives/edgar/data/1024305/000102430526000048/coty-20260630.htm

> We are also deploying improvements across touchpoints to drive generative engine optimization, to strengthen our brands’ visibility and recommendations by top AI platforms.

**Yext, Inc.  (YEXT)  (CIK 0001614178)** — 8-K, filed 2026-09-01 — https://www.sec.gov/Archives/edgar/data/1614178/000162828026059706/ex993q2fy27productupdatepr.htm

> Many businesses are still observing the problem of AI visibility without a proven path to improve their visibility across these new AI answer surfaces.

**Yext, Inc.  (YEXT)  (CIK 0001614178)** — 8-K, filed 2026-09-01 — https://www.sec.gov/Archives/edgar/data/1614178/000162828026059706/ex993q2fy27productupdatepr.htm

> Scout has proven to help multi-location brands increase AI visibility at the local-level by increasing citations by 186% for one hearing care provider.

**Yext, Inc.  (YEXT)  (CIK 0001614178)** — 8-K, filed 2026-09-01 — https://www.sec.gov/Archives/edgar/data/1614178/000162828026059706/ex993q2fy27productupdatepr.htm

> Yext used its own product to grow its AI visibility by 147% and win share of voice against two leading competitors in only two weeks.

**Yext, Inc.  (YEXT)  (CIK 0001614178)** — 8-K, filed 2026-03-09 — https://www.sec.gov/Archives/edgar/data/1614178/000162828026016005/ex992q4fy26shareholderlett.htm

> Importantly, Scout reinforces the value of the rest of the Yext platform by demonstrating that brand visibility in AI search is driven by structured listings, local and intent pages, online reputation, and social presence. 2 EXHIBIT 99.2 Scout citation data shows that roughly 42% of AI citations originate from online directories, with the majority coming from long-tail and niche sources.

**REZOLVE AI PLC  (RZLV, RZLVW)  (CIK 0001** — 6-K, filed 2026-06-05 — https://www.sec.gov/Archives/edgar/data/1920294/000119312526259945/rzlv-ex99_1.htm

> AI Visibility – Answer Engine Optimization (AEO) As consumers increasingly discover products through AI-powered answer engines such as ChatGPT, Gemini and Claude, Rezolve Ai’s technologies help merchants improve visibility and discoverability within AI-generated shopping experiences.

**JOINT Corp  (JYNT)  (CIK 0001612630)** — 8-K, filed 2026-08-06 — https://www.sec.gov/Archives/edgar/data/1612630/000161263026000063/a8-05x26q22026resultsdec.htm

> All Rights Reserved. | Driving Top-Line Momentum Messaging continues to be on chiropractic care for pain relief, and helping patients get back to what they love to do • Sequential improvement in active member growth each month this year • Increasing focus on our MVPs (most valuable patients) • SEO and AI visibility optimization driving organic traffic and lead quality • Positive trends in traffic and high-intent actions on local clinic microsites • New and expanded flexible membership plan options • Rolled out optimized pricing in over 500 clinics 9NASDAQ: JYNT | © 2026 The Joint Corp.

**Amplitude, Inc.  (AMPL)  (CIK 0001866692** — 8-K, filed 2025-11-05 — https://www.sec.gov/Archives/edgar/data/1866692/000119312525266930/ampl-ex99_1.htm

> • Announced AI Visibility , a new capability that gives marketers unprecedented insight into how their brand shows up in AI search results, accompanied by recommendations on how to improve it based on a company’s actual data.

**Amplitude, Inc.  (AMPL)  (CIK 0001866692** — 10-K, filed 2026-02-19 — https://www.sec.gov/Archives/edgar/data/1866692/000119312526057847/ampl-20251231.htm

> • Amplitude AI Visibility: Launched in October 2025, AI Visibility is a new capability that gives marketers unprecedented insight into how their brand shows up in AI search results, accompanied by recommendations on how to improve it based on a company’s actual data.

**Amplitude, Inc.  (AMPL)  (CIK 0001866692** — 10-K, filed 2026-02-19 — https://www.sec.gov/Archives/edgar/data/1866692/000119312526057847/ampl-20251231.htm

> In October 2025, we launched AI Visibility, a new capability that gives marketers unprecedented insight into how their brand shows up in AI search results, accompanied by recommendations on how to improve it based on a company’s actual data.

**Trump Media & Technology Group Corp.  (D** — 8-K, filed 2025-08-06 — https://www.sec.gov/Archives/edgar/data/1849635/000114036125029058/ef20053299_ex99-1.htm

> Powered by Perplexity, a software and AI company dedicated to providing direct, contextually accurate answers with transparent citations, Truth Search AI is intended to enhance the Truth Social platform and exponentially increase the amount of information available to its users.

**Snap Inc  (SNAP)  (CIK 0001564408)** — 8-K, filed 2025-11-05 — https://www.sec.gov/Archives/edgar/data/1564408/000156440825000063/q32025investorletter.htm

> We advanced Dynamic Product Ads with large language models that better understand products, driving over 4x higher conversion rates compared to baseline for certain campaigns.

**Snap Inc  (SNAP)  (CIK 0001564408)** — 8-K, filed 2026-05-06 — https://www.sec.gov/Archives/edgar/data/1564408/000156440826000024/snapincq12026investorlet.htm

> In Q1, we launched LLM-based user intent understanding for Dynamic Product Ads retrieval, which improved Pixel Purchase conversions by more than 2%, and multimodal similar-product retrieval using a vision-language model fine-tuned on Snap data, which delivered an additional high-single-digit lift in DPA purchase conversions.

**Snap Inc  (SNAP)  (CIK 0001564408)** — 10-K, filed 2026-02-05 — https://www.sec.gov/Archives/edgar/data/1564408/000156440826000013/snap-20251231.htm

> If Perplexity or other third-party AI providers experience service outages, significant latency, or otherwise fail to scale their systems to meet our traffic demands, users may experience a degraded version of our products and services, which could result in a negative user experience, decreased engagement, and a loss of trust.

**Rent the Runway, Inc.  (RENT)  (CIK 0001** — 10-K, filed 2026-04-14 — https://www.sec.gov/Archives/edgar/data/1468327/000146832726000020/wdq-20260131.htm

> In addition, we continue to focus on growing traffic and conversion rates by optimizing our organic social media channels, improving our email marketing performance, refreshing our lifecycle marketing engine, increasing paid marketing efficiency, focusing on referrals and other community-driven “word of mouth” strategies, and aiming to optimize discovery via search engine optimization, agentic search, and enhanced iOS App Store presence.

**Rent the Runway, Inc.  (RENT)  (CIK 0001** — 10-Q, filed 2026-09-11 — https://www.sec.gov/Archives/edgar/data/1468327/000146832726000088/rent-20260731.htm

> These efforts are ongoing and, although we have seen some positive results, they are subject to change and may not result in a sustained increase in customer conversion, loyalty or engagement.The impact of emerging technologies, including, but not limited to, AI tools such as agentic search, is not yet certain and may increase these risks.

**Klarna Group plc  (KLAR)  (CIK 000200329** — 6-K, filed 2026-08-18 — https://www.sec.gov/Archives/edgar/data/2003292/000162828026057573/q22026earningsrelease.htm

> Traffic from AI platforms to retailers grew sharply last holiday season and converts at higher rates.

**ETSY INC  (ETSY)  (CIK 0001370637)** — 8-K, filed 2026-04-29 — https://www.sec.gov/Archives/edgar/data/1370637/000137063726000042/q126shareholderletter.htm

> We’re encouraged by the early learnings shared on our last earnings call — and data continues to support strong growth in traffic and high-intent engagement from buyers who come to Etsy through agentic search.

**CIMPRESS plc  (CMPR)  (CIK 0001262976)** — 10-K, filed 2025-08-08 — https://www.sec.gov/Archives/edgar/data/1262976/000162828025039200/cmpr-20250630.htm

> As generative AI and agentic search tools become more prevalent and integrated into consumers’ browsing and purchasing workflows, we may experience a decline in visibility within digital ecosystems we do not directly control.

**Zedge, Inc.  (ZDGE)  (CIK 0001667313)** — 10-K, filed 2025-10-28 — https://www.sec.gov/Archives/edgar/data/1667313/000121390025103098/ea0262035-10k_zedge.htm

> For example, platforms may incorporate AI-driven wallpaper, emoji, or other personalization features directly into their services or AI overviews, reduce referral traffic, alter algorithms or terms governing AI content, or restrict use of third-party AI tools, any of which could decrease usage of our products or increase customer acquisition costs.

**Zedge, Inc.  (ZDGE)  (CIK 0001667313)** — 10-K, filed 2025-10-28 — https://www.sec.gov/Archives/edgar/data/1667313/000121390025103098/ea0262035-10k_zedge.htm

> Complying with overlapping and potentially inconsistent regimes may require us to modify algorithms, retrain models, restrict features, alter data-handling practices, or delay or forego product launches. 38 In addition, as major platforms and competitors integrate their own AI features, such as Google’s AI Overviews in search, AI-driven emoji rendering, or direct delivery of wallpaper and personalization content, traffic to our properties, including Emojipedia and the Zedge Marketplace, could decline, which could adversely impact user acquisition, engagement, and monetization.

**TNL Mediagene  (TNMG, TNMWF)  (CIK 00020** — 20-F, filed 2026-04-30 — https://www.sec.gov/Archives/edgar/data/2013186/000121390026049832/ea0286618-20f_tnlmedia.htm

> In addition, the increasing adoption of AI technologies, including large language models integrated into search engines, may change how users discover and access content, potentially reducing referral traffic to our digital media brands and adversely affecting the effectiveness and value of advertising on our platforms. 7 Further, we need to maintain good relationships with advertisers to provide us with a sufficient inventory of advertisements and offers.

**TNL Mediagene  (TNMG, TNMWF)  (CIK 00020** — 20-F, filed 2026-04-30 — https://www.sec.gov/Archives/edgar/data/2013186/000121390026049832/ea0286618-20f_tnlmedia.htm

> If usage of LLM-based AI products continues to expand and displaces traditional search engine queries, this structural change could lead to a sustained decline in referral traffic to our digital media brands, reducing our user engagement and advertising revenues.

**Locafy Ltd  (LCFY, LCFYW)  (CIK 00018755** — 20-F, filed 2025-11-12 — https://www.sec.gov/Archives/edgar/data/1875547/000149315225021910/form20-f.htm

> ● Landing Pages optimized for both traditional search and AI search; and ● Map Boosting technology that increases visibility in Google’s Local Pack search results.

**Locafy Ltd  (LCFY, LCFYW)  (CIK 00018755** — 20-F, filed 2025-11-12 — https://www.sec.gov/Archives/edgar/data/1875547/000149315225021910/form20-f.htm

> This technology supports both traditional search and newer AI search optimization, helping businesses increase online visibility and attract relevant consumer traffic.

**SIMILARWEB LTD.  (SMWB)  (CIK 0001842731** — 6-K, filed 2025-05-13 — https://www.sec.gov/Archives/edgar/data/1842731/000184273125000018/q12025smwbshareholderlet.htm

> As AI chatbots increasingly influence how people discover and engage with content, they are becoming powerful sources of referral traffic.

**trivago N.V.  (TRVG)  (CIK 0001683825)** — 20-F, filed 2026-02-26 — https://www.sec.gov/Archives/edgar/data/1683825/000168382526000006/trvg-20251231.htm

> For example, travel-related search results (including hotel results) may increasingly be made more or less prominent through AI-enabled search features and LLM-based (as defined above) chatbots, which could reduce traffic to traditional metasearch websites and alter the ways in which users discover and compare accommodation offerings.

**Gambling.com Group Ltd  (GAMB)  (CIK 000** — 20-F, filed 2026-03-19 — https://www.sec.gov/Archives/edgar/data/1839799/000183979926000048/gamb-20251231.htm

> Changes in search engine algorithms, the proliferation of artificial intelligence within search results and as alternative answer engines, the growth of zero-click searches, and the evolving competitive and regulatory landscape could materially reduce traffic to our websites and adversely affect our business, financial condition, and results of operations.

**Gambling.com Group Ltd  (GAMB)  (CIK 000** — 20-F, filed 2026-03-19 — https://www.sec.gov/Archives/edgar/data/1839799/000183979926000048/gamb-20251231.htm

> If AI answer engines increasingly address the query types that drive traffic and revenue for our business, the resulting decline in organic search traffic could have a material adverse effect on our business, financial condition, and results of operations.

**VisitIQ Corp.  (VIIQ)  (CIK 0001470129)** — 10-K, filed 2026-05-20 — https://www.sec.gov/Archives/edgar/data/1470129/000175392626000917/g085722_10k.htm

> AI Search Decimating Organic Traffic (NOW) ● Gartner, Inc. predicts 50% reduction in organic search traffic by 2026 ● Google AI Overviews + ChatGPT Search eliminating website visits ● Brands need alternative audience sources immediately 2.

**VisitIQ Corp.  (VIIQ)  (CIK 0001470129)** — 10-K, filed 2026-05-20 — https://www.sec.gov/Archives/edgar/data/1470129/000175392626000917/g085722_10k.htm

> Real-time intent and geo-signals enable timely promotions, retargeting and personalized offers that increase conversions. 15 ● Franchise.

**VisitIQ Corp.  (VIIQ)  (CIK 0001470129)** — 10-K, filed 2026-05-20 — https://www.sec.gov/Archives/edgar/data/1470129/000175392626000917/g085722_10k.htm

> Franchise systems identify local demand, surface active shoppers, build location-specific ICPs, and activate high-intent, geo-targeted campaigns to drive in-store visits and regional growth.

**SFIDA X, Inc.  (CIK 0002035964)** — F-1/A, filed 2025-06-02 — https://www.sec.gov/Archives/edgar/data/2035964/000164117225013267/formf-1a.htm

> Based on these metrics, the AI platform identifies strategies to boost website traffic and presents a monthly report on content themes and article structures that align with traffic trends and search behavior, which can help with increasing the likelihood of website engagement.

**SFIDA X, Inc.  (CIK 0002035964)** — F-1/A, filed 2025-11-28 — https://www.sec.gov/Archives/edgar/data/2035964/000149315225025342/formf-1a.htm

> Based on these data, the AI platform identifies strategies to boost website traffic and presents a monthly report on content themes and article structures that align with traffic trends and search behavior, which can help with increasing the likelihood of website engagement.

**IAC Inc.  (IAC)  (CIK 0001800227)** — 8-K, filed 2026-05-04 — https://www.sec.gov/Archives/edgar/data/1800227/000162828026029796/q12026iacearningscallpre.htm

> Social Events D/Cipher AI LicensingMyRecipes Apple News PEOPLE App Commerce 10,192 16,545 20,962 - 5,000 10,000 15,000 20,000 25,000 Q1'24 Q1'25 Q1'26 Off Platform Views 1,027 1,452 1,378 1,245 759 463 2,273 2,211 1,841 - 500 1,000 1,500 2,000 2,500 Q1'24 Q1'25 Q1'26 All Other Google Search +16% (M) -39% -10% ‘24-’26 CAGR Q1 Audience Trends 6 Core Sessions Off-Platform Views +43% ‘24-’26 CAGR 1 (M) 54% 37% 1 AI Overviews penetration is an internally-sourced metric that tracks the presence of AI Overviews on the top 10,000 People Inc. search keywords. 2 Reflects off-platform views from Core brands. 2 25%55% 34% • Growing Digital revenue at a 7% CAGR despite 63% decline in Google Search referrals over two years • AI Overviews appear on nearly 70% of top People Inc. queries • People Inc. brands reach large and rapidly expanding audiences across Meta, Apple News, TikTok, YouTube • Distribute

**IAC Inc.  (IAC)  (CIK 0001800227)** — 8-K, filed 2026-02-03 — https://www.sec.gov/Archives/edgar/data/1800227/000162828026004988/ex_991q42025iac-pressrelea.htm

> Revenue ($ in millions, rounding differences may occur) Q4 2025 Q4 2024 Growth Revenue Digital $ 354.8 $ 310.6 14 % Print 168.5 217.9 -23 % Intersegment eliminations (11.4) (6.5) -77 % Total $ 511.8 $ 522.1 -2 % • Revenue of $511.8 million decreased 2% year-over-year reflecting: ◦ 14% Digital revenue growth driven by: ▪ Advertising revenue increased 9% reflecting: • Higher premium advertising revenue due primarily to the Health and Pharmaceuticals, Finance, and Media and Entertainment categories as well as increased contribution from D/Cipher+ • Lower programmatic advertising revenue due to lower impression volumes driven by 13% declines in Core Sessions, due primarily to the impact of the growing prominence of Google AI Overviews on Google search sessions, and an increased portion of impression volume consumed by premium advertising, partially offset by higher rates ▪ Performance market

**IAC Inc.  (IAC)  (CIK 0001800227)** — 10-Q, filed 2025-11-03 — https://www.sec.gov/Archives/edgar/data/1800227/000162828025048244/iaci-20250930.htm

> The decrease in Advertising revenue was driven primarily by lower programmatic revenue primarily due to lower impression volumes driven by a 6% decline in Core Sessions, due primarily to the impact of the increasing prominence of Google AI Overviews on Google search sessions, and an increased portion of impression volume consumed by premium advertising, partially offset by higher programmatic rates.

**IAC Inc.  (IAC)  (CIK 0001800227)** — 10-Q, filed 2025-11-03 — https://www.sec.gov/Archives/edgar/data/1800227/000162828025048244/iaci-20250930.htm

> The Company expects the increasing prominence of Google AI Overviews to continue to negatively impact Core Sessions.

**IAC Inc.  (IAC)  (CIK 0001800227)** — 8-K, filed 2026-05-04 — https://www.sec.gov/Archives/edgar/data/1800227/000162828026029796/ex_991q12026iac-pressrelea.htm

> Revenue ($ in millions, rounding differences may occur) Q1 2026 Q1 2025 Growth Revenue Digital $ 253.2 $ 234.5 8 % Print 137.8 163.3 -16 % Intersegment eliminations (5.3) (4.7) -13 % Total $ 385.7 $ 393.1 -2 % • Revenue of $385.7 million decreased 2% year-over-year reflecting: ◦ 8% Digital revenue growth reflecting: ▪ Advertising revenue increased 1% reflecting: • Higher premium advertising revenue due to direct-sold growth from the Health and Pharmaceuticals, Home and Consumer Packaged Goods, and Technology and Telecommunications categories as well as increased contribution from D/Cipher+ and other Non-session-based revenue streams, partially offset by declines in premium programmatic volume • Lower open programmatic advertising revenue due to lower impression volumes driven by a 17% decline in Core Sessions, due primarily to the impact of the growing prominence of Google AI Overviews o

**IAC Inc.  (IAC)  (CIK 0001800227)** — 10-Q, filed 2026-05-04 — https://www.sec.gov/Archives/edgar/data/1800227/000162828026029798/iaci-20260331.htm

> Additionally, open programmatic advertising revenue decreased due primarily to lower impression volumes driven by a 17% decline in Core Sessions, due primarily to the impact of the increasing prominence of Google AI Overviews on Google search sessions, partially offset by higher programmatic rates.

**IAC Inc.  (IAC)  (CIK 0001800227)** — 10-Q, filed 2026-05-04 — https://www.sec.gov/Archives/edgar/data/1800227/000162828026029798/iaci-20260331.htm

> The Comp any expects the increasing prominence of Google AI Overviews to continue to negatively impact Core Sessions and advertising revenue. ◦ The Print decrease was due primarily to decreases of $12.9 million, or 17%, in subscription revenue, $7.6 million, or 20%, in advertising revenue, $2.5 million, or 16%, in project and other revenue and $2.2 million, or 27%, in performance marketing revenue.

**IAC Inc.  (IAC)  (CIK 0001800227)** — 10-K, filed 2026-02-20 — https://www.sec.gov/Archives/edgar/data/1800227/000162828026009997/iaci-20251231.htm

> The increase in premium advertising was partially offset by lower programmatic revenue primarily due to lower impression volumes driven by a 5% decline in Core Sessions, due primarily to the impact of the increasing prominence of Google AI Overviews on Google search sessions, and an increased portion of impression volume consumed by premium advertising, partially offset by higher programmatic rates.

**CHEGG, INC  (CHGG)  (CIK 0001364954)** — 8-K, filed 2025-08-05 — https://www.sec.gov/Archives/edgar/data/1364954/000136495425000090/a9901-financialresultsq220.htm

> We had 2.6 million subscribers during the quarter, representing a year-over-year decline of 40%, as we continue to feel the impact of lower traffic, largely due to Google AI Overviews.

**People Inc  (PPLI)  (CIK 0001800227)** — 8-K, filed 2026-09-11 — https://www.sec.gov/Archives/edgar/data/1800227/000162828026061531/iaci-20260911_d2.htm

> The programmatic revenue decline was due primarily to lower impression volumes driven by a 5% decline in Core Sessions, due primarily to the impact of the increasing prominence of Google AI Overviews on Google search sessions, and an increased portion of impression volume consumed by premium advertising, partially offset by higher programmatic rates.

**People Inc  (PPLI)  (CIK 0001800227)** — 8-K, filed 2026-09-11 — https://www.sec.gov/Archives/edgar/data/1800227/000162828026061531/iaci-20260911_d2.htm

> The Comp any expects the increasing prominence of Google AI Overviews to continue to negatively impact Core Sessions and advertising revenue.

**People Inc  (PPLI)  (CIK 0001800227)** — 10-Q, filed 2026-08-03 — https://www.sec.gov/Archives/edgar/data/1800227/000162828026051881/ppli-20260630.htm

> Open programmatic advertising revenue increased due primarily to higher programmatic rates, partially offset by lower impression volumes driven by a 22% decline in Core Sessions, due primarily to the impact of the increasing prominence of Google AI Overviews on Google search sessions.

**YELP INC  (YELP)  (CIK 0001345016)** — 8-K, filed 2026-08-06 — https://www.sec.gov/Archives/edgar/data/1345016/000134501626000059/yelpq22026ex992lettertos.htm

> In fact, we commissioned a recent study that found Yelp was the most organically cited home services discovery platform by LLMs in the fourth quarter of 2025, receiving 3.4x as many AI citations than the next closest platform.5 Through data licensing and APIs, we are extending the reach of our trusted content to provide consumers with reliable local answers.

**YELP INC  (YELP)  (CIK 0001345016)** — 8-K, filed 2026-08-06 — https://www.sec.gov/Archives/edgar/data/1345016/000134501626000059/yelpq22026ex992lettertos.htm

> Yelp BBB Angi Thumbtack HomeAdvisor Nextdoor 512.7k 149.7k 145.6k 56.0k 33.6k 10.3k 512.7k Yelp Citations 3.4x VS. #2 (BBB) ChatGPT now utilizes Yelp ratings and reviews 5 Based on an analysis that measured the number of times Yelp was cited by ChatGPT, Google Gemini, Perplexity and Google AI Mode in the fourth quarter of 2025, compared to the number of citations received over the same period by five home services discovery platforms (Better Business Bureau, Angi, Thumbtack, HomeAdvisor and Nextdoor).

**YELP INC  (YELP)  (CIK 0001345016)** — 8-K, filed 2026-08-06 — https://www.sec.gov/Archives/edgar/data/1345016/000134501626000059/yelpq22026ex992lettertos.htm

> Home Services Competitors — Major AI platforms combined5 Total citations across ChatGPT, Gemini, Perplexity & Google AI Mode Ye lp Q 2 20 26 10 23 Investing for growth In recent years, we have delivered strong profitability through our product-led strategy as we held overall headcount approximately flat.

**YELP INC  (YELP)  (CIK 0001345016)** — 8-K/A, filed 2026-02-27 — https://www.sec.gov/Archives/edgar/data/1345016/000134501626000018/yelpq42025ex992lettertos.htm

> This growth was primarily driven by increases in revenue from our subscription products, data licensing, including from recently signed agreements with major AI search providers, and food takeout and delivery orders, primarily due to our partnership with DoorDash.

**Perion Network Ltd.  (PERI)  (CIK 000133** — 20-F, filed 2026-03-16 — https://www.sec.gov/Archives/edgar/data/1338940/000117891326000927/zk2634522.htm

> • The rapid development and broad adoption of generative AI chatbots cause a shift to AI mediated content and a decrease in web traffic and a disruption in our industry, which could harm our business.

**Perion Network Ltd.  (PERI)  (CIK 000133** — 20-F, filed 2026-03-16 — https://www.sec.gov/Archives/edgar/data/1338940/000117891326000927/zk2634522.htm

> The rapid development and broad adoption of generative AI chatbots cause a shift to AI mediated content and a decrease in web traffic and a disruption in our industry, which could harm our business.

**Perion Network Ltd.  (PERI)  (CIK 000133** — 20-F, filed 2026-03-16 — https://www.sec.gov/Archives/edgar/data/1338940/000117891326000927/zk2634522.htm

> • Supply sources may experience a decline in users’ traffic due to the extensive availability of generative AI chatbots, which would restrain our supply of available inventory.

**Perion Network Ltd.  (PERI)  (CIK 000133** — 20-F, filed 2026-03-16 — https://www.sec.gov/Archives/edgar/data/1338940/000117891326000927/zk2634522.htm

> For more information on AI relatd risks see Risk Factor titled – “ The rapid development and broad adoption of generative AI chatbots cause a shift to AI mediated content and a decrease in web traffic and a disruption in our industry, which could harm our business . “ Sales efforts with advertisers and advertising agencies require significant time and expense and may ultimately be unsuccessful.

**Perion Network Ltd.  (PERI)  (CIK 000133** — 20-F, filed 2026-03-16 — https://www.sec.gov/Archives/edgar/data/1338940/000117891326000927/zk2634522.htm

> For additional information see also the Risk Factor titled – “ The rapid development and broad adoption of generative AI chatbots cause a shift to AI mediated content and a decrease in web traffic and a disruption in our industry, which could harm our business .” The generation of search advertising revenue through publishers is subject to competition.

**Expedia Group, Inc.  (EXPE)  (CIK 000132** — 10-K, filed 2026-02-13 — https://www.sec.gov/Archives/edgar/data/1324424/000132442426000008/expe-20251231.htm

> In addition, the emergence of AI search platforms and changing consumer behavior adversely affect search traffic and margins. 10 Table of Contents We rely on the value of our brands, and the costs of maintaining and enhancing our brand awareness are increasing.

**Baidu, Inc.  (BIDU, BAIDF)  (CIK 0001329** — 20-F, filed 2026-03-17 — https://www.sec.gov/Archives/edgar/data/1329099/000119312526109289/d38065d20f.htm

> If any of our competitors provides a smarter search experience or a more advanced AI search mode, internet video services, or cloud services, our user traffic and revenue could decline significantly.

**1 800 FLOWERS COM INC  (FLWS)  (CIK 0001** — 10-K, filed 2026-09-11 — https://www.sec.gov/Archives/edgar/data/1084869/000108486926000029/flws-20260628.htm

> Consumers may increasingly rely on generative AI search, shopping assistants, social commerce, marketplace recommendations, or other intermediated discovery tools that reduce traffic to our owned websites and mobile applications or change how and whether our brands and products are described or ranked.

**EverQuote, Inc.  (EVER)  (CIK 0001640428** — 8-K, filed 2026-08-03 — https://www.sec.gov/Archives/edgar/data/1640428/000119312526330540/ever-ex99_2.htm

> P&C Insurance Market: Distribution and Advertising Spend Sources: S&P Global Market Intelligence, Insider Intelligence, and Company’s own estimates as of 12/31/25 - includes commissions and advertising spend What We Do: Drive High-Intent Consumers to P&C Insurers TARGETING & BIDDING CONVERSION &DISTRIBUTION ORIGINATION Filter out “non-target” shoppers “Right-target,right-price bids for desired shoppers TikTok Taboola YouTube Criteo MediaGo MSN Consumer history Location Demographics Insurance history Underwriting preferences Profitability targets State regulatory variations LTV analysis Predictive modeling Allstate Liberty Mutual Farmers USAA Progressive Root State Farm Carriers & Agents Google ChatGPT Facebook Instagram AI TRAFFIC ENGINE PROPRIETARY DATA Regulated Carrier and agent modelsare governed by regulationsthat vary greatly acrosseach of the 50 states The Market We Serve: A Data-

**EverQuote, Inc.  (EVER)  (CIK 0001640428** — 8-K, filed 2026-08-03 — https://www.sec.gov/Archives/edgar/data/1640428/000119312526330540/ever-ex99_2.htm

> While negatively impacting our expense ratio, this approach has led to nearly double the personal lines new business volume produced in the prior year quarter.” - Liberty Mutual Insurance P&C Combined Ratio (1) Source: S&P CapIQ0 Source: various carriers’ earnings transcripts in 2025 Marketplace Our AI Opportunity Today: Unlocking Value in our Marketplace Transforming online acquisition while preserving carriers’ rate opacity, brand integrity and underwriting preferences More traffic As LLMs become a channel of high-intent buyers over time Higher conversion rates As personalization drives better matching Greater bind performance As precise targeting improves consumer-carrier alignment Larger budget share As intelligent bidding optimizes clients’ cost per acquisition Our Growth Strategy: Path to $1B+ of Annual Revenue (1) Proprietary data, applied AI, and consultative partnerships to opti

**ZIPRECRUITER, INC.  (ZIP)  (CIK 00016175** — 8-K, filed 2026-05-07 — https://www.sec.gov/Archives/edgar/data/1617553/000161755326000030/q12026shareholderletter-.htm

> Taken together — our increased share of total traffic, 26% year-over-year growth in engaged job seekers through organic channels, and a new distribution footprint across generative AI platforms — we believe ZipRecruiter is gaining share at a moment when cyclical hiring demand remains muted.

**CHECK POINT SOFTWARE TECHNOLOGIES LTD  (** — 20-F, filed 2026-03-31 — https://www.sec.gov/Archives/edgar/data/1015922/000117891326001932/zk2634942.htm

> R82.10 delivers over 20 new capabilities for enterprise customers including: - Supporting Safe AI Adoption : R82.10 strengthens oversight of AI-driven activity by detecting unauthorized Generative AI (“GenAI”) tools, expanding visibility into AI applications such as ChatGPT, Claude, Gemini, among others, and monitoring model context protocol (“MCP) usage to protect AI-powered workflows. - Strengthening Hybrid Mesh Network Security : Organizations gain more consistent protection across distributed environments with centralized internet access management for SASE and firewalls, simplified gateway-to-SASE connectivity, and improved identity and device posture validation to support “Zero Trust” framework at scale. - Taking a Prevention-First Approach to Modern Threats : R82.10, introduces phishing protection that works without HTTPS inspection, adaptive IPS to reduce alert fatigue, and new T

**CoreWeave, Inc.  (CRWV)  (CIK 0001769628** — S-1/A, filed 2025-03-12 — https://www.sec.gov/Archives/edgar/data/1769628/000119312525052207/d899798ds1a.htm

> In addition, regulatory frameworks are expected to increasingly restrict data from flowing across borders, meaning that AI models may eventually need to be trained on regional data pools and served locally.

**CoreWeave, Inc.  (CIK 0001769628)** — S-1, filed 2025-03-03 — https://www.sec.gov/Archives/edgar/data/1769628/000119312525044231/d899798ds1.htm

> In addition, regulatory frameworks are expected to increasingly restrict data from flowing across borders, meaning that AI models may eventually need to be trained on regional data pools and served locally.

**Youdao, Inc.  (DAO)  (CIK 0001781753)** — 20-F, filed 2025-04-15 — https://www.sec.gov/Archives/edgar/data/1781753/000119312525080651/d758034d20f.htm

> Furthermore, our AI-driven LLM improves conversion efficiency by continuously refining advertising strategies through data-driven insights and performance analytics.

**Ribbon Communications Inc.  (RBBN)  (CIK** — 10-K, filed 2025-02-27 — https://www.sec.gov/Archives/edgar/data/1708055/000155837025001773/tmb-20241231x10k.htm

> The exponential growth in traffic has largely been driven by the consumption of video and in the next several years, it is expected that new applications leveraging large language model (“LLM”) AI will dramatically increase the amount of network bandwidth usage.

**Ribbon Communications Inc.  (RBBN)  (CIK** — 10-K, filed 2025-02-27 — https://www.sec.gov/Archives/edgar/data/1708055/000155837025001773/tmb-20241231x10k.htm

> New applications enabled by LLM AI will dramatically increase the traffic from the subscriber device to the data center.

**Ribbon Communications Inc.  (RBBN)  (CIK** — 10-K, filed 2026-02-26 — https://www.sec.gov/Archives/edgar/data/1708055/000170805526000012/rbbn-20251231x10k.htm

> The exponential growth in traffic has largely been driven by video consumption, and over the next several years, new applications leveraging large language model (“LLM”) AI are expected to dramatically increase network bandwidth usage.

**Ribbon Communications Inc.  (RBBN)  (CIK** — 10-K, filed 2026-02-26 — https://www.sec.gov/Archives/edgar/data/1708055/000170805526000012/rbbn-20251231x10k.htm

> New applications enabled by LLM AI will dramatically increase traffic from subscriber devices to the data center.

**DigitalOcean Holdings, Inc.  (DOCN)  (CI** — 10-K, filed 2025-02-25 — https://www.sec.gov/Archives/edgar/data/1582961/000158296125000035/docn-20241231.htm

> In 2024, we released a number of new products and product features, including GPU Droplets, our GenAI platform, Autonomous on our Managed Hosting offering to automatically scale resources based on website traffic, and enhancements to our role-based access control functionality and Backups offering.

**Stagwell Inc  (STGW)  (CIK 0000876883)** — 8-K, filed 2026-03-10 — https://www.sec.gov/Archives/edgar/data/876883/000087688326000004/a4q25earningspresentatio.htm

> EBITDA: $129M Investing IN THE BUSINESS Accelerating GROWTH Improving CASH & COSTS Continuing NEW BUSINESS MOMENTUM Debuted The Machine, marketing's first agentic operating system connecting proprietary data and tools to clients' existing tech stacks Released NewVoices.ai, an independent AI agent for sales conversions and global customer assistance 24/7 Launched Stagwell Search+ in partnership with Emberos, an industry-first agentic tool helping brands navigate AI Search Announced partnership with AppLovin to bring advanced AI-powered mobileadvertising platform Axon into Stagwell’smedia offering Repurchased 5.5M shares in 4Q25 bringing YTD repurchases to 23.1M $106M of net new business in 4Q25, bringing LTM to a record-breaking $476M Secured multiple high profile new customer wins and expansions with leading companies including Target, Microsoft, GrubHub, and Venmo Top 25 customers grew 

### Context windows — filings that state an AI-visibility or AI-referral result, or name an AI-visibility action (sets 1, 2 and per-CIK)

**TechTarget, Inc.  (TTGT)  (CIK 0002018064)** — 10-K 2026-03-11 — https://www.sec.gov/Archives/edgar/data/2018064/000119312526102183/ttgt-20251231.htm

> ...ndamental change in how technology buyers discover and consume information. With the rise of answer engines and AI-driven search, we believe that there is an accompanying skepticism towards generic content. According to our research, over four out of five technology buyers do not fully trust AI today. We believe that our focus is on high-value expert-driven editorial content and specialized audience communities is prescient as audiences seek to verify with trusted sources. We have been seeing a 2x to 3x higher membership conversion rate from answer engine and LLM citations compared to traditional organic search. 13 Table of Contents Delivering decision support content to key audiences that drive purchase behavior We deliver trusted, independent research, primary data, analysis and high-quality editorial content to technology and business professionals that drive purchase behavior in the markets it serves. Our products offer technology buyers and other business professionals the followi...

**TechTarget, Inc.  (TTGT)  (CIK 0002018064)** — 8-K 2025-08-12 — https://www.sec.gov/Archives/edgar/data/2018064/000095017025106920/ttgt-ex99_1.htm

> ... their business decisions, and by informing and accelerating the buying journey. Artificial Intelligence (AI) is evolving the way audiences discover and consume information, including a shift from traditional search to AI-enabled platforms. We have multiple audience engagement strategies that continue to serve us well with active members holding steady. These strategies include Search Engine Optimization (SEO) where our traditional strength translates directly to AI visibility appearing in over 50,000 AI overviews monthly and generating a substantial increase in traffic from AI overviews and with higher conversion rates , but also including the outbound email and newsletter model at Industry Dive which is seeing double-digit growth, partnership models at BrightTALK and NetLine as well as first-party data from Informa PLC. Ultimately, B2B tech buyers require trusted, independent, authoritative sources to support vital technology investment decisions and we continue to prioritize the qua...

**Yext, Inc.  (YEXT)  (CIK 0001614178)** — 8-K 2026-09-01 — https://www.sec.gov/Archives/edgar/data/1614178/000162828026059706/ex993q2fy27productupdatepr.htm

> ...as proven to help multi-location brands increase AI visibility at the local-level by increasing citations by 186% for one hearing care provider. Now, Yext is expanding to offer brand and location-level AI visibility optimization across more sources that AI cites to capture intent at critical times in the consideration process. In early use, the new capabilities have been shown to double inbound leads for a programmatic advertising platform. Yext used its own product to grow its AI visibility by 147% and win share of voice against two leading competitors in only two weeks. Yext is currently piloting it with a small number of enterprise customers ahead of broader availability on September 30. Yext is also continuing to advance Action Center, which reached general availability for all customers on August 5. Action Center allows brands to manage and govern all Yext agents in one place. It now triggers and completes agentic actions surfaced by Scout across listings, reviews, social, and the...

**Yext, Inc.  (YEXT)  (CIK 0001614178)** — 8-K 2026-09-01 — https://www.sec.gov/Archives/edgar/data/1614178/000162828026059706/ex993q2fy27productupdatepr.htm

> ... without a proven path to improve their visibility across these new AI answer surfaces. According to a Corporate Ink survey, 88% of CMOs and VP-level marketers are being asked by leadership or their board about AI visibility. Yet, only 34% of all marketers surveyed say they have a defined AI visibility strategy. Scout is Yext’s comprehensive answer to this problem for enterprises. Scout has proven to help multi-location brands increase AI visibility at the local-level by increasing citations by 186% for one hearing care provider. Now, Yext is expanding to offer brand and location-level AI visibility optimization across more sources that AI cites to capture intent at critical times in the consideration process. In early use, the new capabilities have been shown to double inbound leads for a programmatic advertising platform. Yext used its own product to grow its AI visibility by 147% and win share of voice against two leading competitors in only two weeks. Yext is currently piloting it ...

**JOINT Corp  (JYNT)  (CIK 0001612630)** — 8-K 2026-08-06 — https://www.sec.gov/Archives/edgar/data/1612630/000161263026000063/a8-05x26q22026resultsdec.htm

> ...try into international markets ✓ Leverage shifting consumer trends around: • Longevity; health span; mindfulness; sleep quality; non-invasive whole-body care 8NASDAQ: JYNT | © 2026 The Joint Corp. All Rights Reserved. | Driving Top-Line Momentum Messaging continues to be on chiropractic care for pain relief, and helping patients get back to what they love to do • Sequential improvement in active member growth each month this year • Increasing focus on our MVPs (most valuable patients) • SEO and AI visibility optimization driving organic traffic and lead quality • Positive trends in traffic and high-intent actions on local clinic microsites • New and expanded flexible membership plan options • Rolled out optimized pricing in over 500 clinics 9NASDAQ: JYNT | © 2026 The Joint Corp. All Rights Reserved. | Comp Growth & Patient Retention • Q2 comp sales of (2.8)% improved compared to the first quarter • Comp sales expected to continue improving, throughout the second half of the year • Achi...

**COTY INC.  (COTY)  (CIK 0001024305)** — 10-K 2026-08-20 — https://www.sec.gov/Archives/edgar/data/1024305/000102430526000048/coty-20260630.htm

> ...nd and market data analytics to develop branding, merchandising and marketing execution strategies to maximize the consumer experience and build a better business. We have implemented artificial intelligence (“AI”) tools to power our media allocation models and support content creation and optimization, including search engine optimization copy 2 generation and translation, to improve efficiency and reach of our marketing campaigns. We are also deploying improvements across touchpoints to drive generative engine optimization, to strengthen our brands’ visibility and recommendations by top AI platforms. Distribution Channels and Retail Sales We market, sell and distribute our products in approximately 122 countries and territories, with dedicated local sales forces in most of our significant markets. We have a balanced multi-channel distribution strategy which complements our product categories. Our mass beauty brands are primarily sold through hypermarkets, supermarkets, drug stores an...

**Klarna Group plc  (KLAR)  (CIK 0002003292)** — 6-K 2026-08-18 — https://www.sec.gov/Archives/edgar/data/2003292/000162828026057573/q22026earningsrelease.htm

> .... PSPs bring merchants and merchants bring consumer surfaces. We win when a merchant offers a choice at checkout and we take the largest share of it and that is what drives profitable growth. We are also moving with where consumers search. Klarna's flexible payments are coming to Google Search and the Gemini app within Google Pay, and our AI-powered Shopping Search app is live in ChatGPT, putting our dataset of over 100 million products, and our payments, inside the world's largest AI surfaces. Traffic from AI platforms to retailers grew sharply last holiday season and converts at higher rates. We enter the second half with real momentum. Our payment-platform partnerships are scaling ahead of the holiday season, our new device-upgrade program is ramping, and each new merchant and consumer turns the same flywheel: a wider network, deeper engagement, and better economics on every transaction. 3 Klarna Q2’26 Earnings Release Financial highlights The business executed well and we delivered...

**ETSY INC  (ETSY)  (CIK 0001370637)** — 8-K 2026-04-29 — https://www.sec.gov/Archives/edgar/data/1370637/000137063726000042/q126shareholderletter.htm

> ...overall experience. 6 Integrated agentic experiences, off-site and on Agentic commerce as a driver of incremental traffic to Etsy. Much of the conversation around AI in ecommerce has focused on agentic shopping — and we’re leaning into that opportunity through our partnerships with OpenAI, Microsoft, and Google. We’re encouraged by the early learnings shared on our last earnings call — and data continues to support strong growth in traffic and high-intent engagement from buyers who come to Etsy through agentic search. We see this ch annel as an important and growing source of discovery — particularly for a marketplace like Etsy, which has high brand awareness, but has historically lacked buyer consideration for the many types of purchase occasions we can serve. These are early partnerships in a space that is evolving rapidly: for example, we recently developed an Etsy App in ChatGPT, aligned with Open AI’s shift for agentic shopping to be focused on retailer-run apps. We’re also leanin...

**Rent the Runway, Inc.  (RENT)  (CIK 0001468327)** — 10-Q 2026-09-11 — https://www.sec.gov/Archives/edgar/data/1468327/000146832726000088/rent-20260731.htm

> ...our base of new customers. In addition, we continue to focus on growing traffic and conversion rates by optimizing our organic social media channels, improving our email marketing performance, refreshing our lifecycle marketing engine, increasing paid marketing efficiency, focusing on referrals and other community-driven “word of mouth” strategies, and aiming to optimize discovery via search engine optimization, agentic search, and enhanced iOS App Store presence. These efforts are ongoing and, although we have seen some positive results, they are subject to change and may not result in a sustained increase in customer conversion, loyalty or engagement.The impact of emerging technologies, including, but not limited to, AI tools such as agentic search, is not yet certain and may increase these risks. See “Our use of AI may subject us to new or heightened legal, regulatory, ethical, operational or other challenges.” As a result, our levels of paid and organic growth may continue to fluct...

**ZIPRECRUITER, INC.  (ZIP)  (CIK 0001617553)** — 8-K 2026-05-07 — https://www.sec.gov/Archives/edgar/data/1617553/000161755326000030/q12026shareholderletter-.htm

> ...blishing us as the preferred destination across both traditional search engines and emerging AI assistants. On the SEO front, we are seeing strong growth in high-intent traffic, despite a year-over-year decline in total web traffic across the category5. In Q1, engaged job seekers, defined as those who applied to job postings, grew 26% year-over-year through organic search. Simultaneously, we are expanding our distribution across emerging generative AI platforms. In late March, we launched a new ZipRecruiter app for ChatGPT, bringing the power of our marketplace directly into the generative AI tool. This integration extends our reach to where job seekers are increasingly starting their search, while demonstrating the strength of the ZipRecruiter brand and marketplace. We see this as an early step in broadening our presence across generative AI platforms and will look to expand our integrations over time. Taken together — our increased share of total traffic, 26% year-over-year growth in...

**High Roller Technologies, Inc.  (ROLR)  (CIK 0001947210)** — 8-K 2026-04-20 — https://www.sec.gov/Archives/edgar/data/1947210/000175392626000693/ex992_3.htm

> ...es a rapidly growing, sports-focused social media network of 4+ million followers, with content achieving over 500 million views in the last 30 days. The partnership is structured to introduce High Roller’s regulated prediction market offerings to audiences already familiar with implied probability, odds-based decision-making, and event-driven trading dynamics. In addition to traditional search visibility, Lines.com has established a leadership position across AI-driven discovery channels, with nearly 800 AI citations spanning platforms such as Google AI Overview, ChatGPT, Perplexity, and Gemini—more than three times that of key competitors. This AI-native visibility is expected to further enhance High Roller’s brand discovery as consumers increasingly rely on AI-powered tools to evaluate market-based products. The Lines.com agreement represents a core component of High Roller’s broader strategy to combine regulated infrastructure, premium consumer experience, and scalable digital dist...

**YELP INC  (YELP)  (CIK 0001345016)** — 8-K 2026-08-06 — https://www.sec.gov/Archives/edgar/data/1345016/000134501626000059/yelpq22026ex992lettertos.htm

> ...ccelerated product velocity Ye lp Q 2 20 26 9 23 Extend our reach to power local discovery across the AI ecosystem As local discovery moves beyond traditional search into new devices, apps and AI-powered interfaces, we believe Yelp is well positioned to serve as an essential partner wherever consumers are making local decisions. In fact, we commissioned a recent study that found Yelp was the most organically cited home services discovery platform by LLMs in the fourth quarter of 2025, receiving 3.4x as many AI citations than the next closest platform.5 Through data licensing and APIs, we are extending the reach of our trusted content to provide consumers with reliable local answers. In the second quarter, we saw robust demand for our data licensing products, including from our partnership with OpenAI, contributing to strong growth in other revenue. Yelp ratings and reviews recently began powering ChatGPT’s local experience in relevant categories. Request-a-Quote integration with ChatGP...

**Freshworks Inc.  (FRSH)  (CIK 0001544522)** — 10-K 2026-02-26 — https://www.sec.gov/Archives/edgar/data/1544522/000154452226000036/frsh-20251231.htm

> ...outside our control. The search ecosystem is also evolving to include AI-generated responses and standalone AI search experiences, which increasingly provide answers without requiring users to click through to a website. These changes have contributed to a rise in “zero-click” searches, which could have an adverse impact on business, results of operations, and financial condition. Historically, traffic to our websites from search engines has been driven by our position in unpaid search results. Traffic from large language model (LLM)-based platforms currently represents a small portion of our total website traffic but has been growing in recent quarters. As these platforms become more widely adopted, they may become a more material component of our customer acquisition strategy. 23 Table of Contents At the same time, the rise of AI-powered search may reduce the effectiveness of traditional SEO strategies. Our rankings and visibility may be affected by changes to search engine algorithm...

**https://www.sec.gov/Archives/edgar/data/1404655/000119312526182210/hubs-20260427.htm** —   — https://www.sec.gov/Archives/edgar/data/1404655/000119312526182210/hubs-20260427.htm

> ...I agents the full context they need to act with confidence. New features to persona-based Hubs for marketing, sales, and service: Marketing Hub. We launched the Loop Marketing playbook and Marketing Studio to help marketers win in the age of AI — introducing AI-powered email personalization and optimized send timing, an AI-driven Segments feature to surface high-intent audiences, and A nswer Engine Optimization (“AEO”) to help brands appear in large language model (“LLM”) driven search results. AI referrals are now tracked as a lead source. Content Hub . Content Hub serves as the all-in-one content marketing solution, with AI-driven creation, brand voice management, and podcast tooling now tightly integrated with Marketing Studio — enabling teams to plan, create, and repurpose content across the customer journey from a single workspace. Sales Hub . In 2025, Sales Hub sharpened deal prioritization with Predictive Deal Score and Meeting Notetaker, which turn calls, emails, and meetings i...

**https://www.sec.gov/Archives/edgar/data/1795586/000162827925000036/filename1.htm** —   — https://www.sec.gov/Archives/edgar/data/1795586/000162827925000036/filename1.htm

> ...embers build their credit scores. 112 In addition to highlighting our products individually, our product-led marketing content also holistically emphasizes the value our platform can bring as a central part of our members’ financial lives. • Data-Driven Member Acquisition: We use an efficient, data-driven member acquisition strategy to fuel growth through search engine optimization (“SEO”) and targeted paid media. Our SEO approach focuses on creating high-impact content utilizing our AI-powered Chime Content GPT — which is a generative AI solution using ChatGPT to leverage the knowledge base of our best performing blogs, editorial pieces, and videos for the creation of new content — in partnership with our internal editorial team and certified financial writers. We believe our content generation strategy has put Chime in a strong position compared to traditional banks in organic search results for the key financial categories that resonate most with everyday Americans. Within targeted ...

**LendingTree, Inc.  (TREE)  (CIK 0001434621)** — 8-K 2026-07-29 — https://www.sec.gov/Archives/edgar/data/1434621/000162828026050633/tree-63026xer.htm

> ...today announced results for the quarter ended June 30, 2026. The company has posted a letter to shareholders on the company's website at investors.lendingtree.com. "We posted our eighth straight quarter of double-digit year-over-year adjusted EBITDA growth in Q2, powered by another solid quarter from our Insurance segment," said Scott Peyree, CEO. "We also accomplished a great deal on the product and AI front during the period. We launched several new consumer-facing AI capabilities such as our ChatGPT app, expanded our marketplace into six new verticals, and we are continuing to see strong results from our homepage redesign. We remain laser focused as a team on executing our strategy to become the Number One Destination to Shop For Financial Products." Jason Bengel, CFO, commented, "Solid Insurance segment results were offset by weaker than expected Consumer performance in Q2. Last quarter we called out an expected sequential decline in Consumer, driven by suppressed borrower demand i...

### Full hit list — every document returned by sets 1 and 2 (company | form | filed | URL | queries)

| Company | Form | Filed | URL | Queries |
|---|---|---|---|---|
| 1 800 FLOWERS COM INC  (FLWS)  (CIK 0001084869) | 10-K | 2026-09-11 | https://www.sec.gov/Archives/edgar/data/1084869/000108486926000029/flws-20260628.htm | "AI search" "conversion"; "AI search" "traffic" |
| 1stdibs.com, Inc.  (DIBS)  (CIK 0001600641) | 8-K | 2026-09-02 | https://www.sec.gov/Archives/edgar/data/1600641/000160064126000040/final_roadmapreviewx2026.htm | "AI search" "conversion"; "AI search" "traffic" |
| 8X8 INC /DE/  (EGHT)  (CIK 0001023731) | 10-K | 2026-05-22 | https://www.sec.gov/Archives/edgar/data/1023731/000102373126000041/eght-20260331.htm | "AI platforms" "referrals" |
| ADOBE INC.  (ADBE)  (CIK 0000796343) | 10-K | 2026-01-15 | https://www.sec.gov/Archives/edgar/data/796343/000079634326000003/adbe-20251128.htm | "AI assistants" "traffic"; "AI-powered search" "traffic"; "generative engine optimization" |
| ADOBE INC.  (ADBE)  (CIK 0000796343) | 10-Q | 2026-06-15 | https://www.sec.gov/Archives/edgar/data/796343/000079634326000112/adbe-20260529.htm | "agentic search"; "generative engine optimization" |
| ADOBE INC.  (ADBE)  (CIK 0000796343) | 10-Q | 2026-09-22 | https://www.sec.gov/Archives/edgar/data/796343/000079634326000156/adbe-20260828.htm | "agentic search"; "generative engine optimization" |
| AGNT, Inc.  (AGNT)  (CIK 0001495932) | 10-Q | 2026-08-04 | https://www.sec.gov/Archives/edgar/data/1495932/000110465926090337/agnt-20260630xex10d14.htm | "AI platforms" "referrals"; "ChatGPT" "referral"; "ChatGPT" "traffic" |
| AI Unlimited Group, Inc.  (AIUG)  (CIK 0001932244) | S-1 | 2025-02-14 | https://www.sec.gov/Archives/edgar/data/1932244/000149315225006887/forms-1.htm | "AI assistants" "traffic" |
| AIAI Holdings Corp  (AIAI)  (CIK 0002096362) | S-1/A | 2026-03-04 | https://www.sec.gov/Archives/edgar/data/2096362/000149315226008887/forms-1a.htm | "AI platforms" "referrals" |
| AIAI Holdings Corp  (AIAI)  (CIK 0002096362) | S-1/A | 2026-03-23 | https://www.sec.gov/Archives/edgar/data/2096362/000149315226012102/forms-1a.htm | "AI platforms" "referrals" |
| AIAI Holdings Corp  (AIAI)  (CIK 0002096362) | S-1/A | 2026-04-08 | https://www.sec.gov/Archives/edgar/data/2096362/000149315226015707/forms-1a.htm | "AI platforms" "referrals" |
| AIAI Holdings Corp  (AIAI)  (CIK 0002096362) | S-1/A | 2026-04-20 | https://www.sec.gov/Archives/edgar/data/2096362/000149315226018040/forms-1a.htm | "AI platforms" "referrals" |
| AIAI Holdings Corp  (AIAI)  (CIK 0002096362) | S-1/A | 2026-04-24 | https://www.sec.gov/Archives/edgar/data/2096362/000149315226018924/forms-1a.htm | "AI platforms" "referrals" |
| AIAI Holdings Corp  (AIAI)  (CIK 0002096362) | S-1/A | 2026-04-30 | https://www.sec.gov/Archives/edgar/data/2096362/000149315226020261/forms-1a.htm | "AI platforms" "referrals" |
| AIAI Holdings Corp  (AIAI)  (CIK 0002096362) | S-1/A | 2026-05-01 | https://www.sec.gov/Archives/edgar/data/2096362/000149315226020803/forms-1a.htm | "AI platforms" "referrals" |
| AIAI Holdings Corp  (AIAI)  (CIK 0002096362) | 424B4 | 2026-05-14 | https://www.sec.gov/Archives/edgar/data/2096362/000149315226022855/form424b4.htm | "AI platforms" "referrals" |
| AIAI Holdings Corp  (CIK 0002096362) | S-1 | 2026-01-26 | https://www.sec.gov/Archives/edgar/data/2096362/000149315226003639/forms-1.htm | "AI platforms" "referrals" |
| AIRWA INC.  (YYAI)  (CIK 0001674440) | 10-K | 2026-09-21 | https://www.sec.gov/Archives/edgar/data/1674440/000149315226043608/form10-k.htm | "AI platforms" "referrals" |
| AKAMAI TECHNOLOGIES INC  (AKAM)  (CIK 0001086222) | 10-K | 2026-02-20 | https://www.sec.gov/Archives/edgar/data/1086222/000108622226000022/akam-20251231.htm | "LLMs" "referral" |
| AMAZE HOLDINGS, INC.  (AMZE)  (CIK 0001880343) | S-1 | 2025-06-06 | https://www.sec.gov/Archives/edgar/data/1880343/000155479525000153/amze0606forms1.htm | "large language models" "organic traffic" |
| AMAZE HOLDINGS, INC.  (AMZE)  (CIK 0001880343) | S-1/A | 2025-06-23 | https://www.sec.gov/Archives/edgar/data/1880343/000155479525000165/amze0619forms1a1.htm | "large language models" "organic traffic" |
| AMAZON COM INC  (AMZN)  (CIK 0001018724) | 8-K | 2026-04-09 | https://www.sec.gov/Archives/edgar/data/1018724/000110465926041034/tm263815d3_ex99-1.htm | "ChatGPT" "traffic" |
| AMBARELLA INC  (AMBA)  (CIK 0001280263) | 10-K | 2025-03-28 | https://www.sec.gov/Archives/edgar/data/1280263/000095017025046499/amba-20250131.htm | "LLM" "referral"; "LLMs" "referral" |
| AMBARELLA INC  (AMBA)  (CIK 0001280263) | 10-K | 2026-03-23 | https://www.sec.gov/Archives/edgar/data/1280263/000119312526119321/amba-20260131.htm | "LLM" "referral"; "LLMs" "referral" |
| AMC Robotics Corp  (AMCI)  (CIK 0001937891) | S-1/A | 2026-01-16 | https://www.sec.gov/Archives/edgar/data/1937891/000149315226002555/forms-1a.htm | "ChatGPT" "traffic" |
| AMC Robotics Corp  (AMCI, ATMV, ATMVR, ATMVU)  (CIK 00019378 | S-1 | 2025-12-30 | https://www.sec.gov/Archives/edgar/data/1937891/000149315225029590/forms-1.htm | "ChatGPT" "traffic" |
| AMERICAN REBEL HOLDINGS INC  (AREB, AREBW)  (CIK 0001648087) | 10-Q | 2025-11-10 | https://www.sec.gov/Archives/edgar/data/1648087/000149315225021519/ex99-25.htm | "answer engine" |
| ASGN Inc  (ASGN)  (CIK 0000890564) | 10-K | 2026-02-25 | https://www.sec.gov/Archives/edgar/data/890564/000089056426000013/asgn-20251231.htm | "AI platforms" "referrals" |
| ASIAFIN HOLDINGS CORP.  (ASFH)  (CIK 0001828748) | S-1/A | 2026-04-28 | https://www.sec.gov/Archives/edgar/data/1828748/000121390026048351/ea0286904-s1a3_asiafin.htm | "ChatGPT" "referral" |
| AXCELIS TECHNOLOGIES INC  (ACLS)  (CIK 0001113232) | 10-K | 2025-02-28 | https://www.sec.gov/Archives/edgar/data/1113232/000155837025001855/acls-20241231x10k.htm | "ChatGPT" "bookings" |
| AXCELIS TECHNOLOGIES INC  (ACLS)  (CIK 0001113232) | 10-K | 2026-02-26 | https://www.sec.gov/Archives/edgar/data/1113232/000110465926020461/acls-20251231x10k.htm | "ChatGPT" "bookings" |
| Absci Corp  (ABSI)  (CIK 0001672688) | 8-K | 2026-03-24 | https://www.sec.gov/Archives/edgar/data/1672688/000167268826000066/generalcorporatepresenta.htm | "AI discovery" |
| Accelerant Holdings  (ARX)  (CIK 0001997350) | S-1/A | 2025-07-15 | https://www.sec.gov/Archives/edgar/data/1997350/000119312525159018/d543111ds1a.htm | "LLM" "referral"; "LLMs" "referral" |
| Accelerant Holdings  (ARX)  (CIK 0001997350) | S-1/A | 2025-07-18 | https://www.sec.gov/Archives/edgar/data/1997350/000119312525161013/d543111ds1a.htm | "LLM" "referral"; "LLMs" "referral" |
| Accelerant Holdings  (ARX)  (CIK 0001997350) | 424B4 | 2025-07-25 | https://www.sec.gov/Archives/edgar/data/1997350/000119312525164549/d543111d424b4.htm | "LLM" "referral"; "LLMs" "referral" |
| Accelerant Holdings  (CIK 0001997350) | S-1 | 2025-06-30 | https://www.sec.gov/Archives/edgar/data/1997350/000119312525152889/d543111ds1.htm | "LLM" "referral"; "LLMs" "referral" |
| Aclarion, Inc.  (ACON, ACONW)  (CIK 0001635077) | S-1/A | 2025-01-10 | https://www.sec.gov/Archives/edgar/data/1635077/000168316825000233/aclarion_s1a2.htm | "AI platforms" "referrals" |
| Aclarion, Inc.  (ACON, ACONW)  (CIK 0001635077) | 424B4 | 2025-01-16 | https://www.sec.gov/Archives/edgar/data/1635077/000168316825000389/aclarion_424b4.htm | "AI platforms" "referrals" |
| Aclarion, Inc.  (ACON, ACONW)  (CIK 0001635077) | 10-K | 2025-04-09 | https://www.sec.gov/Archives/edgar/data/1635077/000168316825002351/aclarion_i10k-123124.htm | "AI platforms" "referrals" |
| Aclarion, Inc.  (ACON, ACONW)  (CIK 0001635077) | 10-K | 2026-03-18 | https://www.sec.gov/Archives/edgar/data/1635077/000168316826001986/aclarion_i10k-123125.htm | "AI platforms" "referrals" |
| Acrivon Therapeutics, Inc.  (ACRV)  (CIK 0001781174) | 10-K | 2025-03-27 | https://www.sec.gov/Archives/edgar/data/1781174/000095017025046056/acrv-20241231.htm | "AI platforms" "referrals" |
| Acrivon Therapeutics, Inc.  (ACRV)  (CIK 0001781174) | 10-K | 2026-03-19 | https://www.sec.gov/Archives/edgar/data/1781174/000119312526115123/acrv-20251231.htm | "AI platforms" "referrals" |
| Adaptive Biotechnologies Corp  (ADPT)  (CIK 0001478320) | 8-K | 2026-01-12 | https://www.sec.gov/Archives/edgar/data/1478320/000119312526009840/d29941dex992.htm | "AI discovery" |
| Aether Holdings, Inc.  (ATHR)  (CIK 0002026353) | 10-K | 2025-12-17 | https://www.sec.gov/Archives/edgar/data/2026353/000149315225028195/form10-k.htm | "LLM" "referral" |
| Airbnb, Inc.  (ABNB)  (CIK 0001559720) | 8-K | 2025-11-06 | https://www.sec.gov/Archives/edgar/data/1559720/000119312525269432/d40503dex991.htm | "AI-powered search" "traffic" |
| Airbnb, Inc.  (ABNB)  (CIK 0001559720) | 8-K | 2026-02-12 | https://www.sec.gov/Archives/edgar/data/1559720/000119312526048670/d58192dex991.htm | "AI-powered search" "traffic" |
| Akso Health Group  (AHG)  (CIK 0001702318) | 20-F | 2025-08-14 | https://www.sec.gov/Archives/edgar/data/1702318/000121390025076862/ea0250582-20f_akso.htm | "ChatGPT" "traffic" |
| Akso Health Group  (AHG)  (CIK 0001702318) | 20-F | 2026-07-23 | https://www.sec.gov/Archives/edgar/data/1702318/000121390026080868/ea0294288-20f_akso.htm | "ChatGPT" "traffic" |
| Alarm.com Holdings, Inc.  (ALRM)  (CIK 0001459200) | 10-K | 2026-02-19 | https://www.sec.gov/Archives/edgar/data/1459200/000145920026000005/alrm-20251231.htm | "AI-powered search" "traffic" |
| Alarum Technologies Ltd.  (ALAR)  (CIK 0001725332) | 6-K | 2026-05-28 | https://www.sec.gov/Archives/edgar/data/1725332/000121390026061770/ea029228701ex99-2.htm | "ChatGPT" "traffic" |
| Alibaba Group Holding Ltd  (BABA, BABAF, BBAAY)  (CIK 000157 | 20-F | 2025-06-26 | https://www.sec.gov/Archives/edgar/data/1577552/000095017025090161/baba-ex15_5.htm | "AI search" "conversion"; "AI search" "traffic" |
| Alibaba Group Holding Ltd  (BABA, BABAF, BBAAY)  (CIK 000157 | 6-K | 2025-06-26 | https://www.sec.gov/Archives/edgar/data/1577552/000110465925062815/tm2519164d1_ex99-1.pdf | "AI search" "conversion"; "AI search" "traffic" |
| Alibaba Group Holding Ltd  (BABA, BABAF, BBAAY)  (CIK 000157 | 20-F | 2026-05-20 | https://www.sec.gov/Archives/edgar/data/1577552/000119312526231755/baba-20260331.htm | "large language models" "organic traffic" |
| Alphabet Inc.  (GOOG, GOOGL)  (CIK 0001652044) | 8-K | 2025-02-04 | https://www.sec.gov/Archives/edgar/data/1652044/000165204425000010/googexhibit991q42024.htm | "AI Overviews" "traffic" |
| Alphabet Inc.  (GOOG, GOOGL)  (CIK 0001652044) | 10-K | 2025-02-05 | https://www.sec.gov/Archives/edgar/data/1652044/000165204425000014/goog-20241231.htm | "AI Overviews" "traffic"; "AI platforms" "referrals" |
| Alphabet Inc.  (GOOG, GOOGL)  (CIK 0001652044) | 8-K | 2025-04-24 | https://www.sec.gov/Archives/edgar/data/1652044/000165204425000040/googexhibit991q12025.htm | "AI Overviews" "traffic" |
| Alphabet Inc.  (GOOG, GOOGL)  (CIK 0001652044) | 8-K | 2025-07-23 | https://www.sec.gov/Archives/edgar/data/1652044/000165204425000056/googexhibit991q22025.htm | "AI Mode" "traffic"; "AI Overviews" "traffic" |
| Alphabet Inc.  (GOOG, GOOGL)  (CIK 0001652044) | 8-K | 2025-10-29 | https://www.sec.gov/Archives/edgar/data/1652044/000165204425000087/googexhibit991q32025.htm | "AI Mode" "traffic"; "AI Overviews" "traffic" |
| Alphabet Inc.  (GOOG, GOOGL)  (CIK 0001652044) | 10-K | 2026-02-05 | https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm | "AI Mode" "traffic"; "AI Overviews" "traffic"; "AI platforms" "referrals" |
| Amber International Holding Ltd  (AMBR)  (CIK 0001697818) | 6-K | 2026-09-10 | https://www.sec.gov/Archives/edgar/data/1697818/000110465926106504/ambr-20260910xex99d2.htm | "AI search" "conversion" |
| Ambiq Micro, Inc.  (AMBQ)  (CIK 0001500412) | S-1/A | 2025-07-21 | https://www.sec.gov/Archives/edgar/data/1500412/000119312525161443/d377490ds1a.htm | "ChatGPT" "new members" |
| Ambiq Micro, Inc.  (AMBQ)  (CIK 0001500412) | 424B4 | 2025-07-31 | https://www.sec.gov/Archives/edgar/data/1500412/000119312525169401/d377490d424b4.htm | "ChatGPT" "new members" |
| Ambiq Micro, Inc.  (AMBQ)  (CIK 0001500412) | S-1 | 2026-01-21 | https://www.sec.gov/Archives/edgar/data/1500412/000119312526017240/d62272ds1.htm | "ChatGPT" "new members" |
| Ambiq Micro, Inc.  (AMBQ)  (CIK 0001500412) | 424B4 | 2026-01-26 | https://www.sec.gov/Archives/edgar/data/1500412/000119312526021460/d62272d424b4.htm | "ChatGPT" "new members" |
| Ambiq Micro, Inc.  (CIK 0001500412) | S-1 | 2025-07-03 | https://www.sec.gov/Archives/edgar/data/1500412/000119312525155270/d377490ds1.htm | "ChatGPT" "new members" |
| Amplitude, Inc.  (AMPL)  (CIK 0001866692) | 8-K | 2025-11-05 | https://www.sec.gov/Archives/edgar/data/1866692/000119312525266930/ampl-ex99_1.htm | "AI visibility" |
| Amplitude, Inc.  (AMPL)  (CIK 0001866692) | 10-K | 2026-02-19 | https://www.sec.gov/Archives/edgar/data/1866692/000119312526057847/ampl-20251231.htm | "AI search" "conversion"; "AI search" "traffic"; "AI visibility" |
| Amplitude, Inc.  (AMPL)  (CIK 0001866692) | 10-Q | 2026-05-07 | https://www.sec.gov/Archives/edgar/data/1866692/000119312526209631/ampl-20260331.htm | "AI search" "conversion"; "AI search" "traffic"; "AI visibility" |
| Amplitude, Inc.  (AMPL)  (CIK 0001866692) | 10-Q | 2026-08-06 | https://www.sec.gov/Archives/edgar/data/1866692/000119312526335706/ampl-20260630.htm | "AI search" "conversion"; "AI search" "traffic"; "AI visibility" |
| Andersen Group Inc.  (ANDG)  (CIK 0002065708) | S-1/A | 2025-11-19 | https://www.sec.gov/Archives/edgar/data/2065708/000119312525288325/d921520ds1a.htm | "LLM" "referral"; "LLMs" "referral" |
| Andersen Group Inc.  (ANDG)  (CIK 0002065708) | S-1/A | 2025-12-08 | https://www.sec.gov/Archives/edgar/data/2065708/000119312525310538/d921520ds1a.htm | "LLM" "referral"; "LLMs" "referral" |
| Andersen Group Inc.  (ANDG)  (CIK 0002065708) | 424B4 | 2025-12-17 | https://www.sec.gov/Archives/edgar/data/2065708/000119312525322948/d921520d424b4.htm | "LLM" "referral"; "LLMs" "referral" |
| Andersen Group Inc.  (ANDG)  (CIK 0002065708) | 10-K | 2026-03-27 | https://www.sec.gov/Archives/edgar/data/2065708/000119312526128949/d63874d10k.htm | "LLM" "referral"; "LLMs" "referral" |
| Andersen Group Inc.  (CIK 0002065708) | S-1 | 2025-09-19 | https://www.sec.gov/Archives/edgar/data/2065708/000119312525209262/d921520ds1.htm | "LLM" "referral"; "LLMs" "referral" |
| Aptevo Therapeutics Inc.  (APVO)  (CIK 0001671584) | 10-K | 2025-02-14 | https://www.sec.gov/Archives/edgar/data/1671584/000095017025020467/apvo-20241231.htm | "LLM" "referral" |
| Aptevo Therapeutics Inc.  (APVO)  (CIK 0001671584) | 10-K | 2026-03-26 | https://www.sec.gov/Archives/edgar/data/1671584/000119312526126278/apvo-20251231.htm | "LLM" "referral" |
| Aptorum Group Ltd  (APM)  (CIK 0001734005) | 6-K | 2025-10-08 | https://www.sec.gov/Archives/edgar/data/1734005/000121390025097467/ea026056301ex99-1_aptorum.htm | "LLM" "referral" |
| Aptorum Group Ltd  (APM)  (CIK 0001734005) | F-1 | 2025-11-17 | https://www.sec.gov/Archives/edgar/data/1734005/000121390025111548/ea0263151-f1_aptorum.htm | "LLM" "referral" |
| Aptorum Group Ltd  (APM)  (CIK 0001734005) | 6-K | 2026-03-31 | https://www.sec.gov/Archives/edgar/data/1734005/000121390026037563/ea0284133ex99-1_aptorum.htm | "LLM" "referral" |
| Aptorum Group Ltd  (APM)  (CIK 0001734005) | 6-K | 2026-05-14 | https://www.sec.gov/Archives/edgar/data/1734005/000121390026056820/ea029049401ex99-1.htm | "LLM" "referral" |
| Arena Group Holdings, Inc.  (AREN)  (CIK 0000894871) | 10-Q | 2026-08-10 | https://www.sec.gov/Archives/edgar/data/894871/000162828026055208/aren-20260630.htm | "AI-driven traffic" |
| Arrive AI Inc.  (ARAI)  (CIK 0001818274) | S-1/A | 2025-01-27 | https://www.sec.gov/Archives/edgar/data/1818274/000149315225003660/forms-1a.htm | "ChatGPT" "traffic" |
| Arrive AI Inc.  (ARAI)  (CIK 0001818274) | S-1/A | 2025-03-24 | https://www.sec.gov/Archives/edgar/data/1818274/000164117225000350/forms-1a.htm | "ChatGPT" "traffic" |
| Arrive AI Inc.  (ARAI)  (CIK 0001818274) | S-1/A | 2025-04-18 | https://www.sec.gov/Archives/edgar/data/1818274/000164117225005394/forms-1a.htm | "ChatGPT" "traffic" |
| Arrive AI Inc.  (ARAI)  (CIK 0001818274) | S-1/A | 2025-05-13 | https://www.sec.gov/Archives/edgar/data/1818274/000164117225009841/forms-1a.htm | "ChatGPT" "traffic" |
| Arrive AI Inc.  (ARAI)  (CIK 0001818274) | 424B4 | 2025-05-15 | https://www.sec.gov/Archives/edgar/data/1818274/000164117225010892/form424b4.htm | "ChatGPT" "traffic" |
| Arrive AI Inc.  (ARAI)  (CIK 0001818274) | S-1 | 2025-06-17 | https://www.sec.gov/Archives/edgar/data/1818274/000164117225015428/forms-1.htm | "ChatGPT" "traffic" |
| Arrive AI Inc.  (ARAI)  (CIK 0001818274) | S-1/A | 2025-07-15 | https://www.sec.gov/Archives/edgar/data/1818274/000164117225019572/forms-1a.htm | "ChatGPT" "traffic" |
| Arrive AI Inc.  (ARAI)  (CIK 0001818274) | S-1 | 2026-02-10 | https://www.sec.gov/Archives/edgar/data/1818274/000149315226005967/forms-1.htm | "ChatGPT" "traffic" |
| Arrive AI Inc.  (ARAI)  (CIK 0001818274) | 10-K | 2026-04-15 | https://www.sec.gov/Archives/edgar/data/1818274/000149315226016808/form10-k.htm | "ChatGPT" "traffic" |
| Asset Entities Inc.  (ASST)  (CIK 0001920406) | 10-K | 2025-03-31 | https://www.sec.gov/Archives/edgar/data/1920406/000121390025026431/ea0235693-10k_assetenti.htm | "ChatGPT" "traffic" |
| Athena Technology Acquisition Corp. II  (ATEK, ATEKU, ATEKW) | 10-K | 2026-03-11 | https://www.sec.gov/Archives/edgar/data/1882198/000121390026025927/ea0280158-10k_athena2.htm | "AI search" "conversion" |
| Atlantic Union Bankshares Corp  (AUB, AUB-PA)  (CIK 00008839 | 8-K | 2025-12-10 | https://www.sec.gov/Archives/edgar/data/883948/000088394825000114/aub-20251210xex99d1.htm | "AI Overviews" "traffic"; "AI-powered search" "traffic"; "ChatGPT" "referral"; "ChatGPT" "traffic"; "Perplexity" "traffic"; "generative engine optimization" |
| Atlassian Corp  (TEAM)  (CIK 0001650372) | 10-K | 2025-08-15 | https://www.sec.gov/Archives/edgar/data/1650372/000165037225000036/team-20250630.htm | "AI search" "conversion"; "AI search" "traffic" |
| Atlassian Corp  (TEAM)  (CIK 0001650372) | 10-K | 2026-08-14 | https://www.sec.gov/Archives/edgar/data/1650372/000165037226000036/team-20260630.htm | "AI assistants" "traffic"; "AI search" "conversion"; "AI search" "traffic" |
| Avalon GloboCare Corp.  (ALBT)  (CIK 0001630212) | S-1 | 2026-07-13 | https://www.sec.gov/Archives/edgar/data/1630212/000121390026077307/ea0297456-s1_avalon.htm | "AI search" "conversion"; "AI search" "traffic"; "AI visibility"; "AI-powered search" "traffic"; "ChatGPT" "traffic"; "Perplexity" "traffic"; "generative engine optimization" |
| BANK OF CHILE  (BCH)  (CIK 0001161125) | 6-K | 2026-03-06 | https://www.sec.gov/Archives/edgar/data/1161125/000121390026024652/ea028019201ex99-1.pdf | "AI assistants" "traffic" |
| BANK OF MONTREAL /CAN/  (BMO, BERZ, BNKD, BNKU, BULZ, CARD,  | 6-K | 2025-03-06 | https://www.sec.gov/Archives/edgar/data/927971/000119312525048406/d922553dex991.htm | "ChatGPT" "new members" |
| BANK OF NOVA SCOTIA  (BNS)  (CIK 0000009631) | 6-K | 2025-03-07 | https://www.sec.gov/Archives/edgar/data/9631/000119312525049073/d930721dex991.htm | "ChatGPT" "new members" |
| BANK OF NOVA SCOTIA  (BNS)  (CIK 0000009631) | 6-K | 2025-12-02 | https://www.sec.gov/Archives/edgar/data/9631/000119312525304603/d41644dex992.htm | "LLM" "referral" |
| BANK OF NOVA SCOTIA  (BNS)  (CIK 0000009631) | 6-K | 2025-12-02 | https://www.sec.gov/Archives/edgar/data/9631/000119312525304609/d10762dex991.pdf | "LLM" "referral" |
| BCE INC  (BCE, BCAEF, BCEFF, BCENF, BCEPF, BCEXF, BCPPF, BEC | 6-K | 2025-11-06 | https://www.sec.gov/Archives/edgar/data/718940/000071894025000019/a2025-q3xmda.htm | "answer engine" |
| BED BATH & BEYOND, INC.  (BBBY)  (CIK 0001130713) | 10-Q | 2025-10-27 | https://www.sec.gov/Archives/edgar/data/1130713/000113071325000078/byon-20250930.htm | "ChatGPT" "traffic"; "answer engines" |
| BED BATH & BEYOND, INC.  (BBBY, BBBY-WT)  (CIK 0001130713) | 10-K | 2026-02-24 | https://www.sec.gov/Archives/edgar/data/1130713/000113071326000018/bbby-20251231.htm | "ChatGPT" "referral"; "ChatGPT" "traffic"; "answer engines" |
| BEST BUY CO INC  (BBY)  (CIK 0000764478) | 10-K | 2026-03-18 | https://www.sec.gov/Archives/edgar/data/764478/000076447826000009/bby-20260131.htm | "AI-powered search" "traffic" |
| BICYCLE THERAPEUTICS PLC  (BCYC)  (CIK 0001761612) | 10-K | 2025-02-25 | https://www.sec.gov/Archives/edgar/data/1761612/000155837025001438/bcyc-20241231x10k.htm | "AI platforms" "referrals" |
| BIOREGENX, INC.  (BRGX)  (CIK 0001593184) | 10-K | 2025-04-15 | https://www.sec.gov/Archives/edgar/data/1593184/000168316825002614/bioregenx_i10k-123124.htm | "AI-powered search" "traffic" |
| BIOREGENX, INC.  (BRGX)  (CIK 0001593184) | 10-K/A | 2025-04-16 | https://www.sec.gov/Archives/edgar/data/1593184/000168316825002623/bioregenx_i10ka1-123124.htm | "AI-powered search" "traffic" |
| BIOREGENX, INC.  (BRGX)  (CIK 0001593184) | 10-K | 2026-04-15 | https://www.sec.gov/Archives/edgar/data/1593184/000168316826002975/bioregenx_i10k-123125.htm | "AI-powered search" "traffic" |
| BITMINE IMMERSION TECHNOLOGIES, INC.  (BMNP, BMNR)  (CIK 000 | 8-K | 2026-07-16 | https://www.sec.gov/Archives/edgar/data/1829311/000149315226033460/ex99-2.htm | "ChatGPT" "traffic" |
| BITMINE IMMERSION TECHNOLOGIES, INC.  (BMNR)  (CIK 000182931 | 8-K | 2026-05-11 | https://www.sec.gov/Archives/edgar/data/1829311/000149315226022150/ex99-2.htm | "ChatGPT" "traffic" |
| BLACKLINE, INC.  (BL)  (CIK 0001666134) | 10-K | 2026-02-26 | https://www.sec.gov/Archives/edgar/data/1666134/000162828026011915/bl-20251231.htm | "LLMs" "referral" |
| BOX INC  (BOX, BXCAP)  (CIK 0001372612) | 10-Q | 2026-08-26 | https://www.sec.gov/Archives/edgar/data/1372612/000119312526368289/box-20260731.htm | "ChatGPT" "traffic" |
| Baidu, Inc.  (BIDU, BAIDF)  (CIK 0001329099) | 20-F | 2025-03-28 | https://www.sec.gov/Archives/edgar/data/1329099/000119312525066199/d853848d20f.htm | "ChatGPT" "new members"; "ChatGPT" "traffic" |
| Baidu, Inc.  (BIDU, BAIDF)  (CIK 0001329099) | 20-F | 2026-03-17 | https://www.sec.gov/Archives/edgar/data/1329099/000119312526109289/d38065d20f.htm | "AI search" "conversion"; "AI search" "traffic"; "AI-powered search" "traffic"; "ChatGPT" "new members"; "ChatGPT" "traffic" |
| Baidu, Inc.  (BIDU, BAIDF)  (CIK 0001329099) | 6-K | 2026-03-17 | https://www.sec.gov/Archives/edgar/data/1329099/000119312526110843/d34060dex991.pdf | "AI search" "conversion"; "AI search" "traffic"; "ChatGPT" "new members"; "ChatGPT" "traffic" |
| Banco Santander, S.A.  (SAN, BCDRF)  (CIK 0000891478) | 6-K | 2026-02-25 | https://www.sec.gov/Archives/edgar/data/891478/000089147826000022/annualreport2025.pdf | "AI assistants" "traffic" |
| Banco Santander, S.A.  (SAN, BCDRF)  (CIK 0000891478) | 20-F | 2026-02-27 | https://www.sec.gov/Archives/edgar/data/891478/000089147826000030/san-20251231.htm | "AI assistants" "traffic" |
| Bank of N.T. Butterfield & Son Ltd  (NTB)  (CIK 0001653242) | 20-F | 2025-02-19 | https://www.sec.gov/Archives/edgar/data/1653242/000165324225000010/ntb-20241231.htm | "LLM" "referral" |
| Baosheng Media Group Holdings Ltd  (BAOS)  (CIK 0001811216) | 6-K | 2026-08-18 | https://www.sec.gov/Archives/edgar/data/1811216/000110465926098402/tm2622290d2_ex99-1.htm | "AI-driven traffic" |
| Baozun Inc.  (BZUN)  (CIK 0001625414) | 20-F | 2025-04-23 | https://www.sec.gov/Archives/edgar/data/1625414/000141057825000824/bzun-20241231x20f.htm | "ChatGPT" "referral"; "ChatGPT" "traffic" |
| Baozun Inc.  (BZUN)  (CIK 0001625414) | 6-K | 2025-04-23 | https://www.sec.gov/Archives/edgar/data/1625414/000110465925037722/tm2512874d1_ex99-2.pdf | "ChatGPT" "traffic" |
| Berto Acquisition Corp.  (CIK 0002033122) | S-1 | 2025-03-21 | https://www.sec.gov/Archives/edgar/data/2033122/000182912625001978/bertoacquisition_s1.htm | "AI platforms" "referrals" |
| Berto Acquisition Corp.  (TACO)  (CIK 0002033122) | S-1/A | 2025-04-09 | https://www.sec.gov/Archives/edgar/data/2033122/000182912625002484/bertoacquisition_s1a.htm | "AI platforms" "referrals" |
| Berto Acquisition Corp.  (TACO)  (CIK 0002033122) | S-1/A | 2025-04-15 | https://www.sec.gov/Archives/edgar/data/2033122/000182912625002650/bertoacquisition_s1a.htm | "AI platforms" "referrals" |
| Berto Acquisition Corp.  (TACO)  (CIK 0002033122) | S-1/A | 2025-04-18 | https://www.sec.gov/Archives/edgar/data/2033122/000182912625002771/bertoacquisition_s1a.htm | "AI platforms" "referrals" |
| Berto Acquisition Corp.  (TACO)  (CIK 0002033122) | 424B4 | 2025-05-01 | https://www.sec.gov/Archives/edgar/data/2033122/000182912625003237/bertoacquisition_424b4.htm | "AI platforms" "referrals" |
| Berto Acquisition Corp.  (TACO, TACOU, TACOW)  (CIK 00020331 | 10-K | 2026-03-31 | https://www.sec.gov/Archives/edgar/data/2033122/000182912626002856/bertoacquisition_10k.htm | "AI platforms" "referrals" |
| Better Home & Finance Holding Co  (BETR, BETRW)  (CIK 000183 | 10-K | 2025-03-19 | https://www.sec.gov/Archives/edgar/data/1835856/000162828025013683/aurcu-20241231.htm | "large language models" "organic traffic" |
| Bilibili Inc.  (BILI, BLBLF)  (CIK 0001723690) | 6-K | 2025-04-09 | https://www.sec.gov/Archives/edgar/data/1723690/000119312525076807/d926409dex992.htm | "AI search" "traffic" |
| BillionToOne, Inc.  (BLLN)  (CIK 0002070849) | 10-Q | 2025-12-10 | https://www.sec.gov/Archives/edgar/data/2070849/000162828025056321/blln-20250930.htm | "LLMs" "referral" |
| BillionToOne, Inc.  (BLLN)  (CIK 0002070849) | 10-K | 2026-03-11 | https://www.sec.gov/Archives/edgar/data/2070849/000207084926000017/blln-20251231.htm | "LLMs" "referral" |
| BillionToOne, Inc.  (CIK 0002070849) | S-1 | 2025-10-07 | https://www.sec.gov/Archives/edgar/data/2070849/000119312525233697/d903739ds1.htm | "LLMs" "referral" |
| BillionToOne, Inc.  (CIK 0002070849) | S-1/A | 2025-10-17 | https://www.sec.gov/Archives/edgar/data/2070849/000119312525242632/d903739ds1a.htm | "LLMs" "referral" |
| BillionToOne, Inc.  (CIK 0002070849) | 424B4 | 2025-11-06 | https://www.sec.gov/Archives/edgar/data/2070849/000119312525270155/d903739d424b4.htm | "LLMs" "referral" |
| BioLineRx Ltd.  (BLRX)  (CIK 0001498403) | 20-F | 2025-03-31 | https://www.sec.gov/Archives/edgar/data/1498403/000117891325001123/zk2532907.htm | "LLM" "referral" |
| Blackstone Digital Infrastructure Trust Inc.  (BXDC)  (CIK 0 | 424B4 | 2026-05-15 | https://www.sec.gov/Archives/edgar/data/2100161/000119312526225090/d52761d424b4.htm | "AI platforms" "referrals" |
| Blaize Holdings, Inc.  (BRKH, BZAI, BRKHU, BRKHW, BZAIW)  (C | S-1 | 2025-01-21 | https://www.sec.gov/Archives/edgar/data/1871638/000119312525008689/d906819ds1.htm | "LLMs" "referral" |
| Blaize Holdings, Inc.  (BZAI, BZAIW)  (CIK 0001871638) | S-1/A | 2025-02-10 | https://www.sec.gov/Archives/edgar/data/1871638/000119312525023099/d906819ds1a.htm | "LLMs" "referral" |
| Blaize Holdings, Inc.  (BZAI, BZAIW)  (CIK 0001871638) | 10-K | 2025-04-15 | https://www.sec.gov/Archives/edgar/data/1871638/000095017025053870/bzai-20241231.htm | "LLMs" "referral" |
| Blaize Holdings, Inc.  (BZAI, BZAIW)  (CIK 0001871638) | S-1 | 2025-07-18 | https://www.sec.gov/Archives/edgar/data/1871638/000119312525160671/d944597ds1.htm | "LLMs" "referral" |
| Blaize Holdings, Inc.  (BZAI, BZAIW)  (CIK 0001871638) | S-1/A | 2025-07-29 | https://www.sec.gov/Archives/edgar/data/1871638/000119312525166574/d944597ds1a.htm | "LLMs" "referral" |
| Blaize Holdings, Inc.  (BZAI, BZAIW)  (CIK 0001871638) | S-1/A | 2025-08-01 | https://www.sec.gov/Archives/edgar/data/1871638/000119312525171690/d944597ds1a.htm | "LLMs" "referral" |
| Blaize Holdings, Inc.  (BZAI, BZAIW)  (CIK 0001871638) | S-1 | 2025-11-28 | https://www.sec.gov/Archives/edgar/data/1871638/000119312525302570/d64210ds1.htm | "LLMs" "referral" |
| Bluerock Homes Trust, Inc.  (BHM)  (CIK 0001903382) | 424B4 | 2025-12-11 | https://www.sec.gov/Archives/edgar/data/1903382/000110465925120257/tm2520049d7_424b4.htm | "LLM" "referral" |
| Booking Holdings Inc.  (BKNG)  (CIK 0001075531) | 10-K | 2026-02-18 | https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm | "AI assistants" "traffic" |
| Boost Run Inc.  (BRUN, BRUNW)  (CIK 0002090646) | S-1 | 2026-07-02 | https://www.sec.gov/Archives/edgar/data/2090646/000149315226031923/forms-1.htm | "ChatGPT" "traffic" |
| Brainsway Ltd.  (BWAY, BRSYF)  (CIK 0001505065) | 20-F | 2025-04-22 | https://www.sec.gov/Archives/edgar/data/1505065/000117184325002347/f20f_032625.htm | "LLM" "referral" |
| Brainsway Ltd.  (BWAY, BRSYF)  (CIK 0001505065) | 20-F | 2026-04-20 | https://www.sec.gov/Archives/edgar/data/1505065/000117184326002568/f20f_032726.htm | "LLM" "referral" |
| Brand Engagement Network Inc.  (BNAI, BNAIW)  (CIK 000183816 | 10-K | 2026-04-16 | https://www.sec.gov/Archives/edgar/data/1838163/000149315226016954/form10-k.htm | "AI assistants" "traffic" |
| Brand Engagement Network Inc.  (BNAI, BNAIW)  (CIK 000183816 | 8-K | 2026-04-30 | https://www.sec.gov/Archives/edgar/data/1838163/000149315226019778/ex2-1.htm | "AI assistants" "traffic" |
| Braze, Inc.  (BRZE)  (CIK 0001676238) | 10-K | 2026-03-25 | https://www.sec.gov/Archives/edgar/data/1676238/000167623826000013/brze-20260131.htm | "ChatGPT" "bookings"; "ChatGPT" "traffic" |
| Bridgeline Digital, Inc.  (BLIN)  (CIK 0001378590) | 8-K | 2025-02-18 | https://www.sec.gov/Archives/edgar/data/1378590/000143774925004209/ex_778424.htm | "AI-powered search" "traffic" |
| Bridgeline Digital, Inc.  (BLIN)  (CIK 0001378590) | 8-K | 2025-05-19 | https://www.sec.gov/Archives/edgar/data/1378590/000143774925017637/ex_818121.htm | "AI-powered search" "traffic" |
| Bridgeline Digital, Inc.  (BLIN)  (CIK 0001378590) | 8-K | 2025-08-18 | https://www.sec.gov/Archives/edgar/data/1378590/000143774925027267/ex_853685.htm | "AI search" "conversion"; "AI search" "traffic" |
| Bridgeline Digital, Inc.  (BLIN)  (CIK 0001378590) | 10-K | 2025-12-19 | https://www.sec.gov/Archives/edgar/data/1378590/000143774925038337/blin20250930_10k.htm | "AI search" "conversion"; "AI search" "traffic" |
| Bridgeline Digital, Inc.  (BLIN)  (CIK 0001378590) | 8-K | 2025-12-23 | https://www.sec.gov/Archives/edgar/data/1378590/000143774925038708/ex_900988.htm | "AI-powered search" "traffic" |
| Bridgeline Digital, Inc.  (BLIN)  (CIK 0001378590) | 8-K | 2026-05-04 | https://www.sec.gov/Archives/edgar/data/1378590/000143774926014683/ex_955788.htm | "AI-powered search" "traffic" |
| Bridgeline Digital, Inc.  (BLIN)  (CIK 0001378590) | 8-K | 2026-05-04 | https://www.sec.gov/Archives/edgar/data/1378590/000143774926014683/ex_955787.htm | "AI-powered search" "traffic" |
| Bridgeline Digital, Inc.  (BLIN)  (CIK 0001378590) | 8-K | 2026-05-19 | https://www.sec.gov/Archives/edgar/data/1378590/000143774926017660/ex_963476.htm | "AI assistants" "traffic"; "AI-powered search" "traffic" |
| Bridgeline Digital, Inc.  (BLIN)  (CIK 0001378590) | 8-K | 2026-08-18 | https://www.sec.gov/Archives/edgar/data/1378590/000143774926028360/ex_1005034.htm | "AI search" "traffic" |
| Bright Mountain Media, Inc.  (BMTM)  (CIK 0001568385) | 10-K | 2026-03-24 | https://www.sec.gov/Archives/edgar/data/1568385/000119312526121933/bmtm-20251231.htm | "AI-powered search" "traffic" |
| Brookfield Infrastructure Corp  (BIPC)  (CIK 0001788348) | 20-F | 2025-03-24 | https://www.sec.gov/Archives/edgar/data/1788348/000162828025014377/bipc-20241231.htm | "LLM" "referral" |
| Brookfield Infrastructure Corp  (BIPC)  (CIK 0001788348) | 20-F | 2026-03-17 | https://www.sec.gov/Archives/edgar/data/1788348/000178834826000001/bipc-20251231.htm | "LLM" "referral" |
| Brookfield Infrastructure Partners L.P.  (BIP, BIPH, BIPI, B | 20-F | 2025-03-24 | https://www.sec.gov/Archives/edgar/data/1406234/000162828025014380/bip-20241231.htm | "LLM" "referral" |
| Brookfield Infrastructure Partners L.P.  (BIP, BIPH, BIPI, B | 20-F | 2026-03-17 | https://www.sec.gov/Archives/edgar/data/1406234/000140623426000002/bip-20251231.htm | "LLM" "referral" |
| Bubblr Inc.  (BBLR)  (CIK 0001873722) | 10-K | 2025-03-31 | https://www.sec.gov/Archives/edgar/data/1873722/000164117225001484/form10-k.htm | "ChatGPT" "traffic" |
| Bubblr Inc.  (BBLR)  (CIK 0001873722) | 10-K | 2026-03-31 | https://www.sec.gov/Archives/edgar/data/1873722/000149315226013999/form10-k.htm | "ChatGPT" "traffic" |
| BuzzFeed, Inc.  (BZFD, BZFDW)  (CIK 0001828972) | 10-Q | 2025-08-07 | https://www.sec.gov/Archives/edgar/data/1828972/000182897225000195/bzfd-20250630.htm | "AI Mode" "traffic"; "AI Overviews" "traffic"; "generative AI" "referral traffic" |
| BuzzFeed, Inc.  (BZFD, BZFDW)  (CIK 0001828972) | 10-Q | 2025-11-06 | https://www.sec.gov/Archives/edgar/data/1828972/000182897225000240/bzfd-20250930.htm | "AI Mode" "traffic"; "AI Overviews" "traffic"; "generative AI" "referral traffic" |
| BuzzFeed, Inc.  (BZFD, BZFDW)  (CIK 0001828972) | 10-K | 2026-03-16 | https://www.sec.gov/Archives/edgar/data/1828972/000182897226000030/bzfd-20251231.htm | "AI Mode" "traffic"; "AI Overviews" "traffic"; "generative AI" "referral traffic" |
| C3.ai, Inc.  (AI)  (CIK 0001577526) | 10-K | 2026-06-24 | https://www.sec.gov/Archives/edgar/data/1577526/000157752626000078/ai-20260430.htm | "ChatGPT" "bookings"; "ChatGPT" "traffic" |
| CANADIAN IMPERIAL BANK OF COMMERCE /CAN/  (CM)  (CIK 0001045 | 6-K | 2025-03-04 | https://www.sec.gov/Archives/edgar/data/1045520/000119312525045119/d942797dex991.htm | "ChatGPT" "referral" |
| CARVANA CO.  (CVNA)  (CIK 0001690820) | 10-K | 2025-02-19 | https://www.sec.gov/Archives/edgar/data/1690820/000169082025000074/cvna-20241231.htm | "AI platforms" "referrals" |
| CARVANA CO.  (CVNA)  (CIK 0001690820) | 10-K | 2026-02-18 | https://www.sec.gov/Archives/edgar/data/1690820/000169082026000009/cvna-20251231.htm | "AI platforms" "referrals" |
| CEMEX SAB DE CV  (CX, CXMSF)  (CIK 0001076378) | 20-F | 2026-04-24 | https://www.sec.gov/Archives/edgar/data/1076378/000119312526177605/d120395d20f.htm | "AI assistants" "traffic" |
| CHAIN BRIDGE BANCORP INC  (CBNA)  (CIK 0001392272) | 10-K | 2026-03-20 | https://www.sec.gov/Archives/edgar/data/1392272/000162828026020177/chnbrdg-20251231.htm | "AI platforms" "referrals" |
| CHECK POINT SOFTWARE TECHNOLOGIES LTD  (CHKP)  (CIK 00010159 | 20-F | 2026-03-31 | https://www.sec.gov/Archives/edgar/data/1015922/000117891326001932/zk2634942.htm | "ChatGPT" "bookings"; "ChatGPT" "traffic" |
| CHEGG, INC  (CHGG)  (CIK 0001364954) | 8-K | 2025-02-24 | https://www.sec.gov/Archives/edgar/data/1364954/000136495425000011/a9901-financialresultsq420.htm | "AI Overviews" "traffic"; "answer engine" |
| CHEGG, INC  (CHGG)  (CIK 0001364954) | 10-K | 2025-02-24 | https://www.sec.gov/Archives/edgar/data/1364954/000136495425000013/chgg-20241231.htm | "AI Overviews" "traffic"; "large language models" "organic traffic" |
| CHEGG, INC  (CHGG)  (CIK 0001364954) | 8-K | 2025-05-12 | https://www.sec.gov/Archives/edgar/data/1364954/000136495425000049/a9901-financialresultsq120.htm | "AI Overviews" "traffic" |
| CHEGG, INC  (CHGG)  (CIK 0001364954) | 10-Q | 2025-05-12 | https://www.sec.gov/Archives/edgar/data/1364954/000136495425000052/chgg-20250331.htm | "AI Overviews" "traffic" |
| CHEGG, INC  (CHGG)  (CIK 0001364954) | 8-K | 2025-08-05 | https://www.sec.gov/Archives/edgar/data/1364954/000136495425000090/a9901-financialresultsq220.htm | "AI Overviews" "traffic" |
| CHEGG, INC  (CHGG)  (CIK 0001364954) | 10-Q | 2025-08-08 | https://www.sec.gov/Archives/edgar/data/1364954/000136495425000096/chgg-20250630.htm | "AI Overviews" "traffic" |
| CHEGG, INC  (CHGG)  (CIK 0001364954) | 10-Q | 2025-11-10 | https://www.sec.gov/Archives/edgar/data/1364954/000136495425000117/chgg-20250930.htm | "AI Overviews" "traffic" |
| CHEGG, INC  (CHGG)  (CIK 0001364954) | 10-K | 2026-03-09 | https://www.sec.gov/Archives/edgar/data/1364954/000136495426000021/chgg-20251231.htm | "AI Overviews" "traffic"; "ChatGPT" "bookings"; "ChatGPT" "traffic"; "large language models" "organic traffic" |
| CHEGG, INC  (CHGG)  (CIK 0001364954) | 10-Q | 2026-05-11 | https://www.sec.gov/Archives/edgar/data/1364954/000136495426000048/chgg-20260331.htm | "AI Overviews" "traffic"; "ChatGPT" "traffic" |
| CHEGG, INC  (CHGG)  (CIK 0001364954) | 10-Q | 2026-08-06 | https://www.sec.gov/Archives/edgar/data/1364954/000136495426000088/chgg-20260630.htm | "ChatGPT" "bookings"; "ChatGPT" "traffic" |
| CHEMED CORP  (CHE)  (CIK 0000019584) | 10-K | 2026-02-27 | https://www.sec.gov/Archives/edgar/data/19584/000156276226000020/che-20251231x10k.htm | "AI platforms" "referrals" |
| CIENA CORP  (CIEN)  (CIK 0000936395) | 8-K | 2026-06-04 | https://www.sec.gov/Archives/edgar/data/936395/000162828026040614/ex9922026q2earningsprese.htm | "ChatGPT" "traffic" |
| CIMPRESS plc  (CMPR)  (CIK 0001262976) | 10-K | 2025-08-08 | https://www.sec.gov/Archives/edgar/data/1262976/000162828025039200/cmpr-20250630.htm | "AI search" "conversion"; "AI search" "traffic"; "agentic search"; "generative AI" "referral traffic" |
| CIMPRESS plc  (CMPR)  (CIK 0001262976) | 10-K | 2026-08-07 | https://www.sec.gov/Archives/edgar/data/1262976/000126297626000027/cmpr-20260630.htm | "AI search" "conversion"; "AI search" "traffic"; "generative AI" "referral traffic" |
| COMSCORE, INC.  (SCOR)  (CIK 0001158172) | 10-K | 2026-03-26 | https://www.sec.gov/Archives/edgar/data/1158172/000115817226000009/scor-20251231.htm | "AI visibility"; "ChatGPT" "referral"; "ChatGPT" "traffic" |
| CONDUENT Inc  (CNDT)  (CIK 0001677703) | 10-K | 2026-02-19 | https://www.sec.gov/Archives/edgar/data/1677703/000167770326000024/cndt-20251231.htm | "AI assistants" "traffic" |
| COTY INC.  (COTY)  (CIK 0001024305) | 10-K | 2026-08-20 | https://www.sec.gov/Archives/edgar/data/1024305/000102430526000048/coty-20260630.htm | "generative engine optimization" |
| CTW Cayman  (CIK 0002047148) | F-1 | 2025-05-15 | https://www.sec.gov/Archives/edgar/data/2047148/000121390025044061/ea0229974-05.htm | "large language models" "organic traffic" |
| CTW Cayman  (CTW)  (CIK 0002047148) | F-1/A | 2025-06-12 | https://www.sec.gov/Archives/edgar/data/2047148/000121390025053729/ea0229974-08.htm | "large language models" "organic traffic" |
| CTW Cayman  (CTW)  (CIK 0002047148) | F-1/A | 2025-06-26 | https://www.sec.gov/Archives/edgar/data/2047148/000121390025058248/ea0229974-10.htm | "large language models" "organic traffic" |
| CTW Cayman  (CTW)  (CIK 0002047148) | F-1/A | 2025-07-03 | https://www.sec.gov/Archives/edgar/data/2047148/000121390025061284/ea0229974-12.htm | "large language models" "organic traffic" |
| CTW Cayman  (CTW)  (CIK 0002047148) | 424B4 | 2025-08-07 | https://www.sec.gov/Archives/edgar/data/2047148/000121390025072850/ea0229974-16.htm | "large language models" "organic traffic" |
| CTW Cayman  (CTW)  (CIK 0002047148) | 20-F | 2025-11-17 | https://www.sec.gov/Archives/edgar/data/2047148/000121390025111604/ea0265341-20f_ctwcayman.htm | "large language models" "organic traffic" |
| Cambium Networks Corp  (CMBM, CMBMF)  (CIK 0001738177) | 10-K | 2026-04-07 | https://www.sec.gov/Archives/edgar/data/1738177/000119312526144057/cmbm-20241231.htm | "ChatGPT" "traffic" |
| Cambium Networks Corp  (CMBMF)  (CIK 0001738177) | 10-K | 2026-05-01 | https://www.sec.gov/Archives/edgar/data/1738177/000119312526201759/cmbmf-20251231.htm | "ChatGPT" "traffic" |
| Cars.com Inc.  (CARS)  (CIK 0001683606) | 10-K | 2025-02-27 | https://www.sec.gov/Archives/edgar/data/1683606/000095017025029023/cars-20241231.htm | "ChatGPT" "referral"; "ChatGPT" "traffic" |
| Cars.com Inc.  (CARS)  (CIK 0001683606) | 8-K | 2025-11-06 | https://www.sec.gov/Archives/edgar/data/1683606/000119312525268110/cars-ex99_1.htm | "AI-powered search" "traffic" |
| Cars.com Inc.  (CARS)  (CIK 0001683606) | 10-K | 2026-02-26 | https://www.sec.gov/Archives/edgar/data/1683606/000119312526076546/cars-20251231.htm | "AI-powered search" "traffic"; "answer engines" |
| Cerebras Systems Inc.  (CBRS)  (CIK 0002021728) | S-1/A | 2026-05-04 | https://www.sec.gov/Archives/edgar/data/2021728/000162828026029503/cerebras-sx1amay2026.htm | "ChatGPT" "traffic" |
| Cerebras Systems Inc.  (CBRS)  (CIK 0002021728) | S-1/A | 2026-05-11 | https://www.sec.gov/Archives/edgar/data/2021728/000162828026033143/cerebras-sx1a2.htm | "ChatGPT" "traffic" |
| Cerebras Systems Inc.  (CBRS)  (CIK 0002021728) | 424B4 | 2026-05-14 | https://www.sec.gov/Archives/edgar/data/2021728/000162828026035214/cerebras-424b4.htm | "ChatGPT" "traffic" |
| Cerebras Systems Inc.  (CIK 0002021728) | S-1 | 2026-04-17 | https://www.sec.gov/Archives/edgar/data/2021728/000162828026025762/cerebras-sx1april2026.htm | "ChatGPT" "traffic" |
| Change Agents Corporation.  (ALBT)  (CIK 0001630212) | 8-K | 2026-07-21 | https://www.sec.gov/Archives/edgar/data/1630212/000121390026079830/ea029857301ex99-1.htm | "generative engine optimization" |
| Change Agents Corporation.  (CHGA)  (CIK 0001630212) | S-1 | 2026-08-07 | https://www.sec.gov/Archives/edgar/data/1630212/000121390026086806/ea0300078-s1_change.htm | "AI search" "conversion"; "AI search" "traffic"; "AI visibility"; "AI-powered search" "traffic"; "ChatGPT" "traffic"; "Perplexity" "traffic"; "generative engine optimization" |
| Change Agents Corporation.  (CHGA)  (CIK 0001630212) | 10-Q | 2026-08-14 | https://www.sec.gov/Archives/edgar/data/1630212/000121390026090229/ea0301266-10q_change.htm | "AI visibility"; "generative engine optimization" |
| Change Agents Corporation.  (CHGA)  (CIK 0001630212) | S-1/A | 2026-08-25 | https://www.sec.gov/Archives/edgar/data/1630212/000121390026093149/ea0302304-s1a1_change.htm | "AI search" "conversion"; "AI search" "traffic"; "AI visibility"; "AI-powered search" "traffic"; "ChatGPT" "traffic"; "Perplexity" "traffic"; "generative engine optimization" |
| Change Agents Corporation.  (CHGA)  (CIK 0001630212) | S-1/A | 2026-09-15 | https://www.sec.gov/Archives/edgar/data/1630212/000121390026100214/ea0305058-s1a2_change.htm | "AI search" "conversion"; "AI search" "traffic"; "AI visibility"; "AI-powered search" "traffic"; "ChatGPT" "traffic"; "Perplexity" "traffic"; "generative engine optimization" |
| Change Agents Corporation.  (CHGA)  (CIK 0001630212) | S-1/A | 2026-09-16 | https://www.sec.gov/Archives/edgar/data/1630212/000121390026100576/ea0305711-s1a3_change.htm | "AI search" "conversion"; "AI search" "traffic"; "AI visibility"; "AI-powered search" "traffic"; "ChatGPT" "traffic"; "Perplexity" "traffic"; "generative engine optimization" |
| Chime Financial, Inc.  (CHYM)  (CIK 0001795586) | S-1/A | 2025-06-02 | https://www.sec.gov/Archives/edgar/data/1795586/000162828025028733/chimefinancialinc-sx1a.htm | "AI platforms" "referrals"; "ChatGPT" "new members"; "ChatGPT" "referral" |
| Chime Financial, Inc.  (CHYM)  (CIK 0001795586) | 424B4 | 2025-06-12 | https://www.sec.gov/Archives/edgar/data/1795586/000162828025030855/chimefinancialinc-finalpro.htm | "AI platforms" "referrals"; "ChatGPT" "new members"; "ChatGPT" "referral" |
| Chime Financial, Inc.  (CHYM)  (CIK 0001795586) | 10-K | 2026-03-06 | https://www.sec.gov/Archives/edgar/data/1795586/000179558626000013/chym-20251231.htm | "AI platforms" "referrals" |
| Chime Financial, Inc.  (CIK 0001795586) | S-1 | 2025-05-13 | https://www.sec.gov/Archives/edgar/data/1795586/000162828025025059/chimefinancialinc-sx1wq1da.htm | "AI platforms" "referrals"; "ChatGPT" "new members"; "ChatGPT" "referral" |
| Clear Channel Outdoor Holdings, Inc.  (CCO)  (CIK 0001334978 | 10-K | 2025-02-24 | https://www.sec.gov/Archives/edgar/data/1334978/000133497825000008/cco-20241231.htm | "ChatGPT" "traffic" |
| ClearPoint Neuro, Inc.  (CLPT)  (CIK 0001285550) | 8-K | 2025-11-06 | https://www.sec.gov/Archives/edgar/data/1285550/000119312525269992/clpt-ex10_1.htm | "ChatGPT" "referral" |
| Cloudflare, Inc.  (NET)  (CIK 0001477333) | 8-K | 2026-08-06 | https://www.sec.gov/Archives/edgar/data/1477333/000147733326000053/q226exhibit991.htm | "answer engines" |
| CoastalSouth Bancshares, Inc.  (COSO)  (CIK 0001297107) | S-1 | 2025-06-06 | https://www.sec.gov/Archives/edgar/data/1297107/000095017025083183/s-1_3.31.2025.htm | "LLM" "referral" |
| CoastalSouth Bancshares, Inc.  (COSO)  (CIK 0001297107) | S-1/A | 2025-06-24 | https://www.sec.gov/Archives/edgar/data/1297107/000095017025089216/s-1_3.31.2025_-_amend1-n.htm | "LLM" "referral" |
| CoastalSouth Bancshares, Inc.  (COSO)  (CIK 0001297107) | 424B4 | 2025-07-02 | https://www.sec.gov/Archives/edgar/data/1297107/000095017025092949/coso_424_july_2025.htm | "LLM" "referral" |
| Coincheck Group N.V.  (CNCK, CNCKW)  (CIK 0001913847) | 20-F | 2026-06-29 | https://www.sec.gov/Archives/edgar/data/1913847/000162828026046005/cnck-20260331.htm | "LLM" "referral" |
| Collab Z Inc.  (CIK 0002050338) | S-1 | 2025-07-21 | https://www.sec.gov/Archives/edgar/data/2050338/000121390025066182/ea0249132-s1_collab.htm | "AI assistants" "traffic" |
| Collab Z Inc.  (CLBZ)  (CIK 0002050338) | S-1/A | 2025-08-11 | https://www.sec.gov/Archives/edgar/data/2050338/000121390025073810/ea0251972-s1a1_collab.htm | "AI assistants" "traffic" |
| Collab Z Inc.  (CLBZ)  (CIK 0002050338) | S-1/A | 2025-08-22 | https://www.sec.gov/Archives/edgar/data/2050338/000121390025080014/ea0254291-s1a2_collab.htm | "AI assistants" "traffic" |
| Collab Z Inc.  (CLBZ)  (CIK 0002050338) | S-1/A | 2025-10-20 | https://www.sec.gov/Archives/edgar/data/2050338/000121390025100246/ea0261742-s1a3_collab.htm | "AI assistants" "traffic" |
| Collab Z Inc.  (CLBZ)  (CIK 0002050338) | S-1 | 2026-02-27 | https://www.sec.gov/Archives/edgar/data/2050338/000121390026021753/ea0276629-s1_collab.htm | "AI assistants" "traffic" |
| Collab Z Inc.  (CLBZ)  (CIK 0002050338) | S-1/A | 2026-05-26 | https://www.sec.gov/Archives/edgar/data/2050338/000121390026060720/ea0291261-s1a1_collab.htm | "AI assistants" "traffic" |
| Commerce.com, Inc.  (BIGC)  (CIK 0001626450) | 8-K | 2025-07-31 | https://www.sec.gov/Archives/edgar/data/1626450/000095017025100556/bigc-ex99_3.htm | "agentic search" |
| Commerce.com, Inc.  (BIGC)  (CIK 0001626450) | 8-K | 2025-07-31 | https://www.sec.gov/Archives/edgar/data/1626450/000095017025100556/bigc-ex99_2.htm | "ChatGPT" "traffic"; "Perplexity" "traffic"; "answer engines" |
| Commerce.com, Inc.  (BIGC)  (CIK 0001626450) | 10-Q | 2025-07-31 | https://www.sec.gov/Archives/edgar/data/1626450/000095017025100557/bigc-20250630.htm | "AI-powered search" "traffic"; "answer engines" |
| Commerce.com, Inc.  (CMRC)  (CIK 0001626450) | 10-Q | 2025-11-06 | https://www.sec.gov/Archives/edgar/data/1626450/000119312525268071/bigc-20250930.htm | "AI discovery"; "AI-powered search" "traffic"; "answer engines" |
| Comstock Inc.  (LODE)  (CIK 0001120970) | 10-K | 2025-03-06 | https://www.sec.gov/Archives/edgar/data/1120970/000143774925006453/lode20241231_10k.htm | "ChatGPT" "traffic" |
| Comstock Inc.  (LODE)  (CIK 0001120970) | 10-K | 2026-03-24 | https://www.sec.gov/Archives/edgar/data/1120970/000143774926009589/lode20251231_10k.htm | "ChatGPT" "traffic" |
| ConnectM Technology Solutions, Inc.  (CNTM)  (CIK 0001895249 | 10-K | 2026-04-16 | https://www.sec.gov/Archives/edgar/data/1895249/000110465926044467/cntm-20251231x10k.htm | "AI platforms" "referrals" |
| ConnectM Technology Solutions, Inc.  (CNTM)  (CIK 0001895249 | S-1/A | 2026-06-17 | https://www.sec.gov/Archives/edgar/data/1895249/000110465926074787/cntm-20260331xs1a.htm | "AI platforms" "referrals" |
| ConnectM Technology Solutions, Inc.  (CNTM)  (CIK 0001895249 | S-1/A | 2026-09-21 | https://www.sec.gov/Archives/edgar/data/1895249/000110465926109217/cntm-20260630xs1a.htm | "AI platforms" "referrals" |
| Core AI Holdings, Inc.  (CHAI)  (CIK 0001649009) | 6-K | 2026-07-28 | https://www.sec.gov/Archives/edgar/data/1649009/000149315226034941/ex99-1.htm | "AI assistants" "traffic" |
| CoreWeave, Inc.  (CIK 0001769628) | S-1 | 2025-03-03 | https://www.sec.gov/Archives/edgar/data/1769628/000119312525044231/d899798ds1.htm | "ChatGPT" "traffic" |
| CoreWeave, Inc.  (CRWV)  (CIK 0001769628) | S-1/A | 2025-03-12 | https://www.sec.gov/Archives/edgar/data/1769628/000119312525052207/d899798ds1a.htm | "ChatGPT" "traffic" |
| CoreWeave, Inc.  (CRWV)  (CIK 0001769628) | S-1/A | 2025-03-20 | https://www.sec.gov/Archives/edgar/data/1769628/000119312525058309/d899798ds1a.htm | "ChatGPT" "traffic" |
| CoreWeave, Inc.  (CRWV)  (CIK 0001769628) | 424B4 | 2025-03-31 | https://www.sec.gov/Archives/edgar/data/1769628/000119312525067651/d899798d424b4.htm | "ChatGPT" "traffic" |
| Coursera, Inc.  (COUR)  (CIK 0001651562) | 10-Q | 2026-08-05 | https://www.sec.gov/Archives/edgar/data/1651562/000165156226000063/cour-20260630.htm | "ChatGPT" "traffic" |
| Covista Inc.  (ATGE)  (CIK 0000730464) | 8-K | 2026-02-24 | https://www.sec.gov/Archives/edgar/data/730464/000073046426000007/cvsa-20260224xex99d2.htm | "AI discovery" |
| Criteo S.A.  (CRTO)  (CIK 0001576427) | 8-K | 2026-08-05 | https://www.sec.gov/Archives/edgar/data/1576427/000162828026052913/exhibit991-8xkq22026.htm | "ChatGPT" "traffic" |
| Criteo S.A.  (CRTO)  (CIK 0001576427) | 10-Q | 2026-08-05 | https://www.sec.gov/Archives/edgar/data/1576427/000157642726000092/crto-20260630.htm | "AI-powered search" "traffic" |
| Cyngn Inc.  (CYN)  (CIK 0001874097) | 10-K | 2026-03-27 | https://www.sec.gov/Archives/edgar/data/1874097/000121390026034900/ea0277796-10k_cyngn.htm | "LLM" "referral" |
| CytoMed Therapeutics Ltd  (GDTC)  (CIK 0001873093) | 20-F | 2025-04-28 | https://www.sec.gov/Archives/edgar/data/1873093/000164117225006458/form20-f.htm | "LLM" "referral" |
| CytoMed Therapeutics Ltd  (GDTC)  (CIK 0001873093) | 20-F | 2026-03-31 | https://www.sec.gov/Archives/edgar/data/1873093/000149315226013813/form20-f.htm | "LLM" "referral" |
| D-Wave Quantum Inc.  (QBTS)  (CIK 0001907982) | 10-K | 2026-02-26 | https://www.sec.gov/Archives/edgar/data/1907982/000190798226000026/qbts-20251231.htm | "LLM" "referral"; "LLMs" "referral" |
| DELCATH SYSTEMS, INC.  (DCTH)  (CIK 0000872912) | 10-K | 2026-02-26 | https://www.sec.gov/Archives/edgar/data/872912/000162828026012019/dcth-20251231.htm | "AI platforms" "referrals" |
| DELUXE CORP  (DLX)  (CIK 0000027996) | 10-K | 2026-02-13 | https://www.sec.gov/Archives/edgar/data/27996/000002799626000037/dlx-20251231.htm | "agentic search" |
| DESTINATION XL GROUP, INC.  (DXLG)  (CIK 0000813298) | 8-K | 2026-06-03 | https://www.sec.gov/Archives/edgar/data/813298/000119312526254584/dxlg-ex99_1.htm | "AI-powered search" "traffic" |
| DESTINATION XL GROUP, INC.  (DXLG)  (CIK 0000813298) | 10-Q | 2026-06-03 | https://www.sec.gov/Archives/edgar/data/813298/000119312526255525/dxlg-20260502.htm | "AI-powered search" "traffic" |
| DESTINATION XL GROUP, INC.  (DXLG)  (CIK 0000813298) | 8-K | 2026-09-09 | https://www.sec.gov/Archives/edgar/data/813298/000119312526385888/dxlg-ex99_1.htm | "AI-powered search" "traffic" |
| DESTINATION XL GROUP, INC.  (DXLG)  (CIK 0000813298) | 10-Q | 2026-09-09 | https://www.sec.gov/Archives/edgar/data/813298/000119312526386417/dxlg-20260801.htm | "AI-powered search" "traffic" |
| DOCUSIGN, INC.  (DOCU)  (CIK 0001261333) | 10-Q | 2025-12-05 | https://www.sec.gov/Archives/edgar/data/1261333/000126133325000150/docu-20251031.htm | "AI-referred" |
| DOCUSIGN, INC.  (DOCU)  (CIK 0001261333) | 10-K | 2026-03-18 | https://www.sec.gov/Archives/edgar/data/1261333/000126133326000021/docu-20260131.htm | "AI-referred" |
| DOCUSIGN, INC.  (DOCU)  (CIK 0001261333) | 10-Q | 2026-06-05 | https://www.sec.gov/Archives/edgar/data/1261333/000126133326000074/docu-20260430.htm | "AI-referred" |
| DOCUSIGN, INC.  (DOCU)  (CIK 0001261333) | 10-Q | 2026-09-04 | https://www.sec.gov/Archives/edgar/data/1261333/000126133326000099/docu-20260731.htm | "AI-referred" |
| DOMO, INC.  (DOMO)  (CIK 0001505952) | 10-K | 2025-04-04 | https://www.sec.gov/Archives/edgar/data/1505952/000150595225000045/domo-20250131.htm | "LLM" "referral" |
| DOMO, INC.  (DOMO)  (CIK 0001505952) | 8-K | 2026-07-22 | https://www.sec.gov/Archives/edgar/data/1505952/000110465926085819/tm2620768d3_ex2-1.htm | "ChatGPT" "referral"; "ChatGPT" "traffic" |
| DRDGOLD LTD  (DRD, DRDGF)  (CIK 0001023512) | 6-K | 2025-10-28 | https://www.sec.gov/Archives/edgar/data/1023512/000162828025046593/drdgoldintegratedreport2.htm | "LLM" "referral" |
| DSC Holdings Ltd.  (CIK 0001966041) | F-1 | 2026-05-26 | https://www.sec.gov/Archives/edgar/data/1966041/000121390026060977/ea0200059-28.htm | "AI platforms" "referrals" |
| DSC Holdings Ltd.  (CIK 0001966041) | F-1/A | 2026-06-08 | https://www.sec.gov/Archives/edgar/data/1966041/000121390026066193/ea0200059-31.htm | "AI platforms" "referrals" |
| DSC Holdings Ltd.  (CIK 0001966041) | F-1/A | 2026-06-17 | https://www.sec.gov/Archives/edgar/data/1966041/000121390026069691/ea0200059-34.htm | "AI platforms" "referrals" |
| DSC Holdings Ltd.  (CIK 0001966041) | F-1/A | 2026-06-22 | https://www.sec.gov/Archives/edgar/data/1966041/000121390026070374/ea0200059-36.htm | "AI platforms" "referrals" |
| DSC Holdings Ltd.  (CIK 0001966041) | 424B4 | 2026-06-26 | https://www.sec.gov/Archives/edgar/data/1966041/000121390026072276/ea0200059-38.htm | "AI platforms" "referrals" |
| DULUTH HOLDINGS INC.  (DLTH)  (CIK 0001649744) | 10-K | 2026-03-20 | https://www.sec.gov/Archives/edgar/data/1649744/000119312526117508/dlth-20260201.htm | "answer engine" |
| Datadog, Inc.  (DDOG)  (CIK 0001561550) | 10-K | 2025-02-20 | https://www.sec.gov/Archives/edgar/data/1561550/000156155025000025/ddog-20241231.htm | "LLM" "referral" |
| Datadog, Inc.  (DDOG)  (CIK 0001561550) | 10-K | 2026-02-18 | https://www.sec.gov/Archives/edgar/data/1561550/000162828026008819/ddog-20251231.htm | "LLM" "referral" |
| Dbim Holdings Ltd  (CIK 0002057757) | F-1 | 2025-08-27 | https://www.sec.gov/Archives/edgar/data/2057757/000192998025000627/dbim_f1.htm | "large language models" "organic traffic" |
| Dbim Holdings Ltd  (DBIM)  (CIK 0002057757) | F-1/A | 2025-10-27 | https://www.sec.gov/Archives/edgar/data/2057757/000192998025000675/dbim_f1a.htm | "large language models" "organic traffic" |
| Dbim Holdings Ltd  (DBIM)  (CIK 0002057757) | F-1/A | 2025-11-05 | https://www.sec.gov/Archives/edgar/data/2057757/000192998025000691/dbim_f1a.htm | "large language models" "organic traffic" |
| Dbim Holdings Ltd  (DBIM)  (CIK 0002057757) | F-1/A | 2026-01-27 | https://www.sec.gov/Archives/edgar/data/2057757/000192998026000023/dbim_f1a.htm | "large language models" "organic traffic" |
| Dbim Holdings Ltd  (DBIM)  (CIK 0002057757) | F-1/A | 2026-02-06 | https://www.sec.gov/Archives/edgar/data/2057757/000192998026000037/dbim_f1a.htm | "large language models" "organic traffic" |
| DiamondRock Hospitality Co  (DRH)  (CIK 0001298946) | 10-K | 2026-02-27 | https://www.sec.gov/Archives/edgar/data/1298946/000129894626000013/drh-20251231.htm | "AI search" "conversion" |
| DigitalOcean Holdings, Inc.  (DOCN)  (CIK 0001582961) | 10-K | 2025-02-25 | https://www.sec.gov/Archives/edgar/data/1582961/000158296125000035/docn-20241231.htm | "LLMs" "referral" |
| DigitalOcean Holdings, Inc.  (DOCN)  (CIK 0001582961) | 10-Q | 2025-08-05 | https://www.sec.gov/Archives/edgar/data/1582961/000158296125000138/docn-20250630.htm | "LLMs" "referral" |
| DigitalOcean Holdings, Inc.  (DOCN)  (CIK 0001582961) | 10-Q | 2025-11-05 | https://www.sec.gov/Archives/edgar/data/1582961/000158296125000150/docn-20250930.htm | "LLMs" "referral" |
| DigitalOcean Holdings, Inc.  (DOCN)  (CIK 0001582961) | 10-K | 2026-02-24 | https://www.sec.gov/Archives/edgar/data/1582961/000158296126000019/docn-20251231.htm | "LLMs" "referral" |
| DigitalOcean Holdings, Inc.  (DOCN)  (CIK 0001582961) | 10-Q | 2026-05-05 | https://www.sec.gov/Archives/edgar/data/1582961/000158296126000049/docn-20260331.htm | "LLMs" "referral" |
| DigitalOcean Holdings, Inc.  (DOCN)  (CIK 0001582961) | 10-Q | 2026-08-04 | https://www.sec.gov/Archives/edgar/data/1582961/000162828026052556/docn-20260630.htm | "LLMs" "referral" |
| Direct Digital Holdings, Inc.  (DRCT)  (CIK 0001880613) | 8-K | 2026-08-12 | https://www.sec.gov/Archives/edgar/data/1880613/000188061326000095/drct-earningsreleaseq226xe.htm | "generative engine optimization" |
| Doximity, Inc.  (DOCS)  (CIK 0001516513) | 10-K | 2026-05-19 | https://www.sec.gov/Archives/edgar/data/1516513/000151651326000025/docs-20260331.htm | "AI platforms" "referrals" |
| Dream Finders Homes, Inc.  (DFH)  (CIK 0001825088) | 10-K | 2025-02-25 | https://www.sec.gov/Archives/edgar/data/1825088/000182508825000014/dfh-20241231.htm | "AI platforms" "referrals" |
| Dream Finders Homes, Inc.  (DFH)  (CIK 0001825088) | 10-K | 2026-02-24 | https://www.sec.gov/Archives/edgar/data/1825088/000162828026010837/dfh-20251231.htm | "AI platforms" "referrals" |
| Dreamland Ltd  (TDIC)  (CIK 0002041338) | 20-F | 2026-08-17 | https://www.sec.gov/Archives/edgar/data/2041338/000149315226038758/form20-f.htm | "AI search" "conversion" |
| Dynatrace, Inc.  (DT)  (CIK 0001773383) | 10-K | 2026-05-20 | https://www.sec.gov/Archives/edgar/data/1773383/000177338326000019/dt-20260331.htm | "AI-referred"; "LLM" "referral"; "LLMs" "referral" |
| Dynatrace, Inc.  (DT)  (CIK 0001773383) | 10-Q | 2026-08-05 | https://www.sec.gov/Archives/edgar/data/1773383/000177338326000050/dt-20260630.htm | "AI-referred" |
| EBAY INC  (EBAY)  (CIK 0001065088) | 10-K | 2025-02-27 | https://www.sec.gov/Archives/edgar/data/1065088/000106508825000037/ebay-20241231.htm | "AI referrals" |
| EBAY INC  (EBAY)  (CIK 0001065088) | 10-K | 2026-02-19 | https://www.sec.gov/Archives/edgar/data/1065088/000106508826000027/ebay-20251231.htm | "AI referrals" |
| ENTRATA, INC.  (ENT)  (CIK 0002028464) | S-1 | 2026-05-28 | https://www.sec.gov/Archives/edgar/data/2028464/000162828026038608/entrata-sx1.htm | "LLM" "referral"; "LLMs" "referral" |
| ENTRATA, INC.  (ENT)  (CIK 0002028464) | S-1/A | 2026-06-11 | https://www.sec.gov/Archives/edgar/data/2028464/000162828026042574/entrata-sx1a1.htm | "LLM" "referral"; "LLMs" "referral" |
| ENTRATA, INC.  (ENT)  (CIK 0002028464) | S-1/A | 2026-09-01 | https://www.sec.gov/Archives/edgar/data/2028464/000162828026059692/entrata-sx1a2.htm | "LLM" "referral"; "LLMs" "referral" |
| ETSY INC  (ETSY)  (CIK 0001370637) | 10-K | 2025-02-19 | https://www.sec.gov/Archives/edgar/data/1370637/000137063725000017/etsy-20241231.htm | "large language models" "organic traffic" |
| ETSY INC  (ETSY)  (CIK 0001370637) | 10-Q | 2025-10-29 | https://www.sec.gov/Archives/edgar/data/1370637/000137063725000100/etsy-20250930.htm | "agentic search" |
| ETSY INC  (ETSY)  (CIK 0001370637) | 8-K | 2025-10-29 | https://www.sec.gov/Archives/edgar/data/1370637/000137063725000098/exhibit991q32025.htm | "ChatGPT" "traffic" |
| ETSY INC  (ETSY)  (CIK 0001370637) | 10-K | 2026-02-19 | https://www.sec.gov/Archives/edgar/data/1370637/000137063726000019/etsy-20251231.htm | "agentic search" |
| ETSY INC  (ETSY)  (CIK 0001370637) | 8-K | 2026-04-29 | https://www.sec.gov/Archives/edgar/data/1370637/000137063726000042/q126shareholderletter.htm | "ChatGPT" "traffic"; "agentic search" |
| ETSY INC  (ETSY)  (CIK 0001370637) | 10-Q | 2026-04-29 | https://www.sec.gov/Archives/edgar/data/1370637/000137063726000044/etsy-20260331.htm | "agentic search" |
| ETSY INC  (ETSY)  (CIK 0001370637) | 10-Q | 2026-08-05 | https://www.sec.gov/Archives/edgar/data/1370637/000137063726000080/etsy-20260630.htm | "agentic search" |
| EXTREME NETWORKS INC  (EXTR)  (CIK 0001078271) | 10-K | 2026-08-17 | https://www.sec.gov/Archives/edgar/data/1078271/000119312526352872/extr-20260630.htm | "AI assistants" "traffic" |
| Edgewise Therapeutics, Inc.  (EWTX)  (CIK 0001710072) | 10-K | 2026-02-26 | https://www.sec.gov/Archives/edgar/data/1710072/000110465926020112/ewtx-20251231x10k.htm | "LLMs" "referral" |
| Edgewise Therapeutics, Inc.  (EWTX)  (CIK 0001710072) | 10-Q | 2026-05-07 | https://www.sec.gov/Archives/edgar/data/1710072/000110465926056713/ewtx-20260331x10q.htm | "LLMs" "referral" |
| Edgewise Therapeutics, Inc.  (EWTX)  (CIK 0001710072) | 10-Q | 2026-08-06 | https://www.sec.gov/Archives/edgar/data/1710072/000110465926091670/ewtx-20260630x10q.htm | "LLMs" "referral" |
| Ehave, Inc.  (EHVVF)  (CIK 0001653606) | 20-F/A | 2026-05-19 | https://www.sec.gov/Archives/edgar/data/1653606/000149315226024273/form20-fa.htm | "AI platforms" "referrals" |
| Eightco Holdings Inc.  (ORBS)  (CIK 0001892492) | 10-K | 2026-04-15 | https://www.sec.gov/Archives/edgar/data/1892492/000149315226016664/form10-k.htm | "ChatGPT" "traffic" |
| Eightco Holdings Inc.  (ORBS)  (CIK 0001892492) | 8-K | 2026-04-16 | https://www.sec.gov/Archives/edgar/data/1892492/000149315226016990/ex99-1.htm | "ChatGPT" "traffic" |
| Eightco Holdings Inc.  (ORBS)  (CIK 0001892492) | 8-K | 2026-04-21 | https://www.sec.gov/Archives/edgar/data/1892492/000149315226018212/ex99-1.htm | "ChatGPT" "traffic" |
| Eightco Holdings Inc.  (ORBS)  (CIK 0001892492) | 8-K | 2026-05-06 | https://www.sec.gov/Archives/edgar/data/1892492/000149315226021420/ex99-1.htm | "ChatGPT" "traffic" |
| Eightco Holdings Inc.  (ORBS)  (CIK 0001892492) | 8-K | 2026-05-13 | https://www.sec.gov/Archives/edgar/data/1892492/000149315226022618/ex99-1.htm | "ChatGPT" "traffic" |
| Eightco Holdings Inc.  (ORBS)  (CIK 0001892492) | 8-K | 2026-05-21 | https://www.sec.gov/Archives/edgar/data/1892492/000149315226024742/ex99-1.htm | "ChatGPT" "traffic" |
| Eightco Holdings Inc.  (ORBS)  (CIK 0001892492) | 8-K | 2026-05-28 | https://www.sec.gov/Archives/edgar/data/1892492/000149315226025547/ex99-1.htm | "ChatGPT" "traffic" |
| Eightco Holdings Inc.  (ORBS)  (CIK 0001892492) | 8-K | 2026-06-04 | https://www.sec.gov/Archives/edgar/data/1892492/000149315226027206/ex99-1.htm | "ChatGPT" "traffic" |
| Eightco Holdings Inc.  (ORBS)  (CIK 0001892492) | 8-K | 2026-09-17 | https://www.sec.gov/Archives/edgar/data/1892492/000149315226043055/ex99-1.htm | "ChatGPT" "traffic" |
| Elastic N.V.  (ESTC)  (CIK 0001707753) | 10-K | 2025-06-10 | https://www.sec.gov/Archives/edgar/data/1707753/000170775325000021/estc-20250430.htm | "LLM" "referral"; "LLMs" "referral" |
| Elastic N.V.  (ESTC)  (CIK 0001707753) | 10-K | 2026-06-08 | https://www.sec.gov/Archives/edgar/data/1707753/000170775326000018/estc-20260430.htm | "AI search" "traffic"; "AI-powered search" "traffic"; "LLM" "referral"; "LLMs" "referral" |
| Elements Ventures Group Inc.  (CIK 0001954227) | S-1 | 2026-07-17 | https://www.sec.gov/Archives/edgar/data/1954227/000209757026000025/elements-20260707_s1.htm | "AI assistants" "traffic" |
| Ethos Technologies Inc.  (LIFE)  (CIK 0001788451) | 10-Q | 2026-05-08 | https://www.sec.gov/Archives/edgar/data/1788451/000119312526214620/life-20260331.htm | "AI platforms" "referrals" |
| Ethos Technologies Inc.  (LIFE)  (CIK 0001788451) | 10-Q | 2026-08-05 | https://www.sec.gov/Archives/edgar/data/1788451/000119312526335209/life-20260630.htm | "AI platforms" "referrals" |
| Evaxion A/S  (EVAX)  (CIK 0001828253) | 20-F | 2026-03-05 | https://www.sec.gov/Archives/edgar/data/1828253/000117184326001346/evax20251231_20f.htm | "AI platforms" "referrals" |
| Eventbrite, Inc.  (EB)  (CIK 0001475115) | 10-K | 2025-02-27 | https://www.sec.gov/Archives/edgar/data/1475115/000147511525000026/eb-20241231.htm | "AI search" "conversion"; "AI search" "traffic" |
| Eventbrite, Inc.  (EB)  (CIK 0001475115) | 10-K | 2026-03-12 | https://www.sec.gov/Archives/edgar/data/1475115/000147511526000005/eb-20251231.htm | "AI search" "conversion"; "AI search" "traffic" |
| EverQuote, Inc.  (EVER)  (CIK 0001640428) | 8-K | 2026-08-03 | https://www.sec.gov/Archives/edgar/data/1640428/000119312526330540/ever-ex99_2.htm | "ChatGPT" "traffic" |
| Evogene Ltd.  (EVGN)  (CIK 0001574565) | 6-K | 2025-11-20 | https://www.sec.gov/Archives/edgar/data/1574565/000117891325003915/exhibit_99-1.htm | "AI discovery" |
| Evogene Ltd.  (EVGN)  (CIK 0001574565) | 6-K | 2025-12-30 | https://www.sec.gov/Archives/edgar/data/1574565/000117891325004127/exhibit_99-1.htm | "AI discovery" |
| Expedia Group, Inc.  (EXPE)  (CIK 0001324424) | 10-K | 2026-02-13 | https://www.sec.gov/Archives/edgar/data/1324424/000132442426000008/expe-20251231.htm | "AI search" "conversion"; "AI search" "traffic" |
| Expedia Group, Inc.  (EXPE)  (CIK 0001324424) | 10-Q | 2026-05-08 | https://www.sec.gov/Archives/edgar/data/1324424/000132442426000035/expe-20260331.htm | "AI platforms" "referrals" |
| Expedia Group, Inc.  (EXPE)  (CIK 0001324424) | 10-Q | 2026-08-06 | https://www.sec.gov/Archives/edgar/data/1324424/000132442426000053/expe-20260630.htm | "AI platforms" "referrals" |
| F5, INC.  (FFIV)  (CIK 0001048695) | 10-Q | 2026-08-06 | https://www.sec.gov/Archives/edgar/data/1048695/000104869526000067/ffiv-20260630.htm | "AI discovery" |
| FAST CASUAL CONCEPTS, INC.  (FCCI)  (CIK 0001807689) | 10-K | 2026-03-31 | https://www.sec.gov/Archives/edgar/data/1807689/000117152026000037/eps12514_fcci.htm | "AI platforms" "referrals" |
| Fastly, Inc.  (FSLY)  (CIK 0001517413) | 10-K | 2025-02-26 | https://www.sec.gov/Archives/edgar/data/1517413/000151741325000063/fsly-20241231.htm | "LLM" "referral"; "LLMs" "referral" |
| Fastly, Inc.  (FSLY)  (CIK 0001517413) | 8-K | 2025-11-05 | https://www.sec.gov/Archives/edgar/data/1517413/000151741325000293/ex991-fslypressrelease93025.htm | "AI assistants" "traffic" |
| Fastly, Inc.  (FSLY)  (CIK 0001517413) | 8-K | 2025-11-05 | https://www.sec.gov/Archives/edgar/data/1517413/000151741325000293/ex992-investorsupplement93.htm | "AI assistants" "traffic" |
| Fastly, Inc.  (FSLY)  (CIK 0001517413) | 10-K | 2026-02-25 | https://www.sec.gov/Archives/edgar/data/1517413/000151741326000053/fsly-20251231.htm | "AI assistants" "traffic"; "AI-driven traffic"; "LLM" "referral"; "generative engine optimization" |
| Fastly, Inc.  (FSLY)  (CIK 0001517413) | 10-Q | 2026-05-06 | https://www.sec.gov/Archives/edgar/data/1517413/000151741326000132/fsly-20260331.htm | "AI-driven traffic" |
| Fastly, Inc.  (FSLY)  (CIK 0001517413) | 10-Q | 2026-08-05 | https://www.sec.gov/Archives/edgar/data/1517413/000151741326000213/fsly-20260630.htm | "AI-driven traffic" |
| Fidelity Private Credit Co LLC  (CIK 0001899996) | 10-K | 2026-03-23 | https://www.sec.gov/Archives/edgar/data/1899996/000119312526119504/ck0001899996-20251231.htm | "ChatGPT" "referral" |
| Fidelity Private Credit Fund  (CIK 0001920453) | 10-K | 2026-03-23 | https://www.sec.gov/Archives/edgar/data/1920453/000119312526119488/ck0001920453-20251231.htm | "ChatGPT" "referral" |
| Figma, Inc.  (FIG)  (CIK 0001579878) | 10-K | 2026-02-18 | https://www.sec.gov/Archives/edgar/data/1579878/000162828026009228/fig-20251231.htm | "ChatGPT" "traffic" |
| FinVolution Group  (FINV, FVGPY)  (CIK 0001691445) | 20-F | 2026-04-29 | https://www.sec.gov/Archives/edgar/data/1691445/000149315226019597/form20-f.htm | "LLM" "referral" |
| FiscalNote Holdings, Inc.  (NOTE, NOTE-WT)  (CIK 0001823466) | 10-K | 2026-03-24 | https://www.sec.gov/Archives/edgar/data/1823466/000119312526120769/note-20251231.htm | "ChatGPT" "bookings"; "ChatGPT" "new members" |
| Five9, Inc.  (FIVN)  (CIK 0001288847) | 10-K | 2025-02-21 | https://www.sec.gov/Archives/edgar/data/1288847/000128884725000028/fivn-20241231.htm | "LLMs" "referral" |
| Five9, Inc.  (FIVN)  (CIK 0001288847) | 10-K | 2026-02-20 | https://www.sec.gov/Archives/edgar/data/1288847/000128884726000023/fivn-20251231.htm | "LLMs" "referral" |
| Fiverr International Ltd.  (FVRR)  (CIK 0001762301) | 20-F | 2026-03-12 | https://www.sec.gov/Archives/edgar/data/1762301/000117891326000858/zk2634486.htm | "AI assistants" "traffic"; "AI platforms" "referrals"; "generative engine optimization" |
| Flywire Corp  (FLYW)  (CIK 0001580560) | 10-Q | 2025-11-10 | https://www.sec.gov/Archives/edgar/data/1580560/000119312525274358/flyw-20250930.htm | "ChatGPT" "referral" |
| Flywire Corp  (FLYW)  (CIK 0001580560) | 10-K | 2026-02-24 | https://www.sec.gov/Archives/edgar/data/1580560/000119312526067540/flyw-20251231.htm | "ChatGPT" "referral" |
| Flywire Corp  (FLYW)  (CIK 0001580560) | 10-Q | 2026-05-06 | https://www.sec.gov/Archives/edgar/data/1580560/000158056026000005/flyw-20260331.htm | "ChatGPT" "bookings"; "ChatGPT" "referral"; "ChatGPT" "traffic" |
| Flywire Corp  (FLYW)  (CIK 0001580560) | 10-Q | 2026-08-05 | https://www.sec.gov/Archives/edgar/data/1580560/000158056026000016/flyw-20260630.htm | "ChatGPT" "bookings"; "ChatGPT" "referral"; "ChatGPT" "traffic" |
| Football Manager SPAC Inc.  (CIK 0002133939) | S-1 | 2026-09-09 | https://www.sec.gov/Archives/edgar/data/2133939/000110465926106403/tmb-20260910xs1.htm | "LLM" "referral" |
| Fortinet, Inc.  (FTNT)  (CIK 0001262039) | 10-Q | 2026-07-30 | https://www.sec.gov/Archives/edgar/data/1262039/000126203926000021/ftnt-20260630.htm | "AI visibility" |
| Freshworks Inc.  (FRSH)  (CIK 0001544522) | 10-K | 2026-02-26 | https://www.sec.gov/Archives/edgar/data/1544522/000154452226000036/frsh-20251231.htm | "AI search" "conversion"; "AI search" "traffic"; "AI-powered search" "traffic"; "LLM" "referral" |
| Freshworks Inc.  (FRSH)  (CIK 0001544522) | 8-K | 2026-05-14 | https://www.sec.gov/Archives/edgar/data/1544522/000119312526224188/d14719dex991.htm | "ChatGPT" "bookings" |
| Futu Holdings Ltd  (FUTU)  (CIK 0001754581) | 20-F | 2026-04-15 | https://www.sec.gov/Archives/edgar/data/1754581/000110465926043451/futu-20251231x20f.htm | "AI-powered search" "traffic" |
| FutureCore Acquisition Corp  (CIK 0002142699) | S-1 | 2026-09-11 | https://www.sec.gov/Archives/edgar/data/2142699/000182912626010047/futurecoreacq_s1.htm | "generative engine optimization" |
| GENESCO INC  (GCO)  (CIK 0000018498) | 8-K | 2026-03-06 | https://www.sec.gov/Archives/edgar/data/18498/000119312526094963/gco-ex99_2.htm | "agentic search" |
| GENESCO INC  (GCO)  (CIK 0000018498) | 8-K | 2026-05-29 | https://www.sec.gov/Archives/edgar/data/18498/000119312526246280/gco-ex99_2.htm | "agentic search" |
| GENESCO INC  (GCO)  (CIK 0000018498) | 8-K | 2026-09-03 | https://www.sec.gov/Archives/edgar/data/18498/000119312526381023/gco-ex99_2.htm | "agentic search" |
| GENMAB A/S  (GMAB, GNMSF)  (CIK 0001434265) | 6-K | 2025-02-12 | https://www.sec.gov/Archives/edgar/data/1434265/000155837025000831/gmab-20241231xex99d1a.htm | "ChatGPT" "new members" |
| GENMAB A/S  (GMAB, GNMSF)  (CIK 0001434265) | 6-K | 2025-02-12 | https://www.sec.gov/Archives/edgar/data/1434265/000155837025000831/gmab-20241231xex99d1.htm | "ChatGPT" "new members" |
| GENMAB A/S  (GMAB, GNMSF)  (CIK 0001434265) | 20-F | 2026-02-17 | https://www.sec.gov/Archives/edgar/data/1434265/000143426526000014/gmab-20251231.htm | "ChatGPT" "new members" |
| GRID DYNAMICS HOLDINGS, INC.  (GDYN)  (CIK 0001743725) | 10-K | 2026-03-05 | https://www.sec.gov/Archives/edgar/data/1743725/000174372526000007/gdyn-20251231.htm | "AI search" "conversion" |
| GSI TECHNOLOGY INC  (GSIT)  (CIK 0001126741) | 10-K | 2026-06-05 | https://www.sec.gov/Archives/edgar/data/1126741/000110465926070962/gsit-20260331x10k.htm | "AI search" "traffic" |
| GSI TECHNOLOGY INC  (GSIT)  (CIK 0001126741) | 10-Q | 2026-08-11 | https://www.sec.gov/Archives/edgar/data/1126741/000110465926094044/gsit-20260630x10q.htm | "AI search" "traffic" |
| Gambling.com Group Ltd  (GAMB)  (CIK 0001839799) | 20-F | 2025-03-20 | https://www.sec.gov/Archives/edgar/data/1839799/000183979925000022/gamb-20241231.htm | "AI Overviews" "traffic"; "ChatGPT" "referral"; "ChatGPT" "traffic"; "answer engines" |
| Gambling.com Group Ltd  (GAMB)  (CIK 0001839799) | 6-K | 2025-04-04 | https://www.sec.gov/Archives/edgar/data/1839799/000183979925000038/a2024annualreport.pdf | "AI Overviews" "traffic"; "AI-powered search" "traffic"; "ChatGPT" "referral"; "ChatGPT" "traffic"; "answer engines"; "traffic from AI" |
| Gambling.com Group Ltd  (GAMB)  (CIK 0001839799) | 20-F | 2026-03-19 | https://www.sec.gov/Archives/edgar/data/1839799/000183979926000048/gamb-20251231.htm | "AI Overviews" "traffic"; "ChatGPT" "referral"; "ChatGPT" "traffic"; "Perplexity" "traffic"; "answer engines" |
| Gamehaus Holdings Inc.  (GMHS)  (CIK 0002000530) | F-1 | 2025-05-23 | https://www.sec.gov/Archives/edgar/data/2000530/000164117225012159/formf-1.htm | "ChatGPT" "bookings" |
| Gamehaus Holdings Inc.  (GMHS)  (CIK 0002000530) | F-1/A | 2025-06-13 | https://www.sec.gov/Archives/edgar/data/2000530/000164117225015069/formf-1a.htm | "ChatGPT" "bookings" |
| Gamehaus Holdings Inc.  (GMHS)  (CIK 0002000530) | 20-F | 2025-10-23 | https://www.sec.gov/Archives/edgar/data/2000530/000149315225019002/form20-f.htm | "ChatGPT" "bookings"; "ChatGPT" "traffic" |
| Gannett Co., Inc.  (GCI)  (CIK 0001579684) | 8-K | 2025-07-31 | https://www.sec.gov/Archives/edgar/data/1579684/000157968425000061/gciq22025ex991earningsrele.htm | "Perplexity" "traffic"; "answer engine" |
| Gemini Space Station, Inc.  (GEMI)  (CIK 0002055592) | 8-K | 2026-05-14 | https://www.sec.gov/Archives/edgar/data/2055592/000205559226000048/gemiq12026earningsreleas.htm | "ChatGPT" "referral" |
| GenEmbryomics Ltd  (XGEN)  (CIK 0002038033) | F-1/A | 2025-03-17 | https://www.sec.gov/Archives/edgar/data/2038033/000143774925007827/ex_790183.htm | "LLM" "referral" |
| GeneDx Holdings Corp.  (WGS, WGSWW)  (CIK 0001818331) | 10-K | 2025-02-20 | https://www.sec.gov/Archives/edgar/data/1818331/000181833125000021/wgs-20241231.htm | "AI platforms" "referrals" |
| GeneDx Holdings Corp.  (WGS, WGSWW)  (CIK 0001818331) | 10-K | 2026-02-23 | https://www.sec.gov/Archives/edgar/data/1818331/000181833126000015/wgs-20251231.htm | "AI platforms" "referrals" |
| Genius Group Ltd  (GNS)  (CIK 0001847806) | 6-K | 2026-06-05 | https://www.sec.gov/Archives/edgar/data/1847806/000149315226027417/ex99-2.htm | "answer engine" |
| Genius Sports Ltd  (GENI)  (CIK 0001834489) | 20-F | 2026-03-17 | https://www.sec.gov/Archives/edgar/data/1834489/000119312526110749/geni-20251231.htm | "AI platforms" "referrals" |
| Ginkgo Bioworks Holdings, Inc.  (DNA, DNABW)  (CIK 000183021 | 10-K | 2025-02-25 | https://www.sec.gov/Archives/edgar/data/1830214/000162828025007819/dna-20241231.htm | "LLM" "referral"; "LLMs" "referral" |
| Ginkgo Bioworks Holdings, Inc.  (DNA, DNABW)  (CIK 000183021 | 10-K | 2026-02-26 | https://www.sec.gov/Archives/edgar/data/1830214/000162828026012346/dna-20251231.htm | "LLMs" "referral" |
| Glidelogic Corp.  (GDLG)  (CIK 0001848672) | 10-Q | 2025-09-05 | https://www.sec.gov/Archives/edgar/data/1848672/000109690625001483/gdlg-20250731_10q.htm | "generative engine optimization" |
| Glidelogic Corp.  (GDLG)  (CIK 0001848672) | 10-Q | 2025-12-05 | https://www.sec.gov/Archives/edgar/data/1848672/000109690625001969/gdlg-20251031_10q.htm | "generative engine optimization" |
| Glidelogic Corp.  (GDLG)  (CIK 0001848672) | 10-K | 2026-04-27 | https://www.sec.gov/Archives/edgar/data/1848672/000109690626000615/gdlg-20260131_10k.htm | "ChatGPT" "traffic"; "generative engine optimization" |
| Global Business Travel Group, Inc.  (GBTG)  (CIK 0001820872) | 10-K | 2025-03-07 | https://www.sec.gov/Archives/edgar/data/1820872/000162828025011370/gbtg-20241231.htm | "LLM" "referral"; "LLMs" "referral" |
| Global Business Travel Group, Inc.  (GBTG)  (CIK 0001820872) | 10-K | 2026-03-09 | https://www.sec.gov/Archives/edgar/data/1820872/000162828026015817/gbtg-20251231.htm | "LLM" "referral"; "LLMs" "referral" |
| Global-E Online Ltd.  (GLBE)  (CIK 0001835963) | 20-F | 2025-03-27 | https://www.sec.gov/Archives/edgar/data/1835963/000117891325001086/zk2532899.htm | "ChatGPT" "referral"; "ChatGPT" "traffic" |
| Global-E Online Ltd.  (GLBE)  (CIK 0001835963) | 20-F | 2026-03-26 | https://www.sec.gov/Archives/edgar/data/1835963/000117891326001772/zk2634880.htm | "ChatGPT" "referral"; "ChatGPT" "traffic" |
| Globant S.A.  (GLOB)  (CIK 0001557860) | 20-F | 2025-02-28 | https://www.sec.gov/Archives/edgar/data/1557860/000162828025009110/glob-20241231.htm | "AI platforms" "referrals" |
| Globant S.A.  (GLOB)  (CIK 0001557860) | 20-F | 2026-02-27 | https://www.sec.gov/Archives/edgar/data/1557860/000162828026012910/glob-20251231.htm | "AI platforms" "referrals" |
| Gloo Holdings, Inc.  (CIK 0002069785) | S-1 | 2025-10-17 | https://www.sec.gov/Archives/edgar/data/2069785/000119312525242216/ck0002069785-20251017.htm | "LLM" "referral" |
| Gloo Holdings, Inc.  (CIK 0002069785) | S-1/A | 2025-10-30 | https://www.sec.gov/Archives/edgar/data/2069785/000119312525258610/ck0002069785-20251030.htm | "LLM" "referral" |
| Gloo Holdings, Inc.  (CIK 0002069785) | 424B4 | 2025-11-19 | https://www.sec.gov/Archives/edgar/data/2069785/000119312525288305/project_grace_424b4.htm | "LLM" "referral" |
| GoDaddy Inc.  (GDDY)  (CIK 0001609711) | 10-Q | 2025-10-31 | https://www.sec.gov/Archives/edgar/data/1609711/000160971125000209/gddy-20250930.htm | "LLM" "referral" |
| GoDaddy Inc.  (GDDY)  (CIK 0001609711) | 10-K | 2026-02-25 | https://www.sec.gov/Archives/edgar/data/1609711/000160971126000010/gddy-20251231.htm | "LLM" "referral"; "LLMs" "referral" |
| GoDaddy Inc.  (GDDY)  (CIK 0001609711) | 10-Q | 2026-05-01 | https://www.sec.gov/Archives/edgar/data/1609711/000160971126000037/gddy-20260331.htm | "LLM" "referral"; "LLMs" "referral" |
| GoDaddy Inc.  (GDDY)  (CIK 0001609711) | 10-Q | 2026-07-31 | https://www.sec.gov/Archives/edgar/data/1609711/000160971126000088/gddy-20260630.htm | "LLM" "referral" |
| Graham Holdings Co  (GHC)  (CIK 0000104889) | 10-K | 2025-02-26 | https://www.sec.gov/Archives/edgar/data/104889/000010488925000022/ghc-20241231.htm | "generative AI" "referral traffic" |
| Guardforce AI Co., Ltd.  (GFAI, GFAIW)  (CIK 0001804469) | 20-F | 2026-04-21 | https://www.sec.gov/Archives/edgar/data/1804469/000121390026046137/ea0284325-20f_guardforce.htm | "ChatGPT" "traffic" |
| Guardforce AI Co., Ltd.  (GFAI, GFAIW, GRDAF)  (CIK 00018044 | 20-F | 2025-04-28 | https://www.sec.gov/Archives/edgar/data/1804469/000121390025036049/ea0236715-20f_guardforce.htm | "ChatGPT" "traffic" |
| HDFC BANK LTD  (HDB)  (CIK 0001144967) | 20-F | 2025-07-14 | https://www.sec.gov/Archives/edgar/data/1144967/000119312525158722/d854075d20f.htm | "LLM" "referral" |
| HDFC BANK LTD  (HDB)  (CIK 0001144967) | 6-K | 2026-07-14 | https://www.sec.gov/Archives/edgar/data/1144967/000119312526302438/d140627dex99.pdf | "LLMs" "referral" |
| HOST HOTELS & RESORTS, INC.  (HST)  (CIK 0001070750) | 10-K | 2025-02-26 | https://www.sec.gov/Archives/edgar/data/1070750/000107075025000071/hst-20241231.htm | "AI search" "conversion" |
| HOST HOTELS & RESORTS, INC.  (HST)  (CIK 0001070750) | 10-K | 2026-02-25 | https://www.sec.gov/Archives/edgar/data/1070750/000107075026000054/hst-20251231.htm | "AI search" "conversion"; "AI search" "traffic" |
| HUBSPOT INC  (HUBS)  (CIK 0001404655) | 10-Q | 2025-11-05 | https://www.sec.gov/Archives/edgar/data/1404655/000119312525267056/hubs-20250930.htm | "answer engine" |
| HUBSPOT INC  (HUBS)  (CIK 0001404655) | 10-K | 2026-02-11 | https://www.sec.gov/Archives/edgar/data/1404655/000119312526046646/hubs-20251231.htm | "AI-referred"; "answer engine" |
| HUBSPOT INC  (HUBS)  (CIK 0001404655) | 10-Q | 2026-05-07 | https://www.sec.gov/Archives/edgar/data/1404655/000119312526212122/hubs-20260331.htm | "AI-referred" |
| HUBSPOT INC  (HUBS)  (CIK 0001404655) | 10-Q | 2026-08-05 | https://www.sec.gov/Archives/edgar/data/1404655/000119312526335232/hubs-20260630.htm | "AI-referred" |
| Hancock Park Corporate Income, Inc.  (CIK 0001661306) | 10-K | 2025-03-14 | https://www.sec.gov/Archives/edgar/data/1661306/000166130625000013/hpci-20241231.htm | "ChatGPT" "referral" |
| Health In Tech, Inc.  (HIT)  (CIK 0002019505) | 10-K | 2026-03-25 | https://www.sec.gov/Archives/edgar/data/2019505/000121390026034211/ea0283147-10k_health.htm | "AI platforms" "referrals" |
| HealthLynked Corp  (HLYK)  (CIK 0001680139) | S-1 | 2026-02-10 | https://www.sec.gov/Archives/edgar/data/1680139/000121390026013824/ea0275639-s1_health.htm | "LLM" "referral"; "LLMs" "referral" |
| HealthLynked Corp  (HLYK)  (CIK 0001680139) | 10-K | 2026-03-31 | https://www.sec.gov/Archives/edgar/data/1680139/000121390026037499/ea0282013-10k_health.htm | "LLM" "referral"; "LLMs" "referral" |
| HealthLynked Corp  (HLYK)  (CIK 0001680139) | S-1/A | 2026-04-30 | https://www.sec.gov/Archives/edgar/data/1680139/000121390026050297/ea0286031-s1a1_health.htm | "LLM" "referral"; "LLMs" "referral" |
| HealthLynked Corp  (HLYK)  (CIK 0001680139) | S-1/A | 2026-05-29 | https://www.sec.gov/Archives/edgar/data/1680139/000121390026062879/ea0292204-s1a2_health.htm | "LLM" "referral"; "LLMs" "referral" |
| High Roller Technologies, Inc.  (ROLR)  (CIK 0001947210) | 8-K | 2026-01-21 | https://www.sec.gov/Archives/edgar/data/1947210/000175392626000160/ex992_2.htm | "AI citations" |
| High Roller Technologies, Inc.  (ROLR)  (CIK 0001947210) | 8-K | 2026-04-20 | https://www.sec.gov/Archives/edgar/data/1947210/000175392626000693/ex992_3.htm | "AI citations" |
| Hyatt Hotels Corp  (H)  (CIK 0001468174) | 10-K | 2026-02-13 | https://www.sec.gov/Archives/edgar/data/1468174/000146817426000007/h-20251231.htm | "ChatGPT" "bookings"; "ChatGPT" "new members" |
| Hyatt Hotels Corp  (H)  (CIK 0001468174) | 8-K | 2026-05-28 | https://www.sec.gov/Archives/edgar/data/1468174/000110465926067209/tm2615108d1_ex99-1.htm | "ChatGPT" "bookings"; "ChatGPT" "new members" |
| IAC Inc.  (IAC)  (CIK 0001800227) | 8-K | 2025-11-03 | https://www.sec.gov/Archives/edgar/data/1800227/000162828025048237/iacq32025earningscallpre.htm | "AI Overviews" "traffic" |
| IAC Inc.  (IAC)  (CIK 0001800227) | 8-K | 2025-11-03 | https://www.sec.gov/Archives/edgar/data/1800227/000162828025048237/ex_991q32025iac-pressrelea.htm | "AI Overviews" "traffic" |
| IAC Inc.  (IAC)  (CIK 0001800227) | 10-Q | 2025-11-03 | https://www.sec.gov/Archives/edgar/data/1800227/000162828025048244/iaci-20250930.htm | "AI Overviews" "traffic" |
| IAC Inc.  (IAC)  (CIK 0001800227) | 8-K | 2026-02-03 | https://www.sec.gov/Archives/edgar/data/1800227/000162828026004988/ex_991q42025iac-pressrelea.htm | "AI Overviews" "traffic" |
| IAC Inc.  (IAC)  (CIK 0001800227) | 10-K | 2026-02-20 | https://www.sec.gov/Archives/edgar/data/1800227/000162828026009997/iaci-20251231.htm | "AI Overviews" "traffic"; "AI search" "conversion"; "AI search" "traffic" |
| IAC Inc.  (IAC)  (CIK 0001800227) | 8-K | 2026-05-04 | https://www.sec.gov/Archives/edgar/data/1800227/000162828026029796/q12026iacearningscallpre.htm | "AI Overviews" "traffic" |
| IAC Inc.  (IAC)  (CIK 0001800227) | 8-K | 2026-05-04 | https://www.sec.gov/Archives/edgar/data/1800227/000162828026029796/ex_991q12026iac-pressrelea.htm | "AI Overviews" "traffic" |
| IAC Inc.  (IAC)  (CIK 0001800227) | 10-Q | 2026-05-04 | https://www.sec.gov/Archives/edgar/data/1800227/000162828026029798/iaci-20260331.htm | "AI Overviews" "traffic" |
| ICICI BANK LTD  (IBN)  (CIK 0001103838) | 6-K | 2026-07-22 | https://www.sec.gov/Archives/edgar/data/1103838/000095010326011004/dp250272_ex9901.pdf | "LLM" "referral" |
| INNOCAN PHARMA Corp  (CIK 0001889791) | F-1 | 2025-07-23 | https://www.sec.gov/Archives/edgar/data/1889791/000164117225020718/formf-1.htm | "LLM" "referral" |
| INNOCAN PHARMA Corp  (INNP, INNPD)  (CIK 0001889791) | F-1/A | 2025-09-30 | https://www.sec.gov/Archives/edgar/data/1889791/000149315225016393/formf-1a.htm | "LLM" "referral" |
| INNOCAN PHARMA Corp  (INNP, INNPF)  (CIK 0001889791) | F-1/A | 2025-08-04 | https://www.sec.gov/Archives/edgar/data/1889791/000149315225011564/formf-1a.htm | "LLM" "referral" |
| INNOCAN PHARMA Corp  (INNP, INNPF)  (CIK 0001889791) | F-1/A | 2025-09-05 | https://www.sec.gov/Archives/edgar/data/1889791/000149315225012688/formf-1a.htm | "LLM" "referral" |
| INNOCAN PHARMA Corp  (INNP, INNPF)  (CIK 0001889791) | F-1/A | 2025-12-10 | https://www.sec.gov/Archives/edgar/data/1889791/000149315225027017/formf-1a.htm | "LLM" "referral" |
| INNOCAN PHARMA Corp  (INNP, INNPF)  (CIK 0001889791) | F-1/A | 2026-01-06 | https://www.sec.gov/Archives/edgar/data/1889791/000149315226000539/formf-1a.htm | "LLM" "referral" |
| INNOCAN PHARMA Corp  (INNP, INNPF)  (CIK 0001889791) | F-1/A | 2026-04-03 | https://www.sec.gov/Archives/edgar/data/1889791/000149315226015152/formf-1a.htm | "LLM" "referral" |
| INNOCAN PHARMA Corp  (INNPF)  (CIK 0001889791) | F-1 | 2026-03-16 | https://www.sec.gov/Archives/edgar/data/1889791/000149315226010255/formf-1.htm | "LLM" "referral" |
| INNODATA INC  (INOD)  (CIK 0000903651) | 10-K | 2025-02-24 | https://www.sec.gov/Archives/edgar/data/903651/000141057825000194/inod-20241231x10k.htm | "ChatGPT" "traffic" |
| INTELLIGENT PROTECTION MANAGEMENT CORP.  (IPM)  (CIK 0001355 | 10-K | 2025-03-24 | https://www.sec.gov/Archives/edgar/data/1355839/000101376225001600/ea0233784-10k_intelligent.htm | "generative engine optimization" |
| INTELLIGENT PROTECTION MANAGEMENT CORP.  (IPM)  (CIK 0001355 | 10-K | 2026-03-17 | https://www.sec.gov/Archives/edgar/data/1355839/000121390026029095/ea0277611-10k_intelligent.htm | "generative engine optimization" |
| INTERCONTINENTAL HOTELS GROUP PLC /NEW/  (IHG, ICHGF)  (CIK  | 6-K | 2026-02-17 | https://www.sec.gov/Archives/edgar/data/858446/000165495426001290/a2532t.htm | "AI search" "conversion" |
| INTERCONTINENTAL HOTELS GROUP PLC /NEW/  (IHG, ICHGF)  (CIK  | 6-K | 2026-08-11 | https://www.sec.gov/Archives/edgar/data/858446/000165495426007436/a0528q.htm | "AI search" "conversion"; "ChatGPT" "bookings" |
| INTERNATIONAL BUSINESS MACHINES CORP  (IBM)  (CIK 0000051143 | 8-K | 2025-02-04 | https://www.sec.gov/Archives/edgar/data/51143/000005114325000010/ibm-ex99_1.htm | "ChatGPT" "bookings" |
| INTUIT INC.  (INTU)  (CIK 0000896878) | 10-K | 2025-09-03 | https://www.sec.gov/Archives/edgar/data/896878/000089687825000035/intu-20250731.htm | "generative engine optimization" |
| INTUIT INC.  (INTU)  (CIK 0000896878) | 10-K | 2026-09-09 | https://www.sec.gov/Archives/edgar/data/896878/000089687826000037/intu-20260731.htm | "generative engine optimization" |
| IREN Ltd  (IREN)  (CIK 0001878848) | 10-K | 2026-08-27 | https://www.sec.gov/Archives/edgar/data/1878848/000187884826000052/iren-20260630.htm | "AI platforms" "referrals"; "Perplexity" "traffic" |
| IZEA Worldwide, Inc.  (IZEA)  (CIK 0001495231) | 10-K | 2025-03-27 | https://www.sec.gov/Archives/edgar/data/1495231/000149523125000050/izea-20241231.htm | "ChatGPT" "bookings"; "ChatGPT" "traffic" |
| Iambic Therapeutics, Inc.  (CIK 0001997038) | S-1 | 2026-09-21 | https://www.sec.gov/Archives/edgar/data/1997038/000119312526396704/iam-20260921.htm | "AI discovery"; "AI platforms" "referrals"; "LLM" "referral" |
| ImmunoPrecise Antibodies Ltd.  (IPA)  (CIK 0001715925) | 6-K | 2025-01-22 | https://www.sec.gov/Archives/edgar/data/1715925/000095017025007566/ipa-ex99_1.htm | "AI discovery" |
| ImmunoPrecise Antibodies Ltd.  (IPA)  (CIK 0001715925) | 6-K | 2025-08-27 | https://www.sec.gov/Archives/edgar/data/1715925/000095017025111598/ipa-ex99_1.htm | "AI discovery" |
| Information Services Group Inc.  (III)  (CIK 0001371489) | 10-K | 2026-03-06 | https://www.sec.gov/Archives/edgar/data/1371489/000110465926024573/iii-20251231x10k.htm | "AI platforms" "referrals" |
| Innovative Eyewear Inc  (LUCY, LUCYW)  (CIK 0001808377) | 10-K | 2025-03-24 | https://www.sec.gov/Archives/edgar/data/1808377/000182912625002025/innovative_10k.htm | "AI assistants" "traffic"; "ChatGPT" "referral"; "ChatGPT" "traffic" |
| Innovative Eyewear Inc  (LUCY, LUCYW)  (CIK 0001808377) | S-1 | 2025-05-09 | https://www.sec.gov/Archives/edgar/data/1808377/000182912625003518/innovativeeye_s1.htm | "AI assistants" "traffic"; "ChatGPT" "traffic" |
| Innovative Eyewear Inc  (LUCY, LUCYW)  (CIK 0001808377) | 10-Q | 2025-05-13 | https://www.sec.gov/Archives/edgar/data/1808377/000182912625003623/innovative_10q.htm | "ChatGPT" "referral" |
| Innovative Eyewear Inc  (LUCY, LUCYW)  (CIK 0001808377) | S-1 | 2025-07-18 | https://www.sec.gov/Archives/edgar/data/1808377/000182912625005161/innovativeeye_s1.htm | "AI assistants" "traffic"; "ChatGPT" "traffic" |
| Innovative Eyewear Inc  (LUCY, LUCYW)  (CIK 0001808377) | 10-Q | 2025-08-14 | https://www.sec.gov/Archives/edgar/data/1808377/000182912625006313/innovative_10q.htm | "ChatGPT" "referral" |
| Innovative Eyewear Inc  (LUCY, LUCYW)  (CIK 0001808377) | 10-Q | 2025-11-13 | https://www.sec.gov/Archives/edgar/data/1808377/000182912625009128/innovative_10q.htm | "ChatGPT" "referral" |
| Innovative Eyewear Inc  (LUCY, LUCYW)  (CIK 0001808377) | 10-K | 2026-03-25 | https://www.sec.gov/Archives/edgar/data/1808377/000182912626002695/innovativeeye_10k.htm | "AI assistants" "traffic"; "ChatGPT" "referral"; "ChatGPT" "traffic" |
| Innovative Eyewear Inc  (LUCY, LUCYW)  (CIK 0001808377) | 10-Q | 2026-05-14 | https://www.sec.gov/Archives/edgar/data/1808377/000182912626005226/innovative_10q.htm | "ChatGPT" "referral" |
| Innovative Eyewear Inc  (LUCY, LUCYW)  (CIK 0001808377) | S-1 | 2026-07-23 | https://www.sec.gov/Archives/edgar/data/1808377/000182912626007808/innovativeeye_s1.htm | "AI assistants" "traffic"; "ChatGPT" "traffic" |
| Innovative Eyewear Inc  (LUCY, LUCYW)  (CIK 0001808377) | 10-Q | 2026-08-14 | https://www.sec.gov/Archives/edgar/data/1808377/000182912626008847/innovative_10q.htm | "ChatGPT" "referral" |
| Innventure, Inc.  (INV, INVLW)  (CIK 0002001557) | 10-K | 2026-03-30 | https://www.sec.gov/Archives/edgar/data/2001557/000200155726000060/innv-20251231.htm | "ChatGPT" "bookings" |
| Intapp, Inc.  (INTA)  (CIK 0001565687) | 10-K | 2026-08-14 | https://www.sec.gov/Archives/edgar/data/1565687/000156568726000073/inta-20260630.htm | "AI assistants" "traffic" |
| Inter & Co, Inc.  (INTR)  (CIK 0001864163) | 6-K | 2025-09-04 | https://www.sec.gov/Archives/edgar/data/1864163/000186416325000008/interco-anual_reportx202.htm | "ChatGPT" "referral" |
| Inter & Co, Inc.  (INTR)  (CIK 0001864163) | 6-K | 2026-06-29 | https://www.sec.gov/Archives/edgar/data/1864163/000186416326000059/a2025annualreport-compac.htm | "LLM" "referral" |
| Inuvo, Inc.  (INUV)  (CIK 0000829323) | 10-K | 2025-02-27 | https://www.sec.gov/Archives/edgar/data/829323/000165495425002032/inuvo_10k.htm | "ChatGPT" "referral"; "ChatGPT" "traffic" |
| Inuvo, Inc.  (INUV)  (CIK 0000829323) | 10-K | 2026-03-05 | https://www.sec.gov/Archives/edgar/data/829323/000165495426001943/inuvo_10k.htm | "LLM" "referral" |
| Inuvo, Inc.  (INUV)  (CIK 0000829323) | 10-Q | 2026-05-14 | https://www.sec.gov/Archives/edgar/data/829323/000165495426004909/inuvo_10q.htm | "LLM" "referral" |
| Inuvo, Inc.  (INUV)  (CIK 0000829323) | 8-K | 2026-08-11 | https://www.sec.gov/Archives/edgar/data/829323/000165495426007482/inuvo_ex992.htm | "ChatGPT" "traffic" |
| Inuvo, Inc.  (INUV)  (CIK 0000829323) | 10-Q | 2026-08-11 | https://www.sec.gov/Archives/edgar/data/829323/000165495426007480/inuvo_10q.htm | "LLM" "referral" |
| JOINT Corp  (JYNT)  (CIK 0001612630) | 8-K | 2026-05-07 | https://www.sec.gov/Archives/edgar/data/1612630/000161263026000048/jyntq12026resultsdeck-fi.htm | "AI visibility" |
| JOINT Corp  (JYNT)  (CIK 0001612630) | 8-K | 2026-08-06 | https://www.sec.gov/Archives/edgar/data/1612630/000161263026000063/a8-05x26q22026resultsdec.htm | "AI visibility" |
| JUNIPER NETWORKS INC  (JNPR)  (CIK 0001043604) | 10-K | 2025-02-21 | https://www.sec.gov/Archives/edgar/data/1043604/000104360425000025/jnpr-20241231.htm | "ChatGPT" "traffic" |
| JX Luxventure Group Inc.  (JXG)  (CIK 0001546383) | 20-F | 2025-05-15 | https://www.sec.gov/Archives/edgar/data/1546383/000121390025043744/ea0239227-20f_jxluxven.htm | "ChatGPT" "traffic" |
| JX Luxventure Group Inc.  (JXG)  (CIK 0001546383) | 20-F | 2026-05-15 | https://www.sec.gov/Archives/edgar/data/1546383/000121390026057231/ea0289610-20f_jxluxven.htm | "ChatGPT" "traffic" |
| Jet.AI Inc.  (JTAI)  (CIK 0001861622) | 10-K | 2025-03-26 | https://www.sec.gov/Archives/edgar/data/1861622/000164117225000794/form10-k.htm | "ChatGPT" "bookings"; "ChatGPT" "traffic" |
| Jet.AI Inc.  (JTAI)  (CIK 0001861622) | S-1 | 2025-12-01 | https://www.sec.gov/Archives/edgar/data/1861622/000149315225025591/forms-1.htm | "ChatGPT" "bookings"; "ChatGPT" "traffic" |
| Jet.AI Inc.  (JTAI)  (CIK 0001861622) | 10-K | 2026-03-06 | https://www.sec.gov/Archives/edgar/data/1861622/000149315226009165/form10-k.htm | "ChatGPT" "bookings"; "ChatGPT" "traffic" |
| KALA BIO, Inc.  (KALA)  (CIK 0001479419) | 10-K | 2026-04-15 | https://www.sec.gov/Archives/edgar/data/1479419/000110465926043782/kala-20251231x10k.htm | "LLM" "referral"; "LLMs" "referral" |
| KE Holdings Inc.  (BEKE)  (CIK 0001809587) | 6-K | 2025-08-27 | https://www.sec.gov/Archives/edgar/data/1809587/000110465925083992/tm2524409d1_ex99-3.htm | "AI assistants" "traffic" |
| KE Holdings Inc.  (BEKE)  (CIK 0001809587) | 6-K | 2025-09-17 | https://www.sec.gov/Archives/edgar/data/1809587/000110465925090630/tm2526321d1_ex99-1.pdf | "AI assistants" "traffic" |
| Kanzhun Ltd  (BZ)  (CIK 0001842827) | 6-K | 2025-04-10 | https://www.sec.gov/Archives/edgar/data/1842827/000110465925033602/tm2512044d1_ex99-1.pdf | "AI assistants" "traffic"; "large language models" "organic traffic" |
| Kanzhun Ltd  (BZ)  (CIK 0001842827) | 6-K | 2025-08-20 | https://www.sec.gov/Archives/edgar/data/1842827/000110465925080902/tm2523955d3_ex99-1.htm | "large language models" "organic traffic" |
| Kanzhun Ltd  (BZ)  (CIK 0001842827) | 6-K | 2025-09-29 | https://www.sec.gov/Archives/edgar/data/1842827/000110465925094466/tm2527346d1_ex99-1.pdf | "large language models" "organic traffic" |
| Kanzhun Ltd  (BZ)  (CIK 0001842827) | 6-K | 2026-03-18 | https://www.sec.gov/Archives/edgar/data/1842827/000110465926030857/tm269240d1_ex99-2.htm | "large language models" "organic traffic" |
| Kanzhun Ltd  (BZ)  (CIK 0001842827) | 20-F | 2026-04-29 | https://www.sec.gov/Archives/edgar/data/1842827/000110465926050959/bz-20251231x20f.htm | "ChatGPT" "traffic"; "large language models" "organic traffic" |
| Kanzhun Ltd  (BZ)  (CIK 0001842827) | 6-K | 2026-04-29 | https://www.sec.gov/Archives/edgar/data/1842827/000110465926051472/tm2612917d1_ex99-1.pdf | "large language models" "organic traffic" |
| Kindly MD, Inc.  (KDLY, KDLYW)  (CIK 0001946573) | 10-K | 2025-03-28 | https://www.sec.gov/Archives/edgar/data/1946573/000164117225001314/form10-k.htm | "ChatGPT" "referral"; "ChatGPT" "traffic"; "LLMs" "referral" |
| Kindly MD, Inc.  (KDLY, KDLYW)  (CIK 0001946573) | 424B4 | 2025-05-07 | https://www.sec.gov/Archives/edgar/data/1946573/000164117225008901/form424b4.htm | "ChatGPT" "traffic" |
| Kingsoft Cloud Holdings Ltd  (KC, KCLHF)  (CIK 0001795589) | 20-F | 2025-04-15 | https://www.sec.gov/Archives/edgar/data/1795589/000141057825000732/kc-20241231x20f.htm | "AI assistants" "traffic"; "AI platforms" "referrals" |
| Kingsoft Cloud Holdings Ltd  (KC, KCLHF)  (CIK 0001795589) | 20-F | 2026-04-23 | https://www.sec.gov/Archives/edgar/data/1795589/000110465926047100/kc-20251231x20f.htm | "AI assistants" "traffic"; "AI platforms" "referrals" |
| Klarna Group plc  (KLAR)  (CIK 0002003292) | 6-K | 2026-07-01 | https://www.sec.gov/Archives/edgar/data/2003292/000162828026046370/exhibitno991pricerunnerl.htm | "ChatGPT" "traffic" |
| Klarna Group plc  (KLAR)  (CIK 0002003292) | 6-K | 2026-08-18 | https://www.sec.gov/Archives/edgar/data/2003292/000162828026057573/q22026earningsrelease.htm | "ChatGPT" "traffic"; "traffic from AI" |
| Klaviyo, Inc.  (KVYO)  (CIK 0001835830) | 10-K | 2026-02-10 | https://www.sec.gov/Archives/edgar/data/1835830/000183583026000007/kvyo-20251231.htm | "ChatGPT" "referral"; "LLMs" "referral" |
| Klook Technology Ltd  (CIK 0002071502) | F-1 | 2025-11-10 | https://www.sec.gov/Archives/edgar/data/2071502/000121390025108023/ea0248324-08.htm | "AI-powered search" "traffic"; "large language models" "organic traffic" |
| Knightscope, Inc.  (KSCP)  (CIK 0001600983) | 10-K | 2025-03-31 | https://www.sec.gov/Archives/edgar/data/1600983/000155837025004171/kscp-20241231x10k.htm | "AI-powered search" "traffic" |
| LEE ENTERPRISES, Inc  (LEE)  (CIK 0000058361) | 8-K | 2025-02-07 | https://www.sec.gov/Archives/edgar/data/58361/000162828025004403/leeq125earningspresentat.htm | "answer engine" |
| LEGALZOOM.COM, INC.  (LZ)  (CIK 0001286139) | 10-K | 2025-02-26 | https://www.sec.gov/Archives/edgar/data/1286139/000128613925000044/lz-20241231.htm | "large language models" "organic traffic" |
| LEGALZOOM.COM, INC.  (LZ)  (CIK 0001286139) | 10-K | 2026-02-23 | https://www.sec.gov/Archives/edgar/data/1286139/000128613926000012/lz-20251231.htm | "AI-powered search" "traffic"; "answer engines"; "large language models" "organic traffic" |
| LEGALZOOM.COM, INC.  (LZ)  (CIK 0001286139) | 10-Q | 2026-05-06 | https://www.sec.gov/Archives/edgar/data/1286139/000128613926000022/lz-20260331.htm | "AI platforms" "referrals"; "AI-powered search" "traffic"; "large language models" "organic traffic" |
| LEGALZOOM.COM, INC.  (LZ)  (CIK 0001286139) | 10-Q | 2026-08-05 | https://www.sec.gov/Archives/edgar/data/1286139/000128613926000031/lz-20260630.htm | "AI Overviews" "traffic"; "AI platforms" "referrals"; "large language models" "organic traffic" |
| LOGILITY SUPPLY CHAIN SOLUTIONS, INC  (LGTY)  (CIK 000071342 | 10-Q | 2025-02-28 | https://www.sec.gov/Archives/edgar/data/713425/000162828025008931/amswa-20250131.htm | "ChatGPT" "bookings" |
| LOGITECH INTERNATIONAL S.A.  (LOGI)  (CIK 0001032975) | 10-K | 2026-05-21 | https://www.sec.gov/Archives/edgar/data/1032975/000103297526000021/logi-20260331.htm | "AI platforms" "referrals" |
| LOGOOM TECHNOLOGIES, INC.  (CIK 0002124913) | S-1 | 2026-08-31 | https://www.sec.gov/Archives/edgar/data/2124913/000164033426001434/logoom_s1.htm | "LLM" "referral"; "LLMs" "referral" |
| LPL Financial Holdings Inc.  (LPLA)  (CIK 0001397911) | 8-K | 2025-03-31 | https://www.sec.gov/Archives/edgar/data/1397911/000119312525067661/d697025dex21.htm | "ChatGPT" "referral" |
| Lantern Pharma Inc.  (LTRN)  (CIK 0001763950) | 10-K | 2026-03-30 | https://www.sec.gov/Archives/edgar/data/1763950/000149315226013612/form10-k.htm | "AI platforms" "referrals"; "LLM" "referral" |
| LendingTree, Inc.  (TREE)  (CIK 0001434621) | 10-K | 2026-03-09 | https://www.sec.gov/Archives/edgar/data/1434621/000162828026016084/tree-20251231.htm | "AI Overviews" "traffic" |
| LendingTree, Inc.  (TREE)  (CIK 0001434621) | 8-K | 2026-07-29 | https://www.sec.gov/Archives/edgar/data/1434621/000162828026050633/tree-63026xer.htm | "ChatGPT" "traffic" |
| LexinFintech Holdings Ltd.  (LX)  (CIK 0001708259) | 20-F | 2026-04-29 | https://www.sec.gov/Archives/edgar/data/1708259/000119312526189256/lx-20251231.htm | "large language models" "organic traffic" |
| Liberty TripAdvisor Holdings, Inc.  (LTRPA, LTRPB)  (CIK 000 | 10-K | 2025-02-20 | https://www.sec.gov/Archives/edgar/data/1606745/000155837025001181/ltrpa-20241231x10k.htm | "AI platforms" "referrals"; "ChatGPT" "bookings"; "ChatGPT" "traffic" |
| Life360, Inc.  (LIF, LIFX)  (CIK 0001581760) | 8-K | 2026-03-02 | https://www.sec.gov/Archives/edgar/data/1581760/000158176026000017/a360q425resultspresentat.htm | "ChatGPT" "referral"; "LLMs" "referral" |
| Life360, Inc.  (LIF, LIFX)  (CIK 0001581760) | 8-K | 2026-05-11 | https://www.sec.gov/Archives/edgar/data/1581760/000158176026000079/a993-360q126resultsprese.htm | "ChatGPT" "referral"; "LLMs" "referral" |
| Life360, Inc.  (LIF, LIFX)  (CIK 0001581760) | 8-K | 2026-08-10 | https://www.sec.gov/Archives/edgar/data/1581760/000158176026000142/a360q226resultspresentat.htm | "ChatGPT" "referral"; "LLMs" "referral" |
| Lifeward Ltd.  (LFWD)  (CIK 0001607962) | S-1 | 2025-02-11 | https://www.sec.gov/Archives/edgar/data/1607962/000117891325000411/zk2532632.htm | "LLM" "referral" |
| Lifeward Ltd.  (LFWD)  (CIK 0001607962) | S-1/A | 2025-02-14 | https://www.sec.gov/Archives/edgar/data/1607962/000117891325000495/zk2532731.htm | "LLM" "referral" |
| Lifeward Ltd.  (LFWD)  (CIK 0001607962) | 10-K | 2025-03-07 | https://www.sec.gov/Archives/edgar/data/1607962/000117891325000736/zk2532799.htm | "LLM" "referral" |
| Liminatus Pharma, Inc.  (LIMN, LIMNW)  (CIK 0001971387) | S-1 | 2025-06-24 | https://www.sec.gov/Archives/edgar/data/1971387/000141057825001432/limn-20250331xs1.htm | "LLM" "referral" |
| Liminatus Pharma, Inc.  (LIMN, LIMNW)  (CIK 0001971387) | S-1/A | 2025-07-28 | https://www.sec.gov/Archives/edgar/data/1971387/000141057825001518/limn-20250331xs1a.htm | "LLM" "referral" |
| Liminatus Pharma, Inc.  (LIMN, LIMNW)  (CIK 0001971387) | S-1 | 2026-02-11 | https://www.sec.gov/Archives/edgar/data/1971387/000110465926012942/limn-20250930xs1.htm | "LLM" "referral" |
| Liminatus Pharma, Inc.  (LIMN, LIMNW)  (CIK 0001971387) | 424B4 | 2026-02-18 | https://www.sec.gov/Archives/edgar/data/1971387/000110465926016706/limn-20250930x424b4.htm | "LLM" "referral" |
| Liminatus Pharma, Inc.  (LIMN, LIMNW)  (CIK 0001971387) | S-1 | 2026-06-24 | https://www.sec.gov/Archives/edgar/data/1971387/000110465926076958/limn-20260331xs1.htm | "LLM" "referral" |
| Linkhome Holdings Inc.  (LHAI)  (CIK 0002017758) | 424B4 | 2025-07-25 | https://www.sec.gov/Archives/edgar/data/2017758/000121390025067578/ea0203553-24.htm | "large language models" "organic traffic" |
| Linkhome Holdings Inc.  (LHAI)  (CIK 0002017758) | 10-K | 2026-03-26 | https://www.sec.gov/Archives/edgar/data/2017758/000121390026034538/ea0281818-10k_linkhome.htm | "large language models" "organic traffic" |
| Linkhome Holdings Inc.  (LHAI)  (CIK 0002017758) | 10-K/A | 2026-05-19 | https://www.sec.gov/Archives/edgar/data/2017758/000121390026059081/ea0291456-10ka1_linkhome.htm | "large language models" "organic traffic" |
| LiveRamp Holdings, Inc.  (RAMP)  (CIK 0000733269) | 10-K | 2026-05-21 | https://www.sec.gov/Archives/edgar/data/733269/000073326926000025/ramp-20260331.htm | "AI assistants" "traffic" |
| Locafy Ltd  (LCFY, LCFYW)  (CIK 0001875547) | 6-K | 2025-08-29 | https://www.sec.gov/Archives/edgar/data/1875547/000164117225026051/ex99-1.htm | "AI search engines" "increase" |
| Locafy Ltd  (LCFY, LCFYW)  (CIK 0001875547) | 6-K | 2025-09-25 | https://www.sec.gov/Archives/edgar/data/1875547/000149315225014870/ex99-1.htm | "AI search engines" "increase" |
| Locafy Ltd  (LCFY, LCFYW)  (CIK 0001875547) | 20-F | 2025-11-12 | https://www.sec.gov/Archives/edgar/data/1875547/000149315225021910/form20-f.htm | "AI search" "conversion"; "AI search" "traffic"; "generative AI" "referral traffic" |
| Locafy Ltd  (LCFY, LCFYW)  (CIK 0001875547) | 6-K | 2025-11-12 | https://www.sec.gov/Archives/edgar/data/1875547/000149315225021918/ex99-1.htm | "AI search engines" "increase"; "AI search" "traffic"; "ChatGPT" "traffic"; "Perplexity" "traffic" |
| Locafy Ltd  (LCFY, LCFYW)  (CIK 0001875547) | 6-K | 2025-12-17 | https://www.sec.gov/Archives/edgar/data/1875547/000149315225028061/ex99-1.htm | "AI search engines" "increase" |
| Locafy Ltd  (LCFY, LCFYW)  (CIK 0001875547) | 6-K | 2026-07-01 | https://www.sec.gov/Archives/edgar/data/1875547/000149315226031582/ex99-1.htm | "AI search engines" "increase"; "answer engine" |
| Lomond Therapeutics Holdings, Inc.  (CIK 0001900520) | S-1/A | 2025-01-31 | https://www.sec.gov/Archives/edgar/data/1900520/000121390025008902/ea0228910-s1a1_lomond.htm | "LLMs" "referral" |
| Lomond Therapeutics Holdings, Inc.  (CIK 0001900520) | S-1/A | 2025-03-10 | https://www.sec.gov/Archives/edgar/data/1900520/000121390025022311/ea0233207-s1a2_lomond.htm | "LLM" "referral"; "LLMs" "referral" |
| Lomond Therapeutics Holdings, Inc.  (CIK 0001900520) | 10-K | 2025-04-15 | https://www.sec.gov/Archives/edgar/data/1900520/000121390025032200/ea0234915-10k_lomond.htm | "LLM" "referral"; "LLMs" "referral" |
| Lomond Therapeutics Holdings, Inc.  (CIK 0001900520) | S-1/A | 2025-06-18 | https://www.sec.gov/Archives/edgar/data/1900520/000121390025055292/ea0245215-s1a3_lomond.htm | "LLM" "referral"; "LLMs" "referral" |
| Lomond Therapeutics Holdings, Inc.  (CIK 0001900520) | S-1/A | 2025-08-01 | https://www.sec.gov/Archives/edgar/data/1900520/000121390025070684/ea0250378-s1a4_lomond.htm | "LLM" "referral"; "LLMs" "referral" |
| Lomond Therapeutics Holdings, Inc.  (CIK 0001900520) | 10-K | 2026-04-15 | https://www.sec.gov/Archives/edgar/data/1900520/000121390026044136/ea0283646-10k_lomond.htm | "LLM" "referral"; "LLMs" "referral" |
| Lulu's Fashion Lounge Holdings, Inc.  (LVLU)  (CIK 000178020 | 10-K | 2026-03-30 | https://www.sec.gov/Archives/edgar/data/1780201/000110465926036884/lvlu-20251228x10k.htm | "AI Mode" "traffic"; "ChatGPT" "new members"; "ChatGPT" "traffic"; "answer engines"; "large language models" "organic traffic" |
| Lunai Bioworks Inc.  (RENB)  (CIK 0001527728) | 10-K | 2025-09-29 | https://www.sec.gov/Archives/edgar/data/1527728/000173112225001316/e6882_10-k.htm | "LLMs" "referral" |
| Lytus Technologies Holdings PTV. Ltd.  (LYTHF)  (CIK 0001816 | 20-F | 2025-08-14 | https://www.sec.gov/Archives/edgar/data/1816319/000121390025076810/ea0246081-20f_lytustech.htm | "LLM" "referral" |
| Lytus Technologies Holdings PTV. Ltd.  (LYTHF)  (CIK 0001816 | F-1 | 2025-09-16 | https://www.sec.gov/Archives/edgar/data/1816319/000121390025088188/ea0256941-f1_lytus.htm | "LLM" "referral" |
| Lytus Technologies Holdings PTV. Ltd.  (LYTHF)  (CIK 0001816 | F-1/A | 2025-12-10 | https://www.sec.gov/Archives/edgar/data/1816319/000121390025119900/ea0268870-f1a1_lytus.htm | "LLM" "referral" |
| Lytus Technologies Holdings PTV. Ltd.  (LYTHF)  (CIK 0001816 | F-1/A | 2025-12-30 | https://www.sec.gov/Archives/edgar/data/1816319/000121390025126690/ea0271219-f1a2_lytus.htm | "LLM" "referral" |
| Lytus Technologies Holdings PTV. Ltd.  (LYTHF)  (CIK 0001816 | F-1/A | 2026-01-30 | https://www.sec.gov/Archives/edgar/data/1816319/000121390026010368/ea0274555-f1a3_lytus.htm | "LLM" "referral" |
| MAGNITE, INC.  (MGNI)  (CIK 0001595974) | 10-K | 2026-02-25 | https://www.sec.gov/Archives/edgar/data/1595974/000159597426000007/mgni-20251231.htm | "generative AI" "referral traffic" |
| MAGNITE, INC.  (MGNI)  (CIK 0001595974) | 10-Q | 2026-08-05 | https://www.sec.gov/Archives/edgar/data/1595974/000162828026053343/mgni-20260630.htm | "generative AI" "referral traffic" |
| MDxHealth SA  (MDXH)  (CIK 0001872529) | 20-F | 2025-03-31 | https://www.sec.gov/Archives/edgar/data/1872529/000121390025026226/ea0235301-20f_mdxhealth.htm | "LLM" "referral" |
| MDxHealth SA  (MDXH)  (CIK 0001872529) | 20-F | 2026-04-03 | https://www.sec.gov/Archives/edgar/data/1872529/000121390026039540/ea0283903-20f_mdxhealth.htm | "LLM" "referral" |
| MEDIAON GROUP INC.  (CIK 0002059702) | F-1 | 2025-12-03 | https://www.sec.gov/Archives/edgar/data/2059702/000149315225025925/formf-1.htm | "ChatGPT" "traffic" |
| MEDIAON GROUP INC.  (CIK 0002059702) | F-1/A | 2025-12-04 | https://www.sec.gov/Archives/edgar/data/2059702/000149315225026027/formf-1a.htm | "ChatGPT" "traffic" |
| MEDIAON GROUP INC.  (CIK 0002059702) | F-1/A | 2026-05-13 | https://www.sec.gov/Archives/edgar/data/2059702/000149315226022550/formf-1a.htm | "ChatGPT" "traffic" |
| MEDICAL EXERCISE INC.  (CIK 0002001249) | 10-K | 2026-06-29 | https://www.sec.gov/Archives/edgar/data/2001249/000121390026073032/ea0295808-10k_medical.htm | "LLM" "referral"; "LLMs" "referral" |
| MERCADOLIBRE INC  (MELI)  (CIK 0001099590) | 8-K | 2025-08-04 | https://www.sec.gov/Archives/edgar/data/1099590/000109959025000041/meli-20250804xex991.htm | "AI-powered search" "traffic" |
| MERCADOLIBRE INC  (MELI)  (CIK 0001099590) | 8-K | 2026-05-07 | https://www.sec.gov/Archives/edgar/data/1099590/000109959026000014/meli-20260507xex991.htm | "AI-powered search" "traffic" |
| MESOBLAST LTD  (MESO, MEOBF)  (CIK 0001345099) | 20-F | 2025-08-29 | https://www.sec.gov/Archives/edgar/data/1345099/000134509925000067/meso-20250630.htm | "LLM" "referral" |
| MESOBLAST LTD  (MESO, MEOBF)  (CIK 0001345099) | 6-K | 2025-10-28 | https://www.sec.gov/Archives/edgar/data/1345099/000134509925000090/exhibit991annualreportno.htm | "LLM" "referral" |
| MESOBLAST LTD  (MESO, MEOBF)  (CIK 0001345099) | 20-F | 2026-08-27 | https://www.sec.gov/Archives/edgar/data/1345099/000134509926000081/meso-20260630.htm | "AI platforms" "referrals"; "LLM" "referral" |
| MICROCHIP TECHNOLOGY INC  (MCHP)  (CIK 0000827054) | 10-Q | 2025-02-06 | https://www.sec.gov/Archives/edgar/data/827054/000082705425000019/mchp-20241231.htm | "ChatGPT" "traffic" |
| MICROCHIP TECHNOLOGY INC  (MCHP, MCHPP)  (CIK 0000827054) | 10-K | 2025-05-23 | https://www.sec.gov/Archives/edgar/data/827054/000082705425000077/mchp-20250331.htm | "ChatGPT" "traffic" |
| MICROCHIP TECHNOLOGY INC  (MCHP, MCHPP)  (CIK 0000827054) | 10-Q | 2025-08-07 | https://www.sec.gov/Archives/edgar/data/827054/000082705425000133/mchp-20250630.htm | "ChatGPT" "traffic" |
| MICROCHIP TECHNOLOGY INC  (MCHP, MCHPP)  (CIK 0000827054) | 10-Q | 2025-11-06 | https://www.sec.gov/Archives/edgar/data/827054/000082705425000183/mchp-20250930.htm | "ChatGPT" "traffic" |
| MICROCHIP TECHNOLOGY INC  (MCHP, MCHPP)  (CIK 0000827054) | 10-Q | 2026-02-05 | https://www.sec.gov/Archives/edgar/data/827054/000082705426000009/mchp-20251231.htm | "ChatGPT" "traffic" |
| MICROCHIP TECHNOLOGY INC  (MCHP, MCHPP)  (CIK 0000827054) | 10-K | 2026-05-21 | https://www.sec.gov/Archives/edgar/data/827054/000082705426000016/mchp-20260331.htm | "ChatGPT" "traffic" |
| MICROCHIP TECHNOLOGY INC  (MCHP, MCHPP)  (CIK 0000827054) | 10-Q | 2026-08-06 | https://www.sec.gov/Archives/edgar/data/827054/000082705426000038/mchp-20260630.htm | "ChatGPT" "traffic" |
| MITSUBISHI UFJ FINANCIAL GROUP INC  (MUFG, MBFJF)  (CIK 0000 | 6-K | 2025-08-26 | https://www.sec.gov/Archives/edgar/data/67088/000119312525188053/d902769dex991.pdf | "ChatGPT" "referral" |
| MakeMyTrip Ltd  (MMYT)  (CIK 0001495153) | 20-F | 2026-07-27 | https://www.sec.gov/Archives/edgar/data/1495153/000119312526318134/mmyt-20260331.htm | "AI search" "conversion"; "AI search" "traffic" |
| MediaAlpha, Inc.  (MAX)  (CIK 0001818383) | 10-K | 2026-02-23 | https://www.sec.gov/Archives/edgar/data/1818383/000181838326000049/max-20251231.htm | "AI platforms" "referrals"; "LLM" "referral" |
| Medtronic plc  (MDT)  (CIK 0001613103) | 10-K | 2025-06-20 | https://www.sec.gov/Archives/edgar/data/1613103/000161310325000091/mdt-20250425.htm | "AI platforms" "referrals" |
| Medtronic plc  (MDT)  (CIK 0001613103) | 10-K | 2026-06-18 | https://www.sec.gov/Archives/edgar/data/1613103/000162828026044354/mdt-20260424.htm | "AI platforms" "referrals" |
| Meey Global Corp  (CIK 0002134106) | F-1 | 2026-09-11 | https://www.sec.gov/Archives/edgar/data/2134106/000121390026099370/ea0291005-02.htm | "LLMs" "referral" |
| Merck & Co., Inc.  (MRK)  (CIK 0000310158) | 10-K | 2026-02-24 | https://www.sec.gov/Archives/edgar/data/310158/000031015826000063/mrk-20251231.htm | "AI platforms" "referrals" |
| MindWalk Holdings Corp.  (HYFT)  (CIK 0001715925) | 20-F | 2026-07-23 | https://www.sec.gov/Archives/edgar/data/1715925/000119312526312694/hyft-20260430.htm | "AI platforms" "referrals" |
| MiniMed Group, Inc.  (CIK 0002062583) | S-1 | 2025-12-19 | https://www.sec.gov/Archives/edgar/data/2062583/000162828025058231/minimedgroupincs-1.htm | "AI platforms" "referrals" |
| MiniMed Group, Inc.  (MMED)  (CIK 0002062583) | S-1/A | 2026-01-23 | https://www.sec.gov/Archives/edgar/data/2062583/000162828026003281/minimedgroupincs-1a1.htm | "AI platforms" "referrals" |
| MiniMed Group, Inc.  (MMED)  (CIK 0002062583) | S-1/A | 2026-02-24 | https://www.sec.gov/Archives/edgar/data/2062583/000162828026010862/minimedgroupincs-1a2.htm | "AI platforms" "referrals" |
| MiniMed Group, Inc.  (MMED)  (CIK 0002062583) | S-1/A | 2026-02-27 | https://www.sec.gov/Archives/edgar/data/2062583/000162828026012865/minimedgroupincs-1a3.htm | "AI platforms" "referrals" |
| MiniMed Group, Inc.  (MMED)  (CIK 0002062583) | 424B4 | 2026-03-06 | https://www.sec.gov/Archives/edgar/data/2062583/000162828026015648/minimedgroupinc424b4.htm | "AI platforms" "referrals" |
| MiniMed Group, Inc.  (MMED)  (CIK 0002062583) | 10-K | 2026-06-29 | https://www.sec.gov/Archives/edgar/data/2062583/000162828026045915/mdt-20260424.htm | "AI platforms" "referrals" |
| Mint Inc Ltd  (MIMI)  (CIK 0001998560) | 20-F | 2026-08-14 | https://www.sec.gov/Archives/edgar/data/1998560/000121390026090165/ea0300620-20f_mint.htm | "AI platforms" "referrals" |
| Mobile-health Network Solutions  (MNDR)  (CIK 0001976695) | F-1 | 2025-03-21 | https://www.sec.gov/Archives/edgar/data/1976695/000149315225011165/formf-1.htm | "AI search" "conversion"; "AI search" "traffic" |
| Mobile-health Network Solutions  (MNDR)  (CIK 0001976695) | F-1/A | 2025-03-28 | https://www.sec.gov/Archives/edgar/data/1976695/000164117225001031/formf-1a.htm | "AI search" "conversion"; "AI search" "traffic" |
| Mobile-health Network Solutions  (MNDR)  (CIK 0001976695) | 20-F | 2025-10-31 | https://www.sec.gov/Archives/edgar/data/1976695/000149315225020325/form20-f.htm | "AI search" "conversion"; "AI search" "traffic" |
| Mobile-health Network Solutions  (MNDR)  (CIK 0001976695) | F-1 | 2026-03-09 | https://www.sec.gov/Archives/edgar/data/1976695/000149315226009241/formf-1.htm | "AI search" "conversion"; "AI search" "traffic" |
| Mobile-health Network Solutions  (MNDR)  (CIK 0001976695) | F-1/A | 2026-04-17 | https://www.sec.gov/Archives/edgar/data/1976695/000149315226017149/formf-1a.htm | "AI search" "conversion"; "AI search" "traffic" |
| Moderna, Inc.  (MRNA)  (CIK 0001682852) | 10-K | 2025-02-21 | https://www.sec.gov/Archives/edgar/data/1682852/000168285225000022/mrna-20241231.htm | "ChatGPT" "referral" |
| Moderna, Inc.  (MRNA)  (CIK 0001682852) | 10-K | 2026-02-20 | https://www.sec.gov/Archives/edgar/data/1682852/000168285226000033/mrna-20251231.htm | "ChatGPT" "referral" |
| Morningstar, Inc.  (MORN)  (CIK 0001289419) | 8-K | 2025-11-25 | https://www.sec.gov/Archives/edgar/data/1289419/000128941925000174/a112525investorquestions.htm | "through ChatGPT" |
| Muzinich BDC, Inc.  (CIK 0001779523) | 10-K | 2026-03-27 | https://www.sec.gov/Archives/edgar/data/1779523/000121390026035730/ea0282653-10k_muzinich.htm | "ChatGPT" "referral" |
| Muzinich Corporate Lending Income Fund, Inc.  (CIK 000198537 | 10-K | 2026-03-27 | https://www.sec.gov/Archives/edgar/data/1985375/000121390026035737/ea0282651-10k_muzinich.htm | "ChatGPT" "referral"; "ChatGPT" "traffic" |
| N-able, Inc.  (NABL)  (CIK 0001834488) | 8-K | 2026-08-10 | https://www.sec.gov/Archives/edgar/data/1834488/000183448826000044/nabl-20260630x8kxex991.htm | "AI visibility" |
| NERDWALLET, INC.  (NRDS)  (CIK 0001625278) | 8-K | 2026-02-25 | https://www.sec.gov/Archives/edgar/data/1625278/000162527826000012/earningsreleaseq4fy25.htm | "AI Overviews" "traffic"; "LLMs" "referral" |
| NEURALBASE AI LTD.  (NBBI)  (CIK 0001130781) | S-1/A | 2025-02-12 | https://www.sec.gov/Archives/edgar/data/1130781/000147793225000901/vira_s1a.htm | "ChatGPT" "new members" |
| NEURALBASE AI LTD.  (NBBI)  (CIK 0001130781) | 424B4 | 2025-02-19 | https://www.sec.gov/Archives/edgar/data/1130781/000147793225001112/vira_424b4.htm | "ChatGPT" "new members" |
| NEURALBASE AI LTD.  (NBBI)  (CIK 0001130781) | 10-K | 2025-04-25 | https://www.sec.gov/Archives/edgar/data/1130781/000147793225002956/nbbi_10k.htm | "ChatGPT" "new members" |
| NEURALBASE AI LTD.  (NBBI, VIRAD)  (CIK 0001130781) | S-1 | 2025-01-31 | https://www.sec.gov/Archives/edgar/data/1130781/000147793225000605/vira_s1.htm | "ChatGPT" "new members" |
| NEW YORK TIMES CO  (NYT)  (CIK 0000071691) | 10-K | 2026-02-27 | https://www.sec.gov/Archives/edgar/data/71691/000007169126000011/nyt-20251231.htm | "AI platforms" "referrals"; "Perplexity" "traffic"; "generative AI" "referral traffic" |
| NEWS CORP  (NWS, NWSA)  (CIK 0001564708) | 8-K | 2025-02-05 | https://www.sec.gov/Archives/edgar/data/1564708/000156470825000069/release-q2fy2025.htm | "Perplexity" "traffic" |
| NEWS CORP  (NWS, NWSA, NWSAL)  (CIK 0001564708) | 10-K | 2025-08-06 | https://www.sec.gov/Archives/edgar/data/1564708/000156470825000419/nws-20250630.htm | "AI platforms" "referrals" |
| NEWS CORP  (NWS, NWSA, NWSLL)  (CIK 0001564708) | 8-K | 2026-03-16 | https://www.sec.gov/Archives/edgar/data/1564708/000156470826000057/dowjones2026investorbrie.htm | "AI-powered search" "traffic"; "ChatGPT" "referral"; "ChatGPT" "traffic"; "LLMs" "referral" |
| NEWS CORP  (NWS, NWSA, NWSLL)  (CIK 0001564708) | 10-K | 2026-08-07 | https://www.sec.gov/Archives/edgar/data/1564708/000156470826000175/nws-20260630.htm | "AI platforms" "referrals" |
| NSCALE Ltd  (CIK 0002110365) | S-1 | 2026-09-18 | https://www.sec.gov/Archives/edgar/data/2110365/000119312526395475/ck0002110365-20260918.htm | "ChatGPT" "traffic" |
| NatWest Group plc  (NWG, RBSPF)  (CIK 0000844150) | 6-K | 2026-02-13 | https://www.sec.gov/Archives/edgar/data/844150/000110465926014634/tm2531856d2_ex99-1.pdf | "AI search" "conversion" |
| NatWest Group plc  (NWG, RBSPF)  (CIK 0000844150) | 20-F | 2026-02-17 | https://www.sec.gov/Archives/edgar/data/844150/000110465926016245/nwg-20251231xex15d2.htm | "AI search" "conversion" |
| Natera, Inc.  (NTRA)  (CIK 0001604821) | 8-K | 2025-08-07 | https://www.sec.gov/Archives/edgar/data/1604821/000110465925075189/tm2522162d1_ex99-2.htm | "AI discovery" |
| Nebius Group N.V.  (NBIS)  (CIK 0001513845) | 6-K | 2025-08-07 | https://www.sec.gov/Archives/edgar/data/1513845/000110465925075028/tm2522866d1_ex99-2.htm | "LLM" "referral"; "LLMs" "referral" |
| Nebius Group N.V.  (NBIS)  (CIK 0001513845) | 6-K | 2025-11-12 | https://www.sec.gov/Archives/edgar/data/1513845/000110465925109806/tm2530882d1_ex99-2.htm | "LLM" "referral" |
| Nebius Group N.V.  (NBIS)  (CIK 0001513845) | 6-K | 2026-02-10 | https://www.sec.gov/Archives/edgar/data/1513845/000110465926012492/tm265786d1_ex99-1.htm | "agentic search" |
| Nebius Group N.V.  (NBIS)  (CIK 0001513845) | 6-K | 2026-02-12 | https://www.sec.gov/Archives/edgar/data/1513845/000110465926013946/tm266173d1_ex99-2.htm | "agentic search" |
| Nebius Group N.V.  (NBIS)  (CIK 0001513845) | 20-F | 2026-04-30 | https://www.sec.gov/Archives/edgar/data/1513845/000110465926052948/nbis-20251231x20f.htm | "AI discovery"; "agentic search" |
| Nebius Group N.V.  (NBIS)  (CIK 0001513845) | 20-F | 2026-04-30 | https://www.sec.gov/Archives/edgar/data/1513845/000110465926052948/nbis-20251231xex4d6.htm | "LLMs" "referral" |
| Nebius Group N.V.  (NBIS)  (CIK 0001513845) | 6-K | 2026-05-13 | https://www.sec.gov/Archives/edgar/data/1513845/000110465926059872/tm2614392d1_ex99-2.htm | "agentic search" |
| Neptune Insurance Holdings Inc.  (NP)  (CIK 0002067129) | S-1 | 2026-05-11 | https://www.sec.gov/Archives/edgar/data/2067129/000162828026033573/neptuneflood-sx1.htm | "ChatGPT" "referral" |
| Neptune Insurance Holdings Inc.  (NP)  (CIK 0002067129) | 424B4 | 2026-05-14 | https://www.sec.gov/Archives/edgar/data/2067129/000162828026035207/neptuneflood-424b4.htm | "ChatGPT" "referral" |
| Neptune Insurance Holdings Inc.  (NP)  (CIK 0002067129) | 10-Q | 2026-07-27 | https://www.sec.gov/Archives/edgar/data/2067129/000162828026049809/np-20260630.htm | "LLM" "referral" |
| Netcapital Inc.  (NCPL, NCPLW)  (CIK 0001414767) | S-1/A | 2026-02-02 | https://www.sec.gov/Archives/edgar/data/1414767/000149315226004742/forms-1a.htm | "LLM" "referral" |
| Netcapital Inc.  (NCPL, NCPLW)  (CIK 0001414767) | S-1/A | 2026-02-24 | https://www.sec.gov/Archives/edgar/data/1414767/000149315226007888/forms-1a.htm | "LLM" "referral" |
| Netcapital Inc.  (NCPL, NCPLW)  (CIK 0001414767) | S-1/A | 2026-03-24 | https://www.sec.gov/Archives/edgar/data/1414767/000149315226012402/forms-1a.htm | "LLM" "referral" |
| Netskope Inc  (CIK 0002063196) | S-1 | 2025-08-22 | https://www.sec.gov/Archives/edgar/data/2063196/000095017025110855/ck0002063196-20250822.htm | "ChatGPT" "bookings"; "ChatGPT" "referral"; "ChatGPT" "traffic"; "LLMs" "referral" |
| Netskope Inc  (NTSK)  (CIK 0002063196) | S-1/A | 2025-09-08 | https://www.sec.gov/Archives/edgar/data/2063196/000095017025113358/ck0002063196-20250908.htm | "ChatGPT" "bookings"; "ChatGPT" "referral"; "ChatGPT" "traffic"; "LLMs" "referral" |
| Netskope Inc  (NTSK)  (CIK 0002063196) | S-1/A | 2025-09-16 | https://www.sec.gov/Archives/edgar/data/2063196/000119312525204285/ck0002063196-20250916.htm | "ChatGPT" "bookings"; "ChatGPT" "referral"; "ChatGPT" "traffic"; "LLMs" "referral" |
| Netskope Inc  (NTSK)  (CIK 0002063196) | 424B4 | 2025-09-18 | https://www.sec.gov/Archives/edgar/data/2063196/000119312525207534/netskope_424b4_sept_2025.htm | "ChatGPT" "bookings"; "ChatGPT" "referral"; "ChatGPT" "traffic"; "LLMs" "referral" |
| Netskope Inc  (NTSK)  (CIK 0002063196) | 8-K | 2026-03-11 | https://www.sec.gov/Archives/edgar/data/2063196/000119312526102142/ck0002063196-ex99_1.htm | "AI visibility" |
| Netskope Inc  (NTSK)  (CIK 0002063196) | 10-K | 2026-03-31 | https://www.sec.gov/Archives/edgar/data/2063196/000119312526135011/ck0002063196-20260131.htm | "AI visibility"; "ChatGPT" "referral"; "ChatGPT" "traffic"; "LLMs" "referral"; "Perplexity" "traffic" |
| NeuroSense Therapeutics Ltd.  (NRSN, NRSNW)  (CIK 0001875091 | 20-F | 2025-04-07 | https://www.sec.gov/Archives/edgar/data/1875091/000121390025029464/ea0237295-20f_neuro.htm | "LLM" "referral" |
| NeuroSense Therapeutics Ltd.  (NRSN, NRSNW)  (CIK 0001875091 | 20-F | 2026-03-31 | https://www.sec.gov/Archives/edgar/data/1875091/000121390026036970/ea0283072-20f_neurosense.htm | "LLM" "referral" |
| New Mountain Finance Corp  (NMFC, NMFCZ)  (CIK 0001496099) | 10-K | 2025-02-26 | https://www.sec.gov/Archives/edgar/data/1496099/000149609925000010/nmfc-20241231.htm | "ChatGPT" "referral" |
| New Mountain Finance Corp  (NMFC, NMFCZ)  (CIK 0001496099) | 10-K | 2026-02-24 | https://www.sec.gov/Archives/edgar/data/1496099/000149609926000008/nmfc-20251231.htm | "ChatGPT" "referral" |
| New Mountain Net Lease Trust  (CIK 0002033695) | 10-K | 2025-03-28 | https://www.sec.gov/Archives/edgar/data/2033695/000141057825000532/tmb-20241231x10k.htm | "ChatGPT" "referral" |
| New Mountain Net Lease Trust  (CIK 0002033695) | 10-K | 2026-03-31 | https://www.sec.gov/Archives/edgar/data/2033695/000110465926037121/tmb-20251231x10k.htm | "ChatGPT" "referral" |
| Newegg Commerce, Inc.  (NEGG)  (CIK 0001474627) | 20-F | 2025-04-28 | https://www.sec.gov/Archives/edgar/data/1474627/000121390025036055/ea0238113-20f_newegg.htm | "ChatGPT" "referral"; "ChatGPT" "traffic" |
| Newegg Commerce, Inc.  (NEGG)  (CIK 0001474627) | 20-F | 2026-04-28 | https://www.sec.gov/Archives/edgar/data/1474627/000121390026048633/ea0286017-20f_newegg.htm | "ChatGPT" "referral"; "ChatGPT" "traffic" |
| Nextdoor Holdings, Inc.  (NXDR)  (CIK 0001846069) | 10-Q | 2026-08-04 | https://www.sec.gov/Archives/edgar/data/1846069/000184606926000155/nxdr-20260630.htm | "AI-powered search" "traffic" |
| Nurix Therapeutics, Inc.  (NRIX)  (CIK 0001549595) | 8-K | 2025-01-13 | https://www.sec.gov/Archives/edgar/data/1549595/000154959525000005/investorwebcastslidedeck.htm | "AI discovery" |
| Nurix Therapeutics, Inc.  (NRIX)  (CIK 0001549595) | 8-K | 2025-01-13 | https://www.sec.gov/Archives/edgar/data/1549595/000154959525000005/nrix20250113form8-kex991jpm.htm | "AI discovery" |
| Nurix Therapeutics, Inc.  (NRIX)  (CIK 0001549595) | 10-K | 2025-01-28 | https://www.sec.gov/Archives/edgar/data/1549595/000154959525000016/nrix-20241130.htm | "AI discovery" |
| Nurix Therapeutics, Inc.  (NRIX)  (CIK 0001549595) | 10-Q | 2025-04-08 | https://www.sec.gov/Archives/edgar/data/1549595/000154959525000055/nrix-20250228.htm | "AI discovery" |
| Nurix Therapeutics, Inc.  (NRIX)  (CIK 0001549595) | 10-Q | 2025-07-09 | https://www.sec.gov/Archives/edgar/data/1549595/000154959525000095/nrix-20250531.htm | "AI discovery" |
| Nurix Therapeutics, Inc.  (NRIX)  (CIK 0001549595) | 10-Q | 2025-10-09 | https://www.sec.gov/Archives/edgar/data/1549595/000154959525000113/nrix-20250831.htm | "AI discovery" |
| Nurix Therapeutics, Inc.  (NRIX)  (CIK 0001549595) | 10-K | 2026-01-28 | https://www.sec.gov/Archives/edgar/data/1549595/000154959526000016/nrix-20251130.htm | "AI discovery" |
| Nurix Therapeutics, Inc.  (NRIX)  (CIK 0001549595) | 8-K | 2026-06-08 | https://www.sec.gov/Archives/edgar/data/1549595/000154959526000030/ex991_nurixpressrelease202.htm | "AI discovery" |
| OFS Capital Corp  (OFS, OFSSH)  (CIK 0001487918) | 10-K | 2025-03-04 | https://www.sec.gov/Archives/edgar/data/1487918/000148791825000009/ofs-20241231.htm | "ChatGPT" "referral" |
| ON24 INC.  (ONTF)  (CIK 0001110611) | 10-K | 2026-03-12 | https://www.sec.gov/Archives/edgar/data/1110611/000162828026017337/ontf-20251231.htm | "AI-powered search" "traffic" |
| OOMA INC  (OOMA)  (CIK 0001327688) | 10-K | 2026-04-03 | https://www.sec.gov/Archives/edgar/data/1327688/000132768826000009/ooma-20260131.htm | "generative engine optimization" |
| ORANGEKLOUD TECHNOLOGY INC.  (ORKT)  (CIK 0001979407) | 20-F | 2025-05-02 | https://www.sec.gov/Archives/edgar/data/1979407/000164117225008322/form20-f.htm | "ChatGPT" "referral" |
| ORANGEKLOUD TECHNOLOGY INC.  (ORKT)  (CIK 0001979407) | 20-F | 2026-04-30 | https://www.sec.gov/Archives/edgar/data/1979407/000149315226019732/form20-f.htm | "AI platforms" "referrals" |
| Ondas Holdings Inc.  (ONDS)  (CIK 0001646188) | 8-K | 2025-11-25 | https://www.sec.gov/Archives/edgar/data/1646188/000121390025114433/ea026688601ex2-1_ondas.htm | "LLMs" "referral" |
| OneMeta Inc.  (ONEI)  (CIK 0001388295) | S-1/A | 2025-01-15 | https://www.sec.gov/Archives/edgar/data/1388295/000149315225002433/forms-1a.htm | "LLM" "referral" |
| OneMeta Inc.  (ONEI)  (CIK 0001388295) | 10-K | 2025-03-06 | https://www.sec.gov/Archives/edgar/data/1388295/000149315225009285/form10-k.htm | "LLM" "referral" |
| OneMeta Inc.  (ONEI)  (CIK 0001388295) | S-1/A | 2025-03-06 | https://www.sec.gov/Archives/edgar/data/1388295/000149315225009352/forms-1a.htm | "LLM" "referral"; "LLMs" "referral" |
| OneMeta Inc.  (ONEI)  (CIK 0001388295) | S-1/A | 2025-06-05 | https://www.sec.gov/Archives/edgar/data/1388295/000164117225013763/forms-1a.htm | "LLM" "referral"; "LLMs" "referral" |
| OneMeta Inc.  (ONEI)  (CIK 0001388295) | 10-K | 2026-04-15 | https://www.sec.gov/Archives/edgar/data/1388295/000149315226016782/form10-k.htm | "LLM" "referral" |
| OneMeta Inc.  (ONEI)  (CIK 0001388295) | 10-K/A | 2026-05-04 | https://www.sec.gov/Archives/edgar/data/1388295/000149315226020948/form10-ka.htm | "LLM" "referral" |
| Onex Direct Lending BDC Fund  (CIK 0001860424) | 10-K | 2025-03-07 | https://www.sec.gov/Archives/edgar/data/1860424/000095017025035197/ck0001860424-20241231.htm | "ChatGPT" "referral" |
| Onex Direct Lending BDC Fund  (CIK 0001860424) | 10-K | 2026-03-06 | https://www.sec.gov/Archives/edgar/data/1860424/000119312526095711/ck0001860424-20251231.htm | "ChatGPT" "referral" |
| Onfolio Holdings, Inc  (ONFO, ONFOP, ONFOW)  (CIK 0001825452 | S-1 | 2025-08-22 | https://www.sec.gov/Archives/edgar/data/1825452/000165495425009950/onfo_s1.htm | "AI Overviews" "traffic"; "AI visibility"; "ChatGPT" "referral"; "ChatGPT" "traffic"; "LLM" "referral"; "Perplexity" "traffic"; "answer engines"; "generative engine optimization"; "traffic from AI" |
| Onfolio Holdings, Inc  (ONFO, ONFOP, ONFOW)  (CIK 0001825452 | 424B4 | 2025-09-02 | https://www.sec.gov/Archives/edgar/data/1825452/000165495425010231/onfo_424b4.htm | "AI Overviews" "traffic"; "AI visibility"; "ChatGPT" "referral"; "ChatGPT" "traffic"; "LLM" "referral"; "Perplexity" "traffic"; "answer engines"; "generative engine optimization"; "traffic from AI" |
| Onfolio Holdings, Inc  (ONFO, ONFOP, ONFOW)  (CIK 0001825452 | S-1 | 2025-12-18 | https://www.sec.gov/Archives/edgar/data/1825452/000165495425014068/onfo_s1.htm | "AI Overviews" "traffic"; "ChatGPT" "referral"; "ChatGPT" "traffic"; "Perplexity" "traffic"; "answer engines"; "generative engine optimization"; "traffic from AI" |
| Onfolio Holdings, Inc  (ONFO, ONFOP, ONFOW)  (CIK 0001825452 | S-1/A | 2026-01-28 | https://www.sec.gov/Archives/edgar/data/1825452/000165495426000655/onfo_s1a.htm | "AI Overviews" "traffic"; "ChatGPT" "referral"; "ChatGPT" "traffic"; "Perplexity" "traffic"; "answer engines"; "generative engine optimization"; "traffic from AI" |
| Onfolio Holdings, Inc  (ONFO, ONFOP, ONFOW)  (CIK 0001825452 | 10-K | 2026-03-31 | https://www.sec.gov/Archives/edgar/data/1825452/000165495426003083/onfo_10k.htm | "AI Overviews" "traffic"; "AI search" "conversion"; "AI search" "traffic"; "AI visibility"; "AI-powered search" "traffic"; "ChatGPT" "referral"; "ChatGPT" "traffic"; "Perplexity" "traffic"; "generative AI" "referral traffic"; "generative engine optimization" |
| Onfolio Holdings, Inc  (ONFO, ONFOP, ONFOW)  (CIK 0001825452 | S-1/A | 2026-04-09 | https://www.sec.gov/Archives/edgar/data/1825452/000165495426003380/onfo_s1a.htm | "AI Overviews" "traffic"; "AI search" "conversion"; "AI search" "traffic"; "AI visibility"; "ChatGPT" "referral"; "ChatGPT" "traffic"; "Perplexity" "traffic"; "generative engine optimization" |
| Opera Ltd  (OPRA)  (CIK 0001737450) | 20-F | 2025-04-10 | https://www.sec.gov/Archives/edgar/data/1737450/000095017025052668/opra-20241231.htm | "ChatGPT" "traffic" |
| Opera Ltd  (OPRA)  (CIK 0001737450) | 20-F | 2026-03-27 | https://www.sec.gov/Archives/edgar/data/1737450/000173745026000005/opra-20251231.htm | "AI assistants" "traffic"; "AI platforms" "referrals"; "LLM" "referral"; "LLMs" "referral" |
| Optimal AI Ltd  (CIK 0002083345) | F-1 | 2025-12-30 | https://www.sec.gov/Archives/edgar/data/2083345/000121390025126476/ea0271093-f1_optimal.htm | "AI platforms" "referrals" |
| Optimal AI Ltd  (CIK 0002083345) | F-1/A | 2026-01-26 | https://www.sec.gov/Archives/edgar/data/2083345/000121390026007642/ea0273888-f1a1_optimal.htm | "AI platforms" "referrals" |
| Optimal AI Ltd  (CIK 0002083345) | F-1/A | 2026-03-06 | https://www.sec.gov/Archives/edgar/data/2083345/000121390026024460/ea0277218-f1a2_optimal.htm | "AI platforms" "referrals" |
| Oric Pharmaceuticals, Inc.  (ORIC)  (CIK 0001796280) | 10-Q | 2025-08-12 | https://www.sec.gov/Archives/edgar/data/1796280/000095017025107359/oric-20250630.htm | "AI platforms" "referrals" |
| Oric Pharmaceuticals, Inc.  (ORIC)  (CIK 0001796280) | 10-Q | 2025-11-13 | https://www.sec.gov/Archives/edgar/data/1796280/000119312525280234/oric-20250930.htm | "AI platforms" "referrals" |
| Oric Pharmaceuticals, Inc.  (ORIC)  (CIK 0001796280) | 10-K | 2026-02-23 | https://www.sec.gov/Archives/edgar/data/1796280/000119312526064005/oric-20251231.htm | "AI platforms" "referrals" |
| Oric Pharmaceuticals, Inc.  (ORIC)  (CIK 0001796280) | 10-Q | 2026-05-04 | https://www.sec.gov/Archives/edgar/data/1796280/000119312526204047/oric-20260331.htm | "AI platforms" "referrals" |
| Oric Pharmaceuticals, Inc.  (ORIC)  (CIK 0001796280) | 10-Q | 2026-08-03 | https://www.sec.gov/Archives/edgar/data/1796280/000119312526330631/oric-20260630.htm | "AI platforms" "referrals" |
| Our Bond, Inc.  (OBAI)  (CIK 0001756064) | 10-K | 2026-03-31 | https://www.sec.gov/Archives/edgar/data/1756064/000149315226014133/form10-k.htm | "ChatGPT" "bookings"; "ChatGPT" "traffic" |
| Our Bond, Inc.  (OBAI)  (CIK 0001756064) | S-1 | 2026-04-02 | https://www.sec.gov/Archives/edgar/data/1756064/000149315226014927/forms-1.htm | "ChatGPT" "bookings"; "ChatGPT" "traffic" |
| Our Bond, Inc.  (OBAI)  (CIK 0001756064) | 10-Q | 2026-05-15 | https://www.sec.gov/Archives/edgar/data/1756064/000149315226023347/form10-q.htm | "ChatGPT" "bookings" |
| Our Bond, Inc.  (OBAI)  (CIK 0001756064) | S-1 | 2026-07-17 | https://www.sec.gov/Archives/edgar/data/1756064/000149315226033754/forms-1.htm | "ChatGPT" "bookings"; "ChatGPT" "traffic" |
| Our Bond, Inc.  (OBAI)  (CIK 0001756064) | 10-Q | 2026-08-14 | https://www.sec.gov/Archives/edgar/data/1756064/000149315226037989/form10-q.htm | "ChatGPT" "bookings" |
| Oura Inc.  (CIK 0002133022) | S-1 | 2026-09-03 | https://www.sec.gov/Archives/edgar/data/2133022/000119312526381855/d119865ds1.htm | "LLM" "referral"; "LLMs" "referral" |
| Oura Inc.  (OURA)  (CIK 0002133022) | S-1/A | 2026-09-21 | https://www.sec.gov/Archives/edgar/data/2133022/000119312526396051/d119865ds1a.htm | "LLM" "referral"; "LLMs" "referral" |
| Overland Advantage  (CIK 0001965934) | 10-K | 2025-03-26 | https://www.sec.gov/Archives/edgar/data/1965934/000095017025045206/ck0001965934-20241231.htm | "ChatGPT" "referral" |
| Owlet, Inc.  (OWLT, OWLTW)  (CIK 0001816708) | 10-K | 2026-03-09 | https://www.sec.gov/Archives/edgar/data/1816708/000181670826000018/owlt-20251231.htm | "LLMs" "referral"; "large language models" "organic traffic" |
| PINTEREST, INC.  (PINS)  (CIK 0001506293) | 10-K | 2026-02-12 | https://www.sec.gov/Archives/edgar/data/1506293/000150629326000021/pins-20251231.htm | "ChatGPT" "traffic" |
| PINTEREST, INC.  (PINS)  (CIK 0001506293) | 10-Q | 2026-05-04 | https://www.sec.gov/Archives/edgar/data/1506293/000150629326000068/pins-20260331.htm | "ChatGPT" "traffic" |
| PINTEREST, INC.  (PINS)  (CIK 0001506293) | 10-Q | 2026-08-04 | https://www.sec.gov/Archives/edgar/data/1506293/000150629326000104/pins-20260630.htm | "ChatGPT" "traffic" |
| PROGRESS SOFTWARE CORP /MA  (PRGS)  (CIK 0000876167) | 8-K | 2026-07-22 | https://www.sec.gov/Archives/edgar/data/876167/000155278126000390/e26303_ex2-1.htm | "ChatGPT" "referral"; "ChatGPT" "traffic" |
| PVH CORP. /DE/  (PVH)  (CIK 0000078239) | 10-K | 2026-03-31 | https://www.sec.gov/Archives/edgar/data/78239/000007823926000021/pvh-20260201.htm | "ChatGPT" "traffic" |
| Palladyne AI Corp.  (PDYN, PDYNW)  (CIK 0001826681) | 10-K | 2025-02-20 | https://www.sec.gov/Archives/edgar/data/1826681/000095017025024148/pdyn-20241231.htm | "LLM" "referral"; "LLMs" "referral" |
| Palladyne AI Corp.  (PDYN, PDYNW)  (CIK 0001826681) | 10-K | 2026-03-05 | https://www.sec.gov/Archives/edgar/data/1826681/000119312526092443/pdyn-20251231.htm | "LLM" "referral"; "LLMs" "referral" |
| Palo Alto Networks Inc  (PANW)  (CIK 0001327567) | 10-K | 2026-09-10 | https://www.sec.gov/Archives/edgar/data/1327567/000132756726000023/panw-20260731.htm | "AI platforms" "referrals" |
| Pattern Group Inc.  (CIK 0001811935) | S-1 | 2025-08-22 | https://www.sec.gov/Archives/edgar/data/1811935/000162828025041036/pattern-sx1.htm | "LLMs" "referral" |
| Pattern Group Inc.  (PTRN)  (CIK 0001811935) | S-1/A | 2025-09-10 | https://www.sec.gov/Archives/edgar/data/1811935/000181193525000009/pattern-sx1a1.htm | "LLMs" "referral" |
| Pattern Group Inc.  (PTRN)  (CIK 0001811935) | S-1/A | 2025-09-17 | https://www.sec.gov/Archives/edgar/data/1811935/000181193525000025/pattern-sx1a3.htm | "LLMs" "referral" |
| Pattern Group Inc.  (PTRN)  (CIK 0001811935) | S-1/A | 2025-09-18 | https://www.sec.gov/Archives/edgar/data/1811935/000181193525000038/pattern-sx1a4.htm | "LLMs" "referral" |
| Pattern Group Inc.  (PTRN)  (CIK 0001811935) | 424B4 | 2025-09-19 | https://www.sec.gov/Archives/edgar/data/1811935/000162828025042213/pattern-424b4.htm | "LLMs" "referral" |
| Pattern Group Inc.  (PTRN)  (CIK 0001811935) | 10-K | 2026-03-06 | https://www.sec.gov/Archives/edgar/data/1811935/000181193526000013/ptrn-20251231.htm | "LLMs" "referral" |
| PayPay Corp  (CIK 0002080845) | F-1 | 2026-02-12 | https://www.sec.gov/Archives/edgar/data/2080845/000119312526047933/d941409df1.htm | "AI platforms" "referrals" |
| PayPay Corp  (CIK 0002080845) | F-1/A | 2026-03-02 | https://www.sec.gov/Archives/edgar/data/2080845/000119312526085389/d941409df1a.htm | "AI platforms" "referrals" |
| PayPay Corp  (CIK 0002080845) | 424B4 | 2026-03-12 | https://www.sec.gov/Archives/edgar/data/2080845/000208084526000001/d941409d424b4.htm | "AI platforms" "referrals" |
| PayPay Corp  (PAYP)  (CIK 0002080845) | 20-F | 2026-06-30 | https://www.sec.gov/Archives/edgar/data/2080845/000119312526289382/payp-20260331.htm | "AI platforms" "referrals" |
| People Inc  (PPLI)  (CIK 0001800227) | 8-K | 2026-08-03 | https://www.sec.gov/Archives/edgar/data/1800227/000162828026051836/ex_991q22026ppli-pressrele.htm | "AI Overviews" "traffic" |
| People Inc  (PPLI)  (CIK 0001800227) | 10-Q | 2026-08-03 | https://www.sec.gov/Archives/edgar/data/1800227/000162828026051881/ppli-20260630.htm | "AI Overviews" "traffic" |
| People Inc  (PPLI)  (CIK 0001800227) | 8-K | 2026-09-11 | https://www.sec.gov/Archives/edgar/data/1800227/000162828026061531/iaci-20260911_d2.htm | "AI Overviews" "traffic" |
| Perfect Corp.  (PERF, PERF-WT)  (CIK 0001899830) | 20-F | 2026-03-13 | https://www.sec.gov/Archives/edgar/data/1899830/000189983026000013/perf-20251231.htm | "AI platforms" "referrals" |
| Perion Network Ltd.  (PERI)  (CIK 0001338940) | 20-F | 2025-03-25 | https://www.sec.gov/Archives/edgar/data/1338940/000117891325001021/zk2532820.htm | "AI search" "conversion"; "AI search" "traffic"; "AI-powered search" "traffic"; "ChatGPT" "traffic" |
| Perion Network Ltd.  (PERI)  (CIK 0001338940) | 20-F | 2026-03-16 | https://www.sec.gov/Archives/edgar/data/1338940/000117891326000927/zk2634522.htm | "AI assistants" "traffic"; "AI search" "conversion"; "AI search" "traffic"; "ChatGPT" "traffic"; "Perplexity" "traffic" |
| Pharming Group N.V.  (PHAR)  (CIK 0001828316) | 20-F | 2026-04-02 | https://www.sec.gov/Archives/edgar/data/1828316/000182831626000015/pharm-20251231.htm | "LLM" "referral" |
| Pharming Group N.V.  (PHAR)  (CIK 0001828316) | 20-F/A | 2026-04-13 | https://www.sec.gov/Archives/edgar/data/1828316/000182831626000019/pharm-20251231.htm | "LLM" "referral" |
| Platinum Analytics Cayman Ltd  (CIK 0002053033) | F-1 | 2025-05-09 | https://www.sec.gov/Archives/edgar/data/2053033/000164117225009388/formf-1.htm | "LLMs" "referral" |
| Platinum Analytics Cayman Ltd  (PLTS)  (CIK 0002053033) | F-1/A | 2025-06-20 | https://www.sec.gov/Archives/edgar/data/2053033/000164117225015854/formf-1a.htm | "LLMs" "referral" |
| Platinum Analytics Cayman Ltd  (PLTS)  (CIK 0002053033) | F-1/A | 2025-07-21 | https://www.sec.gov/Archives/edgar/data/2053033/000164117225020392/formf-1a.htm | "LLMs" "referral" |
| Platinum Analytics Cayman Ltd  (PLTS)  (CIK 0002053033) | F-1/A | 2025-08-05 | https://www.sec.gov/Archives/edgar/data/2053033/000164117225022205/formf-1a.htm | "LLMs" "referral" |
| Platinum Analytics Cayman Ltd  (PLTS)  (CIK 0002053033) | 424B4 | 2025-09-19 | https://www.sec.gov/Archives/edgar/data/2053033/000149315225014278/form424b4.htm | "LLMs" "referral" |
| Platinum Analytics Cayman Ltd  (PLTS)  (CIK 0002053033) | 424B4 | 2025-09-22 | https://www.sec.gov/Archives/edgar/data/2053033/000149315225014361/form424b4.htm | "LLMs" "referral" |
| Platinum Analytics Cayman Ltd  (PLTS)  (CIK 0002053033) | 20-F | 2026-01-30 | https://www.sec.gov/Archives/edgar/data/2053033/000149315226004347/form20-f.htm | "LLMs" "referral" |
| Prenetics Global Ltd  (PRE, PRENW)  (CIK 0001876431) | 20-F | 2026-04-30 | https://www.sec.gov/Archives/edgar/data/1876431/000162828026028623/pre-20251231.htm | "AI search" "conversion"; "AI search" "traffic"; "AI-powered search" "traffic" |
| Prenetics Global Ltd  (PRE, PRENW)  (CIK 0001876431) | 20-F/A | 2026-07-30 | https://www.sec.gov/Archives/edgar/data/1876431/000162828026050791/pre-20251231.htm | "AI search" "conversion"; "AI search" "traffic"; "AI-powered search" "traffic" |
| Prenetics Global Ltd  (PRE, PRENW)  (CIK 0001876431) | 20-F/A | 2026-09-04 | https://www.sec.gov/Archives/edgar/data/1876431/000162828026060650/pre-20251231.htm | "AI search" "conversion"; "AI search" "traffic"; "AI-powered search" "traffic" |
| Primerica, Inc.  (PRI)  (CIK 0001475922) | 10-K | 2026-02-27 | https://www.sec.gov/Archives/edgar/data/1475922/000119312526082233/pri-20251231.htm | "generative engine optimization" |
| Priority Technology Holdings, Inc.  (PRTH, PRTHU)  (CIK 0001 | 8-K | 2025-08-19 | https://www.sec.gov/Archives/edgar/data/1653558/000165355825000107/assetpurchaseagreement-boo.htm | "ChatGPT" "referral" |
| Priority Technology Holdings, Inc.  (PRTH, PRTHU)  (CIK 0001 | 8-K | 2025-10-02 | https://www.sec.gov/Archives/edgar/data/1653558/000162828025043526/a101assetpurchaseandcontri.htm | "ChatGPT" "referral" |
| Priority Technology Holdings, Inc.  (PRTH, PRTHU)  (CIK 0001 | 8-K | 2026-08-26 | https://www.sec.gov/Archives/edgar/data/1653558/000165355826000134/ex101membershipinterestp.htm | "ChatGPT" "referral" |
| ProQR Therapeutics N.V.  (PRQR)  (CIK 0001612940) | 6-K | 2026-04-08 | https://www.sec.gov/Archives/edgar/data/1612940/000110465926040893/tm2611275d2_ex99-1.htm | "AI discovery" |
| PubMatic, Inc.  (PUBM)  (CIK 0001422930) | 10-K | 2026-02-26 | https://www.sec.gov/Archives/edgar/data/1422930/000142293026000010/pubm-20251231.htm | "generative AI" "referral traffic" |
| PubMatic, Inc.  (PUBM)  (CIK 0001422930) | 10-Q | 2026-05-07 | https://www.sec.gov/Archives/edgar/data/1422930/000142293026000024/pubm-20260331.htm | "AI-powered search" "traffic" |
| Q2 Holdings, Inc.  (QTWO)  (CIK 0001410384) | 10-K | 2025-02-12 | https://www.sec.gov/Archives/edgar/data/1410384/000141038425000010/qtwo-20241231.htm | "AI discovery" |
| Q2 Holdings, Inc.  (QTWO)  (CIK 0001410384) | 10-K | 2026-02-11 | https://www.sec.gov/Archives/edgar/data/1410384/000141038426000006/qtwo-20251231.htm | "AI discovery" |
| Quad/Graphics, Inc.  (QUAD)  (CIK 0001481792) | 10-K | 2026-02-18 | https://www.sec.gov/Archives/edgar/data/1481792/000148179226000042/quad-20251231.htm | "AI discovery" |
| QumulusAI, Inc.  (CIK 0002084026) | S-1 | 2025-12-31 | https://www.sec.gov/Archives/edgar/data/2084026/000143774925039073/quma20251223_s1.htm | "ChatGPT" "traffic" |
| QumulusAI, Inc.  (QMLS)  (CIK 0002084026) | S-1/A | 2026-02-13 | https://www.sec.gov/Archives/edgar/data/2084026/000143774926004148/quma20260210_s1a.htm | "ChatGPT" "traffic" |
| QumulusAI, Inc.  (QMLS)  (CIK 0002084026) | S-1/A | 2026-04-07 | https://www.sec.gov/Archives/edgar/data/2084026/000143774926011598/quma20260402c_s1a.htm | "ChatGPT" "traffic" |
| QumulusAI, Inc.  (QMLS)  (CIK 0002084026) | S-1/A | 2026-05-01 | https://www.sec.gov/Archives/edgar/data/2084026/000143774926014458/quma20260428_s1a.htm | "ChatGPT" "traffic" |
| QumulusAI, Inc.  (QMLS)  (CIK 0002084026) | S-1/A | 2026-05-14 | https://www.sec.gov/Archives/edgar/data/2084026/000143774926017093/quma20260513_s1a.htm | "ChatGPT" "traffic" |
| QumulusAI, Inc.  (QMLS)  (CIK 0002084026) | S-1/A | 2026-06-10 | https://www.sec.gov/Archives/edgar/data/2084026/000143774926020200/quma20260605_s1a.htm | "ChatGPT" "traffic" |
| QumulusAI, Inc.  (QMLS)  (CIK 0002084026) | S-1/A | 2026-06-29 | https://www.sec.gov/Archives/edgar/data/2084026/000143774926022020/quma20260626_s1a.htm | "ChatGPT" "traffic" |
| QumulusAI, Inc.  (QMLS)  (CIK 0002084026) | 424B4 | 2026-07-15 | https://www.sec.gov/Archives/edgar/data/2084026/000143774926023622/quma20260714_424b4.htm | "ChatGPT" "traffic" |
| RECURSION PHARMACEUTICALS, INC.  (RXRX)  (CIK 0001601830) | 10-K | 2025-02-28 | https://www.sec.gov/Archives/edgar/data/1601830/000160183025000035/rxrx-20241231.htm | "LLM" "referral"; "LLMs" "referral" |
| RELX PLC  (RELX, RLXXF)  (CIK 0000929869) | 6-K | 2025-02-20 | https://www.sec.gov/Archives/edgar/data/929869/000092986925000025/tmb-20250213xex99d1.htm | "LLM" "referral"; "LLMs" "referral" |
| RELX PLC  (RELX, RLXXF)  (CIK 0000929869) | 20-F | 2025-02-20 | https://www.sec.gov/Archives/edgar/data/929869/000155837025001178/relx-20241231xex15d2.htm | "LLM" "referral"; "LLMs" "referral" |
| RELX PLC  (RELX, RLXXF)  (CIK 0000929869) | 6-K | 2025-02-20 | https://www.sec.gov/Archives/edgar/data/929869/000092986925000028/tmb-20241231xex99d1.pdf | "LLM" "referral" |
| RELX PLC  (RELX, RLXXF)  (CIK 0000929869) | 6-K | 2026-02-19 | https://www.sec.gov/Archives/edgar/data/929869/000092986926000019/relx-20260212xex99d1.pdf | "AI search" "conversion"; "AI search" "traffic"; "LLM" "referral" |
| RELX PLC  (RELX, RLXXF)  (CIK 0000929869) | 20-F | 2026-02-19 | https://www.sec.gov/Archives/edgar/data/929869/000110465926017277/relx-20251231xex15d2.htm | "AI search" "conversion"; "AI search" "traffic"; "LLM" "referral" |
| RENTOKIL INITIAL PLC /FI  (RTO, RKLIF)  (CIK 0000930157) | 20-F | 2026-03-25 | https://www.sec.gov/Archives/edgar/data/930157/000110465926034062/rto-20251231xex15d1.htm | "AI search" "conversion"; "LLMs" "referral" |
| RENTOKIL INITIAL PLC /FI  (RTO, RKLIF)  (CIK 0000930157) | 6-K | 2026-03-25 | https://www.sec.gov/Archives/edgar/data/930157/000110465926034082/tm261151d2_ex99-1.pdf | "AI search" "conversion"; "LLMs" "referral" |
| REVELATION BIOSCIENCES, INC.  (REVB, REVBW)  (CIK 0001810560 | 10-K | 2026-02-26 | https://www.sec.gov/Archives/edgar/data/1810560/000119312526076552/revb-20251231.htm | "AI platforms" "referrals" |
| REZOLVE AI Ltd  (RZLV, RZLVW)  (CIK 0001920294) | F-1 | 2025-01-13 | https://www.sec.gov/Archives/edgar/data/1920294/000095017025004476/rzlv-20250111.htm | "LLM" "referral"; "LLMs" "referral" |
| REZOLVE AI Ltd  (RZLV, RZLVW)  (CIK 0001920294) | F-1/A | 2025-01-29 | https://www.sec.gov/Archives/edgar/data/1920294/000095017025010107/rzlv-20250129.htm | "LLM" "referral"; "LLMs" "referral" |
| REZOLVE AI PLC  (RZLV, RZLVW)  (CIK 0001920294) | 20-F | 2025-04-24 | https://www.sec.gov/Archives/edgar/data/1920294/000095017025057622/rzlv-20241231.htm | "AI search" "conversion"; "AI search" "traffic"; "LLM" "referral"; "LLMs" "referral" |
| REZOLVE AI PLC  (RZLV, RZLVW)  (CIK 0001920294) | F-1 | 2025-05-16 | https://www.sec.gov/Archives/edgar/data/1920294/000095017025073708/rzlv-20250516.htm | "AI search" "conversion"; "AI search" "traffic"; "LLM" "referral"; "LLMs" "referral" |
| REZOLVE AI PLC  (RZLV, RZLVW)  (CIK 0001920294) | F-1 | 2025-07-30 | https://www.sec.gov/Archives/edgar/data/1920294/000095017025100411/rzlv-20250730.htm | "AI search" "conversion"; "AI search" "traffic"; "LLM" "referral"; "LLMs" "referral" |
| REZOLVE AI PLC  (RZLV, RZLVW)  (CIK 0001920294) | F-1/A | 2025-09-09 | https://www.sec.gov/Archives/edgar/data/1920294/000119312525199264/rzlv-20250909.htm | "AI search" "conversion"; "AI search" "traffic"; "LLM" "referral"; "LLMs" "referral" |
| REZOLVE AI PLC  (RZLV, RZLVW)  (CIK 0001920294) | 20-F | 2026-03-30 | https://www.sec.gov/Archives/edgar/data/1920294/000119312526132456/rzlv-20251231.htm | "AI discovery"; "AI platforms" "referrals"; "AI search" "conversion"; "AI search" "traffic"; "AI-powered search" "traffic"; "LLM" "referral"; "LLMs" "referral" |
| REZOLVE AI PLC  (RZLV, RZLVW)  (CIK 0001920294) | 6-K | 2026-06-05 | https://www.sec.gov/Archives/edgar/data/1920294/000119312526259945/rzlv-ex99_1.htm | "AI visibility"; "answer engine"; "answer engines" |
| RICHTECH ROBOTICS INC.  (RR)  (CIK 0001963685) | 10-K | 2026-01-20 | https://www.sec.gov/Archives/edgar/data/1963685/000121390026005343/ea0272362-10k_richtech.htm | "AI platforms" "referrals" |
| RICHTECH ROBOTICS INC.  (RR)  (CIK 0001963685) | 10-K/A | 2026-08-07 | https://www.sec.gov/Archives/edgar/data/1963685/000121390026086751/ea0298288-10ka1_richtech.htm | "AI platforms" "referrals" |
| ROGERS COMMUNICATIONS INC  (RCI, RCIAF)  (CIK 0000733099) | 6-K | 2025-01-02 | https://www.sec.gov/Archives/edgar/data/733099/000119312525000564/d843628dex991.htm | "ChatGPT" "referral" |
| ROGERS COMMUNICATIONS INC  (RCI, RCIAF)  (CIK 0000733099) | 6-K | 2026-01-05 | https://www.sec.gov/Archives/edgar/data/733099/000119312526001436/d85125dex991.htm | "ChatGPT" "referral" |
| RPM Interactive, Inc.  (CIK 0002018293) | S-1 | 2025-06-16 | https://www.sec.gov/Archives/edgar/data/2018293/000121390025054837/ea0243614-s1_rpminter.htm | "ChatGPT" "traffic" |
| Rackspace Technology, Inc.  (RXT)  (CIK 0001810019) | 10-K | 2026-03-06 | https://www.sec.gov/Archives/edgar/data/1810019/000181001926000015/rxt-20251231.htm | "AI platforms" "referrals" |
| RedHill Biopharma Ltd.  (RDHL)  (CIK 0001553846) | 20-F | 2025-04-10 | https://www.sec.gov/Archives/edgar/data/1553846/000155837025004648/rdhl-20241231x20f.htm | "LLM" "referral" |
| RedHill Biopharma Ltd.  (RDHL)  (CIK 0001553846) | 20-F | 2026-04-27 | https://www.sec.gov/Archives/edgar/data/1553846/000110465926049055/rdhl-20251231x20f.htm | "AI platforms" "referrals"; "LLM" "referral" |
| Reddit, Inc.  (RDDT)  (CIK 0001713445) | 8-K | 2025-02-12 | https://www.sec.gov/Archives/edgar/data/1713445/000171344525000016/exhibit992q424.htm | "AI-powered search" "traffic" |
| Reddit, Inc.  (RDDT)  (CIK 0001713445) | 10-K | 2025-02-13 | https://www.sec.gov/Archives/edgar/data/1713445/000171344525000018/rddt-20241231.htm | "ChatGPT" "traffic" |
| Reddit, Inc.  (RDDT)  (CIK 0001713445) | 8-K | 2025-07-31 | https://www.sec.gov/Archives/edgar/data/1713445/000171344525000194/exhibit992q225.htm | "AI search engines" "increase" |
| Reddit, Inc.  (RDDT)  (CIK 0001713445) | 10-Q | 2025-08-01 | https://www.sec.gov/Archives/edgar/data/1713445/000171344525000196/rddt-20250630.htm | "AI Overviews" "traffic" |
| Reddit, Inc.  (RDDT)  (CIK 0001713445) | 10-Q | 2025-10-31 | https://www.sec.gov/Archives/edgar/data/1713445/000171344525000227/rddt-20250930.htm | "AI Overviews" "traffic" |
| Reddit, Inc.  (RDDT)  (CIK 0001713445) | 8-K | 2026-02-05 | https://www.sec.gov/Archives/edgar/data/1713445/000171344526000020/exhibit992q425.htm | "AI-powered search" "traffic"; "agentic search" |
| Reddit, Inc.  (RDDT)  (CIK 0001713445) | 10-K | 2026-02-06 | https://www.sec.gov/Archives/edgar/data/1713445/000171344526000022/rddt-20251231.htm | "AI Overviews" "traffic"; "ChatGPT" "traffic" |
| Reddit, Inc.  (RDDT)  (CIK 0001713445) | 10-Q | 2026-05-01 | https://www.sec.gov/Archives/edgar/data/1713445/000171344526000069/rddt-20260331.htm | "AI Overviews" "traffic" |
| Reddit, Inc.  (RDDT)  (CIK 0001713445) | 8-K | 2026-07-30 | https://www.sec.gov/Archives/edgar/data/1713445/000171344526000098/exhibit992q226.htm | "ChatGPT" "referral"; "ChatGPT" "traffic"; "LLM" "referral"; "LLMs" "referral" |
| Reddit, Inc.  (RDDT)  (CIK 0001713445) | 10-Q | 2026-07-31 | https://www.sec.gov/Archives/edgar/data/1713445/000171344526000100/rddt-20260630.htm | "AI Overviews" "traffic"; "AI search" "conversion"; "AI search" "traffic" |
| Reformation Inc.  (CIK 0001787117) | S-1 | 2026-06-25 | https://www.sec.gov/Archives/edgar/data/1787117/000110465926077832/tm2513004-7_s1.htm | "AI Mode" "traffic"; "agentic search" |
| Reformation Inc.  (REF)  (CIK 0001787117) | S-1/A | 2026-07-20 | https://www.sec.gov/Archives/edgar/data/1787117/000110465926084856/tm2513004-10_s1.htm | "AI Mode" "traffic"; "agentic search" |
| Reformation Inc.  (REF)  (CIK 0001787117) | 424B4 | 2026-07-30 | https://www.sec.gov/Archives/edgar/data/1787117/000110465926088733/tm2513004-17_424b4.htm | "AI Mode" "traffic"; "agentic search" |
| Reformation Inc.  (REF)  (CIK 0001787117) | 10-Q | 2026-09-11 | https://www.sec.gov/Archives/edgar/data/1787117/000162828026061594/lymi-20260627.htm | "AI Mode" "traffic"; "agentic search" |
| Regenique Group Ltd  (CIK 0002063022) | F-1 | 2025-10-31 | https://www.sec.gov/Archives/edgar/data/2063022/000121390025104769/ea0235572-08.htm | "ChatGPT" "referral" |
| Rekor Systems, Inc.  (REKR)  (CIK 0001697851) | 8-K | 2025-03-31 | https://www.sec.gov/Archives/edgar/data/1697851/000143774925010184/ex_796684.htm | "AI-driven traffic" |
| Rekor Systems, Inc.  (REKR)  (CIK 0001697851) | 10-K | 2025-03-31 | https://www.sec.gov/Archives/edgar/data/1697851/000143774925010193/rekr20241231_10k.htm | "AI-driven traffic" |
| Rekor Systems, Inc.  (REKR)  (CIK 0001697851) | 10-K | 2026-03-31 | https://www.sec.gov/Archives/edgar/data/1697851/000143774926010647/rekr20251231_10k.htm | "AI-driven traffic" |
| Rent the Runway, Inc.  (RENT)  (CIK 0001468327) | 10-K | 2025-04-15 | https://www.sec.gov/Archives/edgar/data/1468327/000146832725000056/wdq-20250131.htm | "AI search" "conversion"; "AI search" "traffic" |
| Rent the Runway, Inc.  (RENT)  (CIK 0001468327) | 10-Q | 2025-06-06 | https://www.sec.gov/Archives/edgar/data/1468327/000146832725000097/rent-20250430.htm | "AI search" "conversion"; "AI search" "traffic" |
| Rent the Runway, Inc.  (RENT)  (CIK 0001468327) | 8-K | 2026-04-14 | https://www.sec.gov/Archives/edgar/data/1468327/000146832726000018/fy2025earningsrelease.htm | "answer engine" |
| Rent the Runway, Inc.  (RENT)  (CIK 0001468327) | 10-K | 2026-04-14 | https://www.sec.gov/Archives/edgar/data/1468327/000146832726000020/wdq-20260131.htm | "agentic search"; "answer engine" |
| Rent the Runway, Inc.  (RENT)  (CIK 0001468327) | 10-Q | 2026-06-03 | https://www.sec.gov/Archives/edgar/data/1468327/000146832726000031/rent-20260430.htm | "agentic search" |
| Rent the Runway, Inc.  (RENT)  (CIK 0001468327) | 10-Q | 2026-09-11 | https://www.sec.gov/Archives/edgar/data/1468327/000146832726000088/rent-20260731.htm | "agentic search" |
| Republic Power Group Ltd  (RPGL)  (CIK 0001912884) | F-1 | 2026-03-18 | https://www.sec.gov/Archives/edgar/data/1912884/000121390026030971/ea0282024-01.htm | "LLM" "referral" |
| Republic Power Group Ltd  (RPGL)  (CIK 0001912884) | F-1/A | 2026-03-27 | https://www.sec.gov/Archives/edgar/data/1912884/000121390026035446/ea0282024-02.htm | "LLM" "referral" |
| Republic Power Group Ltd  (RPGL)  (CIK 0001912884) | 424B4 | 2026-04-03 | https://www.sec.gov/Archives/edgar/data/1912884/000121390026039917/ea0282024-04.htm | "LLM" "referral" |
| Republic Power Group Ltd  (RPGL)  (CIK 0001912884) | F-1 | 2026-07-23 | https://www.sec.gov/Archives/edgar/data/1912884/000121390026080753/ea0298965-f1_republic.htm | "LLM" "referral" |
| Republic Power Group Ltd  (RPGL)  (CIK 0001912884) | 424B4 | 2026-08-04 | https://www.sec.gov/Archives/edgar/data/1912884/000121390026085063/ea0299881-424b4_republic.htm | "LLM" "referral" |
| Republic Power Group Ltd  (RPGL)  (CIK 0001912884) | F-1 | 2026-08-20 | https://www.sec.gov/Archives/edgar/data/1912884/000121390026091992/ea0302806-f1_republic.htm | "LLM" "referral" |
| Republic Power Group Ltd  (RPGL)  (CIK 0001912884) | 424B4 | 2026-08-27 | https://www.sec.gov/Archives/edgar/data/1912884/000121390026094237/ea0303554-424b4_republic.htm | "LLM" "referral" |
| Revolve Group, Inc.  (RVLV)  (CIK 0001746618) | 10-Q | 2025-08-05 | https://www.sec.gov/Archives/edgar/data/1746618/000095017025103103/rvlv-20250630.htm | "AI Mode" "traffic" |
| Revolve Group, Inc.  (RVLV)  (CIK 0001746618) | 10-Q | 2025-11-04 | https://www.sec.gov/Archives/edgar/data/1746618/000119312525264815/rvlv-20250930.htm | "AI Mode" "traffic" |
| Revolve Group, Inc.  (RVLV)  (CIK 0001746618) | 10-K | 2026-02-25 | https://www.sec.gov/Archives/edgar/data/1746618/000119312526071307/rvlv-20251231.htm | "AI Mode" "traffic" |
| Revolve Group, Inc.  (RVLV)  (CIK 0001746618) | 10-Q | 2026-05-05 | https://www.sec.gov/Archives/edgar/data/1746618/000119312526206542/rvlv-20260331.htm | "AI Mode" "traffic" |
| Revolve Group, Inc.  (RVLV)  (CIK 0001746618) | 8-K | 2026-06-03 | https://www.sec.gov/Archives/edgar/data/1746618/000119312526254659/rvlv-ex99_1.htm | "AI search" "conversion" |
| Revolve Group, Inc.  (RVLV)  (CIK 0001746618) | 10-Q | 2026-08-04 | https://www.sec.gov/Archives/edgar/data/1746618/000119312526332938/rvlv-20260630.htm | "AI Mode" "traffic" |
| Ribbon Communications Inc.  (RBBN)  (CIK 0001708055) | 10-K | 2025-02-27 | https://www.sec.gov/Archives/edgar/data/1708055/000155837025001773/tmb-20241231x10k.htm | "LLM" "referral" |
| Ribbon Communications Inc.  (RBBN)  (CIK 0001708055) | 10-K | 2026-02-26 | https://www.sec.gov/Archives/edgar/data/1708055/000170805526000012/rbbn-20251231x10k.htm | "AI platforms" "referrals"; "LLM" "referral" |
| Robot Consulting Co., Ltd.  (CIK 0002007599) | F-1 | 2025-02-12 | https://www.sec.gov/Archives/edgar/data/2007599/000149315225006147/formf-1.htm | "ChatGPT" "traffic" |
| Robot Consulting Co., Ltd.  (LAWR)  (CIK 0002007599) | F-1/A | 2025-03-19 | https://www.sec.gov/Archives/edgar/data/2007599/000149315225010940/formf-1a.htm | "ChatGPT" "traffic" |
| Robot Consulting Co., Ltd.  (LAWR)  (CIK 0002007599) | F-1/A | 2025-03-26 | https://www.sec.gov/Archives/edgar/data/2007599/000164117225000731/formf-1a.htm | "ChatGPT" "traffic" |
| Robot Consulting Co., Ltd.  (LAWR)  (CIK 0002007599) | F-1/A | 2025-04-14 | https://www.sec.gov/Archives/edgar/data/2007599/000164117225004390/formf-1a.htm | "ChatGPT" "traffic" |
| Robot Consulting Co., Ltd.  (LAWR)  (CIK 0002007599) | F-1/A | 2025-06-16 | https://www.sec.gov/Archives/edgar/data/2007599/000164117225015287/formf-1a.htm | "ChatGPT" "traffic" |
| Robot Consulting Co., Ltd.  (LAWR)  (CIK 0002007599) | 424B4 | 2025-07-18 | https://www.sec.gov/Archives/edgar/data/2007599/000164117225020137/form424b4.htm | "ChatGPT" "traffic" |
| Robot Consulting Co., Ltd.  (LAWR)  (CIK 0002007599) | 20-F | 2025-08-15 | https://www.sec.gov/Archives/edgar/data/2007599/000164117225024240/form20-f.htm | "ChatGPT" "traffic" |
| Robot Consulting Co., Ltd.  (LAWR)  (CIK 0002007599) | 20-F | 2026-07-31 | https://www.sec.gov/Archives/edgar/data/2007599/000149315226035636/form20-f.htm | "ChatGPT" "traffic" |
| Rocket Companies, Inc.  (RKT)  (CIK 0001805284) | 10-K | 2026-03-02 | https://www.sec.gov/Archives/edgar/data/1805284/000162828026013283/rkt-20251231.htm | "AI Overviews" "traffic"; "large language models" "organic traffic" |
| Roivant Sciences Ltd.  (ROIV)  (CIK 0001635088) | 10-Q | 2025-08-11 | https://www.sec.gov/Archives/edgar/data/1635088/000114036125030001/ef20050394_10q.htm | "LLMs" "referral" |
| Roivant Sciences Ltd.  (ROIV)  (CIK 0001635088) | 10-Q | 2025-11-10 | https://www.sec.gov/Archives/edgar/data/1635088/000163508825000016/roiv-20250930.htm | "LLMs" "referral" |
| Roivant Sciences Ltd.  (ROIV)  (CIK 0001635088) | 10-Q | 2026-02-06 | https://www.sec.gov/Archives/edgar/data/1635088/000163508826000011/roiv-20251231.htm | "LLMs" "referral" |
| Roivant Sciences Ltd.  (ROIV)  (CIK 0001635088) | 10-K | 2026-05-20 | https://www.sec.gov/Archives/edgar/data/1635088/000163508826000061/roiv-20260331.htm | "AI platforms" "referrals"; "LLMs" "referral" |
| Root, Inc.  (ROOT)  (CIK 0001788882) | 10-K | 2026-02-25 | https://www.sec.gov/Archives/edgar/data/1788882/000178888226000014/root-20251231.htm | "ChatGPT" "referral"; "ChatGPT" "traffic"; "Perplexity" "traffic" |
| Rumble Inc.  (RUM, RUMBW)  (CIK 0001830081) | 8-K | 2025-11-10 | https://www.sec.gov/Archives/edgar/data/1830081/000121390025107926/ea026473501ex99-1_rumble.htm | "AI-powered search" "traffic"; "Perplexity" "traffic" |
| Rumble Inc.  (RUM, RUMBW)  (CIK 0001830081) | 8-K | 2026-03-05 | https://www.sec.gov/Archives/edgar/data/1830081/000121390026024095/ea028001301ex99-1.htm | "AI-powered search" "traffic"; "Perplexity" "traffic" |
| SAGTEC GLOBAL Ltd  (SAGT)  (CIK 0002029138) | F-1/A | 2025-01-28 | https://www.sec.gov/Archives/edgar/data/2029138/000121390025007199/ea0211571-06.htm | "ChatGPT" "referral"; "ChatGPT" "traffic" |
| SAGTEC GLOBAL Ltd  (SAGT)  (CIK 0002029138) | F-1/A | 2025-02-19 | https://www.sec.gov/Archives/edgar/data/2029138/000121390025015247/ea0211571-09.htm | "ChatGPT" "referral"; "ChatGPT" "traffic" |
| SAGTEC GLOBAL Ltd  (SAGT)  (CIK 0002029138) | 424B4 | 2025-03-07 | https://www.sec.gov/Archives/edgar/data/2029138/000121390025021563/ea0211571-11.htm | "ChatGPT" "referral"; "ChatGPT" "traffic" |
| SANTANDER UK GROUP HOLDINGS PLC  (CIK 0001649373) | 20-F | 2025-03-07 | https://www.sec.gov/Archives/edgar/data/1649373/000162828025011193/san-20241231.htm | "AI search" "conversion" |
| SANTANDER UK GROUP HOLDINGS PLC  (CIK 0001649373) | 20-F | 2026-03-12 | https://www.sec.gov/Archives/edgar/data/1649373/000164937326000013/san-20251231.htm | "ChatGPT" "new members" |
| SAP SE  (SAP, SAPGF)  (CIK 0001000184) | 20-F | 2026-02-26 | https://www.sec.gov/Archives/edgar/data/1000184/000110465926020058/sap-20251231x20f.htm | "AI assistants" "traffic"; "Perplexity" "traffic" |
| SAP SE  (SAP, SAPGF)  (CIK 0001000184) | 6-K | 2026-03-06 | https://www.sec.gov/Archives/edgar/data/1000184/000110465926024381/tm2529416d2_ex99-1.htm | "AI assistants" "traffic"; "Perplexity" "traffic" |
| SB Energy, Inc.  (CIK 0002133037) | S-1 | 2026-09-01 | https://www.sec.gov/Archives/edgar/data/2133037/000162828026059639/sbenergy-sx1.htm | "ChatGPT" "traffic" |
| SB Energy, Inc.  (SBE)  (CIK 0002133037) | S-1/A | 2026-09-21 | https://www.sec.gov/Archives/edgar/data/2133037/000162828026062846/sbenergy-sx1a2.htm | "ChatGPT" "traffic" |
| SEMrush Holdings, Inc.  (SEMR)  (CIK 0001831840) | 10-K | 2025-03-03 | https://www.sec.gov/Archives/edgar/data/1831840/000162828025009448/semr-20241231.htm | "ChatGPT" "referral"; "ChatGPT" "traffic" |
| SEMrush Holdings, Inc.  (SEMR)  (CIK 0001831840) | 8-K | 2025-08-04 | https://www.sec.gov/Archives/edgar/data/1831840/000162828025037458/semrush8-kexhibit991q22025.htm | "AI-powered search" "traffic"; "ChatGPT" "traffic"; "Perplexity" "traffic" |
| SEMrush Holdings, Inc.  (SEMR)  (CIK 0001831840) | 10-Q | 2025-08-07 | https://www.sec.gov/Archives/edgar/data/1831840/000162828025038933/semr-20250630.htm | "AI-powered search" "traffic" |
| SEMrush Holdings, Inc.  (SEMR)  (CIK 0001831840) | 8-K | 2025-11-05 | https://www.sec.gov/Archives/edgar/data/1831840/000162828025049628/semrush8-kexhibit991q32025.htm | "AI discovery"; "AI visibility" |
| SEMrush Holdings, Inc.  (SEMR)  (CIK 0001831840) | 10-Q | 2025-11-10 | https://www.sec.gov/Archives/edgar/data/1831840/000162828025051083/semr-20250930.htm | "AI search" "conversion"; "AI search" "traffic"; "AI-powered search" "traffic" |
| SEMrush Holdings, Inc.  (SEMR)  (CIK 0001831840) | 10-K | 2026-03-02 | https://www.sec.gov/Archives/edgar/data/1831840/000162828026013259/semr-20251231.htm | "AI platforms" "referrals"; "AI search" "conversion"; "AI search" "traffic"; "AI visibility"; "AI-powered search" "traffic"; "ChatGPT" "referral"; "ChatGPT" "traffic"; "LLM" "referral"; "LLMs" "referral"; "Perplexity" "traffic"; "answer engine"; "answer engines"; "generative engine optimization" |
| SFIDA X, Inc.  (CIK 0002035964) | F-1/A | 2025-04-25 | https://www.sec.gov/Archives/edgar/data/2035964/000164117225006157/formf-1a.htm | "ChatGPT" "referral" |
| SFIDA X, Inc.  (CIK 0002035964) | F-1/A | 2025-06-02 | https://www.sec.gov/Archives/edgar/data/2035964/000164117225013267/formf-1a.htm | "ChatGPT" "referral"; "ChatGPT" "traffic" |
| SFIDA X, Inc.  (CIK 0002035964) | F-1/A | 2025-06-03 | https://www.sec.gov/Archives/edgar/data/2035964/000164117225013380/formf-1a.htm | "ChatGPT" "referral"; "ChatGPT" "traffic" |
| SFIDA X, Inc.  (CIK 0002035964) | F-1/A | 2025-09-05 | https://www.sec.gov/Archives/edgar/data/2035964/000149315225012661/formf-1a.htm | "ChatGPT" "referral"; "ChatGPT" "traffic" |
| SFIDA X, Inc.  (CIK 0002035964) | F-1/A | 2025-09-05 | https://www.sec.gov/Archives/edgar/data/2035964/000149315225012663/formf-1a.htm | "ChatGPT" "referral"; "ChatGPT" "traffic" |
| SFIDA X, Inc.  (CIK 0002035964) | F-1/A | 2025-11-14 | https://www.sec.gov/Archives/edgar/data/2035964/000149315225023594/formf-1a.htm | "ChatGPT" "referral"; "ChatGPT" "traffic" |
| SFIDA X, Inc.  (CIK 0002035964) | F-1/A | 2025-11-28 | https://www.sec.gov/Archives/edgar/data/2035964/000149315225025342/formf-1a.htm | "ChatGPT" "referral"; "ChatGPT" "traffic" |
| SHOPIFY INC.  (SHOP)  (CIK 0001594805) | 10-K | 2026-02-11 | https://www.sec.gov/Archives/edgar/data/1594805/000159480526000007/shop-20251231.htm | "AI platforms" "referrals"; "AI-powered search" "traffic" |
| SHOPIFY INC.  (SHOP)  (CIK 0001594805) | 8-K | 2026-05-08 | https://www.sec.gov/Archives/edgar/data/1594805/000159480526000022/yearend2025mic.htm | "ChatGPT" "referral"; "LLM" "referral" |
| SIMILARWEB LTD.  (SMWB)  (CIK 0001842731) | 6-K | 2025-05-13 | https://www.sec.gov/Archives/edgar/data/1842731/000184273125000018/q12025smwbshareholderlet.htm | "AI platforms" "referrals"; "ChatGPT" "referral"; "ChatGPT" "traffic"; "LLM" "referral"; "LLMs" "referral"; "Perplexity" "traffic" |
| SIMILARWEB LTD.  (SMWB)  (CIK 0001842731) | 6-K | 2025-08-12 | https://www.sec.gov/Archives/edgar/data/1842731/000184273125000028/q22025smwbshareholderlet.htm | "ChatGPT" "traffic" |
| SIMILARWEB LTD.  (SMWB)  (CIK 0001842731) | 6-K | 2025-11-12 | https://www.sec.gov/Archives/edgar/data/1842731/000184273125000049/a6-kxex992xq32025smwbsha.htm | "LLM" "referral"; "LLMs" "referral"; "generative AI" "referral traffic" |
| SIMILARWEB LTD.  (SMWB)  (CIK 0001842731) | 20-F | 2026-03-02 | https://www.sec.gov/Archives/edgar/data/1842731/000184273126000018/smwb-20251231.htm | "AI platforms" "referrals"; "AI visibility"; "LLM" "referral"; "LLMs" "referral"; "answer engine"; "answer engines" |
| SIMILARWEB LTD.  (SMWB)  (CIK 0001842731) | 6-K | 2026-05-13 | https://www.sec.gov/Archives/edgar/data/1842731/000184273126000031/a6-kxexhibit991xq131032026.htm | "LLM" "referral" |
| SK TELECOM CO LTD  (SKM)  (CIK 0001015650) | 20-F | 2026-04-29 | https://www.sec.gov/Archives/edgar/data/1015650/000119312526188763/d78252d20f.htm | "AI search" "conversion"; "AI search" "traffic"; "Perplexity" "traffic" |
| SK TELECOM CO LTD  (SKM, SKMTF)  (CIK 0001015650) | 20-F | 2025-04-29 | https://www.sec.gov/Archives/edgar/data/1015650/000119312525101730/d877090d20f.htm | "AI search" "conversion"; "AI search" "traffic"; "Perplexity" "traffic" |
| SOUNDHOUND AI, INC.  (SOUN, SOUNW)  (CIK 0001840856) | 10-K | 2025-03-11 | https://www.sec.gov/Archives/edgar/data/1840856/000162828025011821/soun-20241231.htm | "AI platforms" "referrals"; "ChatGPT" "bookings"; "ChatGPT" "traffic" |
| SOUNDHOUND AI, INC.  (SOUN, SOUNW)  (CIK 0001840856) | 10-K | 2026-03-02 | https://www.sec.gov/Archives/edgar/data/1840856/000184085626000006/soun-20251231.htm | "AI platforms" "referrals"; "ChatGPT" "bookings"; "ChatGPT" "traffic" |
| SOUNDHOUND AI, INC.  (SOUN, SOUNW)  (CIK 0001840856) | 10-Q | 2026-05-11 | https://www.sec.gov/Archives/edgar/data/1840856/000184085626000015/soun-20260331.htm | "AI platforms" "referrals" |
| SOUNDHOUND AI, INC.  (SOUN, SOUNW)  (CIK 0001840856) | 10-Q | 2026-08-10 | https://www.sec.gov/Archives/edgar/data/1840856/000184085626000022/soun-20260630.htm | "AI platforms" "referrals" |
| SPECTRAL IP, INC.  (CIK 0002042176) | S-1 | 2025-03-20 | https://www.sec.gov/Archives/edgar/data/2042176/000121390025025266/ea0218945-04.htm | "AI-referred" |
| SURO CAPITAL CORP.  (SSSS, SSSSL)  (CIK 0001509470) | 10-K | 2026-03-11 | https://www.sec.gov/Archives/edgar/data/1509470/000149315226009641/form10-k.htm | "ChatGPT" "new members"; "ChatGPT" "referral" |
| Sachem Capital Corp.  (SACH, SCCD, SCCE, SCCF, SCCG, SACH-PA | 10-K | 2026-03-13 | https://www.sec.gov/Archives/edgar/data/1682220/000168222026000014/sach-20251231.htm | "LLM" "referral" |
| SailPoint, Inc.  (SAIL)  (CIK 0002030781) | 10-K | 2026-03-19 | https://www.sec.gov/Archives/edgar/data/2030781/000203078126000003/sail-20260131.htm | "answer engines" |
| Santander UK plc  (SNTUF, STNDF)  (CIK 0001087711) | 20-F | 2025-03-07 | https://www.sec.gov/Archives/edgar/data/1087711/000162828025011199/san-20241231.htm | "AI search" "conversion" |
| Santander UK plc  (SNTUF, STNDF)  (CIK 0001087711) | 20-F | 2026-03-12 | https://www.sec.gov/Archives/edgar/data/1087711/000108771126000008/san-20251231.htm | "ChatGPT" "new members" |
| SentinelOne, Inc.  (S)  (CIK 0001583708) | 8-K | 2025-08-28 | https://www.sec.gov/Archives/edgar/data/1583708/000158370825000146/s-q2fy26earningspresenta.htm | "ChatGPT" "bookings" |
| SentinelOne, Inc.  (S)  (CIK 0001583708) | 8-K | 2025-12-04 | https://www.sec.gov/Archives/edgar/data/1583708/000158370825000157/s-q3fy26earningspresenta.htm | "ChatGPT" "bookings" |
| ServiceNow, Inc.  (NOW)  (CIK 0001373715) | 10-K | 2025-01-30 | https://www.sec.gov/Archives/edgar/data/1373715/000137371525000010/now-20241231.htm | "LLMs" "referral" |
| ServiceNow, Inc.  (NOW)  (CIK 0001373715) | 10-K | 2026-01-29 | https://www.sec.gov/Archives/edgar/data/1373715/000137371526000007/now-20251231.htm | "LLMs" "referral" |
| ServiceTitan, Inc.  (TTAN)  (CIK 0001638826) | 10-Q | 2025-01-14 | https://www.sec.gov/Archives/edgar/data/1638826/000095017025005456/ttan-20241031.htm | "LLM" "referral"; "LLMs" "referral" |
| ServiceTitan, Inc.  (TTAN)  (CIK 0001638826) | 10-K | 2025-04-02 | https://www.sec.gov/Archives/edgar/data/1638826/000095017025048834/ttan-20250131.htm | "LLM" "referral"; "LLMs" "referral" |
| ServiceTitan, Inc.  (TTAN)  (CIK 0001638826) | 10-Q | 2025-06-12 | https://www.sec.gov/Archives/edgar/data/1638826/000095017025085509/ttan-20250430.htm | "LLM" "referral"; "LLMs" "referral" |
| ServiceTitan, Inc.  (TTAN)  (CIK 0001638826) | 10-Q | 2025-09-10 | https://www.sec.gov/Archives/edgar/data/1638826/000095017025114005/ttan-20250731.htm | "LLM" "referral"; "LLMs" "referral" |
| ServiceTitan, Inc.  (TTAN)  (CIK 0001638826) | 10-Q | 2025-12-09 | https://www.sec.gov/Archives/edgar/data/1638826/000119312525312847/ttan-20251031.htm | "LLM" "referral"; "LLMs" "referral" |
| ServiceTitan, Inc.  (TTAN)  (CIK 0001638826) | 10-K | 2026-03-25 | https://www.sec.gov/Archives/edgar/data/1638826/000163882626000028/ttan-20260131.htm | "LLM" "referral"; "LLMs" "referral" |
| ServiceTitan, Inc.  (TTAN)  (CIK 0001638826) | 10-Q | 2026-06-05 | https://www.sec.gov/Archives/edgar/data/1638826/000163882626000047/ttan-20260430.htm | "LLM" "referral"; "LLMs" "referral" |
| ServiceTitan, Inc.  (TTAN)  (CIK 0001638826) | 10-Q | 2026-09-08 | https://www.sec.gov/Archives/edgar/data/1638826/000163882626000094/ttan-20260731.htm | "LLM" "referral"; "LLMs" "referral" |
| SharonAI Holdings Inc.  (SHAZ)  (CIK 0002068385) | 10-K | 2026-03-31 | https://www.sec.gov/Archives/edgar/data/2068385/000149315226014068/form10-k.htm | "LLM" "referral"; "LLMs" "referral" |
| SharonAI Holdings Inc.  (SHAZ, SHAZW)  (CIK 0002068385) | S-1 | 2026-06-05 | https://www.sec.gov/Archives/edgar/data/2068385/000149315226027509/forms-1.htm | "LLM" "referral"; "LLMs" "referral" |
| SharonAI Holdings Inc.  (SHAZ, SHAZW)  (CIK 0002068385) | S-1 | 2026-07-31 | https://www.sec.gov/Archives/edgar/data/2068385/000149315226035629/forms-1.htm | "LLM" "referral"; "LLMs" "referral" |
| SharonAI Holdings Inc.  (SHAZ, SHAZW)  (CIK 0002068385) | S-1/A | 2026-08-11 | https://www.sec.gov/Archives/edgar/data/2068385/000149315226037203/forms-1a.htm | "LLM" "referral"; "LLMs" "referral" |
| SharonAI Holdings Inc.  (SHAZ, SHAZW)  (CIK 0002068385) | S-1 | 2026-08-12 | https://www.sec.gov/Archives/edgar/data/2068385/000149315226037453/forms-1.htm | "LLM" "referral"; "LLMs" "referral" |
| SharonAI Holdings Inc.  (SHAZ, SHAZW)  (CIK 0002068385) | S-1/A | 2026-08-18 | https://www.sec.gov/Archives/edgar/data/2068385/000149315226039014/forms-1a.htm | "LLM" "referral"; "LLMs" "referral" |
| SharonAI Holdings Inc.  (SHAZ, SHAZW)  (CIK 0002068385) | S-1/A | 2026-08-20 | https://www.sec.gov/Archives/edgar/data/2068385/000149315226039475/forms-1a.htm | "LLM" "referral"; "LLMs" "referral" |
| Silexion Therapeutics Corp  (SLXN, SLXNW)  (CIK 0002022416) | S-1/A | 2025-01-14 | https://www.sec.gov/Archives/edgar/data/2022416/000117891325000100/zk2432429.htm | "LLM" "referral" |
| Silexion Therapeutics Corp  (SLXN, SLXNW)  (CIK 0002022416) | S-1/A | 2025-01-14 | https://www.sec.gov/Archives/edgar/data/2022416/000117891325000110/zk2532549.htm | "LLM" "referral" |
| Silexion Therapeutics Corp  (SLXN, SLXNW)  (CIK 0002022416) | 424B4 | 2025-01-17 | https://www.sec.gov/Archives/edgar/data/2022416/000117891325000141/zk2532560.htm | "LLM" "referral" |
| Silexion Therapeutics Corp  (SLXN, SLXNW)  (CIK 0002022416) | S-1 | 2025-02-12 | https://www.sec.gov/Archives/edgar/data/2022416/000117891325000443/zk2532684.htm | "LLM" "referral" |
| Silexion Therapeutics Corp  (SLXN, SLXNW)  (CIK 0002022416) | 10-K | 2025-03-18 | https://www.sec.gov/Archives/edgar/data/2022416/000117891325000887/zk2532833.htm | "LLM" "referral" |
| Silexion Therapeutics Corp  (SLXN, SLXNW)  (CIK 0002022416) | S-1/A | 2025-03-27 | https://www.sec.gov/Archives/edgar/data/2022416/000117891325001087/zk2532930.htm | "LLM" "referral" |
| Silexion Therapeutics Corp  (SLXN, SLXNW)  (CIK 0002022416) | S-1 | 2025-08-26 | https://www.sec.gov/Archives/edgar/data/2022416/000117891325003107/zk2533703.htm | "LLM" "referral" |
| Silexion Therapeutics Corp  (SLXN, SLXNW)  (CIK 0002022416) | S-1 | 2025-09-05 | https://www.sec.gov/Archives/edgar/data/2022416/000117891325003260/zk2533684.htm | "LLM" "referral" |
| Silexion Therapeutics Corp  (SLXN, SLXNW)  (CIK 0002022416) | 424B4 | 2025-09-12 | https://www.sec.gov/Archives/edgar/data/2022416/000117891325003306/zk2533779.htm | "LLM" "referral" |
| Silexion Therapeutics Corp  (SLXN, SLXNW)  (CIK 0002022416) | 10-K | 2026-03-17 | https://www.sec.gov/Archives/edgar/data/2022416/000117891326000953/zk2634529.htm | "LLM" "referral" |
| Silexion Therapeutics Corp  (SLXN, SLXNW)  (CIK 0002022416) | S-1 | 2026-08-07 | https://www.sec.gov/Archives/edgar/data/2022416/000117891326003961/zk2635892.htm | "LLM" "referral" |
| Silexion Therapeutics Corp  (SLXN, SLXNW)  (CIK 0002022416) | S-1/A | 2026-08-10 | https://www.sec.gov/Archives/edgar/data/2022416/000117891326004003/zk2635896.htm | "LLM" "referral" |
| Silexion Therapeutics Corp  (SLXN, SLXNW)  (CIK 0002022416) | 424B4 | 2026-08-13 | https://www.sec.gov/Archives/edgar/data/2022416/000117891326004116/zk2635948.htm | "LLM" "referral" |
| Skillsoft Corp.  (SKIL, SKILW)  (CIK 0001774675) | 10-K | 2025-04-14 | https://www.sec.gov/Archives/edgar/data/1774675/000143774925011912/skil20250131_10k.htm | "ChatGPT" "bookings" |
| Skillsoft Corp.  (SKIL, SKILW)  (CIK 0001774675) | 10-K | 2026-04-07 | https://www.sec.gov/Archives/edgar/data/1774675/000143774926011602/skil20260131_10k.htm | "ChatGPT" "bookings" |
| Snap Inc  (SNAP)  (CIK 0001564408) | 8-K | 2025-11-05 | https://www.sec.gov/Archives/edgar/data/1564408/000156440825000063/q32025investorletter.htm | "answer engine" |
| Snap Inc  (SNAP)  (CIK 0001564408) | 8-K | 2026-02-04 | https://www.sec.gov/Archives/edgar/data/1564408/000156440826000011/snapincq42025investorlet.htm | "Perplexity" "traffic" |
| Snap Inc  (SNAP)  (CIK 0001564408) | 10-K | 2026-02-05 | https://www.sec.gov/Archives/edgar/data/1564408/000156440826000013/snap-20251231.htm | "AI platforms" "referrals"; "AI search" "conversion"; "AI search" "traffic"; "Perplexity" "traffic" |
| Snap Inc  (SNAP)  (CIK 0001564408) | 8-K | 2026-05-06 | https://www.sec.gov/Archives/edgar/data/1564408/000156440826000024/snapincq12026investorlet.htm | "Perplexity" "traffic" |
| Snap Inc  (SNAP)  (CIK 0001564408) | 10-Q | 2026-05-07 | https://www.sec.gov/Archives/edgar/data/1564408/000156440826000027/snap-20260331.htm | "AI platforms" "referrals" |
| Snap Inc  (SNAP)  (CIK 0001564408) | 10-Q | 2026-08-04 | https://www.sec.gov/Archives/edgar/data/1564408/000156440826000052/snap-20260630.htm | "AI platforms" "referrals" |
| Snowflake Inc.  (SNOW)  (CIK 0001640147) | 10-K | 2025-03-21 | https://www.sec.gov/Archives/edgar/data/1640147/000164014725000052/snow-20250131.htm | "LLM" "referral"; "LLMs" "referral" |
| Snowflake Inc.  (SNOW)  (CIK 0001640147) | 10-K | 2026-03-20 | https://www.sec.gov/Archives/edgar/data/1640147/000164014726000008/snow-20260131.htm | "LLM" "referral" |
| Sportradar Group AG  (SRAD)  (CIK 0001836470) | 20-F | 2026-03-27 | https://www.sec.gov/Archives/edgar/data/1836470/000110465926035485/srad-20251231x20f.htm | "AI assistants" "traffic" |
| Spotify Technology S.A.  (SPOT)  (CIK 0001639920) | 20-F | 2026-02-10 | https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/ck0001639920-20251231.htm | "ChatGPT" "traffic" |
| Sprinklr, Inc.  (CXM)  (CIK 0001569345) | 10-K | 2025-03-21 | https://www.sec.gov/Archives/edgar/data/1569345/000156934525000019/cxm-20250131.htm | "LLM" "referral"; "LLMs" "referral" |
| Sprinklr, Inc.  (CXM)  (CIK 0001569345) | 10-K | 2026-03-19 | https://www.sec.gov/Archives/edgar/data/1569345/000156934526000015/cxm-20260131.htm | "LLM" "referral"; "LLMs" "referral" |
| Sprout Social, Inc.  (SPT)  (CIK 0001517375) | 10-K | 2026-02-27 | https://www.sec.gov/Archives/edgar/data/1517375/000151737526000015/spt-20251231.htm | "AI-powered search" "traffic"; "answer engines"; "large language models" "organic traffic" |
| Stagwell Inc  (STGW)  (CIK 0000876883) | 10-K | 2025-03-11 | https://www.sec.gov/Archives/edgar/data/876883/000087688325000009/stgw-20241231.htm | "ChatGPT" "referral" |
| Stagwell Inc  (STGW)  (CIK 0000876883) | 8-K | 2026-03-10 | https://www.sec.gov/Archives/edgar/data/876883/000087688326000004/a4q25earningspresentatio.htm | "AI search" "conversion" |
| Stagwell Inc  (STGW)  (CIK 0000876883) | 10-K | 2026-03-13 | https://www.sec.gov/Archives/edgar/data/876883/000087688326000010/stgw-20251231.htm | "ChatGPT" "referral" |
| Star Fashion Culture Holdings Ltd  (STFS)  (CIK 0002003061) | F-1 | 2025-05-19 | https://www.sec.gov/Archives/edgar/data/2003061/000121390025044988/ea0240026-f1_starfashion.htm | "LLM" "referral" |
| Star Fashion Culture Holdings Ltd  (STFS)  (CIK 0002003061) | F-1/A | 2025-06-16 | https://www.sec.gov/Archives/edgar/data/2003061/000121390025054620/ea0245531-f1a1_starfashion.htm | "LLM" "referral" |
| Star Fashion Culture Holdings Ltd  (STFS)  (CIK 0002003061) | 424B4 | 2025-07-07 | https://www.sec.gov/Archives/edgar/data/2003061/000121390025061646/ea0247720-424b4_starfashion.htm | "LLM" "referral" |
| StoneCo Ltd.  (STNE)  (CIK 0001745431) | 20-F | 2025-04-24 | https://www.sec.gov/Archives/edgar/data/1745431/000162828025019653/stne-20241231.htm | "LLM" "referral" |
| StoneCo Ltd.  (STNE)  (CIK 0001745431) | 20-F | 2026-04-23 | https://www.sec.gov/Archives/edgar/data/1745431/000207097926000170/stne-20251231.htm | "LLM" "referral" |
| Stonepeak-Plus Infrastructure Fund LP  (CIK 0002045458) | 10-K | 2026-03-31 | https://www.sec.gov/Archives/edgar/data/2045458/000204545826000012/sp-20251231.htm | "ChatGPT" "referral"; "ChatGPT" "traffic" |
| SunCar Technology Group Inc.  (SDA, SDAWW)  (CIK 0001936804) | 20-F | 2026-04-28 | https://www.sec.gov/Archives/edgar/data/1936804/000121390026048537/ea0287753-20f_suncar.htm | "LLM" "referral" |
| Sunrise Communications AG  (SNNRF)  (CIK 0002021938) | 20-F | 2026-02-18 | https://www.sec.gov/Archives/edgar/data/2021938/000202193826000004/updatedexhbit151-annualr.htm | "AI-powered search" "traffic"; "Perplexity" "traffic" |
| System1, Inc.  (SST, SSTPW)  (CIK 0001805833) | 8-K | 2025-11-05 | https://www.sec.gov/Archives/edgar/data/1805833/000180583325000013/q32025-ex991pressrelease.htm | "ChatGPT" "traffic"; "Perplexity" "traffic" |
| TAO Synergies Inc.  (TAOX)  (CIK 0001571934) | 10-K | 2026-03-31 | https://www.sec.gov/Archives/edgar/data/1571934/000110465926037915/taox-20251231x10k.htm | "AI platforms" "referrals" |
| TELEFONICA S A  (TEF, TEFOF)  (CIK 0000814052) | 20-F | 2025-02-27 | https://www.sec.gov/Archives/edgar/data/814052/000081405225000036/tef-20241231.htm | "Perplexity" "traffic"; "answer engine" |
| TELEFONICA S A  (TEF, TEFOF)  (CIK 0000814052) | 6-K | 2025-02-27 | https://www.sec.gov/Archives/edgar/data/814052/000081405225000021/tefres4q24.htm | "Perplexity" "traffic" |
| TELEFONICA S A  (TEF, TEFOF)  (CIK 0000814052) | 6-K | 2025-07-30 | https://www.sec.gov/Archives/edgar/data/814052/000081405225000084/tefhalfyr1s25.htm | "Perplexity" "traffic" |
| TELUS CORP  (TU)  (CIK 0000868675) | 6-K | 2025-04-04 | https://www.sec.gov/Archives/edgar/data/868675/000110465925032268/tm2510043d2_ex99-1.pdf | "ChatGPT" "bookings"; "ChatGPT" "traffic" |
| TELUS CORP  (TU)  (CIK 0000868675) | 6-K | 2025-05-09 | https://www.sec.gov/Archives/edgar/data/868675/000110465925046467/tm2510346d1_ex99-2.htm | "ChatGPT" "bookings"; "ChatGPT" "traffic" |
| TELUS CORP  (TU)  (CIK 0000868675) | 6-K | 2025-08-01 | https://www.sec.gov/Archives/edgar/data/868675/000110465925072894/tu-20250630xex99d2.htm | "ChatGPT" "bookings"; "ChatGPT" "traffic" |
| TELUS CORP  (TU)  (CIK 0000868675) | 6-K | 2025-11-07 | https://www.sec.gov/Archives/edgar/data/868675/000110465925108120/tm2525674d1_ex99-2.htm | "ChatGPT" "traffic" |
| TELUS CORP  (TU)  (CIK 0000868675) | 6-K | 2026-04-02 | https://www.sec.gov/Archives/edgar/data/868675/000110465926039249/tm2610149d2_ex99-1.pdf | "ChatGPT" "traffic" |
| TELUS CORP  (TU)  (CIK 0000868675) | 6-K | 2026-07-31 | https://www.sec.gov/Archives/edgar/data/868675/000110465926088973/tu-20260630xex99d2.htm | "AI discovery"; "ChatGPT" "bookings"; "ChatGPT" "traffic" |
| TELUS International (Cda) Inc.  (TIXT)  (CIK 0001825155) | 20-F | 2025-02-13 | https://www.sec.gov/Archives/edgar/data/1825155/000162828025005299/tixt-20241231.htm | "AI platforms" "referrals" |
| TG-17, Inc.  (CIK 0001756064) | S-1 | 2025-10-07 | https://www.sec.gov/Archives/edgar/data/1756064/000149315225017274/forms-1.htm | "ChatGPT" "bookings"; "ChatGPT" "traffic" |
| TG-17, Inc.  (CIK 0001756064) | S-1/A | 2025-11-12 | https://www.sec.gov/Archives/edgar/data/1756064/000149315225021730/forms-1a.htm | "ChatGPT" "bookings"; "ChatGPT" "traffic" |
| TG-17, Inc.  (CIK 0001756064) | S-1/A | 2025-11-26 | https://www.sec.gov/Archives/edgar/data/1756064/000149315225025181/forms-1a.htm | "ChatGPT" "bookings"; "ChatGPT" "traffic" |
| TG-17, Inc.  (CIK 0001756064) | S-1/A | 2025-12-22 | https://www.sec.gov/Archives/edgar/data/1756064/000149315225028852/forms-1a.htm | "ChatGPT" "bookings"; "ChatGPT" "traffic" |
| TG-17, Inc.  (CIK 0001756064) | S-1/A | 2026-01-12 | https://www.sec.gov/Archives/edgar/data/1756064/000149315226001260/forms-1a.htm | "ChatGPT" "bookings"; "ChatGPT" "traffic" |
| TG-17, Inc.  (CIK 0001756064) | S-1/A | 2026-01-23 | https://www.sec.gov/Archives/edgar/data/1756064/000149315226003351/forms-1a.htm | "ChatGPT" "bookings"; "ChatGPT" "traffic" |
| TG-17, Inc.  (CIK 0001756064) | S-1/A | 2026-01-27 | https://www.sec.gov/Archives/edgar/data/1756064/000149315226003834/forms-1a.htm | "ChatGPT" "bookings"; "ChatGPT" "traffic" |
| TG-17, Inc.  (CIK 0001756064) | S-1/A | 2026-01-29 | https://www.sec.gov/Archives/edgar/data/1756064/000149315226004108/forms-1a.htm | "ChatGPT" "bookings"; "ChatGPT" "traffic" |
| TG-17, Inc.  (CIK 0001756064) | 424B4 | 2026-02-03 | https://www.sec.gov/Archives/edgar/data/1756064/000149315226004930/form424b4.htm | "ChatGPT" "bookings"; "ChatGPT" "traffic" |
| TNL Mediagene  (TNMG, TNMWF)  (CIK 0002013186) | 20-F | 2026-04-30 | https://www.sec.gov/Archives/edgar/data/2013186/000121390026049832/ea0286618-20f_tnlmedia.htm | "AI-powered search" "traffic"; "LLM" "referral"; "generative AI" "referral traffic" |
| TORONTO DOMINION BANK  (TD, TDBCP, TDBKF, TDOMF)  (CIK 00009 | 6-K | 2025-03-04 | https://www.sec.gov/Archives/edgar/data/947263/000110465925020238/tm251010d3_ex99-1.htm | "ChatGPT" "new members" |
| TRUPANION, INC.  (TRUP)  (CIK 0001371285) | 10-K | 2026-02-13 | https://www.sec.gov/Archives/edgar/data/1371285/000137128526000018/trup-20251231.htm | "ChatGPT" "new members"; "ChatGPT" "referral"; "ChatGPT" "traffic" |
| TURKCELL ILETISIM HIZMETLERI A S  (TKC)  (CIK 0001071321) | 6-K | 2026-03-13 | https://www.sec.gov/Archives/edgar/data/1071321/000110465926027444/tm267568d3_ex99-1.pdf | "ChatGPT" "traffic" |
| Tailored Brands, Inc. / DE  (CIK 0002045151) | S-1 | 2026-07-10 | https://www.sec.gov/Archives/edgar/data/2045151/000121390026077111/ea0285017-05.htm | "answer engine" |
| Tailored Brands, Inc. / DE  (MENW)  (CIK 0002045151) | S-1/A | 2026-08-31 | https://www.sec.gov/Archives/edgar/data/2045151/000121390026095715/ea0285017-07.htm | "answer engine" |
| Talkspace, Inc.  (TALK, TALKW)  (CIK 0001803901) | 10-K | 2026-03-13 | https://www.sec.gov/Archives/edgar/data/1803901/000119312526105146/talk-20251231.htm | "LLM" "referral"; "LLMs" "referral" |
| TechTarget, Inc.  (TTGT)  (CIK 0002018064) | 8-K | 2025-08-12 | https://www.sec.gov/Archives/edgar/data/2018064/000095017025106920/ttgt-ex99_1.htm | "AI Overviews" "traffic"; "AI visibility"; "traffic from AI" |
| TechTarget, Inc.  (TTGT)  (CIK 0002018064) | 10-K | 2026-03-11 | https://www.sec.gov/Archives/edgar/data/2018064/000119312526102183/ttgt-20251231.htm | "AI search" "conversion"; "AI search" "traffic"; "LLM citations"; "answer engine"; "answer engines"; "generative engine optimization" |
| TechTarget, Inc.  (TTGT)  (CIK 0002018064) | 8-K | 2026-05-07 | https://www.sec.gov/Archives/edgar/data/2018064/000119312526211953/ttgt-ex99_1.htm | "AI visibility"; "generative engine optimization" |
| TechTarget, Inc.  (TTGT)  (CIK 0002018064) | 8-K | 2026-08-06 | https://www.sec.gov/Archives/edgar/data/2018064/000119312526338041/ttgt-ex99_1.htm | "AI visibility" |
| Tencent Music Entertainment Group  (TME, TCMEF)  (CIK 000174 | 20-F | 2025-04-23 | https://www.sec.gov/Archives/edgar/data/1744676/000095017025056949/tme-20241231.htm | "AI assistants" "traffic" |
| Tencent Music Entertainment Group  (TME, TCMEF)  (CIK 000174 | 20-F | 2026-04-17 | https://www.sec.gov/Archives/edgar/data/1744676/000119312526160257/tme-20251231.htm | "AI assistants" "traffic" |
| Townsquare Media, Inc.  (TSQ)  (CIK 0001499832) | 10-K | 2026-03-16 | https://www.sec.gov/Archives/edgar/data/1499832/000149983226000020/tsq-20251231.htm | "Perplexity" "traffic" |
| Triller Group Inc.  (CIK 0001769624) | 10-K | 2026-01-26 | https://www.sec.gov/Archives/edgar/data/1769624/000121390026007545/ea0265891-10k_triller.htm | "LLMs" "referral" |
| Triller Group Inc.  (ILLR, ILLRW)  (CIK 0001769624) | S-1 | 2025-01-24 | https://www.sec.gov/Archives/edgar/data/1769624/000121390025006210/ea0228228-s1_triller.htm | "LLMs" "referral" |
| Triller Group Inc.  (ILLR, ILLRW)  (CIK 0001769624) | 10-K | 2026-04-14 | https://www.sec.gov/Archives/edgar/data/1769624/000121390026043341/ea0283656-10k_triller.htm | "LLMs" "referral" |
| TripAdvisor, Inc.  (TRIP)  (CIK 0001526520) | 10-K | 2025-02-20 | https://www.sec.gov/Archives/edgar/data/1526520/000095017025023736/trip-20241231.htm | "AI platforms" "referrals"; "ChatGPT" "bookings"; "ChatGPT" "traffic" |
| TripAdvisor, Inc.  (TRIP)  (CIK 0001526520) | 10-K | 2026-02-13 | https://www.sec.gov/Archives/edgar/data/1526520/000119312526051281/trip-20251231.htm | "AI Overviews" "traffic" |
| TripAdvisor, Inc.  (TRIP)  (CIK 0001526520) | 10-Q | 2026-05-07 | https://www.sec.gov/Archives/edgar/data/1526520/000119312526210297/trip-20260331.htm | "AI Overviews" "traffic" |
| TripAdvisor, Inc.  (TRIP)  (CIK 0001526520) | 10-Q | 2026-08-06 | https://www.sec.gov/Archives/edgar/data/1526520/000119312526336693/trip-20260630.htm | "AI Overviews" "traffic" |
| TriplePoint Private Venture Credit Inc.  (CIK 0001792509) | 10-K | 2026-03-10 | https://www.sec.gov/Archives/edgar/data/1792509/000179250926000003/tpvc-20251231.htm | "AI platforms" "referrals" |
| TriplePoint Venture Growth BDC Corp.  (TPVG)  (CIK 000158034 | 10-K | 2026-03-04 | https://www.sec.gov/Archives/edgar/data/1580345/000158034526000008/tpvg-20251231.htm | "AI platforms" "referrals" |
| TruBridge, Inc.  (TBRG)  (CIK 0001169445) | 10-K | 2026-03-31 | https://www.sec.gov/Archives/edgar/data/1169445/000116944526000006/tbrg-20251231.htm | "AI search" "conversion"; "LLM" "referral" |
| Trump Media & Technology Group Corp.  (DJT, DJTWW)  (CIK 000 | 8-K | 2025-08-06 | https://www.sec.gov/Archives/edgar/data/1849635/000114036125029058/ef20053299_ex99-1.htm | "answer engine" |
| Trump Media & Technology Group Corp.  (DJT, DJTWW)  (CIK 000 | 10-Q | 2025-11-07 | https://www.sec.gov/Archives/edgar/data/1849635/000114036125040977/ef20054981_10q.htm | "AI search" "conversion" |
| Trump Media & Technology Group Corp.  (DJT, DJTWW)  (CIK 000 | 10-K | 2026-02-27 | https://www.sec.gov/Archives/edgar/data/1849635/000114036126007174/ef20062365_10k.htm | "AI search" "conversion"; "AI search" "traffic" |
| Tuya Inc.  (TUYA)  (CIK 0001829118) | 20-F | 2025-04-24 | https://www.sec.gov/Archives/edgar/data/1829118/000141057825000850/tuya-20241231x20f.htm | "ChatGPT" "new members"; "ChatGPT" "traffic" |
| Tuya Inc.  (TUYA)  (CIK 0001829118) | 20-F | 2026-04-22 | https://www.sec.gov/Archives/edgar/data/1829118/000110465926046399/tuya-20251231x20f.htm | "ChatGPT" "new members"; "ChatGPT" "traffic" |
| Tuya Inc.  (TUYA)  (CIK 0001829118) | 6-K | 2026-04-22 | https://www.sec.gov/Archives/edgar/data/1829118/000110465926046445/tm2612436d1_ex99-3.pdf | "LLM" "referral" |
| Twin Vee PowerCats, Co.  (VEEE)  (CIK 0001855509) | 8-K | 2025-09-10 | https://www.sec.gov/Archives/edgar/data/1855509/000173112225001224/e6834_ex99-1.htm | "AI search" "traffic" |
| URBAN ONE, INC.  (UONE, UONEK)  (CIK 0001041657) | 10-K | 2026-03-20 | https://www.sec.gov/Archives/edgar/data/1041657/000104165726000016/uone-20251231.htm | "AI search engines" "increase"; "AI search" "conversion"; "AI search" "traffic" |
| Udemy, Inc.  (UDMY)  (CIK 0001607939) | 10-Q | 2025-10-30 | https://www.sec.gov/Archives/edgar/data/1607939/000160793925000139/udmy-20250930.htm | "AI platforms" "referrals" |
| Udemy, Inc.  (UDMY)  (CIK 0001607939) | 10-K | 2026-02-19 | https://www.sec.gov/Archives/edgar/data/1607939/000160793926000034/udmy-20251231.htm | "AI platforms" "referrals"; "ChatGPT" "bookings"; "ChatGPT" "traffic" |
| Udemy, Inc.  (UDMY)  (CIK 0001607939) | 10-Q | 2026-05-11 | https://www.sec.gov/Archives/edgar/data/1607939/000160793926000061/udmy-20260331.htm | "AI platforms" "referrals" |
| Upland Software, Inc.  (UPLD)  (CIK 0001505155) | 10-K | 2026-03-03 | https://www.sec.gov/Archives/edgar/data/1505155/000150515526000007/upld-20251231.htm | "AI search" "conversion"; "generative engine optimization" |
| VARONIS SYSTEMS INC  (VRNS)  (CIK 0001361113) | 10-K | 2026-02-04 | https://www.sec.gov/Archives/edgar/data/1361113/000162828026005450/vrns-20251231.htm | "ChatGPT" "traffic" |
| VERINT SYSTEMS INC  (VRNT)  (CIK 0001166388) | 10-K | 2025-03-26 | https://www.sec.gov/Archives/edgar/data/1166388/000116638825000014/vrnt-20250131.htm | "LLMs" "referral" |
| VERTEX PHARMACEUTICALS INC / MA  (VRTX)  (CIK 0000875320) | 10-K | 2025-02-13 | https://www.sec.gov/Archives/edgar/data/875320/000087532025000053/vrtx-20241231.htm | "ChatGPT" "referral" |
| VIP Play, Inc.  (VIPZ)  (CIK 0001832161) | 8-K | 2025-06-04 | https://www.sec.gov/Archives/edgar/data/1832161/000164117225013598/form8-k.htm | "answer engines" |
| VIP Play, Inc.  (VIPZ)  (CIK 0001832161) | 8-K | 2025-06-04 | https://www.sec.gov/Archives/edgar/data/1832161/000164117225013598/ex10-2.htm | "answer engines" |
| VIP Play, Inc.  (VIPZ)  (CIK 0001832161) | 10-K | 2025-09-29 | https://www.sec.gov/Archives/edgar/data/1832161/000149315225016043/form10-k.htm | "answer engines" |
| VODAFONE GROUP PUBLIC LTD CO  (VOD, VODPF)  (CIK 0000839923) | 20-F | 2026-05-22 | https://www.sec.gov/Archives/edgar/data/839923/000119312526235425/d143190d20f.htm | "LLMs" "referral" |
| VTEX  (VTEX)  (CIK 0001793663) | 20-F | 2025-02-25 | https://www.sec.gov/Archives/edgar/data/1793663/000095017025026601/ck0001793663-20241231.htm | "LLM" "referral" |
| VTEX  (VTEX)  (CIK 0001793663) | 20-F | 2026-02-26 | https://www.sec.gov/Archives/edgar/data/1793663/000119312526076504/ck0001793663-20251231.htm | "LLM" "referral" |
| Veritone, Inc.  (VERI)  (CIK 0001615165) | 10-K | 2025-04-01 | https://www.sec.gov/Archives/edgar/data/1615165/000095017025048602/veri-20241231.htm | "ChatGPT" "bookings"; "ChatGPT" "referral"; "LLM" "referral"; "LLMs" "referral" |
| Veritone, Inc.  (VERI)  (CIK 0001615165) | 10-K | 2026-04-15 | https://www.sec.gov/Archives/edgar/data/1615165/000162828026025214/veri-20251231.htm | "ChatGPT" "bookings"; "ChatGPT" "referral"; "LLM" "referral"; "LLMs" "referral" |
| Verses AI Inc.  (VRSSD, VRSSF)  (CIK 0001879001) | 8-K | 2025-07-02 | https://www.sec.gov/Archives/edgar/data/1879001/000164117225017609/ex99-3.htm | "ChatGPT" "traffic" |
| Verses AI Inc.  (VRSSD, VRSSF)  (CIK 0001879001) | 10-K | 2025-07-14 | https://www.sec.gov/Archives/edgar/data/1879001/000164117225019545/form10-k.htm | "ChatGPT" "traffic" |
| Verses AI Inc.  (VRSSF)  (CIK 0001879001) | S-1 | 2026-04-01 | https://www.sec.gov/Archives/edgar/data/1879001/000149315226014453/forms-1.htm | "ChatGPT" "traffic" |
| Viant Technology Inc.  (DSP)  (CIK 0001828791) | 10-Q | 2026-08-10 | https://www.sec.gov/Archives/edgar/data/1828791/000182879126000072/dsp-20260630.htm | "AI-powered search" "traffic" |
| Vipshop Holdings Ltd  (VIPS)  (CIK 0001529192) | 20-F | 2026-04-16 | https://www.sec.gov/Archives/edgar/data/1529192/000110465926044015/vips-20251231x20f.htm | "AI-powered search" "traffic" |
| VisitIQ Corp.  (VIIQ)  (CIK 0001470129) | 10-K | 2026-05-20 | https://www.sec.gov/Archives/edgar/data/1470129/000175392626000917/g085722_10k.htm | "AI Overviews" "traffic"; "AI search" "conversion"; "AI search" "traffic"; "AI-powered search" "traffic"; "ChatGPT" "bookings"; "ChatGPT" "referral"; "ChatGPT" "traffic" |
| Vocodia Holdings Corp  (VHAI, VHABW, VHAIW)  (CIK 0001880431 | 10-K | 2025-04-30 | https://www.sec.gov/Archives/edgar/data/1880431/000121390025037129/ea0238485-10k_vocodia.htm | "AI assistants" "traffic" |
| Volato Group, Inc.  (SOAR, SOARW)  (CIK 0001853070) | 10-K | 2026-03-12 | https://www.sec.gov/Archives/edgar/data/1853070/000162828026017343/soar-20251231.htm | "LLM" "referral" |
| Voltage X Ltd  (CIK 0002057404) | F-1 | 2025-08-05 | https://www.sec.gov/Archives/edgar/data/2057404/000121390025071704/ea0228406-06.htm | "AI platforms" "referrals" |
| Voltage X Ltd  (CIK 0002057404) | F-1/A | 2025-09-02 | https://www.sec.gov/Archives/edgar/data/2057404/000121390025082979/ea0228406-08.htm | "AI platforms" "referrals" |
| Voltage X Ltd  (CIK 0002057404) | F-1/A | 2025-09-22 | https://www.sec.gov/Archives/edgar/data/2057404/000121390025089951/ea0228406-11.htm | "AI platforms" "referrals" |
| Voltage X Ltd  (CIK 0002057404) | F-1/A | 2025-09-30 | https://www.sec.gov/Archives/edgar/data/2057404/000121390025093661/ea0228406-13.htm | "AI platforms" "referrals" |
| Vuzix Corp  (VUZI)  (CIK 0001463972) | 10-K | 2025-03-13 | https://www.sec.gov/Archives/edgar/data/1463972/000155837025002903/vuzi-20241231x10k.htm | "AI assistants" "traffic"; "ChatGPT" "traffic" |
| WEIBO Corp  (WB)  (CIK 0001595761) | 20-F | 2025-04-15 | https://www.sec.gov/Archives/edgar/data/1595761/000141057825000730/wb-20241231x20f.htm | "AI search" "conversion"; "AI search" "traffic" |
| WOLFSPEED, INC.  (WOLF)  (CIK 0000895419) | 10-K | 2025-08-26 | https://www.sec.gov/Archives/edgar/data/895419/000089541925000110/wolf-20250629.htm | "ChatGPT" "referral"; "ChatGPT" "traffic" |
| WOLFSPEED, INC.  (WOLF)  (CIK 0000895419) | 10-Q | 2025-11-07 | https://www.sec.gov/Archives/edgar/data/895419/000089541925000132/wolf-20250928.htm | "ChatGPT" "traffic" |
| WOLFSPEED, INC.  (WOLF)  (CIK 0000895419) | 10-Q | 2026-02-06 | https://www.sec.gov/Archives/edgar/data/895419/000089541926000016/wolf-20251228.htm | "ChatGPT" "traffic" |
| WPP plc  (WPP, WPPGF)  (CIK 0000806968) | 6-K | 2026-02-26 | https://www.sec.gov/Archives/edgar/data/806968/000165495426001583/a4516u.htm | "answer engines" |
| WW INTERNATIONAL, INC.  (WW)  (CIK 0000105319) | 10-K | 2025-02-28 | https://www.sec.gov/Archives/edgar/data/105319/000095017025029511/ww-20241228.htm | "AI-powered search" "traffic" |
| WW INTERNATIONAL, INC.  (WW)  (CIK 0000105319) | 8-K | 2026-03-16 | https://www.sec.gov/Archives/edgar/data/105319/000119312526107148/d122531dex992.htm | "ChatGPT" "new members" |
| WW INTERNATIONAL, INC.  (WW)  (CIK 0000105319) | 10-K | 2026-03-16 | https://www.sec.gov/Archives/edgar/data/105319/000119312526107176/ww-20251231.htm | "AI-powered search" "traffic" |
| Walmart Inc.  (WMT)  (CIK 0000104169) | 10-K | 2026-03-13 | https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/wmt-20260131.htm | "AI search" "traffic"; "AI-powered search" "traffic" |
| Warburg Pincus Access Fund, L.P.  (CIK 0002082826) | 10-K | 2026-01-29 | https://www.sec.gov/Archives/edgar/data/2082826/000119312526029707/d32585d10k.htm | "LLM" "referral" |
| Waterdrop Inc.  (WDH)  (CIK 0001823986) | 20-F | 2025-04-25 | https://www.sec.gov/Archives/edgar/data/1823986/000141057825000891/wdh-20241231x20f.htm | "LLM" "referral"; "LLMs" "referral" |
| Waterdrop Inc.  (WDH)  (CIK 0001823986) | 6-K | 2025-09-04 | https://www.sec.gov/Archives/edgar/data/1823986/000110465925087282/tm2524976d1_ex99-1.htm | "LLM" "referral" |
| Waterdrop Inc.  (WDH)  (CIK 0001823986) | 20-F | 2026-04-28 | https://www.sec.gov/Archives/edgar/data/1823986/000110465926049772/wdh-20251231x20f.htm | "LLM" "referral"; "LLMs" "referral" |
| Wayfair Inc.  (W)  (CIK 0001616707) | 10-K | 2026-02-19 | https://www.sec.gov/Archives/edgar/data/1616707/000161670726000027/w-20251231.htm | "AI-powered search" "traffic" |
| Wealth Management System Inc.  (CIK 0002074158) | F-1 | 2025-10-02 | https://www.sec.gov/Archives/edgar/data/2074158/000149315225016578/formf-1.htm | "LLM" "referral"; "LLMs" "referral" |
| Wealth Management System Inc.  (CIK 0002074158) | F-1/A | 2025-12-08 | https://www.sec.gov/Archives/edgar/data/2074158/000149315225026606/formf-1a.htm | "LLM" "referral"; "LLMs" "referral" |
| Wealth Management System Inc.  (GIVE)  (CIK 0002074158) | F-1/A | 2026-02-27 | https://www.sec.gov/Archives/edgar/data/2074158/000149315226008305/formf-1a.htm | "LLM" "referral"; "LLMs" "referral" |
| Wealth Management System Inc.  (GIVE)  (CIK 0002074158) | F-1/A | 2026-03-26 | https://www.sec.gov/Archives/edgar/data/2074158/000149315226012895/formf-1a.htm | "LLM" "referral"; "LLMs" "referral" |
| Wealth Management System Inc.  (GIVE)  (CIK 0002074158) | F-1/A | 2026-04-15 | https://www.sec.gov/Archives/edgar/data/2074158/000149315226016768/formf-1a.htm | "LLM" "referral"; "LLMs" "referral" |
| Wearable Devices Ltd.  (WLDS, WLDSW)  (CIK 0001887673) | 20-F | 2026-03-12 | https://www.sec.gov/Archives/edgar/data/1887673/000121390026026977/ea0280234-20f_wearable.htm | "ChatGPT" "bookings" |
| Wise Group plc  (WSE)  (CIK 0002099039) | 6-K | 2026-06-26 | https://www.sec.gov/Archives/edgar/data/2099039/000119312526283123/d192097dex991.htm | "LLMs" "referral" |
| Wix.com Ltd.  (WIX)  (CIK 0001576789) | 6-K | 2025-09-08 | https://www.sec.gov/Archives/edgar/data/1576789/000162828025041728/supplementalcompanydisclos.htm | "AI visibility" |
| Wix.com Ltd.  (WIX)  (CIK 0001576789) | 6-K | 2025-11-12 | https://www.sec.gov/Archives/edgar/data/1576789/000162828025051521/wix-proxystatement2025agm.htm | "AI visibility"; "generative engine optimization" |
| Wix.com Ltd.  (WIX)  (CIK 0001576789) | 20-F | 2026-03-05 | https://www.sec.gov/Archives/edgar/data/1576789/000162828026015222/wix-20251231.htm | "AI platforms" "referrals" |
| Workday, Inc.  (WDAY)  (CIK 0001327811) | 10-K | 2026-03-06 | https://www.sec.gov/Archives/edgar/data/1327811/000132781126000014/wday-20260131.htm | "AI platforms" "referrals"; "AI-referred" |
| Workday, Inc.  (WDAY)  (CIK 0001327811) | 10-Q | 2026-05-22 | https://www.sec.gov/Archives/edgar/data/1327811/000132781126000026/wday-20260430.htm | "AI-referred" |
| Workday, Inc.  (WDAY)  (CIK 0001327811) | 10-Q | 2026-08-27 | https://www.sec.gov/Archives/edgar/data/1327811/000132781126000044/wday-20260731.htm | "AI-referred" |
| XCel Brands, Inc.  (XELB)  (CIK 0001083220) | 10-K | 2025-05-28 | https://www.sec.gov/Archives/edgar/data/1083220/000155837025008172/xelb-20241231x10k.htm | "ChatGPT" "traffic" |
| XCel Brands, Inc.  (XELB)  (CIK 0001083220) | S-1 | 2026-02-04 | https://www.sec.gov/Archives/edgar/data/1083220/000110465926010353/xelb-20250930xs1.htm | "ChatGPT" "traffic" |
| XTI Aerospace, Inc.  (XTIA)  (CIK 0001529113) | 10-K | 2025-04-15 | https://www.sec.gov/Archives/edgar/data/1529113/000121390025032213/ea0235307-10k_xtiaerospace.htm | "ChatGPT" "traffic" |
| Xiao-I Corp  (AIXI)  (CIK 0001935172) | 20-F | 2025-05-15 | https://www.sec.gov/Archives/edgar/data/1935172/000121390025044439/ea0238811-20f_xiaoicorp.htm | "ChatGPT" "traffic" |
| Xiao-I Corp  (AIXI)  (CIK 0001935172) | 20-F | 2026-05-15 | https://www.sec.gov/Archives/edgar/data/1935172/000121390026057986/ea0290336-20f_xiao.htm | "ChatGPT" "traffic" |
| Xiao-I Corp  (AIXI)  (CIK 0001935172) | 20-F/A | 2026-05-22 | https://www.sec.gov/Archives/edgar/data/1935172/000121390026060270/ea0291729-20fa1_xiao.htm | "ChatGPT" "traffic" |
| YD Bio Ltd  (YDES, YDESW)  (CIK 0002011674) | 20-F | 2026-04-30 | https://www.sec.gov/Archives/edgar/data/2011674/000121390026050282/ea0286160-20f_ydbio.htm | "AI platforms" "referrals" |
| YELP INC  (YELP)  (CIK 0001345016) | 10-Q | 2025-05-09 | https://www.sec.gov/Archives/edgar/data/1345016/000134501625000030/yelp-20250331.htm | "LLMs" "referral" |
| YELP INC  (YELP)  (CIK 0001345016) | 8-K | 2025-08-07 | https://www.sec.gov/Archives/edgar/data/1345016/000134501625000038/yelpq22025ex992lettertos.htm | "AI search" "traffic"; "AI-powered search" "traffic" |
| YELP INC  (YELP)  (CIK 0001345016) | 8-K | 2025-11-06 | https://www.sec.gov/Archives/edgar/data/1345016/000134501625000067/yelpq32025ex992lettertos.htm | "AI search" "traffic"; "AI-powered search" "traffic" |
| YELP INC  (YELP)  (CIK 0001345016) | 8-K | 2026-02-12 | https://www.sec.gov/Archives/edgar/data/1345016/000134501626000011/yelpq42025ex992lettertos.htm | "AI search" "conversion"; "AI search" "traffic" |
| YELP INC  (YELP)  (CIK 0001345016) | 10-K | 2026-02-27 | https://www.sec.gov/Archives/edgar/data/1345016/000134501626000019/yelp-20251231.htm | "AI Mode" "traffic"; "AI Overviews" "traffic"; "AI platforms" "referrals"; "AI search" "conversion"; "AI search" "traffic"; "LLMs" "referral" |
| YELP INC  (YELP)  (CIK 0001345016) | 8-K/A | 2026-02-27 | https://www.sec.gov/Archives/edgar/data/1345016/000134501626000018/yelpq42025ex992lettertos.htm | "AI search" "conversion"; "AI search" "traffic" |
| YELP INC  (YELP)  (CIK 0001345016) | 8-K | 2026-08-06 | https://www.sec.gov/Archives/edgar/data/1345016/000134501626000059/yelpq22026ex992lettertos.htm | "AI Mode" "traffic"; "AI citations"; "AI search" "traffic"; "ChatGPT" "traffic"; "Perplexity" "traffic" |
| YELP INC  (YELP)  (CIK 0001345016) | 8-K | 2026-08-06 | https://www.sec.gov/Archives/edgar/data/1345016/000134501626000059/yelpq2-26ex991pressrelease.htm | "ChatGPT" "traffic" |
| YELP INC  (YELP)  (CIK 0001345016) | 10-Q | 2026-08-07 | https://www.sec.gov/Archives/edgar/data/1345016/000134501626000066/yelp-20260630.htm | "ChatGPT" "referral"; "ChatGPT" "traffic" |
| Yalla Group Ltd  (YALA)  (CIK 0001794350) | 6-K | 2025-05-20 | https://www.sec.gov/Archives/edgar/data/1794350/000095017025074863/yala-ex99_1.htm | "AI-driven traffic" |
| Yatra Online, Inc.  (YTRA)  (CIK 0001516899) | 20-F | 2025-07-31 | https://www.sec.gov/Archives/edgar/data/1516899/000164117225021717/form20-f.htm | "large language models" "organic traffic" |
| Yatra Online, Inc.  (YTRA)  (CIK 0001516899) | 20-F | 2026-07-31 | https://www.sec.gov/Archives/edgar/data/1516899/000149315226035684/form20-f.htm | "large language models" "organic traffic" |
| Yext, Inc.  (YEXT)  (CIK 0001614178) | 8-K | 2025-03-05 | https://www.sec.gov/Archives/edgar/data/1614178/000161417825000020/q4fy25shareholderletter.htm | "AI assistants" "traffic"; "AI search" "conversion"; "AI search" "traffic"; "AI visibility"; "ChatGPT" "bookings"; "ChatGPT" "traffic"; "agentic search" |
| Yext, Inc.  (YEXT)  (CIK 0001614178) | 10-K | 2025-03-13 | https://www.sec.gov/Archives/edgar/data/1614178/000161417825000030/yext-20250131.htm | "AI search" "conversion"; "AI search" "traffic" |
| Yext, Inc.  (YEXT)  (CIK 0001614178) | 8-K | 2025-06-03 | https://www.sec.gov/Archives/edgar/data/1614178/000161417825000065/q1fy26shareholderletter.htm | "AI discovery"; "AI search" "conversion"; "AI search" "traffic"; "ChatGPT" "traffic"; "Perplexity" "traffic" |
| Yext, Inc.  (YEXT)  (CIK 0001614178) | 8-K | 2025-09-08 | https://www.sec.gov/Archives/edgar/data/1614178/000161417825000118/ex991q2fy26earningsrelease.htm | "AI search" "conversion" |
| Yext, Inc.  (YEXT)  (CIK 0001614178) | 8-K | 2026-03-09 | https://www.sec.gov/Archives/edgar/data/1614178/000162828026016005/ex992q4fy26shareholderlett.htm | "AI citations"; "AI discovery"; "AI visibility" |
| Yext, Inc.  (YEXT)  (CIK 0001614178) | 10-K | 2026-03-10 | https://www.sec.gov/Archives/edgar/data/1614178/000162828026016402/yext-20260131.htm | "AI search" "conversion"; "AI search" "traffic" |
| Yext, Inc.  (YEXT)  (CIK 0001614178) | 8-K | 2026-06-02 | https://www.sec.gov/Archives/edgar/data/1614178/000162828026039786/ex992q1fy27shareholderlett.htm | "AI discovery"; "AI search" "conversion"; "AI visibility"; "answer engine"; "answer engines" |
| Yext, Inc.  (YEXT)  (CIK 0001614178) | 8-K | 2026-09-01 | https://www.sec.gov/Archives/edgar/data/1614178/000162828026059706/ex993q2fy27productupdatepr.htm | "AI visibility" |
| Yext, Inc.  (YEXT)  (CIK 0001614178) | 8-K | 2026-09-01 | https://www.sec.gov/Archives/edgar/data/1614178/000162828026059706/ex992q2fy27shareholderlett.htm | "AI visibility"; "answer engines" |
| Yiren Digital Ltd.  (YRD)  (CIK 0001631761) | 20-F | 2025-04-28 | https://www.sec.gov/Archives/edgar/data/1631761/000141057825000931/yrd-20241231x20f.htm | "LLMs" "referral" |
| Yiren Digital Ltd.  (YRD)  (CIK 0001631761) | 20-F | 2026-04-29 | https://www.sec.gov/Archives/edgar/data/1631761/000121390026049159/ea0287206-20f_yirendigi.htm | "LLM" "referral"; "LLMs" "referral" |
| Youdao, Inc.  (DAO)  (CIK 0001781753) | 20-F | 2025-04-15 | https://www.sec.gov/Archives/edgar/data/1781753/000119312525080651/d758034d20f.htm | "large language models" "organic traffic" |
| ZILLOW GROUP, INC.  (Z, ZG)  (CIK 0001617640) | 8-K | 2025-10-30 | https://www.sec.gov/Archives/edgar/data/1617640/000161764025000149/exhibit993.htm | "ChatGPT" "traffic" |
| ZILLOW GROUP, INC.  (Z, ZG)  (CIK 0001617640) | 8-K | 2026-05-06 | https://www.sec.gov/Archives/edgar/data/1617640/000161764026000038/exhibit992.htm | "AI Mode" "traffic" |
| ZILLOW GROUP, INC.  (Z, ZG)  (CIK 0001617640) | 8-K | 2026-08-05 | https://www.sec.gov/Archives/edgar/data/1617640/000161764026000050/exhibit992.htm | "AI Mode" "traffic"; "LLMs" "referral" |
| ZIPRECRUITER, INC.  (ZIP)  (CIK 0001617553) | 10-K | 2025-02-25 | https://www.sec.gov/Archives/edgar/data/1617553/000161755325000011/zip-20241231.htm | "large language models" "organic traffic" |
| ZIPRECRUITER, INC.  (ZIP)  (CIK 0001617553) | 8-K | 2026-02-25 | https://www.sec.gov/Archives/edgar/data/1617553/000161755326000015/ex992-q42025shareholderl.htm | "AI discovery" |
| ZIPRECRUITER, INC.  (ZIP)  (CIK 0001617553) | 8-K | 2026-05-07 | https://www.sec.gov/Archives/edgar/data/1617553/000161755326000030/q12026shareholderletter-.htm | "AI assistants" "traffic"; "ChatGPT" "traffic" |
| Zedge, Inc.  (ZDGE)  (CIK 0001667313) | 10-K | 2025-10-28 | https://www.sec.gov/Archives/edgar/data/1667313/000121390025103098/ea0262035-10k_zedge.htm | "AI Overviews" "traffic"; "ChatGPT" "referral"; "ChatGPT" "traffic"; "LLM" "referral"; "LLMs" "referral"; "generative AI" "referral traffic"; "large language models" "organic traffic" |
| Zedge, Inc.  (ZDGE)  (CIK 0001667313) | 10-Q | 2025-12-12 | https://www.sec.gov/Archives/edgar/data/1667313/000121390025121203/ea0268775-10q_zedge.htm | "ChatGPT" "traffic" |
| Zedge, Inc.  (ZDGE)  (CIK 0001667313) | 10-Q | 2026-03-16 | https://www.sec.gov/Archives/edgar/data/1667313/000121390026028295/ea0281041-10q_zedge.htm | "AI platforms" "referrals"; "ChatGPT" "traffic" |
| Zedge, Inc.  (ZDGE)  (CIK 0001667313) | 10-Q | 2026-06-12 | https://www.sec.gov/Archives/edgar/data/1667313/000121390026068278/ea0293880-10q_zedge.htm | "AI platforms" "referrals"; "ChatGPT" "traffic" |
| Zenvia Inc.  (ZENV)  (CIK 0001836934) | 20-F | 2025-05-16 | https://www.sec.gov/Archives/edgar/data/1836934/000155485525000506/zenv-20241231.htm | "ChatGPT" "referral" |
| Zeta Global Holdings Corp.  (ZETA)  (CIK 0001851003) | 10-K | 2026-02-25 | https://www.sec.gov/Archives/edgar/data/1851003/000119312526068598/zeta-20251231.htm | "generative engine optimization" |
| Zhihu Inc.  (ZH)  (CIK 0001835724) | 6-K | 2025-03-26 | https://www.sec.gov/Archives/edgar/data/1835724/000110465925027991/tm2510477d1_ex99-2.pdf | "AI search" "conversion" |
| Zhihu Inc.  (ZH)  (CIK 0001835724) | 6-K | 2025-04-15 | https://www.sec.gov/Archives/edgar/data/1835724/000110465925034875/tm2512283d1_ex99-2.pdf | "AI search" "conversion"; "AI search" "traffic"; "AI-powered search" "traffic" |
| Zhihu Inc.  (ZH)  (CIK 0001835724) | 20-F | 2025-04-15 | https://www.sec.gov/Archives/edgar/data/1835724/000141057825000729/zh-20241231x20f.htm | "AI search" "conversion"; "AI search" "traffic"; "AI-powered search" "traffic" |
| Zhihu Inc.  (ZH)  (CIK 0001835724) | 6-K | 2025-04-15 | https://www.sec.gov/Archives/edgar/data/1835724/000110465925034875/tm2512283d1_ex99-1.pdf | "AI search" "conversion" |
| Zhihu Inc.  (ZH, ZHIHF)  (CIK 0001835724) | 6-K | 2025-08-27 | https://www.sec.gov/Archives/edgar/data/1835724/000110465925083400/tm2524489d1_ex99-2.pdf | "AI search engines" "increase"; "AI search" "conversion" |
| Zhihu Inc.  (ZH, ZHIHF)  (CIK 0001835724) | 6-K | 2025-09-10 | https://www.sec.gov/Archives/edgar/data/1835724/000110465925088857/tm2525764d1_ex99-1.pdf | "AI search engines" "increase"; "AI search" "conversion" |
| Zhihu Inc.  (ZH, ZHIHF)  (CIK 0001835724) | 6-K | 2026-03-25 | https://www.sec.gov/Archives/edgar/data/1835724/000110465926034208/tm269796d1_ex99-2.pdf | "AI search engines" "increase"; "AI search" "conversion" |
| Zhihu Inc.  (ZH, ZHIHF)  (CIK 0001835724) | 6-K | 2026-04-17 | https://www.sec.gov/Archives/edgar/data/1835724/000110465926044609/tm2611950d1_ex99-2.pdf | "AI assistants" "traffic"; "AI search" "conversion"; "AI search" "traffic"; "LLM" "referral"; "LLMs" "referral" |
| Zhihu Inc.  (ZH, ZHIHF)  (CIK 0001835724) | 20-F | 2026-04-17 | https://www.sec.gov/Archives/edgar/data/1835724/000110465926044557/zh-20251231x20f.htm | "AI search" "conversion"; "AI search" "traffic"; "AI-powered search" "traffic" |
| Zhihu Inc.  (ZH, ZHIHF)  (CIK 0001835724) | 6-K | 2026-04-17 | https://www.sec.gov/Archives/edgar/data/1835724/000110465926044609/tm2611950d1_ex99-1.pdf | "AI search engines" "increase"; "AI search" "conversion" |
| Zoom Communications, Inc.  (ZM)  (CIK 0001585521) | 10-K | 2025-02-28 | https://www.sec.gov/Archives/edgar/data/1585521/000158552125000042/zm-20250131.htm | "LLMs" "referral" |
| Zoom Communications, Inc.  (ZM)  (CIK 0001585521) | 10-Q | 2025-05-23 | https://www.sec.gov/Archives/edgar/data/1585521/000158552125000090/zm-20250430.htm | "LLMs" "referral" |
| Zoom Communications, Inc.  (ZM)  (CIK 0001585521) | 10-Q | 2025-08-22 | https://www.sec.gov/Archives/edgar/data/1585521/000158552125000141/zm-20250731.htm | "LLMs" "referral" |
| Zoom Communications, Inc.  (ZM)  (CIK 0001585521) | 10-Q | 2025-11-25 | https://www.sec.gov/Archives/edgar/data/1585521/000158552125000202/zm-20251031.htm | "LLMs" "referral" |
| Zoom Communications, Inc.  (ZM)  (CIK 0001585521) | 10-K | 2026-02-27 | https://www.sec.gov/Archives/edgar/data/1585521/000158552126000030/zm-20260131.htm | "LLMs" "referral" |
| Zoom Communications, Inc.  (ZM)  (CIK 0001585521) | 10-Q | 2026-05-22 | https://www.sec.gov/Archives/edgar/data/1585521/000158552126000071/zm-20260430.htm | "LLMs" "referral" |
| Zoom Communications, Inc.  (ZM)  (CIK 0001585521) | 10-Q | 2026-08-26 | https://www.sec.gov/Archives/edgar/data/1585521/000158552126000121/zm-20260731.htm | "LLMs" "referral"; "agentic search" |
| ZoomInfo Technologies Inc.  (GTM)  (CIK 0001794515) | 10-K | 2026-02-12 | https://www.sec.gov/Archives/edgar/data/1794515/000179451526000012/zi-20251231.htm | "AI-powered search" "traffic" |
| Zscaler, Inc.  (ZS)  (CIK 0001713683) | 10-K | 2025-09-11 | https://www.sec.gov/Archives/edgar/data/1713683/000171368325000158/zs-20250731.htm | "AI discovery"; "ChatGPT" "traffic" |
| eHealth, Inc.  (EHTH)  (CIK 0001333493) | 10-K | 2026-02-26 | https://www.sec.gov/Archives/edgar/data/1333493/000133349326000010/ehth-20251231.htm | "AI platforms" "referrals" |
| eHealth, Inc.  (EHTH)  (CIK 0001333493) | 10-Q | 2026-05-07 | https://www.sec.gov/Archives/edgar/data/1333493/000133349326000027/ehth-20260331.htm | "AI platforms" "referrals" |
| eHealth, Inc.  (EHTH)  (CIK 0001333493) | 10-Q | 2026-08-05 | https://www.sec.gov/Archives/edgar/data/1333493/000133349326000036/ehth-20260630.htm | "AI platforms" "referrals" |
| eXp World Holdings, Inc.  (EXPI)  (CIK 0001495932) | 10-Q | 2025-11-06 | https://www.sec.gov/Archives/edgar/data/1495932/000110465925107719/expi-20250930xex10d3.htm | "AI platforms" "referrals" |
| eXp World Holdings, Inc.  (EXPI)  (CIK 0001495932) | 10-K | 2026-02-24 | https://www.sec.gov/Archives/edgar/data/1495932/000110465926019145/expi-20251231xex10d14.htm | "AI platforms" "referrals" |
| iBio, Inc.  (IBIO)  (CIK 0001420720) | 8-K | 2025-01-10 | https://www.sec.gov/Archives/edgar/data/1420720/000142072025000003/ibio-20250110xex99d1.htm | "AI discovery" |
| iBio, Inc.  (IBIO)  (CIK 0001420720) | 8-K | 2025-04-08 | https://www.sec.gov/Archives/edgar/data/1420720/000142072025000018/ibio-20250408xex99d1.htm | "AI discovery" |
| iBio, Inc.  (IBIO)  (CIK 0001420720) | 8-K | 2025-08-18 | https://www.sec.gov/Archives/edgar/data/1420720/000110465925079816/tm2523706d1_8k.htm | "AI discovery" |
| iBio, Inc.  (IBIO)  (CIK 0001420720) | 10-K | 2025-09-05 | https://www.sec.gov/Archives/edgar/data/1420720/000155837025011888/ibio-20250630x10k.htm | "AI discovery" |
| iBio, Inc.  (IBIO)  (CIK 0001420720) | 10-K | 2026-08-28 | https://www.sec.gov/Archives/edgar/data/1420720/000142072026000020/ibio-20260731x10k.htm | "AI discovery" |
| iHuman Inc.  (IH)  (CIK 0001814423) | 20-F | 2025-04-28 | https://www.sec.gov/Archives/edgar/data/1814423/000141057825000944/ih-20241231x20f.htm | "large language models" "organic traffic" |
| iHuman Inc.  (IH)  (CIK 0001814423) | 20-F | 2026-04-24 | https://www.sec.gov/Archives/edgar/data/1814423/000110465926048541/ih-20251231x20f.htm | "large language models" "organic traffic" |
| trivago N.V.  (TRVG)  (CIK 0001683825) | 20-F | 2025-02-27 | https://www.sec.gov/Archives/edgar/data/1683825/000168382525000013/trvg-20241231.htm | "ChatGPT" "bookings"; "ChatGPT" "referral"; "ChatGPT" "traffic"; "Perplexity" "traffic" |
| trivago N.V.  (TRVG)  (CIK 0001683825) | 20-F | 2026-02-26 | https://www.sec.gov/Archives/edgar/data/1683825/000168382526000006/trvg-20251231.htm | "ChatGPT" "bookings"; "ChatGPT" "referral"; "ChatGPT" "traffic"; "LLM" "referral"; "LLMs" "referral"; "Perplexity" "traffic" |

## Pull notes — mechanical only

- A forms filter containing a slash (10-K/A, S-1/A) made EFTS return a truncated set; the final filter omits slashed forms. EFTS still returned S-1/A, 8-K/A, DEF 14A, DRS/A and ARS documents under the root forms.
- Two queries returned HTTP 500 on count and were not collected: '"ChatGPT" "sign-ups"' and '"from ChatGPT"'. Per-CIK calls that errored: AXP, COF ('AI search'); EVER ('ChatGPT'); SOFI, ELF ('AI Overviews'); NRDS ('LLM'); ULTA, SOFI, DOCN ('answer engine').
- Sentence filter: AI term within 160 characters of an outcome term, sentence also containing a percent, multiple or direction word. Security-product uses of 'AI visibility' (Netskope, Fortinet, Check Point, N-able) and network-traffic uses of 'LLM traffic' (Ribbon) returned as hits and are kept in the hit list.
- Set 2 filtered sentences not already in set 1 are carried in the context-window section (High Roller, Commerce.com, Locafy 6-K, ZoomInfo) or the hit list.
- No login, no credential. Fetch rate held at or below about six requests per second.
