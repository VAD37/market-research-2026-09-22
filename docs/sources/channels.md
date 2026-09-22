# Channels

**Amended 2026-09-22 per `query-book-redteam.md`: C60, C61, C62, C63, C64, C65, C66, C67 added — the eight §6 additions, closing blind spots B4, B5, B6, B8, B9 and B11. No row removed. The `## Regulators` heading was widened to `## Regulators, courts and enforcement`. Access codes on the new rows are this agent's own checks of 2026-09-22; three differ from the red-team's expectation — see caveats.**

Pass 1, task P1-a, compiled 2026-09-22. Where each lane pulls from. Per `docs/CLAUDE.md`: channel, what it reliably yields, refresh rate, access cost, known bias. Tier is the expectation from `../method/trust-rubric.md`, not an assignment. Lanes A–F per `../method/glossary.md`; signals S1–S12 per `../method/demand-signals.md`. No market facts here — channels, not numbers. Every vendor and publisher name below came from a search run 2026-09-22; the URL recorded is where it was found.

**Access codes**, from HTTP status checks run 2026-09-22 on this machine: `200` loads to plain fetch; `403→ext` refuses fetch, needs the Chrome extension; `404` the checked URL is gone; `000` no response; `login` / `paid` as marked.

## Platform primary — priority-1 and priority-2 engines

| # | Channel | URL | Yields | Refresh | Access | Bias | Tier | Lane | Pass | Signal |
|---|---|---|---|---|---|---|---|---|---|---|
| C1 | OpenAI announcement index | `openai.com/index/testing-ads-in-chatgpt/`, `/new-ways-to-buy-chatgpt-ads/`, `/our-approach-to-advertising-and-expanding-access/` | Ad product existence, launch framing, surface description | Irregular | 403→ext | Own framing; no volumes | 3 | B, C | 2 | S2 |
| C2 | OpenAI Help Center — ads article | `help.openai.com/en/articles/20001047-ads-in-chatgpt` | User-facing ad rules, labelling, data handling | Irregular | 403→ext | Consumer-facing wording | 3 | B | 2 | — |
| C3 | OpenAI platform docs — crawlers | `platform.openai.com/docs/bots` | Crawler user-agents, IP ranges, opt-out mechanics | Irregular | 200 | Publisher-facing | 3 | A, D | 2, 5 | — |
| C4 | Agentic Commerce Protocol spec (OpenAI + Stripe) | `github.com/agentic-commerce-protocol/agentic-commerce-protocol`; `docs.stripe.com/agentic-commerce` | Checkout spec, versioning, licence, merchant-of-record model | Dated snapshots | 200 (Stripe) | Two-vendor standard | 3 | C | 2 | — |
| C5 | Anthropic news + docs | `anthropic.com/news`; `docs.anthropic.com` | Commerce-agent material, model/surface changes, usage policy | Irregular | 200 | Own framing | 3 | A, C | 2 | S2 |
| C6 | Google Ads Help — AI surfaces | `support.google.com/google-ads/answer/16297775?hl=en` | Ad eligibility inside AI Overviews, country list, formats | Continuous | 200 | Advertiser-facing, no volumes | 3 | B | 2 | — |
| C7 | Google ads/commerce blog | `blog.google/products/ads-commerce/` | Marketing Live announcements, new AI Mode formats | Weekly-ish | 200 | Launch framing | 3 | B, C | 2 | — |
| C8 | Google Search Central — crawler docs | `developers.google.com/search/docs/crawling-indexing/google-common-crawlers` | Crawler identities, indexing rules, structured-data guidance | Continuous | 200 | Publisher-facing | 3 | A, D | 2, 5 | — |
| C9 | Microsoft Advertising blog + platform | `about.ads.microsoft.com/en/blog`; `ads.microsoft.com` | Copilot ad surfaces, Merchant Center feeds, checkout, brand agents | Monthly | 200 | Launch framing | 3 | B, C | 2 | — |
| C10 | Amazon Ads — what's new | `advertising.amazon.com/resources/whats-new` | Sponsored-prompt formats, billing model, console reporting | Irregular | 200 | Seller-facing | 3 | B, C | 2 | — |
| C11 | Perplexity blog / hub | `perplexity.ai/hub/blog` | Ad-product status, publisher revenue-share programme | Irregular | 403→ext | Own framing; ad status has reversed | 3 | B | 2 | — |
| C12 | Priority-3 engine own surfaces (Meta AI, Grok, DeepSeek) | `unknown — checked "Meta AI Grok DeepSeek ads commercial surface 2026" 2026-09-22` | Existence check only per `plan.md` | — | — | — | 3 | B | 2 | — |
| C61 | Wayback Machine | `web.archive.org` | Prior state of a withdrawn or edited platform page | Continuous | root 200; WebFetch refused 2026-09-22 → ext | Capture gaps; robots-era exclusions | 3 | A, B, C | 2, 4 | — |

## Filings, funding, procurement

| # | Channel | URL | Yields | Refresh | Access | Bias | Tier | Lane | Pass | Signal |
|---|---|---|---|---|---|---|---|---|---|---|
| C13 | SEC EDGAR full-text search API | `efts.sec.gov/LATEST/search-index?q=` | Filed mentions of category terms; 8-K earnings exhibits; Form D | Daily | 200 (HTML UI at `sec.gov/edgar/search/` 403→ext) | US registrants only | 2 | B, E, F | 2, 4 | S3, S7, S11 |
| C14 | Crunchbase free profiles | `crunchbase.com` | Round size, date, investors on free profile pages | Continuous | 200, partial paywall | Self-submitted; rounds over-counted | 5 | A, E | 3 | S3 |
| C15 | EU-Startups | `eu-startups.com` | European round announcements with named amounts | Daily | 200 | Press-release derived | 5 | A | 3 | S3 |
| C16 | PYMNTS investment tracker | `pymnts.com/news/investment-tracker/` | Round announcements, payments and commerce weighted | Daily | 200 | Press-release derived | 5 | A, C | 3 | S3 |
| C17 | SAM.gov | `sam.gov/search/` | US federal contract awards naming the category | Daily | 200 | Public sector only | 2 | A, F | 8 | S10 |
| C18 | UK Contracts Finder | `contractsfinder.service.gov.uk/Search` | UK public contract awards and values | Daily | 200 | Public sector only | 2 | A, F | 8 | S10 |
| C19 | USAspending | `usaspending.gov` | Award values against vendor names | Daily | 200 | Public sector only | 2 | A | 8 | S10, S11 |
| C20 | TED (EU tenders) | `ted.europa.eu/en/` | EU contract-award notices | Daily | 405 to plain GET — search API or ext | Public sector only | 2 | A | 8 | S10 |
| C67 | UK Companies House | `find-and-update.company-information.service.gov.uk` | Filing histories and accounts for UK-registered vendors | Continuous | 200 | UK only; small-company exemptions hide detail | 2 | A, E | 3 | S3 |

## Clickstream, panel, referral telemetry — Pass 2 first

| # | Channel | URL | Yields | Refresh | Access | Bias | Tier | Lane | Pass | Signal |
|---|---|---|---|---|---|---|---|---|---|---|
| C21 | Similarweb AI-search research blog | `aisearch.similarweb.com/blog/gen-ai-stats/`, `/zero-click-marketing/` | Assistant share of visits, referral and citation series | Monthly-ish | 200 | Panel + ISP + crawl mix; sells the adjacent product | 4 | A, E | 2 | S9 |
| C22 | Datos (Semrush-owned clickstream) | `datos.live` | State-of-search reports, zero-click rate, strict-clickstream method | Quarterly | 200 | Desktop-panel weighted; owner sells SEO tooling | 4 | A, E | 2 | S9 |
| C23 | SparkToro | `sparktoro.com/blog` | Joint clickstream studies, method appendices | Irregular | 200 | Founder-opinionated; partner data | 4 | A, E | 2 | S9 |
| C24 | StatCounter GlobalStats | `gs.statcounter.com` | Referrer-tag share series, method page published | Monthly | 200 | Tag-install bias, not a panel | 4 | A | 2 | S9 |
| C25 | Comscore | `unknown — checked "Comscore AI assistant share 2026 free report" 2026-09-22` | Panel share, method disclosure unverified | — | — | — | 4 | A | 2 | S9 |

## CDN and crawler telemetry

| # | Channel | URL | Yields | Refresh | Access | Bias | Tier | Lane | Pass | Signal |
|---|---|---|---|---|---|---|---|---|---|---|
| C26 | Cloudflare Radar — AI Insights | `radar.cloudflare.com/ai-insights` | Crawl-to-refer ratio per AI operator, bot share, industry filter | Continuous | 403→ext | Cloudflare-customer sites only; sells bot control | 4 | A, D | 2 | S9 |
| C27 | Cloudflare blog — Radar method posts | `blog.cloudflare.com/ai-search-crawl-refer-ratio-on-radar/`, `/ai-crawler-traffic-by-purpose-and-industry/` | The method behind the Radar cards, definitions | Irregular | 200 | Same population bias, method stated | 4 | A, D | 2 | — |
| C28 | HTTP Archive | `httparchive.org/reports`; `discuss.httparchive.org` | Crawlable corpus-wide adoption of on-page artifacts | Monthly | 200 | Crawl-list bias; home pages weighted | 4 | A, D | 2, 5 | S12 |
| C29 | Other CDN telemetry publishers (Fastly, Akamai, Vercel) | `unknown — checked "CDN AI crawler telemetry report 2026" 2026-09-22, only Cloudflare returned a public series` | — | — | — | — | 4 | A | 2 | — |

## Retail and e-commerce analytics publishing free

| # | Channel | URL | Yields | Refresh | Access | Bias | Tier | Lane | Pass | Signal |
|---|---|---|---|---|---|---|---|---|---|---|
| C30 | Adobe Digital Insights | `business.adobe.com/resources/sdk/` quarterly AI-traffic PDFs; `business.adobe.com/blog` | AI-referred retail traffic, conversion and engagement deltas | Quarterly | blog URL returned `000` 2026-09-22; PDF path found via search | Adobe Analytics customers only; sells the adjacent product | 4 | A, C, E | 2 | S9 |
| C31 | Salesforce newsroom / Shopping Index | `salesforce.com/news/stories/` | Holiday and quarterly AI-influenced spend estimates | Quarterly | 200 | Modelled "influenced" figures; vendor-reported | 5 | C, E | 2 | — |
| C32 | Shopify newsroom | `shopify.com/news` | Order growth attributed to AI surfaces; protocol support | Irregular | 200 | Vendor-reported, no base disclosed | 5 | C | 2 | — |

## Demand-side channels

| # | Channel | URL | Yields | Refresh | Access | Bias | Tier | Lane | Pass | Signal |
|---|---|---|---|---|---|---|---|---|---|---|
| C33 | LinkedIn Jobs | `linkedin.com/jobs/search/?keywords=generative%20engine%20optimization` | Postings naming GEO/AEO/AI visibility, employer, seniority | Continuous | 200 anonymous, deeper paging needs login | Large firms over-represented; lags spend | 3 | A, F | 8 | S1 |
| C34 | Indeed | `indeed.com/q-generative-engine-optimization-jobs-jobs.html` | Posting counts per term | Continuous | 403→ext | Aggregates duplicates | 3 | A, F | 8 | S1 |
| C35 | Employer career pages | e.g. `careers.indegene.com` | Full job text, team placement, budget signals | Continuous | mixed | Employer self-presentation | 3 | A, F | 8 | S1 |
| C36 | G2 | `g2.com/categories/ai-search-visibility` | Category membership, review velocity and dates | Continuous | 403→ext | Vendors farm reviews; category naming shifts | 5 | A, E | 3, 8 | S4 |
| C37 / C38 | Capterra; TrustRadius | `capterra.com`; `trustradius.com` | Second and third review corpora for cross-check | Continuous | 403→ext both | Same farming risk; Capterra is Gartner-owned; TrustRadius smaller n | 5 | A | 3, 8 | S4 |
| C39 | Reddit — r/SEO, r/PPC, r/bigseo | `reddit.com/r/SEO`, `/r/PPC`, `/r/bigseo` | Thread volume, practitioner complaints, tool churn | Continuous | 200 (JSON API blocked in predecessor sessions) | Vocal minority; anti-vendor skew | 4 | A, B, D, F | 4, 8 | S5 |
| C40 | Hacker News via Algolia API | `hn.algolia.com/api/v1/search?query=` | Dated thread and comment counts, no key needed | Continuous | 200 | Engineer-weighted, not marketer | 4 | A, C, D | 4, 8 | S5 |
| C41 | GEO practitioner Slack/Discord | `genengineoptimizers.com`; index at `thehiveindex.com/topics/seo/` (returned `000` 2026-09-22) | Named communities, channel names, membership claims | Continuous | login for content | Self-reported membership; 90-day archive loss | 5 | A, F | 4, 8 | S5 |
| C42 | Agency service pages and rate cards | discovered per query-book, not a fixed list | Service existence, list price, claimed deliverables | Irregular | 200 mostly | Asking price, never a purchase | 3 existence / 6 framing | A, F | 4, 8 | S6 |
| C43 | Earnings-call transcripts | `fool.com/earnings-call-transcripts/`; 8-K exhibits via C13; company IR pages | Brand-side mentions of AI-surface performance, named budget lines | Quarterly | 200 | Transcriber errors; mentions are rare | 2 filed / 5 transcript | B, E, F | 4 | S7, S11 |
| C44 | Conference agendas | `marketingaiinstitute.com/events/marketing-artificial-intelligence-conference/agenda`; ANA, Content Marketing World, GEO Conference listings | Session counts, speaker employers, track names | Annual | 200 | Sponsor-driven; a paid slot is not demand | 3 | A, B, F | 4, 8 | S8 |
| C45 | Google Trends | `trends.google.com/trends/` | Indexed interest for alias terms, relative only | Continuous | 200 | Index not a count; GEO term is ambiguous | 4 | A | 8 | S9 |
| C65 | OMR Reviews | `omr.com/en/reviews/category/ai`; `omr.com/de/reviews/` | DACH B2B review corpus carrying its own GEO category criteria | Continuous | 200 | DACH only; same review-farming risk as C36 | 5 | A, E | 3, 8 | S4 |
| C66 | Buyer-side surveys and freelance marketplaces | `gartner.com/en/newsroom`; `bluevine.com/blog`; `sbecouncil.org`; `upwork.com`; `freelancer.com` | CMO spend allocations; SMB adoption bands; posted freelance rates | Annual / continuous | Gartner and Upwork 403→ext; other three 200 | Self-report; Gartner enterprise-skewed; a posted rate is an asking rate | 4–5 | A, E, F | 8 | S1, S6, S7, S11 |
| C46 | Vendor own sites — pricing, customers, case studies | `tryprofound.com`, `peec.ai`, `scrunchai.com`, `otterly.ai`, `geosurge.ai`, `ahrefs.com/brand-radar`, `semrush.com/blog` | Disclosed price, named logos, case-study rosters, claimed n | Continuous | 200 (`semrush.com/ai/` 404 2026-09-22) | Vendor-reported; logos are not contracts | 5 with n, 6 without | A, E | 3, 4 | S2, S11 |

## Academic

| # | Channel | URL | Yields | Refresh | Access | Bias | Tier | Lane | Pass | Signal |
|---|---|---|---|---|---|---|---|---|---|---|
| C47 | arXiv | `arxiv.org/list/cs.IR/recent`; `arxiv.org/abs/2606.17443` verified 2026-09-22 | GEO-manipulation papers, benchmarks, defence work, prompt sets | Daily | 200 | Preprint, unreviewed; tier 4 with code, 5 without | 4–5 | D, E | 5 | — |
| C48 | ACL Anthology | `aclanthology.org` | Peer-reviewed NLP venue papers with artefacts | Per conference | 200 | Venue lag against a monthly-changing market | 3 | D, E | 5 | — |
| C49 | Semantic Scholar | `semanticscholar.org` | Citation graph, replication trails, venue metadata | Continuous | 200 (API keyless, rate-limited) | Coverage gaps outside CS | 3 | D, E | 5 | — |
| C50 | Google Scholar | `scholar.google.com` | Cited-by counts, grey literature, vendor whitepapers | Continuous | 200, aggressive rate limiting | Mixes preprint and reviewed without labelling | 4 | D, E | 5 | — |
| C63 | ACM DL, OpenReview, USENIX, IEEE Xplore, DBLP | `dl.acm.org`; `openreview.net`; `usenix.org`; `ieeexplore.ieee.org`; `dblp.org` | SIGIR, CIKM, WSDM, RecSys, WWW, KDD and security-venue papers | Per conference | ACM 403→ext; IEEE 418 default UA, 200 browser UA; three 200 | Venue lag; ACM partly paywalled | 3 | D, E | 5 | — |

## Regulators, courts and enforcement

| # | Channel | URL | Yields | Refresh | Access | Bias | Tier | Lane | Pass | Signal |
|---|---|---|---|---|---|---|---|---|---|---|
| C51 / C52 | EUR-Lex — AI Act; DSA | `eur-lex.europa.eu/eli/reg/2024/1689/oj`; `/eli/reg/2022/2065/oj` | Binding text: transparency, ad disclosure, recommender articles | On amendment | 202 to plain GET — retry or ext | Text only, no enforcement record | 2 | B, D | 2 | — |
| C53 | FTC | `ftc.gov/business-guidance/blog` (endorsement-guides URL checked 2026-09-22 returned 404) | Endorsement and disclosure guidance, enforcement actions | Irregular | 200 | US only | 2 | B, D | 2, 5 | — |
| C54 | UK CMA | `gov.uk/cma` | Market studies, digital-markets decisions | Irregular | 200 | UK only | 2 | B | 2 | — |
| C55 | UK ASA | `asa.org.uk` | Ad-labelling rulings that reach AI surfaces | Weekly | 200 | UK only, complaint-driven | 2 | B | 2 | — |
| C60 | EU DSA — enforcement, and Art. 39 ad repositories | `transparency.dsa.ec.europa.eu/`; `digital-strategy.ec.europa.eu`; `cnam.ie` | Designations and proceedings; each designated service's own ad repository | Continuous | 200 all three 2026-09-22 | EU-designated services only; field coverage varies per platform | 2 | B, C, D | 2 | S11 |
| C62 | CourtListener / RECAP | `courtlistener.com` | Dockets and exhibits in publisher-versus-engine litigation | Daily | 403→ext 2026-09-22, curl and fetch alike | US dockets only; exhibits often sealed | 2 | B, D, E | 2, 4 | S11 |

## Trade press that links primary data

| # | Channel | URL | Yields | Refresh | Access | Bias | Tier | Lane | Pass | Signal |
|---|---|---|---|---|---|---|---|---|---|---|
| C56 | PPC Land | `ppc.land` | Paid-surface changes, usually with a primary link | Daily | 200 | Announcement-led; little verification | 5 pointer | B, C | 2, 4 | — |
| C57 | Search Engine Land | `searchengineland.com` | Organic and paid surface changes | Daily | 403→ext | Vendor-sponsored content mixed in | 5 pointer | A, B | 2, 4 | — |
| C58 | Digital Commerce 360, TechCrunch, Search Engine Journal | per query-book | Commerce and funding pointers to primary sources | Daily | mixed | Press-release derived | 5 pointer | C, E | 3, 4 | S3 |
| C64 | EU trade press, German-language | `horizont.net`; `wuv.de`; `t3n.de`; `onlinemarketing.de` | EU ad-rollout coverage no English-language query surfaced | Daily | 200 all four | Announcement-led; DACH-weighted | 5 pointer | A, B | 2, 4 | — |
| C59 | Wikipedia — category article | `en.wikipedia.org/wiki/Generative_engine_optimization` | Reference list as a pointer set only, never as a source | Continuous | 200 | Editor-selected; cites listicles | 6 | A | 3 | — |

Trade press is a **pointer channel**: pull the primary it links, and file the trade item only when the primary is unreachable.

## Predecessor repo — one channel

`D:\researchs\market-research\docs\raw\`. Read as a source like any other, cited via a new `raw/` file with `pull_method: predecessor repo`. **Conclusions are not inherited** (root `CLAUDE.md`). Every file below carries pull date 2026-09-16 in its own header; headers only were read on 2026-09-22. Expected tier: whatever the underlying source was — the file is a container, not a source. Each `*-source-index.md` is the URL list for its paired `*-pulls.md`.

| File | Pull date | Subject per its own header | Lane it can feed |
|---|---|---|---|
| `ai-search-ads-pulls.md` / `-source-index.md` | 2026-09-16 | AI search visibility services sizing and index, 23 verbatim pulls | A, B |
| `buyer-integrity-pulls.md` / `-source-index.md` | 2026-09-16 | Who pays for answer-engine integrity; named budget owners, job postings, RFPs | A, D, F |
| `injection-feasibility-pulls.md` / `-source-index.md` | 2026-09-16 | Crawler identification, live retrieval, influence-measurement method, policy boundary | D, E |
| `ai-attack-defense-pulls.md` / `-source-index.md` | 2026-09-16 | AI red-teaming services market and sizing sources | D |
| `ai-trend-suite-pulls.md` / `-source-index.md` | 2026-09-16 | Category AI funding, revenue reality, bundling, analyst predictions | E |
| `market-gaps-2026-pulls.md` / `-source-index.md` | 2026-09-16 | Market gaps as of 2026-09; HN Algolia and Discourse JSON access notes | A, E |
| `verify-pass2-pulls.md` / `-source-index.md` | 2026-09-16 | Fact-check pass; EDGAR full-text and raw-API pulls marked `[direct fetch]` | B, E |
| `services-lane-pulls.md` / `-source-index.md` | 2026-09-16 | Real engagement pricing, demand channels, regulatory mandate, boutique census | A, F |
| `tos-browser-pulls.md` | 2026-09-16 | Four ToS pages recovered by Chrome extension after 403 to fetch | B, C |
| `recovery-pulls.md` / `-source-index.md` | 2026-09-16 | Browser-based retry of prior 403 and JS-shell failures; access-path notes | all |
| `agent-dashboard-pulls.md` / `-source-index.md` | 2026-09-16 | Agent tooling and repos | — |
| `first-customers-pulls.md` / `-source-index.md` | 2026-09-16 | First-ten-customers channel evidence for two-person companies | F |
| `two-founder-cases`, `creative-technical-pair`, `localization-play`, `sg-hcmc-scene` (`-pulls.md` / `-source-index.md` each) | 2026-09-16 | Founder pairing, two-founder companies, Vietnam/Singapore access layer, HCMC ecosystem | — (builder-constraint framing, demoted per `scope.md` R1) |

## Signal coverage check — every S has a channel

S1 jobs: C33, C34, C35, C66. S2 vendor customers: C46, C1, C5. S3 funding and ARR: C13, C14, C15, C16, C58, C67. S4 reviews: C36, C37, C38, C65. S5 community: C39, C40, C41. S6 agency pages: C42, C66. S7 earnings: C43, C13, C66. S8 agendas: C44. S9 search interest and share: C45, C21, C22, C23, C24, C26, C30. S10 procurement: C17, C18, C19, C20. S11 price paid: C43, C13, C19, C46, C60, C62, C66. S12 on-property artifacts: C28, plus our own domain sampling (`../method/panel-protocol.md`).

## Lane coverage check — three or more channels each

A: C1, C3, C5, C8, C21–C24, C26–C28, C33–C46, C57, C59, C61, C64, C65, C66, C67. B: C1, C2, C6, C7, C9–C11, C13, C43, C51–C58, C60, C61, C62, C64. C: C4, C5, C9, C10, C30–C32, C40, C58, C60, C61. D: C3, C8, C26, C28, C39, C40, C47–C50, C53, C60, C62, C63. E: C13, C21–C24, C30, C43, C46, C47–C50, C62, C63, C65, C66, C67. F: C13, C17, C18, C33–C35, C41–C44, C66.

## Caveats

- Access codes are one observation from one machine on 2026-09-22. A `403` is a fetch-path result, not proof the channel is closed; the Chrome extension reached several such pages in the predecessor repo's `recovery-pulls.md`.
- Tier columns are expectations from `../method/trust-rubric.md`. Hidden method drops a tier at pull time, every time.
- Four rows read `unknown — checked <terms> 2026-09-22`: C12 (priority-3 commercial surfaces), C25 (Comscore free series), C29 (non-Cloudflare CDN telemetry), and the C41 community index (`thehiveindex.com` returned `000`).
- Every clickstream and CDN row sells something adjacent to what it measures. C21, C22, C26 and C30 are publisher-and-vendor in one; `plan.md`'s reweight rule rests on them, so conflicting share figures sit side by side and are never averaged.
- C60 correction, on read 2026-09-22: `transparency.dsa.ec.europa.eu` is the statements-of-reasons database plus a Research API and publishes no ad records. DSA ad repositories are per-service under Art. 39 and are reached through each designated engine's own transparency page, not centrally. The red-team's row called the central database an ad repository; the row above says what the page says.
- Three red-team access expectations did not hold to this agent's fetch on 2026-09-22: C62 CourtListener (expected 200, observed 403 to curl and to plain fetch), C63 `dl.acm.org` (403) and `ieeexplore.ieee.org` (418 to a default user-agent, 200 to a browser one), C66 `gartner.com/en/newsroom` and `upwork.com` (403). Each is recorded `403→ext`, which is a fetch-path result and not proof the channel is closed.
- C59 Wikipedia is a pointer at tier 6; its reference list routinely includes tier-7 listicles. This file names no vendor as a competitor and ranks nothing — the census is Pass 3.
