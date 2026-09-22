# STATE — scheduler state

Created 2026-09-22. The only interface between sessions and between agents. Updated by the main thread after every spawn, landing, and commit. Agents append only under "Landed — pending verify".

## Current pass

Pass 4 done 2026-09-22 (13 clusters). Pass 5: c7, c3, c4, c5, c6 live; c1, c2 landed. Pass 6 compile open (P6-c0 landed): organic and paid live, agentic queued. Pass 7 open (gate 3+4): seven rows queued. Pass 8: three raw sweeps live, compiles queued. Pass 9 blocked by 5, 6, 7, 8. Pass 10 held by user; Pass 11 blocked.

## Live agents

Cap 10 from 2026-09-22 22:30 (user). Browser: one extension holder (`ext`) and one Playwright holder (`pw`) at a time; the rest fetch only.

| id | model | task | deliverable | spawned |
|---|---|---|---|---|
| P5-c3 | Sonnet | Comparison-page farming | `docs/raw/d-comparison-*`, `d-technique-census-c3-2026-09-22.md` | 2026-09-22 |
| P5-c7 | Sonnet | Engine countermeasures, priority-1 and priority-2 engines | `docs/raw/d-countermeasure-*`, `d-technique-census-c7-2026-09-22.md` | 2026-09-22 |
| P8-c1-hr | Sonnet | Demand-signal sweep, high-CPA regulated, nine cells | `docs/raw/f-signal-hr-*`, `f-signal-census-hr-2026-09-22.md` | 2026-09-22 |
| P6-paid | Opus | Compile `markets/paid-placement.md` | `docs/markets/paid-placement.md` | 2026-09-22 |
| P8-c1-sk | Sonnet | Demand-signal sweep, skincare and beauty, nine cells | `docs/raw/f-signal-sk-*`, `f-signal-census-sk-2026-09-22.md` | 2026-09-22 |
| P6-organic | Opus | Compile `markets/organic-recommendation.md` | `docs/markets/organic-recommendation.md` | 2026-09-22 |
| P5-c4 | Sonnet | Content written to satisfy known citation preferences | `docs/raw/d-citationpref-*`, `d-technique-census-c4-2026-09-22.md` | 2026-09-22 |
| P5-c5 | Sonnet | Structured data and llms.txt-style signalling | `docs/raw/d-structured-*`, `d-technique-census-c5-2026-09-22.md` | 2026-09-22 |
| P5-c6 | Sonnet | Prompt injection embedded in indexed content | `docs/raw/d-injection-*`, `d-technique-census-c6-2026-09-22.md` | 2026-09-22 |
| P8-c1-bs | Sonnet | Demand-signal sweep, B2B SaaS, nine cells | `docs/raw/f-signal-bs-*`, `f-signal-census-bs-2026-09-22.md` | 2026-09-22 |

## Queue

Front first. Order per `plan-review-1-2026-09-22.md` §1 (2026-09-22 22:40 user priority). Spawn on completion only. Filenames carry the cluster id. Rows marked `10 held` stay held until the user reopens Pass 10.

| id | pass | model | task | deliverable |
|---|---|---|---|---|
| P6-agentic | 6 | Opus | Compile `markets/agentic-commerce.md` | `docs/markets/agentic-commerce.md` |
| P8-skincare, P8-b2b-saas, P8-high-cpa | 8 | Opus | Compile one customers/ file per vertical as each sweep lands | `docs/customers/<vertical>.md` |
| P7-INDEX, P7-organic-a, P7-organic-b, P7-incumbent-a, P7-incumbent-b, P7-agency, P7-sellside | 7 | Opus | Pre-staged; spawn when Pass 4 lands | `docs/competitors/` |
| P3-repull-sec | 3 | Sonnet | Probe-gated: one EDGAR fetch first; 403 → record blocked and stop. Re-pull CHGA, LCFY, HUBS, YEXT filings | `docs/raw/a-<co>-filing-sec-<date>.md` |
| P10-d0-copilot, P10-d0-rufus-p3, P10-d0-google-aimode-remainder (7 P + 9 X prompts), P10-d0-gemini-remainder, P10-d0-claude-remainder, P10-d0-chatgpt-retry | 10 held | Sonnet | Held by user decision 2026-09-22 22:40; gap rows, never back-filled | per panel-protocol.md |
| P9, P10-analysis, P11 | 9–11 | Opus | Blocked | per plan.md |

## Landed

| task | deliverable | verified | commit |
|---|---|---|---|
| P0-a glossary and templates | `docs/method/glossary.md`, `docs/method/templates/` (7 files) | 2026-09-22 | 5d2950d |
| P0-b hypotheses and demand signals | `docs/method/hypotheses.md`, `docs/method/demand-signals.md` | 2026-09-22 | 7cfc7b9 |
| P0-c panel protocol | `docs/method/panel-protocol.md` | 2026-09-22 | f5a06cd |
| **Pass 0 done** | all five Pass 0 deliverables | 2026-09-22 | f5a06cd |
| P10-d0-chatgpt | `docs/raw/e-chatgpt-panel-2026-09-22.md` — surface blocked, 0 of 160 runs | 2026-09-22 | 58e469b |
| P1-a channels, shortlist, query book | `docs/sources/channels.md` (145), `shortlist.md` (78), `query-book.md` (118); 29 clusters | 2026-09-22 | 9aca6b4 |
| P1-b red-team | `docs/sources/query-book-redteam.md` (120); 13 blind spots, verdict amend all three | 2026-09-22 | 34994b8 |
| P1-c amendments applied | `channels.md` (157), `shortlist.md` (101), `query-book.md` (151); 22 of 22 applied, 32 clusters | 2026-09-22 | f78663a |
| **Pass 1 done** | channels, shortlist, query book, red-team | 2026-09-22 | f78663a |
| P2-c1 assistant share | 11 pulls `docs/raw/a-*-share-*-2026-09-22.md` + `a-assistant-share-table-2026-09-22.md` + `a-statcounter-methodology-2026-09-22.md`; 29 screened out; Rufus unknown | 2026-09-22 | 4d05c71, f6a8b5c |
| P2-c2 crawler telemetry | 11 pulls `docs/raw/a-*-crawler-*`, `a-cloudflare-*` + `a-crawler-telemetry-table-2026-09-22.md`; 6 engines' crawler docs + Apple | 2026-09-22 | 892b119 |
| P2-reweight | `docs/method/plan.md` §Engine matrix — reweight 1 (35 lines appended); Perplexity 2→3, Grok 3→2 | 2026-09-22 | 45f8721 |
| P2-c3 OpenAI platform | 20 pulls `docs/raw/{a,b,c}-openai-*` + `b-openai-platform-summary-2026-09-22.md`; ChatGPT Ads exist per OpenAI pages, no rate card, CPC guidance stated | 2026-09-22 | 0f3846b |
| P2-c5 Anthropic + Perplexity | 13 pulls `docs/raw/*anthropic*`, `*perplexity*` + `b-anthropic-perplexity-platform-summary-2026-09-22.md`; Claude no-ads policy dated 2026-02-04; Perplexity ad status by absence | 2026-09-22 | 92e5992 |
| P2-c6 Microsoft + Amazon | 16 pulls `docs/raw/*microsoft*`, `*amazon*` + `b-microsoft-amazon-platform-summary-2026-09-22.md`; Copilot ads via Bing auction, Copilot Checkout 0% commission; Amazon sponsored prompts CPC, Rufus renamed Alexa for Shopping 2026-05-13 | 2026-09-22 | 113f074 |
| P2-c7 protocols | 10 pulls `docs/raw/c-*-protocol-*` + `c-agentic-commerce-protocols-table-2026-09-22.md`; ACP, AP2 (to FIDO 2026-04-28), UCP, x402, Visa TAP readable; Mastercard Agent Pay gated | 2026-09-22 | a6a41b0 |
| P2-c8 retail analytics | 16 pulls `docs/raw/c-{adobe,salesforce,shopify}-analytics-*` + `c-retail-analytics-table-2026-09-22.md`; no per-engine breakout by any publisher; influenced-revenue figures flagged modelled | 2026-09-22 | 07a5740 |
| P10-d0-claude | `docs/raw/e-claude-panel-2026-09-22.md` (1739 lines) — 83 of 160 runs: all C prompts n=5, 3 toggle arms, 2 P prompts; model shown "Fable 5.1"; logged-in, Memory personalises to Vietnam (confound recorded) | 2026-09-22 | ce405f8 |
| P2-c9 regulators | 7 pulls `docs/raw/b-{eu,us,uk}-regulator-*` + `b-regulators-ad-disclosure-table-2026-09-22.md`; EU AI Act Art. 50 in force 2026-08-02, DSA Art. 26/27, 16 CFR 255, CMA SMS names AI Overviews/AI Mode | 2026-09-22 | 311f71d |
| P2-c10 EU DSA | 18 pulls `docs/raw/b-eu-*` + `b-eu-dsa-ad-repositories-table-2026-09-22.md`; ChatGPT designated VLOSE 2026-08-31; no repository distinguishes ads inside AI answers | 2026-09-22 | aa7530c |
| P2-c2 addendum | `docs/raw/a-crawler-telemetry-table-2026-09-22.md` (missed by commit glob) | 2026-09-22 | 4494fb8 |
| P3-c0 vendor roster | `docs/raw/a-vendor-roster-2026-09-22.md` (278 lines); 121 screened, 70 held, 26 rostered: 13 organic, 12 incumbent bundling, 1 agency; sell-side thin | 2026-09-22 | 3ff2d70 |
| P2-c11 partial | 7 docket files `docs/raw/b-court-*` (agent rate-limited before summary; resumed) | 2026-09-22 | 9c8ae92 |
| P2-c11 dockets | 9 dockets `docs/raw/b-court-*` + `b-court-dockets-table-2026-09-22.md`; OpenAI, Microsoft, Google ×2, Perplexity, Anthropic vs publishers/platforms; 4 candidates not opened (WAF) | 2026-09-22 | 60bd861 |
| **Pass 2 done** | 11 clusters, ~150 raw pulls, reweight 1 | 2026-09-22 | 60bd861 |
| P10-d0-gemini | `docs/raw/e-gemini-panel-2026-09-22.md` (1128 lines) — 24 of 160 runs, logged-out, model shown "Flash-Lite", toggle not exposed, surface silently throttled mid-session | 2026-09-22 | 28fffc5 |
| P10-d0-google-aimode | `docs/raw/e-google-aimode-panel-2026-09-22.md` — surface blocked, 0 runs: google.com/search reCAPTCHA on Playwright IP 159.26.119.97 | 2026-09-22 | 66e3d42 |
| P10-d0-perplexity | `docs/raw/e-perplexity-panel-2026-09-22.md` — surface blocked, 0 runs: Cloudflare challenge on Playwright, two Ray IDs | 2026-09-22 | 132ee18 |
| P3-c1 organic vendors 1–8 | 44 pulls + `docs/raw/a-vendor-census-c1-2026-09-22.md`; 50 cases screened, 0 Gold/Silver, 19 Bronze, 14 Fools gold; no vendor discloses prompt set behind a composite; Profound $180M Series D 2026-09-15 | 2026-09-22 | a9d467d |
| P3-c2 organic vendors 9–13 + Scrunch | 34 pulls + `docs/raw/a-vendor-census-c2-2026-09-22.md`; 48 cases screened, 0 Gold/Silver, 13 Bronze; 0 of 6 disclose prompt set; sec.gov blocked, CHGA/LCFY filings via tier-5 substitute | 2026-09-22 | 47475f3 |
| P3-c3 incumbents 1–6 | 29 pulls + `docs/raw/a-vendor-census-c3-2026-09-22.md`; no incumbent discloses a public price delta; 0 Gold/Silver, best Bronze; SEC filings via IR-site copies (tier 3) | 2026-09-22 | 5791e3e |
| P3-c5 agencies | 23 pulls + `docs/raw/f-agency-census-c5-2026-09-22.md`; 5 rostered (Pace Generative, Orange142, Intero Digital, Seer Interactive, Fire&Spark), 7 held; 1 public rate card; best grade Bronze | 2026-09-22 | 493064a |
| P3-c4 incumbents 7–12 + held | 33 pulls + `docs/raw/a-vendor-census-c4-2026-09-22.md`; Semrush delta +$60/mo; Adobe acquired Semrush 2026-04-28 (SEC 8-K); first Silver case (Quattr / Men's Wearhouse); SOCi, SE Ranking, Uberall, Onclusive cleared | 2026-09-22 | 2c53a4f |
| P3-c6 sell-side | 18 pulls + `docs/raw/c-vendor-census-c6-2026-09-22.md`; 7 rostered (Feedonomics, Shopware, Wix, Criteo, StackAdapt, Pacvue, Kargo); Shopware only public rate card; no case clears the bar | 2026-09-22 | 6421f11 |
| **Pass 3 done** | roster + 6 clusters, ~190 raw pulls; 1 Silver case total, rest Bronze or below | 2026-09-22 | 6421f11 |
| REVIEW-1 plan review | `docs/method/plan-review-1-2026-09-22.md` (109 lines); Pass 4 second sweep c7–c13, grading rule 1, panel hold, gates 6 and 8 open, 6 plan.md appends | 2026-09-22 | d876d32 |
| P4-c1 earnings and filings | 10 hits `docs/raw/e-case-{chegg,criteo,everquote,iac,lendingtree,nerdwallet,reddit,techtarget,yelp}-*` + `e-case-census-c1-2026-09-22.md`; 64 screened; 1 Silver (NerdWallet 2026-02-25, negative direction), 3 Bronze, 0 Gold; skincare and B2B SaaS 0 cleared | 2026-09-22 | a88bdd7 |
| P4-c4 vendor cases full-page | 12 cases `docs/raw/e-case-{athenahq,conductor,profound,quattr,rankprompt,rankscale,sitefire}-*` + `e-case-census-c4-2026-09-22.md`; 1 up (Sitefire/Pointhound → Silver), 0 down; Silvers: Quattr/Men's Wearhouse, Sitefire/Pointhound; 0 Gold; paid-by-outcome unknown ×12 | 2026-09-22 | 76f039e |
| P5-c1 corpus seeding | 12 items `docs/raw/d-seeding-*` + `d-technique-census-c1-2026-09-22.md`; tiers 3–5; 10 quantified effects, none a single-action before-and-after; 70 candidates screened; no engine names seeding as a policy category | 2026-09-22 | ac841d4 |
| P4-c2 agency data posts | 8 pulls `docs/raw/e-case-{foundation-inc,fractl,intero-digital,pace-generative,partnercentric,seer-interactive}-*` + `e-case-census-c2-2026-09-22.md`; 12 agencies checked; 1 Silver (Seer content recency, B2B SaaS), 3 Bronze, 2 Fools gold; no client null result found | 2026-09-22 | 90dbdc1 |
| P5-c2 review manufacture | 8 items `docs/raw/d-review-*` + `d-technique-census-c2-2026-09-22.md`; tiers 2–5; 3 measured rows, none a before-and-after; H5 unresolved — checked; 46 screened, vertical density thin; reddit.com blocked | 2026-09-22 | 7a9b617 |
| AMEND-1 review appends | plan.md +56, ORCHESTRATION.md +6, panel-protocol.md +6, shortlist.md +34 (42 clusters), hypotheses.md +1, run-prompt.md +6; insertions only | 2026-09-22 | 985e51e |
| P4-c6 trade press | 10 items resolved: 9 primaries `docs/raw/{a,b}-*` + 1 pointer + `e-case-census-c6-2026-09-22.md`; tier-2 unsealed exhibit ECF 1977-1 (Microsoft Bing/Copilot CTR drops 83–94%); 30 screened; Search Engine Land blocked | 2026-09-22 | 31c7c6c |
| P4-c5 practitioner write-ups | 10 pulls `docs/raw/e-case-practitioner-*`, `a-practitioner-*` + `e-case-census-c5-2026-09-22.md`; 1 Silver (Tiwari GSC 18 vs 32 control queries, observational), 24 screened, all `none named`; Reddit unreachable ×5 methods | 2026-09-22 | fd386d8 |
| P4-c7 brand-side corroboration | `docs/raw/e-case-census-c7-2026-09-22.md`; ~166 brands named, 59 checked on own domains, 0 corroborate, 0 contradict, 59 silent, ~107 not checked (cap); Men's Wearhouse silent on Quattr | 2026-09-22 | 70ab8c2 |
| P4-c3 conferences | 7 agendas `docs/raw/f-conference-*` + 2 talks + `e-case-census-c3-2026-09-22.md`; 9 events, brightonSEO 9 of 81 sessions match, GEO Conference series found; 6 talks screened, best Fools gold, all `none named`; MozCon file paraphrased (site copyright notice) — not verbatim | 2026-09-22 | f71fcb7 |
| P4-c8 skincare sweep | 9 pulls `docs/raw/e-case-c8-*` + `e-case-census-c8-2026-09-22.md`; ~133 screened, 15 opened; 2 Bronze (eMarketer index via BeautyMatter; 5W ranking via Glossy), 0 Silver; Estée Lauder × Profound partnership 2026-09-15 stated, no metric; Coty / Olaplex IR unreachable | 2026-09-22 | 5b72c20 |
| P4-c10 high-CPA sweep | 1 new pull `docs/raw/e-case-c10-sitefire-jerry-2026-09-22.md` (Bronze) + `e-case-census-c10-2026-09-22.md`; cards 16/1, insurance 12/2, supplements 6/0 screened/cleared; NerdWallet Silver cited; card issuers and supplement filers silent | 2026-09-22 | c11a23d |
| P10-d0-google-aimode-retry | `docs/raw/e-google-aimode-panel-2026-09-22-retry.md` (898 lines, supersedes blocked file) — AI Mode 76 of 160 runs (all 14 C prompts n=5), AI Overviews 14 checks with 0 blocks rendered, 0 ad units, model not displayed, logged-out, IP-localised to Vietnam (VND, Vietnamese UI) | 2026-09-22 | 17a875e |
| P4-c9 B2B SaaS sweep | 9 pulls `docs/raw/e-case-c9-*` + `e-case-census-c9-2026-09-22.md`; ~100 screened, 32 opened; 4 Bronze (G2 own post tier 3, HubSpot negative via OMR, Heyflow ×2), 3 Fools gold, 0 Silver; 10 SaaS filings opened, none on-topic | 2026-09-22 | 361b810 |
| P4-c11 negative results | 6 pulls `docs/raw/e-case-c11-*` + `e-case-census-c11-2026-09-22.md`; ~180 screened; 1 Silver null result (TW3 Partners/Citead arXiv 2609.07559: GEO levers move citation on none of 10 engine families, n=605–1,531, code+data); review sites skew 4.4–5.0, 1–2-star reviews rare and off-target; G2 DataDome CAPTCHA | 2026-09-22 | 64df380 |
| P4-c12 EU-brand sweep | 12 pulls `docs/raw/e-case-c12-*` + `e-case-census-c12-2026-09-22.md`; DE 116/10/4, EN 17/3/2, FR 4/3/0, ES 6/1/0, IT 8/0/0, NL 0 (screened/opened/graded); 4 Bronze (MiniFinder/Rankscale, sixclicks, rapidmail/Brevo, Spanish bank), 0 Silver; wuv.de paywalled | 2026-09-22 | 0030c7c |
| P4-c13 Pass 3 re-grade | 13 pulls `docs/raw/e-case-c13-*` + `e-case-census-c13-2026-09-22.md`; ~150 titles: 45 Bronze, 3 Silver, 0 Gold, 24 Fools gold, 34 no claim, 25 not opened; 12 up, 0 down; Sitefire/Jerry → Silver (conflicts with P4-c10's Bronze — both stand) | 2026-09-22 | 718b133 |
| **Pass 4 done** | 13 clusters; Silvers: Quattr/Men's Wearhouse, Sitefire/Pointhound, Sitefire/Jerry (vendor); Seer content-recency (agency); Tiwari GSC audit (practitioner); NerdWallet (filing, negative); TW3/Citead replication (null); 0 Gold; per vertical: skincare 0 Silver, B2B SaaS 1, high-CPA 1 (negative) | 2026-09-22 | 718b133 |
| P6-c0 published sizes | 16 pulls `docs/raw/e-market-size-*` + `e-market-size-table-2026-09-22.md`; 18 figures, 15 forecast-labelled, 3 measured (none a TAM), 6 with no base year; agentic forecasts diverge $5.7B–$15T; Gartner/GVR 403, no Forrester/IDC/Statista figure found | 2026-09-22 | 4b10b4c |
| P2-c4 Google platform | 13 pulls `docs/raw/{a,b,c}-google-*` + `b-google-platform-summary-2026-09-22.md`; Gemini app ad format unknown | 2026-09-22 | edd2725 |

## Landed — pending verify

Agents append one block here (or at end of file) on finish: deliverable path, pulls made (count), unknowns recorded (count), blockers. The main thread registers each block in Landed and deletes it.

## Pass 10 sampling log

| sample date | prompt-set version | engines | raw file |
|---|---|---|---|
| 2026-09-22 (day 0) | v1 | ChatGPT — blocked, 0 runs | `docs/raw/e-chatgpt-panel-2026-09-22.md` |
| 2026-09-22 (day 0) | v1 | Claude — 83 of 160 runs, logged-in researcher account, memory confound | `docs/raw/e-claude-panel-2026-09-22.md` |
| 2026-09-22 (day 0) | v1 | Gemini — 24 of 160 runs, logged-out, Flash-Lite, throttled | `docs/raw/e-gemini-panel-2026-09-22.md` |
| 2026-09-22 (day 0) | v1 | Google AI Mode + AI Overviews — blocked, 0 runs | `docs/raw/e-google-aimode-panel-2026-09-22.md` |
| 2026-09-22 (day 0) | v1 | Perplexity — blocked, 0 runs | `docs/raw/e-perplexity-panel-2026-09-22.md` |
| 2026-09-22 (day 0) | v1 | Google AI Mode — 76 runs via extension, logged-out, VN-localised; AI Overviews 0 of 14 rendered | `docs/raw/e-google-aimode-panel-2026-09-22-retry.md` |
| gap from 2026-09-22 22:40 | v1 | all — user hold 2026-09-22 (panel low value until published evidence is in); never back-filled | — |

## Decisions taken

| date | choice | reason |
|---|---|---|
| 2026-09-22 | Pass 0 split into three tasks (P0-a, P0-b, P0-c) rather than one agent | `panel-protocol.md` gates Pass 10, which needs elapsed calendar time; splitting lets it land sooner. P0-a first because glossary metric definitions feed the other two |
| 2026-09-22 | Pass 10 sampling split one agent per engine per sample date, run one at a time | 32 prompts × 5 runs per engine is too large for one agent and the browser extension is a single shared resource; per-engine files match the protocol's one-file-per-engine-per-date rule |
| 2026-09-22 | Panel raw files use lane `e` with `pass: P10` header | `templates/raw-pull.md` fixes lane slot to a–f; noted in panel-protocol.md |
| 2026-09-22 | Red-team amendments applied by a third Pass 1 agent (P1-c), not by the scheduler | Scheduler does no research; amendments change source coverage and need the same rules as the original pass |
| 2026-09-22 | Claude day-0 sampled logged-in on the researcher-owned account (browser already authenticated); protocol default is logged-out | Sampler brief allowed it; the Memory personalisation confound is recorded in the raw file. Later Claude samples should attempt a logged-out private window first and record which state was achieved |
| 2026-09-22 | Pass 3 clusters re-cut against the 26-name roster: c1 organic 1–8, c2 organic 9–13 + Scrunch, c3 incumbents 1–6, c4 incumbents 7–12 + four held corroborations, c5 agencies by discovery, c6 sell-side from partner lists | shortlist.md assumed 24 dedicated vendors; roster found 13 organic and 12 incumbents |
| 2026-09-22 | Three agents (P2-c11, P3-c1, P10-d0-gemini) killed by API session rate limit at ~20:50 HCM; respawned as resumptions after reset, complete partial raw files kept and committed, in-progress panel file continued by the successor | Raw files are self-contained pulls; a partial cluster is not a failed cluster |
| 2026-09-22 | Samplers may fall back to the MCP_DOCKER Playwright browser when the claude-in-chrome extension reports not connected; pull method recorded as `browser (Playwright MCP)` | Extension dropped mid-session 2026-09-22; Playwright is a shared browser, so samplers use a dedicated new tab and never touch other tabs |
| 2026-09-22 | Remaining day-0 samplers (Copilot, Rufus + P3 checks, and the ChatGPT / AI Mode / Gemini / Claude retries) held until the claude-in-chrome extension reconnects; the sampling slot is lent to Passes 3–5 meanwhile | Two consecutive surfaces bot-blocked the Playwright fallback; a third blocked file adds no evidence. Not a skipped date: day 0 is recorded per engine as sampled, partial, or blocked |
| 2026-09-22 | Chrome extension reconnected ~22:00 HCM (tabs_context_mcp answers); held samplers resume one at a time, priority-1 engines first | Extension is the only browser path not bot-blocked on consumer surfaces |
| 2026-09-22 | WebSearch tool budget (200 calls) exhausted for this orchestrator session; agent briefs now tell agents to rely on direct fetch, site search endpoints (EDGAR full-text, HN Algolia, DuckDuckGo HTML) and the browser | Reported by P3-c0, P3-c1, P3-c3, P3-c5 |
| 2026-09-22 22:30 | Concurrency cap raised by the user from 3 to 10 live agents machine-wide; one browser sampler at a time still | User instruction in chat; supersedes ORCHESTRATION.md and plan.md cap of 3 for this programme |
| 2026-09-22 22:40 | User: success-story hunt (Pass 4) is the most important thing; the panel's own model-output sampling is low value now — other people's published information first, our own validation later. A Fable agent reviews orchestration and plan with the new context | User instruction in chat, verbatim intent recorded; review lands at `docs/method/plan-review-1-2026-09-22.md`, scheduler applies its accepted amendments |
| 2026-09-22 22:55 | REVIEW-1 accepted in full: queue reordered per its §1, grading rule 1 goes into every P4 brief, filenames carry cluster id, one `ext` and one `pw` browser holder, agents append STATE blocks by shell append; AMEND-1 applies the §7 dated appends | Review cites file and line for each change; nothing existing is edited |
| 2026-09-22 | Sitefire/Jerry carries two grades (P4-c10 Bronze: engine and sample size missing; P4-c13 Silver: date window and untouched-page control present). Both recorded; Pass 9 scores with both visible | Conflicting reads sit side by side, never averaged |
| 2026-09-22 | Session works in worktree `worktree-orchestrator`, master fast-forwarded after every commit | Background-session harness rejects edits in the shared checkout; root `CLAUDE.md` wants master only. Fast-forward keeps master current |

## Unknowns

| question | channels checked | date |
|---|---|---|
| Copilot-specific crawler token (Bing page shows none); Apple absent from Cloudflare crawl-to-refer table; HTTP Archive has no AI-crawler report | engine docs, Cloudflare Radar, httparchive.org | 2026-09-22 |
| Anthropic public merchant / checkout program; Perplexity ad-product live status (no page, no withdrawal statement); Perplexity merchant terms prior text (archive blank SPA) | anthropic.com, support.claude.com, perplexity.ai/hub, web.archive.org | 2026-09-22 |
| On-surface ad-label wording for Copilot and Amazon assistant ads | about.ads.microsoft.com, advertising.amazon.com | 2026-09-22 |
| Fee / settlement clauses for ACP, AP2, UCP, x402, Visa TAP; Mastercard Agent Pay schema | protocol repos and owner pages | 2026-09-22 |
| Per-engine (ChatGPT / Claude / Google) referral or conversion breakout from any free retail-analytics publisher | Adobe Digital Insights, Salesforce, Shopify | 2026-09-22 |
| Any ad repository entry distinguishing an ad inside a conversational AI answer; Amazon Ad Library fields; UK codified AI-ad disclosure rule | DSA repositories of Google, Microsoft, Meta, X, Amazon; ASA/CAP | 2026-09-22 |
| AthenaHQ funding (Crunchbase / PitchBook 403); Peec AI price (JS-rendered) | vendor sites, crunchbase.com, pitchbook.com | 2026-09-22 |
| sec.gov, data.sec.gov, efts.sec.gov all 403 this session (robots.txt too) | fetch, Playwright | 2026-09-22 |
| SEC EDGAR full-text on "AI visibility" (HTTP 500); Capterra / TrustRadius not reached | efts.sec.gov, capterra.com, trustradius.com | 2026-09-22 |
| Dockets naming Amazon, Meta AI or xAI with a publisher/brand/advertiser | courtlistener.com (WAF challenge blocked search) | 2026-09-22 |
| OpenAI Instant Checkout fee / take rate | openai.com, help.openai.com, developers.openai.com commerce pages | 2026-09-22 |
| Gemini app ad format; CPC/CPA or billing model for any Google AI-surface ad unit | Google Ads Help, blog.google, GML 2026 pages | 2026-09-22 |
| Amazon Rufus assistant share | Similarweb, Comscore, Datos/SparkToro, StatCounter | 2026-09-22 |
| Google AI Mode / AI Overviews consumer surface — reCAPTCHA "unusual traffic" on the Playwright browser's IP; claude-in-chrome extension disconnected | Playwright MCP ×2 (udm=50 and plain search) | 2026-09-22 |
| Perplexity consumer surface — Cloudflare "Performing security verification" on the Playwright browser | Playwright MCP ×2 | 2026-09-22 |
| ChatGPT consumer surface — extension denied on chatgpt.com ("Permission denied for this action on this domain"), tab reverts to newtab; site permission not granted | fetch (403), Chrome extension ×3 | 2026-09-22 |

## Done conditions

| condition | bar | status |
|---|---|---|
| Load-bearing claims in `findings/` at tier 3 or better | 80 percent or more | not started |
| Priority-1 engine × sub-market cells | Every cell a number or `unknown — checked` | not started |
| Segment matrix | Every cell spend, attention, or none, with signals | not started |
| Success stories | One Silver per vertical, or documented absence with screened count | not started |
| Hypotheses | Every H confirmed, killed, or unresolved with channel checked | not started |
| Pass 10 | Three pre-registered predictions checked against the panel | not started |
