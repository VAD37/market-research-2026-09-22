# Plan review 2 — the plan against nine passes

Task REVIEW-2, 2026-09-23. Method review only: what `plan.md` and the run carry that nine passes showed to be wrong, missing or unmeasurable. Nothing existing is edited; every change is a dated append in §8. No market claim goes beyond a cited compiled or `raw/` file. Line numbers as read 2026-09-23. Inputs: the method set, `STATE.md`, the five `findings/` files, `markets/`, `customers/`, `competitors/INDEX.md`; `raw/` headers only to check labels. `findings/transition-evidence.md` (Pass 11, live) was not read.

## 1. Done-condition arithmetic

Status per `STATE.md` lines 188–195 and `review-1-2026-09-23.md` §5. "Moves without Pass 10": an internet pull at the named tier can change the row while the hold stands.

| Row | Status 2026-09-23 | Moves without Pass 10 | Evidence needed |
|---|---|---|---|
| Tier-3 share ≥80% | 17 of 25 = 68.0% (Pass 9); 12 of 27 = 44.4% (review-1) | yes | Re-evidence at tier ≤3: 3 of Pass 9's 8 sub-tier claims; 10 of review-1's 15 |
| P1 engine × sub-market | met, 9 of 9 | holds | none |
| Segment matrix | 19 of 27; strict 8, loose 27 | yes | 8 high-CPA cells: S2, S3, S9, rest of S10, plus band attribution — §5 |
| Success stories | met under both grade readings | holds | none; §3 fixes which reading counts |
| Hypotheses | 15 of 23 scored | **no** | Pass 11 can score H10, H11: ceiling 17 of 23. HE2, HE3, HP1–HP4 need tier-1 panel records |
| Pass 10 | 0 of 3 | **no** | tier-1 panel records, `panel-protocol.md` schema |

While the hold stands, 4 of 6 rows are reachable; 2 are not. Adding new tier-≤3 claims alone needs +15 (Pass 9 count) or +48 (review count). Routes to tier ≤3 open to internet pulls: a brand's own page (tier 3; 0 of 59 corroborate, ~107 unchecked — `raw/e-case-census-c7-2026-09-22.md`), a filing (tier 2; sec.gov 403 then 503 — `STATE.md` line 176), peer-reviewed work (tier 2–3, `trust-rubric.md` lines 27–28). Append: §8(a).

## 2. Tier-3 share — the bar against a tier-5 category

Evidence: `trust-rubric.md` line 15 puts "Vendor or agency study with n, dates, method" at tier 5; `unknowns.md` line 62: the sub-tier-3 load-bearing claims are Lane E, "structurally vendor-reported at tier 5"; `review-1-2026-09-23.md` lines 51–77 itemise all 27 claims. The review-1 residual, 15 of 27 below tier 3 or without a raw tier:

| Group | Claims (file:claim) | Tier | Why below 3 |
|---|---|---|---|
| Case corpus, Lane E | proof C1, C2, C3, C4, C6, row L53; unknowns C1; whitespace C6 | 4–6 | cases are published by the vendor or agency that sold the work |
| Market forecasts | whitespace C2 | 6 | report-sales firms; Gartner, GVR 403; EMARKETER gated |
| Third-party panels, benchmarks | whitespace C8 (5), C5 (4) | 4–5 | ad-presence and llms.txt measured by vendors or preprints |
| Review-site signal | demand C1 via E1 | 5 | one OMR reviewer |
| Meta-claims, no raw | demand C6; unknowns C4, C5 | n/a | count the findings themselves |

Reading: the bar measures both the research and the category. 9 of 15 sit below tier 3 because of how the category publishes (vendor cases, report-sales forecasts) while brands stay silent; 3 are a counting-rule artefact; 3 rest on third-party measurement no tier-≤3 source replicates. Excluding the 8 case-corpus claims: 12 of 19 = 63.2%; excluding the 3 meta-claims too: 12 of 16 = 75.0% (review-1's list; `unknowns.md` line 55 does not itemise Pass 9's 25). Residual: 32.0% (Pass 9), 55.6% (review-1); both stand. No bar change: `plan.md` line 88 sets the evidence bar "before pulling so it cannot be relaxed to fit what turns up", and lowering 80% after the count repeats that failure. The append adds reporting splits, not a threshold. Append: §8(b).

## 3. Grading rule 1 — which reading counts

Evidence: `plan.md` line 117, "a case missing any of items 1–7 is Bronze at best". Review-1 line 102: 6 of 7 raw Silvers miss an item (Quattr 3; Pointhound 6; Jerry c13 6; Seer 3, 7; Tiwari 3, 5; NerdWallet 6); only TW3 answers all seven. `e-case-c10-sitefire-jerry` applied the literal reading, `-c13-` did not (review-1 line 157). `proof-scorecard.md` lines 17, 23 and `STATE.md` line 193 carry both counts.

Problem: the Success-stories row holds either way, but H6's mark (`unknowns.md` line 30) and every downstream Silver count turn on the reading, and Pass 11 cites Pass 4 cases with no rule for which grade to use. Proposal: the literal reading becomes the operative grade, because it is the rule's own wording, registered 2026-09-22 before the Pass 4 second sweep ran; the census grade is kept beside it, never deleted. Append: §8(c).

## 4. Pass 10 — what the hold leaves open

Held by user 2026-09-22 22:40 (`plan.md` lines 271–275; `STATE.md` line 134). Done rows held with it: Pass 10 (0 of 3) and Hypotheses (ceiling 17 of 23). Evidence only; reopening is the user's decision.

| Row, all `not produced` (`unknowns.md` lines 42–47) | One sampling date | Why |
|---|---|---|
| HE2, HP1, HP3 | can close | one engine, full set (HE2); two P1 engines, one date, one surface (HP1); coded from the same records (HP3) |
| HE3 | can confirm only | kill needs "no format doc tier 3"; AI Mode "Sponsored" doc exists (`markets/paid-placement.md` line 77) |
| HP2, HP4 | cannot | two dates ≥14 days apart; HP4 also a toggle both engines expose (`hypotheses.md` lines 70, 72) |

One date reaches at most 4 of 6 panel rows, so the bar of three is reachable from one date only if three of HE2, HE3, HP1, HP3 score. Confounds recorded on day 0, 2026-09-22:

| Engine | Record | Raw |
|---|---|---|
| Claude | 83 of 160 runs, logged-in, Memory localises answers to Vietnam; `region_intended: US` failed every run | `raw/e-claude-panel-2026-09-22.md` |
| Gemini | 24 of 160, logged-out, "Flash-Lite", silent throttle, no search toggle | `raw/e-gemini-panel-2026-09-22.md` |
| Google AI Mode / AIO | 76 of a possible 176; IP-localised to Vietnam; AIO 0 of 14 rendered | `raw/e-google-aimode-panel-2026-09-22-retry.md` |
| ChatGPT; Perplexity | 0 runs: extension "Permission denied for this action on this domain"; Cloudflare, two Ray IDs | `raw/e-chatgpt-panel-2026-09-22.md`; `raw/e-perplexity-panel-2026-09-22.md` |

Copilot and Rufus were never sampled (`STATE.md` line 24). No raw file records a US egress path: `unknown — checked the six day-0 files 2026-09-23`. Append: §8(d).

## 5. Segment matrix — 8 blanks and the `none` split

Evidence: `customers/high-cpa-regulated.md` lines 19–27; `demand-map.md` lines 38–45; `demand-signals.md` line 38 ("Every catalogue signal checked") and line 59 (band proxies); `channels.md` line 143.

| Blank cells, high-CPA | Unchecked or unattributed | Channels that close it |
|---|---|---|
| Organic × SMB, × mid-market | S3, S9 unchecked; S10 part; S1, S2, S7, S8 found, no band | S3: C13–C16, C58, C67. S9: C45, C21–C24, C26, C30. Band: filing, careers page, network profile |
| Paid × 3 sizes | S2, S3, S9 unchecked; S10 part | S2: C46, C1, C5; S3, S9 as above; S10: C18, C20 |
| Agentic × 3 sizes | as paid; S8 John Lewis FS names no band | as paid, plus band for the S8 name |

S9 needs a browser (trends.google.com JS-rendered, `raw/f-signal-hr-S9-search-interest-2026-09-22.md`); a closed cell may read `none` and still meets the row. The split: under the strict reading the 11 `none` cells also fail — skincare organic-mid (10 of 12), skincare paid/agentic SMB and mid (S4, S6, S12 unrun), B2B SaaS paid/agentic ×6 (S5, S6 run with organic terms only); under the loose reading all 27 meet. A third fault: `customers/b2b-saas.md` line 36 marks S12 `n/a` by construction for paid and agentic, so strict-reading cells there can never read `none`. Running the unrun signals makes both readings agree. Append: §8(e).

## 6. Method debt — recorded in the run, absent from the plan (append §8(f))

| Debt | Recorded at | Plan carries today |
|---|---|---|
| WebSearch budget (200 calls) exhausted | `STATE.md` line 150 | nothing; substitutes named only in review-1 §5 |
| sec.gov 403, then 503; filings via IR copies (tier 3) or StockTitan relays (tier 5) | `STATE.md` lines 103, 176; `markets/organic-recommendation.md` line 29 | review-1 §5 only |
| G2, Capterra, Reddit, Indeed, Upwork, Trends blocked | `unknowns.md` lines 91–93; `whitespace.md` line 85 | no blocked-vs-exhausted mark in the done rows |
| MozCon abstracts paraphrased (site copyright) | `STATE.md` line 76; `raw/f-conference-mozcon-london-2026-agenda-2026-09-22.md` line 21 | nothing |
| WebFetch summarises; "verbatim is best-effort" | `STATE.md` line 93; `raw/a-similarweb-share-gen-ai-stats-2026-09-22.md` line 18 | nothing |
| S7 Coty raw edited after creation (headcount added) | `STATE.md` line 87; `demand-map.md` line 99 | `docs/CLAUDE.md` line 27 forbids it; no check at verify |
| "c2 19", "c3 27", "Seven named channels" untraceable | `review-1-2026-09-23.md` lines 84, 153 | no count-to-raw-line rule |
| P8 censuses read the tier-5 floor as a ceiling | `STATE.md` lines 86–88 | nothing in the brief text |
| Cap: plan 10 (line 312), STATE 3 (line 158), MegaPlan 3 (line 32) | as cited | two figures in force |

## 7. Reporting layer — the director brief

No file in `docs/` serves a reader with ten minutes; `docs/CLAUDE.md` line 57 lists "the summary a reader opens first" as a `findings/` kind and none exists. Specification for `findings/executive-brief-2026-09-23.md`, written alongside this file, 70 lines, re-stating compiled numbers only and rewritten under a new date whenever a cited finding changes:

| Contains | Excludes |
|---|---|
| The `plan.md` line 11 question and a five-sentence answer | a verdict (`MegaPlan.md` line 17) |
| One table of decision metrics, each with label, tier and path | any figure absent from a compiled file |
| Forecasts beside the "no measured size" line, with tiers | a forecast presented as a size (`trust-rubric.md` line 42) |
| Conflicting figures side by side; both tier-3 counts | averages, reconciled ranges |
| What the evidence does not show | prescriptions or sequencing (`MegaPlan.md` line 15) |
| Owner decisions, phrased as questions with no lean | dates for future work, budgets, build steps |

Append: §8(g).

## 8. Paste-ready appends — `plan.md`, dated 2026-09-23

| # | Where | Append, verbatim |
|---|---|---|
| a | append to plan.md §Programme done | `### Programme done — arithmetic note 1, 2026-09-23` "While the Pass 10 hold stands, the Hypotheses row has a ceiling of 17 of 23 and the Pass 10 row 0 of 3; neither is reachable. The tier-3, segment-matrix, P1-cell and success-story rows are reachable by internet pulls. Each done-row status names both counts where two exist. Source: `plan-review-2-2026-09-23.md` §1." |
| b | append to plan.md §Programme done | `### Tier-3 share — reporting splits, 2026-09-23` "Bar unchanged at 80%. Every count reports three figures: all load-bearing claims; claims excluding the Lane E case corpus; claims excluding meta-claims with no raw tier. Every count itemises its claims file:claim so a second count can be diffed against it. Source: review-2 §2." |
| c | append to plan.md §Evidence bar | `### Evidence bar — grading rule 1 reading fixed, 2026-09-23` "Every graded case carries `grade_raw`, as its census assigned it, and `grade_rule1`, the literal reading: any of items 1–7 absent on the case's own page caps it at Bronze. From Pass 11 on, counts, done rows and hypothesis marks use `grade_rule1` and cite `grade_raw` beside it. Neither is deleted. A grade moves only through a new dated raw file naming the item that changed." |
| d | append to plan.md §Pass 10 and Pass 11 — hold note | `### Pass 10 — closure map, 2026-09-23` "One neutral sampling date can close HE2, HP1, HP3 and confirm HE3; HP2 and HP4 need two dates ≥14 days apart. Day-0 confounds on record: Claude logged-in with Memory, Gemini Flash-Lite throttled, AI Mode IP-localised to Vietnam, ChatGPT and Perplexity blocked. No raw file records a US egress path. Recorded for the user's decision; the hold is unchanged." |
| e | append to plan.md §Segments | `### Demand signals — none rule, 2026-09-23` "A signal marked `n/a` because it cannot apply to the sub-market by construction counts as checked. The Segment-matrix row is reported under the strict and loose readings until every cell has every applicable signal run; closing it needs S2, S3, S9 and S10 in high-CPA, S4, S6, S12 for skincare paid and agentic, S5 and S6 with paid and agentic terms in B2B SaaS." |
| f | append to plan.md §Known failure modes | `### Known failure modes — addition 1, 2026-09-23` rows: "Search budget exhausted → briefs carry seed URLs and substitute endpoints"; "Filing host blocked → filing via relay is tier 5, via IR copy tier 3, never tier 2"; "Channel blocked → done rows mark blocked, not exhausted"; "Paraphrased or summarised pull → raw header `verbatim: partial`, no compiled quote from that part"; "Raw file edited after landing → re-pulled as a new dated file, old kept"; "Count untraceable → every count cites the raw line it sums"; "Tier misread → briefs state lower tier number is stronger"; "Cap figures disagree → STATE decision line is the cap in force". |
| g | append to plan.md §Pass sequence | `### Reporting layer, 2026-09-23` "`findings/executive-brief-<date>.md`, 70 lines, re-stated from compiled files only, per the review-2 §7 contains/excludes table. Rewritten under a new date whenever a finding it cites changes. Not a pass; no gate." |

## Caveats

- One reviewer, desk only, 2026-09-23, 0 pulls. Pass 11's live output was not read; §1 assumes it moves H10 and H11 only.
- §2's splits use review-1's itemisation; Pass 9's 25-claim list is not itemised in any file, so its split is not computed.
- §4 maps hypothesis conditions to sampling dates from `hypotheses.md` text; it does not estimate whether a date yields usable records. §1 names reachability, not likelihood; every blocked channel in §6 was blocked on 2026-09-22 from one machine.
- This file carries method evidence, not a verdict on the market or on reopening Pass 10.
