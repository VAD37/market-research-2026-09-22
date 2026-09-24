# R0 deck notes

Model `claude-opus-5-5[1m]`; 2026-09-24T10:30+0700. Control run: method = baseline-template.md plus own judgment.

## What the template made me do

- "Section titles are full-sentence takeaways: reading titles alone gives the whole story" (baseline-template.md:18): every slide title states the finding.
- "Evidence ladder — proven / inferred / assumed. Explicit. Table." (:11): slide 13 table.
- "Or explicit 'no decision'" (:14): slide 18.
- "Appendix — glossary (every acronym), sources graded, method, raw tables" (:15): appendices A–C.

## Overrides

1. "Headline — one sentence answer" (:7) — deck constraint 5: answer slide states where evidence stops, no action.
2. "Confidence grade per number" (:9) — constraint 4: kind and date in footer; tier inline, no separate grade.
3. "Likelihood, impact, … mitigant" (:12) — constraint 3: "no source states one".
4. "options with tradeoffs" (:14) — constraint 5: three readings the director owns, no lean.
5. "where hypothetical product could sit" (:10) — constraint 5: gaps labelled hypotheses, not plans.

## Storyline changes from brief.md

- Order: answer slide before definitions; tiers withheld from slide 2, defined on slide 4 (constraint 6).
- Split: market into floors / forecasts / growth / buyers / budget line (slides 6–10); solution space into vendors / engines.
- Promoted to main: budget-line filings (appendix in brief); evidence-quality chart with the 2026-09-22 reading beside.
- Renamed "R1/R2 reading" to "experimental/observational reading" (constraint 6, no codenames).
- Charts: forecasts on a log axis, labels verbatim, horizons 2034 vs 2030 flagged.

## QA

Route: PyMuPDF PNG render of the real PDF, every page read. 2 rounds. Round 1 fixed: date hyphen wraps, label hit by 80% line, sub-14 pt kicker/meta text, one "success cases" wording. PDF 23 pages = 18 main + 5 appendix. No defect left unfixed.
