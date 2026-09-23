# Shared instruction — identical for every run. Only {RUN_ID}, {OUT_DIR}, {SKILL_FILES} differ.

You are run {RUN_ID}. Write to {OUT_DIR} only. Do not run git. Do not use the web. Do not read any file under `.claude/` except the ones listed below. Do not read any other folder under `docs/method/brief-bakeoff/`.

## Operating instruction

Read these files first and treat them as your method for this task. Follow them where they do not conflict with the constraints below; where they conflict, the constraints win and you record the conflict in notes.md:

{SKILL_FILES}

## Situation

A director will read one document for 10 minutes. They have never heard of this project, this market, or any of its acronyms. They want: what is this, why now, how big, who is already there, what could kill it, what do you want from me.

The existing document written for them failed. It is `D:\researchs\market-research-2026-09-22\docs\findings\director-brief-2026-09-23.md`. Read it fully. It is your primary source. Everything it cites lives under `D:\researchs\market-research-2026-09-22\docs\` — `findings/`, `markets/`, `competitors/`, `customers/`, `raw/`. You may read any of those to check or strengthen a figure. Evidence tier scale: `docs/method/trust-rubric.md` — lower tier number is stronger.

The subject: whether real demand exists, per segment, for brand visibility and product recommendation inside AI assistants (ChatGPT, Gemini, Perplexity, Copilot, Claude), and what evidence shows it works. The programme is research only — it produces evidence, not a go/no-go. The verdict belongs to the reader.

## Task

Write the document the director should have received. Save as `{OUT_DIR}\brief.md`.

## Constraints (win over the operating instruction)

1. Every number in brief.md exists in a repo file. Record each in `{OUT_DIR}\trace.md` as `number | brief line | repo path:line | source kind | source date`. A number you cannot trace does not go in.
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

`{OUT_DIR}\notes.md`, max 300 words:
- Model id and timestamp.
- What the operating instruction made you do that you would not have done unaided. Quote the rule with its file path and line.
- Every place you overrode the operating instruction because of a constraint above. Quote the rule, state the constraint.
- What the operating instruction had no opinion on that mattered here.

## Return

Five lines: run id · body word count · rows in trace.md · count of "unknown" entries in brief.md · count of overrides in notes.md.