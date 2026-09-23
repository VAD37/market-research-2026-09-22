# Unknowns, hypotheses scored, and the programme-done arithmetic

| | |
|---|---|
| File date | 2026-09-22 |
| Oldest pull depended on | 2026-09-22 — every `raw/` file cited, the three day-0 panel files included |
| Lane | all six |
| Hypotheses touched | all 23 — H1–H16, HE1–HE3, HP1–HP4 |
| Claims at tier 3 or better | 4 of 5 |

## Question

> What remains unknown, on which channel checked and when — and how does every pre-registered hypothesis score against what was pulled?

## Answer

Fifteen of 23 hypotheses are scorable: **4 confirmed, 3 killed, 8 unresolved — checked**. Eight take `not produced` — six panel rows held by user decision 2026-09-22, plus H10 and H11, whose producing pass 11 has not run. Two of six programme-done rows hold.

## Evidence

### Hypotheses register — every row marked, with the deciding evidence and its tier

| ID | Mark | Deciding evidence | Path | Tier |
|---|---|---|---|---|
| H1 — AI referral converts above organic search | unresolved — checked Adobe, Salesforce, Shopify 2026-09-22 | Adobe at the tier-4 floor compares AI to **non-AI** visits ("Conversion Now 42% Higher"), not to organic search; the organic-search comparator exists only at tier 5 (Shopify, "nearly 50% higher rates than organic search"); no publisher breaks out per engine | `markets/agentic-commerce.md` → `raw/c-retail-analytics-table-2026-09-22.md` | 4 |
| H2 — paid inventory exists at scale | **confirmed** | Self-serve Ads Manager beta live on a P1 engine from 2026-02-09, plus Google AI Overviews/AI Mode auto-eligible | `markets/paid-placement.md` → `raw/b-openai-platform-summary-2026-09-22.md` | 3 |
| H3 — at least one vendor demonstrates causal lift | **killed** | Zero Gold after the Pass 4 screen: ~980 candidates, 0 holdout / geo-split / switchback | `findings/proof-scorecard.md` → `raw/e-case-census-c13-2026-09-22.md` | 5 |
| H4 — demand is attention-only in every SMB cell | **killed** | B2B SaaS organic × SMB reads spend on a tier-3 employer posting; source census read the floor the other way, both stand | `findings/demand-map.md` → `raw/f-signal-bs-S1-linkedin-jobs-guest-api-2026-09-22.md` | 3 |
| H5 — corpus seeding measurably moves an answer | unresolved — checked arXiv, HN Algolia, vendor and engine pages 2026-09-22 | kill unmet: FeatGEO Table 4 is a published pre/post, tier 3 (`raw/d-citationpref-featgeo-2026-09-22.md`); confirm unmet: "0 in this cluster's 12 pulls" have a true before-and-after design; no Pass 5 technique has a published single-action before-and-after on a production surface | `raw/d-technique-census-c1-`…`-c7-2026-09-22.md` | 4 |
| H6 — a brand action precedes a measured visibility change on a P1 engine | unresolved — checked vendor case pages 2026-09-22 | Visibility Score models unnamed, item 6 absent (Bronze under rule 1); Sitefire/Pointhound: content live 2026-03-14 inside an absolute window 2026-02-23 to 2026-06-29, ChatGPT and Claude named, Visibility Score 0 → 1.0%, untouched-page control | `findings/proof-scorecard.md` → `raw/e-case-sitefire-pointhound-2026-09-22.md` | 5 |
| H7 — organic carries spend in more cells than paid or agentic | unresolved — checked (channel list in `demand-map.md`) 2026-09-22 | Organic 5 spend cells against 1 each; both conditions require all 27 cells checked and 8 read blank | `findings/demand-map.md` | 3 |
| H8 — a protocol is published fully enough to implement without a contract | **confirmed** | ACP, UCP and x402 all Apache-2.0 with no gate to read the spec | `markets/agentic-commerce.md` → `raw/c-agentic-commerce-protocols-table-2026-09-22.md` | 3 |
| H9 — agentic spend in enterprise, absent from SMB | unresolved — checked (same list) 2026-09-22 | One agentic enterprise cell spends, no agentic SMB cell does, 2 of the 6 read blank | `findings/demand-map.md` | 3 |
| H10 — org / content-ops changes named more often than paid-media changes | **not produced** | Producing pass 11 has not run; its gate reads "9, and 10 or its recorded hold". Pass 4 case material is the pointer, not the score | `method/plan.md` §Pass 10 and 11 hold note | — |
| H11 — tier-3 transition evidence in each vertical | **not produced** | Producing pass 11 has not run; tier-3 postings exist in all three verticals (e.l.f., Actindo, Cigna). Pass 4 read: Sitefire/Jerry tier 5, Conductor/Zurich UK tier 6, NerdWallet tier 2 but names no brand action. Channels recorded in that file | `customers/high-cpa-regulated.md` → `raw/e-case-census-c10-2026-09-22.md` | 2 |
| H12 — where paid inventory exists its price is disclosed publicly | unresolved — checked openai.com, support.google.com/google-ads, about.ads.microsoft.com, advertising.amazon.com 2026-09-22 | Confirm needs a rate card or pricing page: 0 of 8. Kill needs no price at all at tier 3: OpenAI states "$3–$5 USD per click" recommended max bid. Neither condition is met | `markets/paid-placement.md` | 3 |
| H13 — a P1 engine publishes a countermeasure naming a Pass-5 technique | **confirmed** | 6 of 36 engine × technique cells read `named` — Anthropic on fake reviews, Google disclaiming llms.txt, four engines on prompt injection | `raw/d-technique-census-c7-2026-09-22.md` | 3 |
| H14 — manipulation evidence denser in regulated than in the anchor | **killed** | Regulated 0 filed specimens and 0 tested specimens; anchor 0 at the tier-4 floor (one skincare item, tier 5, `raw/d-seeding-incumbent-advantage-2026-09-22.md`) — the anchor equals it, which is the kill condition | `customers/high-cpa-regulated.md` → `raw/d-technique-census-c2-`, `-c3-2026-09-22.md` | 4 |
| H15 — vendors publishing a composite disclose its prompt set | unresolved — checked vendor method pages c1–c4 2026-09-22 | kill unmet: 5 of 8 in c1 publish no composite; confirm unmet: 0 of 34 rostered vendors disclose a fixed published prompt set with n | `markets/organic-recommendation.md` → `raw/a-vendor-census-c1-`…`-c4-2026-09-22.md` | 3 |
| H16 — every published sub-market size is a forecast | unresolved — checked research-house pages 2026-09-22 | forecasts are tier 6, below floor; rows 4–5 label base years "reached"/"valued at"; 15 of 18 figures author-labelled forecasts; the 3 measured ones carry no forward target year and none is a sub-market size | `findings/whitespace.md` → `raw/e-market-size-table-2026-09-22.md` | 3 |
| HE1 — ChatGPT paid product live and documented on its own surface | **confirmed** | Ads doc, formats, label wording and bid guidance on OpenAI's own pages | `markets/paid-placement.md` → `raw/b-openai-platform-summary-2026-09-22.md` | 3 |
| HE2 — Claude returns brand-level recommendations to buying-shaped prompts | **not produced** | Day 0: 83 of 160 runs, logged-in, Memory localising every answer to Vietnam; `region_intended: US` failed for every run. Sampling held 2026-09-22 22:40 | `raw/e-claude-panel-2026-09-22.md` | 1 (unusable for this row) |
| HE3 — ad-labelled formats render inside Google AI surfaces for the prompt set | **not produced** | Day 0 retry: 76 of a possible 176 AI Mode runs, 0 ad units; AI Overviews 0 of 14 rendered; logged-out, IP-localised to Vietnam, text-extraction-scoped. Panel held | `raw/e-google-aimode-panel-2026-09-22-retry.md` | 1 (one date, not the protocol's n) |
| HP1 — between-engine gap exceeds within-engine spread | **not produced** | Needs two P1 engines on one date and surface; ChatGPT 0 runs, Gemini 24 of 160 on Flash-Lite with a silent throttle | `raw/e-gemini-panel-2026-09-22.md`, `raw/e-chatgpt-panel-2026-09-22.md` | 1 |
| HP2 — recommended brand set unstable between dates | **not produced** | Needs two sampling dates ≥14 days apart; only day 0 exists and the gap is recorded, never back-filled | `method/STATE.md` §Pass 10 sampling log | — |
| HP3 — citation-to-mention ratio below 0.50 | **not produced** | Codable only from a neutral day 0; the one usable engine-day is `personalised — logged-in, Memory on` | `raw/e-claude-panel-2026-09-22.md` | 1 |
| HP4 — citation rate higher with web search on than off | **not produced** | Needs a toggle both engines expose; Gemini logged-out exposes none | `raw/e-gemini-panel-2026-09-22.md` | 1 |

Marks: **confirmed 4** (H2, H8, H13, HE1) · **killed 3** (H3, H4, H14) · **unresolved — checked 8** (H1, H5, H6, H7, H9, H12, H15, H16) · **not produced 8** (H10, H11, HE2, HE3, HP1–HP4).

### Programme done — every row, with the arithmetic where there is one

| Condition | Bar | Status | Owned by |
|---|---|---|---|
| Load-bearing claims in `findings/` at tier 3 or better | 80 percent or more | **not met — 17 of 25 = 68.0% (Pass 9); 12 of 27 = 44.4% (`review-1-2026-09-23.md`) — both stand.** By file: `proof-scorecard.md` 1 of 6, `demand-map.md` 6 of 6, `whitespace.md` 6 of 8, this file 4 of 5. Across all 27 claims including the 2 non-load-bearing: 18 of 27 = 66.7% | this file |
| Priority-1 engine × sub-market cells | every cell a number or an explicit `unknown — checked` | **met — 9 of 9** | `whitespace.md` |
| Segment matrix | every cell spend, attention or none, with signals | **not met — 19 of 27**; 8 high-CPA cells read `blank` | `demand-map.md` |
| Success stories | one Silver per vertical, or documented absence with screened count | **met** — B2B SaaS and high-CPA on the Silver arm, skincare on the documented-absence arm (0 Silver at ~133 screened) | `proof-scorecard.md` |
| Hypotheses | every H confirmed, killed or unresolved with the channel checked | **not met — 15 of 23**; 8 take `not produced`, which the scoring rule defines as distinct from unresolved | this file |
| Pass 10 | three pre-registered predictions checked against the panel | **not met — 0 of 3.** Six rows are panel-checkable against a bar of three; sampling held by user decision 2026-09-22 22:40, day 0 recorded per engine as sampled, partial or blocked | this file |

The tier-3 shortfall is concentrated: every load-bearing claim below tier 3 is a Lane E case claim, and published case studies are structurally vendor-reported at tier 5 (`method/trust-rubric.md`).

## Claims

| # | Claim | Evidence | Tier of weakest row | Grade | Load-bearing |
|---|---|---|---|---|---|
| C1 | 23 hypotheses score 4 confirmed, 3 killed, 8 unresolved — checked, 8 not produced | register above | 5 | n/a | yes |
| C2 | Eight rows cannot be scored at all: six because Pass 10 sampling is held, two (H10, H11) because Pass 11 has not run | HE2, HE3, HP1–HP4, H10, H11 | 1 | n/a | yes |
| C3 | Channels listed below are blocked this session rather than exhausted, and carry most of the open unknowns | blocked-channel table below | 1 | n/a | yes |
| C4 | Two of six programme-done rows hold | done table above | n/a — findings files only, no raw/ | n/a | yes |
| C5 | 17 of 25 load-bearing claims across the four findings files sit at tier 3 or better — 68.0% against a bar of 80% | done table above | n/a — findings files only, no raw/ | n/a | yes |

## Survivorship

Not case-based — the screened and cleared counts behind H3, H6, H11 and H14 are stated once in `proof-scorecard.md`.

## Unknowns

Merged from `method/STATE.md` §Unknowns, every compiled file's unknowns table, and the census unknowns. Every row was checked 2026-09-22.

| Lane | Question | Channels checked | Blocked or exhausted |
|---|---|---|---|
| A | Native AI-visibility tooling from OpenAI or Anthropic; the roster ceiling beyond G2 pages 1–2 of 43 and 36; AthenaHQ funding; Peec AI price; Scrunch/Sitecore deal value from a primary; any vendor's AI-visibility product revenue broken out | help.openai.com, anthropic.com, docs.claude.com, platform.claude.com, g2.com, crunchbase.com (403), pitchbook.com (403), sitecore.com, bloomberg.com (403), every c1–c4 census row | exhausted on the engines', vendors' and acquirers' own pages; **blocked** at g2.com and the two funding aggregators |
| A, E | sec.gov, data.sec.gov, efts.sec.gov 403 all session; re-probe returned HTTP 503 Akamai maintenance; EDGAR full-text on "AI visibility" HTTP 500 | fetch, Playwright, curl with contact UA | **blocked** — filings entered only as IR-site copies (tier 3) or aggregator relays (tier 5) |
| B | Any engine rate card and a precise advertiser count; take rate at any reseller; Gemini app ad format; AI Mode pricing model; Copilot and Amazon on-surface label wording | openai.com, support.google.com/google-ads, blog.google, about.ads.microsoft.com, advertising.amazon.com, criteo.com, stackadapt.com, pacvue.com (404), kargo.com | exhausted on each owner's own pages — the pages exist and name no price |
| B | Any ad repository entry distinguishing an ad inside a conversational AI answer; Amazon Ad Library fields; a codified UK AI-ad disclosure rule | DSA repositories of Google, Microsoft, Meta, X, Amazon; ASA/CAP | exhausted — ChatGPT's own Art. 39 repository is not yet due |
| C | Instant Checkout fee; fee clauses for ACP, AP2, UCP, x402, Visa TAP; Mastercard Agent Pay schema; merchant counts; whether Anthropic or Rufus runs a merchant program; Perplexity merchant terms; Shopify's UCP trust tiers | developers.openai.com, docs.stripe.com, each protocol repo and owner page, support.google.com/merchants, anthropic.com, advertising.amazon.com, perplexity.ai/hub (404 on terms), shopify.dev (404) | exhausted on public pages; Mastercard and Shopify gate behind registration |
| D | Whether any named brand has run and published a corpus-seeding campaign with a before-and-after; arXiv 2609.06811; whether Microsoft or Amazon names any of the six techniques in its own policy | 70 candidates screened across the Lane D censuses; arxiv.org (scratch file lost mid-pull); bing.com/webmasters (JS shell), learn.microsoft.com (404), amazon.com review-guidelines (503) | exhausted at 70 screened; one paper a **technical failure**, re-pullable; the two policy surfaces **blocked** — browser backlog |
| E | Per-engine referral or conversion breakout from any free retail-analytics publisher; a dollar share of SEO budget reallocated to GEO/AEO; any Gartner, Forrester, IDC, EMARKETER or Statista size | Adobe Digital Insights, Salesforce, Shopify; IAB relay; emarketer.com (subscription-gated); DuckDuckGo html endpoint | exhausted on free publishers; **blocked** behind two subscriptions |
| E | Whether the ~107 unchecked named brands corroborate anything; whether the 25 unopened and 2 unreachable Pass 3 titles hold a Silver; paid-by-outcome on any case; whether any negative or null case exists inside the three tracked verticals | brand newsrooms and IR pages (59 of ~166 checked), airops.com, otterly.ai, feedonomics.com, criteo.com, pacvue.com, kargo.com, searchengineland.com (gated stub), reddit.com (403 ×5 methods), html.duckduckgo.com (rate-limited), g2.com (DataDome CAPTCHA), hn.algolia.com | **cap, not exhaustion**, on the brand and title rows; **blocked** on the three richest negative channels |
| F | SMB and mid-market postings; review velocity and reviewer industry; thread volume; absolute search interest; procurement awards; willingness to pay; switching costs and buying process | indeed.com (403), upwork.com (Cloudflare), freelancer.com (JS shell), g2.com (403), capterra.com (403), omr.com (reached), reddit.com (403), trends.google.com (relative index only), sam.gov, contractsfinder, ted.europa.eu (405), EDGAR ×35 sweeps | **blocked** on six; exhausted on OMR, EDGAR and the three procurement registers, whose search paths returned untrusted results rather than zero |
| F, all | Consumer surfaces for measured-by-us sampling: chatgpt.com (extension "Permission denied for this action on this domain", 403 to fetch), perplexity.ai (Cloudflare, two Ray IDs), google.com/search (reCAPTCHA on the Playwright IP) | Chrome extension ×3, Playwright MCP ×2 each, fetch | **blocked**, and then held by user decision — not exhausted |

## Caveats

- C1 is load-bearing and sits at tier 5: its weakest deciding rows are H3's and H6's vendor-reported case corpus; review-1 reads H6 unresolved (item 6 absent). C2, C3 and C5 rest on measured-by-us records of this session's own pulls and files (tier 1); C4 on the four findings files.
- Every `killed` mark resting on absence — H3, H14 — is only as strong as the channels listed beside it (`method/hypotheses.md` caveats); an absence with no channel list is not a kill, and each of the two carries one. H5 and H15 carry both marks side by side: killed in the 2026-09-22 read, unresolved — checked per review-1. H4's kill and H7's and H9's `unresolved` all inherit `demand-signals.md`'s biases, and H4 turns on a tier-floor reading the source censuses applied the other way. Both readings are in `demand-map.md`, side by side.
- `not produced` is not `unresolved`: eight rows are unscored because their producing pass did not run, and no channel exhaustion is claimed for any of them. H14's "equal screen effort" is not measurable to a fine grain; both verticals returned zero specimens, so the comparison is stated rather than assumed. The tier-3 share of 68.0% is computed over the 25 load-bearing claims in the four files written 2026-09-22; review-1 recounts 12 of 27 = 44.4% over its own enumeration; both stand; adding or retiring a claim moves it. The oldest pull cited is 2026-09-22; no cited pull is stale under `method/plan.md`. This file carries evidence, not a verdict.
- Amended 2026-09-23 per `findings/review-1-2026-09-23.md` §9; both readings stand where the review and the original disagree.

### Pass 8 re-run, 2026-09-23

Task P8-r closed the eight high-CPA segment-matrix blanks (S2, S3, S9, S10) and the eleven partial-`none` cells in skincare and B2B SaaS (S4/S6/S12 paid+agentic; S5/S6 paid- and agentic-framed). Full detail: `findings/demand-map.md` §"Pass 8 re-run, 2026-09-23"; per-vertical detail in the three `customers/*.md` files, same date.

| ID | 2026-09-22 mark | 2026-09-23 mark, beside it | Deciding change |
|---|---|---|---|
| H4 | **killed** | **killed — unchanged, reinforced** | Six newly-banded high-CPA employers (GEICO, Amica, Embrace Pet Insurance, Insurify, The Juice Plus+ Company, Simply Business) band three Mid-market, three Enterprise — zero SMB. The kill still rests on B2B SaaS Organic/SMB alone (`raw/f-signal-bs-S1-linkedin-jobs-guest-api-2026-09-22.md`); today's pull found no new SMB spend cell and no counter-evidence |
| H7 | unresolved — checked (channel list in `demand-map.md`) 2026-09-22 | **confirmed (loose reading) / unresolved — checked (strict reading), both stand** | Organic now carries spend in 6 of 27 cells (was 5) against 1 each for paid and agentic; loose reading has all 27 cells checked, so the confirm condition ("all 27 checked") is met for the first time. Strict reading still has 8 cells blank |
| H9 | unresolved — checked (same list) 2026-09-22 | **confirmed (loose reading) / unresolved — checked (strict reading), both stand** | The 6 agentic SMB+enterprise cells: agentic spend sits at exactly one, skincare Enterprise; no agentic SMB cell reads spend under either reading. Loose reading has all 6 checked, meeting the confirm condition. Strict reading leaves high-CPA's two agentic cells blank |

Marks, updated: **confirmed 4** (H2, H8, H13, HE1) plus **2 dual-mark** (H7, H9, confirmed under loose only) · **killed 3** (H3, H4, H14) · **unresolved — checked 8** (H1, H5, H6, H7, H9, H12, H15, H16 — H7 and H9 carry both marks) · **not produced 8** (unchanged).

**Programme-done, Segment matrix row, restated:** was "not met — 19 of 27; 8 high-CPA cells read blank". Now: **loose — met, 27 of 27. Strict — not met, 19 of 27; 8 cells blank** (down from 19 blank before this pass). See `demand-map.md` for the full arithmetic and the channel each remaining blank rests on.

**Caveats, this append:** H7's and H9's loose-reading `confirmed` marks depend on treating a channel retried today and logged in `blocked-channels.md` (TED) as "checked" for the none-rule's purpose — a convention this repo's `customers/skincare-beauty.md` and `customers/b2b-saas.md` already applied before this pass, extended here to `customers/high-cpa-regulated.md` for consistency. A reader who requires literal 100% signal completion should read both hypotheses as unchanged from 2026-09-22: `unresolved — checked`. Neither mark is deleted; both sit side by side, per root `CLAUDE.md`'s rule against overwriting a prior reading.

### Pass 4 re-run, 2026-09-23

Task P4-r. Full detail: `findings/proof-scorecard.md` §"Pass 4 re-run, 2026-09-23"; census `raw/e-case-census-r1-2026-09-23.md`.

| ID | 2026-09-22 mark | 2026-09-23 mark, beside it | Deciding change | Tier |
|---|---|---|---|---|
| H3 | **killed** | **killed — unchanged** | 0 Gold in ~1,640 more items; best new design two arms, one unit each | 5 |
| H6 | unresolved — checked | **confirmed (rule1, narrow) / unresolved — checked (three verticals), both stand** | OtterlyAI Reddit test: own communities, dated action, six engines, Silver rule1 | 5 |
| H11 | **not produced** | **confirmed — action named; outcome unknown in two of three** | Coty 10-K; LendingTree 8-K; HubSpot op-ed; Chime careers page | 2–3 |

Marks, updated: H6 moves from `unresolved — checked 8` to a dual mark; H11 moves from `not produced 8` to confirmed.

**Caveats, this append:** H6's confirm rests on a vendor testing a tactic on communities it created, not on a named brand in a tracked vertical; the grade_raw Silvers X5 and X6 (anonymised sites) sit beside it. H11's high-CPA row relies on LendingTree's ChatGPT app (tier 2) or Chime (tier 3, borderline vertical). This file was over its line budget before this append; overrun stated here.

## Tier-3 recount, P9-r, 2026-09-23

Task P9-r. Fetch-only: sec.gov Archives re-fetched with curl (generic User-Agent), HTTP 200 on every URL tried between 06:09 and 06:14 UTC; efts.sec.gov full-text search still 403. Then every load-bearing claim below tier 3 on the Pass 9 list (25) and the review-1 list (27) was re-checked against `raw/*-2026-09-23.md` (204 files at read time).

### sec.gov primaries — 10 queue rows, 14 raw files, 0 failed

| queue row (substitute) | filing reached | raw | carried claim now at |
|---|---|---|---|
| `a-changeagents-funding-filing` (t5) | S-1/A No. 3, 2026-09-16 | `raw/b-sec-change-agents-s1a-2026-09-16-2026-09-23.md` | 2; "AWS $125,000" line not in the filing, stays 5 |
| `a-hubspot-filing` (index only) | 10-K FY2025, 2026-02-11 | `raw/b-sec-hubspot-10k-2026-02-11-2026-09-23.md` | 2 — Item 1 names AEO three times |
| `a-locafy-funding-filing` (t5) | F-3 2026-08-04; 6-K 2026-07-01; 6-K 2025-12-17 | `raw/b-sec-locafy-f3-2026-08-04-`, `-6k-2026-07-01-`, `-6k-2025-12-17-2026-09-23.md` | 2 |
| `a-yext-filing` (IR copy, t3) | 8-K Ex. 99.1, 2026-09-01 | `raw/b-sec-yext-8k-ex991-2026-09-01-2026-09-23.md` | 2; text identical to the IR copy |
| `b-criteo-second-source` (t5) | 10-Q Q2 2026, 2026-08-05 | `raw/b-sec-criteo-10q-2026-08-05-2026-09-23.md` | 2 |
| `b-microsoft-fy26-q4-release` (IR copy, t3) | 8-K Ex. 99.1 and 10-K, 2026-07-29 | `raw/b-sec-microsoft-8k-ex991-`, `-10k-2026-07-29-2026-09-23.md` | 2; no Copilot ad line in either |
| `c-feedonomics-second-source` (t5) | 10-Q 2026-08-06; 8-K Ex. 99.1 2026-09-10 | `raw/b-sec-commerce-10q-2026-08-06-`, `-8k-ex991-2026-09-10-2026-09-23.md` | 2 |
| `c-wix-second-source` (t5) | 6-K Ex. 99.1, 2026-08-04 (20-F checked) | `raw/b-sec-wix-6k-ex991-2026-08-04-2026-09-23.md` | ticker and revenue 2; ChatGPT app and Symphony not in any filing, stay 5 |
| `e-case-iac-investor-deck` (t2, chart) | 8-K Ex. 99.2, 2026-02-03 | `raw/b-sec-iac-8k-ex992-2026-02-03-2026-09-23.md` | 2 unchanged; text layer only, callout still not reconcilable |
| `e-spacex-s1a-grok-mau` (t2, digits cut) | S-1/A, 2026-06-03 | `raw/b-sec-spacex-s1a-2026-06-03-2026-09-23.md` | 2 unchanged; figures completed: 1.3 billion accounts; 0.9M / 1.9M SuperGrok subscribers |

### Sub-tier claims re-checked — itemised, both lists

Tiers: Pass 9 as the file stated on 2026-09-22; review-1 as `review-1-2026-09-23.md` §2 recounted; P9-r after this pass. n/a = meta-claim with no raw tier. Raw checked: P4-r `raw/e-case-census-r1-`, `e-case-*-`, `e-case-edgar-fulltext-results-`; P8-r `f-signal-*-`; P12 `b-*-`; P13 `e-*-user-counts-`, `e-market-size-*-`, `a-similarweb-*`, `e-statcounter-*`; P14 `d-paper-*`; R-BLOCKED `*-repull-2026-09-23.md`; the 14 `b-sec-*` files above.

| list | claim | file:line | Pass 9 | review-1 | P9-r | raw path / checked |
|---|---|---|---|---|---|---|
| both | C1 no Gold of ~980 | proof:59 | 5 | 5 | 5 | unchanged — `e-case-census-r1` (rows tier 5; 0 Gold in ~1,640 more), `e-case-edgar-fulltext-results` (tier 2, filings name actions, no design) |
| both | C2 seven Silver, observational | proof:60 | 5 | 5 | 5 | unchanged — X1, X2, X5, X6 raws tier 5; `e-nerdwallet-8k-repull` tier 2 lifts no weakest row |
| both | C3 two negative or null | proof:61 | 4 | 4 | 4 | unchanged — claim is about the seven Silvers; TW3 tier 4 remains; new negatives (HubSpot, Fortune tier 3) sit in the P4-r append, outside the seven |
| both | C4 paid-by-outcome 0/0/12 | proof:62 | 5 | 6 | 6 | unchanged — P4-r "0 new cases state fees" |
| both | C6 anchor 0 Silver | proof:64 | 5 | 5 | 5 | unchanged — P4-r skincare 0 Silver at ~155 |
| review-1 | success-stories row | proof:53 | — | 5 | 5 | unchanged — absence arm in all three under rule 1; case grades tier 5 |
| both | C1 cells 7/1/11/8 | demand:76 | 3 | 5 | 5 | unchanged — E1 `f-signal-sk-S4-omr-reviews` tier 5 still the weakest row; P8-r `f-signal-*-2026-09-23` restate cells, not this row |
| both | C6 compilers differ | demand:81 | 3 | n/a | n/a | unchanged — no raw by construction |
| both | C2 no measured size | white:59 | 3 | 6 | 6 | unchanged — P13 `e-market-size-*-2026-09-23` tier 5–6; `market-potential.md` C5 tier 6, H16 unresolved |
| both | C5 llms.txt unread | white:62 | 4 | 4 | 4 | unchanged — only 2026-09-23 raws naming llms.txt are `e-case-otterly-llms-txt-experiment` (tier 5) and census rows |
| both | C6 two evidence deserts | white:63 | 5 | 5 | 5 | unchanged — supplements first Bronze (Fire&Spark, tier 5); no Silver |
| both | C8 9 of 9 cells | white:65 | 3 | 5 | 5 | unchanged — Similarweb, Adthena rows (tier 5) still in the ChatGPT × paid cell; P12 tier-3 rows (`b-openai-help-*`, `b-google-ads-help-aio-ads`, `b-alphabet-*`) and tier-2 `b-alphabet-10k-2025-search-revenue` sit beside them, weakest row unchanged |
| both | C1 hypothesis tallies | unk:68 | 5 | 5 | 5 | unchanged — H3, H6 deciding rows tier 5 |
| both | C4 two of six done rows | unk:71 | 3 | n/a | n/a | unchanged — findings files only |
| both | C5 17 of 25 | unk:72 | 1 | n/a | n/a | unchanged — findings files only |

Claims already at tier ≤3 on both lists (not re-checked, tiers as review-1 §2): proof:63 C5 (3); demand:77 C2, :78 C3, :79 C4, :80 C5 (3); white:58 C1, :60 C3, :61 C4, :64 C7 (3); white:17 fee row (3); unk:69 C2, :70 C3 (1). Re-evidenced: 0 of 12 sub-tier claims. The sec.gov primaries move rows in `competitors/` (6 files), `findings/ai-ads-evidence.md` E13 and `markets/paid-placement.md:140` — evidence rows, not claims on either list; each carries a "Tier revisions, P9-r, 2026-09-23" append.

### Recount — six figures beside the three prior ones

| list | count | prior | P9-r 2026-09-23 |
|---|---|---|---|
| Pass 9 (25) | all load-bearing | 17 of 25 = 68.0% (2026-09-22 tiers) | 11 of 25 = 44.0% (tiers as the files now state, n/a counted as not ≤3) |
| Pass 9 (25) | excluding Lane E case corpus (proof C1, C2, C3, C4, C6; white C6; unk C1 = 7) | — | 11 of 18 = 61.1% |
| Pass 9 (25) | excluding meta-claims without raw tier (demand C6, unk C4, unk C5 = 3) | — | 11 of 22 = 50.0% |
| review-1 (27) | all load-bearing | 12 of 27 = 44.4% | 12 of 27 = 44.4% |
| review-1 (27) | excluding Lane E case corpus (the 7 above + proof:53 = 8) | — | 12 of 19 = 63.2% |
| review-1 (27) | excluding meta-claims (3) | 12 of 24 = 50.0% | 12 of 24 = 50.0% |

The Pass 9 "all" figure falls from 68.0% to 44.0% only because review-1's amendments (demand C1 3→5, white C2 3→6, white C8 3→5, unk C4/C5 →n/a) are now the tiers the files state; no tier moved down in this pass. Bar 80% not met on any of the six.

### Hypotheses — H17–H25, HE, HP, with prior marks side by side

| ID | mark | producing file:line | evidence tier | prior marks |
|---|---|---|---|---|
| H17 | **killed** | `ai-ads-evidence.md:74` | 3 | registered `unresolved` 2026-09-23; sec.gov re-fetch: Microsoft 8-K/10-K state search advertising only, no AI-surface line (`raw/b-sec-microsoft-8k-ex991-2026-07-29-2026-09-23.md`) — consistent, no new mark |
| H18 | **confirmed** | `ai-ads-evidence.md:75` | 3 (Kontext "$3 CPM", network, not an engine) | registered `unresolved` |
| H19 | **confirmed** | `ai-ads-evidence.md:76` | 3 (Microsoft Advertising into Snap My AI, 2023 page) | registered `unresolved` |
| H20 | **killed** | `ai-ads-evidence.md:77` | 5 (15 screened, 0 with control) | registered `unresolved` |
| H21 | **killed** | `market-potential.md:82`, `:84` | 3 (Claude: no dated user count) | registered `unresolved` |
| H22 | **killed** | `market-potential.md:82`, `:84` | 6 (organic 1.92× ≤ 3) | registered `unresolved` |
| H23 | **confirmed** | `frontier-scan.md:61` | 3 | registered `unresolved` |
| H24 | **confirmed** | `frontier-scan.md:62` | 4 | registered `unresolved` |
| H25 | **confirmed** | `frontier-scan.md:63` | 4 | registered `unresolved` |
| HE1 | **confirmed** | this file, register row HE1 (2026-09-22); `review-1:33` agree | 3 | Pass 9 confirmed; review-1 confirmed |
| HE2, HE3, HP1–HP4 | **not produced** ×6 | `hypotheses.md` log additions 2026-09-23 | — | Pass 9 not produced; review-1 not produced; Pass 10 skipped by user 2026-09-23 |

H1–H16, every prior mark side by side (Pass 9 = 2026-09-22 file before amendment; review-1 = `review-1-2026-09-23.md` §1; P8-r, P4-r = appends above; P11 = `STATE.md` Done conditions row; P13/P14 = restated marks in `market-potential.md:84`, `frontier-scan.md:64–65`):

| ID | Pass 9 | review-1 | P8-r | P4-r | P11 / P13 / P14 | P9-r 2026-09-23 |
|---|---|---|---|---|---|---|
| H1 | unresolved | unresolved | — | — | — | no change |
| H2 | confirmed | confirmed | — | — | — | no change |
| H3 | killed | killed | — | killed — unchanged | — | no change |
| H4 | killed | killed | killed — reinforced | — | — | no change |
| H5 | killed | unresolved — checked | — | — | P14: Pass-9 mark stands, confirm side strengthened (t3/4 pre/post) | no change |
| H6 | confirmed | unresolved — checked | — | confirmed (rule1, narrow) / unresolved (verticals) | — | no change |
| H7 | unresolved | unresolved | confirmed (loose) / unresolved (strict) | — | — | no change |
| H8 | confirmed | confirmed | — | — | — | no change |
| H9 | unresolved | unresolved | confirmed (loose) / unresolved (strict) | — | — | no change |
| H10 | not produced | not produced | — | — | P11: confirmed | no change |
| H11 | killed | not produced | — | confirmed — action named; outcome unknown in two of three | P11: confirmed | mark unchanged; B2B SaaS row evidence tier 3 → 2: HubSpot 10-K Item 1, "launched the marketing playbook for the AI era: Loop Marketing… modern tactics such as AEO" (`raw/b-sec-hubspot-10k-2026-02-11-2026-09-23.md`), beside the Fortune op-ed (tier 3) |
| H12 | unresolved | unresolved | — | — | — | no change |
| H13 | confirmed | confirmed | — | — | P14: stands, dated P1 statements added | no change |
| H14 | killed | killed | — | — | — | no change |
| H15 | killed | unresolved — checked | — | — | — | no change |
| H16 | confirmed | unresolved — checked | — | — | P13: unresolved — checked | no change |

Marks now carried, every H: confirmed H2, H8, H13, HE1, H10, H11, H18, H19, H23, H24, H25 (plus H6, H7, H9 dual); killed H3, H4, H14, H17, H20, H21, H22; unresolved — checked H1, H5, H12, H15, H16 (plus H6, H7, H9 dual); not produced HE2, HE3, HP1–HP4. Programme-done Hypotheses row: 26 of 32 scored; 6 `not produced`, not reachable while Pass 10 is skipped.

### Caveats, this append

- Not re-checked: the 12 claims already at tier ≤3 (tiers taken from review-1 §2); the review-1 line numbers were verified unchanged in `proof-scorecard.md`, `demand-map.md`, `whitespace.md` and this file on 2026-09-23. `demand-map.md`'s P8-r restated tallies and `proof-scorecard.md`'s P4-r restated claims are new rows, not on either list, and are not counted.
- sec.gov: 0 fetches failed; efts.sec.gov full-text search 403 (not needed — filings located through `data.sec.gov/submissions/`). HubSpot's revenue and headcount passages were not extracted (outside the carried claim). The Wix ChatGPT-app claim has no filed primary; the Change Agents "AWS $125,000" line has none.
- Recount "all" counts n/a meta-claims as not at tier 3; a reader treating n/a as excluded reads the ex-meta row. Lane E case corpus membership follows `plan-review-2-2026-09-23.md` §2's decomposition (8 case-corpus, 1 forecast, 3 third-party, 3 meta).
- H17–H25 marks are copied from the producing files, not re-scored here; H18 and H19 confirm outside P1 engines (`ai-ads-evidence.md:98`). This file was over budget before this append; overrun stated here. Evidence, not a verdict.

## Hypothesis register — 32 rows, COMPILE-2, 2026-09-23

Task COMPILE-2 (Pass 16), per `method/plan.md` "Pass sequence — addition 3" and `method/biz-review-solution-2026-09-23.md` §2 row 6. Appended only. Every prior mark copied verbatim from its producing file; nothing re-scored, nothing reconciled. `—` = that pass did not re-score the row; `not registered` = row registered 2026-09-23, after the pass ran; `not produced` = producing pass did not run (`hypotheses.md` scoring rule). Statements abbreviated from `method/hypotheses.md` register rows. Line numbers as read 2026-09-23 before this append.

| ID | Statement | Pass 9 (2026-09-22) | review-1 | P8-r / P4-r / R-BLOCKED-2 / P11–P14 | P9-r 2026-09-23 | Producing file:line | Strongest raw (tier) |
|---|---|---|---|---|---|---|---|
| H1 | AI referral converts above organic search | unresolved — checked Adobe, Salesforce, Shopify 2026-09-22 | unresolved | — | no change | `unknowns.md:25` | `raw/c-retail-analytics-table-2026-09-22.md` (4) |
| H2 | Paid inventory inside AI surfaces exists at scale | **confirmed** | confirmed | — | no change | `unknowns.md:26`; `markets/paid-placement.md:74` | `raw/b-openai-platform-summary-2026-09-22.md` (3) |
| H3 | At least one vendor demonstrates causal lift | **killed** | killed | P4-r: killed — unchanged | no change | `unknowns.md:27`, `:124`; `proof-scorecard.md:59`, `:112` | `raw/e-case-census-c13-2026-09-22.md` (5); `raw/e-case-census-r1-2026-09-23.md` (5) |
| H4 | Demand is attention-only in every SMB cell | **killed** | killed | P8-r: killed — unchanged, reinforced; R-BLOCKED-2: killed, unchanged | no change | `unknowns.md:28`, `:108`; `demand-map.md:148` §R-BLOCKED-2 | `raw/f-signal-bs-S1-linkedin-jobs-guest-api-2026-09-22.md` (3) |
| H5 | Corpus seeding measurably moves an answer | killed | **unresolved — checked** | P14: Pass-9 mark stands, confirm side strengthened (t3/4 pre/post) | no change | `unknowns.md:29`; `frontier-scan.md:64` | `raw/d-citationpref-featgeo-2026-09-22.md` (3); `raw/d-paper-bias-beware-cognitive-bias-2026-09-23.md` (3) |
| H6 | Brand action precedes measured visibility change, P1 engine | confirmed | **unresolved — checked** | P4-r: confirmed (rule1, narrow) / unresolved — checked (three verticals), both stand | no change | `unknowns.md:30`, `:125`; `proof-scorecard.md:102` §P4-r | `raw/e-case-otterly-reddit-experiment-2026-09-23.md` (5); `raw/e-case-sitefire-pointhound-2026-09-22.md` (5) |
| H7 | Organic carries spend in more cells than others | unresolved — checked (channel list in `demand-map.md`) 2026-09-22 | unresolved | P8-r: confirmed (loose reading) / unresolved — checked (strict reading), both stand; R-BLOCKED-2: strict unchanged, unresolved — checked, resting on E2 alone | no change | `unknowns.md:31`, `:109`; `demand-map.md:130`, `:148` | `raw/f-ted-S10-repull2-2026-09-23.md` (2); S1 posting raws (3) |
| H8 | A protocol is implementable without a contract | **confirmed** | confirmed | — | no change | `unknowns.md:32`; `markets/agentic-commerce.md:84` | `raw/c-agentic-commerce-protocols-table-2026-09-22.md` (3) |
| H9 | Agentic spend in enterprise cells, absent from SMB | unresolved — checked (same list) 2026-09-22 | unresolved | P8-r: confirmed (loose reading) / unresolved — checked (strict reading), both stand; R-BLOCKED-2: strict unresolved — checked → **confirmed**; both readings now confirmed | no change | `unknowns.md:33`, `:110`; `demand-map.md:148` §R-BLOCKED-2; `hypotheses.md` log R-BLOCKED-2 | `raw/f-ted-S10-repull2-2026-09-23.md` (2); `raw/c-google-ucp-merchant-agentic-2026-09-22.md` (3) |
| H10 | Org / content-ops changes outnumber paid-media changes | **not produced** | not produced | P11: **confirmed** — tier ≤3: org/content 28 (13 excl. llms.txt), paid 2 | no change | `unknowns.md:34`; `transition-evidence.md:66` | `raw/c-google-ucp-merchant-agentic-2026-09-22.md` (3); `f-signal-*-S1-*` (3) |
| H11 | Tier-3 transition evidence in each vertical | **killed** | **not produced** | P4-r: confirmed — action named; outcome unknown in two of three; P11: **confirmed** — e.l.f., Pennylane, Cigna | mark unchanged; B2B SaaS row evidence tier 3 → 2 | `unknowns.md:35`, `:126`, `:218`; `transition-evidence.md:67` | `raw/b-sec-hubspot-10k-2026-02-11-2026-09-23.md` (2) |
| H12 | Paid inventory price disclosed publicly, not under contract | unresolved — checked openai.com, support.google.com/google-ads, about.ads.microsoft.com, advertising.amazon.com 2026-09-22 | unresolved | — | no change | `unknowns.md:36`; `markets/paid-placement.md:39` | `raw/b-openai-ads-basics-pricing-2026-09-22.md` (3) |
| H13 | A P1 engine names a Pass-5 technique | **confirmed** | confirmed | P14: stands, dated P1 statements added | no change | `unknowns.md:37`; `frontier-scan.md:65` | `raw/d-technique-census-c7-2026-09-22.md` (3) |
| H14 | Manipulation evidence denser in regulated than anchor | **killed** | killed | — | no change | `unknowns.md:38` | `raw/d-technique-census-c2-2026-09-22.md` (4) |
| H15 | Composite-score vendors disclose the prompt set | killed | **unresolved — checked** | — | no change | `unknowns.md:39`; `markets/organic-recommendation.md` | `raw/a-vendor-census-c1-2026-09-22.md` (3) |
| H16 | Every published sub-market size is a forecast | confirmed | **unresolved — checked** | P13: unresolved — checked | no change | `unknowns.md:40`; `market-potential.md:84` | `raw/e-market-size-table-2026-09-22.md` (6) |
| HE1 | ChatGPT paid product live on its own surface | **confirmed** | confirmed | — | **confirmed** | `unknowns.md:41`, `:201` | `raw/b-openai-platform-summary-2026-09-22.md` (3) |
| HE2 | Claude returns brand recommendations to buying prompts | **not produced** | not produced | Pass 10 skipped by owner 2026-09-23 | **not produced** | `unknowns.md:42`, `:202`; `plan.md:320` | `raw/e-claude-panel-2026-09-22.md` (1, unusable for this row) |
| HE3 | Ad-labelled formats render inside Google AI surfaces | **not produced** | not produced | Pass 10 skipped by owner 2026-09-23 | **not produced** | `unknowns.md:43`, `:202` | `raw/e-google-aimode-panel-2026-09-22-retry.md` (1, one date) |
| HP1 | Between-engine gap exceeds within-engine spread | **not produced** | not produced | Pass 10 skipped by owner 2026-09-23 | **not produced** | `unknowns.md:44`, `:202` | `raw/e-gemini-panel-2026-09-22.md`, `raw/e-chatgpt-panel-2026-09-22.md` (1) |
| HP2 | Recommended brand set unstable between dates | **not produced** | not produced | Pass 10 skipped by owner 2026-09-23 | **not produced** | `unknowns.md:45`, `:202` | none — `method/STATE.md` §Pass 10 sampling log |
| HP3 | Citation-to-mention ratio below 0.50 | **not produced** | not produced | Pass 10 skipped by owner 2026-09-23 | **not produced** | `unknowns.md:46`, `:202` | `raw/e-claude-panel-2026-09-22.md` (1) |
| HP4 | Citation rate higher with web search on | **not produced** | not produced | Pass 10 skipped by owner 2026-09-23 | **not produced** | `unknowns.md:47`, `:202` | `raw/e-gemini-panel-2026-09-22.md` (1) |
| H17 | Non-ChatGPT engine discloses AI-surface advertiser count or revenue | not registered | not registered | P12: **killed**; R-BLOCKED-2: not moved | **killed** | `ai-ads-evidence.md:74`, `:129`; `unknowns.md:192` | `raw/b-sec-microsoft-8k-ex991-2026-07-29-2026-09-23.md` (2); `raw/b-alphabet-q2-2026-earnings-transcript-2026-09-23.md` (3) |
| H18 | An engine or network publishes an AI-answer rate card | not registered | not registered | P12: **confirmed**; R-BLOCKED-2: not moved | **confirmed** | `ai-ads-evidence.md:75`; `unknowns.md:193` | `raw/b-kontext-advertisers-page-2026-09-23.md` (3) |
| H19 | A party outside an engine's ad program sells placement | not registered | not registered | P12: **confirmed**; R-BLOCKED-2: not moved | **confirmed** | `ai-ads-evidence.md:76`; `unknowns.md:194` | `raw/b-microsoft-ads-snap-my-ai-partnership-2026-09-23.md` (3) |
| H20 | Advertiser reports a controlled AI-ads result, n and window | not registered | not registered | P12: **killed** — 15 screened; R-BLOCKED-2: killed mark stands, near-miss RB1b recorded | **killed** | `ai-ads-evidence.md:77`, `:129`; `unknowns.md:195` | `raw/b-reddit-advertiser-reports-repull2-2026-09-23.md` (5) |
| H21 | Every P1 engine has two dated tier-3 user counts | not registered | not registered | P13: **killed** | **killed** | `market-potential.md:82`, `:84`; `unknowns.md:196` | `raw/e-anthropic-claude-scale-statements-2026-09-23.md` (3) |
| H22 | Highest forecast exceeds lowest by more than 3× everywhere | not registered | not registered | P13: **killed** | **killed** | `market-potential.md:82`, `:84`; `unknowns.md:197` | `raw/e-market-size-table-2026-09-22.md` (6); organic 2034 rows (6) |
| H23 | Peer-reviewed steering technique with code, no named countermeasure | not registered | not registered | P14: **confirmed** | **confirmed** | `frontier-scan.md:61`; `unknowns.md:198` | `raw/d-paper-bias-beware-cognitive-bias-2026-09-23.md` (3); `raw/d-technique-census-c7-2026-09-22.md` (3) |
| H24 | Paper describes in-answer monetisation no P1 engine offers | not registered | not registered | P14: **confirmed** | **confirmed** | `frontier-scan.md:62`; `unknowns.md:199` | `raw/d-paper-token-auction-mechanism-2026-09-23.md` (4) |
| H25 | A kept capability runs on public code and models | not registered | not registered | P14: **confirmed** | **confirmed** | `frontier-scan.md:63`; `unknowns.md:200` | `raw/d-paper-strategic-text-sequence-2026-09-23.md` (4); `raw/d-paper-meta-secalign-open-defense-2026-09-23.md` (4) |

**Tallies, one line per source of marks** — each as its source states it, none reconciled:

| Source | Rows | confirmed | killed | unresolved — checked | not produced | Where stated |
|---|---|---|---|---|---|---|
| Pass 9, 2026-09-22 file before amendment | 23 | 6 (H2, H6, H8, H13, H16, HE1) | 6 (H3, H4, H5, H11, H14, H15) | 4 (H1, H7, H9, H12) | 7 (H10, HE2, HE3, HP1–HP4) | `unknowns.md:206–223` "Pass 9" column; `biz-review-1:73` "6/6/4/7" |
| Pass 9 as amended 2026-09-23 per review-1 §9 | 23 | 4 (H2, H8, H13, HE1) | 3 (H3, H4, H14) | 8 (H1, H5, H6, H7, H9, H12, H15, H16) | 8 (H10, H11, HE2, HE3, HP1–HP4) | `unknowns.md:49` |
| review-1, 2026-09-23 | 23 | 4 | 3 | 8 | 8 | `review-1-2026-09-23.md:41`; disagreements 5 |
| P8-r | 23 | 4 + 2 dual (H7, H9, loose only) | 3 | 8 (H7, H9 carry both) | 8 | `unknowns.md:112` |
| P4-r | 3 touched | H6 dual; H11 confirmed | H3 unchanged | H6 dual | H11 leaves `not produced` | `unknowns.md:128` |
| P11 | 2 touched | H10, H11 | — | — | — | `transition-evidence.md:66–67`, `:74` |
| P12 | 4 touched | H18, H19 | H17, H20 | — | — | `ai-ads-evidence.md:74–77` |
| P13 | 3 touched | — | H21, H22 | H16 | — | `market-potential.md:84` |
| P14 | 5 touched | H23, H24, H25; H13 stands | — | H5 stands | — | `frontier-scan.md:61–65` |
| R-BLOCKED-2 | 6 touched | H9 (strict → confirmed) | H20 stands; H4 unchanged | H7 unchanged | — | `hypotheses.md` log R-BLOCKED-2; `demand-map.md:148`; `ai-ads-evidence.md:129` |
| P9-r, 2026-09-23 (latest full register) | 32 | 11 (H2, H8, H10, H11, H13, HE1, H18, H19, H23, H24, H25) + 3 dual (H6, H7, H9) | 7 (H3, H4, H14, H17, H20, H21, H22) | 5 (H1, H5, H12, H15, H16) + 3 dual | 6 (HE2, HE3, HP1–HP4) | `unknowns.md:225`; `STATE.md` Done conditions "26 of 32 scored" |
| P9-r with R-BLOCKED-2's H9 mark applied | 32 | 12 + 2 dual (H6, H7) | 7 | 5 + 2 dual | 6 | this table — arithmetic on the two rows above, not a new score |

Programme-done Hypotheses row, as `plan.md` "Programme done — addition 2026-09-23" asks: scored 26 of 32; the six named `not produced` are HE2, HE3, HP1, HP2, HP3, HP4, Pass 10 skipped by owner 2026-09-23.

**Caveats, this append.** Marks are copied, not re-scored; where a producing file gives a mark with a qualifier ("loose", "strict", "rule1, narrow", "action named; outcome unknown") the qualifier is part of the mark and stays. Dual marks count once in each of two columns; the "12 + 2 dual" row is this append's arithmetic on stated marks, not a score from any pass. H17–H25 "not registered" for Pass 9 and review-1 is a registration fact (`hypotheses.md` "Additions 2026-09-23"), not a scoring mark. Line numbers cite files as read 2026-09-23 before this append; concurrent appends by other agents do not move lines above them. This file was over its 100-line budget before this append; overrun stated here. Evidence, not a verdict.

## Figures carried twice, COMPILE-2, 2026-09-23

Task COMPILE-2 (Pass 16), per `method/biz-review-solution-2026-09-23.md` §2 (contradictions paragraph). Rows 1–14 are `method/biz-review-1-2026-09-23.md` §4 verbatim; rows 15 on are pairs found in this pass. Both figures stand; nothing reconciled or averaged. Kinds: stale duplicate · two bases · two tiers · two definitions · two sources · two dates · two readings. Line numbers as read 2026-09-23.

| # | Figure A (file:line) | Figure B (file:line) | Kind |
|---|---|---|---|
| 1 | Organic floor "$5.3M–$35.2M annualised", tier 5 — `organic-recommendation.md:36`; `executive-brief:22` | Floor "$42.2M–$48.2M + €2.2M", tier 2/5 — `market-potential.md:60`; `organic-recommendation.md:131` | two bases (price × count vs disclosed ARR); same label "floor" |
| 2 | Segment tally 7/1/11/8 — `demand-map.md:17`; `executive-brief:36`; `director-brief:126` | 8/1/18/0 loose, 8/1/10/8 strict — `demand-map.md:121–124`; 8/1/17/1 strict after R-BLOCKED-2 — `demand-map.md:148` § | stale duplicate; three dated reads |
| 3 | "15 of 18 published figures are forecasts" — `executive-brief:21`; `whitespace.md:24` | 10 new forecasts added — `market-potential.md:46`, `:84` | stale count |
| 4 | Agentic spread "roughly 35×" (2029–30) — `agentic-commerce.md:54`; `director-brief:58` | 26.3× (2030 only) — `market-potential.md:54`; `agentic-commerce.md:132` | two bases |
| 5 | Paid engines live "5 of 8" — `paid-placement.md:39` | "Four engines" — `ai-ads-evidence.md:18`; "two of the three priority-1 engines" — `executive-brief:15` | three counting bases |
| 6 | Perplexity ads "status read by absence" — `paid-placement.md:82` | "winding down… by the end of 2026", tier 5 — `ai-ads-evidence.md:53` E15 | two dates; older row not annotated |
| 7 | Within-AIO ads "12 named countries" — `paid-placement.md:76` | "Australia… and US" — `ai-ads-evidence.md:48` E10 | two dates, same page family |
| 8 | ChatGPT VLOSE, filed tier 2 — `executive-brief:40`; `paid-placement.md:92` | Same fact, analyst-derived tier 5 — `ai-ads-evidence.md:56` E18 | two tiers |
| 9 | Datos ChatGPT "34.80% share of total desktop visits" — `plan.md:183` | Datos "AI tools 1.65% of desktop search events" — `market-potential.md:41` | two definitions (glossary rows added 2026-09-23) |
| 10 | AI Mode "1B MAU" 2026-05-19 — `market-potential.md:26` | AI Mode "query share 0.34%" Jan–Apr 2026 — `plan.md:185` | two definitions; not contradictory |
| 11 | Hypothesis tallies 6/6/4/7 (Pass 9), 4/3/8/8 (review-1), "4 + 2 dual" — `unknowns.md:49`, `:112` | H17–H25 marks only in `ai-ads-evidence.md:74–77`, `market-potential.md:84`, `frontier-scan.md:61–63`; 32-row register now above | stale duplicate; closed this pass |
| 12 | Pass 10 "held" — `director-brief:36`, `:245` | "skipped by owner" — `plan.md:320–328`; `STATE.md` Done conditions | stale status wording |
| 13 | By-file tier-3 counts "demand-map 6 of 6, whitespace 6 of 8" — `unknowns.md:55` | Headers "5 of 7" (`demand-map.md:9`), "4 of 8" (`whitespace.md:9`) | stale roll-up; restated below |
| 14 | Copilot Checkout fee 0% — `agentic-commerce.md:25`, `:89` | `unknown` — `raw/c-agentic-commerce-protocols-table-2026-09-22.md` | two pulls, one FAQ; recorded at `agentic-commerce.md:119` |
| 15 | Peec AI ARR "more than $4 million", 2025-11-17 — `competitors/peec-ai.md:26`; `market-potential.md:60` | "10m", 2026-05-23 headline slug — `peec-ai.md:26`; `organic-recommendation.md:115` | two dates, two sources |
| 16 | geoSurge "$12M seed" — `competitors/geosurge.md:28`; `organic-recommendation.md:28` | "€10M" same round, EU-Startups — `geosurge.md:61`; `organic-recommendation.md:117` | two sources, one round |
| 17 | Scrunch acquisition "not disclosed", tier 3 — `competitors/scrunch-ai.md:32`; `organic-recommendation.md:87` | "$225 Million", tier 5 — `raw/a-bloomberg-scrunch-sitecore-primary-2026-09-23.md`; `raw/a-vendor-roster-2026-09-22.md` row 1 | two tiers |
| 18 | Tier-3 share "17 of 25 = 68.0%" — `unknowns.md:55`, `:72` | "12 of 27 = 44.4%" — `review-1:9`; "11 of 25 = 44.0%" — `unknowns.md:179` | two lists, two tier bases |
| 19 | Silver "7" as graded in raw — `proof-scorecard.md:23`, `:60` | Silver "1" under grading rule 1 — `proof-scorecard.md:23`, `:113` | two readings (grade_raw / grade_rule1) |
| 20 | Sitefire / Jerry "Bronze (c10)" — `proof-scorecard.md:27`; `competitors/sitefire.md:52` | "Silver (c13)" — same lines | two censuses, one page |
| 21 | ChatGPT ad presence "0.8% of 500+ prompts" (launch weeks) — `ai-ads-evidence.md:46` E8 | "26% US desktop (Jun)"; "24.7% (Jul)"; "25.94% of 50,006 US prompts" — `ai-ads-evidence.md:45–46` E7, E8 | two dates, panels; not reconciled per `ai-ads-evidence.md:58` |
| 22 | Amazon Q1 2026 ads growth "up 22%" — `paid-placement.md:141`; `ai-ads-evidence.md:58` | "24%" — PPC Land, same lines | two sources, tier 3 vs 5 |
| 23 | Hypotheses scored "15 of 23" — `unknowns.md:17`, `:59` | "26 of 32" — `unknowns.md:225`; `STATE.md` Done conditions | stale count |
| 24 | OpenAI ads "$1 billion in annualized revenue run rate", tier 3 — `paid-placement.md:25`; `ai-ads-evidence.md:39` | "roughly $83 million a month", tier 5 — `paid-placement.md:131`; `ai-ads-evidence.md:40` | two tiers, same fact |
| 25 | ChatGPT advertisers "tens of thousands", 2026-08-31, tier 3 — `ai-ads-evidence.md:39` | "over 600", 2026-03-26, tier 5 — `ai-ads-evidence.md:40`; panels 820 to 7,378 — `:44` | two dates; panel scopes |
| 26 | Microsoft "search ad revenue ex-TAC +10%", tier 3 — `paid-placement.md:140`; `ai-ads-evidence.md:51` | same, tier 2 (8-K Ex. 99.1) — `ai-ads-evidence.md:139` | two tiers |
| 27 | Kontext "Rates starting from just $3 CPM", tier 3 — `paid-placement.md:150` | "$2.50 CPM vs Facebook $7.35 (one pilot)", tier 5 — `paid-placement.md:151` | two kinds (floor vs pilot), two tiers |
| 28 | Comscore Copilot "US desktop unique visitors" 5.02M, Mar 2026 — `plan.md:187` | Comscore "desktop unique visitors", CustomIQ 33.4M, Dec 2025 — `plan.md:187` | two bases, one publisher |
| 29 | Similarweb AI Mode "query share 0.34%" — `plan.md:185` | Datos AI Mode "0.16% US, 0.21% EU/UK, share of total desktop visits" — `plan.md:185` | two definitions, two panels |
| 30 | Rankscale "$20/mo" — `competitors/rankscale-ai.md:22` | "from €20" on /facts — same line; `organic-recommendation.md:117` | two pages, one vendor |
| 31 | Ahrefs Brand Radar standalone "$199" — `competitors/ahrefs.md:71` | "¥30,600/mo" — same line; `organic-recommendation.md:117` | two pages, geolocated |
| 32 | RankPrompt Starter "$39 per month" — `INDEX.md:26` | "$49/mo" same page — `INDEX.md:26`; `organic-recommendation.md:117` | one page, two figures |
| 33 | HubSpot standalone "¥6,000/mo" — `INDEX.md:25` | "$50/mo" — `INDEX.md:25` | two pages, geolocated |
| 34 | Shopware Rise "€600/mo" — `competitors/shopware.md:77` | "$600" on G2 — same line | two sources |
| 35 | Similarweb ticker SMWB "Nasdaq" — `competitors/similarweb.md:11` | "NYSE" own release 2026-08-17 — same line | two sources |
| 36 | Peec AI headcount "the 20-person startup", 2025-11 — `competitors/peec-ai.md:27` | "around 70+ people", undated — same line | two dates |
| 37 | Peec AI customers "1,300 companies and agencies" — `peec-ai.md:28` | "Trusted by 3000+ brands and agencies" — same line | two dates, two units |
| 38 | SE Ranking ARR "$35M", 2024 — `INDEX.md:42` | "$21M", 2024 — same line; `competitors/se-ranking.md:78` | two aggregators, one year |
| 39 | Change Agents "AWS gave $125,000 project funding" — `competitors/change-agents-corp.md:31` | not found in the S-1/A or 10-Q — `change-agents-corp.md:89` | tier-5 substitute vs tier-2 filing |
| 40 | Similarweb "share of worldwide generative AI web traffic" ChatGPT ~53%, May 2026 — `plan.md:183` | StatCounter "AI Chatbot Market Share" 79.4%, Aug 2026 — `plan.md:183` | two definitions, two publishers |
| 41 | Skincare × Agentic × Enterprise reads "spend" — `demand-map.md:135`, `:52` | Same cell reads "attention" — e.l.f. posting tier 3, "below the tier-5 spend floor" — `agentic-commerce.md:105` | two readings, two compilers |

41 pairs: 14 from review §4, 27 found. Kinds: stale duplicate or count 6; two bases or definitions 9; two tiers 5; two sources, dates or pages 17; two readings 3; two pulls 1.

**Caveats, this section.** A pair is listed so the brief writer sees both figures; listing is not a judgment that either is wrong. Rows 30–38 are vendor-page conflicts already carried unreconciled in their profiles; they are repeated here because the profile caveats are not read from `findings/`. Row 11 and row 13 are closed by this pass's appends (register above, roll-up below); the older lines stand unedited. Line numbers were verified 2026-09-23 before this append.

## By-file tier-3 roll-up restated, 2026-09-23

Per `biz-review-1-2026-09-23.md` §4 row 13 and §7 row 21. The stale roll-up at `unknowns.md:55` sits beside each findings file's current header line ("Claims at tier 3 or better"), read 2026-09-23. Headers count every claim the file lists; the L55 roll-up counted load-bearing claims as of 2026-09-22.

| File | Roll-up at `unknowns.md:55` (2026-09-22) | Header line, as read 2026-09-23 | What moved |
|---|---|---|---|
| `proof-scorecard.md` | 1 of 6 | 1 of 7 (`:9`) | header counts C1–C7; C4 5 → 6 per review-1 §9 |
| `demand-map.md` | 6 of 6 | 5 of 7 (`:9`) | review-1 §9: header "7 of 7" → "5 of 7"; C1 3 → 5, C6 → n/a |
| `whitespace.md` | 6 of 8 | 4 of 8 (`:9`) | review-1 §9: "6 of 8" → "4 of 8"; C2 → 6, C8 → 5 |
| `unknowns.md` | 4 of 5 | 4 of 5 (`:9`) | none in header; C4, C5 → n/a per review-1 §2 |
| `ai-ads-evidence.md` | not in roll-up | 3 of 5 (`:10`) | file written 2026-09-23 |
| `market-potential.md` | not in roll-up | 3 of 7 (`:8`) | file written 2026-09-23 |
| `frontier-scan.md` | not in roll-up | 6 of 9 (`:9`) | file written 2026-09-23 |
| `transition-evidence.md` | not in roll-up | 5 of 7 (`:9`) | file written 2026-09-23 |
| `trigger-timeline.md` | not in roll-up | 2 of 2 (`:9`) | file written 2026-09-23 |
| `review-1-2026-09-23.md` | not in roll-up | "recount 12 of 27 = 44.4%; findings state 17 of 25" (`:9`) | recount, not a file count |
| `executive-brief-2026-09-23.md`; `director-brief-2026-09-23.md` | not in roll-up | "none new; restates compiled figures" (`:9`) | no own claims |

Sum of the nine header lines with a count: 33 of 57. Stated for diffing only: it is a sum of headers, not a recount on the Pass 9 list (11 of 25 = 44.0%) or the review-1 list (12 of 27 = 44.4%) at `unknowns.md:177–184`, and headers include non-load-bearing claims. Programme-done bar 80% is met by no figure in this section.

**Caveats, this section.** The L55 roll-up is not edited; it is the 2026-09-22 read and stands. Headers are self-reported by each file's author on its file date and were not re-verified claim by claim here; P9-r's itemised recount (`unknowns.md:155–171`) is the verified count. This file was over its 100-line budget before this append; overrun stated here. Evidence, not a verdict.

## Tier-3 recount and done rows, RECOUNT-2, 2026-09-23

Task RECOUNT-2. Desk only, 0 pulls. P9-r method (`unknowns.md` §Tier-3 recount, P9-r) re-run on both lists against every `raw/` file on disk (1,013 files; 405 dated 2026-09-23, up from 204 at P9-r). Claim tier = tier of its weakest load-bearing row; moved only if that row now has a tier ≤3 source. Line numbers as read 2026-09-23.

### Pass 9 (25) and review-1 (27) lists, itemised

Tiers column: Pass 9 / review-1 / P9-r. n/a = meta-claim, no raw tier.

| list | file:claim | best raw now (tier) | weakest row now (tier) | tiers | now | moved |
|---|---|---|---|---|---|---|
| both | proof:59 C1 0 Gold | `e-case-edgar-fulltext-results-2026-09-23` (2) | `e-case-census-r1-2026-09-23` (5) | 5/5/5 | 5 | no |
| both | proof:60 C2 seven Silver | `e-case-nerdwallet-earnings-release-2026-02-25-2026-09-22` (2) | E1–E5 raws; Otterly `-repull2` (5) | 5/5/5 | 5 | no |
| both | proof:61 C3 two negative/null | NerdWallet 8-K (2) | `e-case-c11-arxiv-tw3-partners-geo-score` (4), no reviewed version | 4/4/4 | 4 | no |
| both | proof:62 C4 paid-by-outcome | `e-case-ulta-nielseniq-smart-beauty-primary` (3), Bronze, ungraded set | `e-case-census-c4-2026-09-22` (6) | 5/6/6 | 6 | no |
| both | proof:63 C5 59 brands silent | `e-case-census-c7-2026-09-22` (3) | same (3); count stale, 1 of 168 | 3/3/3 | 3 | no |
| both | proof:64 C6 anchor 0 Silver | `e-case-ulta-*-primary-2026-09-23` (3), Bronze / no claim | Seer E4 (5) | 5/5/5 | 5 | no |
| r1 | proof:53 success-stories row | NerdWallet 8-K (2) | Seer E4 (5) | —/5/5 | 5 | no |
| both | demand:76 C1 7/1/11/8 | `f-signal-sk-S1-hydrafacial-workday-geo-aeo-2026-09-23` (3) | `f-signal-sk-S4-omr-reviews-2026-09-22` (5) | 3/5/5 | 5 | no; count stale |
| both | demand:77 C2 S1 weakest class | same Hydrafacial raw (3) | S1 raws (3) | 3/3/3 | 3 | no; now 7 of 9 |
| both | demand:78 C3 WTP unknown | `f-signal-*-S11-price-paid-2026-09-22` (2 / n/a) | same (3) | 3/3/3 | 3 | no |
| both | demand:79 C4 organic 5/1/1 | S1 raws (3) | same (3) | 3/3/3 | 3 | no; now 7/1/1 |
| both | demand:80 C5 5 of 7 enterprise | S1 raws (3) | same (3) | 3/3/3 | 3 | no; now 5 of 9 |
| both | demand:81 C6 compilers differ | none by construction | — | 3/n/a/n/a | n/a | no |
| both | white:58 C1 0 rate cards | `b-openai-help-ads-basics-2026-09-23` (3) | same (3) | 3/3/3 | 3 | no |
| both | white:59 C2 no measured size | `e-market-size-emarketer-aiads-primary-2026-09-23` (4) | `e-market-size-table-2026-09-22` (6) | 3/6/6 | 6 | no |
| both | white:60 C3 techniques unnamed | `d-openai-prompt-injections-primary-2026-09-23` (3) | `d-technique-census-c7` (3); Google generic clause beside | 3/3/3 | 3 | no |
| both | white:61 C4 no prompt set | `a-vendor-census-c1`…`-c4-2026-09-22` (3) | same (3) | 3/3/3 | 3 | no |
| both | white:62 C5 llms.txt unread | `a-google-ai-features-guidance-2026-09-22` (3) | Borysenko preprint (4); Otterly 81 ChatGPT-User fetches (5) contra | 4/4/4 | 4 | no; contested |
| both | white:63 C6 two deserts | `e-case-census-c8`, `-c10-2026-09-22` (5) | same (5) | 5/5/5 | 5 | no |
| both | white:64 C7 59 of 59 silent | `e-case-census-c7-2026-09-22` (3) | same (3); P4-r 1 of 168 | 3/3/3 | 3 | no |
| both | white:65 C8 9 of 9 cells | `b-openai-1bn-run-rate-milestone-2026-09-22` (3) | `b-similarweb-ai-ads-2026-09-22` (5) | 3/5/5 | 5 | no |
| r1 | white:17 no protocol fee | `c-agentic-commerce-protocols-table-2026-09-22` (3) | same; Instant Checkout "small fee" beside (3) | —/3/3 | 3 | no |
| both | unk:68 C1 hypothesis tallies | `b-sec-hubspot-10k-2026-02-11-2026-09-23` (2) | H3, H6 case raws (5) | 5/5/5 | 5 | no |
| both | unk:69 C2 unscorable rows | day-0 panel raws (1) | same (1) | 1/1/1 | 1 | no |
| both | unk:70 C3 channels blocked | pull logs; `method/blocked-channels.md` (1) | same (1) | 1/1/1 | 1 | no |
| both | unk:71 C4 done rows | findings files only | — | 3/n/a/n/a | n/a | no |
| both | unk:72 C5 17 of 25 | findings files only | — | 1/n/a/n/a | n/a | no |

Moved: 0 of 12 sub-tier claims (review-1), 0 of 11 (Pass 9); 0 of 12 at ≤3 moved down. Content drift without tier change: demand C1, C2, C4, C5 counts stale after GAP-SK; white C5 contradicted by a tier-5 row (`raw/e-case-otterly-llms-txt-experiment-repull2-2026-09-23.md`: "81 ChatGPT-User" of 84 llms.txt hits); white:17 beside `raw/b-openai-buy-it-in-chatgpt-instant-checkout-primary-2026-09-23.md` "Merchants pay a small fee on completed purchases", rate undisclosed.

### Do the two lists still carry the findings' load?

No. `executive-brief-2026-09-23-r2.md` metric spine has 27 rows; 12 touch a list claim (rows 1, 8, 12, 14, 15, 18, 19, 21, 23, 24, 26, 27), 15 cite only files written 2026-09-23 (`ai-ads-evidence.md`, `market-potential.md`, `transition-evidence.md`, `frontier-scan.md`, P16 appends). Third list counted below.

### Third list — r2 brief metric spine, 27 rows

Brief = the tier the row's "Label, tier" cell states. E = Lane E case corpus (P9-r membership rule). M = meta-claim.

| # | row | best raw now (tier) | weakest row now (tier) | brief | now | ≤3 | E/M |
|---|---|---|---|---|---|---|---|
| 1 | Market size, measured | `e-market-size-emarketer-aiads-primary-2026-09-23` (4) | `e-market-size-table-2026-09-22` (6) | 6 | 6 | no | |
| 2 | Organic floor, two bases | `b-semrush-10k-2025-geo-demand-2026-09-23` (2) | `a-peec-funding-techcrunch-2025-11-2026-09-22` (5) | 2 / 5 | 5 | no | |
| 3 | Paid floor; agentic floor | `b-alphabet-10k-2025-search-revenue-2026-09-23` (2) | `b-openai-1bn-run-rate-milestone-2026-09-22` (3) | 3; 2 | 3 | yes | |
| 4 | Forecasts, never sizes | emarketer primaries 2026-09-23 (4) | forecast rows, `e-market-size-*` (6) | 5–6 | 6 | no | |
| 5 | Engine reach | `b-sec-spacex-s1a-2026-06-03-2026-09-23` (2) | `e-openai-chatgpt-user-counts-2026-09-23` (3) | 3; 2 | 3 | yes | |
| 6 | Ad baselines, filed | `b-alphabet-10k-2025-search-revenue-2026-09-23` (2) | `e-iab-pwc-internet-ad-revenue-fy2025-2026-09-23` (4) | 2 (IAB 4) | 4 | no | |
| 7 | Paid inventory per engine | `b-openai-help-ads-in-chatgpt-2026-09-23` (3) | `b-campaign-perplexity-ads-end-2026-09-23` (5) | 3 (5) | 5 | no | |
| 8 | Prices published | `b-openai-help-ads-basics-2026-09-23` (3) | `b-ppcland-openai-ads-manager-cpc-2026-09-23`, "$60" (5) | 3 (5) | 5 | no | |
| 9 | ChatGPT ad presence, advertisers | `b-openai-1bn-run-rate-milestone-2026-09-22` (3) | `b-similarweb-chatgpt-ad-stats-2026-09-23` (5) | 5 | 5 | no | |
| 10 | Publisher side | `b-sec-reddit-10q-q2-2026-content-licensing-2026-09-23` (2) | `c-cloudflare-pay-per-crawl-docs-2026-09-23` (3) | 3; 2 | 3 | yes | |
| 11 | Regulation in force | `b-regulators-ad-disclosure-table-2026-09-22` (2) | `b-compliance-vendor-dsa-ai-act-check-2026-09-23` (3) | 2 | 3 | yes | |
| 12 | Supply | `b-semrush-10k-2025-geo-demand-2026-09-23` (2) | `a-bloomberg-scrunch-sitecore-primary-2026-09-23`, "$225 Million" (5) | 3–5; 2 | 5 | no | |
| 13 | Measurement, tooling | `a-openai-help-measurement-partners-2026-09-23` (3) | same (3) | 3 | 3 | yes | |
| 14 | Demand, 27 cells | S1 raws (3) | `f-signal-sk-S4-omr-reviews-2026-09-22` (5); figure stale | 3–5 | 5 | no | |
| 15 | Where demand sits | `f-signal-sk-S1-hydrafacial-workday-geo-aeo-2026-09-23` (3) | S1 raws (3); counts stale | 3 | 3 | yes | |
| 16 | Local 9; EU 45; S13 | `f-edgar-fts-local-multilocation-S7-2026-09-23` (2) | `f-reddit-localseo-smallbusiness-franchise-S5-2026-09-23` (5) | 2–5 | 5 | no | |
| 17 | Engine × segment; bodies | `f-engine-mentions-raw-count-2026-09-23` (1) | `f-indeed-S1-repull3-2026-09-23` (3) | 1; 3 | 3 | yes | |
| 18 | WTP; budget line | `f-signal-sk-S7-coty-8k-q4-fy2026-2026-09-23` (2) | `f-signal-*-S11-price-paid-2026-09-22` (3, per review-1) | — | 3 | yes | |
| 19 | Proof: Gold; Silver | NerdWallet 8-K (2) | case raws (5) | 5 | 5 | no | E |
| 20 | Three-counts | `e-case-edgar-fulltext-results-2026-09-23` (2) | `e-case-*` vendor pages (5) | 1 | 5 | no | E |
| 21 | Negative tail vs positives | `e-case-iac-investor-deck-repull2-2026-09-23` (2) | seven positive Silvers (5) | 2; 5 | 5 | no | E |
| 22 | What movers changed | `b-sec-hubspot-10k-2026-02-11-2026-09-23` (2) | transition raws (6) | 2–6 | 6 | no | |
| 23 | Lane D | `d-paper-bias-beware-cognitive-bias-2026-09-23` (3) | `d-paper-ecogeo-evidence-ecosystem-2026-09-23` (5) | 3–5 | 5 | no | |
| 24 | Hypotheses, 32 | `b-sec-hubspot-10k-2026-02-11-2026-09-23` (2) | `e-market-size-table-2026-09-22` (6) | 1–6 | 6 | no | E |
| 25 | Risks | `b-regulators-ad-disclosure-table-2026-09-22` (2) | `e-market-size-table-2026-09-22`, risk 11 (6) | 2–6 | 6 | no | |
| 26 | Done rows | findings files only | — | — | n/a | no | M |
| 27 | Channels | `method/blocked-channels.md`; pull logs (1) | same (1) | 1 | 1 | yes | |

Moved against the brief's own label: 0 up; rows 11 (2 → 3) and 20 (1 → 5) read lower under weakest-row. Row 20's counts are ours; the rows counted are vendor pages.

### Recount — nine figures, prior six beside

| list | split | prior (P9-r) | RECOUNT-2 |
|---|---|---|---|
| Pass 9 (25) | all | 11/25 = 44.0% (68.0% on 2026-09-22 tiers) | 11/25 = 44.0% |
| Pass 9 (25) | excl. Lane E (7) | 11/18 = 61.1% | 11/18 = 61.1% |
| Pass 9 (25) | excl. meta (3) | 11/22 = 50.0% | 11/22 = 50.0% |
| review-1 (27) | all | 12/27 = 44.4% | 12/27 = 44.4% |
| review-1 (27) | excl. Lane E (8) | 12/19 = 63.2% | 12/19 = 63.2% |
| review-1 (27) | excl. meta (3) | 12/24 = 50.0% | 12/24 = 50.0% |
| r2 spine (27) | all | — | 9/27 = 33.3% |
| r2 spine (27) | excl. Lane E (rows 19, 20, 21, 24) | — | 9/23 = 39.1% |
| r2 spine (27) | excl. meta (row 26) | — | 9/26 = 34.6% |

Bar 80%: met by none of the nine. At ≤3 on the spine: rows 3, 5, 10, 11, 13, 15, 17, 18, 27.

### Segment matrix — three cuts, strict and loose

| cut | reading | spend / attention / none / blank | closed | prior beside |
|---|---|---|---|---|
| core 27 | strict | 9 / 1 / 17 / 0 | 27 of 27 | 8/1/17/1, 26 of 27 (R-BLOCKED-2); 19 of 27 (P8-r); 8 of 27 (review-1) |
| core 27 | loose | 9 / 1 / 17 / 0 | 27 of 27 | 8/1/18/0 (P8-r, R-BLOCKED-2); 7/1/11/8 (Pass 9) |
| local 9 | as file states | 1 / 3 / 5 / 0 | 9 of 9, strict = loose | P16-c4, same |
| local 9 | strict, S9 unrun | 1 / 3 / 0 / 5 | 4 of 9 | not stated before |
| EU 45 | demand-map | 2 / 0 / 41, 2 cells unassigned | 43 of 45 | P16-c3b, same; P16-c3 organic only, 15 of 45 |
| EU 45 | customers files | 2 / 0 / 43; 4 unassigned beside | 45 of 45 | not stated before |
| EU 45 | strict, cut's four signals | 2 / 0 / 28–29; 14 S5 failed or void | 30–31 of 45 | not stated before |
| EU 45 | strict, full catalogue | 2 / 0 / 0 | 2 of 45 | not stated before |

Core 27 verified from `customers/`: skincare 4/1/4/0 (E2 spend per GAP-SK; file header still reads "spend 3, attention 1, none 5"), B2B SaaS 3/0/6/0, high-CPA 2/0/7/0. Local S9: "S9 unrun" in paid and agentic cells (`customers/local-multi-location.md` signals table; Trends token gate). EU S5: 9 paid/agentic cells "(S5 failed)", 422 ×2; UK and FR organic S5 from aggregate calls whose "0 is not evidence of absence" (`raw/f-reddit-arcticshift-S5-eu-national-subs-2026-09-23.md`) — 5 cells (customers basis), 4 (demand-map basis). EU cut ran S1, S2, S5, S10 (S13 organic) only. EU unassigned: demand-map counts ES × B2B SaaS and UK × high-CPA organic as unassigned cells; customers files read both `none — checked`, Make and Compare the Market beside. Both stand.

### Hypotheses — scored-of-32

Scored 26 of 32, unchanged. Not produced: HE2, HE3, HP1, HP2, HP3, HP4 (Pass 10 skipped by owner 2026-09-23). Marks since the P9-r register: H9 strict → confirmed (R-BLOCKED-2, already in COMPILE-2 last row); H7 strict → confirmed (`demand-map.md` §GAP-SK, "strict now also confirmed"; not yet in `hypotheses.md` log). Marks now: confirmed 13 + 1 dual (H6) · killed 7 · unresolved — checked 5 + 1 dual · not produced 6. P9-r tallies 11 + 3 dual / 7 / 5 + 3 dual / 6 beside.

Checked, no mark moved: RP2-A (IAC slide 7 "50%" reconciled, tier 2 unchanged; Otterly ×3 grades unchanged — H3, H6; Ulta IR primaries no metric — H11); RP2-B (Adobe Q3 open — H1; Adthena walls — H20); GAP-IND (0 cells; no SMB spend — H4; GEO/AEO duties outside verticals — H10 unchanged); REPULL-1b (Instant Checkout "small fee" — H12; Edgar Dunn primary — H22 rests on organic 1.92×); P16-c1…c4b (H4, H7, H9 "consistent" per local file; H17 no AI-surface ad line in any filer).

### Caveats, this append

- Weakest-row rule follows each findings file's "Tier of weakest row" column and P9-r; a best-row rule would lift proof C4 (Ulta "paid_by_outcome: no"), white C8 and spine rows 2, 6–9, 12, 14 to ≤3. Not applied; stated for diffing.
- Spine tiers are this append's assignment from the brief's cited compiled files and their raws; row 18's "—" is read as 3 per review-1's demand C3. Lane E membership on the spine follows P9-r (case-corpus rows plus the hypothesis tally); row 22 is Lane F, kept in.
- `raw/` count is a directory listing on 2026-09-23; files landed by agents after this read are not counted. Strict EU and local reads are this append's arithmetic on the none rule (`method/plan.md` "Demand signals — none rule"), not a compiler's read; the compilers' reads stand beside.
- H7's GAP-SK mark is copied from `demand-map.md`, not re-scored. This file was over its 100-line budget before this append; overrun stated here. Evidence, not a verdict.
