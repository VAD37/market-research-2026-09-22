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

Sixteen of 23 hypotheses are scorable: **6 confirmed, 6 killed, 4 unresolved — checked**. Seven take `not produced` — six panel rows held by user decision 2026-09-22, plus H10, whose producing pass has not run. Two of six programme-done rows hold.

## Evidence

### Hypotheses register — every row marked, with the deciding evidence and its tier

| ID | Mark | Deciding evidence | Path | Tier |
|---|---|---|---|---|
| H1 — AI referral converts above organic search | unresolved — checked Adobe, Salesforce, Shopify 2026-09-22 | Adobe at the tier-4 floor compares AI to **non-AI** visits ("Conversion Now 42% Higher"), not to organic search; the organic-search comparator exists only at tier 5 (Shopify, "nearly 50% higher rates than organic search"); no publisher breaks out per engine | `markets/agentic-commerce.md` → `raw/c-retail-analytics-table-2026-09-22.md` | 4 |
| H2 — paid inventory exists at scale | **confirmed** | Self-serve Ads Manager beta live on a P1 engine from 2026-02-09, plus Google AI Overviews/AI Mode auto-eligible | `markets/paid-placement.md` → `raw/b-openai-platform-summary-2026-09-22.md` | 3 |
| H3 — at least one vendor demonstrates causal lift | **killed** | Zero Gold after the Pass 4 screen: ~980 candidates, 0 holdout / geo-split / switchback | `findings/proof-scorecard.md` → `raw/e-case-census-c13-2026-09-22.md` | 5 |
| H4 — demand is attention-only in every SMB cell | **killed** | B2B SaaS organic × SMB reads spend on a tier-3 employer posting; source census read the floor the other way, both stand | `findings/demand-map.md` → `raw/f-signal-bs-S1-linkedin-jobs-guest-api-2026-09-22.md` | 3 |
| H5 — corpus seeding measurably moves an answer | **killed** | "0 in this cluster's 12 pulls" have a true before-and-after design; no Pass 5 technique has a published single-action before-and-after on a production surface | `raw/d-technique-census-c1-`…`-c7-2026-09-22.md` | 4 |
| H6 — a brand action precedes a measured visibility change on a P1 engine | **confirmed** | Sitefire/Pointhound: content live 2026-03-14 inside an absolute window 2026-02-23 to 2026-06-29, ChatGPT and Claude named, Visibility Score 0 → 1.0%, untouched-page control | `findings/proof-scorecard.md` → `raw/e-case-sitefire-pointhound-2026-09-22.md` | 5 |
| H7 — organic carries spend in more cells than paid or agentic | unresolved — checked (channel list in `demand-map.md`) 2026-09-22 | Organic 5 spend cells against 1 each; both conditions require all 27 cells checked and 8 read blank | `findings/demand-map.md` | 3 |
| H8 — a protocol is published fully enough to implement without a contract | **confirmed** | ACP, UCP and x402 all Apache-2.0 with no gate to read the spec | `markets/agentic-commerce.md` → `raw/c-agentic-commerce-protocols-table-2026-09-22.md` | 3 |
| H9 — agentic spend in enterprise, absent from SMB | unresolved — checked (same list) 2026-09-22 | One agentic enterprise cell spends, no agentic SMB cell does, 2 of the 6 read blank | `findings/demand-map.md` | 3 |
| H10 — org / content-ops changes named more often than paid-media changes | **not produced** | Producing pass 11 has not run; its gate reads "9, and 10 or its recorded hold". Pass 4 case material is the pointer, not the score | `method/plan.md` §Pass 10 and 11 hold note | — |
| H11 — tier-3 transition evidence in each vertical | **killed** | High-CPA regulated has zero: Sitefire/Jerry tier 5, Conductor/Zurich UK tier 6, NerdWallet tier 2 but names no brand action. Channels recorded in that file | `customers/high-cpa-regulated.md` → `raw/e-case-census-c10-2026-09-22.md` | 2 |
| H12 — where paid inventory exists its price is disclosed publicly | unresolved — checked openai.com, support.google.com/google-ads, about.ads.microsoft.com, advertising.amazon.com 2026-09-22 | Confirm needs a rate card or pricing page: 0 of 8. Kill needs no price at all at tier 3: OpenAI states "$3–$5 USD per click" recommended max bid. Neither condition is met | `markets/paid-placement.md` | 3 |
| H13 — a P1 engine publishes a countermeasure naming a Pass-5 technique | **confirmed** | 6 of 36 engine × technique cells read `named` — Anthropic on fake reviews, Google disclaiming llms.txt, four engines on prompt injection | `raw/d-technique-census-c7-2026-09-22.md` | 3 |
| H14 — manipulation evidence denser in regulated than in the anchor | **killed** | Regulated 0 filed specimens and 0 tested specimens; anchor 0 — the anchor equals it, which is the kill condition | `customers/high-cpa-regulated.md` → `raw/d-technique-census-c2-`, `-c3-2026-09-22.md` | 4 |
| H15 — vendors publishing a composite disclose its prompt set | **killed** | 0 of 34 rostered vendors disclose a fixed published prompt set with n | `markets/organic-recommendation.md` → `raw/a-vendor-census-c1-`…`-c4-2026-09-22.md` | 3 |
| H16 — every published sub-market size is a forecast | **confirmed** | 15 of 18 figures author-labelled forecasts; the 3 measured ones carry no forward target year and none is a sub-market size | `findings/whitespace.md` → `raw/e-market-size-table-2026-09-22.md` | 3 |
| HE1 — ChatGPT paid product live and documented on its own surface | **confirmed** | Ads doc, formats, label wording and bid guidance on OpenAI's own pages | `markets/paid-placement.md` → `raw/b-openai-platform-summary-2026-09-22.md` | 3 |
| HE2 — Claude returns brand-level recommendations to buying-shaped prompts | **not produced** | Day 0: 83 of 160 runs, logged-in, Memory localising every answer to Vietnam; `region_intended: US` failed for every run. Sampling held 2026-09-22 22:40 | `raw/e-claude-panel-2026-09-22.md` | 1 (unusable for this row) |
| HE3 — ad-labelled formats render inside Google AI surfaces for the prompt set | **not produced** | Day 0 retry: 76 of 160 AI Mode runs, 0 ad units; AI Overviews 0 of 14 rendered; logged-out, IP-localised to Vietnam, text-extraction-scoped. Panel held | `raw/e-google-aimode-panel-2026-09-22-retry.md` | 1 (one date, not the protocol's n) |
| HP1 — between-engine gap exceeds within-engine spread | **not produced** | Needs two P1 engines on one date and surface; ChatGPT 0 runs, Gemini 24 of 160 on Flash-Lite with a silent throttle | `raw/e-gemini-panel-2026-09-22.md`, `raw/e-chatgpt-panel-2026-09-22.md` | 1 |
| HP2 — recommended brand set unstable between dates | **not produced** | Needs two sampling dates ≥14 days apart; only day 0 exists and the gap is recorded, never back-filled | `method/STATE.md` §Pass 10 sampling log | — |
| HP3 — citation-to-mention ratio below 0.50 | **not produced** | Codable only from a neutral day 0; the one usable engine-day is `personalised — logged-in, Memory on` | `raw/e-claude-panel-2026-09-22.md` | 1 |
| HP4 — citation rate higher with web search on than off | **not produced** | Needs a toggle both engines expose; Gemini logged-out exposes none | `raw/e-gemini-panel-2026-09-22.md` | 1 |

Marks: **confirmed 6** (H2, H6, H8, H13, H16, HE1) · **killed 6** (H3, H4, H5, H11, H14, H15) · **unresolved — checked 4** (H1, H7, H9, H12) · **not produced 7** (H10, HE2, HE3, HP1–HP4).

### Programme done — every row, with the arithmetic where there is one

| Condition | Bar | Status | Owned by |
|---|---|---|---|
| Load-bearing claims in `findings/` at tier 3 or better | 80 percent or more | **not met — 17 of 25 = 68.0%.** By file: `proof-scorecard.md` 1 of 6, `demand-map.md` 6 of 6, `whitespace.md` 6 of 8, this file 4 of 5. Across all 27 claims including the 2 non-load-bearing: 18 of 27 = 66.7% | this file |
| Priority-1 engine × sub-market cells | every cell a number or an explicit `unknown — checked` | **met — 9 of 9** | `whitespace.md` |
| Segment matrix | every cell spend, attention or none, with signals | **not met — 19 of 27**; 8 high-CPA cells read `blank` | `demand-map.md` |
| Success stories | one Silver per vertical, or documented absence with screened count | **met** — B2B SaaS and high-CPA on the Silver arm, skincare on the documented-absence arm (0 Silver at ~133 screened) | `proof-scorecard.md` |
| Hypotheses | every H confirmed, killed or unresolved with the channel checked | **not met — 16 of 23**; 7 take `not produced`, which the scoring rule defines as distinct from unresolved | this file |
| Pass 10 | three pre-registered predictions checked against the panel | **not met — 0 of 3.** Six rows are panel-checkable against a bar of three; sampling held by user decision 2026-09-22 22:40, day 0 recorded per engine as sampled, partial or blocked | this file |

The tier-3 shortfall is concentrated: every load-bearing claim below tier 3 is a Lane E case claim, and published case studies are structurally vendor-reported at tier 5 (`method/trust-rubric.md`).

## Claims

| # | Claim | Evidence | Tier of weakest row | Grade | Load-bearing |
|---|---|---|---|---|---|
| C1 | 23 hypotheses score 6 confirmed, 6 killed, 4 unresolved — checked, 7 not produced | register above | 5 | n/a | yes |
| C2 | Seven rows cannot be scored at all: six because Pass 10 sampling is held, one because Pass 11 has not run | HE2, HE3, HP1–HP4, H10 | 1 | n/a | yes |
| C3 | Seven named channels are blocked this session rather than exhausted, and carry most of the open unknowns | blocked-channel table below | 1 | n/a | yes |
| C4 | Two of six programme-done rows hold | done table above | 3 | n/a | yes |
| C5 | 17 of 25 load-bearing claims across the four findings files sit at tier 3 or better — 68.0% against a bar of 80% | done table above | 1 | n/a | yes |

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

- C1 is load-bearing and sits at tier 5: its weakest deciding rows are H3's and H6's vendor-reported case corpus. C2, C3 and C5 rest on measured-by-us records of this session's own pulls and files (tier 1); C4 on the four findings files.
- Every `killed` mark resting on absence — H3, H5, H14, H15 — is only as strong as the channels listed beside it (`method/hypotheses.md` caveats); an absence with no channel list is not a kill, and each of the four carries one. H4's kill and H7's and H9's `unresolved` all inherit `demand-signals.md`'s biases, and H4 turns on a tier-floor reading the source censuses applied the other way. Both readings are in `demand-map.md`, side by side.
- `not produced` is not `unresolved`: seven rows are unscored because their producing pass did not run, and no channel exhaustion is claimed for any of them. H14's "equal screen effort" is not measurable to a fine grain; both verticals returned zero specimens, so the comparison is stated rather than assumed. The tier-3 share of 68.0% is computed over the 25 load-bearing claims in the four files written 2026-09-22; adding or retiring a claim moves it.
- The oldest pull cited is 2026-09-22; no cited pull is stale under `method/plan.md`. This file carries evidence, not a verdict.
