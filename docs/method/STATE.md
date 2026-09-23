# STATE — scheduler state

Created 2026-09-22. The only interface between sessions and between agents. Updated by the main thread after every spawn, landing, and commit. Agents append only under "Landed — pending verify".

## Current pass

**Passes 0–9 and 11 done; Pass 10 skipped by user 2026-09-23. Wave 2 open 2026-09-23:** AMEND-2 (plan appends + new pass sections), R-BLOCKED (browser probe and re-pull of blocked channels), P12-ads (AI-ads evidence, Lane B) live. Then P8-r, P4-r, P13-size, P14-papers, P9-r, BRIEF-4. `findings/executive-brief-2026-09-23.md` and `findings/director-brief-2026-09-23.md` are the reader entry points until BRIEF-4 rewrites them.

## Live agents

Cap 3 from 2026-09-23 resume (run prompt hard rule; see decisions). Browser: one extension holder (`ext`) and one Playwright holder (`pw`) at a time; the rest fetch only.

| id | model | task | deliverable | spawned |
|---|---|---|---|---|
| P14-papers | Opus, `pw` | Research-paper scan: capabilities that steer LLM recommendation or monetise answers; builder-constraint; descriptive only | `docs/raw/d-paper-*-2026-09-23.md`; `docs/findings/frontier-scan.md` | 2026-09-23 |
| P4-r | Opus, `pw` + fetch | Success-story re-hunt: ~107 unchecked brand pages, 25 unopened titles, EDGAR full-text via curl; metric-moved experimental cases only; Reddit/G2 deferred to `ext` slot | `docs/raw/e-case-*-2026-09-23.md`; `findings/proof-scorecard.md` append | 2026-09-23 |
| R-BLOCKED | Opus, `ext` | Probe every blocked channel via browser; re-pull filings, funding, Trends, review sites; credential register | `docs/method/blocked-channels.md`; `docs/raw/*-repull-2026-09-23.md` | 2026-09-23 |

## Queue

Front first. Order per `plan-review-1-2026-09-22.md` §1 (2026-09-22 22:40 user priority). Spawn on completion only. Filenames carry the cluster id. Rows marked `10 held` stay held until the user reopens Pass 10.

| id | pass | model | task | deliverable |
|---|---|---|---|---|
| P8-r | 8 re-run | Sonnet, `ext` after R-BLOCKED | Close the 8 blank high-CPA cells and unrun signals (S2, S3, S9, S10; skincare S4, S6, S12; B2B SaaS S5, S6 paid/agentic terms) via browser | `docs/raw/f-signal-*-2026-09-23.md`; `customers/*.md` appends; `findings/demand-map.md` append |
| P9-r | 9 re-run | Opus | Tier-3 re-evidence of sub-tier claims using re-pulled filings and brand pages; recount both ways | `findings/*.md` appends; `findings/unknowns.md` append |
| BRIEF-4 | reporting | Opus | Rewrite executive and director briefs with an evidence-quality section; regenerate deck | `findings/executive-brief-<date>.md`, `findings/director-brief-<date>.md`, `.pptx` |
| P10-* , P10-analysis | 10 skipped | — | Skipped by user 2026-09-23; day-0 gap stays recorded, never back-filled | — |

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
| P8-c1-bs B2B SaaS signals | 15 pulls `docs/raw/f-signal-bs-S*` + `f-signal-census-bs-2026-09-22.md`; 3 of 9 cells checked (organic × SMB / mid / enterprise via S1 job postings, tier 3); paid and agentic cells none; S1/S4/S5/S9/S10 channels 403 or gated; 9 browser backlog. Note: agent's block reads the tier floor backwards — tier 3 is above the tier-5 floor; compile applies demand-signals.md literally | 2026-09-22 | ae1644b |
| P8-c1-sk skincare signals | 10 pulls `docs/raw/f-signal-sk-S*` + `f-signal-census-sk-2026-09-22.md`; enterprise organic (e.l.f. AEO/GEO team posting; Coty 10-K GEO passage, tier 2) and enterprise agentic (e.l.f. AI Product Owner, $110–140K) checked; SMB organic one OMR reviewer; paid and mid-market none; Indeed / Upwork / G2 / Capterra blocked even via extension; S7 Coty file edited once post-creation (headcount added) — flagged; tier-floor misread as in bs | 2026-09-22 | 20e92a4 |
| P8-c1-hr high-CPA signals | 12 pulls `docs/raw/f-signal-hr-S*` + `f-signal-census-hr-2026-09-22.md`; 1 of 9 cells attributed (organic × enterprise, Cigna SEO/AEO/GEO posting, tier 3); 8 unattributed — sources state no buyer band; Primerica 10-K new S7 filer; cards sub-vertical 0 GEO postings; llms.txt 3 of 9; tier-floor misread as in sk/bs | 2026-09-22 | 3a801c8 |
| P5-c3 comparison farming | 7 pulls `docs/raw/d-comparison-*` + `d-technique-census-c3-2026-09-22.md`; tiers 3–7; 4 measured rows, none before-and-after; academic literature on the technique near-absent; density: B2B SaaS 1 specimen, regulated 0, skincare 0 (against H14 direction); G2/Capterra/SaaSHub blocked | 2026-09-22 | e16775e |
| P5-c7 countermeasures | 9 pulls `docs/raw/d-countermeasure-*` + `d-technique-census-c7-2026-09-22.md`; 6 of 36 engine × technique cells named (OpenAI 1, Anthropic 2, Google 2, Microsoft 1, Perplexity 0, Amazon 0); prompt injection named by 4 engines; no engine names seeding, comparison farming or citation-preference content; 4 defence papers tier 4–5; Amazon policy surface unreachable | 2026-09-22 | 28c5b82 |
| P6-organic | `docs/markets/organic-recommendation.md` (120 lines); bottom-up floor $5.3M–$35.2M annualised from 4 of 34 disclosing vendors; 5 published sizes all tier-6 forecasts; 5 of 5 structural checks answered; proof: 0 Gold / 3 Silver / 45 Bronze | 2026-09-22 | 4efff1a |
| P6-paid | `docs/markets/paid-placement.md` (120 lines); 5 of 8 engines live product, Claude explicit no; 0 rate cards, no computable size; OpenAI $1B run-rate tier 3; 4 of 4 checks + addition 1; litigation table | 2026-09-22 | 4efff1a |
| P5-c6 prompt injection | 13 pulls `docs/raw/d-injection-*` + `d-technique-census-c6-2026-09-22.md`; 9 papers tier 3–5, 4 engine statements, 1 disclosure (Brave / Comet 2025-08-20); no in-the-wild brand-steering campaign documented; OpenAI Operator card carries the only quantified figures; caveat: WebFetch summarises, "verbatim" is best-effort | 2026-09-22 | 937ab68 |
| P8-b2b-saas | `docs/customers/b2b-saas.md` (100 lines); organic × SMB / mid / enterprise read spend on S1 job postings (Actindo, AutoLeap, Pennylane, Mercury; tier 3); 6 paid / agentic cells none — checked (9 of 12 signals); willingness to pay unknown ×9 | 2026-09-22 | f91ad1c |
| P5-c4 citation preference | 9 pulls `docs/raw/d-citationpref-*` + `d-technique-census-c4-2026-09-22.md`; tiers 3–5; 9 measured rows all benchmark, 0 live-site; C-SEO Bench, FeatGEO, CC-GSEO-Bench contradict foundational GEO gains (side by side); engines name no content feature as a citation input | 2026-09-22 | 22e9125 |
| P8-skincare | `docs/customers/skincare-beauty.md` (100 lines); spend 3 (organic / paid / agentic × enterprise: e.l.f. AEO team and agentic PO postings, Google Direct Offers pilot, Estée Lauder Brandlight client), attention 1 (organic × SMB), none 5 on 9–10 of 12 signals; willingness to pay unknown ×9; proof 0 Silver / 2 Bronze | 2026-09-22 | 96b29d3 |
| P8-high-cpa | `docs/customers/high-cpa-regulated.md` (100 lines); spend 1 (organic × enterprise, Cigna posting tier 3), blank 8 (S3 / S9 unchecked, so not `none`); 9 unattributed signals listed; Jerry Bronze (c10) and Silver (c13) side by side | 2026-09-22 | 0b99feb |
| **Pass 8 done** | three customers/ files; 27 cells: spend 7, attention 1, none 11, blank 8; willingness to pay unknown in all 27 | 2026-09-22 | 0b99feb |
| P5-c5 structured data / llms.txt | 9 pulls `docs/raw/d-structured-*` + `d-technique-census-c5-2026-09-22.md`; ChatGPT, Claude, Google, Perplexity read as not consuming llms.txt (Google explicit 2026-07-10; Borysenko HTTP study tier 4, zero fetches); 5 of 6 engines self-publish one; adoption 9 figures incl. measured-by-us; 5 measured rows, strongest vendor-authored RAG experiment | 2026-09-22 | 93898c1 |
| **Pass 5 done** | 7 technique clusters, ~70 raw pulls; no technique has a published single-action before-and-after on a production surface; engines name prompt injection, fake reviews, scaled content abuse — not seeding, comparison farming or citation-preference content | 2026-09-22 | 93898c1 |
| P6-agentic | `docs/markets/agentic-commerce.md` (120 lines); no computable size; 7 forecasts $144B–$5T (2029–30) plus Gartner $15T and GVR $5.7B side by side; measured present-state figures kept separate; 6 protocols with owner, licence, governance, gate; only fee disclosed Copilot 0% | 2026-09-22 | 1db88aa |
| **Pass 6 done** | three markets/ files, 120 lines each, all structural checks answered or unknown; no sub-market has a measured size | 2026-09-22 | 1db88aa |
| P3-repull-sec | `docs/raw/a-sec-probe-2026-09-22.md` — HTTP 503 Akamai maintenance page; re-pull deferred, substitutes stand | 2026-09-22 | 1db88aa |
| P7-organic-b | `docs/competitors/{scrunch-ai,brandlight-ai,change-agents-corp,locafy,otterly-ai,rankscale-ai}.md` (65–78 lines); 3 of 6 publish a price; 0 Gold / 0 Silver; CHGA going-concern, Locafy AUD 3.11M 9-month revenue via tier-5 substitute; 11 brand subjects checked, 0 corroborate | 2026-09-22 | 3a27dbc |
| P7-incumbent-a | `docs/competitors/{airops,conductor,hubspot,yext,ahrefs,birdeye}.md` (77–80 lines); price delta disclosed 2 of 6 (HubSpot, Ahrefs, JPY); 0 Gold / 0 Silver, 13 Bronze; HubSpot control claim beside its negative case; headcount unknown ×6 | 2026-09-22 | fa3cf48 |
| P7-agency | `docs/competitors/{pace-generative,orange142,intero-digital,seer-interactive,fire-and-spark}.md` (77–80 lines); price disclosed 1 of 5 (Pace $1,499 / $1,999 / $2,499 packages); best grade Silver once (Seer content recency); Intero/Freshpet Bronze; Pace two Fools-gold versions of one engagement side by side; parent-level scale only for the two public-company-owned | 2026-09-22 | 7d913f6 |
| P7-organic-a | `docs/competitors/{searchable,geosurge,peec-ai,promptwatch,profound,athenahq,rankprompt,sitefire}.md` (74–80 lines); price 5 of 8; revenue 2 of 8 (Searchable €2.2M ARR; Peec $4M vs $10M pointer side by side); 1 Silver (Sitefire/Pointhound), Jerry two grades side by side; Profound 13 Bronze / 10 Fools gold; 0 Gold; paid-by-outcome unknown on every case | 2026-09-22 | b95392e |
| P7-sellside | `docs/competitors/{feedonomics,shopware,wix,criteo,stackadapt,pacvue,kargo}.md` (79–80 lines); price 1 of 7 (Shopware €600 / €2,400 tiers; Criteo CPM model only); 0 of 7 clear the bar, all cases `screened — not opened`; Pacvue and Kargo named only by OpenAI's partner page, not their own sites — conflict recorded | 2026-09-22 | c5f2f5c |
| P7-incumbent-b | `docs/competitors/{brightedge,muck-rack,quattr,semrush,similarweb,soci,se-ranking,uberall,onclusive}.md` (78–80 lines); price delta 2 of 9 (Semrush +$60/mo, SE Ranking +¥10,478/mo); 1 Silver (Quattr / Men's Wearhouse, brand silent); 0 Gold; four cleared names rest on 1–2 pulls each | 2026-09-22 | 8112990 |
| **Pass 7 profiles done** | 41 profiles in `docs/competitors/`; INDEX pending; across all: 0 Gold, 2 Silver (Quattr, Sitefire/Pointhound) + Jerry contested; 0 of 41 disclose a prompt set with n | 2026-09-22 | 8112990 |
| P7-INDEX | `docs/competitors/INDEX.md` — 41 rows in roster order, brand-side column added, header and caveats per root CLAUDE.md; oldest pull 2026-09-22 | 2026-09-22 | 39b1468 |
| **Pass 7 done** | 41 profiles + INDEX | 2026-09-22 | 39b1468 |
| P9 findings | `docs/findings/{proof-scorecard,demand-map,whitespace,unknowns}.md` (100/100/90/100); hypotheses: 6 confirmed, 6 killed, 4 unresolved, 7 not produced; done rows 2 of 6; 17 of 25 load-bearing claims tier ≤3 = 68%; 0 Gold in ~980 screened, 7 Silver | 2026-09-22 | a43edc9 |
| P9-review | `docs/findings/review-1-2026-09-23.md` (160 lines); 5 of 23 H marks disputed (H5, H6, H15, H16 → unresolved; H11 → not produced); tier-3 share recount 12 of 27 = 44.4% vs 17 of 25 = 68.0%, both stand; 3 of 16 traces mismatch; grading rule 1 literal leaves 1 of 7 Silvers; no execution language, Lane D clean; amendments per file | 2026-09-23 | 83ed796 |
| P9-amend | four findings files amended per review-1 §9: 34 of 34 applied verbatim; tallies 4/3/8/8; 68.0% and 44.4% side by side; line counts 100/100/91/100 | 2026-09-23 | b5ed1c7 |
| P9-amend-2 | `proof-scorecard.md`, `unknowns.md` reconciled: C4 tier 6, eight `not produced` rows, H5/H15/H6 both marks side by side, 44.4% beside 68.0% | 2026-09-23 | bd62e6f |
| **Pass 9 done** | four findings + review-1 + amendments; hypotheses 4 confirmed / 3 killed / 8 unresolved / 8 not produced; tier-3 share 68.0% (P9) and 44.4% (review-1) both stand; 0 Gold, 7 raw Silver (1 under grading rule 1 literal) | 2026-09-23 | bd62e6f |
| P11 | `docs/findings/transition-evidence.md` (92 lines); 108 cases (70 Pass 4 Bronze+, 23 Pass 8 signal rows, 15 llms.txt domains), 99 name a change: content ops 63, stack 58, other 19, org 12, paid 2; H10 confirmed (28 vs 2 at tier ≤3; 13 vs 2 excl. llms.txt), H11 confirmed (e.l.f., Pennylane, Cigna, tier 3) with Pass 9 killed and review-1 not produced beside; 14 grouped rows hold 93 cases (budget flag) | 2026-09-23 | 91c8059 |
| **Pass 11 done** | transition-evidence.md; Pass 10 hold recorded per plan.md hold note | 2026-09-23 | 91c8059 |
| REVIEW-2 | `docs/method/plan-review-2-2026-09-23.md` (119): 4 of 6 done rows can still move while Pass 10 held; tier-3 shortfall decomposed (8 case-corpus, 1 forecast, 3 third-party, 3 meta); grading rule 1 append; Pass 10 one date closes HE2, HP1, HP3, HP2/HP4 need two; 7 appends §8 a–g. `docs/findings/executive-brief-2026-09-23.md` (69): 22 metric rows, all sourced, no verdict, 4 owner questions | 2026-09-23 | 54ae617 |
| REVIEW-2b | `docs/findings/executive-brief-2026-09-23.md` (70): Pass 11 row added (99 of 108 name a change; H10, H11 confirmed with prior marks beside), last caveat replaced | 2026-09-23 | 950c8e7 |
| P2-c4 Google platform | 13 pulls `docs/raw/{a,b,c}-google-*` + `b-google-platform-summary-2026-09-22.md`; Gemini app ad format unknown | 2026-09-22 | edd2725 |
| BRIEF-3 | `docs/findings/director-brief-2026-09-23.md` (293 lines, budget 300) — 10–20 min director reading brief, 14 sections, 140 sourced rows, all 23 H, both-readings pairs kept; `docs/method/gen-director-deck.py` → `docs/findings/director-brief-2026-09-23.pptx` (18 slides, generated, never hand-edited; run with Python 3.14 where python-pptx is installed). 0 pulls | 2026-09-23 | fee9d0d |
| AMEND-2 | `docs/method/plan.md` 362 → 567 lines, additions only; `docs/method/hypotheses.md` 105 → 156, H17–H25 (post-hoc to Passes 2–9, pre-registered for 12–14). §8 a–g applied; scope addition 1; Pass 10 skipped; Pass 12/13/14 + P8-r/P4-r/P9-r sections; evidence-quality reporting; browser/search revision; 15 failure-mode rows + debt map; done rows for 12–14. 0 pulls | 2026-09-23 | d1d62cf |
| P12-ads | `docs/findings/ai-ads-evidence.md` (100 lines); `docs/markets/paid-placement.md` +69 (L121–189). 91 raw `b-*-2026-09-23.md`: tier 2 ×1, tier 3 ×38, tier 5 ×48, tier 6 noise ×4. Live ads at tier 3: ChatGPT, Google AIO, AI Mode (testing), Copilot, Rufus/Alexa, Snap My AI (stale). Prices: OpenAI $3–$5 CPC bid + 25 USD/day min (t3); Kontext $3 CPM (t3, network); launch $60 CPM / $200–250K min (t5). Revenue at t3: OpenAI $1B run rate only. Controlled results: 0 of 15. H17 killed, H18 confirmed, H19 confirmed, H20 killed. 60 WebSearch calls. Blocked: sec.gov 10-Q 403, investing.com 403, searchengineland 403, markey.senate.gov 403; Adweek/EMARKETER/FT paywalled | 2026-09-23 | c86608f |
| P13-size | `docs/findings/market-potential.md` (100 lines); `markets/` appends organic +15, paid +15, agentic +14 (overrun in caveats). 24 raw `-2026-09-23.md`: t2 ×2 (Alphabet 10-K, SpaceX S-1/A), t3 ×8, t4 ×2, t5 ×3, t6 ×8, t7 ×1. ≥2 dated user-count points at t≤3: ChatGPT, Google (Gemini app/AIO/AI Mode), Copilot, Meta AI, Grok (t2), Rufus; none for Claude, Perplexity 2026, DeepSeek. Forecast spread: organic 1.92× (2034), paid ~20× (2030, scopes differ), agentic 26.3× (2030). Floors: organic $42.2M–$48.2M + €2.2M ARR (4 vendors); paid ≥$1B (ChatGPT only); agentic GMV unknown. H16 unresolved, H21 killed, H22 killed. Done cells 9 of 9. 43 WebSearch. openai.com/perplexity.ai/gartner.com 403 → archive captures; datos.live behind form (register) | 2026-09-23 | 248b1d3 |

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
| 2026-09-22 | Pass 8 files differ on partial checks: skincare-beauty writes `none — checked` on 9–10 of 12 signals with the shortfall itemised; high-cpa-regulated writes `blank` where S3 / S9 were unchecked. Both stand; Pass 9 scores H4 / H7 / H9 with the difference stated, not reconciled | demand-signals.md's `none` rule reads strictly; two compilers applied it differently on the same day |
| 2026-09-22 | Pass 9 opened while P7-INDEX compiles: findings cite profiles and raw, not INDEX; INDEX is derived from landed profiles and lands before Pass 9 is marked done | Gate substance met; INDEX is a derived entry point |
| 2026-09-23 | Run paused on user instruction; P9-review and its two helper agents stopped, nothing written; re-queued at front rather than resumed | User: "pause new agents and remember progress and state. we end here". Stopped agents had produced no file, so a fresh spawn is cheaper than a partial resume |
| 2026-09-23 | Resumed; cap read as 3 live agents | Re-pasted run prompt states "never more than 3" as a hard rule; stricter reading never violates either instruction. Next tasks are sequential, so the cap does not bind |
| 2026-09-23 | Pass 10 hold kept despite run prompt's "never skip a sampling date" | Specific dated user decision 2026-09-22 22:40 outranks the generic run-prompt template; gap stays recorded, never back-filled |
| 2026-09-23 | Session works on master checkout directly, no worktree | Root CLAUDE.md: master only, no worktrees |
| 2026-09-23 | REVIEW-2 spawned on user request: plan improvements plus a director-level brief; brief is evidence only, verdict stays the user's | User: report to a business owner what was done and what could improve the plan; MegaPlan.md non-goals forbid a verdict, so the brief names owner decisions as questions |
| 2026-09-23 | P9-review respawned after a session /clear; deliverable renamed `review-1-2026-09-23.md` (was `-09-22`); budget 160 lines | Prior spawn wrote no file; file date must be the write date; amendments quote lines verbatim, which the 100-line finding budget cannot hold |
| 2026-09-23 | Pass 10 skipped, not held: own-panel sampling out of scope for now | User: "pass 10 skip for now. We dont care about what observed ourself". HE2, HE3, HP1–HP4 stay `not produced`; gap recorded |
| 2026-09-23 | Pass 12 opened: evidence of AI ads and of AI engines selling ads, Lane B deep pull | User: "vastly important key details that we are missing" |
| 2026-09-23 | plan-review-2 §8 appends applied (AMEND-2); tasks that failed to qualify re-run: P8-r segment blanks, P4-r success hunt on blocked channels, P9-r tier-3 re-evidence | User: "apply review-2 and then rerun whatever tasks failed to qualified" |
| 2026-09-23 | Scope: potential of all three sub-markets; market size read from trends, engine user counts and forecasts side by side (Pass 13). Forecasts stay labelled forecast, tier 6 | User: "researching potential for all markets... trends and user count regarding market size of organic vs paid vs agentic and future prediction" |
| 2026-09-23 | Builder-constraint question back in scope; engineering-enabled new market potential and novel solutions in scope; research-paper scan (Pass 14) for state-of-the-art capabilities open to abuse or monetisation, descriptive only | User items 5 and feedback 6 |
| 2026-09-23 | Browser (extension `ext`, Playwright `pw`) allowed for every agent including blocked channels; one `ext` holder at a time (shared browser); WebSearch budget 5000+ | User: "Allow chrome extension and browser access", "I allow 5000+ websearch budget now" |
| 2026-09-23 | Blocked channels re-pulled (R-BLOCKED); any channel needing registration or paid credentials goes to `docs/method/blocked-channels.md` for the user | User: "if any channels require registration then feedback to user"; "append to blocked list for human to review" |
| 2026-09-23 | Briefs report evidence quality explicitly: transition evidence with no moved metric = "everyone did this, unknown if it works"; metric-moved experimental cases are the target and must be pulled when found | User feedback 3 |
| 2026-09-23 | Method debt (plan-review-2 §6) cleaned by AMEND-2 appends | User feedback 4 |
| 2026-09-23 | BRIEF-3 spawned on user request: a 10–20 minute director reading brief, metrics and key details, plus a PowerPoint. Budget 300 lines (finding budget 100 lifted for this file only); deck is a generated file from `docs/method/gen-director-deck.py`, never hand-edited; `python-pptx` may be installed for it | User: "brief reading 10-20 minutes max, full of key metrics and highlight key details; convert reading into powerpoint". Compiled files only, no verdict, no execution language |
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
| sec.gov, data.sec.gov, efts.sec.gov 403 all session; probe at ~01:00 next day HTTP 503 Akamai maintenance | fetch, Playwright, curl with contact UA | 2026-09-22 |
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
| Load-bearing claims in `findings/` at tier 3 or better | 80 percent or more | not met — 17 of 25 (68.0%) per Pass 9 and 12 of 27 (44.4%) per review-1, both stand; shortfall is Lane E vendor-reported cases and tier-6 market forecasts |
| Priority-1 engine × sub-market cells | Every cell a number or `unknown — checked` | met — 9 of 9 in whitespace.md; review-1 re-derived, agrees |
| Segment matrix | Every cell spend, attention, or none, with signals | not met — 19 of 27; 8 high-CPA cells `blank` (S3 / S9 unchecked); review-1: strict `none` rule leaves 8 of 27, loose rule 27 of 27, both recorded |
| Success stories | One Silver per vertical, or documented absence with screened count | met — raw grades: B2B SaaS and high-CPA on the Silver arm, skincare on absence (~133 screened); grading rule 1 literal: all three on the absence arm (~133 / ~100 / 34 screened) |
| Hypotheses | Every H confirmed, killed, or unresolved with channel checked | partial — 17 of 23 scored (Pass 11 adds H10, H11 confirmed; review-1 4 / 3 / 8 and Pass 9 6 / 6 / 4 both stand); 6 `not produced` (HE2, HE3, HP1–HP4 held with Pass 10) |
| Pass 10 | Three pre-registered predictions checked against the panel | skipped by user 2026-09-23 — 0 of 3; day-0 gap recorded, never back-filled |
