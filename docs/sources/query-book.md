# Query book

**Amended 2026-09-22 per `query-book-redteam.md`: all eight §6 amendments applied — 1 exclusion scope and `-"vs"` deletion (correction, B1), 2 set O append (B2), 3 set P append (B3), 4 new alias set X non-English (B6), 5 new grid rows A×Perplexity / A×Copilot / A×Amazon / C×Claude / C×Perplexity plus the Google merged-surface token (B12), 6 buyer-size overlay, 7 negative-result query set (B10), 8 EDGAR and academic venue appends plus the split date rule (B8, B9, B12). This file carries no strike-through convention, so the two corrected rows are replaced outright and the change is named here.**

Pass 1, task P1-a, compiled 2026-09-22. The query set for Passes 2–5. Cluster ids are `shortlist.md`'s; channel ids are `channels.md`'s; aliases are `../method/glossary.md`'s; exclusions are `../method/trust-rubric.md`'s discard-on-sight list turned into operators. Red-teamed by a second agent before Pass 2 spawns (`plan.md` Pass 1 detail).

Queries are written for two surfaces: **web search**, where `blocked_domains` and `allowed_domains` are the real filter and operators are advisory; and **site-restricted fetch**, where `site:` or a direct path is the filter. Where a query is site-restricted the site is named.

## Alias sets — expand every organic query across set O, every paid query across set P

| Set | Terms |
|---|---|
| **O** organic | `"generative engine optimization"`, `"generative engine optimisation"`, `GEO` (only with a disambiguator — see below), `"answer engine optimization"`, `AEO`, `LLMO`, `"LLM SEO"`, `"AI SEO"`, `"AI visibility"`, `"AI search visibility"`, `"brand visibility in AI"`, `"LLM visibility"`, `"citation rate"`, `"share of voice in AI answers"`; **appended 2026-09-22** `"share of model"`, `"AI share of voice"`, `"AI SOV"`, `AIO`, `GSO`, `AISEO`, `"AI search optimization"`, `"AI Overviews optimisation"`, `"citation economy"`, `"AI discoverability"` |
| **P** paid | `"ads in ChatGPT"`, `"sponsored answers"`, `"sponsored results"`, `"sponsored prompts"`, `"sponsored follow-up questions"`, `"AI ads"`, `"conversational ads"`, `"ads in AI Overviews"`, `"ads in AI Mode"`, `"AI ad inventory"`, `"Copilot ads"`, `"rate card"`; **per-engine product names appended 2026-09-22** — OpenAI `"ChatGPT Ads"`, `"Advertise in ChatGPT"`; Google `"Conversational Discovery"`, `"Highlighted Answers"`, `"AI-Powered Shopping Ads"`, `"Business Agent for Leads"`; Microsoft `"Offer Highlights"`, `"sponsored recommendations"`; Amazon `"Sponsored Products prompts"`, `"Sponsored Brands prompts"`, `"Alexa for Shopping"` |
| **C** agentic | `"agentic commerce"`, `"agentic checkout"`, `"agent payments"`, `"Agentic Commerce Protocol"`, `ACP`, `AP2`, `"Universal Commerce Protocol"`, `x402`, `"merchant of record"`, `"product feed"` |
| **D** manipulation | `"GEO manipulation"`, `"ranking manipulation"`, `"corpus seeding"`, `"indirect prompt injection"`, `"content poisoning"`, `"LLM recommendation bias"`, `"brand bias"`, `"listicle manufacture"`, `"comparison page"`, `llms.txt` |
| **E** measurement | `holdout`, `"geo split"`, `switchback`, `incremental`, `"incrementality"`, `"prompt set"`, `"sample size"`, `"methodology"`, `"before and after"` |
| **X** non-English, added 2026-09-22 | German `"KI-Sichtbarkeit"`, `"Generative Engine Optimierung"`, `"KI-Suche"`, `"Werbung in ChatGPT"`; French `"optimisation pour moteurs génératifs"`, `"visibilité IA"`; Spanish `"visibilidad en IA"` |

**Set X is the only route to the EU sources.** The search surface is US-only by its own description (`query-book-redteam.md` B7), so an EU source is reached only when the query text is itself non-English. Run set X against C64 (`horizont.net`, `wuv.de`, `t3n.de`, `onlinemarketing.de`), C65 (`omr.com`) and open EU search. An absence found only through English queries is not an absence; it is `unknown — checked <English queries only> 2026-09-22`.

**`GEO` is ambiguous** (`glossary.md`): it also means geographic. Never query bare `GEO`. Always pair: `GEO "AI search"`, `GEO "generative engine"`, `GEO ChatGPT`, `"GEO manager" marketing`. A result using GEO geographically is discarded on sight, not filed.

## Exclusions — the discard-on-sight list as operators

**Scope, corrected 2026-09-22 (B1): this block applies to open web search only. It never applies to a `site:`- or `allowed_domains`-pinned query.** On a pinned tier-2 or tier-3 domain the listicle risk is nil and the block discards primaries — `-inurl:best-` and `-inurl:top-` killed `g2.com/best-software-companies/top-ai`, and `-"best"` killed `help.openai.com/en/articles/6654000-how-to-use-chatgpt-effectively` and `help.openai.com/en/articles/12627856-publishers-and-developers-faq`, the page carrying OAI-SearchBot access and the `utm_source=chatgpt.com` referral tag. Within open web search, apply to every query unless the cluster's purpose is explicitly `evidence about category noise`.

| Rubric item | Operator |
|---|---|
| Listicle, roundup, affiliate comparison (tier 7) | `-"best" -"top 10" -"top 15" -"tools compared" -"alternatives" -inurl:best- -inurl:top- -inurl:alternatives -inurl:roundup -inurl:review-` — `-"vs"` and `-inurl:-vs-` **deleted 2026-09-22 (B1)**: engine-difference support pages and academic comparisons take the "vs" form, so the operator discarded the primary and the paper alike |
| "Studies show" with no link | `-"studies show" -"research shows" -"experts say"`; and on read, discard any figure whose sentence names no source |
| No n, no date window, no method | add set E terms as **requirements**, not options: `"sample size" OR "n =" OR "methodology" OR "date range"` |
| Percentage with no base | discard on read; no operator reaches it |
| Forecast presented as measurement | `-"market size" -"CAGR" -"forecast" -"projected to reach" -"2030" -"2032"` on every Pass 2–5 query; forecasts are pulled only by the Pass 6 sizing task, labelled as forecasts |
| Vendor measuring what it sells | not excluded — pulled and bias-flagged inline. Filtered only when it is also a listicle |

**Domain-level routing.** Prefer `allowed_domains` pinned to the channel (`openai.com`, `support.google.com`, `about.ads.microsoft.com`, `advertising.amazon.com`, `anthropic.com`, `arxiv.org`, `aclanthology.org`, `efts.sec.gov`, `eur-lex.europa.eu`, `cloudflare.com`, `httparchive.org`) over open web search. Where open search is unavoidable, set `blocked_domains` to the listicle farms the previous query returned — the block list is built during the pass and recorded in the cluster's `raw/` pull notes, not guessed in advance.

## Date rules

- **Split 2026-09-22 (B12).** Surface-state questions — what an engine ships, labels or charges for now — take `after:2026-06-22`. Census, funding and filings keep `after:2026-01-01`. The single default admitted material the staleness rule flags on arrival: a survey fielded January–March and published 2026-05-11 passes `after:2026-01-01` and is already stale as surface evidence.
- Default recency filter where neither applies: results published **2026**.
- Anything published **before 2026-06-22** (one quarter before today) is flagged `stale — published <date>` in the `raw/` header and re-checked against a current page before a compiled file cites it (`plan.md` staleness rule).
- Platform primary (C1–C12) is exempt from the recency filter: the changelog's own history is the evidence. Pull the dated post, not a summary of it.
- Academic (C47–C50) is exempt from the recency filter and subject to the harder rule: **record the model versions and test dates the paper used.** A 2024 result on a retired model is evidence about 2024.

## Lane × priority-1 engine — the core grid

Engine tokens: `ChatGPT OR OpenAI`; `Claude OR Anthropic`; `"AI Overviews" OR "AI Mode" OR Gemini OR Google`. Priority-2 tokens: `Perplexity`; `Copilot OR "Microsoft Advertising"`; `Rufus OR "Alexa for Shopping" OR "Amazon Ads"`.

**Google token correction, 2026-09-22 (B12).** `blog.google/products-and-platforms/products/search/search-io-2026/`, dated 2026-05-19, announces "one AI search experience". The `"AI Overviews" OR "AI Mode"` pair is therefore a possibly-stale token pair, not a live distinction: run `Google "AI Search" merged surface` beside it, and record which naming the engine's own page uses on the pull date rather than normalising to either.

| Lane × engine | Query (expand across the alias set named) | Finds |
|---|---|---|
| A × ChatGPT | `site:openai.com ChatGPT (search OR shopping OR citation OR publisher)`; open: `<O> ChatGPT citation` + exclusions | P2-c3, P2-c2 |
| A × Claude | `site:anthropic.com (commerce OR shopping OR recommendation OR search)`; `site:docs.anthropic.com search tool`; open: `<O> Claude recommendation brand` | P2-c5 |
| A × Google | `site:developers.google.com/search AI features guidance`; `site:support.google.com "AI Overviews"`; `site:blog.google/products-and-platforms/products/search/` (added 2026-09-22, C7 pins `blog.google/products/ads-commerce/` only); open: `<O> "AI Overviews" citation` | P2-c4, P2-c2 |
| A × Perplexity, added 2026-09-22 | `site:perplexity.ai (publisher OR citation OR sources)`; open: `<O> Perplexity citation publisher` | P2-c5 |
| A × Copilot, added 2026-09-22 | `site:learn.microsoft.com/advertising copilot answers citation`; open: `<O> Copilot answer citation brand` | P2-c6 |
| A × Amazon, added 2026-09-22 | `site:advertising.amazon.com Rufus OR "Alexa for Shopping" organic placement`; open: `<O> Rufus organic product recommendation` | P2-c6 |
| B × ChatGPT | `site:openai.com ads`; `site:help.openai.com ads`; open: `<P> ChatGPT advertiser "Ads Manager"` + `-"guide" -"complete guide"` | P2-c3 |
| B × Claude | `site:anthropic.com (advertising OR sponsored OR ads)`; open: `<P> Claude Anthropic advertising` — expect an absence; record it as `unknown — checked <queries> 2026-09-22` | P2-c5 |
| B × Google | `site:support.google.com/google-ads "AI Mode" OR "AI Overviews"`; `site:blog.google ads-commerce AI Mode format`; open: `<P> "AI Mode" format sponsored label` | P2-c4 |
| B × Perplexity | `site:perplexity.ai (advertising OR sponsored OR publisher)`; open: `<P> Perplexity advertising status 2026` | P2-c5 |
| B × Copilot | `site:about.ads.microsoft.com Copilot (ads OR checkout OR merchant)`; `site:ads.microsoft.com Merchant Center` | P2-c6 |
| B × Amazon | `site:advertising.amazon.com sponsored prompts`; open: `<P> Amazon sponsored prompts billable CPC` | P2-c6 |
| C × Claude, added 2026-09-22 | `site:docs.anthropic.com MCP commerce OR payments OR checkout`; `site:anthropic.com MCP commerce` | P2-c5, P2-c7 |
| C × Perplexity, added 2026-09-22 | `site:perplexity.ai shopping OR checkout OR merchant`; open: `<C> Perplexity shopping checkout merchant` | P2-c5, P2-c7 |
| C × all | `site:github.com agentic-commerce-protocol spec`; `site:docs.stripe.com agentic commerce`; `<C> specification "open standard" -"guide" -"explained"` | P2-c7 |
| C × Google / Microsoft / Amazon | `AP2 "Agent Payments Protocol" specification site:google`; `"Universal Commerce Protocol" site:microsoft.com OR site:about.ads.microsoft.com`; `site:advertising.amazon.com checkout` | P2-c7, P2-c6 |
| D × all | see the academic set below; plus `site:developers.google.com/search spam policies scaled content`; `site:openai.com usage policies`; `site:anthropic.com usage policy` | P5-c7 |
| E × all | `<O> <E>` together: `"AI visibility" ("holdout" OR "incrementality" OR "prompt set")` + exclusions | P2-c1, P4-c4 |
| F × all | `<O> ("we changed" OR "what we did" OR "our team") -"guide"`; plus the earnings and agency queries below | P4-c1, P4-c2, P4-c5 |

## Cluster query sets

| Cluster | Queries |
|---|---|
| P2-c1 | `site:aisearch.similarweb.com methodology`; `site:datos.live "state of search"`; `site:sparktoro.com clickstream methodology`; `site:gs.statcounter.com methodology`; `"clickstream" "panel" AI assistant share methodology 2026 -"best" -"market size"`; `Comscore AI assistant share panel 2026` |
| P2-c2 | `site:blog.cloudflare.com crawl-to-refer`; `site:radar.cloudflare.com ai-insights`; `site:httparchive.org report`; `site:platform.openai.com bots`; `site:developers.google.com/search common crawlers` |
| P2-c8 | `site:business.adobe.com AI traffic retail quarterly`; `site:salesforce.com/news shopping index AI`; `site:shopify.com/news AI orders` |
| P2-c9 | `site:eur-lex.europa.eu 32024R1689 transparency`; `site:eur-lex.europa.eu 32022R2065 advertising`; `site:ftc.gov endorsement guides disclosure AI`; `site:gov.uk CMA AI search market`; `site:asa.org.uk ruling AI ad label` |
| **P3-c0 discovery** | `<O> platform pricing -"best" -"top" -"alternatives"` (`-"vs"` deleted 2026-09-22 with the operator row); `site:g2.com AI visibility category` — pinned, so the exclusion block does not apply and `g2.com/best-software-companies/top-ai` and `company.g2.com/news/` category pages are in scope; `site:capterra.com AI search visibility`; `site:crunchbase.com "AI visibility"`; `efts.sec.gov` full-text: `"generative engine optimization"`, `"answer engine optimization"`, `"AI visibility"`, plus **appended 2026-09-22** `"AI search visibility"`, `"AI Overviews"`, `"LLM optimization"`, `"share of voice"`, `"answer engine"`; **UK leg appended 2026-09-22** — `find-and-update.company-information.service.gov.uk` company-name search per rostered vendor, filing history and accounts; `site:eu-startups.com "AI visibility" raises`; `site:pymnts.com "AI visibility" funding`; `"<O>" (raises OR "Series A" OR "Series B" OR seed) 2026 -"best"`; `site:linkedin.com/jobs "generative engine optimization"`; `hn.algolia.com/api/v1/search?query=generative+engine+optimization`; conference speaker lists per P4-c3 |
| P3-c1–c3 | Per rostered vendor: `site:<vendor> pricing`; `site:<vendor> customers OR "case study"`; `site:<vendor> methodology OR "how it works"`; `site:<vendor> changelog`; `site:<vendor> careers` |
| P3-c4 | `site:ahrefs.com brand radar pricing`; `site:semrush.com AI toolkit pricing`; `site:similarweb.com AI search product`; `<incumbent> "AI visibility" add-on price` |
| P3-c5 | `"<O>" agency (services OR retainer OR "pricing") -"best" -"top" -"agencies to"` ; `site:<agency> "<O>" pricing` |
| P4-c1 | `efts.sec.gov` full-text over 8-K/10-Q/10-K: `"AI search"`, `"AI Overviews"`, `"ChatGPT"` + `traffic`; `site:fool.com earnings call transcript "AI search" traffic`; `<brand> investor relations transcript "AI"` |
| P4-c2 | `"<O>" ("case study" OR "client results") ("baseline" OR "holdout" OR "control") -"best" -"top"`; `site:<agency> results AI visibility` |
| P4-c3 | `site:marketingaiinstitute.com agenda`; `site:ana.net conference AI marketers agenda`; `"GEO conference" 2026 agenda speakers`; `"content marketing world" agenda generative engine optimization` |
| P4-c4 | `site:<vendor> "case study"` for every rostered vendor; then filter on set E terms present |
| P4-c5 | `site:reddit.com/r/SEO "AI visibility" results`; `site:reddit.com/r/bigseo generative engine optimization test`; `site:reddit.com/r/PPC "ads in ChatGPT"`; `hn.algolia.com/api/v1/search?query=<alias>` |
| P4-c6 | `site:ppc.land AI ads`; `site:searchengineland.com AI Mode ads`; each result read only for the primary it links |
| **Negative results, added 2026-09-22 (B10)** | `site:reddit.com/r/SEO ("no lift" OR "no change" OR "didn't move" OR "waste of money" OR "cancelled" OR "churned") ("AI visibility" OR GEO OR AEO)`, and the same on `/r/bigseo` and `/r/PPC`; `hn.algolia.com/api/v1/search?query=%22generative+engine+optimization%22` read for dissent, not for endorsement; `("we tested" OR "our experiment") ("null result" OR "no correlation") LLM citation`; academic leg `"generative engine optimization" survey ("no stable effect" OR "did not replicate")`. Feeds P4-c5, P5-c1, P5-c4 |
| **Buyer-side, added 2026-09-22 (B11)** | `CMO survey 2026 AI search spend budget allocation (Gartner OR Duke OR WFA OR ISBA)`; `small business SMB "AI visibility" tool pricing adoption survey 2026`; `site:bluevine.com/blog small business AI trends`; `site:sbecouncil.org AI tools small business`; `site:upwork.com "generative engine optimization"`; `site:freelancer.com/jobs generative-engine-optimization`. Every hit is tagged with the respondent revenue band the publisher states, or `unknown — checked <page> 2026-09-22`. Feeds P8-c1 |
| **EU, added 2026-09-22 (B5, B6)** | Set X against C64 and C65; `site:transparency.dsa.ec.europa.eu research API`; `site:digital-strategy.ec.europa.eu DSA designation search engine`; `site:cnam.ie Digital Services Coordinator`; `site:omr.com/de/reviews KI-Sichtbarkeit`. Feeds P2-c10 |
| **Courts, added 2026-09-22 (B8)** | `site:courtlistener.com docket (publisher OR "Dow Jones" OR "US News") v (OpenAI OR Perplexity OR Google)` (403→ext, use the Chrome extension); complaint and exhibit PDFs where unsealed. Feeds P2-c11 |
| **Archive, added 2026-09-22 (B4)** | `web.archive.org/web/2025*/perplexity.ai/hub/blog/*` and the same over each engine's ad and publisher-programme paths — browser extension only, plain fetch refused 2026-09-22. Every capture recorded with its capture date, never with the pull date. Feeds P2-c5 |

## Vertical overlays — append to any lane query where the cluster is vertical-scoped

| Vertical | Tokens |
|---|---|
| Skincare and beauty (anchor) | `skincare OR beauty OR cosmetics OR serum OR sunscreen` |
| B2B SaaS | `"B2B SaaS" OR "best tool for" OR software OR CRM OR "vendor selection"` |
| High-CPA regulated | `insurance OR "credit card" OR supplements OR loans OR "personal injury"` |

## Buyer-size overlay — added 2026-09-22 per B11, parallel to the vertical overlays

| Buyer size | Tokens |
|---|---|
| SMB | `"small business" OR SMB OR freelance OR "under 100 employees"` |
| Mid-market | `"mid-market" OR "100-999 employees"` |
| Enterprise | `enterprise OR "Fortune 500" OR "global brand"` |

Both overlays serve Pass 8 cell reads and Pass 5's H14 density comparison. A source that does not itself name the vertical, or the buyer size, is **not** assigned to it (`demand-signals.md` cell-attribution rule) — it is recorded against the cell as `unknown — checked <query> <date>`. Before the overlay existed, no signal row could be cut SMB / mid / enterprise from its query alone, which is why H4, H7 and H9 had no evidence route.

## Academic set — Lane D, clusters P5-c1 to P5-c7

Venues to combine with the keyword column: `arxiv.org` (cs.IR, cs.CL, cs.CR listings), `aclanthology.org` (ACL, EMNLP, NAACL, EACL, COLING, WWW-adjacent), `semanticscholar.org` (citation trails and replication), `scholar.google.com` (cited-by counts and grey literature).

**Appended 2026-09-22 per B9.** ACL Anthology indexes no SIGIR, CIKM, WSDM, RecSys, WWW or KDD paper and no security venue, so the four venues above could not reach the work this lane needs. Add C63: `dl.acm.org` (SIGIR, CIKM, WSDM, RecSys, WWW, KDD — 403→ext), `openreview.net`, `usenix.org`, `ieeexplore.ieee.org` (browser user-agent), `dblp.org` as the index that names which venue a paper actually appeared in.

| Keyword combination | Cluster |
|---|---|
| `"generative engine optimization" survey` / `"generative engine optimization" benchmark` | P5-c1, P5-c4 |
| `"ranking manipulation" "generative engine"` / `GEO-Bench` | P5-c1 |
| `LLM recommendation "brand bias"` / `"incumbent advantage" LLM recommendation` | P5-c1, P5-c4 |
| `"recommendation agents" GEO risk` / `SafeGEO` | P5-c1, P5-c7 |
| `"indirect prompt injection"` `web agent` `red-team` | P5-c6 |
| `"agent data injection"` / `"out-of-band defenses" prompt injection` | P5-c6 |
| `"content poisoning"` `retrieval augmented generation` `search` | P5-c1, P5-c3 |
| `defense OR defence "generative engine optimization" manipulation` | P5-c7 |
| `llms.txt` adoption measurement | P5-c5 |
| `review manipulation` `LLM` `product recommendation` | P5-c2 |
| `"stealth" ranking manipulation LLM` — added 2026-09-22 | P5-c1, P5-c3 |
| `"web agent" security benchmark` — added 2026-09-22 | P5-c6 |
| `"retrieval poisoning" RAG` — added 2026-09-22 | P5-c1, P5-c6 |

Seeds returned by these combinations on 2026-09-22, recorded with the URL they were found at, not inherited as conclusions: `arxiv.org/abs/2606.17443`, `arxiv.org/html/2606.12439v1`, `arxiv.org/html/2607.14035v1`, `arxiv.org/pdf/2605.29107`, `arxiv.org/pdf/2606.28356`, `arxiv.org/pdf/2605.21948`, `arxiv.org/pdf/2607.05120`, `arxiv.org/pdf/2606.26479`, `arxiv.org/pdf/2605.11868`, `arxiv.org/pdf/2605.16471`.

For each paper, the intake question set is fixed: venue and review status; code, data or prompt set published; model versions tested; test dates; whether the authors sell the thing measured. These set the tier per `trust-rubric.md`'s academic table before anything else is read.

## Caveats

- Operators are advisory on every web-search surface tested. `blocked_domains` is the only filter that reliably holds; the exclusion strings above reduce listicles, they do not remove them. The screened count absorbs the rest.
- The listicle block list is built during a pass from what the queries actually return, not pre-guessed. A pre-guessed block list hides the farms it does not know about.
- `GEO` disambiguation is the single highest-cost query defect in this book. Every bare `GEO` query returns geographic results and burns a search.
- Absence queries (B × Claude, and any engine where the product is expected not to exist) must be recorded as `unknown — checked <exact queries> 2026-09-22`. An absence with no query list is not evidence of absence (`hypotheses.md` caveats).
- Coverage gaps from `query-book-redteam.md` §2 that these amendments close: A × Perplexity, Copilot and Amazon, and C × Claude and Perplexity, now carry grid rows; D × priority-2 engines is closed in `shortlist.md` by the P5-c7 pull-list extension, not here. The vertical columns are closed by `shortlist.md`'s P8-c1 and the Pass 4 per-vertical tagging rule, since a vertical is a cluster scope, not a query.
- Residual and recorded, not closed: H16 forecast queries stay routed to the Pass 6 sizing task, which is outside this book's Passes 2–5 remit; S12's brand sample frame is `panel-protocol.md`'s, not a query. Both `unknown — checked query-book-redteam.md §3, §4 2026-09-22`.
- Three priority-1 engine consumer surfaces are off-limits to this task's browsing while the Pass 10 sampler owns those tabs. Every engine query above is answered from the engine's own documentation domain, not from its chat surface.
