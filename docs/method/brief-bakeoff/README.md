# Brief bake-off — Pass 15, brief-method evaluation

Set 2026-09-23 by the user: "not part of claude skills, but a real evaluation report … part of this project … final step of this project research". Registered in `../plan.md` "Pass sequence — addition 2, 2026-09-23". Status: **not run**.

One question:

> Which brief-writing method turns this programme's evidence into a document a cold director reads in 10 minutes, without a single invented number?

Method: same input, same instruction, ten agents. Each follows one external brief-writing method; one follows the user's own template (control). Each writes one brief into its own folder. A blind judge scores all ten; the user scores them second. The compiled read lands in `docs/findings/`.

## Read first

1. `../../../CLAUDE.md` — repo rules. Agents never run git. Research only.
2. `../../CLAUDE.md` — folder scopes. Runs write here, under `method/`; the finding goes to `findings/`.
3. `../plan.md` §"Pass sequence — addition 2, 2026-09-23" — gate.
4. `../STATE.md` — cap in force; add queue row `P15-brief-eval` before spawning.
5. This file, then `shared-instruction.md`, `baseline-template.md`, `scoresheet.csv`.

## Method sources — provenance

External methods are source material, pulled 2026-09-23, kept outside `docs/` in `.claude/skill-candidates/<repo>/` (untracked; two are unlicensed and may not be vendored). Re-clone at the recorded commit to re-run.

| repo | origin | commit | last commit | license | quoting in `docs/` |
|---|---|---|---|---|---|
| pyramid-principle | github.com/tyroneross/pyramid-principle | e6c6a12 | 2026-09-07 | Apache-2.0 | verbatim OK, attribute |
| minto-pyramid-skill | github.com/millwright-labs/minto-pyramid-skill | 49d1f58 | 2026-08-16 | MIT | verbatim OK, attribute |
| awesome-claude-corporate-skills | github.com/w95/awesome-claude-corporate-skills | 78dbc7c | 2026-02-26 | MIT | verbatim OK, attribute |
| business-consulting | github.com/abinauv/business-consulting | 8808ffb | 2026-02-28 | MIT | verbatim OK, attribute |
| claude-skill-management-consultant-B1 | github.com/DogInfantry/claude-skill-management-consultant-B1 | 97e1db7 | 2026-09-21 | Apache-2.0 | verbatim OK, attribute |
| strategyu-skills | github.com/paulmil11/strategyu-skills | 538df2e | 2026-09-20 | **none** | path:line + paraphrase ≤12 words only |
| strategy-skills-for-claude | github.com/aapersh/strategy-skills-for-claude | 1a6fdf6 | 2026-09-08 | **none** | path:line + paraphrase ≤12 words only |

```
git clone <origin> .claude/skill-candidates/<repo> && git -C .claude/skill-candidates/<repo> checkout <commit>
```

## Input — identical for every run

- Failed brief: `../../findings/director-brief-2026-09-23.md` (293 lines, 144 table rows, one hop from raw). If BRIEF-4 has landed, the failed brief stays the input; BRIEF-4's output is judged as run R10, no agent spawned.
- Evidence: `../../findings/*.md`, `../../markets/*.md`, `../../competitors/INDEX.md`, `../../customers/*.md`, `../../raw/` — read-only, cite by path.
- Tier scale: `../trust-rubric.md`.
- Known failures of the input, cold-reader audit 2026-09-23, **for the judge only**: no one-sentence answer; no why-now; process leaks (pass numbers, H-codes, folder names); risks unranked; ask is research-admin; tier scale undefined in-file; positives rest on vendor marketing while tier-2 filings all read negative; platform capture never named as a risk.

Agents are not told the failure list.

## Runs

`SC` = `D:\researchs\market-research-2026-09-22\.claude\skill-candidates`.

| id | folder | operating instruction the agent reads | note |
|---|---|---|---|
| R0 | `runs/R0-baseline` | `baseline-template.md` | control — user's template, no external method |
| R1 | `runs/R1-pyramid-principle` | `SC\pyramid-principle\skills\pyramid-principle-core\SKILL.md`, `pyramid-long-form\SKILL.md`, `pyramid-source-integrity\SKILL.md`, their `references\` | substitute `${CLAUDE_PLUGIN_ROOT}` → `SC\pyramid-principle`; audit skill not loaded |
| R2 | `runs/R2-minto-pyramid` | `SC\minto-pyramid-skill\SKILL.md` | single file |
| R3 | `runs/R3-strategy-communicator` | `SC\strategyu-skills\strategyu-skills-claude\strategy-communicator\SKILL.md` | unlicensed source |
| R4 | `runs/R4-structure-synthesize` | `SC\strategyu-skills\strategyu-skills-claude\structure-synthesize\SKILL.md` | unlicensed source |
| R5 | `runs/R5-knowledge-synthesis` | `SC\awesome-claude-corporate-skills\01-executive-leadership\knowledge-synthesis\SKILL.md` | — |
| R6 | `runs/R6-deliverable-creation` | `SC\business-consulting\skills\deliverable-creation\SKILL.md` + `references\` | ignore the repo's hook persona |
| R7 | `runs/R7-decision-memo` | `SC\strategy-skills-for-claude\skills\06-alignment-and-executive-communication\decision-memo.md` | unlicensed source |
| R8 | `runs/R8-assumption-audit` | `SC\strategy-skills-for-claude\skills\01-diagnosis-and-framing\assumption-audit.md` | audit-shaped method forced to write; expect a different form |
| R9 | `runs/R9-mbb-extract` | `SC\claude-skill-management-consultant-B1\skill\references\`: `pyramid-principle-and-scqa.md`, `board-communication-and-decision-support.md`, `output-craft.md`, `hypothesis-invalidation-discipline.md` | never load its `skill\SKILL.md` — 15k tokens, "never reveal provenance" rule contradicts root `CLAUDE.md` |
| R0b | `runs/R0b-baseline-repeat` | as R0 | run-to-run variance floor; a method effect smaller than R0−R0b is noise |
| R10 | `runs/R10-brief4` | none — copy of BRIEF-4's `director-brief-<date>.md` | only if BRIEF-4 landed; judged, not spawned |

Spawn: `general-purpose`, one model for all (record id), background. Waves of the cap in force, R0–R4 first. Deliverable globs disjoint per spawn.

Per-agent prompt = `shared-instruction.md` verbatim with three substitutions: `{RUN_ID}`, `{OUT_DIR}` (absolute), `{SKILL_FILES}` (absolute paths, one per line). Nothing else differs. Paste, never paraphrase.

## Output contract — `runs/<id>/`

| file | holds | cap |
|---|---|---|
| `brief.md` | the director brief | 1,200 words body; appendix and glossary excluded |
| `notes.md` | model id, timestamp; what the method forced that the agent would not have done unaided (rule quoted or, unlicensed, path:line + paraphrase); every override of the method by a constraint, rule and constraint named; what the method was silent on | 300 words |
| `trace.md` | `number | brief line | repo path:line | source kind | source date`, one row per number in `brief.md` | none |

Agent returns five lines: run id · body words · trace rows · `unknown` count in brief · override count.

## Judge

One `general-purpose` agent, no method file. Orchestrator copies each `brief.md` to `judge/blind/<letter>.md`, map in `judge/map.csv` (letter, run id); judge never sees the map. Judge writes one row per letter into `scoresheet.csv`, `scorer=judge`:

| col | test | scale |
|---|---|---|
| headline | one disputable sentence, first line, repeatable to the director's boss | 0–3 |
| why_now | dated external triggers as complication, not inventory of work done | 0–3 |
| process_leak | pass numbers, H-codes, repo paths, "what we did" in body | count, lower better |
| heading_assert | headings that argue ÷ all headings | fraction |
| tiers_defined | evidence scale defined in-file before first use, mapped to how it was used | 0–2 |
| risks_ranked | ordered on a stated criterion; decision-changing risk beside the answer | 0–3 |
| platform_capture | engines selling ads or checkout themselves named as a threat | 0/1 |
| negative_tail | tier-2 filings (referral collapse) carried as headline signal, not footnote | 0/2 |
| ask | what, options, if-approved / if-deferred, or explicit "no decision" | 0–3 |
| invented | numbers with no trace row, or trace row pointing nowhere; judge spot-checks 10 rows per brief | count; any >0 fails the run |
| verdict_push | brief tells the director go/no-go | 0/−2 |
| glossary | every acronym defined | 0/1 |
| words | body word count | number |
| cold_read | after 10 minutes the judge can state what · why now · size · who · kill · ask | 0–6 |

Judge also writes `judge/verdict.md`: rank; one line per run on what its method visibly added or broke; the single rules behind the top-3 differences, quoted per the provenance table's quoting column. Judge reads the failure list above only after scoring.

## Human comparison

User scores every letter on the same columns, `scorer=human`, R0 first. Then `judge/human-notes.md`:

1. Which brief would you send? Why over R0?
2. Which one rule would you add to `baseline-template.md`? Quote or cite it.
3. Which rule fought the repo — invented numbers, pushed a verdict, hid unknowns?

Rows where judge and human disagree by ≥2 are the read.

## Deliverable — `../../findings/brief-method-eval-<date>.md`

Per `../templates/finding.md`, 100 lines, Lane E. Its "evidence" is the scoresheet and `trace.md` files, cited by path; its "raw" is `runs/`. It reports: the rank both ways; the R0−R0b variance floor; per-method rules that added or broke, with quoting per provenance; which methods produced an `invented` count above zero; what none of them fixed. Survivorship: "not case-based". It does not pick a method for the user; it states what each did.

Downstream, reporting layer only: the final rewrite of `findings/executive-brief-<date>.md` and `findings/director-brief-<date>.md` cites this finding for the rules it adopts. No skill is created in `.claude/` as a pass deliverable; that is tooling, outside research scope.

## Rules that bind every run

- Agents never run git. Main thread commits `docs/method/brief-bakeoff/` and the finding on master after each wave.
- Runs write only inside their own `runs/<id>/`. Nothing else under `docs/` is touched by a run.
- No web in runs. Input is the repo. This tests the method, not research ability.
- One model, one instruction text, one input, one day. Model id and timestamp in every `notes.md`.
- One method per agent. An agent that reads another candidate's files invalidates its run; rerun under a new id.
- Unlicensed method text (StrategyU, aapersh) is never copied into `docs/`. Cite path:line, paraphrase ≤12 words.
- `SC\pyramid-principle\commands\submit-feedback.md` runs `gh issue create`. Never executed.

## Caveats

- Ten single runs; R0b is the only variance measure. A rank gap inside the R0−R0b spread is not a result.
- Judge is one model reading briefs written by the same model family. Human scores exist to bound that bias.
- The failed input is one document. A method that wins here won on this evidence base and this reader; the finding says so.
- External methods were read at the commits above. Later commits are not this evaluation.

## Amendments, 2026-09-23 — before any run

Per `../biz-review-2-bakeoff-2026-09-23.md`. Nothing above is edited.

- Input snapshot: the orchestrator pins one commit hash here at spawn (`snapshot: <hash>`); every run and the judge read that tree; compiled files appended after it are not input. Line ranges in `shared-instruction.md` Addition 1 are filled from the pinned tree.
- `shared-instruction.md` Addition 1 (evidence pack as required second read; constraints 11–16) is part of the identical text every run receives.
- Judge note: trace rows pointing at `STATE.md` or `plan.md` line numbers count as "pointing nowhere" (column `invented`); those files are appended all day.
- Open owner decisions recorded in `../STATE.md` §Open decisions, not decided here: whether column `negative_tail` is rubric or thumb (README L92 vs the side-by-side rule); whether sub-market choice is a permissible ask; importance order over the 32 hypotheses.
- snapshot: 8badc05 (evidence tree; the bake-off method files themselves are as of the commit that follows it). Pinned 2026-09-23 by the main thread at P15 spawn. R10 = `docs/findings/director-brief-2026-09-23-r2.md` (BRIEF-4, landed f78a7a1), copied into `runs/R10-brief4/brief.md` at judge time; runs are told not to open `-r2` files (shared-instruction Addition 2).
- Wave plan under cap 8: wave 1 R0, R0b, R1, R2, R3, R4, R5, R6; wave 2 R7, R8, R9; then judge.
