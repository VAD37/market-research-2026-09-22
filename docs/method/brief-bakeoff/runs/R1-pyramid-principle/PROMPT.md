# Shared instruction — identical for every run. Only {RUN_ID}, {OUT_DIR}, {SKILL_FILES} differ.

You are run R1. Write to D:\researchs\market-research-2026-09-22\docs\method\brief-bakeoff\runs\R1-pyramid-principle only. Do not run git. Do not use the web. Do not read any file under `.claude/` except the ones listed below. Do not read any other folder under `docs/method/brief-bakeoff/`.

## Operating instruction

Read these files first and treat them as your method for this task. Follow them where they do not conflict with the constraints below; where they conflict, the constraints win and you record the conflict in notes.md:

- `D:\researchs\market-research-2026-09-22\.claude\skill-candidates\pyramid-principle\skills\pyramid-principle-core\SKILL.md`
- `D:\researchs\market-research-2026-09-22\.claude\skill-candidates\pyramid-principle\skills\pyramid-principle-core\references\rules-of-pyramid.md`
- `D:\researchs\market-research-2026-09-22\.claude\skill-candidates\pyramid-principle\skills\pyramid-principle-core\references\scqa-pattern.md`
- `D:\researchs\market-research-2026-09-22\.claude\skill-candidates\pyramid-principle\skills\pyramid-principle-core\references\mece-grouping.md`
- `D:\researchs\market-research-2026-09-22\.claude\skill-candidates\pyramid-principle\skills\pyramid-principle-core\references\vertical-horizontal-logic.md`
- `D:\researchs\market-research-2026-09-22\.claude\skill-candidates\pyramid-principle\skills\pyramid-principle-core\references\llm-adaptation.md`
- `D:\researchs\market-research-2026-09-22\.claude\skill-candidates\pyramid-principle\skills\pyramid-long-form\SKILL.md`
- `D:\researchs\market-research-2026-09-22\.claude\skill-candidates\pyramid-principle\skills\pyramid-long-form\references\report-skeleton.md`
- `D:\researchs\market-research-2026-09-22\.claude\skill-candidates\pyramid-principle\skills\pyramid-long-form\references\key-line-examples.md`
- `D:\researchs\market-research-2026-09-22\.claude\skill-candidates\pyramid-principle\skills\pyramid-source-integrity\SKILL.md`
- `D:\researchs\market-research-2026-09-22\.claude\skill-candidates\pyramid-principle\skills\pyramid-source-integrity\references\strict-trace.md`

## Situation

A director will read one document for 10 minutes. They have never heard of this project, this market, or any of its acronyms. They want: what is this, why now, how big, who is already there, what could kill it, what do you want from me.

The existing document written for them failed. It is `D:\researchs\market-research-2026-09-22\docs\findings\director-brief-2026-09-23.md`. Read it fully. It is your primary source. Everything it cites lives under `D:\researchs\market-research-2026-09-22\docs\` — `findings/`, `markets/`, `competitors/`, `customers/`, `raw/`. You may read any of those to check or strengthen a figure. Evidence tier scale: `docs/method/trust-rubric.md` — lower tier number is stronger.

The subject: whether real demand exists, per segment, for brand visibility and product recommendation inside AI assistants (ChatGPT, Gemini, Perplexity, Copilot, Claude), and what evidence shows it works. The programme is research only — it produces evidence, not a go/no-go. The verdict belongs to the reader.

## Task

Write the document the director should have received. Save as `D:\researchs\market-research-2026-09-22\docs\method\brief-bakeoff\runs\R1-pyramid-principle\brief.md`.

## Constraints (win over the operating instruction)

1. Every number in brief.md exists in a repo file. Record each in `D:\researchs\market-research-2026-09-22\docs\method\brief-bakeoff\runs\R1-pyramid-principle\trace.md` as `number | brief line | repo path:line | source kind | source date`. A number you cannot trace does not go in.
2. No arithmetic on repo numbers unless the repo file already did it. No invented examples, illustrative figures, or placeholders presented as data.
3. `unknown — not in repo` beats a guess. Say what is missing.
4. Conflicting figures sit side by side, attributed. Never averaged, never silently picked.
5. Every number carries its source kind (vendor-reported / analyst-derived / filed / company-stated / measured-by-us) and an absolute date (YYYY-MM at least).
6. No execution planning: no dates for action, budgets, MVPs, roadmaps, owners. A hypothetical product may be described as a hypothesis, not a plan.
7. Do not tell the director whether to proceed. Give them what they need to decide.
8. Define every acronym on first use or in a glossary. No internal codenames (pass numbers, hypothesis codes like H3, file or folder names, review round names) in the body.
9. Body hard cap 1,200 words. Appendix and glossary do not count. Tables count.
10. Absolute dates. Never "recently", "currently" without a date.

## Also write

`D:\researchs\market-research-2026-09-22\docs\method\brief-bakeoff\runs\R1-pyramid-principle\notes.md`, max 300 words:
- Model id and timestamp.
- What the operating instruction made you do that you would not have done unaided. Quote the rule with its file path and line.
- Every place you overrode the operating instruction because of a constraint above. Quote the rule, state the constraint.
- What the operating instruction had no opinion on that mattered here.

## Return

Five lines: run id · body word count · rows in trace.md · count of "unknown" entries in brief.md · count of overrides in notes.md.

## Addition 1, 2026-09-23 — applies to every run; set before any run was spawned

Per `../biz-review-2-bakeoff-2026-09-23.md` §3. Identical for all runs; the orchestrator filled the snapshot hash (8badc05) here and the pack line ranges in Addition 2 at spawn.

Read next, in order, and treat as the same input as the failed brief. Input snapshot is commit `8badc05`; cite nothing newer:

1. `docs/method/scope.md` §what the market is; `docs/method/glossary.md` — what: market, three sub-markets, three metrics never crossed
2. `docs/method/trust-rubric.md`; `docs/method/plan.md` §"Evidence bar — evidence-quality reporting" — tier, grade, demand-read and evidence-class scales
3. `docs/findings/trigger-timeline.md` — why now: dated events
4. `docs/findings/market-potential.md` — size three ways; floors; forecast spreads; sub-markets side by side; pricing
5. `docs/findings/ai-ads-evidence.md`; `docs/markets/paid-placement.md` — paid supply: who sells, prices published, baselines
6. `docs/competitors/INDEX.md`; `docs/markets/organic-recommendation.md` — who is there; disclosure ratios; funding table; publisher side
7. `docs/markets/agentic-commerce.md` — agentic supply, fees, gates
8. `docs/findings/demand-map.md`; `docs/customers/*.md` cell tables — who buys: latest 27-cell tallies, both readings; local vertical
9. `docs/findings/proof-scorecard.md` §three-count and §negative tail — evidence ladder; negative tail beside positives
10. `docs/findings/transition-evidence.md` — what movers changed; three-count of 108
11. `docs/findings/whitespace.md` §risk register — gaps; ranked risks with platform capture
12. `docs/findings/unknowns.md` §tier-3 recount, §hypothesis register, §figures carried twice; `docs/method/blocked-channels.md` — unknowns, tier-3 share six ways, 32 hypothesis marks, credential-gated channels

Constraints 11–16 (win over the operating instruction, same as 1–10):

11. The answer slot every method demands (governing thought, recommendation, resolution, verdict) carries the evidential answer to the reader's question — what the evidence supports and where it stops — never a course of action. Where a method's gate asks whether the reader must accept a judgment, the judgment is that reading.
12. Audience fields: stance neutral; decision wanted: none, the reader decides; priorities: none stated. You cannot ask; record every assumption in notes.md.
13. Method commentary the operating instruction requires (sequencing choice, emotional lever, MECE groups, pyramid visual, self-checks) goes to notes.md, never brief.md.
14. When one figure carries two readings or two dates, the body carries the later-dated figure with its reading label (strict/loose, raw/rule-1, R1/R2) and names that another reading exists; the appendix carries the pair with both dates and paths. Neither is dropped.
15. A rounded, re-unitised or converted number is arithmetic. Carry the figure as the repo states it. Likelihood, impact, mitigation and owner: write "no source states one".
16. trace.md cites `docs/raw/` path:line, or a compiled file plus row id (E1, C1, T1, rank 1). Never a `STATE.md` or `plan.md` line number. Repo paths may appear in the appendix, never in the body. The return-line `unknown` count includes both `unknown — not in repo` and `unknown — checked`.

## Addition 2, 2026-09-23 — line ranges at snapshot 8badc05; files outside the input

Line ranges for the evidence pack above, as read at commit 8badc05 (files are append-only; nothing after these lines is input):

| pack # | file | lines |
|---|---|---|
| 1 | `docs/method/scope.md` §The market splits three ways | L17–26 (file 96) |
| 1 | `docs/method/glossary.md` | whole, 223 |
| 2 | `docs/method/trust-rubric.md` | whole, 61 |
| 2 | `docs/method/plan.md` §Evidence bar — evidence-quality reporting | L142–157 (grading rule 1 L128–141 beside) |
| 3 | `docs/findings/trigger-timeline.md` | whole, 104 |
| 4 | `docs/findings/market-potential.md` | whole, 288; §Pricing L102–159; §Sub-markets side by side L160–171; §Brand-side adoption series L195–241; §EU engine share L242–273 |
| 5 | `docs/findings/ai-ads-evidence.md` | whole, 152 |
| 5 | `docs/markets/paid-placement.md` | whole, 308 |
| 6 | `docs/competitors/INDEX.md` | whole, 140; §Funding, M&A and valuation L60–130; §Measurement and compliance vendors L131–140 |
| 6 | `docs/markets/organic-recommendation.md` | whole, 214; §Publisher-side monetisation L144–162 |
| 7 | `docs/markets/agentic-commerce.md` | whole, 156 |
| 8 | `docs/findings/demand-map.md` | whole, 266; §Local / multi-location L201–233; §S1 body check L234–250; §EU paid and agentic L251–266 |
| 8 | `docs/customers/skincare-beauty.md`, `b2b-saas.md`, `high-cpa-regulated.md`, `local-multi-location.md` | whole: 240, 242, 262, 94 |
| 9 | `docs/findings/proof-scorecard.md` §Evidence-quality three-count L180–245; §Negative tail L246–294 | file 300 |
| 10 | `docs/findings/transition-evidence.md` §Evidence-quality three-count L94–145 | file 148 |
| 11 | `docs/findings/whitespace.md` §Risk register L93–112 | file 131 |
| 12 | `docs/findings/unknowns.md` §Tier-3 recount L132–135; §Hypothesis register L234–293; §Figures carried twice L294–345; §By-file roll-up L346–366 | file 366 |
| 12 | `docs/method/blocked-channels.md` | whole, 108 |

Not input, do not open: any file whose name contains `-r2` (`docs/findings/executive-brief-2026-09-23-r2.md`, `director-brief-2026-09-23-r2.md`, `.pptx`), `docs/method/gen-director-deck*.py`, `docs/method/STATE.md`, `docs/method/biz-review-*.md`, `docs/method/brief-bakeoff/` beyond this file. A trace row pointing at any of them counts as pointing nowhere.
