# R9 deck notes

Model: claude-opus-5-5[1m]. Timestamp: 2026-09-24T03:27Z.

## What the method made me do

- Sentence titles on every slide: "Every chart needs a message title, not a topic title." (`data-visualization.md:9`)
- Axis units and zero baselines stated under each chart: "Every axis is labeled with units." (`data-visualization.md:59`); "Always start bar charts at zero." (`:125`)
- Paired figures and risks 8–11 moved to the appendix: "Put the full table in the appendix." (`data-visualization.md:123`)
- The ask on slide 2 and again near the end: "State the decision request on slide 1. Repeat it on the final slide." (`board-communication-and-decision-support.md:213`)
- No speaker notes: "Design the pack for pre-reading." (`board-communication-and-decision-support.md:129`).

## Overrides (5)

1. Risk heatmap and "likelihood, potential impact, current mitigation, risk owner" (`board-communication-and-decision-support.md:74`, `:78`). Constraints 1–2: no source states likelihood; no heatmap.
2. "We are asking the board to approve [X] today" (`board-communication-and-decision-support.md:174`). Constraint 5: options, no request.
3. Implementation slides (`output-craft.md:33`) and next steps. Constraint 5: none.
4. "Being presented options when you should have a recommendation" (`output-craft.md:208`). Constraint 5.
5. Full source note under each chart (`data-visualization.md:61`). Constraint 4: kind and date only.

## Storyline changes from brief.md

- Risks: the brief showed 7. The register ranks 11, so the title says eleven and ranks 8–11 go in the appendix.
- R1/R2 renamed "Reading 1/2" (constraint 6: not run codes).
- Situation and complication share one slide. Added: a 27-cell grid, a provenance-tier ladder, "18 figures, 15 forecasts, 0 measured", and "0 Gold; 0 of 15".

## QA

2 rounds. Route: PyMuPDF renders PDF pages to PNG, then Read (the Read tool has no pdftoppm). 22 pages for 22 slides. Round 1 fixed clipped SVGs (slides 14, 16), stretched tables, two overclaiming titles. Unfixed: lower-third whitespace on several slides.
