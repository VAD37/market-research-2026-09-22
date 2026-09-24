# Deck notes — R0b

Model `claude-opus-5-5[1m]`. Finished 2026-09-24T03:26Z (system clock, UTC).

## What the method made me do

Control run: method is `docs/method/brief-bakeoff/baseline-template.md`.
- "Section titles are full-sentence takeaways: reading titles alone gives the whole story" (`:18`): every main slide title is a sentence.
- "Evidence ladder — proven / inferred / assumed. Explicit. Table." (`:11`): kept as a table slide, then added a chart slide of evidence classes.
- "Appendix — glossary (every acronym), sources graded, method, raw tables" (`:15`): seven appendix slides.

## Overrides

1. "Risks — kill-shots first. Likelihood, impact…" (`:12`): ranked by evidence tier; likelihood, impact, mitigant "no source states one" (brief constraint 15; deck constraint 5).
2. "Decision / ask — options with tradeoffs" (`:14`): two evidence readings only, no options (deck constraint 5).
3. "Headline — one sentence answer" (`:7`): evidential reading, not an action (deck constraint 5).
4. "where hypothetical product could sit" (`:10`): "open; no evidence addresses it" (deck constraint 5).
5. "Appendix — … sources graded" (`:15`): repo paths dropped from slides; they live in the trace files (deck constraints 4, 6).

## Storyline changes from brief.md

- Order kept; answer slide added up front, tier and grade slide moved before first use (deck constraint 6).
- "R1 / R2" relabelled "control as experimental / observational"; "rule 1" as "strict seven-item bar" (no codenames).
- Risk rows 7–11 gained early signals from the risk register's early-signal column.
- Market section split into four slides.

## QA

Route: PyMuPDF PNG render of the real PDF (Read tool could not open PDF, no pdftoppm). 3 render-and-review rounds; 26 pages = 26 slides. Fixed: row labels clipped by bars, axis-end labels over markers, in-bar caption clipped, SVG labels under 14 pt. Unfixed: slides 12 and 19 leave lower third empty.
