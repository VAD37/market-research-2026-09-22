# Query book — red team

Pass 1, task P1-b, compiled 2026-09-22. Adversarial review of `channels.md`, `shortlist.md`, `query-book.md` per `../method/plan.md` Pass 1 detail. Lanes, aliases and metrics are `../method/glossary.md`'s; tiers `../method/trust-rubric.md`'s; signals `../method/demand-signals.md`'s; hypotheses `../method/hypotheses.md`'s. This file edits nothing — it lists amendments; the scheduler decides. No market facts: every URL below is an address where a query landed on 2026-09-22, not a finding.

## 1. Method

28 queries and fetches run 2026-09-22 (26 web searches, 2 EDGAR full-text fetches, 1 archive fetch that failed). Three attacks: **coverage matrix** — lane × engine × vertical walked cell by cell against the grid in `query-book.md` §"Lane × priority-1 engine" and the 29 clusters in `shortlist.md`; **adversarial search** — each suspected gap turned into a query and run, keeping only what came back today with its URL; **negative-space check** — sources the operators, the alias sets and the roster rule structurally exclude, tested by searching for a member of the excluded class. The search surface is US-only by its own description, which is itself finding B7.

## 2. Coverage matrix — lane × engine, and vertical reach

`q` query in the book, `c` cluster in the shortlist, `—` neither. P1: ChatGPT, Claude, Google. P2: Perplexity, Copilot, Amazon.

| Lane | ChatGPT | Claude | Google | Perplexity | Copilot | Amazon | Skincare | B2B SaaS | Regulated |
|---|---|---|---|---|---|---|---|---|---|
| A organic | q+c | q+c | q+c | **—** | **—** | **—** | **—** | **—** | **—** |
| B paid | q+c | q+c | q+c | q+c | q+c | q+c | **—** | **—** | **—** |
| C agentic | q+c | **c only** | q+c | **—** | q+c | q+c | **—** | **—** | **—** |
| D manipulation | q+c | q+c | q+c | **—** | **—** | **—** | **c only** | **—** | **c only** |
| E measurement | q+c | q+c | q+c | c only | c only | c only | **—** | **—** | **—** |
| F transition | engine-agnostic by design — no per-engine query or cluster | | | | | | **—** | **—** | **—** |

Gaps: A × all three P2 engines — organic visibility inside Perplexity, Copilot and Rufus is never asked. C × Claude has a cluster pull line ("MCP commerce-relevant docs") and no query; C × Perplexity is absent. D × P2 engines absent: P5-c7 checks P1 countermeasures only. **No cluster in `shortlist.md` is vertical-scoped** — the overlays exist as tokens that no cluster invokes, so every vertical column is a gap except H14's density comparison inside P5-c2 and P5-c3.

## 3. Hypothesis coverage

| H | Cluster whose pulls can confirm or kill it | Gap |
|---|---|---|
| H1 | P2-c1, P2-c2, P2-c8 | Partial — none yields conversion **by referrer**; P2-c8 is nearest and its figures are modelled |
| H2, H12, HE1, HE3 | P2-c3, c4, c5, c6 | — |
| H3, H6, H10, H11 | P4-c1…c6 | H11 needs one case per vertical; no P4 cluster is vertical-scoped |
| H5, H8 | P5-c1…c6; P2-c7 | — |
| H13, H14 | P5-c7; P5-c2, P5-c3 | H13 P1 engines only, no P2-engine policy pull; H14's vertical overlay is named, not built into either pull list |
| H15 | P3-c1…c4 | — |
| **H4, H7, H9** | **none** | Pass 8 has no clusters and no query set; 27 cells rest on channels alone |
| **H16** | **none** | Forecasts excluded from every Pass 2–5 query, routed to "the Pass 6 sizing task", which has no cluster and no queries |

HE2 and HP1–HP4 sit with the Pass 10 panel and are out of this book by design (`panel-protocol.md`).

## 4. Demand-signal coverage — per vertical, per buyer size

| S | Channel(s) | Cluster / query | Vertical reach | Buyer-size reach | Gap |
|---|---|---|---|---|---|
| S1 jobs | C33–C35 | P3-c0, as vendor discovery only | none | none | No EU job board; no SMB/freelance board |
| S2 vendor customers | C46, C1, C5 | P3-c1…c4 | none | vendor's own claim only | Cell attribution unsourced |
| S3 funding/ARR | C13–C16, C58 | P3-c0 | none | none | Non-US registries absent |
| S4 reviews | C36–C38 | P3-c0 | none | reviewer firm size undisclosed | DACH/EU review corpus absent |
| S5 community | C39–C41 | P4-c5 | none | none | Non-English communities absent |
| S6 agency pages, S8 agendas | C42; C44 | P3-c5; P4-c3 | none | none | EU agencies and EU events unreached by English queries |
| S7 earnings | C43, C13 | P4-c1 | none | enterprise only, structurally | No CMO/CFO survey channel |
| S9 search/share | C45, C21–C24, C26, C30 | P2-c1 | none | none | — |
| S10 procurement, S11 price paid | C17–C20; C43, C13, C19, C46 | **none** | none | public sector only, for S10 | No cluster, no query, either signal |
| S12 on-property | C28 + own sampling | P5-c5 partial | none | none | Brand sample frame undefined |

**Buyer size is unqueried everywhere.** The book carries vertical overlays and no buyer-size overlay; no signal row above can be cut SMB / mid / enterprise from its query alone.

## 5. Systematic blind spots

Thirteen. Every evidence line is a query run 2026-09-22 on the surface named in §1.

- **B1 — The exclusion block discards tier-3 and tier-5 primaries, and is applied where listicle risk is nil.** `-"best" -"top 10" -inurl:best- -inurl:top- -"alternatives" -"vs"` runs on *every* query, `site:`- and `allowed_domains`-pinned ones included. Query `G2 best AI visibility software category page 2026` returned `company.g2.com/news/new-categories-introduced-to-g2-in-march-2026` — the primary that dates the S4 category — beside `g2.com/best-software-companies/top-ai`, which `-inurl:best-` and `-inurl:top-` both kill. Query `OpenAI help center "best practices" ChatGPT search publishers page` returned tier-3 `help.openai.com/en/articles/6654000-how-to-use-chatgpt-effectively` (title carries "Best practices") and `help.openai.com/en/articles/12627856-publishers-and-developers-faq`, the page carrying OAI-SearchBot access and the `utm_source=chatgpt.com` referral tag — Lane A and the traffic metric both. Query `"AI Mode vs AI Overviews" support.google.com help page difference` returned nine results, every one carrying "vs", e.g. `greenflagdigital.com/learning-ai/google-ai-overviews-vs-ai-mode-vs-gemini/`; academic comparisons take the same form. Fix: scope the block to open web search only, and delete `-"vs"` and `-inurl:-vs-` outright.
- **B2 — Alias drift in set O.** Query `"AEO" "GEO" "AIO" "LLMO" "GSO" terminology debate which term marketers use 2026` returned `guptadeepak.com/geo-compass/guides/seo-aeo-geo-aio-llmo-disambiguation/` and `xponent21.com/insights/the-alphabet-soup-of-seo-what-aeo-aio-geo-and-aiseo-mean-for-your-strategy/`, naming AIO, GSO, AISEO. Query `"share of model" OR "share of voice" AI answers brand visibility term 2026` returned `aiocopilot.com/blog/share-of-model-ai-visibility-measurement-2026` plus eight pages using "AI Share of Voice" / "AI SOV". Fix: amendment 2 in §6.
- **B3 — Paid-side vocabulary is generic, never per-engine.** Set P names no engine's own product names. Queries today returned `openai.com/index/new-ways-to-buy-chatgpt-ads/` and `openai.com/index/expanding-access-to-ai-with-chatgpt-ads/` (a URL C1 does not list); Google's "Conversational Discovery", "Highlighted Answers", "AI-Powered Shopping Ads", "Business Agent for Leads" via `business.google.com/us/accelerate/announcements/ads-in-ai-mode/`; Microsoft's "Offer Highlights" and "sponsored recommendations" via `learn.microsoft.com/en-us/advertising/msa-help/hlp_ba_conc_adsforcopilot`, a domain absent from C9; Amazon's "Sponsored Products prompts" / "Sponsored Brands prompts" via `advertising.amazon.com/resources/whats-new/unboxed-2025-sponsored-products-and-sponsored-brands-prompts`.
- **B4 — Withdrawn products, and no archival channel.** `channels.md` notes Perplexity's "ad status has reversed" and no channel recovers a page as it stood. Query `Perplexity advertising sponsored questions status 2026` returned `pymnts.com/artificial-intelligence-2/2026/perplexity-pulling-sponsored-answers-from-ai-platform/` and `searchengineland.com/perplexity-stops-testing-advertising-469452`. A fetch of `web.archive.org/web/2025*/perplexity.ai/hub/blog/*` returned `Claude Code is unable to fetch from web.archive.org`; the archive is reachable only through the browser extension.
- **B5 — EU enforcement and the mandated ad repositories are absent.** C51/C52 carry only EUR-Lex text, their own bias column conceding "no enforcement record". Query `DSA enforcement AI chatbot advertising transparency Digital Services Coordinator 2026` returned `winbuzzer.com/2026/09/01/eu-designates-chatgpt-tougher-dsa-search-engine-scrutiny-xcxwbn/` and `lexology.com/library/detail.aspx?g=ac428b38-9c6e-4414-8ea0-0f40825ce013` on a VLOSE designation. Query `DSA ad repository transparency database very large online search engine advertisements API 2026` returned `transparency.dsa.ec.europa.eu/`, `github.com/digital-services-act/transparency-database`, and a peer-reviewed audit at `petsymposium.org/popets/2026/popets-2026-0059.php`. A mandated repository is a filed, queryable paid-inventory channel for Lane B, and nothing in the three files reaches it.
- **B6 — Non-English EU sources are unreachable from an English-only alias set.** Query `"KI-Sichtbarkeit" OR "Generative Engine Optimierung" Marken 2026` returned `aufgesang.de/blog/generative-engine-optimierung-der-neue-standard-fuer-digitale-sichtbarkeit/` and `springerprofessional.de/en/generative-engine-optimization-sichtbar-in-ki-systemen/52100740`. Query `Horizont OR "W&V" … KI-Suche Werbung ChatGPT Anzeigen Marken 2026` returned `horizont.net/medien/nachrichten/openai-so-sieht-die-europaeische-werbeoffensive-von-chatgpt-aus-235468`, `wuv.de`, `t3n.de`, `onlinemarketing.de` — trade press on a European ad rollout that no English pull surfaced. Query `OMR Reviews KI Sichtbarkeit Software Bewertungen Kategorie 2026` returned `omr.com/en/reviews/category/ai`, a DACH review corpus with its own GEO category and inclusion criteria, and `omr.com/de/reviews/b2b/growthhub/ki-sichtbarkeit-2026-b2b-tech-dach`.
- **B7 — The search surface is US-only.** Stated in the tool's own description. B6's EU gap is therefore measured by the instrument that causes it: the German queries reached EU sources only because the query text was German. Every absence recorded against an EU question inherits this.
- **B8 — Filings: thin EDGAR terms, and no non-US registry.** Both fetches ran today against `efts.sec.gov/LATEST/search-index?q=`. `"generative engine optimization"` over 2026-01-01→2026-09-22 returned 41 hits (Change Agents Corporation 8-K, Direct Digital Holdings 8-K, TechTarget 8-K); `"answer engine optimization"` returned 16 (REZOLVE AI PLC 6-K, Locafy Ltd 6-K, HubSpot ×4). The endpoint works; the three-term list is the binding constraint, and `"AI search visibility"`, `"AI Overviews"`, `"LLM optimization"`, `"share of voice"` are untested. Query `Companies House … AI visibility startup filing accounts 2026 GEO platform` returned only Companies House's own annual report — no query reaches a non-US registry, though `find-and-update.company-information.service.gov.uk` indexes filing histories. Related: `trust-rubric.md` rates a court exhibit tier 2 and no court channel exists; query `courtlistener docket publishers v AI search engine citation lawsuit 2026 exhibit` returned `courtlistener.com/docket/69280523/dow-jones-company-inc-v-perplexity-ai-inc/`, `/69879510/in-re-openai-inc-copyright-infringement-litigation/`, `/71970530/us-news-world-report-lp-v-openai-inc/`.
- **B9 — The Lane D venue set misses the venues that publish this work.** The book lists arXiv, ACL Anthology, Semantic Scholar, Scholar. ACL Anthology indexes no SIGIR, CIKM, WSDM, RecSys, WWW or KDD paper, and no security venue. Query `SIGIR OR CIKM OR RecSys 2026 generative engine optimization ranking manipulation LLM recommendation` returned `dl.acm.org/doi/10.1145/3767695.3769522` (SIGIR-AP) and `arxiv.org/pdf/2504.05804` (StealthRank), neither reachable from the listed venues.
- **B10 — Negative results are not queried for.** Query `"we tried" GEO "didn't work" OR "no results" AI visibility tool waste reddit 2026` returned nine results — four listicle or off-topic (`nogood.io` ×2, `mexc.com` ×2), zero practitioner negative posts. The only negative evidence surfaced today came from the academic channel: `arxiv.org/pdf/2607.14035` (critical survey, 45 studies, "no technique shows a stable, cross-platform effect") and `arxiv.org/pdf/2606.12439`. Survivorship is scheduled against in `plan.md` by counting screens; no query shape hunts the failures themselves.
- **B11 — Buyer-side voices are sell-side-shaped and skew enterprise.** S7 reaches only earnings calls. Query `CMO survey 2026 AI search spend budget allocation Gartner OR Duke OR WFA OR ISBA` returned `gartner.com/en/newsroom/press-releases/2026-05-11-gartner-2026-cmo-spend-survey-finds-cmos-allocate-15-point-3-percent-of-marketing-budgets-to-ai-but-only-30-percent-are-ready-to-scale-ai-capabilities` — n=401, respondents "the vast majority … over $1 billion" revenue, so it reads enterprise cells only. Query `small business SMB "AI visibility" tool pricing adoption survey 2026` returned SMB publishers absent from `channels.md`: `bluevine.com/blog/small-business-ai-trends-report-2026`, `sbecouncil.org/2026/04/25/the-ai-tools-small-businesses-are-using/`. Query `"generative engine optimization" jobs Europe …` returned `freelancer.com/jobs/generative-engine-optimization` and `upwork.com` — the SMB-side S1 channel, unlisted.
- **B12 — Staleness and stale tokens are built into the date rule.** The default `after:2026-01-01` admits material the staleness rule flags on arrival at 2026-06-22: the Gartner survey above was fielded January–March and published 2026-05-11; query `Google merges AI Overviews and AI Mode "one AI search experience" May 2026 announcement` returned `blog.google/products-and-platforms/products/search/search-io-2026/` dated 2026-05-19, a blog path C7 does not cover (C7 pins `blog.google/products/ads-commerce/` only) and an event that makes the grid's `"AI Overviews" OR "AI Mode"` split a stale token pair; Amazon's prompts reached US general availability 2026-03-25.
- **B13 — The roster rule is gameable by PR and excludes quiet vendors.** Query `Brandlight OR Athena OR ZipTie AI visibility platform funding 2026` returned one Series A covered at `pulse2.com/brandlight-30-million-series-a-raised-for-enterprise-ai-visibility-platform/`, `finance.yahoo.com/news/ai-market-shelf-just-got-140000437.html`, `calcalistech.com/ctechnews/article/h18lbwqpbx` and `contentgrip.com/brandlight-series-a-ai-adtech/` — four publishers, one announcement. Limb (a) survives on the "same single origin" clause; limb (b) does not, since a self-submitted `crunchbase.com/organization/brandlight-6a6b` profile is tier 5 and alone satisfies "a filing **or** a funding record at tier 2 or 5". Conversely names that surfaced today only inside listicles or a single review corpus — Superlines and Relixir at `omr.com/en/reviews/category/ai`, ZipTie and Positive Surfer via `nicklafferty.com/blog/best-ai-visibility-optimization-platforms/` — are screened out by a rule written for listicle hygiene, not vendor exclusion.

## 6. Verdict per file

- `channels.md` — **amend**, 8 additions. No row is wrong; the set has holes at EU enforcement, archives, courts, ACM and security venues, and SMB-side demand.
- `query-book.md` — **amend**, 8 amendments. Two are corrections (exclusion scope, `-"vs"`); the rest additions.
- `shortlist.md` — **amend**, 3 new clusters, 1 rule amendment, 2 pull-list additions.

### Amendments to `channels.md` — paste as rows in its own format

| # | Channel | URL | Yields | Refresh | Access | Bias | Tier | Lane | Pass | Signal |
|---|---|---|---|---|---|---|---|---|---|---|
| C60 | EU DSA enforcement and ad repositories | `transparency.dsa.ec.europa.eu/`; `digital-strategy.ec.europa.eu`; `cnam.ie` | Designations, proceedings; mandated ad records and API shape | Continuous | untested 2026-09-22 | EU-designated services only; field coverage varies | 2 | B, C, D | 2 | S11 |
| C61 | Wayback Machine | `web.archive.org` | Prior state of a withdrawn or edited platform page | Continuous | fetch refused 2026-09-22 → ext | Capture gaps; robots-era exclusions | 3 | A, B, C | 2, 4 | — |
| C62 | CourtListener / RECAP | `courtlistener.com` | Dockets and exhibits in publisher-versus-engine litigation | Daily | 200 | US dockets only; exhibits often sealed | 2 | B, D, E | 2, 4 | S11 |
| C63 | ACM DL, OpenReview, USENIX, IEEE, DBLP | `dl.acm.org`; `openreview.net`; `usenix.org`; `ieeexplore.ieee.org`; `dblp.org` | SIGIR/CIKM/RecSys/WWW and security-venue papers | Per conference | mixed, paywalls | Venue lag; ACM partly gated | 3 | D, E | 5 | — |
| C64 | EU trade press | `horizont.net`; `wuv.de`; `t3n.de`; `onlinemarketing.de` | EU rollout and ad-market coverage, German-language | Daily | 200 | Announcement-led; DACH-weighted | 5 pointer | A, B | 2, 4 | — |
| C65 | OMR Reviews | `omr.com/en/reviews/category/ai` | DACH B2B review corpus; its own GEO category criteria | Continuous | 200 | DACH only; same farming risk as C36 | 5 | A, E | 3, 8 | S4 |
| C66 | Buyer-side surveys and freelance marketplaces | `gartner.com/en/newsroom`; `bluevine.com/blog`; `sbecouncil.org`; `upwork.com`; `freelancer.com` | CMO spend allocations; SMB adoption bands; posted freelance rates | Annual / continuous | 200 / untested | Self-report; Gartner enterprise-skewed; rate is an asking rate | 4–5 | A, E, F | 8 | S1, S6, S7, S11 |
| C67 | Non-US company registries | `find-and-update.company-information.service.gov.uk` | Filing histories and accounts for UK-registered vendors | Continuous | untested 2026-09-22 | UK only; small-company exemptions hide detail | 2 | A, E | 3 | S3 |

### Amendments to `query-book.md`

1. Exclusion block: prepend "applies to open web search only; never to a `site:`- or `allowed_domains`-pinned query", and delete `-"vs"` and `-inurl:-vs-` from the tier-7 operator row.
2. Set O append: `"share of model"`, `"AI share of voice"`, `"AI SOV"`, `AIO`, `GSO`, `AISEO`, `"AI search optimization"`, `"AI Overviews optimisation"`, `"citation economy"`, `"AI discoverability"`.
3. Set P append: `"ChatGPT Ads"`, `"Advertise in ChatGPT"`, `"Conversational Discovery"`, `"Highlighted Answers"`, `"AI-Powered Shopping Ads"`, `"Business Agent for Leads"`, `"Offer Highlights"`, `"sponsored recommendations"`, `"Sponsored Products prompts"`, `"Sponsored Brands prompts"`, `"Alexa for Shopping"`.
4. New alias set **X** non-English: `"KI-Sichtbarkeit"`, `"Generative Engine Optimierung"`, `"KI-Suche"`, `"Werbung in ChatGPT"`, `"optimisation pour moteurs génératifs"`, `"visibilité IA"`, `"visibilidad en IA"` — run against C64, C65 and open EU search.
5. New grid rows: `A × Perplexity` `site:perplexity.ai (publisher OR citation OR sources)`; `A × Copilot` `site:learn.microsoft.com/advertising copilot answers citation`; `A × Amazon` `site:advertising.amazon.com Rufus OR "Alexa for Shopping" organic placement`; `C × Claude` `site:docs.anthropic.com MCP commerce OR payments OR checkout`; `C × Perplexity` `site:perplexity.ai shopping OR checkout OR merchant`. Google rows: add `blog.google/products-and-platforms/products/search/` to the pinned paths and `Google "AI Search" merged surface` as a token beside the `"AI Overviews" OR "AI Mode"` pair.
6. New buyer-size overlay, parallel to the vertical overlays: SMB `"small business" OR SMB OR freelance OR "under 100 employees"`; mid-market `"mid-market" OR "100-999 employees"`; enterprise `enterprise OR "Fortune 500" OR "global brand"`.
7. Negative-result row: `site:reddit.com/r/SEO ("no lift" OR "no change" OR "didn't move" OR "waste of money" OR "cancelled" OR "churned") ("AI visibility" OR GEO OR AEO)`, same on `/r/bigseo` and `/r/PPC`; `hn.algolia.com/api/v1/search?query=%22generative+engine+optimization%22` read for dissent; `("we tested" OR "our experiment") ("null result" OR "no correlation") LLM citation`.
8. EDGAR full-text term list append: `"AI search visibility"`, `"AI Overviews"`, `"LLM optimization"`, `"share of voice"`, `"answer engine"`; plus a UK leg — `find-and-update.company-information.service.gov.uk` company-name search per rostered vendor. Academic venue list append: `dl.acm.org` (SIGIR, CIKM, WSDM, RecSys, WWW, KDD), `openreview.net`, `usenix.org`, `ieeexplore.ieee.org`, `dblp.org`; keyword rows `"stealth" ranking manipulation LLM`, `"web agent" security benchmark`, `"retrieval poisoning" RAG`. Date rule: `after:2026-06-22` for surface-state questions, `after:2026-01-01` retained for census, funding and filings.

### Amendments to `shortlist.md` — new clusters, in its row format

| id | lane | target | pulls | tier | moves | done when |
|---|---|---|---|---|---|---|
| P2-c10 | B, C | EU enforcement and mandated ad repositories | `transparency.dsa.ec.europa.eu/` schema and query interface; `digital-strategy.ec.europa.eu` designation and proceedings pages; `cnam.ie`; each P1 engine's own EU-transparency page; `petsymposium.org/popets/2026/popets-2026-0059.php` | 2 regulator, 3 platform | H2, H12, H13, HE1 | For each designated engine: whether an ad repository is published and machine-readable, and which fields it exposes — yes/no per engine or `unknown — checked <pages> 2026-09-22` |
| P2-c11 | B, E | Litigation dockets and exhibits | `courtlistener.com` dockets naming a P1 or P2 engine and a publisher; complaint and exhibit PDFs where unsealed | 2 filed | H1, H3, H12 | Each docket recorded with case number, court and date; every number quoted verbatim with the exhibit it sits in; sealed items recorded as sealed, never as absent |
| P8-c1 | F, E | Demand-signal sweep per cell — S1, S4, S5, S6, S8, S10, S11 | `linkedin.com/jobs`, `indeed.com`, `upwork.com`, `freelancer.com` per alias × buyer-size overlay; `g2.com`, `capterra.com`, `omr.com` review velocity; `sam.gov`, `contractsfinder.service.gov.uk`, `ted.europa.eu`; `gartner.com/en/newsroom`, `bluevine.com/blog`, `sbecouncil.org` | 2–5 | H4, H7, H9 | Every one of the 27 cells carries a checked-or-blank mark per signal with the exact query recorded; no cell inferred from a vendor target-customer page |

Pull-list additions: **P2-c5** — a withdrawal check via `web.archive.org` (browser extension) on Perplexity's ad and publisher-programme pages, capturing the prior wording with its capture date. **P5-c7** — extend the countermeasure check from the P1 engines to Perplexity, Copilot and Amazon.

**Roster-rule amendment (P3 preamble).** Limb (b) currently admits a single tier-5 self-submitted profile. Replace with: "(b) it has a **filing** at tier 2, **or** a funding record at tier 5 corroborated by one source that is not the vendor, its investors, or a syndication of their announcement." Add a third limb so a listicle-only name is not lost: "(c) a name appearing only in listicles or a single review corpus is recorded in a **held** list with the pages it appeared on, counted in the screened total, and rostered if any later pull produces an independent source."

## 7. Caveats

- One search surface, one machine, one day. The two fetch-based access notes (EDGAR 200 with results, Wayback refused) are single observations, not a channel's steady state. Blind spots are the ones this method could find: an alias no one used in a 2026-09-22 result set, or a channel no query shape reaches, stays invisible to a red team built from the same surface.
- Vendor and publisher names above are addresses a query landed on 2026-09-22, recorded so an amendment can be pasted. None is rostered, tiered, or asserted to be a competitor; the census is Pass 3 and tiers are assigned at pull time.
- The coverage matrix scores the presence of a query or cluster, not its adequacy: a cell marked `q+c` can still return nothing. §6 lists amendments only — nothing here edits the three reviewed files, and no amendment carries a date, an order, or a cost.
