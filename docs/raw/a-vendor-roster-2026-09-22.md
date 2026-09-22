# Vendor roster — discovery sweep — P3-c0

```yaml
source:          discovery sweep over channels C13–C16, C65, C67, review sites, job boards, HN, conference agendas
url_or_doc_id:   multi-channel — see discovery log below for every URL and query
pull_date:       2026-09-22
pull_method:     fetch (WebSearch/WebFetch), browser extension (g2.com), API (SEC EDGAR full-text, HN Algolia, UK Companies House)
pull_purpose:    evidence about a number (vendor roster composition and count)
tier:            mixed 2-6 — see tier column in the roster table; each row's tier is the tier of its weakest qualifying source per docs/method/trust-rubric.md
tier_reason:     roster rows mixing an SEC/Companies House filing (tier 2) with a G2 category listing (tier 5) are tiered at the weaker source per the task's own rule; G2/OMR self-submitted profiles with no n or verified-buyer flag sit at tier 5-6
source_label:    mixed — filed (SEC EDGAR, UK Companies House), analyst-derived (funding trackers, G2 review counts), company-stated (press releases), vendor-reported (G2/OMR/Crunchbase self-listings, held not rostered on their own)
lane:            A
sub_market:      mixed — organic recommendation | paid placement | agentic commerce | incumbent bundling | agency — see sub-market column
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        partial — one or more pages per source; per-row citations carry their own URL and date
```

## 1. Discovery log

Every query run 2026-09-22, verbatim, with the surface and an approximate count of distinct company/product names the results screened. "Screened" = distinct names encountered in the returned results, not the count of search-result links.

### 1a. Web search (WebSearch tool, US-only surface per query-book.md caveat)

| # | Query (verbatim) | Surface | Date | Names screened (approx) |
|---|---|---|---|---|
| 1 | `"AI visibility" platform pricing -"best" -"top" -"alternatives" 2026` | web search | 2026-09-22 | 9 listicle publishers, 0 new vendor names beyond known seeds |
| 2 | `"generative engine optimization" platform pricing 2026` | web search | 2026-09-22 | 9 listicle publishers |
| 3 | `"answer engine optimization" tool platform 2026` | web search | 2026-09-22 | Profound, Scrunch AI, Otterly.AI, Athena HQ, Goodie AI, Peec AI, Semrush, Ahrefs Brand Radar, Bluefish AI |
| 4 | `AEO LLMO "AI SEO" software platform 2026` | web search | 2026-09-22 | HubSpot AEO Grader, Rank Prompt |
| 5 | `"AI visibility" (raises OR "Series A" OR "Series B" OR seed) 2026 -"best"` | web search | 2026-09-22 | 0 vendor names — general AI-funding market coverage only |
| 6 | `"generative engine optimization" (raises OR "Series A" OR funding) 2026` | web search | 2026-09-22 | Profound ($96M Series C), GenerativeX ($4M Series A — later screened out), Promptwatch (€6M seed), Azoma ($4M pre-Series A), Peec AI ($21M Series A, LinkedIn pointer) |
| 7 | `site:eu-startups.com "AI visibility" raises` | web search, pinned | 2026-09-22 | geoSurge, Searchable |
| 8 | `site:pymnts.com "AI visibility" funding` | web search, pinned | 2026-09-22 | geoSurge (via a general AI-funding tag page) |
| 9 | `site:linkedin.com/jobs "generative engine optimization"` | web search, pinned | 2026-09-22 | KNWN App, ChatGPT Jobs listing (recruiter, not a vendor), Akamai, Busylike, Right Side Up, Albusleo Ventures, Globy — job postings, not vendors |
| 10 | `"AI search visibility" platform startup 2026` | web search | 2026-09-22 | Profound, LLMrefs, Otterly, Geneo, ZipTie, Rankscale (listicle context) |
| 11 | `site:crunchbase.com "AI visibility" organization` | web search, pinned | 2026-09-22 | AI Visibility Rank, Visibly, BrandViz.ai, Appear on AI, Profound, GetFoundOnAI.com |
| 12 | `site:crunchbase.com "generative engine optimization" organization` | web search, pinned | 2026-09-22 | Optivara, LovedByAI, Optimize Ai Search, Growthner, Profit Engine Marketing, AuthorityTech, Discovered Labs, GenRankEngine |
| 13 | `"AI ads management platform" ChatGPT Perplexity Copilot agency tool 2026` | web search | 2026-09-22 | Ryze AI, AdStellar, Optmyzr, Trapica (paid/agency-tooling side, all screened — thin) |
| 14 | `"agentic commerce" platform merchant feed optimization tool vendor 2026` | web search | 2026-09-22 | Feedonomics/Commerce, commercetools, Salsify, Syndigo, Productsup, Shopify Agentic Storefronts, BigCommerce/Commerce |
| 15 | `"product feed" AI shopping ChatGPT Perplexity optimization software company 2026` | web search | 2026-09-22 | Alhena, DataFeedWatch, WRKNG Digital, Tinuiti, Bowler Digital, Store Growers (mostly agencies) |
| 16 | `marketingaiinstitute.com agenda 2026 speaker GEO AI visibility` | web search, pinned | 2026-09-22 | MAICON 2026 (event, no vendor names surfaced beyond a practitioner speaker) |
| 17 | `"GEO conference" 2026 speakers sponsors AI visibility` | web search | 2026-09-22 | GEO Conference NYC/SF 2026 — speakers are brand-side (Marriott, AT&T, Philip Morris), no vendor sponsors named |
| 18 | `"AI visibility" agency "generative engine optimization" retainer pricing service` | web search | 2026-09-22 | 9 pricing-guide listicle publishers, no new vendor names |
| 19 | `Ahrefs Brand Radar Semrush AI Toolkit Similarweb AI search product launch 2026` | web search | 2026-09-22 | Ahrefs Brand Radar, Semrush AI Toolkit, "Semrush — By Adobe" claim |
| 20 | `HubSpot AEO Yext AI visibility feature launch 2026` | web search | 2026-09-22 | HubSpot AEO, Yext, GoShine (acquired by Yext) |
| 21 | `Locafy REZOLVE AI PLC "answer engine optimization" investor filing 2026` | web search | 2026-09-22 | Locafy (Poseidon AEO platform), REZOLVE AI PLC (unclear fit) |
| 22 | `"Change Agents Corporation" "generative engine optimization" filing` | web search | 2026-09-22 | Change Agents Corporation / Avalon Quantum AI |
| 23 | `Onfolio Holdings "generative engine optimization" S-1 subsidiary` | web search | 2026-09-22 | Onfolio Holdings / Pace Generative LLC |
| 24 | `Glidelogic Corp "generative engine optimization" 10-K` | web search | 2026-09-22 | Glidelogic Corp (discontinued — screened out) |
| 25 | `geoSurge AI visibility funding second source techcrunch sifted` | web search | 2026-09-22 | geoSurge — corroborating sources (PYMNTS, citybiz, retailtechinnovationhub) |
| 26 | `Searchable AI visibility London funding sifted techcrunch` | web search | 2026-09-22 | Searchable — corroborating sources (UKTN, techfundingnews, ventureburn, Yahoo/Headline) |
| 27 | `GenerativeX company "generative engine optimization" what does it sell` | web search | 2026-09-22 | GenerativeX confirmed off-topic — Tokyo generative-AI consulting firm, not a GEO vendor (screened out) |
| 28 | `Brandlight AI visibility platform G2 review OR job posting OR LinkedIn` | web search | 2026-09-22 | Brandlight AI — G2 listing, careers page, third-party reviews |
| 29 | `Sitefire YC W26 AI visibility second source` | web search | 2026-09-22 | Sitefire — YC company page, Product Hunt, founderland.ai |
| 30 | `Yext GoShine acquisition AI search visibility 2026` | web search | 2026-09-22 | Yext, GoShine (subsumed into Yext's "Brand Scout") |
| 31 | `site:omr.com/en/reviews category ai GEO AI visibility software` | web search, pinned | 2026-09-22 | Finseo, Rankscale.ai, Quaro, Kambrium, Peec AI, GEOlyze, Temso AI |
| 32 | `Peec AI Series A funding source techcrunch sifted 2026` | web search | 2026-09-22 | Peec AI — Sifted x2, TechCrunch x2, Yahoo Finance |
| 33 | `Promptwatch AI visibility seed funding second source 2026` | web search | 2026-09-22 | Promptwatch — Vestbee, mainsights.io, Sifted, consultancy.eu, thesaasnews |
| 34 | `site:g2.com "AI Visibility" category software` | web search, pinned | 2026-09-22 | pointed to the two live G2 category URLs (below) |
| 35 | `g2.com category "Generative Engine Optimization" OR "AI Search" list of products` | web search, pinned | 2026-09-22 | AthenaHQ, Ktau.ai, Blym AI, VISIBLE™, Writesonic |
| 36 | `Rankscale.ai OR Finseo OR Kambrium OR "GEOlyze" OR Quaro funding OR launch OR LinkedIn 2026` | web search | 2026-09-22 | Rankscale.ai (getlatka.com revenue profile — independent second source) |
| 37 | `"AthenaHQ" OR "Athena HQ" AI visibility funding second source 2026` | web search | 2026-09-22 | AthenaHQ — Crunchbase, PitchBook, Tracxn |
| 38 | `"Otterly.ai" OR "Scrunch AI" OR "Goodie AI" funding OR G2 OR LinkedIn jobs 2026` | web search | 2026-09-22 | Otterly.AI (Tracxn), Scrunch AI/Sitecore, Goodie AI (thin — no G2/Capterra reviews) |
| 39 | `agency "generative engine optimization" OR "AI visibility" service list -"best" -"top"` | web search | 2026-09-22 | 9 agency listicles naming Go Fish Digital, iPullRank, Relevance, Siege Media, Omniscient Digital, Perrill, Single Grain, Spicy Margarita, EWR Digital, SeoProfy, Digital Elevator, Graphite, Directive, Animalz, First Page Sage |
| 40 | `"Ahrefs" "Brand Radar" launch AI visibility press coverage` | web search | 2026-09-22 | Ahrefs Brand Radar — Businesswire, Yahoo Finance |
| 41 | `Birdeye SOCi Nasdaq ticker AI visibility reputation "answer engine"` | web search | 2026-09-22 | Birdeye, SOCi |
| 42 | `"Muck Rack" AI visibility citation feature launch 2026` | web search | 2026-09-22 | Muck Rack — GlobeNewswire, syndicated copies (National Law Review, citybiz, Manila Times — same release) |
| 43 | `"Conductor" OR "BrightEdge" OR "Onclusive" "AI visibility" OR "answer engine" feature launch press 2026` | web search | 2026-09-22 | Conductor (AgentStack), BrightEdge (AI Hyper Cube), Onclusive (no launch found) |
| 44 | `Quattr AirOps funding OR launch AI SEO content platform 2026` | web search | 2026-09-22 | Quattr, AirOps ($40M Series B) |
| 45 | `"RankPrompt" OR "Qwairy" OR "Waikay" OR "Hall" AI visibility funding OR LinkedIn launch` | web search | 2026-09-22 | RankPrompt (PRNewswire, martechseries), Waikay, Hall AI |
| 46 | `Sitecore acquires Scrunch AI press release 2026` | web search | 2026-09-22 | Sitecore/Scrunch — Bloomberg, Sitecore newsroom, PRNewswire, CMSWire, Pulse2, Yahoo |
| 47 | `Birdeye "generative engine optimization" press release launch independent` | web search | 2026-09-22 | Birdeye — PRNewswire (Search AI launch, 2025-09-03) |
| 48 | `"BrightEdge Prism" OR "AI Agent Insights" BrightEdge launch press release 2026` | web search | 2026-09-22 | BrightEdge — GlobeNewswire, Yahoo Finance, martechcube |
| 49 | `AirOps Series B $40 million funding TechCrunch 2026` | web search | 2026-09-22 | AirOps — Businesswire, Pulse2, Yahoo, Crunchbase funding-round page |
| 50 | `Quattr funding round investors techcrunch OR crunchbase news` | web search | 2026-09-22 | **not run — session WebSearch budget exhausted (200/200)** |
| 51 | `geoSurge OR Searchable OR Brandlight companies house UK filing` | web search | 2026-09-22 | **not run — session WebSearch budget exhausted (200/200)**, superseded by direct Companies House fetch below |

### 1b. Registry / filing / API fetches (WebFetch and browser extension)

| # | Query / target | Surface | Date | Result |
|---|---|---|---|---|
| 52 | `efts.sec.gov` full-text: `"generative engine optimization"`, 2026-01-01→2026-09-22 | SEC EDGAR full-text API, fetch | 2026-09-22 | 40 filing hits across ~24 distinct filers |
| 53 | `efts.sec.gov` full-text: `"AI visibility"`, 2026-01-01→2026-09-22 | SEC EDGAR full-text API, fetch | 2026-09-22 | HTTP 500 — endpoint did not return; not re-tried under this session's remaining budget |
| 54 | `efts.sec.gov` full-text: `"answer engine optimization"`, 2026-01-01→2026-09-22 | SEC EDGAR full-text API, fetch | 2026-09-22 | 14 filing hits across 9 distinct filers |
| 55 | `hn.algolia.com/api/v1/search?query=generative+engine+optimization` | HN Algolia API, fetch | 2026-09-22 | 20 stories screened |
| 56 | `hn.algolia.com/api/v1/search?query=AI%20visibility%20platform` | HN Algolia API, fetch | 2026-09-22 | 12 stories screened |
| 57 | `g2.com/categories/ai-search-visibility` | browser extension | 2026-09-22 | 404 — wrong slug |
| 58 | `g2.com/categories/answer-engine-optimization-aeo`, page 1 | browser extension | 2026-09-22 | 15 products read (631 listings total) |
| 59 | `g2.com/categories/answer-engine-optimization-aeo?page=2` | browser extension | 2026-09-22 | 15 products read |
| 60 | `g2.com/categories/ai-search-visibility-optimization-tools`, page 1 | browser extension | 2026-09-22 | 15 products read (539 listings total) |
| 61 | `find-and-update.company-information.service.gov.uk/search/companies?q=geoSurge` | UK Companies House, fetch | 2026-09-22 | GEOSURGE LIMITED, company no. 16249592, active, incorporated 2025-02-13 |
| 62 | `find-and-update.company-information.service.gov.uk/search/companies?q=Searchable` | UK Companies House, fetch | 2026-09-22 | SEARCHABLE LIMITED, company no. 16579753, active, incorporated 2025-07-14 |
| 63 | `find-and-update.company-information.service.gov.uk/search/companies?q=Brandlight` | UK Companies House, fetch | 2026-09-22 | No matching entity — BRANDLIGHT FOUNDATION and BRANDLIGHTING LIMITED are unrelated UK entities; Brandlight AI (the vendor) not found on this register |

G2's AEO category and AI-Search-Visibility category are two distinct category pages on the one publisher (g2.com) and are counted as **one source** per the roster rule's "two pages by the same publisher... count once." Pagination beyond page 2 of AEO (43 total pages, 631 listings) and page 1 of AI-Search-Visibility (36 total pages, 539 listings) was not read — the category plainly contains many generic SEO/reputation/PR tools tagged into it by G2's own AI classifier, not solely dedicated GEO vendors, and reading it exhaustively was not attempted; page 3+ is recorded as **unknown — checked g2.com page 1-2 of each category only, 2026-09-22**.

## 2. Roster — rostered vendors (26), ordered by source count descending then alphabetically

| # | Name | Website (as found) | Sub-market | Limb qualified | Sources (2+ independent, or filing/funding) with URL and date | Category page / filing that named it | HQ country (if stated) | What the source says it sells (one line) |
|---|---|---|---|---|---|---|---|---|
| 1 | Scrunch AI (acquired by Sitecore) | scrunch.com | organic → now incumbent bundling | (a) 7 sources | Bloomberg, `bloomberg.com/news/articles/2026-06-03/sitecore-said-to-acquire-scrunch-for-225-million`, 2026-06-03 (deal value $225M); Sitecore newsroom, `sitecore.com/company/newsroom/press-releases/2026/06/sitecore-acquires-scrunch...`, 2026-06-03; PRNewswire, `prnewswire.com/news-releases/sitecore-acquires-scrunch-to-help-brands-influence-discovery-and-buying-decisions-in-the-ai-search-era-302790214.html`, 2026-06-03; CMSWire, `cmswire.com/digital-experience/sitecore-acquires-scrunch-to-boost-ai-search-visibility/`, 2026; Pulse2, `pulse2.com/sitecore-acquires-ai-search-optimization-platform-scrunch...`, 2026; Yahoo Finance, `finance.yahoo.com/sectors/technology/articles/sitecore-acquires-scrunch-help-brands-130000012.html`, 2026-06; G2, `g2.com/categories/answer-engine-optimization-aeo?page=2`, read 2026-09-22 | Sitecore acquisition press release; G2 AEO category page 2 ("Scrunch AI — By Sitecore", 4.6/5, 73 reviews) | not stated | "Scrunch's insights, recommendation capabilities, and Agent Experience Platform (AXP)... helps brands understand and improve how they appear in AI search" — Sitecore newsroom |
| 2 | Searchable | searchable.com | organic | (a)+(b) 7 sources | EU-Startups, `eu-startups.com/2026/05/londons-searchable-raises-e11-9-million...`, 2026-05; EU-Startups, `eu-startups.com/2025/12/searchable-raises-e3-4-million...`, 2025-12 (counted with the above as one publisher); UKTN, `uktech.news/ai/ai-search-visibility-startup-secures-3m-investment-20251203`, 2025-12-03; techfundingnews.com, `techfundingnews.com/searchable-10-3m-funding-headline-ai-search-seo/`, 2026; ventureburn.com, `ventureburn.com/searchable-raises-10-3m-to-expand-ai-search-platform/`, 2026; Yahoo Finance, `finance.yahoo.com/sectors/technology/articles/searchable-secures-14m-headline-85m-130000392.html`, 2026; UK Companies House, SEARCHABLE LIMITED no. 16579753, incorporated 2025-07-14, read 2026-09-22; G2, `g2.com/categories/answer-engine-optimization-aeo?page=2`, read 2026-09-22 | EU-Startups funding article; G2 AEO category page 2 (4.8/5, 101 reviews) | United Kingdom (London) — UKTN, EU-Startups | "gives marketers insights into how their content is read, ranked and recommended by large language models... a 'real-time window' into visibility inside AI search engines" — UKTN/EU-Startups |
| 3 | AirOps | airops.com | incumbent bundling (content-ops platform with AEO features) | (a) 5 sources | Businesswire, `businesswire.com/news/home/20251110823725/en/AirOps-Raises-$40M-to-Redefine-How-Brands-Compete-in-the-Era-of-AI-Search`, 2025-11-10; Pulse2, `pulse2.com/airops-40-million-series-b-raised-for-advancing-growth-as-brands-adapt-to-ai-search/`, 2025-11; Yahoo Finance, `finance.yahoo.com/news/airops-raises-40-million-series-113014119.html`, 2025-11; Crunchbase funding-round page, `crunchbase.com/funding_round/airops-1e31-series-b--0783b5af`, read 2026-09-22; G2, `g2.com/categories/answer-engine-optimization-aeo`, read 2026-09-22 | Businesswire Series B release; G2 AEO category page 1 (4.7/5, 134 reviews) | New York / San Francisco — Yahoo Finance | "AI-powered content operations platform"; "$40 million Series B... to rethink marketing in the age of AI" — Yahoo Finance/Businesswire |
| 4 | geoSurge | geosurge.ai | organic | (a)+(b) 5 sources | EU-Startups, `eu-startups.com/2026/07/londons-geosurge-raises-e10-million-to-help-brands-understand-ai-generated-outputs/`, 2026-07; PYMNTS, `pymnts.com/news/investment-tracker/2026/geosurge-raises-12-million-to-help-brands-secure-ai-visibility`, 2026; citybiz, `citybiz.co/article/870365/geosurge-raises-12-million-seed-round-to-expand-ai-visibility-platform/`, 2026; retailtechinnovationhub.com, `retailtechinnovationhub.com/home/2026/7/6/london-based-ai-startup-geosurge-bags-12-million-in-seed-funding-round-led-by-albionvc`, 2026-07-06; UK Companies House, GEOSURGE LIMITED no. 16249592, incorporated 2025-02-13, read 2026-09-22 | EU-Startups/PYMNTS funding coverage; UK Companies House filing | United Kingdom (London) — Companies House, EU-Startups | "proprietary Corpus Engineering method targets how models like ChatGPT, Gemini and Claude internally learn and represent a brand over time" — retailtechinnovationhub.com |
| 5 | Peec AI | peec.ai | organic | (a) 5 sources | Sifted, `sifted.eu/articles/peec-ai-raises-21m-series-a`, 2025-11; Sifted, `sifted.eu/articles/peec-ai-fundraise-new-valuation`, 2026 (same publisher, counted with above as one); TechCrunch, `techcrunch.com/2025/11/17/as-consumers-ditch-google-for-chatgpt-peec-ai-raises-21m-to-help-brands-adapt/`, 2025-11-17; TechCrunch, `techcrunch.com/2026/05/23/peec-one-of-berlins-rising-startups-more-than-doubled-annualized-revenue-in-months-to-10m-sources-say/`, 2026-05-23 (same publisher, counted with above as one); Yahoo Finance, `finance.yahoo.com/sectors/technology/articles/peec-ai-hits-10m-arr-140000315.html`, 2026; OMR Reviews, `omr.com/en/reviews/product/peec-ai`, read 2026-09-22; G2, `g2.com/categories/answer-engine-optimization-aeo`, read 2026-09-22 | Sifted/TechCrunch funding coverage; G2 AEO category page 1 (4.7/5, 21 reviews) | Berlin, Germany — TechCrunch ("Berlin's rising startups") | "help brands win in AI search"; raised $21M Series A backed by Singular and Antler — Sifted |
| 6 | Promptwatch | promptwatch.com | organic | (a) 5 sources | Sifted, `sifted.eu/articles/promptwatch-raises-seed-round`, 2026-07; Vestbee, `vestbee.com/insights/articles/promptwatch-raises-6-m`, 2026; mainsights.io, `mainsights.io/ma-news/netherlands-based-ai-search-optimization-platform-promptwatch-raises-eur-6m-seed-capital...`, 2026; consultancy.eu, `consultancy.eu/news/14076/promptwatch-secures-6-million-growth-capital-with-support-from-torqpartners`, 2026; thesaasnews.com, `thesaasnews.com/news/promptwatch-raises-6m-seed/`, 2026 | Sifted "Exclusive: Peec rival Promptwatch raises €6m seed round" | Amsterdam, Netherlands — Sifted, mainsights.io | "helps brands and agencies understand, optimize and take action on their visibility across AI models such as ChatGPT, Claude and Perplexity" — Sifted |
| 7 | Profound | profound.com (seed found as tryprofound.com) | organic | (a)+(b) 4 sources | everything-pr.com, `everything-pr.com/profound-reaches-1-billion-valuation-with-96m-series-c-cementing-category-leadership-in-ai-search-marketing`, 2026-02; Crunchbase org profile, `crunchbase.com/organization/profound-1b0a`, read 2026-09-22; LinkedIn post referencing the Series B raise, `linkedin.com/posts/niall-moran-3523365a_nvidia-backed-ai-startup-profound-lands-series-activity-7361676221539053569-R15U`, 2026; G2, `g2.com/categories/answer-engine-optimization-aeo`, read 2026-09-22 | everything-pr.com Series C article ($96M, $1B valuation); G2 AEO category page 1, top-ranked (4.5/5, 1,129 reviews) | New York, NY — Crunchbase | "helps the world's biggest brands, including 10% of the Fortune 500, win more business from ChatGPT, Gemini, and other LLMs" — G2 product description |
| 8 | AthenaHQ | athenahq.ai | organic | (a) 4 sources | Crunchbase, `crunchbase.com/organization/athenahq`, read 2026-09-22; PitchBook, `pitchbook.com/profiles/company/759029-50`, read 2026-09-22; Tracxn, `tracxn.com/d/companies/athenahq/...`, read 2026-09-22; G2, `g2.com/categories/answer-engine-optimization-aeo?page=2`, read 2026-09-22 | Crunchbase/Tracxn/PitchBook funding profiles; G2 AEO category page 2 (4.9/5, 47 reviews) | San Francisco, CA — Tracxn | "GEO (generative engine optimization) SaaS solution for marketing, brand, and growth teams to improve their presence on AI Search such as ChatGPT, Perplexity, Gemini, Claude" — G2 |
| 9 | Conductor | conductor.com | incumbent bundling (enterprise SEO platform with AEO add-on) | (a) 3 sources | CMSWire, `cmswire.com/digital-experience/conductor-launches-agentstack-for-aeo/`, 2026-04; DemandGenReport, `demandgenreport.com/industry-news/news-brief/conductor-introduces-agentstack-to-scale-ai-search-visibility/52636/`, 2026-04; G2, `g2.com/categories/answer-engine-optimization-aeo`, read 2026-09-22 | CMSWire AgentStack launch article; G2 AEO category page 1 (4.5/5, 803 reviews) | not stated | AgentStack, billed as "the industry's only system of record for AEO" — CMSWire, 2026-04-01 launch |
| 10 | HubSpot AEO | hubspot.com | incumbent bundling | (a)+(b) 3 sources | SEC 10-K/ARS/DEF 14A (HUBS), filed 2026-02-11 / 2026-04-27, via `efts.sec.gov` full-text search on "answer engine optimization", read 2026-09-22; CMSWire, `cmswire.com/digital-experience/hubspot-launches-aeo-expands-ai-agents-at-spring-2026-spotlight/`, 2026; G2, `g2.com/categories/answer-engine-optimization-aeo`, read 2026-09-22 | SEC EDGAR full-text hit; hubspot.com/company-news/hubspot-aeo (vendor's own announcement, not used as a qualifying source); G2 AEO category page 1 (4.5/5, 142 reviews) | Cambridge, MA — SEC domestic filer | "the answer to showing up in AI search engines"; launched April 2026 — CMSWire |
| 11 | Onfolio Holdings / Pace Generative LLC | onfolio.com (parent, ONFO); subsidiary Pace Generative LLC | agency (public-company-owned) | (b) filing + 3 sources | SEC S-1/A, 10-K, 424B3 (ONFO), filed 2026-01-28 through 2026-09-18, via `efts.sec.gov` full-text search on "generative engine optimization", read 2026-09-22; Nasdaq press release, `nasdaq.com/press-release/onfolio-holdings-inc-subsidiary-pace-generative-drives-358-ai-traffic-improvement`, 2025; Yahoo Finance, `finance.yahoo.com/news/onfolio-holdings-ai-marketing-subsidiary-140000120.html`, 2025 | SEC EDGAR full-text hit; Nasdaq/Yahoo press coverage of subsidiary Pace Generative | United States — SEC domestic filer | Pace Generative "helps brands increase their visibility and traffic from AI answer engines, such as Google AI overviews, ChatGPT, Perplexity, and Grok... using traditional content marketing, SEO, and PR techniques, along with new proprietary methods" — Yahoo Finance/Nasdaq |
| 12 | RankPrompt | rankprompt.com | organic | (a) 3 sources | PRNewswire, `prnewswire.com/news-releases/rank-prompt-launches-as-pioneering-platform-to-optimize-brand-visibility-in-ai-search-engines-302481610.html`, 2026; Yahoo Finance (same release, counted with PRNewswire); martechseries.com, `martechseries.com/predictive-ai/ai-platforms-machine-learning/v7-launch-solidifies-rank-prompts-position-as-one-of-the-leading-ai-visibility-tools/`, 2026; G2, `g2.com/categories/answer-engine-optimization-aeo?page=2`, read 2026-09-22 | PRNewswire launch release; G2 AEO category page 2 (5/5, 33 reviews) | not stated | "AI Search Visibility, AEO & GEO Tracking"; helps businesses "understand if AI Assistants recommend their business" — rankprompt.com via martechseries |
| 13 | Sitefire | sitefire.ai | organic | (a) 3 sources | Y Combinator company page, `ycombinator.com/companies/sitefire`, read 2026-09-22; Product Hunt, `producthunt.com/products/sitefire-ai`, read 2026-09-22; founderland.ai, `founderland.ai/articles/yc-w26s-sitefire-launches-marketing-suite-for-ai-agent-disco-mna5r7pa`, 2026 | Y Combinator W26 batch page; Hacker News Launch HN thread, `news.ycombinator.com/item?id=47457472`, 2026-03-20 (36 points, 27 comments) | not stated | "Marketing suite for the agentic web"; "Automating actions to improve AI visibility" — YC company page |
| 14 | Yext | yext.com | incumbent bundling | (a)+(b) 3 sources | SEC 8-K / Q2 FY27 earnings release (YEXT), filed 2026, `sec.gov/Archives/edgar/data/1614178/000162828026059706/ex991q2fy27earningsrelease.htm`, read 2026-09-22; stocktitan.net, `stocktitan.net/news/YEXT/yext-announces-second-quarter-fiscal-2027-l02qowyjheuw.html`, 2026; G2, `g2.com/categories/answer-engine-optimization-aeo?page=2`, read 2026-09-22 | Yext SEC 8-K/earnings release naming the GoShine acquisition and "Brand Scout"; G2 AEO category page 2 (4.4/5, 1,125 reviews) | New York, NY — NYSE-listed | "completed its GoShine acquisition" and "expanded Scout with brand-level AI visibility" — stocktitan.net summarizing the Yext earnings release |
| 15 | Ahrefs (Brand Radar) | ahrefs.com | incumbent bundling | (a) 2 sources | Businesswire, `businesswire.com/news/home/20260120714417/en/Ahrefs-Launches-Custom-AI-Prompt-Tracking-for-Brand-Visibility`, 2026-01-20; Yahoo Finance (same release, counted with Businesswire); G2, `g2.com/categories/answer-engine-optimization-aeo?page=2`, read 2026-09-22 | Businesswire "Ahrefs Launches Custom AI Prompt Tracking for Brand Visibility"; G2 AEO category page 2 (4.5/5, 714 reviews) | not stated (Ahrefs HQ commonly cited as Singapore, not stated in a pulled source today — recorded unknown) | Brand Radar gives "a new way for teams to monitor how their brand appears in AI-generated answers across platforms like ChatGPT, Gemini, and Perplexity" — Businesswire |
| 16 | Birdeye | birdeye.com | incumbent bundling | (a) 2 sources | PRNewswire, `prnewswire.com/news-releases/birdeye-launches-search-ai-to-put-multi-location-brands-at-the-top-of-ai-answers-302544631.html`, 2025-09-03; G2, `g2.com/categories/ai-search-visibility-optimization-tools`, read 2026-09-22 | PRNewswire Search AI launch release; G2 AI Search Visibility Optimization Tools category page 1 (4.7/5, 4,234 reviews) | not stated | "Search AI to Put Multi-Location Brands at the Top of AI Answers" — PRNewswire, 2025-09-03 |
| 17 | Brandlight AI | brandlight.ai | organic | (a) 2 sources | G2, `g2.com/categories/answer-engine-optimization-aeo`, read 2026-09-22; funding coverage cluster (one announcement, four syndicated publishers per the roster rule's own counting clause) — pulse2.com, finance.yahoo.com, calcalistech.com, contentgrip.com, all 2026, counted once | G2 AEO category page 1 (4.9/5, 213 reviews); pulse2.com "Brandlight: $30 Million Series A Raised For Enterprise AI Visibility Platform" | not stated | "manage brand visibility across AI engines, providing tools to understand how AI perceives and portrays your brand" — G2 product description |
| 18 | BrightEdge | brightedge.com | incumbent bundling | (a) 2 sources | GlobeNewswire, `globenewswire.com/news-release/2026/03/10/3252895/0/en/BrightEdge-Launches-AI-Hyper-Cube-Pulling-Back-the-Curtain-on-How-Brands-Show-Up-in-AI-Search.html`, 2026-03-10; Yahoo Finance (same release, counted with GlobeNewswire); G2, `g2.com/categories/answer-engine-optimization-aeo`, read 2026-09-22 | GlobeNewswire AI Hyper Cube launch release; G2 AEO category page 1 (4.4/5, 842 reviews) | not stated | "AI Hyper Cube, Pulling Back the Curtain on How Brands Show Up in AI Search" — GlobeNewswire, 2026-03-10 |
| 19 | Change Agents Corporation / Avalon Quantum AI | changeagentscorp.com (CHGA) | organic | (b) filing + 1 source | SEC 8-K, 10-Q, S-1/A (CHGA), filed 2026-07-21 through 2026-09-18, via `efts.sec.gov` full-text search, read 2026-09-22; stocktitan.net, `stocktitan.net/sec-filings/CHGA/`, read 2026-09-22 | SEC EDGAR full-text hit naming "Generative Engine Optimization" under the Avalon Quantum AI segment | United States — SEC domestic filer | "AI software segment (agentic video generation and Generative Engine Optimization via Avalon Quantum AI)" — stocktitan.net summarizing CHGA's own filings; going-concern doubt disclosed in the same filings |
| 20 | Locafy (Poseidon) | locafy.com (LCFY) | organic | (b) filing + 1 source | SEC 6-K, `sec.gov/Archives/edgar/data/0001875547/000149315226031582/ex99-1.htm`, 2026; SEC F-3, `sec.gov/Archives/edgar/data/0001875547/000149315226035989/formf-3.htm`, 2026; investing.com, `ng.investing.com/news/stock-market-news/locafy-reports-strong-ai-search-results-ahead-of-june-platform-launch-93ch-2518818`, 2026 | SEC EDGAR full-text hit on "answer engine optimization" | not stated | "SaaS technology company specializing in location-based Search Engine Optimization (SEO) and Answer Engine Optimization (AEO) solutions"; flagship AEO platform "Poseidon" — investing.com summarizing the 6-K |
| 21 | Muck Rack | muckrack.com | incumbent bundling (PR/media-monitoring platform) | (a) 2 sources | GlobeNewswire, `globenewswire.com/news-release/2026/03/05/3250530/0/en/muck-rack-launches-ai-visibility-badges.html`, 2026-03-05 (syndicated at citybiz, National Law Review, Manila Times — same release, counted once); G2, `g2.com/categories/answer-engine-optimization-aeo?page=2`, read 2026-09-22 | GlobeNewswire "Muck Rack Launches AI Visibility Badges"; G2 AEO category page 2 (4.5/5, 527 reviews) | not stated | "AI Visibility Badges" built on "Generative Pulse... based on more than 15 million AI response citations" — GlobeNewswire, 2026-03-05 |
| 22 | Otterly.AI | otterly.ai | organic | (a) 2 sources | Tracxn, `tracxn.com/d/companies/otterlyai/...`, read 2026-09-22; G2, `g2.com/categories/answer-engine-optimization-aeo`, read 2026-09-22 | G2 AEO category page 1 (4.7/5, 54 reviews); Tracxn company profile | Santa Clara, CA — Tracxn | "cheapest honest way to find out whether AI engines mention you" — Tracxn/G2 review summary; unfunded per Tracxn |
| 23 | Quattr | quattr.com | incumbent bundling (SEO/content platform with AEO) | (a) 2 sources | G2, `g2.com/categories/answer-engine-optimization-aeo`, read 2026-09-22 (G2's own "Spring 2026 reports #1 rankings in AEO Results" cited via search); perpetualny.com case study, `perpetualny.com/case-study/quattr`, read 2026-09-22, independent of the vendor | G2 AEO category listing | Palo Alto, CA — searchinfluence.com summary of Quattr | "AI-native Search Visibility Platform... built for mid-market and enterprise brands competing in the age of generative search" — Quattr's own description, corroborated independently by perpetualny.com case study |
| 24 | Rankscale.ai | rankscale.ai | organic | (a) 2 sources | OMR Reviews, `omr.com/en/reviews/product/rankscale-ai`, read 2026-09-22; getlatka.com, `getlatka.com/companies/rankscale.ai`, read 2026-09-22, independent revenue profile | OMR Reviews GEO category page | Königstetten, Austria — getlatka.com | "SaaS platform for AI SEO, AI rank tracking, and Generative Engine Optimization (GEO Tools)"; ~$220K ARR, 2-person team per getlatka.com | 
| 25 | Semrush (AI Visibility Toolkit) | semrush.com | incumbent bundling | (a)+(b) 2 sources | SEC 10-K (SEMR), filed 2026-03-02, via `efts.sec.gov` full-text search, read 2026-09-22; G2, `g2.com/categories/answer-engine-optimization-aeo`, read 2026-09-22 (listed "By Adobe") | SEC EDGAR full-text hit; G2 AEO category page 1, top-ranked (4.4/5, 4,035 reviews) | not stated (SEC domestic filer) | "AI Visibility Toolkit" — a $99/month add-on per earlier listicle summaries (not used as evidence, cited here only as context); G2 lists the product "By Adobe" |
| 26 | Similarweb | similarweb.com | incumbent bundling | (a)+(b) 2 sources | SEC 20-F (SMWB), filed 2026-03-02, via `efts.sec.gov` full-text search on "answer engine optimization", read 2026-09-22; G2, `g2.com/categories/answer-engine-optimization-aeo`, read 2026-09-22 | SEC EDGAR full-text hit; G2 AEO category page 1 (4.4/5, 1,214 reviews) | not stated (SEC 20-F foreign private issuer) | listed on G2 under "Best for: Cross-channel competitive intelligence with AI-traffic visibility" |

**On the Semrush/Adobe attribution:** G2's category pages list "Semrush — By Adobe" on both the AEO and AI-Search-Visibility category pages, read 2026-09-22. No independent second source for an Adobe–Semrush corporate transaction was pulled this session (WebSearch budget was exhausted before a dedicated query could run). Recorded as `unknown — checked G2 category pages only 2026-09-22`; flagged for verification by whichever pass next touches Semrush.

## 3. Held — limb (c), single-source or listicle-only (70 names)

Per the roster rule, limb (c) covers "a name appearing only in listicles or in a single review corpus." Extended in this file, and flagged as an interpretation, to also cover: a name appearing on exactly one G2 category-page listing with no second independent source found; a name appearing only as a self-submitted Crunchbase organization profile; a name appearing only as a founder-submitted "Show HN" post with no independent coverage found. Each is held, not screened out, and is re-checked if any later pull produces an independent source.

### 3a. G2-listed, single source (G2 category pages only, no second source found this pull)

| Name | Page(s) it appeared on | Why held |
|---|---|---|
| Frase | `frase.io` blog listicle context only, e.g. `frase.io/blog/the-10-best-ai-visibility-tools-in-2026` | Appears only in listicle roundups this pull; not confirmed on a G2/Capterra/OMR category page read today |
| AIclicks | `g2.com/categories/answer-engine-optimization-aeo`, read 2026-09-22 (4.9/5, 61 reviews) | One G2 listing, no independent second source found this session |
| Waikay | `g2.com/categories/answer-engine-optimization-aeo?page=2`, read 2026-09-22 (4.7/5, 26 reviews) | Same |
| Hall | `g2.com/categories/answer-engine-optimization-aeo?page=2`, read 2026-09-22 (4.8/5, 12 reviews) | Same; `rankability.com/blog/hall-ai-review/` is a single-product review, not counted as independent per the listicle-adjacent spirit of the rule |
| Qwairy | `g2.com/categories/answer-engine-optimization-aeo?page=2`, read 2026-09-22 (4.7/5, 45 reviews) | One G2 listing only |
| Uberall | `g2.com/categories/answer-engine-optimization-aeo?page=2`, read 2026-09-22 (4.4/5, 237 reviews) | One G2 listing; Uberall is a known local-listings incumbent but no second independent source on its AEO feature was pulled this session |
| aiseo.ai | `g2.com/categories/answer-engine-optimization-aeo?page=2`, read 2026-09-22 (4.6/5, 631 reviews) | One G2 listing only |
| Onclusive | `g2.com/categories/answer-engine-optimization-aeo?page=2`, read 2026-09-22 (4.3/5, 207 reviews) | One G2 listing; no AI-visibility launch article found for Onclusive this session |
| SOCi | `g2.com/categories/ai-search-visibility-optimization-tools`, read 2026-09-22 (4.5/5, 4,683 reviews) | One G2 listing; SOCi is Nasdaq-listed (ticker SOCI) but an EDGAR check for its own AI-visibility language was not run this session |
| Local Falcon | `g2.com/categories/ai-search-visibility-optimization-tools`, read 2026-09-22 (4.7/5, 149 reviews) | One G2 listing only |
| Scalenut | `g2.com/categories/ai-search-visibility-optimization-tools`, read 2026-09-22 (4.7/5, 315 reviews) | One G2 listing only |
| Mentionlytics | `g2.com/categories/answer-engine-optimization-aeo?page=2`, read 2026-09-22 (4.9/5, 114 reviews) | One G2 listing only |
| Brandi AI | `g2.com/categories/answer-engine-optimization-aeo?page=2`, read 2026-09-22 (4.9/5, 36 reviews) | One G2 listing only; note distinct from "Brandlight AI," a separate rostered vendor with a confusingly similar name |
| SE Ranking | `g2.com/categories/answer-engine-optimization-aeo`, read 2026-09-22 (4.7/5, 1,606 reviews) | One G2 listing; a well-known SEO incumbent but no independent AEO-feature launch article was pulled this session |
| Visby AI | `g2.com/categories/answer-engine-optimization-aeo`, read 2026-09-22 (4.8/5, 108 reviews) | One G2 listing only |
| Ktau.ai | G2 AI marketplace tag page, `ai.g2.com/marketplace/?tag=generative-engine-optimization`, read 2026-09-22 | One-line G2 marketplace tag entry only, no category-page listing or second source |
| Blym AI | Same G2 AI marketplace tag page | Same |
| VISIBLE™ | Same G2 AI marketplace tag page | Same |
| Writesonic | Same G2 AI marketplace tag page, plus Wikipedia | Wikipedia is tier 6, a pointer per `channels.md` C59; no tier 2-5 source found |

### 3b. OMR Reviews-listed, single review corpus

| Name | Page(s) it appeared on | Why held |
|---|---|---|
| Finseo | `omr.com/en/reviews/product/finseo`, read 2026-09-22; LinkedIn company page (vendor-controlled, not counted as independent) | Appears only in the OMR GEO category — one review corpus |
| Kambrium | `omr.com/en/reviews/product/kambrium/pricing`, read 2026-09-22 | Same |
| GEOlyze | `omr.com/en/reviews/product/geolyze/alternatives`, read 2026-09-22 | Same |
| Temso AI | `omr.com/en/reviews/product/temso-ai`, read 2026-09-22 | Same |
| Quaro | referenced from the OMR GEO category overview, read 2026-09-22 | Same |

### 3c. Crunchbase self-submitted profile only (no independent corroboration found)

| Name | Page it appeared on | Why held |
|---|---|---|
| Optivara | `crunchbase.com/organization/optivara` | Self-submitted profile only; a self-submitted tier-5 Crunchbase profile alone does not satisfy limb (b) per the 2026-09-22 rewrite (B13) |
| LovedByAI | `crunchbase.com/organization/lovedbyai` | Same |
| Optimize Ai Search | `crunchbase.com/organization/optimize-ai-search` | Same |
| Growthner (agency) | `crunchbase.com/organization/growthner` | Same |
| Discovered Labs (agency) | `crunchbase.com/organization/discovered-labs` | Same |
| GenRankEngine | `crunchbase.com/organization/genrankengine` | Same |
| Profit Engine Marketing (agency) | `crunchbase.com/organization/profit-engine-marketing-ltd` | Same |
| AuthorityTech (agency) | `crunchbase.com/organization/authoritytech` | Same |
| AI Visibility Rank | `crunchbase.com/organization/ai-visibility-rank` | Same |
| Visibly | `crunchbase.com/organization/visibly-bbb7` | Same; distinct from "Visby AI," a separate held name |
| BrandViz.ai | `crunchbase.com/organization/brandviz-ai` | Same |
| Appear on AI | `crunchbase.com/organization/appearonai` | Same |
| GetFoundOnAI.com | `g2.com/products/get-found-on-ai/discuss`; `g2.com/sellers/al-visibility` | G2 discussion/seller pages carry no review count or category listing; treated as thin as a self-submitted profile |

### 3d. Hacker News "Show HN" — founder-submitted, no independent coverage found

| Name | HN item | Why held |
|---|---|---|
| Opttab | `news.ycombinator.com` item by ardaulusoy, 2025-12-03 | Founder self-post, 1 point; no independent source found |
| Rankly (tryrankly.com / rankly.ai) | `news.ycombinator.com` item by satj, 2025-11-06/07 | Same |
| geoark.ai | `news.ycombinator.com` item by abedaarabi, 2026-03-09 | Same |
| mentiondesk.com | `news.ycombinator.com` item by krisozy, 2025-07-15 | Same |
| Citatra | `news.ycombinator.com` item by Citatra, 2026-02-27; `github.com/Citatra/Citatra` | Same |
| Amplift | `news.ycombinator.com` item by dora_wu, 2025-12-11 | Same |
| Hikoo | `news.ycombinator.com` item by Niout, 2026-02-13 | Same |
| GeoRankers | `news.ycombinator.com` item by YJ2023, 2026-02-02 | Same |
| Argeo (argeo.ai) | `news.ycombinator.com` item by faruk_tugtekin, 2026-02-19 | Same |
| dialtoneapp.com | `news.ycombinator.com` item by fcpguru, 2026-04-19 | Same |

### 3e. Other thin single-source names

| Name | Page it appeared on | Why held |
|---|---|---|
| Goodie AI | listicle mentions only; described as "about 11 people, no independently verified reviews on G2 or Capterra" | Explicitly no G2/Capterra presence found; listicle-only |
| Feedonomics / Commerce | `commerce.com/press/feedonomics-unlocks-agentic-discovery-with-agentic-catalog-exports/` (vendor's own press page); `rye.com/blog/agentic-commerce-startups` (roundup) | Vendor's own page plus one roundup blog — neither is an independent qualifying source |
| commercetools (Agent Gateway) | `rye.com/blog/agentic-commerce-startups` | Roundup blog only |
| Salsify (OpenAI Connect) | `rye.com/blog/agentic-commerce-startups` | Roundup blog only |
| Syndigo (OpenAI Connect, GEO product) | `rye.com/blog/agentic-commerce-startups` | Roundup blog only |
| Productsup | `productsup.com/agentic-commerce-tracker/` (vendor); `rye.com/blog/agentic-commerce-startups` | Vendor page plus one roundup blog |
| Alhena | `alhena.ai/blog/perplexity-shopping-merchants-setup-guide/` (vendor) | Vendor's own page only |
| Rye | `rye.com/blog/agentic-commerce-startups` (Rye's own blog) | Vendor's own page describing the wider market, not corroborated elsewhere this pull |

### 3f. Agencies named only in listicles (P3-c5 candidates, none rostered)

Every name below appeared only inside a "best GEO agency" roundup article — tier 7 per `trust-rubric.md`, counted in the screened total, never pulled as evidence. Pages: `thriveagency.com/news/top-generative-engine-optimization-geo-agencies/`, `seoprofy.com/blog/generative-engine-optimization-agencies/`, `grizzle.io/blog/best-generative-engine-optimization-agencies-for-b2b`, `thedigitalelevator.com/blog/best-generative-engine-optimization-geo-agencies/`, `gofishdigital.com/blog/generative-engine-optimization-agencies/`, `20northmarketing.com/blog/top-ai-optimization-agencies`, `concurate.com/best-generative-engine-optimization-companies-ai-visibility/`, `seodiscovery.com/blog/best-generative-engine-optimisation-agencies/` — all read 2026-09-22.

Names carried: Go Fish Digital, iPullRank, Relevance, Siege Media, Omniscient Digital, Perrill, Single Grain, Spicy Margarita, EWR Digital, SeoProfy, Digital Elevator, Graphite, Directive, Animalz, First Page Sage, Percepture, Growwise Media, Thrive Agency (self-listed in its own roundup), Grizzle, 20North Marketing, Concurate, SEO Discovery.

## 4. Screened-out — failing all three limbs (25 names)

| Name | Single source seen | Reason not held, not rostered |
|---|---|---|
| GenerativeX | `crunchbase.com/organization/generativex-co`; Preqin profile | Confirmed off-topic: Tokyo-based generative-AI consulting/app-dev firm, not a GEO/AI-visibility vendor. The "$4M Series A" funding hit (finsmes.com, thesaasnews.com) describes this same unrelated company, not a category fit |
| Glidelogic Corp | SEC 10-K, filed via EDGAR full-text search, read 2026-09-22 | Own 10-K states the company "initiated preliminary development work on a Generative Engine Optimization... product concept" then "determined to discontinue the initiative" — not a current seller |
| REZOLVE AI PLC | SEC 6-K, filed via EDGAR full-text search, read 2026-09-22 | Filing hit on "answer engine optimization" could not be confirmed as describing REZOLVE as a seller of the category rather than a generative-AI retail/e-commerce company using the term in passing; not verified as a fit this session |
| Rent the Runway | SEC 8-K/10-K, EDGAR full-text hit | Filer uses "answer engine optimization" describing its own marketing, not a seller of the category |
| Duluth Holdings | SEC 10-K, EDGAR full-text hit | Same pattern — apparel retailer, not a category seller |
| Tailored Brands | SEC S-1/DRS-A, EDGAR full-text hit | Same pattern — apparel retailer |
| Destination XL Group | SEC PREM14A/PRER14A, EDGAR full-text hit | Same pattern — apparel retailer |
| TechTarget | SEC 8-K/10-K/ARS, EDGAR full-text hit | B2B media company discussing the category, not confirmed as a seller of AI-visibility tooling |
| Fastly | SEC 10-K, EDGAR full-text hit | CDN infrastructure company; term appears in a general AI-traffic context, not as a category seller |
| Ooma | SEC 10-K/ARS, EDGAR full-text hit | Communications company; not a category seller |
| Zeta Global Holdings | SEC 10-K/ARS, EDGAR full-text hit | Marketing-cloud company; term usage not confirmed as a dedicated AI-visibility product this session |
| Upland Software | SEC 10-K/ARS/ARS-A, EDGAR full-text hit | Software conglomerate; term usage not confirmed as a category product |
| Coty | SEC 10-K, EDGAR full-text hit | Beauty conglomerate discussing the category in its own marketing context, not a seller |
| Primerica | SEC 10-K/ARS, EDGAR full-text hit | Financial services company; not a category seller |
| Fiverr | SEC 20-F, EDGAR full-text hit | Freelance marketplace; term usage describes freelancer services offered on the platform, not Fiverr itself selling a tool |
| Stagwell | SEC ARS, EDGAR full-text hit | Marketing holding company; term usage not confirmed as a dedicated product this session |
| Intuit | SEC 10-K, EDGAR full-text hit | Financial software company; term usage context not confirmed as a category product |
| Avalon GloboCare Corp | SEC S-1, EDGAR full-text hit | Biotech/health-tech company; unrelated to AI-visibility tooling on its face, not verified further |
| FutureCore Acquisition Corp | SEC DRS/S-1, EDGAR full-text hit | SPAC; term usage context not identified this session |
| Intelligent Protection Management Corp | SEC 10-K/ARS, EDGAR full-text hit | Not identified as a category seller this session |
| Cluely | Wikipedia tangential hit during HN search | Unrelated product (AI "cheating" assistant), not a GEO/AI-visibility vendor |
| TCab Tech | Wikipedia tangential hit during HN search | Unrelated (ride-hailing), not a fit |
| You.com | Search-summary tangential mention | An AI search engine itself, not a third-party GEO/AI-visibility vendor |
| LMArena | Search-summary tangential mention | Model-evaluation leaderboard, not a fit |
| "al-visibility" (G2 seller page) | `g2.com/sellers/al-visibility` | Garbled/unclear seller-page name, could not confirm a real distinct vendor behind it this session |

## 5. Counts

- **Screened:** 121 distinct names encountered across all queries and registry pulls (26 rostered + 70 held + 25 screened-out)
- **Held:** 70 (per limb (c), including the extended interpretation stated in section 3's header)
- **Rostered:** 26

## 6. Incumbent-bundling and agency candidates — for the scheduler's P3-c1..c6 split

**Incumbent bundling (SEO/analytics/PR/reputation incumbents that added an AI-visibility feature), candidates for P3-c4, already rostered above with evidence:** Semrush (SEC filing + G2, "By Adobe" on G2 — Adobe relationship unconfirmed by a second source, see note under row 25/26), Similarweb (SEC filing + G2), Ahrefs (Businesswire + G2), HubSpot AEO (SEC filing + CMSWire + G2), Yext / Brand Scout (SEC filing + stocktitan + G2), Conductor (CMSWire + DemandGenReport + G2), BrightEdge (GlobeNewswire + G2), Birdeye (PRNewswire + G2), Muck Rack (GlobeNewswire + G2), AirOps (Businesswire + Crunchbase + G2), Quattr (G2 + perpetualny.com), and Scrunch AI post-acquisition (now under Sitecore — Bloomberg + Sitecore newsroom + PRNewswire + G2).

Held-only incumbent-adjacent names worth a second look once corroborated: SOCi (Nasdaq SOCI), SE Ranking, Uberall, Onclusive — all established companies with a single G2 listing this pull; an EDGAR or press check on each was not run this session for lack of remaining WebSearch budget.

**Agencies (P3-c5 candidates):** none cleared the roster rule this pass — every agency name found sits in section 3f, listicle-only. Onfolio Holdings' subsidiary Pace Generative LLC is the one agency-shaped row that did clear (via its parent's SEC filings), and is rostered under sub-market "agency."

**Paid placement / agentic-commerce sell-side tooling (P3-c6 candidates):** this sweep found this sub-market thin. Every named vendor (Feedonomics/Commerce, commercetools, Salsify, Syndigo, Productsup, Alhena, Rye, and the ad-management tools Ryze AI/AdStellar/Optmyzr/Trapica from query 13) sits in the held list — each surfaced through exactly one roundup blog or the vendor's own page, with no independent second source or filing found this session. P2-c6 and P2-c7 (already landed, per `docs/method/STATE.md`) reached the *platform-side* partner lists for agentic-commerce protocols (Visa TAP, Mastercard Agent Pay, PayPal, Shopify, Stripe, and others); this P3-c0 sweep did not re-verify those against the roster rule since they are protocols/platforms, not third-party tooling vendors selling into the category. P3-c6 will need its own targeted queries — this sweep's generic "agentic commerce platform vendor" and "product feed AI shopping" queries surfaced almost nothing that clears two independent non-vendor sources.

## 7. Unknowns

- `unknown — checked efts.sec.gov "AI visibility" full-text query 2026-09-22` — the endpoint returned HTTP 500 on this exact query string; not retried before the session's tool budget was reached.
- `unknown — checked g2.com AEO and AI-Search-Visibility category pages, page 1-2 only, 2026-09-22` — 43 and 36 total pages respectively (631 and 539 listings) exist; pages 3 onward were not read, so the roster is a floor, not a ceiling, on G2-discoverable names.
- `unknown — checked g2.com/sellers/brandlight and checkthat.ai 2026-09-22` — Brandlight AI's G2 review count is reported inconsistently across secondary aggregators (194 vs. 19 vs. 213 depending on the page); the number read directly off the G2 AEO category page (213) is the one recorded in the roster row, the discrepancy is not resolved.
- `unknown — checked companies-house register for Brandlight 2026-09-22` — no matching UK entity found; Brandlight AI's country of incorporation is not established by any source pulled this session.
- `unknown — checked WebSearch for "Semrush" "Adobe" acquisition/relationship confirmation 2026-09-22` — session WebSearch budget (200/200) was exhausted before a dedicated query could confirm or refute the "Semrush — By Adobe" attribution G2 displays; see the note under roster rows 25-26.
- `unknown — checked UK Companies House for geoSurge/Searchable's connection to the specific vendor entities named in funding press 2026-09-22` — the register match is by company name only; no cross-check against the funding article's named founders or investors was performed to confirm the Companies House entity is the same legal person as the press-covered startup.
- `unknown — checked capterra.com and trustradius.com 2026-09-22` — neither review site (C37/C38) was reached this session; both are flagged `403→ext` in `channels.md` and were not attempted given the remaining time budget after the G2 pull.
- `unknown — checked conference speaker/sponsor lists beyond MAICON and GEO Conference NYC/SF 2026-09-22` — no vendor sponsor names were found on either agenda page read; sponsor lists may sit behind a registration wall not reached by this pull.
- `unknown — checked non-English (set X) queries against C64/C65 beyond the single OMR pull 2026-09-22` — no German/French/Spanish-language queries were run this session; the DACH names found (Finseo, Rankscale.ai, Kambrium, GEOlyze, Temso AI, Quaro) all came through the English-language OMR category page, not a set-X query.
