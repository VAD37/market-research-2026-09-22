# B2B SaaS

| | |
|---|---|
| File date | 2026-09-22 |
| Oldest pull depended on | 2026-09-22 — every cited `docs/raw/` file. Oldest *publication* depended on: 2025-06-03 (HN thread title, `raw/f-signal-bs-S5-hn-algolia-2026-09-22.md`) |
| Cells | 3 sub-markets × 3 buyer sizes = 9 |
| Cells with a spend signal | 3 of 9 — all organic recommendation |
| Signals in the catalogue checked | 12 of 12 in the three organic cells; 9 of 12 in the six paid and agentic cells |

## Segment definition

| | |
|---|---|
| What counts as this vertical, and what is excluded | A company the source itself names B2B SaaS / SaaS / B2B software, as the buyer. AI-visibility vendors and agencies themselves are excluded — supply side, handled in `competitors/` |
| Bands, as the sources define them | No source in this vertical publishes a band. `demand-signals.md` method choice applied throughout: SMB under 100 headcount, mid-market 100–999, enterprise 1000 or more. One vendor tag used verbatim: Profound tags MongoDB "SaaS · Enterprise" — `raw/e-case-census-c13-2026-09-22.md` — and defines no band |

## Cell reads

| Sub-market | Size | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 | Read | Deciding signal (tier, raw) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Organic | SMB | Actindo, 52–70 emp (3) | u | n | n | u | u | n | n | n | n | n | u | **spend** | S1 Actindo posting, tier 3, `raw/f-signal-bs-S1-linkedin-jobs-guest-api-2026-09-22.md` |
| Organic | Mid-market | AutoLeap, 199–225 emp (3) | u | n | n | u | u | n | n | n | n | n | u | **spend** | S1 AutoLeap posting, tier 3, same raw file |
| Organic | Enterprise | Pennylane 1,100+; Mercury 1,001–5,000 (3) | MongoDB "SaaS · Enterprise" (6) | n | n | u | u | n | n | n | n | n | `/llms.txt` on 9 of 10 domains, 90% (1) | **spend** | S1 Pennylane posting, tier 3, same raw file |
| Paid | SMB | n | n | n | n | b | b | n | n | n | n | n | n/a | **none — checked** | no signal observed; 9 of 12 signals checked |
| Paid | Mid-market | n | n | n | n | b | b | n | n | n | n | n | n/a | **none — checked** | as above |
| Paid | Enterprise | n | n | n | n | b | b | n | n | n | n | n | n/a | **none — checked** | as above |
| Agentic commerce | SMB | n | n | n | n | b | b | n | n | n | n | n | n/a | **none — checked** | as above |
| Agentic commerce | Mid-market | n | n | n | n | b | b | n | n | n | n | n | n/a | **none — checked** | as above |
| Agentic commerce | Enterprise | n | n | n | n | b | b | n | n | n | n | n | n/a | **none — checked** | as above |

The three organic reads rest on a tier-3 spend-class signal, **above** the tier-5 floor ("tier 5 or better" = tiers 1–5). The source census read that floor the other way and marked the same four hits attention — `raw/f-signal-census-bs-2026-09-22.md` §"Spend-class vs attention-class tally". Both readings stand, attributed.

## Signals

Marks: `n` = none — checked, nothing found, 2026-09-22. `u` = blank — unattributed: checked, data exists, the source states no buyer size, moves no cell. `b` = blank — unchecked: no paid- or agentic-term query was run; never written as `none`. `n/a` = S12's on-property artifact does not apply to paid or agentic commerce by construction. Spend-class and attention-class signals are never summed.

Channels behind each `n`, by signal, all checked 2026-09-22 — **S1** LinkedIn guest API, 18 queries; indeed.com and upwork.com 403; freelancer.com JS shell (`raw/f-signal-bs-S1-linkedin-jobs-guest-api-`, `-S1-indeed-`, `-S1-upwork-freelancer-`). **S2, S3** `raw/a-vendor-census-c1..c4-`, via `raw/f-signal-bs-S2-S3-vendor-census-citation-`. **S4** g2.com and capterra.com 403; omr.com reached — 56 reviews, 4.81 avg, reviewer industry undisclosed (tier 6) (`-S4-g2-capterra-`, `-S4-omr-`). **S7** `raw/e-case-census-c1-` (B2B SaaS screened 0, cleared 0) plus HubSpot and Yext filings (`-S7-earnings-calls-citation-`). **S8** six conference agendas plus `raw/e-case-census-c3-` (0 of 6 graded talks B2B SaaS) (`-S8-conference-sessions-citation-`). **S9** trends.google.com, data API token-gated (`-S9-google-trends-`). **S10** sam.gov 0 relevant, contractsfinder.service.gov.uk filter non-functional, ted.europa.eu grid not static (`-S10-procurement-`). **S11** DuckDuckGo HTML 0 results plus the B2B SaaS case files (`-S11-price-paid-`). Every `f-signal-bs-*` path carries the `2026-09-22` suffix.

Signals marked `u`, recorded at vertical level, moving no cell — **S2** vendor and agency case-study rosters naming a B2B SaaS client without a size: Quattr/CloudEagle "B2B SaaS (Spend Management)" (5), Foundation/Bitly "Link Management & QR Code Software (B2B SaaS)" (5), Seer's "SaaS" HR client (5), RankPrompt/Humand "B2B SaaS · HR technology" (6), deeploi and Heyflow via Radyant (5), Rankscale "AI SMS Platform" (6) — `raw/e-case-census-c4-`, `-c13-`, `-c9-`, `-c2-2026-09-22.md`. **S5** one HN thread, "From Traditional SEO to AI-Driven Answer Engine Optimization in B2B SaaS", 2 points, 1 comment (4) — `raw/f-signal-bs-S5-hn-algolia-2026-09-22.md`; reddit.com 403. **S6** Flow Agency "SaaS startups", Foundation Inc "AI Visibility Agency for B2B Tech & SaaS" (3 on existence) — `raw/f-signal-bs-S6-flow-agency-2026-09-22.md`, `raw/f-agency-census-c5-2026-09-22.md`: target-customer claims, excluded from every read.

## Cells with no signal — channels checked

| Cell | Signals checked | Channels checked | Date | Result |
|---|---|---|---|---|
| Paid and agentic commerce, all three sizes (6 cells) | 9 of 12 each (S5, S6 unchecked; S12 n/a) | LinkedIn guest API, Indeed, Upwork, vendor censuses c1–c4, G2, Capterra, OMR, EDGAR via c1, six conference agendas, Google Trends, SAM.gov, Contracts Finder, TED, DuckDuckGo | 2026-09-22 | none found |

## Willingness to pay

| Cell | Price actually paid | What it bought | Who disclosed it | Label | Raw |
|---|---|---|---|---|---|
| All nine | `unknown — checked DuckDuckGo HTML and the B2B SaaS Pass-4 case files 2026-09-22` | — | nobody | — | `raw/f-signal-bs-S11-price-paid-2026-09-22.md` |

Pass 3 asking prices — Semrush's +$60/mo AI-toolkit delta (`raw/a-vendor-census-c4-2026-09-22.md`), Pace Generative's $1,499–$2,499 list (`raw/f-agency-census-c5-2026-09-22.md`) — are list prices, never purchases, and are not willingness-to-pay observations.

## Buyer personas, jobs-to-be-done, switching costs, buying process

| Source | Role, quoted | Job, quoted | Cell |
|---|---|---|---|
| Actindo posting | "Digital Marketing Manager - B2B SaaS & AI (m/w/d)" | "Du unterstützt SEO- und GEO-Maßnahmen, um die Sichtbarkeit von Actindo in Suchmaschinen und KI-basierten Systemen zu steigern" | Organic / SMB |
| AutoLeap posting | "SEO Lead" | "Experience with AI SEO, Google Analytics, Google Tag Manager" | Organic / Mid-market |
| Pennylane, Mercury postings | "SEO & AI Content Specialist"; "Organic Search Marketer (SEO/AEO)" | "Build an understanding of the questions and prompts prospects use in AI-powered discovery tools"; "define how Mercury shows up across search engines, answer engines, and AI-native discovery" | Organic / Enterprise |
| Profound / MongoDB case | "Fiona Erickson, Team Lead, Organic Acquisition" | "If an Answer Engine gives the wrong information about how to configure MongoDB, the developer doesn't have a bad experience with the AI, they have a bad experience with us" | Organic / Enterprise (vendor tag) |
| Foundation / Bitly case | "Tara Robertson, Chief Marketing Officer, Bitly" | "the answers came from sources Bitly didn't write and couldn't control" | Organic, size unassigned |

Postings: `raw/f-signal-bs-S1-linkedin-jobs-guest-api-2026-09-22.md` (3). Cases: `raw/e-case-profound-mongodb-2026-09-22.md` (6), `raw/e-case-foundation-inc-bitly-2026-09-22.md` (5). Switching costs and buying process: `unknown — checked every raw file this file cites, 2026-09-22` — no source states a contract length, renewal, incumbent displaced, decision maker, blocker, or cycle length for any B2B SaaS buyer in any sub-market. Bitly's "12 Months" is a delivery window the agency states, not a buying-process disclosure.

## Proof landscape — this vertical

| Cluster | Screened / cleared | Best grade | Detail |
|---|---|---|---|
| P4-c9 vertical sweep | ~100 / 4 | Bronze | G2, HubSpot, Heyflow ×2; 3 Fools gold; 0 Silver, 0 Gold; 6 of 9 pulled confirmed B2B SaaS by the source — `raw/e-case-census-c9-2026-09-22.md`. The one negative-direction case is HubSpot: "verlor HubSpot zwischen 30 und 40 Prozent des Traffics auf betroffenen Keywords", 2026-03-16 (5) — `raw/e-case-c9-hubspot-omr-podcast-2026-09-22.md` |
| P4-c2 agency posts | 12 agencies / 3 | **Silver** | Seer's "SaaS HR" client: test pages +219% then +300% AI traffic, site-wide AI sessions "remained stagnant" as control (5) — `raw/e-case-seer-interactive-content-recency-2026-09-22.md` |
| P4-c4 and P4-c13 vendor cases | 12 graded, ~150 titles re-graded / 4 | Bronze | Quattr/CloudEagle (5), RankPrompt/Humand (6), Rankscale/SoWork, Profound/MongoDB (6); Rankscale "AI SMS Platform" Fools gold, "$280,000 in qualified pipeline" — `raw/e-case-census-c4-`, `-c13-2026-09-22.md` |
| P4-c7 brand side, P4-c11 nulls | 59 brands, ~180 negatives / 0 | — | 0 corroborate, 0 contradict, 59 silent (MongoDB, Plaid, Ramp, Airbyte, Strapi, NinjaOne among them); 0 B2B SaaS null cleared — `raw/e-case-census-c7-`, `-c11-2026-09-22.md`. Zero Gold anywhere in this vertical; the one Silver's client is anonymised to "SaaS HR" |

## Hypotheses touched

| # | Claim | This vertical's input |
|---|---|---|
| H4 | Demand is attention-only in every SMB cell | **Falsifier condition met here**: Organic / SMB reads spend on Actindo's own posting, tier 3. Paid / SMB and Agentic / SMB read `none — checked`. Scoring across all 9 SMB cells is Pass 9's |
| H7 | Organic carries spend in more cells than paid or agentic | Input only: organic 3, paid 0, agentic 0 in this vertical. Needs all 27 cells |
| H9 | Agentic spend sits in enterprise cells, absent from SMB | Input only: no agentic cell here reads spend, enterprise included |

## Unknowns

| Question | Channels checked | Date |
|---|---|---|
| Does G2's or Capterra's AI-visibility category show a B2B SaaS reviewer segment, at what velocity? Does OMR expose reviewer industry or size anywhere a static fetch missed? | g2.com, capterra.com (403), omr.com/en/reviews/product/otterly-ai | 2026-09-22 |
| Do Indeed or Upwork carry GEO/AEO postings by B2B SaaS employers that LinkedIn's non-phrase-strict guest API missed? | indeed.com, upwork.com (403), freelancer.com (JS shell) | 2026-09-22 |
| Do r/SEO, r/PPC or r/bigseo carry B2B SaaS threads on any sub-market? Does search interest for GEO/AEO/AI-visibility terms concentrate in software contexts? | reddit.com search.json (403), trends.google.com (data API token-gated) | 2026-09-22 |
| Does any procurement register carry a B2B-SaaS-adjacent AI-visibility award once queried through a working search path? | sam.gov, contractsfinder.service.gov.uk, ted.europa.eu | 2026-09-22 |
| Does a paid-placement or agentic-commerce community thread or agency page exist for B2B SaaS? Sub-market-specific S5 and S6 queries were never run | hn.algolia.com, DuckDuckGo HTML — organic-alias terms only | 2026-09-22 |

## Caveats

- Every read rests on internet-only proxies. No interviews, no outreach (`scope.md` R2). No signal observes a budget. Willingness to pay is `unknown` in all nine cells, and nothing here is inferred from a list price.
- **All three spend reads rest on a single signal, S1, at tier 3.** `demand-signals.md` calls S1 "headcount budget, not category spend — weakest spend class", lagging spend and over-representing large firms. Three of the four postings' headcounts come from third-party data-vendor snippets (PitchBook, Revelio Labs, ZoomInfo, LeadIQ, RocketReach) read via search snippet, not opened; only Pennylane's "More than 1,100 Pennylaners" is primary. AutoLeap's sources conflict — 199 and 225 against a "51-200" range straddling the SMB / mid-market boundary — recorded, not averaged. LinkedIn's guest API does not enforce exact-phrase matching either — `"generative engine optimization"` returned zero relevant hits across two attempts — so S1 counts here likely undercount real hiring.
- **The six `none — checked` reads are partial.** S5 and S6 were run with organic-alias terms only, so those cells rest on 9 of 12 signals; several of the nine are access-level blocks (G2, Capterra, Reddit, Trends, Indeed, Upwork) that would have blocked any sub-market equally. 9 browser-backlog items stay open — `raw/f-signal-census-bs-2026-09-22.md` §Browser backlog.
- Publication bias runs one way: quiet spending leaves no public trace, so `none` reads are weaker evidence than `spend` reads. S12's 90% is measured-by-us at tier 1, but the sample's Enterprise band comes from public-record reputation and was not re-verified in the pull; it decides nothing, its cell already reading spend on S1.

### Pass 8 re-run, 2026-09-23

Task P8-r. Runs S5 and S6 with paid- and agentic-framed query terms against all six Paid and Agentic cells (previously 9 of 12 signals each, S5/S6 run with organic-alias terms only). Raw: `raw/f-signal-bs-S5-S6-paid-agentic-2026-09-23.md`.

**S5, all six cells:** `none — checked`. HN Algolia API, direct fetch, two queries: `"ChatGPT ads" SaaS` → `{"nbHits":0,"hits":[]}`; `agentic commerce SaaS checkout` → `{"nbHits":0,"hits":[]}`. A published zero, tier 4 per `demand-signals.md`'s "4 if the platform publishes counts". reddit.com stays blocked (unchanged from 2026-09-22).

**S6, Paid:** checked, `blank — unattributed` (vertical-level, moves no cell). Found, existence only: Obility ("B2B marketing agency with strong reputation in paid search and performance marketing for SaaS"); E2M ("sponsored answer placements for SaaS, B2B, and service brands", direct fetch 403, recorded via search synthesis); InterTeam Marketing ("a B2B SaaS and services advertising agency ... suited for B2B SaaS and service companies looking to test ChatGPT Ads"); Directive Consulting (uses the Scrunch platform to measure AI-answer surfacing). No named client, no n, no date on any of the four — tier 3 on existence, tier 6 on framing.

**S6, Agentic:** `none — checked`. No agency page names B2B SaaS or SaaS specifically as a served vertical for agentic-checkout setup. 1Digital Agency's "Agentic Strategy Consulting" is general e-commerce, not SaaS-named; commercetools' "Agentic Commerce in B2B" is a platform vendor's own blog post naming no client and no agency service.

**Cell reads, updated:**

| Cell | Change | New read |
|---|---|---|
| Paid / SMB, Mid-market, Enterprise (×3) | 9 of 12 → **12 of 12 signals checked** | none — checked (unchanged word, now fully closed) |
| Agentic / SMB, Mid-market, Enterprise (×3) | 9 of 12 → **12 of 12** | none — checked (fully closed) |

No cell changes its word-level read. All nine B2B SaaS cells now read on a fully-checked signal set (12 of 12, counting S12's `n/a` by construction) under both the strict and loose readings — this vertical carries no remaining strict/loose gap.

**Caveats, this append:** The four paid-placement agency hits are generic B2B/SaaS marketing agencies applying a ChatGPT-ads line of business to existing clients, not agencies built around AI-answer placement specifically; none discloses a client roster or a buyer-size band, so none moves a cell. E2M's claim is recorded via search-tool synthesis only — its own page refused a direct fetch (HTTP 403) — and is flagged `verbatim: partial` in the raw file.

File now 121 lines against the 100-line budget; overrun is this append.

## Budget line, P16-c1, 2026-09-23

Which existing line funds AI-visibility or AI-ads spend for a B2B SaaS buyer. Raw prefix `raw/`, suffix `-2026-09-23.md` unless stated.

| Evidence | What it states | Line named | Tier | Raw |
|---|---|---|---|---|
| HubSpot, 10-K FY2025 | own marketing via "high search engine and answer engine presence"; acquired XFunnel, "an Answer Engine Optimization ("AEO") platform", "$16.5 million, net of cash acquired", 2025-12-01 | M&A cash, not a marketing line; marketing line unnamed | 2 | `f-signal-bs-S7-hubspot-10k-xfunnel` |
| Semrush, 10-K FY2025 (vendor, filed) | "existing customers supplement their traditional SEO tools with newer GEO and AI search products"; "approximately 108,000 paying customers" | SEO-tool line, supplemented — vendor framing | 2, bias flagged | `b-semrush-10k-2025-geo-demand` |
| Informa TechTarget, 10-K FY2025 | "subdued sales and marketing budgets amongst many of Informa TechTarget's enterprise technology customers as more of their expenditures have been concentrated on R&D activities, particularly around artificial intelligence"; "growing audience referrals from AI search channels" | marketing budgets down, R&D up — direction, no line | 2 | `f-signal-bs-S7-techtarget-10k-2025` |
| EDGAR FTS, "AI search", six B2B SaaS filers, 2026 | 3 hits, all Semrush and TechTarget (sellers); ZoomInfo, Sprout, Zoom, HubSpot 0 | none | 2 | `f-edgar-fts-budget-line-queries` |
| Gartner CMO Spend Survey 2026; HubSpot State of Marketing 2026 | `unknown — paid`; gated, no budget statement public | — | —; 6 | `e-gartner-ad-platforms-prediction-2028`; `f-hubspot-state-of-marketing-2026-check` |

**Read.** `unknown — checked EDGAR FTS (6 CIKs plus phrase queries), HubSpot, Semrush, TechTarget 10-Ks, gartner.com, hubspot.com 2026-09-23; search engines walled` (`f-search-engines-wall-log`). Two filed pointers, neither a budget line: a vendor says GEO tools are bought beside SEO tools (tier 2, seller's framing); a B2B media seller says its customers' marketing budgets are subdued while AI R&D absorbs spend (tier 2). File over its 100-line budget; overrun includes this append.

## Primary re-pulls, REPULL-1, 2026-09-23

- Bitly AI-search sessions case · `raw/e-case-foundation-inc-bitly-2026-09-22.md` (5) · `raw/e-case-foundation-inc-bitly-primary-2026-09-23.md` (5) · "citation share for link shorteners grew to 11.7%, nearly double the next competitor"; "referral sessions growing from 178 to 930 (up 422%) and engaged sessions increasing from 98 to 426 (up 335%)" (12 months; published 2026-08-17) · agrees; sections after the cut add 27.3% QR-code visibility, 8 AI Overview citations, 41 top-3 rankings, 2,010 organic monthly visits
- +54% GPT-User bot hits (Silver-graded case) · `raw/e-case-seer-interactive-content-recency-2026-09-22.md` (5) · `raw/e-case-seer-interactive-content-recency-primary-2026-09-23.md` (5) · text figures "300%", "219%", "54%", "80%", "3.6%" unchanged; the two results charts saved at `raw/img/e-case-seer-interactive-content-recency-primary-2026-09-23/02-seer-content-recency-test.png` and `03-seer-content-recency-travel-client-results.png` (unread until IMG-1) · agrees

## Engine × segment and buying process, P16-c4, 2026-09-23

**Engines named, this vertical's raw.** Mentions and files-with-mention across the 38 B2B SaaS raw files (`f-signal-bs-*`, `f-signal-census-bs-*`, `e-case-census-c9-*`, `e-case-c9-*`, `e-case-airops-*`, `e-case-hubspot-*`, `e-case-fortune-hubspot-*`, `e-case-chime-*`), regex count, method in `raw/f-engine-mentions-raw-count-2026-09-23.md` (measured-by-us on raw already pulled). Partial by design.

| Engine | Mentions | Files | Cell-attributable naming, source, tier |
|---|---|---|---|
| ChatGPT | 104 | 22 | none from an S1 posting — the Actindo, AutoLeap, Pennylane and Mercury postings name GEO/SEO duties, no engine (`raw/f-signal-bs-S1-linkedin-jobs-guest-api-2026-09-22.md`; its only ChatGPT hits are query strings); case evidence names ChatGPT at vendor level (AirOps / Chime, HubSpot cohort — `raw/e-case-airops-chime-case-study-2026-09-23.md`, `raw/e-case-hubspot-aeo-data-cohort-2026-09-23.md`), size unassigned |
| Gemini / AI Mode / AI Overviews | 63 | 16 | case and vendor files; no S1 posting names it |
| Perplexity | 30 | 10 | case and vendor files |
| Claude | 29 | 10 | case and vendor files |
| Copilot | 17 | 5 | case and vendor files |
| Rufus / Alexa for Shopping | 0 | 0 | — |
| Grok | 0 | 0 | — |

Top engine by mention: ChatGPT. The three spend cells (Organic × SMB, Mid, Enterprise) rest on postings that name no engine, so engine × cell is `unknown — checked the four S1 postings 2026-09-23` in every B2B SaaS cell; engine naming here is vendor- and case-level only. Paid: agency pages name ChatGPT Ads for "B2B SaaS and service companies" (S6, `raw/f-signal-bs-S5-S6-paid-agentic-2026-09-23.md`, tier 3 on existence) — sell-side.

**Switching cost and buying process.** Buyer-side: `unknown — checked every raw file cited in this document, OMR review text (0 lines naming a buying step), G2 review text (403 to fetch), HN Algolia, sam.gov, TED 2026-09-23`. Vendor-side terms, tier 3, `raw/a-vendor-terms-contract-length-2026-09-23.md`: self-serve tiers cancel monthly (Peec, Otterly, AthenaHQ, Local Falcon "Cancel anytime", BrightLocal 14-day trial with monthly/annual switch "at any time"); annual terms auto-renew (Otterly, Semrush — Semrush non-cancellable with a one-time 7-day refund only on 12-month-or-longer terms); enterprise tiers are order-form contracts of undisclosed length (Profound "Custom", Scrunch Enterprise, AthenaHQ "negotiated as part of the Enterprise contract", SOCi Order Form, Yext "annual and multi-year subscriptions", tier 2). Who in a SaaS buyer signs: G2 reviewer panels — Profound industry "Computer Software (131)" of 1,129 reviews, roles User 394 / Administrator 135 / Executive Sponsor 57 / Agency 112; Peec company size "Small Business (14) · Mid-Market (6) · Enterprise (1)"; Brandlight "Mid-Market (118)" of 216 (`raw/f-g2-capterra-S4-repull-2026-09-23.md`, tier 5; reviewers, not signatories). Board-level pull, not vertical-cut: Corporate Ink survey via Yext 8-K, 88% of CMOs asked about AI visibility, 34% with a strategy, tier 5 relay, no n (`raw/f-edgar-fts-local-multilocation-S7-2026-09-23.md`).

**Caveats, this append.** Counts are word matches over raw files, headers and query strings included; they weight vendor case files, numerous in this vertical, over buyer statements. No posting text in this vertical names an engine, so the engine × cell read is empty where the spend reads are strongest. Vendor terms are list terms; no B2B SaaS buyer's contract length is on record. File over its 100-line budget; overrun includes this append.

## S13 brand accuracy and EU cells, P16-c3, 2026-09-23

S13 per `method/demand-signals.md` addition 2026-09-23. Raw prefix `raw/`, suffix `-2026-09-23.md`.

| Sub-market | Size | S13 | Deciding observation |
|---|---|---|---|
| Organic | SMB, Mid-market, Enterprise | none — checked | size-unassigned observation below moves no cell |
| Paid | all three | none — checked | no observation |
| Agentic commerce | all three | none — checked | no observation |

Unassigned, organic, this vertical: Make (make.com), "Senior GEO Manager - LLM Search Optimization", Madrid, posted 2026-09-03, 151 applicants: "cited (correctly, favorably, and often) across ChatGPT, Perplexity, Google AI Overviews, and Claude"; "Authority & source repair" — spend class, tier 3; headcount `unknown — checked make.com 2026-09-23` → `unassigned` (`f-linkedin-S1-eu-countries`). r/marketing 2026-04-06 "I asked AI 3 questions about my company" — company and size unnamed, attention, tier 5 (`f-reddit-arcticshift-S13-brand-accuracy`).

EU cells — organic sub-market only; paid and agentic not checked with EU terms, blank:

| Country | Size | S1 | Read | Raw, tier |
|---|---|---|---|---|
| FR | Enterprise | Pennylane "SEO & AI Content Specialist", 2026-09-18, 75 applicants, "Generative Engine Optimization (GEO) are central", "ChatGPT and Perplexity"; headcount 1,100+ per cell reads above | **spend** | `f-linkedin-S1-eu-countries`, 3 |
| FR | SMB, Mid-market | no SaaS employer at these bands of 30 cards | none — checked | same |
| ES | unassigned | Make (above) — vertical from employer's product, size unknown | moves no cell | same |
| ES | SMB, Mid-market, Enterprise | none besides Make; Semrush posting is sell-side | none — checked | same |
| UK | Mid-market | Proton "Senior Technical SEO Manager", "700+ team members" — description names no AI-search term; not a category hit | nil | same |
| UK | SMB, Enterprise | 0 SaaS category hits of 30 cards; Compare the Market recorded under high-CPA | none — checked | same |
| IT | all three | 0 SaaS employers of 30 cards (agency and education hits only) | none — checked | same |
| NL | all three | 0 SaaS employers of 30 cards (agencies only) | none — checked | same |

S2 local-language listings: Yext /fr/scout and /it/scout exist, no customer named; no /es, /nl (`f-vendor-S2-yext-scout-localized-fr-it`, 3). S5: 0 threads on r/smallbusinessuk, r/france, r/spain, r/thenetherlands; 1 r/italy post, off-topic (`f-reddit-arcticshift-S5-eu-national-subs`, 5). S10: TED GEO notices 14 of 14 DEU, 1 IRL; FR/ES/IT/NL/UK 0; UK CF 0 on four phrases (`f-ted-ukcf-S10-eu-country-brand-accuracy`, 2).

**Caveats, this append.** Pennylane's FR read repeats the Worldwide enterprise read of 2026-09-22 with a new per-country pull, not a second employer. Make's vertical is read from its product (automation SaaS), not stated in the posting. LinkedIn pages are first-page relevance sets, not counts. File over its 100-line budget; overrun includes this append.
- Agency ChatGPT-ads service claim (E2M, S6 B2B SaaS paid) · `raw/f-signal-bs-S5-S6-paid-agentic-2026-09-23.md` (3 on existence — search synthesis, `verbatim: partial`) · `raw/f-e2m-white-label-chatgpt-ads-services-primary-2026-09-23.md` (3) · "We build ChatGPT Ads as part of a broader white label PPC service, so it complements, rather than competes with, your clients' existing Google, Meta, and LinkedIn Ads campaigns"; "Sponsored Answers for SaaS/B2B, Shopping Carousels for Retail/DTC"; plans "Up to $5K budget $499/mo · Up to $10K budget $999/mo · Up to $20K budget $1,999/mo · Above $20K Custom"; "one-time setup fee starts at $499 per website" · agrees in substance (synthesis wording is not the page's); primary adds list prices — an asking price, not a price paid

## S1 posting bodies, P16-c4b, 2026-09-23

Indeed walled on the first posting page (Cloudflare "Additional Verification Required", 16:21); bodies read from employer career sites instead. Raw: `raw/f-indeed-S1-repull3-2026-09-23.md` (tier 3, company-stated). Format: employer · title · phrase in body · engines named · budget or tool named · salary · size band · raw section.

- AT&T (AT&T Business) · "Lead, Digital Customer Growth" — body: "As an SEO & AEO/GEO Manager supporting AT&T Business" · yes — "Answer Engine Optimization (AEO), Generative Engine Optimization (GEO)"; "generative search, answer engines, AI assistants, and citation-based discovery" · none by brand · tools listed as familiarity: "Google Search Console, Bing Webmaster Tools, Adobe Analytics, Ahrefs, SEMrush, BrightEdge, Botify, Screaming Frog"; no budget figure · "$128,400.00 - $215,800.00 USD Annual" · `unassigned` (no headcount in body); telecom, B2B buyer audience — not B2B SaaS, moves no cell · §posting #2
- Vasion · "Head of Search & AI Visibility" · unread — Indeed wall; Workable board lists 5 roles, this title absent as of 2026-09-23 · — · — · card: no salary · `unassigned` · §Checked, not found
- Intuit · "Staff AI Scientist" · unread — Indeed wall; jobs.intuit.com results script-rendered · — · — · card "$209,500 - $283,500 a year" · `unassigned` · §Checked, not found
- CWILL INC · "Bilingual Mandarin Product Manager (SEO SaaS Product)" · unread — Indeed wall; not attempted · — · — · card "$100,000 - $160,000 a year" · `unassigned` · superseded file

Cell check. No B2B SaaS S1 cell rests on an Indeed card; nothing confirmed or weakened here. The eight B2B-term Indeed queries (SaaS, "B2B software" × 4 phrases) remain unrun — wall.

## Image reads, IMG-1a, 2026-09-23

| Figure / text as shown | Chart or image | Date | Tier | Img raw |
|---|---|---|---|---|
| GPT-User bot hits/day, read off axis: ~80–100 at red marker (~6/17/2025), ~150 at teal marker (~7/9/2025), ~215–245 after ~8/6, ~275 at ~8/28 | "Content Recency Page GPT-User Bot Hits" (Seer, travel client) | 2025-06 to 2025-08 | 5 | `raw/e-case-seer-interactive-content-recency-primary-2026-09-23-img-2026-09-23.md` |
| Text says "red line … blue line"; chart draws red and teal vertical markers; the only blue element is the data series | same | same | 5 | same |
| Test-page sessions/week (left axis 0–12) ~2–12; overall AI sessions (right axis) ~540–840 throughout; two black boxes ~3/8–4/22 and ~6/8–end | "Content Recency Sessions and Organic Sessions" (SaaS HR client) | 2025-01 to 2025-06 | 5 | same |
| Header image is an unrelated 8-bar chart (flight comparison 100% … discounts 74%), no title | header image, no alt | page 2026-01-19 | 5 | same |
| CloudEagle AI Citation Share, read off axis: ~0.075 at deployment (11-02-2025) → ~0.325 at 12-21-2025; weekly clicks ~420 → ~670 (01-11-2026) | "3X Increase in AI Citation Share Within 12 Weeks"; "113% Increase in Clicks…" (Quattr) | 2025-10 to 2026-01 | 5 | `raw/e-case-quattr-cloudeagle-ai-citation-share-primary-2026-09-23-img-2026-09-23.md` |

Caveat: the Seer "54%" and "300%" are not printed on the charts; ~ values are measured-by-us axis readings from vendor screenshots.

## EU paid and agentic cells, P16-c3b, 2026-09-23

Closes the paid and agentic EU cells P16-c3 left blank. Raw prefix `raw/`, suffix `-2026-09-23.md`. Channels as in the skincare append of the same date.

| Country | Sub-market | Size | S1 | S2 | S5 | S10 | Read |
|---|---|---|---|---|---|---|---|
| UK | Paid | all three | 0 SaaS employers of 6 pages; Google posting is sell-side | Jotform, Lovable in Adthena top ten — see unassigned row | 0 threads, 4 queries | TED 0, UK CF 0 | none — checked |
| UK | Agentic | all three | 0 SaaS employers | Shopify /uk names no merchant | query 422 ×2 | UK CF "agentic" 8, all public-sector AI builds | none — checked (S5 failed) |
| FR | Paid | all three | 0 SaaS employers; Hellowork "ChatGPT ads" 3, none SaaS | OpenAI posts name no advertiser | 0 threads | TED 0 | none — checked |
| FR | Agentic | all three | Hellowork "agentic commerce" 2: Alan (insurance), Square (consultancy) | none | 0 threads | TED "commerce agentique" 2, both 2017–2019 training | none — checked |
| ES | Paid | all three | team.blue posting is agentic automation, not ads | none | both queries 422 ×2 | TED 0 | none — checked (S5 failed) |
| ES | Agentic | all three | Accenture Song ×2 (Tecnoempleo, LinkedIn) — sell-side | Shopify /es names no merchant | 0 threads | TED 0 | none — checked |
| IT | Paid | all three | team.blue, Avanade, Deloitte — engineering roles | none | 0 threads | TED 0 | none — checked |
| IT | Agentic | all three | 0 of 8 pages | Shopify /it names no merchant | 0 threads | TED 0 | none — checked |
| NL | Paid | all three | Seedtag PM (ad tech, sell-side); eBay ML | OpenAI nl-NL names no advertiser | 0 threads, 2 queries | TED 0 | none — checked |
| NL | Agentic | all three | Picnic, Zonneplan — own assistants, outside vertical | Adyen (NL vendor) names no SaaS customer | query 422 ×2 | TED 0 | none — checked (S5 failed) |

Unassigned, UK × Paid, this vertical: Jotform "reaches 4.17% across four market groupings" (US, UK, AU, rest of world) and Lovable 3.66% (markets unstated) in Adthena's ChatGPT Ads index, week of 2026-07-13 to 07-20 — form software and software, per the source; spend class, tier 5; Jotform headcount `unknown — checked jotform.com/about 2026-09-23` → `unassigned`, moves no cell (`b-ppcland-adthena-7378-advertisers`, relay; `f-adthena-S2-eu-paid-agentic`, page and images).

Raw: `f-linkedin-S1-eu-paid-agentic` (3), `f-jobboards-S1-eu-paid-agentic` (3), `f-vendor-S2-eu-paid-agentic` (3), `f-adthena-S2-eu-paid-agentic` (5), `f-reddit-arcticshift-S5-eu-paid-agentic` (5), `f-ted-ukcf-S10-eu-paid-agentic` (2).

**Caveats, this append.** Jotform's UK presence is one line in a trade relay of a vendor index, tier 5 at best; the index images are unread (IMG-1). "(S5 failed)" cells rest on S1, S2, S10 only. Sell-side postings (Accenture, Seedtag, Google) are recorded and move no cell. File over its 100-line budget; overrun includes this append.

## Image reads, IMG-1c, 2026-09-23

No advertiser stated as SaaS or software in Adthena's UK leaderboard images (ChatGPT Ad Index, week of 2026-07-13 to 07-20; tier 5, vendor index, vendor-reported). Full UK-tagged list as printed — all-markets table: Booking.com 13.81%, Almedia USA, Inc. 12.76%, efaq.com 4.55%, Expert Market 4.38%, giffgaff 4.28% (UK only); UK card: giffgaff 14.0%, Vodafone 11.3%, Booking.com 9.0%. The images print no vertical for any advertiser. Side by side with the P16-c3b unassigned row above: Jotform 4.17% and Lovable 3.66% are not visible in any image — the all-markets table is cut after rank 5 — so both rest on the trade relay (`b-ppcland-adthena-7378-advertisers`, 5) alone, not on "page and images". UK × Paid cells unchanged: none — checked; Jotform / Lovable stay `unassigned`. Class per `method/demand-signals.md` S2 rules for any advertiser named by a vendor index: attention (vendor-reported, not a budget). Raw: `raw/f-adthena-S2-eu-paid-agentic-2026-09-23-img-2026-09-23.md`.
