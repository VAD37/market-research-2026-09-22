# Notes — R0b

Models: first draft `<synthetic>` (Fable-limited run, per `prior-attempt-digest.md`); partial finish `claude-opus-5-5`; this finish `claude-opus-5-5[1m]`. Finished 2026-09-23T17:36Z (system clock, UTC).
Resumed from the prior draft `brief.md`; all evidence re-read and re-verified from the 8badc05 snapshot.

Body: 1,179 words, raw `wc -w` on lines 1–85, tables included.

## What the template made me do

- Full-sentence section titles and nine-part order (`docs/method/brief-bakeoff/baseline-template.md:7–18`).
- "Market — … budget line it steals from" (`:9`): searched filings, found Coty, eHealth and HubSpot as nearest lines.
- "Unknowns — … cost to close" (`:13`): added a cost column.
- "early signal" (`:12`): added an early-signal column from the risk register.
- "Test per section: 'so what?'" (`:17`): cut a decision option about which sub-market to choose.

## Overrides

1. "Risks — kill-shots first. Likelihood, impact, early signal, mitigant" (`:12`): ranked by evidence tier as the repo does; likelihood, impact and mitigant = "no source states one" (constraints 2, 15).
2. "Decision / ask — options with tradeoffs" (`:14`): no options or tradeoffs, only two open readings (constraints 7, 11, 12).
3. "Headline — one sentence answer" (`:7`): gives the evidential reading, not an action (constraint 11).
4. "cost to close" (`:13`): "unknown — not in repo" where no price exists (constraints 3, 15).
5. "where hypothetical product could sit" (`:10`): the repo's open question, no placement (constraints 2, 6).

## What the template did not cover

Conflicting figures, two readings (strict/loose, R1/R2), source kinds, absolute dates, the word cap, negative evidence, glossary depth.

## Audience assumptions (constraint 12)

- Stance neutral, no decision wanted, no stated priorities.
- The reader knows ChatGPT, Gemini, Copilot and Claude by name but not GEO/AEO, VLOSE or tier scales.
- Ten minutes of reading ≈ the 1,200-word body.
- Dollar and euro figures are carried unconverted.
