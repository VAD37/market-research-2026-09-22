# Glossary

Set 2026-09-22. The category's terms, defined once. Every file in `docs/` uses these words in these senses; a file needing a different sense defines it inline and says why. Authority: root `CLAUDE.md` > `scope.md` > `plan.md` > `trust-rubric.md` > this file. This file adds no rules and holds no facts; it fixes meanings.

## The three metrics — fixed, never crossed

`plan.md` names the failure mode: visibility conflated with traffic conflated with sales. Every compiled claim names which of the three it is, in the sentence carrying the number.

| | **Visibility** | **Traffic** | **Sales** |
|---|---|---|---|
| Definition | Brand, product or domain appears inside a generated AI answer | Session on the brand's own property whose referrer is an AI surface | Revenue or conversion event attributed to an AI surface |
| Unit | Appearances per n runs of a fixed prompt set | Sessions, users or clicks per period, per referrer host | Currency per period; or conversions, conversion rate, AOV |
| Stamped with | Engine, surface, prompt-set version, date, n | Referrer host, date window, analytics tool | Attribution model, date window, order count |
| Measured by | Running a fixed prompt set n times and counting | Brand analytics referrer or UTM; server logs; clickstream panel | Order data joined to referrer, UTM or agentic-checkout ID |
| Is NOT | Traffic. Classical SERP rank. Ad impressions. Awareness | Visibility. Crawler or bot requests from an AI vendor's crawler | Traffic. Visibility. Vendor-modelled "influenced revenue" |
| Conflation to refuse | One screenshot as proof; undisclosed prompt set behind a score | Referral read as influence; zero-click answers leave no referral | Attributed revenue reported as incremental revenue |

**Crossing rule.** A claim starting at one metric and concluding at another states the link and grades it against the `plan.md` evidence bar; an ungraded crossing is downgraded to the weaker metric. Visibility change alone is Bronze and is never cited as sales proof. **Attributed** = credited by an attribution model; **incremental** = the difference against a holdout. Only incremental supports the word "lift".

### Visibility has three sub-metrics — counted separately, never summed

| Term | Means | Counted as |
|---|---|---|
| Mention | Brand named in the answer text, no link | Mention rate |
| Citation | Answer links or footnotes the brand's domain | Citation rate |
| Recommendation | Answer names the brand as an answer to a buying-shaped prompt | Recommendation rate |

A citation without a mention, and a mention without a recommendation, are different results. A vendor "share of voice" or "AI visibility score" composite is recorded as that vendor's composite with its stated inputs, never as one of the three.

## Sub-markets

| Sub-market | Aliases in the wild | What is sold | Buyer |
|---|---|---|---|
| Organic recommendation | GEO, AEO, LLMO, AI visibility, AI SEO | Brand appears in AI answers unpaid | Brand marketing, SEO owner |
| Paid placement | AI ads, sponsored answers, sponsored results | Ad inventory inside AI surfaces | Media buyer |
| Agentic commerce | Transaction rails, agentic checkout | Checkout executed by the agent | E-commerce, payments |

Aliases stay as the source used them in `raw/`, unnormalised; compiled files put the sub-market name in column 1. GEO is ambiguous outside this repo (also geographic); inside `docs/` it means generative engine optimisation only.

## Lanes — research tracks. A lane is not a sub-market and not a segment

| Lane | Track | Core question |
|---|---|---|
| A | Organic recommendation | How does a brand get named in an answer |
| B | Paid placement | What inventory exists, what it costs, who buys |
| C | Agentic commerce | Who controls checkout inside the agent |
| D | Manipulation and gaming | How recommendation is steered, and whether it works |
| E | Measurement and proof — cross-cutting | Who demonstrates causal lift rather than correlation |
| F | Transition evidence — cross-cutting | What brands that moved actually changed |

Every pass in A–D feeds E and F. Lane D is research into manipulation, never execution of it.

## Evidence grades — assigned on intake against the seven-item evidence bar in `plan.md`

| Grade | Standard | Handling |
|---|---|---|
| Gold | Holdout, geo-split or switchback. Causal | Cite as proof |
| Silver | Pre and post, baseline plus an unaffected control metric | Cite as evidence, labelled correlational |
| Bronze | Visibility or mention-rate change only, no revenue link | Cite as visibility only |
| Fools gold | Revenue claim, no baseline or no control | Cite only as evidence of category noise |

## Source labels, tiers, grades — three independent axes

| Label kind | Means |
|---|---|
| vendor-reported | The seller published it about its own product or customers |
| analyst-derived | A third party computed it from other inputs |
| filed | In a regulatory, court or funding filing |
| company-stated | A company said it about itself outside a filing |
| measured-by-us | Produced by our own pull or panel run, output in `raw/` |

**Tier** = the 1–7 provenance score in `trust-rubric.md`, written on every `raw/` file as `tier: <n>` plus the reason if adjusted. Label says *what kind* of number it is; tier says *whether to keep it*; grade says *what a success story proves*. A claim can carry all three.

## Segment, engine, surface

| Term | Means |
|---|---|
| Segment axes | Sub-market × vertical × buyer size |
| Cell | One combination of the three axes — the unit demand is read against |
| Vertical | Skincare and beauty (anchor), B2B SaaS, high-CPA regulated |
| Buyer size | SMB, mid-market, enterprise — as the source defines them, definition quoted |
| Demand signal | A public, internet-only proxy from `demand-signals.md`, with its bias and tier |
| Cell read | One word: **spend**, **attention**, or **none**. Attention never stands in for spend |
| Screened / cleared | Candidates examined / candidates passing the evidence bar. Reported as a pair |
| Survivorship | Only winners publish. Stated once per scorecard, with the screened count |
| Engine | One assistant product, at a named model version where the surface discloses it |
| Engine priority | The 1–4 ranking in `plan.md`; an assumption until the Pass 2 share table reweights it |
| Surface | Where the answer is delivered. Three kinds, never merged |
| — consumer chat | The end-user chat product. **Primary** measurement surface |
| — API | Programmatic access. Secondary, always labelled. Not what users see |
| — search-integrated | An AI answer rendered inside a search results page |
| Prompt set | The fixed, versioned list of prompts a panel runs. Version recorded per sample |
| Run | One execution of one prompt against one engine, surface and date. n counts runs |
| Panel | Repeated runs of a prompt set on a schedule, per `panel-protocol.md` |

## Pipeline and sizing

| Term | Means |
|---|---|
| Pull | One retrieval of one source into one `raw/` file, dated and tiered |
| Pull method | fetch / browser extension / predecessor repo / manual |
| Raw pull | The `raw/` file itself. Verbatim, compression-exempt, never edited after the fact |
| Re-pull | A new `raw/` file for a source already pulled. The old file is kept with its date |
| Compiled file | Anything in `markets/`, `competitors/`, `customers/`, `findings/` |
| Oldest pull depended on | Earliest pull date among the `raw/` files a compiled file cites. One line per file |
| Stale | A pull older than one quarter at citation time. Re-checked, and the re-check dated |
| Predecessor repo | `D:\researchs\market-research\` — one channel, cited via `raw/`, never from memory |
| Bottom-up | Vendor count × disclosed price × disclosed customer count. The sizing method here |
| Top-down | A total divided down. Recorded with its author and base, never as the size |
| Forecast | A future number. Sits beside the size, labelled forecast, never as the size |
| Base period | The window a growth rate is measured over. No growth number without it |

**Structural checks** — four questions every `markets/` file answers or marks `unknown — checked <channel> <date>`: **substitute** (what the brand does instead; is "do nothing" the real competitor), **platform risk** (which engine ships native tooling making third-party vendors redundant), **incumbent bundling** (which SEO or analytics incumbent added this as a feature, at what price delta), **regulatory** (ad-disclosure rules inside AI answers in force as of the pull date).

## Caveats

- Sources use these words loosely. `raw/` keeps the source's word; the compiled file maps it and says so.
- Alias lists are as of 2026-09-22. A new alias found in a pull is appended here with its date.
- "AI visibility" is both a sub-market alias and a vendor product category. Compiled files say which.

### Additions, COMPILE-2, 2026-09-23

Per `biz-review-1-2026-09-23.md` §4 rows 9–10 and §7 row 20; `biz-review-solution-2026-09-23.md` §2 row 20; REV-BIZ-B (acronym coverage of the two briefs). Terms already in use across `findings/` and `plan.md`, fixed here so two files carry one meaning. Adds no rule and no market fact; the figures quoted are examples pointing at their raw file.

#### Metrics, readings and cell states

| Term | Means | Not to be confused with | Fixed where |
|---|---|---|---|
| Datos — "share of total desktop visits" (AI tools combined) | Visits to all AI tools as a share of a desktop panel's total visits; "US Q1 2025: 1.31% \| US Q1 2026: 1.65%" | `market-potential.md:41` labels the same series "share of desktop search events"; the raw heading reads "share of total desktop visits" | `raw/a-ppc-land-share-datos-q1-2026-2026-09-22.md` L33–34 |
| Datos — per-engine "% of desktop users" | Population penetration: share of panel users who used one engine; "34.80% of US desktop users used ChatGPT", Q1 2026 | `plan.md:183` labels it "share of total desktop visits"; it is not category share-of-visits (raw L80) | same raw, L38–40, L80 |
| MAU, engine-stated | Monthly active users as the engine words it; e.g. AI Mode "surpassed 1 billion monthly active users", 2026-05-19 | Not a share; definitions differ per engine (`market-potential.md:99`) | `raw/e-google-alphabet-user-counts-2026-09-23.md` L51 |
| Query share | Share of one engine's searches routed to a surface; Similarweb "Google AI Mode query share 0.34%", Jan–Apr 2026, all Google searches | Not MAU, not visit share; a different denominator | `raw/a-similarweb-share-zero-click-marketing-2026-09-22.md` L42 |
| Visit share | Share of a panel's total web visits; Datos AI Mode "0.16% US, 0.21% EU/UK, March 2026" | Query share (different population and panel); never averaged with it | `raw/a-ppc-land-share-datos-q1-2026-2026-09-22.md` L82 |
| MAU vs query share vs visit share — rule | Three denominators, three panels; carried side by side, never mixed or ranked against each other | "1B MAU" beside "0.34% query share" is not a contradiction (`biz-review-1` §4 row 10) | `market-potential.md:26`; `plan.md:185` |
| Metric moved | "yes — metric, from value, to value, window; or no" | A named change is not a moved metric | `plan.md:150` |
| Experimental (design) | "holdout, geo-split, switchback, pre/post with control" | Does not re-grade a case: pre/post with control stays Silver, correlational | `plan.md:151`, `:154` |
| Observational (design) | Any moved metric without one of the four designs above | "Metric moved" — a moved metric can be observational | `plan.md:151` |
| Action named, outcome unknown | "A case with no moved metric" | Not a null result; outcome is unmeasured, not absent | `plan.md:153` |
| Evidence class (a) | Metric moved, experimental design | Class (b) | `plan.md:155`; `proof-scorecard.md:182` |
| Evidence class (b) | Metric moved, observational | Class (a); a Silver can be (b) under R2 | same |
| Evidence class (c) | Action named, outcome unknown | A negative or null result, which is (a) or (b) with a moved metric | same |
| Reading R1 | Pre/post with control counted as class (a), experimental, per `plan.md:151` | Reading R2 | `proof-scorecard.md:182`; `STATE.md:213` |
| Reading R2 | Vendor pre/post with control counted as class (b), observational, per `proof-scorecard.md` C2 ("observational treated-vs-untreated, not randomized") | Reading R1; every three-count carries both, owner method decision open | `proof-scorecard.md:60`, `:182` |
| grade_raw | The grade as the census that opened the case assigned it | grade_rule1 | `plan.md:140` |
| grade_rule1 | Literal grading rule 1: any of items 1–7 absent on the case's own page caps it at Bronze | grade_raw; counts from Pass 11 use rule1 and cite raw beside | `plan.md:132`, `:140` |
| `none — checked`, strict | Every catalogue signal for the cell, including a still-blocked one, has been run; otherwise the cell is `blank` | Loose | `demand-map.md:121` |
| `none — checked`, loose | A channel blocked-and-logged in `blocked-channels.md` counts as checked; the cell reads `none` | Strict; both readings reported side by side, never merged | `demand-map.md:122`; `unknowns.md:116` |
| Tier-3 share, three ways | (1) all load-bearing claims; (2) excluding the Lane E case corpus; (3) excluding meta-claims with no raw tier — each itemised file:claim | A single percentage; "68.0%" and "44.4%" are different lists, both stand | `plan.md:512`; `unknowns.md:177–184` |

#### Acronyms used in the briefs — expansion, and the raw or regulator file that introduced the term

Token list from `findings/director-brief-2026-09-23.md` and `findings/executive-brief-2026-09-23.md` (all-caps tokens, read 2026-09-23) plus REV-BIZ-B's list. "Introduced in" is the raw file where the term first carries a figure in this repo; `expansion only, no source` where no raw introduces it. Repo task ids (AMEND-1, P4-r, COMPILE-2) and file names (STATE, INDEX) are not acronyms and are listed once.

| Acronym | Expansion | Introduced in (raw or regulator file) |
|---|---|---|
| ACP | Agentic Commerce Protocol — OpenAI and Stripe checkout spec, "Apache 2.0" | `raw/c-agentic-commerce-protocols-table-2026-09-22.md` |
| AEO | Answer engine optimisation — organic sub-market alias (Sub-markets table above) | `raw/a-vendor-census-c1-2026-09-22.md`; HubSpot 10-K names it, `raw/b-sec-hubspot-10k-2026-02-11-2026-09-23.md` |
| AI | Artificial intelligence | expansion only, no source |
| AIO | Google AI Overviews — the AI answer block on a Google results page; a search-integrated surface | `raw/b-google-ads-help-aio-ads-2026-09-23.md`; `raw/b-google-platform-summary-2026-09-22.md` |
| AI Mode | Google's conversational search tab; search-integrated surface distinct from AIO and the Gemini app | `raw/b-google-platform-summary-2026-09-22.md` |
| AP2 | Agent Payments Protocol — Google-led payment protocol; governance changed 2026-04-28 | `raw/c-agentic-commerce-protocols-table-2026-09-22.md` |
| ARR | Annual recurring revenue — subscription revenue annualised; "AI products surpassed $38 million in ARR" | `raw/a-semrush-filing-2026-09-22.md` |
| ATM (facility) | At-the-market equity offering; "maximum aggregate offering amount of $588,883" | `raw/b-sec-locafy-f3-2026-08-04-2026-09-23.md` |
| AOV | Average order value — a Sales unit (three-metrics table above) | `raw/b-reddit-advertiser-reports-repull2-2026-09-23.md` ("AOV ~$650") |
| ASA / CAP | UK Advertising Standards Authority / Committee of Advertising Practice | expansion only, no source — channel named at `findings/unknowns.md:87` |
| B2B | Business-to-business; "B2B SaaS" is a tracked vertical (Segment table above) | expansion only, no source |
| CAGR | Compound annual growth rate; "CAGR of 34.0%" | `raw/e-market-size-valuates-organic-2026-09-22.md` |
| CAPTCHA | Bot-challenge wall blocking a pull; logged in `method/blocked-channels.md` | expansion only, no source |
| CFR | Code of Federal Regulations (US); "16 CFR 255" endorsement guides, "16 CFR 465.2" fake-review rule | `raw/d-technique-census-c2-2026-09-22.md`; `markets/paid-placement.md:92` |
| CMA | Competition and Markets Authority (UK); fair-ranking order 2026-06-17 | `raw/b-uk-regulator-cma-2026-09-22.md` |
| CPA | Cost per acquisition; "high-CPA regulated" = vertical where customer acquisition is costly and regulated (cards, insurance, supplements) | expansion only, no source — vertical set in `method/scope.md` |
| CPC | Cost per click — ad billing unit; "$3–$5 USD per click" is bid guidance | `raw/b-openai-help-ads-basics-2026-09-23.md`; `raw/b-openai-ads-basics-pricing-2026-09-22.md` |
| CPM | Cost per thousand impressions; "Rates starting from just $3 CPM" | `raw/b-openai-help-ads-basics-2026-09-23.md`; `raw/b-kontext-advertisers-page-2026-09-23.md` |
| oCPC / oCPM | Outcome-optimised CPC / CPM billing | `raw/b-openai-help-ads-basics-2026-09-23.md` |
| CTR | Click-through rate — clicks ÷ impressions; a Traffic metric | `raw/b-seranking-chatgpt-ads-study-2026-09-23.md`; `raw/a-court-mdl-microsoft-ctr-data-2026-09-22.md` |
| DAU | Daily active users; AI Mode "over 75 million daily active users" | `raw/e-google-alphabet-user-counts-2026-09-23.md` L33 |
| DSA | EU Digital Services Act, Regulation (EU) 2022/2065; Art. 26 ad identification, Art. 27 recommenders, Art. 39 ad repositories | `raw/b-eu-dsa-ad-repositories-table-2026-09-22.md` |
| DSP | Demand-side platform; "Amazon DSP" buys ChatGPT inventory | `raw/b-amazon-ads-chatgpt-integration-2026-09-22.md` |
| DTC | Direct-to-consumer brand | `raw/b-reddit-advertiser-reports-repull2-2026-09-23.md` |
| ECF | Electronic case filing — US federal docket entry number; "ECF 1977-1" | `raw/a-court-mdl-microsoft-ctr-data-2026-09-22.md` |
| EDGAR | SEC Electronic Data Gathering, Analysis, and Retrieval — filings database; full-text search at efts.sec.gov | `raw/e-case-edgar-fulltext-results-2026-09-23.md` |
| ELOC | Equity line of credit; "purchase up to $10,000,000" | `raw/b-sec-change-agents-s1a-2026-09-16-2026-09-23.md` |
| EMARKETER | Research house publishing AI-ads and agentic forecasts (tier 5–6 here) | `raw/e-market-size-emarketer-aiads-paid-2026-09-22.md` |
| EU / UK / US / VN | European Union / United Kingdom / United States / Vietnam (panel IP localisation) | expansion only, no source — VN at `raw/e-claude-panel-2026-09-22.md` |
| FeatGEO | A GEO technique paper with a published pre/post (Table 4) | `raw/d-citationpref-featgeo-2026-09-22.md` |
| FTC | US Federal Trade Commission; endorsement and fake-review rules | `raw/d-technique-census-c2-2026-09-22.md`; `markets/paid-placement.md:92` |
| FY | Fiscal year | expansion only, no source |
| GA | General availability — launch stage; Rufus sponsored prompts "GA 2026-03-25" | `raw/b-amazon-sponsored-prompts-ga-2026-09-22.md` |
| GA4 | Google Analytics 4 (not "GA") | `raw/e-case-sitefire-pointhound-2026-09-22.md` |
| GEO | Generative engine optimisation — organic sub-market alias; never geographic inside `docs/` | `raw/a-vendor-census-c1-2026-09-22.md` |
| GMV | Gross merchandise volume; Shopify "over $100 billion of GMV" | `raw/c-shopify-protocol-agentic-commerce-2026-09-22.md` |
| GSC | Google Search Console — site owner's query and CTR data | `raw/e-case-practitioner-blog-gauravtiwari-ai-overviews-ctr-2026-09-22.md` |
| HR | Human resources; "SaaS HR client" in the Seer case | `raw/e-case-seer-interactive-content-recency-2026-09-22.md` |
| IAB | Interactive Advertising Bureau — trade body; buyer survey n>200 | `raw/e-market-size-iab-paid-2026-09-22.md` |
| ID / IP / IR / PR / KPI | Identifier / internet protocol address / investor relations / public relations / key performance indicator | expansion only, no source |
| LLM | Large language model | expansion only, no source |
| MAU | Monthly active users (see metrics table) | `raw/e-google-alphabet-user-counts-2026-09-23.md` |
| MCP | Model Context Protocol — Anthropic's tool-connector standard | `raw/c-anthropic-mcp-connector-2026-09-22.md` |
| MDL | Multidistrict litigation (US federal) | `raw/a-court-mdl-microsoft-ctr-data-2026-09-22.md` |
| MoM / YoY / QoQ | Month-, year-, quarter-over-prior-period change | expansion only, no source |
| OMR | OMR Reviews — German software review site (signal S4) | `raw/f-signal-sk-S4-omr-reviews-2026-09-22.md` |
| PMax | Google Performance Max campaign type, auto-eligible for AI surfaces | `raw/b-google-platform-summary-2026-09-22.md` |
| ROAS | Return on ad spend; "3x return on ad spend… over 28 days" | `raw/b-openai-1bn-run-rate-milestone-2026-09-22.md` |
| SaaS | Software as a service | expansion only, no source |
| SEO | Search engine optimisation — classical; out of scope except as proxy | expansion only, no source |
| SMB | Small and medium business — buyer size as the source defines it (Segment table above) | expansion only, no source |
| TAC | Traffic acquisition costs; "Search advertising revenue excluding traffic acquisition costs" | `raw/b-sec-microsoft-8k-ex991-2026-07-29-2026-09-23.md` |
| TAP | Visa Trusted Agent Protocol | `raw/c-agentic-commerce-protocols-table-2026-09-22.md` |
| TED | Tenders Electronic Daily — EU public procurement notices (signal S10) | `raw/f-ted-S10-repull2-2026-09-23.md` |
| TW3 / Citead | TW3 Partners, authors of the Citead GEO replication, arXiv 2609.07559 | `raw/e-case-c11-arxiv-tw3-partners-geo-score-2026-09-22.md` |
| UCP | Universal Commerce Protocol — Google-led; Shopify implements, Microsoft Merchant Center "will support" | `raw/c-agentic-commerce-protocols-table-2026-09-22.md`; `raw/c-microsoft-protocol-ucp-adoption-2026-09-22.md` |
| USD / EUR / GBP / JPY / AUD | Currencies; carried unconverted | expansion only, no source |
| UTM | Urchin Tracking Module — URL parameters for referrer attribution (Traffic row above) | expansion only, no source |
| VLOSE | Very Large Online Search Engine — DSA Art. 33 designation; ChatGPT designated 2026-08-31, obligations from January 2027 | `raw/b-techpolicy-chatgpt-dsa-designation-2026-09-23.md`; `raw/b-eu-dsa-ad-repositories-table-2026-09-22.md` |
| WAU | Weekly active users; ChatGPT "weekly active users… >1 billion" | `raw/e-openai-chatgpt-user-counts-2026-09-23.md` |
| WPP | WPP Media — agency group publishing "This Year Next Year" forecasts | `raw/e-market-size-wppmedia-paid-2026-09-22.md` |
| x402 | HTTP-402-based payment protocol; owner changed | `raw/c-agentic-commerce-protocols-table-2026-09-22.md` |
| YC | Y Combinator — accelerator; Sitefire batch W26 | `raw/a-sitefire-funding-2026-09-22.md` |
| 8-K / 10-K / 10-Q / S-1, S-1/A / 6-K / F-3 / 20-F | SEC forms: current report / annual report / quarterly report / registration statement, amendment / foreign private issuer report / foreign issuer shelf registration / foreign annual report | form names, expansion only; filings at `raw/b-sec-*-2026-09-23.md` |
| Art. | Article of a regulation (DSA Art. 39, AI Act Art. 50) | expansion only, no source |
| AMEND-1, P4-r, COMPILE-2; STATE, INDEX | Repo task ids (`method/STATE.md` Landed table); `method/STATE.md`, `competitors/INDEX.md` | repo terms, not acronyms |

**Caveats, this addition.** The two Datos rows record how the raw names each series and how two compiled files relabelled them; the relabels are not corrected here — a compiled file changes only by dated append. Example figures are copies, not new facts; their tiers are the cited raws' (Datos pointer tier 5; engine statements tier 3; Similarweb tier 4; SEC filings tier 2). "Introduced in" names one raw where the term carries a figure, not the first occurrence in the repo. "GA" and "GBP" are ambiguous across raws (general availability vs Google Analytics; pound sterling vs Google Business Profile in `competitors/locafy.md`); a compiled file using either says which. Alias and term lists as of 2026-09-23.
