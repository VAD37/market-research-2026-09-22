# LinkedIn Jobs — guest search API — GEO/AEO/AI-visibility postings, B2B SaaS employers

```yaml
source:          LinkedIn Jobs (guest, unauthenticated)
url_or_doc_id:   https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=<term>&location=Worldwide&start=0 — 18 query variants, each listed verbatim below with its result
published:       n/a — live search index, not a dated publication; individual postings carry their own LinkedIn posting IDs
pull_date:       2026-09-22
pull_method:     fetch (curl, this session's Bash tool, no browser extension, no login)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default for S1 ("employer's own posting") where a posting names its own employer and description verbatim; the guest search-results HTML itself (title/company/location only, no description) is treated as a pointer to the posting, not a source in its own right
source_label:    company-stated
lane:            F
sub_market:      organic recommendation (paid placement and agentic commerce queries also run — see below, both returned no B2B SaaS employer-side hits)
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        search-result-page fragments (title, company, location, posting URL) for all 18 queries; full job-description text fetched separately for the four postings that named a B2B SaaS employer and an organic-recommendation term (Pennylane, Mercury, AutoLeap, Actindo)
```

## Verbatim

**Access note first.** `linkedin.com/jobs/search` itself (the consumer-facing search page) was not tried; this pull uses the public guest API endpoint `jobs-guest/jobs/api/seeMoreJobPostings/search`, which returns 10 results per call with no visible total-count field and no offset beyond `start=`. This endpoint does **not** enforce exact-phrase matching on quoted keywords — queries quoted `"generative engine optimization"` returned unrelated LLM/ML engineering roles (see query 1 below), matching the individual words rather than the phrase. This is recorded as a channel-bias finding, not corrected for.

### Query 1 — `keywords="generative engine optimization"` (organic, set O bare term)
10 results, all false positives on the literal words "generative," "engine," "optimization" against ML/LLM engineering roles, none GEO-marketing: Principal Machine Learning Engineer (Airbnb), Senior Algorithm Engineer ×3 (Traveloka, Traveloka, Traveloka), 推理优化工程师 (Mobvoi), Founding AI Engineer (Owen Thomas), NLP Performance Engineer (G-Research), Algorithm Engineer (Meituan), Member of Technical Staff (eBay), Artificial Intelligence Engineer (HartleyCo). **No B2B SaaS GEO-marketing hit.**

### Query 2 — `keywords="answer engine optimization"` (organic, set O)
10 results, mixed SEO/GEO-relevant and noise: Senior SEO & AI Search Lead SEO/GEO/AEO (Pete Tong DJ Academy), Lead SEO & Web Intelligence (NEXT Ventures), SEO Manager (iSpeedToLead), Head of SEO (Compare the Market Australia), Director of Technical SEO (Boca Recovery Center), **"Organic Search Marketer - SEO/AEO" (Mercury)**, Head of SEO (iSelect), SEO & GEO Specialist (BeRepublic), SEO/GEO Specialist (ParakeetAI), Sr. Manager SEO (Opendoor). Mercury posting fetched in full — see below.

### Query 3 — `keywords="AI visibility" SaaS`
10 results, developer-relations/product roles at AI-infra vendors, none naming GEO/AEO explicitly: Developer Evangelist ×2 (LlamaIndex), Developer Advocate (SearchApi), VP Customer Success (incident.io), AI Product Analyst (Cohere), Member of Technical Staff (SearchApi), Developer Advocate (Sanity), Senior Developer Advocate (MongoDB), Staff Technical Product Marketing Manager (TELUS Digital), Multimodal AI Content Specialist (unlisted, China). **No AI-visibility-specific B2B SaaS spend signal.**

### Query 4 — `keywords="AI search visibility"`
10 results, general SEO roles, no B2B SaaS employer naming this exact term: HR POD Careers, Auto & General Australia, Recruit AI, Perfect Hideaways, iSelect, ServiceNow (Machine Learning Engineering Manager, GAI Search Relevance — ServiceNow is enterprise B2B SaaS but the role is ML infra, not AI-visibility marketing), GrowYourCorp, 平安健康保险股份有限公司, Searchability, Manifest.

### Query 5 — `keywords=GEO "generative engine"` (disambiguated per glossary rule)
10 results, all geolocation/AI-infra engineering noise (Mapbox Location AI ×2, real-estate, Google Cloud, Engine (VP AI Platform — company literally named "Engine"), Geolava, GIS, X Moonshot Factory, Exodigo): confirms the glossary's warning that bare "GEO" pairings still leak geographic-sense results even with a disambiguator term attached.

### Query 6 — `keywords="sponsored answers"` (paid, set P)
10 results, entirely unrelated (sales/customer-service roles at 4Twenty Consulting, EXADS, eTeam ×2, CGC Recruitment, Third Bridge, SHRI KRISHNA): **zero relevant hits, no B2B SaaS paid-placement signal.**

### Query 7 — `keywords="agentic commerce"`
10 results, all e-commerce/retail engineering: Shopee, Faire ×2, Shopify, Sana Commerce ×2 (B2B e-commerce SaaS, but engineering not marketing/spend role), MANGO, Tudoholic, Picnic Technologies, "Commerce" (company name) ×2. **No B2B SaaS agentic-commerce spend signal.**

### Query 8 — `keywords="AI visibility" "B2B SaaS"`
10 results, DevRel/GTM roles at SaaS/AI vendors, none naming AI-visibility/GEO/AEO specifically as the role's function: LlamaIndex ×2, ClickHouse/Langfuse, MongoDB, Okta, 1Password ×2 (Director GTM Engineering), Propel ("Founding Product Marketing Lead - AI SaaS"), Cribl, Synthesia.

### Query 9 — `keywords=GEO AEO marketing SaaS`
10 results, field-marketing roles at SaaS vendors, none naming GEO/AEO as the role itself: Zoom (Workvivo) ×2, MongoDB, ServiceNow, Xsolla, Datadog, OpenAI, Glean ×2 (Senior Field Marketing Manager).

### Query 10 — `keywords="generative engine optimization" marketing`
10 results: Pragmatike (CMO, EMEA remote) ×8 near-duplicate postings across countries, **"SEO Lead" (AutoLeap)**, AutoLeap posting fetched in full — see below.

### Query 11 — `keywords="LLM SEO"`
10 results, several genuine GEO-marketing hits: Pete Tong DJ Academy, THE COCKTAIL, **"SEO & AI Content Specialist" (Pennylane) ×3 postings (Nice, Paris, Lille — same role, three locations)**, "Senior SEO & LLMO Executive" (M+C Saatchi UK/Group, an agency ×2), "Lead SEO & AI Search Strategist (GEO Lead)" (EngVarta), HR POD Careers, Castlery. Pennylane posting fetched in full — see below.

### Query 12 — `keywords="AI ads" SaaS marketing`
10 results, product-marketing roles at AI vendors, no AI-surface-ad-specific hit: Forsure.ai, Help Scout, ClickHouse/Langfuse ×2, Databricks, deepset/Haystack, Sigma, Cohere, Read AI, SOURCIX.

### Query 13 — `keywords="agentic commerce" SaaS`
10 results, payments/commerce engineering, not B2B SaaS marketing spend: Shopify, Koin Limited ×4, Shopee, "Commerce" (company name) ×3, Profitero+.

### Query 14 — `keywords=GEO AEO "small business" software`
10 results, general software-engineer roles with no GEO/AEO/SMB-marketing relevance: AgileEngine, Bizpoke, Onebeat, Arco Educação, EcoOnline, Enode, ecobee, EBizCharge, EKORE, Erudio.

### Query 15 — `keywords="Ads Manager" ChatGPT software`
10 results, general AI-marketing roles, one strong B2B SaaS hit: Creative Chaos, Snapscale, Lightricks ×2 (B2B Demand Generation Manager), Multiplier AI, Dada Consultants, **"Digital Marketing Manager - B2B SaaS & AI (m/w/d)" (Actindo)**, August, comrocket GmbH, Denave. Actindo posting fetched in full — see below.

### Queries 16–18 — supplementary
`"ChatGPT ads" OR "sponsored answers" OR "AI ad inventory"` (10 results, all irrelevant — Puffy AI Designer ×5, ZhenFund, DevUpLink, Dream Games, Zstate AI); `"Agentic Commerce Protocol" OR "agent payments" software` (10 results, all payments-infrastructure engineering at Global Payments Inc/Sezzle/PagBank — sell-side, not B2B SaaS buyer demand); `"product feed" "merchant of record" SaaS` (10 results, product-management roles, one self-tagged "B2B SaaS Startup" — traide AI — but role is trade-intelligence product, not naming any catalogue signal term).

### The four B2B SaaS employer hits, full posting text

**Pennylane** (`fr.linkedin.com/jobs/view/seo-ai-content-specialist-at-pennylane-4469211663`, and two duplicate postings 4469212558, 4469214077 for the same role in different French cities) — SEO & AI Content Specialist:
> "At Pennylane, SEO and Generative Engine Optimization (GEO) are central to making our product easier to discover and understand, while helping us reach new customers. [...] Pennylane is one of France's leading fintech unicorns, building the financial and accounting operating system for European SMEs and accounting firms. Founded in 2020 [...] More than 1.3 million SMEs already work with Pennylane. More than 7,000 accounting firms use our platform. **More than 1,100 Pennylaners work across the company**, representing more than 25 nationalities. More than €400 million raised since launch. [...] Help develop our GEO approach: Build an understanding of the questions and prompts prospects use in AI-powered discovery tools. Adapt content to help ensure Pennylane is accurately understood and discoverable across emerging AI search journeys."

**Mercury** (`ca.linkedin.com/jobs/view/organic-search-marketer-seo-aeo-at-mercury-4437610537`) — Organic Search Marketer (SEO/AEO):
> "Mercury's Organic Search team is hiring an Organic Search Marketer (SEO/AEO) to help define how Mercury shows up across search engines, answer engines, and AI-native discovery — for founders and entrepreneurs [...] develop SEO and AEO strategies that drive traffic and AI visibility for Mercury products (like Mercury's Business Credit Cards) [...] Define and own high-impact SEO and AI Search strategies across priority products [...] Own the technical SEO/AEO roadmap for Mercury.com."
Mercury's own LinkedIn company page (fetched via DuckDuckGo HTML result snippet, see pull notes): **"Company size 1,001-5,000 employees"**, headquarters San Francisco, CA, Privately Held, Founded 2017. Corroborating third-party estimate (Revelio Labs, via DDG snippet, not independently opened): "Mercury had 1,379 employees as of March 2026."

**AutoLeap** (`pk.linkedin.com/jobs/view/seo-lead-at-autoleap-4464612041`) — SEO Lead:
> "AutoLeap is the market-leading shop management SaaS provider in the underserved auto repair industry. [...] Strong SEO expertise across SaaS/B2B websites, including keyword research, search intent, content strategy, site architecture, and internal linking [...] Experience with AI SEO, Google Analytics, Google Tag Manager, and tools such as Ahrefs, Semrush, or Screaming frog." Funding note in the same posting: "In 2023, we announced our $30M Series B, led by Advanced Venture Partners (AVP)..." — company-history text, not a current-surface claim, so not subject to the `after:2026-06-22` surface-state date rule.
Company size (via DuckDuckGo HTML result snippets, not independently opened): PitchBook "AutoLeap has 199 total employees"; Revelio Labs "AutoLeap, Inc. is an Information Technology Services company that employs 225 people worldwide as of March 2026"; ZoomInfo and LeadIQ both "51-200 employees."

**Actindo** (`de.linkedin.com/jobs/view/digital-marketing-manager-b2b-saas-ai-m-w-d-at-actindo-4455692999`) — Digital Marketing Manager - B2B SaaS & AI (German-language posting):
> "Actindo ist eine B2B-SaaS-Plattform für Unternehmen aus Retail und E-Commerce. [...] Mit offenen Schnittstellen und integrierten KI-Funktionen automatisiert Actindo komplexe Abläufe und schafft die Grundlage für Agentic Commerce. [...] Du unterstützt SEO- und GEO-Maßnahmen, um die Sichtbarkeit von Actindo in Suchmaschinen und KI-basierten Systemen zu steigern." (Translation, mechanical: "Actindo is a B2B SaaS platform for retail and e-commerce companies... With open interfaces and integrated AI functions, Actindo automates complex processes and creates the foundation for Agentic Commerce... You support SEO and GEO measures to increase Actindo's visibility in search engines and AI-based systems.")
Company size (via DuckDuckGo HTML result snippets, not independently opened): PitchBook "Actindo has 52 total employees"; RocketReach "67 employees"; LeadIQ "employing between 51 and 200 people"; one estimate "team of around 70+ employees."

## Pull notes — mechanical only

- Endpoint used throughout: `www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search` — reachable without login or the Chrome extension, HTTP 200 on every one of the 18 queries above plus the 3 individual job-posting-page fetches (Pennylane, Mercury, AutoLeap, Actindo), all via plain `curl` with a browser User-Agent string. `indeed.com` (RSS and HTML search) and `upwork.com` (RSS) were both tried and both returned HTTP 403 — see the separate `f-signal-bs-S1-indeed-2026-09-22.md` and `f-signal-bs-S1-upwork-2026-09-22.md` files.
- Company headcount for Mercury, AutoLeap and Actindo was **not** stated on the job-posting page itself, so it was sourced via `html.duckduckgo.com/html/` search-result **snippets** (with a browser User-Agent — DuckDuckGo HTML returned 403 without one) rather than by opening the LinkedIn company page or a data-vendor profile page directly; each snippet is quoted above with its publisher named. Per `demand-signals.md`'s buyer-size proxy order ("a filing; the company's own site or careers page; a professional-network company profile"), Pennylane's figure (own careers/job-page text, "More than 1,100 Pennylaners") is the strongest of the four; Mercury's LinkedIn company-page range and AutoLeap/Actindo's third-party estimates (PitchBook, Revelio Labs, ZoomInfo, LeadIQ, RocketReach) are one step down that order (professional-network profile / data-vendor estimate) and are recorded as such, not re-verified against a primary filing.
- Buyer-size mapping applied per `demand-signals.md`'s bands (headcount SMB <100, mid-market 100–999, enterprise ≥1000): **Pennylane → Enterprise** (1,100+); **Mercury → Enterprise** (1,001–5,000 per LinkedIn, 1,379 per Revelio Labs, both >1,000); **AutoLeap → Mid-market** (199–225 across three sources, all in the 100–999 band); **Actindo → SMB** (52–70 across three sources, all under 100).
- All four hits are tagged sub-market **organic recommendation** (GEO/AEO/AI-content terms named explicitly in each posting); none of the 18 queries — including the two paid-placement queries (6, 12, 16) and the three agentic-commerce queries (7, 13, 17) — returned a B2B SaaS employer naming a paid-AI-surface or agentic-commerce budget line. This absence is recorded as `none found` for those two sub-markets under S1, not left blank, given the query list run.
- Per the cell-read rule (`demand-signals.md`), all four hits are tier 3 ("employer's own posting"), below the tier-5 floor for a spend read; each is recorded as **attention**, at its own tier and class, not as a qualifying spend signal on its own.
- Noise ratio: of 18 queries × 10 results = 180 listed postings, 4 were usable B2B SaaS organic-recommendation hits (2.2%). The `"generative engine optimization"` and `GEO "generative engine"` queries (1, 5) returned zero relevant hits out of 20 combined — the phrase-matching failure noted in the header above is the dominant driver.
- freelancer.com was tried (`freelancer.com/jobs/generative-engine-optimization/`, HTTP 200) but returned a client-rendered SPA shell with no job data in the static HTML (no `__NEXT_DATA__` or equivalent JSON block found) — browser execution would be required to read actual postings; recorded in the browser backlog, not re-tried.
