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
