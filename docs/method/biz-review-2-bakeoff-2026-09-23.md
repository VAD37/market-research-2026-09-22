# Business-analyst review 2 — what the bake-off methods and judge demand, and what the repo supplies

Task REV-BIZ-B, 2026-09-23. Read-only, 0 pulls, no git, no web. Paths relative to `docs/`; `SC` = `.claude/skill-candidates`. Line numbers as read 2026-09-23 ~13:30 while COMPILE-2, P16-c1…c4 and REPULL-1 were appending; every repo cite is file:line, every "method demands" cell is a cited method line, every "should" is `reviewer judgment`. Unlicensed methods (R3, R4, R7, R8) are cited path:line and paraphrased ≤12 words, never quoted. Rows already in `biz-review-1-2026-09-23.md` (REV-A) are referenced, not repeated. No market number is introduced.

Method keys: R1c `SC/pyramid-principle/skills/pyramid-principle-core/SKILL.md`; R1l `…/pyramid-long-form/SKILL.md`; R1k `…/pyramid-long-form/references/report-skeleton.md`; R1s `…/pyramid-source-integrity/SKILL.md`; R1t `…/pyramid-source-integrity/references/strict-trace.md`; R2 `SC/minto-pyramid-skill/SKILL.md`; R3 `SC/strategyu-skills/strategyu-skills-claude/strategy-communicator/SKILL.md`; R4 `…/structure-synthesize/SKILL.md`; R5 `SC/awesome-claude-corporate-skills/01-executive-leadership/knowledge-synthesis/SKILL.md`; R6 `SC/business-consulting/skills/deliverable-creation/SKILL.md`; R6s `…/references/consulting-writing-style-guide.md`; R7 `SC/strategy-skills-for-claude/skills/06-alignment-and-executive-communication/decision-memo.md`; R8 `…/01-diagnosis-and-framing/assumption-audit.md`; R9p `SC/claude-skill-management-consultant-B1/skill/references/pyramid-principle-and-scqa.md`; R9b `…/board-communication-and-decision-support.md`; R9o `…/output-craft.md`; R9h `…/hypothesis-invalidation-discipline.md`. BA = `brief-bakeoff/baseline-template.md`; SI = `brief-bakeoff/shared-instruction.md`; RM = `brief-bakeoff/README.md`.

## 1. Method × input demand matrix

Quality: **C** complete, **P** partial, **A** absent, **X** forbidden by SI constraints (method slot must be overridden). Add = what BRIEF-4 or an append must supply; "gap n" points to §4.

| Run | Input demanded (method line) | Repo file that supplies it now | Q | Add |
|---|---|---|---|---|
| R0 §1 | One-sentence answer the director repeats (BA:7) | `findings/executive-brief-2026-09-23.md:15` (five sentences); `director-brief:18` | P | REV-A row 1; negative tail now at `proof-scorecard.md:246–278` supplies the tier-2 side |
| R0 §2 | Three dated world changes, not work done (BA:8) | `findings/trigger-timeline.md:23–76`, 54 events, 26 at tier 2 | C | Timeline has no so-what column by design (L17); brief adds the inference, labelled |
| R0 §3 | Size range + method, growth, buyer, budget line, grade per number (BA:9) | `findings/market-potential.md:20–70`; buyer `demand-map.md:23–36, 148–170` | P | Budget line `unknown` (`organic-recommendation.md:38`, `paid-placement.md:47`; P16-c1 live); grade = tier column, present |
| R0 §4 | What exists, gaps, where a hypothetical sits (BA:10) | `competitors/INDEX.md:14–56`; `whitespace.md:21–34`; `frontier-scan.md:31–45` | P | Cross-sub-market supply table, gap 10 |
| R0 §5 | Proven / inferred / assumed table (BA:11) | `proof-scorecard.md:180–244` three-count; `glossary.md:55–60`; `trust-rubric.md:9–17` | C | Two readings R1/R2 (`proof-scorecard.md:182`); classes undefined in glossary, gap 4 |
| R0 §6 | Kill-shots first; likelihood, impact, early signal, mitigant (BA:12) | `whitespace.md:93–111`, 11 ranked rows, criterion at L95 | C | Likelihood and mitigant absent by design (L95); state absence, gap 9 |
| R0 §7 | What is missing, why, cost to close (BA:13) | `unknowns.md:82–93`; `method/blocked-channels.md`; every file's unknowns table | C | REV-A row 17 |
| R0 §8 | Options with trade-offs, or explicit no decision (BA:14) | `director-brief:273–282`; `STATE.md:213` (R1/R2 owner method decision) | P | No consolidated open-decision list with if-deferred consequence, gap 12 |
| R0 §9 | Glossary of every acronym; sources graded (BA:15) | `glossary.md`; `trust-rubric.md`; raw tier lines | P | 30 of 35 acronyms the failed brief uses undefined, gap 3 |
| R1 | Reader question stated first (R1l:30; R1k:22–33) | SI:13 names six reader wants | C | — |
| R1 | Governing thought supplied by user, never strengthened (R1l:31, :72) | none — SI:31 forbids a verdict; no evidential answer sentence exists | A | Owner text defining what fills the slot, gap 5 |
| R1 | Cleared claims: source, exact locator, confidence word, reason, must-preserve scope (R1l:32; R1s:25–31, :62–69) | Every compiled row: label, tier, raw path, window; e.g. `paid-placement.md:155–164` | P | No High/Medium/Low word; tier→confidence mapping is an owner choice; trace by raw path:line (raw lines never move) |
| R1 | Low-confidence claims out of central support (R1s:37–40) | Every positive Silver is tier 5 (`proof-scorecard.md:293`); negatives tier 2 | C | Method effect to expect: positives leave the body under R1; record in notes.md |
| R1 | Claim packet with source register, IDs, contradicted list (R1t:13–25); closed set adds no risk, urgency, next step (R1t:38) | No packet file; risks now cleared via `whitespace.md:93–111`, dates via timeline | P | BRIEF-4 could emit trace.md in packet shape; "urgency" stays an inference |
| R1 | SCQA complication = a dated change (R1c:98; scqa-pattern.md:43–52); asserted headings (R1k:250–300) | `trigger-timeline.md:23–76` | C | — |
| R2 | Gate: document asks reader to accept a judgment (R2:16–18) | MegaPlan.md:17 — no verdict; evidence read only | A | Without gap 5 text the agent may stop or invent a judgment |
| R2 | Answer sentence; SCQA no longer than the answer (R2:54–68); decisive risk beside the answer (R2:85, :142) | `whitespace.md:99` rank-1 referral collapse | P | Answer sentence as R0 §1 |
| R2 | Invent nothing, including arithmetic on source numbers (R2:12, :89) | SI:25–26 same rule | C | Rounding undefined, gap 8 |
| R3 | Reader role, stance, decision wanted, time, priorities (R3:23–29); sequencing chosen from stance (R3:41–69) | SI:13 gives role and time only | P | Stance, decision wanted, priorities absent; agents cannot ask, gap 7 |
| R3 | One emotional lever per document (R3:121–135); close with owner and date (R3:178) | none; SI:30 forbids owners and dates | X | Lever choice risks `verdict_push`; override in notes.md |
| R3 | Output states sequencing choice, lever, weak sections (R3:221–224) | SI silent on where method commentary goes | A | Routing rule to notes.md, gap 6 |
| R3 | Every claim carries number, name or source (R3:261) | every compiled table | C | — |
| R4 | Gather everything in one place (R4:19–23); eliminate by whether the recommendation changes (R4:27–33) | No single pack file; §3 proposes one | P | Elimination test presupposes a recommendation, gap 5 |
| R4 | Two–three MECE themes, rule of three (R4:48–66, :107–114) | Three sub-markets (`scope.md:21–25`), three metrics (`glossary.md:9–16`) | C | Natural groupings exist |
| R4 | Required output: labelled data, groups, pyramid visual, validation (R4:167–175); so-what ends in budget action (R4:118–124) | analysis artefact, not a brief; action forbidden SI:30 | X | Route to notes.md, gap 6 |
| R5 | Source type, location, date, author per claim (R5:90–99); conflicts surfaced, never silently picked (R5:149–162) | every compiled row; SI:28 | C | — |
| R5 | Confidence by freshness, >1 month = lower (R5:107–112); authority by document kind (R5:117–127) | Repo uses tier (`trust-rubric.md:9–17`) and one-quarter staleness (`glossary.md:106`) | A | Instruction: tier replaces freshness and authority tables |
| R5 | Dedup: prefer most complete, authoritative, recent (R5:53–60) | Repo keeps both when one fact carries two tiers (REV-A §4 row 8) | X | Carry both; SI:28 wins |
| R5 | Large-set summary ending with an offer to dig deeper (R5:191–208) | chat form, no brief form | A | Note only |
| R6 | SCR with Resolution = recommendation (R6:26–30); "We recommend" not "We think" (R6s:5) | none | X | gap 5 |
| R6 | Exec summary: context, 3–5 findings each with implication (R6:109–112); assumptions separated from facts (R6:157) | Findings files; `method/hypotheses.md:16–40, 115–125` as the assumption list | C | Implication = inference; label it |
| R6 | Decision memo: options, 3–5 criteria, mitigations, next steps with owner and date (R6:200–230) | none | X | Options table without execution, gap 10 |
| R6 | Number formatting $XXM, one decimal, en-dash ranges (R6s:84–98); client-centric "$ opportunity for client" (R6s:11) | Figures verbatim, e.g. `market-potential.md:44` "$224,532M"; no client | A | Rounding rule, gap 8; the "client" is the hypothetical (`MegaPlan.md:22`) |
| R7 | Recommendation paragraph; decision required (R7:30–34) | none; open decisions scattered | A | gaps 5, 12 |
| R7 | Options with upside, trade-off, verdict per option (R7:39–41); next steps after approval (R7:49–50) | none; per-option verdict forbidden SI:31 | X | gap 10 |
| R7 | Context why now (R7:36–37); evidence; risks and mitigations; economics (R7:21, :43–47) | timeline; `proof-scorecard.md`; `whitespace.md:93–111`; floors `market-potential.md:56–62` | P | Mitigations absent by design; WTP unknown 27 of 27 (`demand-map.md:195`) |
| R8 | Strategy being tested (R8:30–31) | `MegaPlan.md:22` guiding hypothetical | C | — |
| R8 | Assumption register with category, importance, evidence strength, risk (R8:33–35); load-bearing ones ranked (R8:37–39) | `hypotheses.md` 32 rows by lane; marks `unknowns.md:188–225`; strength = tier | P | Importance never assigned, gap 11 |
| R8 | Test plan with owner and decision trigger (R8:41–43); proceed / pause verdict (R8:45–46) | Kill and confirm conditions `hypotheses.md:48–72, 131–141` serve as triggers, no owner | X | Verdict forbidden; triggers exist |
| R8 | Implicit assumptions, not only stated (R8:51) | Only registered H exist | A | Owner: whether to register implicit ones |
| R9 | SCQA templates carrying $ and "we recommend" (R9p:69–98); title stack test (R9p:143) | complication from timeline; recommendation forbidden | P | gap 5 |
| R9 | Strategic KPIs with RAG trend (R9b:57–60) | Engine counts only (`market-potential.md:22–32`); brand-side series absent (P16-c4 live) | A | Write `unknown`; no RAG colouring |
| R9 | Top-5 risks with likelihood, impact, mitigation, owner; heatmap (R9b:73–80) | Rank only (`whitespace.md:97–109`) | P | gap 9 |
| R9 | Decision item: options, recommendation, if approved / if not approved (R9b:86–101) | none; matches judge `ask` (RM:93) | A | gap 12 |
| R9 | Exec summary with implementation, impact, investment (R9o:59–82); financial number plus its key assumption (R9o:201) | $1B run rate `paid-placement.md:25`; floors `market-potential.md:58–62` | P | Implementation and investment forbidden; write `unknown — not in repo` |
| R9 | Steelman alternative, assumption ladder, weakest link (R9h:51–84); evidence log consistent vs inconsistent (R9h:163) | Kill conditions ≈ pre-mortem (R9h:39–49); negative tail + positives `proof-scorecard.md:246–291` | P | Steelman and ladder absent; owner or one append |
| R9 | Confidence calibration high/medium/low per claim (R9h:165); finding before recommendation when evidence contradicts (R9h:145) | Tiers per claim; negative tail supports the second | C | Mapping as R1 |

Tally, 47 rows: complete 14, partial 16, absent 10, forbidden 7. Seven forbidden slots are the same three things — a recommendation, an option verdict, an owner-dated next step — so one instruction line (gap 5) covers them.

## 2. Judge column × repo supply

| Column (RM line) | File that lets a brief score | Exists | Missing |
|---|---|---|---|
| headline (85) | `executive-brief:15`; `proof-scorecard.md:246–278` negative tail | partial | One sentence; REV-A row 1 |
| why_now (86) | `trigger-timeline.md:23–76` | yes | Seven tier-2 rows "not carried" by any compiled file (L25, 31, 34, 61, 65) — usable, uncorroborated by a second compiled read |
| process_leak (87) | none needed; every pack file is pass- and H-coded | n/a | Translation burden on the agent; appendix rule, gap 13 |
| heading_assert (88) | none needed | n/a | — |
| tiers_defined (89) | `trust-rubric.md:9–17`; `glossary.md:55–60` | partial | Classes a/b/c and R1/R2 only at `plan.md:146–155`, `proof-scorecard.md:182`, gap 4 |
| risks_ranked (90) | `whitespace.md:93–111`, criterion L95, rank 1 = decision-changing | yes | Likelihood absent by design |
| platform_capture (91) | `whitespace.md:102` rank 4; `frontier-scan.md:36`; `paid-placement.md:90` | yes | — |
| negative_tail (92) | `proof-scorecard.md:246–278`, 19 rows at tier ≤3 | yes | Column prescribes the headline, gap 14 |
| ask (93) | `director-brief:273–282`; `STATE.md:213` | partial | If-deferred consequence nowhere, gap 12 |
| invented (94) | raw files (837 as read) with tier lines | partial | Trace convention: line cites into `STATE.md`/`plan.md` rot, gap 2; rounding, gap 8 |
| verdict_push (95) | `MegaPlan.md:17` | yes | — |
| glossary (96) | `glossary.md` | no | 30 of 35 acronyms undefined, gap 3 |
| words (97) | none needed | n/a | Counter unspecified; agent self-reports |
| cold_read (98) | §3 pack entries 1–12 map to what · why now · size · who · kill · ask | yes | Ask is the weak leg |

Supplied: 7 complete, 3 partial, 1 absent, 3 need no file.

**Invented spot-check, 15 rows of the failed brief.** Test per RM:94: does the cited compiled line still hold the number, and does a raw file carry it. Raw existence checked by `ls`; figure grep-verified in rows 2, 3, 7, 9, 11, 13.

| # | Brief line, number | Cited path | Compiled line holds it | Raw carries it | Result |
|---|---|---|---|---|---|
| 1 | L47 $5.3M–$35.2M floor | `organic-recommendation.md:36` | yes | `raw/a-vendor-census-c1…c4-2026-09-22.md` exist | traced |
| 2 | L66 "$1 billion… run rate" | `paid-placement.md:25` | yes | `raw/b-openai-1bn-run-rate-milestone-2026-09-22.md:25` | traced |
| 3 | L73 "$3–$5 USD per click" | `whitespace.md:23` | yes | `raw/b-openai-platform-summary-2026-09-22.md` exists | traced |
| 4 | L74 26% · 4.47% · 0.00% | `paid-placement.md:26–28` | yes | three raws exist | traced |
| 5 | L83 Copilot "does not take a commission" | `agentic-commerce.md:25` | yes | `raw/b-microsoft-agentic-commerce-2026-09-22.md` | traced |
| 6 | L89 VLOSE 159.1M | `whitespace.md:33` | yes | `raw/b-eu-dsa-ad-repositories-table-2026-09-22.md` | traced |
| 7 | L93 "83-93% drops" | `paid-placement.md:97` | yes | `raw/a-court-mdl-microsoft-ctr-data-2026-09-22.md:27` | traced |
| 8 | L103 Profound $180M at $1.8B | `organic-recommendation.md:28` | yes | `raw/a-vendor-census-c1-2026-09-22.md` | traced |
| 9 | L111 Semrush $38M AI ARR | `competitors/INDEX.md:39` | yes | `raw/a-semrush-filing-2026-09-22.md:37` | traced |
| 10 | L145 ~980 screened | `proof-scorecard.md:75` | yes | measured-by-us sum; `raw/e-case-census-c13-2026-09-22.md` | traced |
| 11 | L163 NerdWallet "decreased 24%" | `proof-scorecard.md:32` | yes | `raw/e-case-nerdwallet-earnings-release-2026-02-25-2026-09-22.md:37` | traced |
| 12 | L174 content ops 63 | `transition-evidence.md:56` | yes | tally over rows L22–50, each with raw | traced |
| 13 | L56 IAB 76% | `organic-recommendation.md:38` | yes | `raw/e-market-size-iab-paid-2026-09-22.md:35` | traced |
| 14 | L64 ~53% · 79.4% · 34.80% | `method/plan.md L146, L168` | **no** — L146 now evidence-quality text; figures at `plan.md:183, 205` | raws exist | points nowhere |
| 15 | L195 6 techniques + 1, ~70 pulls | `method/STATE.md L99` | **no** — L99 now P6-organic row; figure at `STATE.md:108` | census raws exist | points nowhere |

13 of 15 trace; 2 point nowhere because `plan.md` (AMEND-2) and `STATE.md` were edited mid-file after BRIEF-3. The brief cites `STATE.md` 21 times; all 9 distinct line numbers checked (33, 54, 83, 89, 94, 99, 112, 127, 198) now hold a different row. Rows 1 and 10 also carry figures superseded by dated appends (`market-potential.md:60`; `proof-scorecard.md:112`) — traced, stale, not invented.

## 3. Input shaping — `reviewer judgment` throughout

**Evidence pack — twelve reads, this order.** Chosen so every method finds headline, why-now, size, supply, evidence ladder, risks, unknowns and ask without opening 40 files.

| # | File:lines | Gives |
|---|---|---|
| 1 | `method/scope.md:7–25`; `method/glossary.md:9–16, 30–38` | what: market, three sub-markets, three metrics never crossed |
| 2 | `method/trust-rubric.md:9–17`; `method/glossary.md:55–60, 83`; `method/plan.md:146–155` | tier, grade, demand-read and evidence-class scales |
| 3 | `findings/trigger-timeline.md:17–76` | why now: 54 dated events |
| 4 | `findings/market-potential.md:14–70, 97–100` | size three ways; floors; forecast spreads |
| 5 | `findings/ai-ads-evidence.md:16–33`; `markets/paid-placement.md:143–151` | paid supply: who sells, prices published |
| 6 | `competitors/INDEX.md:12–58`; `markets/organic-recommendation.md:23–38` | who is there: 41 profiles; disclosure ratios |
| 7 | `markets/agentic-commerce.md:19–32, 83–92` | agentic supply, fees, gates |
| 8 | `findings/demand-map.md:148–170`; `customers/*.md` cell tables | who buys: latest 27-cell tallies, both readings |
| 9 | `findings/proof-scorecard.md:180–244, 246–293` | evidence ladder; negative tail beside positives |
| 10 | `findings/transition-evidence.md:14–15, 52–61, 133–142` | what movers changed; three-count of 108 |
| 11 | `findings/whitespace.md:21–34, 93–111` | gaps; ranked risks with platform capture |
| 12 | `findings/unknowns.md:82–93, 175–186, 188–225`; `method/blocked-channels.md` | unknowns, tier-3 share six ways, 32 H marks |

**Contradictions the pack carries as read** (COMPILE-2 will list the full set; these are the ones a brief writer meets inside entries 1–12): tier-3 share 68.0% / 44.4% / 44.0% (`unknowns.md:55, 179–184`); Silver 7 raw / 1 rule-1, then +4 / +1 (`proof-scorecard.md:17, 113`); cells 7·1·11·8 vs strict 8·1·17·1 vs loose 8·1·18·0 (`demand-map.md:17, 165–166`); organic floor $5.3M–$35.2M vs $42.2M–$48.2M + €2.2M (`organic-recommendation.md:36`; `market-potential.md:60`); agentic spread ~35× vs 26.3× (`agentic-commerce.md:54`; `market-potential.md:54`); engines selling ads "5 of 8" vs "four" (`paid-placement.md:39`; `ai-ads-evidence.md:18`); ChatGPT ad presence 0.8% to 26%, five figures (`paid-placement.md:157–160`); advertisers "tens of thousands" vs 820–7,378 (`ai-ads-evidence.md:24`); three-count R1 10/29/13 vs R2 5/34/13 and 6/61/37 vs 1/66/37 (`proof-scorecard.md:235–236`; `transition-evidence.md:135–136`); "99 of 108 name a change, no metric" vs 67 metric-moved (`transition-evidence.md:15, 142`); H6, H7, H9 dual marks (`unknowns.md:225`); hypotheses 23 vs 32 (`director-brief:8`; `unknowns.md:225`); CTR drops "83-93%" vs "87% to 93%" inside one exhibit (`paid-placement.md:97`).

**Cap.** 1,200 words fits: the executive brief body runs 853 words over 22 metric rows (`wc`, L11–59); the director brief body 4,243. A body of ~20 numbers plus six 150-word legs lands near the cap; the appendix, uncounted (SI:33), takes the pairs above. The risk runs the other way — R6/R9 sections (implementation, investment, RAG) would spend words on `unknown`.

**Primary source.** Keep the failed brief as the input RM:39 contracts, so R10 is comparable — but make the pack a required second read, not an optional check (SI:15 "you may read"). Otherwise runs that go looking score on diligence, not method, on `why_now`, `risks_ranked`, `platform_capture`, `negative_tail`, all of which the failed brief lacks and the repo now holds. The failed brief's path column must not be inherited: 21 of its `STATE.md` and `plan.md` cites now point elsewhere (§2).

**Proposed text for SI, owner to paste** (replaces nothing; appended after L34 as constraints 11–16 and after L15 as a read list):

> Read next, in order, and treat as the same input as the failed brief: [pack entries 1–12 with line ranges]. Input snapshot is commit `<hash>`; cite nothing newer.
> 11. The answer slot every method demands (governing thought, recommendation, resolution, verdict) carries the evidential answer to the reader's question — what the evidence supports and stops — never a course of action. Where a method's gate asks whether the reader must accept a judgment, the judgment is that reading.
> 12. Audience fields: stance neutral; decision wanted: none, the reader decides; priorities: none stated. You cannot ask; record every assumption in notes.md.
> 13. Method commentary the operating instruction requires (sequencing choice, emotional lever, MECE groups, pyramid visual, self-checks) goes to notes.md, never brief.md.
> 14. When one figure carries two readings or two dates, the body carries the later-dated figure with its reading label (strict/loose, raw/rule-1, R1/R2) and names that another reading exists; the appendix carries the pair with both dates and paths. Neither is dropped.
> 15. A rounded, re-unitised or converted number is arithmetic. Carry the figure as the repo states it. Likelihood, impact, mitigation and owner: write "no source states one".
> 16. trace.md cites `raw/` path:line, or a compiled file plus row id (E1, C1, T1, rank 1). Never a `STATE.md` or `plan.md` line number. Repo paths may appear in the appendix, never in the body. The return-line `unknown` count includes both `unknown — not in repo` and `unknown — checked`.

## 4. Gaps REV-A did not list

| # | Gap | Where | Closing task |
|---|---|---|---|
| 1 | No pinned input snapshot; compiled files are appended during the run day, so "one input" (RM:123) is not one | RM:37–42, :123 | owner decision: commit hash in RM; runs cite it |
| 2 | Failed brief's `STATE.md`/`plan.md` line cites rot: 9 of 9 checked hold other rows; §2 rows 14–15 | `director-brief:24–36, 64, 195–200, 208, 240–247` | BRIEF-4: raw path:line or row ids only; RM judge note |
| 3 | 30 of 35 acronyms the brief uses undefined: VLOSE, DSA, AIO, CPC, CPM, ARR, MAU, WAU, DAU, ACP, UCP, AP2, MCP, CTR, CMA, FTC, CFR, GSC, ROAS, CAGR, 8-K, 10-K, S-1 … | `glossary.md:1–119` (grep 2026-09-23) | append (COMPILE-2 adds two rows only, solution §2) |
| 4 | Evidence classes a/b/c and the R1/R2 readings live only in `plan.md:146–155` and appends; `tiers_defined` needs them in-file | `proof-scorecard.md:182`; `glossary.md` silent | glossary append; BRIEF-4 defines in-file |
| 5 | Seven method slots demand a recommendation or option verdict; SI says constraints win but not what fills the slot; R2's gate may refuse the document | R1l:31, :72; R2:16–18; R6:26; R7:30–34; R8:45; R9b:94; SI:23–34 | owner text, §3 item 11 |
| 6 | Methods require self-commentary in the output; SI has no routing rule; judge counts it as leak | R3:221–224; R4:167–175; R1c:32; RM:87 | owner text, §3 item 13 |
| 7 | Audience stance, decision wanted, priorities absent; background agents cannot ask | R3:23–29; R9b:31–35; R1l:36; SI:13 | owner text, §3 item 12 |
| 8 | Rounding and re-formatting undefined against constraint 2 and judge `invented` | R6s:84–98; R3:289; SI:26; RM:94 | owner decision; §3 item 15 |
| 9 | Likelihood, impact, mitigation, owner demanded; register carries none by design; methods will supply words like "likely" that R1s:44 treats as claims | R9b:73–80; R7:46–47; BA:12; `whitespace.md:95` | owner text, §3 item 15 |
| 10 | No cross-sub-market table: demand cells, proof grade, supply count and disclosure, floor, risk rank per sub-market — the only "options" a research brief can carry | pieces at `market-potential.md:66–70`; `demand-map.md:165–166`; `proof-scorecard.md:237–240`; `organic-recommendation.md:25–30`; `paid-placement.md:39`; `agentic-commerce.md:22–26`; `whitespace.md:99–109` | one compile append, ~6 rows; owner decides whether sub-market choice is a permissible ask |
| 11 | No importance or load-bearing order over the 32 hypotheses against the guiding hypothetical | `hypotheses.md:16–40, 115–125` list by lane; R8:37–39; R9h:63–84 | owner decision (importance is judgment) or reviewer-labelled append |
| 12 | Open owner decisions scattered, none with an if-deferred consequence; judge `ask` wants one | `STATE.md:213`; `director-brief:277–281`; credentials `STATE.md:135`; RM:93 | append "open decisions" table to `STATE.md` |
| 13 | Body bans file names (SI:32) but BA §9 wants sources graded; judge tests leak "in body" (RM:87) — appendix status unstated | SI:32; RM:87; BA:15 | owner text, §3 item 16 |
| 14 | Judge column prescribes which signal is the headline while the repo keeps readings side by side | RM:92; `proof-scorecard.md:293`; `CLAUDE.md` conflicts rule | owner decision: rubric or thumb; `verdict.md` states it |
| 15 | Return-line `unknown` count undefined: repo phrase `unknown — checked`, SI phrase `unknown — not in repo` | SI:27, :45 | owner text, §3 item 16 |

Top 5 by effect on the bake-off: 1, 5, 2, 6, 3.

## 5. Caveats

- Lines as read 2026-09-23 ~13:30; five agents were appending. `unknowns.md`, `INDEX.md`, `market-potential.md`, `glossary.md` (COMPILE-2) and `customers/*.md` (P16) may have moved below the lines cited; appends land at file end, so cites above the last read line hold.
- Method files read in full: all nine runs' listed files, plus R1 references `report-skeleton.md`, `strict-trace.md`, `scqa-pattern.md`, `llm-adaptation.md` and R6 `pyramid-principle-deep-dive.md`, `slide-templates.md`. Not read: R1 `rules-of-pyramid.md`, `mece-grouping.md`, `vertical-horizontal-logic.md`, `key-line-examples.md`, `docs/source-anchors.md`; never `claude-skill-management-consultant-B1/skill/SKILL.md`. Which method line binds is `reviewer judgment`.
- Spot-check: raw existence by `ls` for all 15; figure grep inside six raws; the rest rest on the compiled line's raw path. The 41 profiles and ~830 raw bodies were not opened.
- Tallies in §1–§2 are counts of this file's own rows, not repo facts. Effort words are shapes (append / one pass / owner decision), never dates.
- Research only: no verdict on the market, no method picked for the user, no market number introduced; every figure quoted is cited to the file that holds it.
