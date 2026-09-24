# R6 deck notes — deliverable-creation

Model `claude-opus-5-5[1m]`; 2026-09-24 (system date). Fact pack read once (F658–F667) to confirm the six 80%-bar counts.

## What the method made me do

- Governing thought first: "State the single most important message" (`commands/strategy-deck.md:13`) → slide 3 title and answer box.
- Action titles: "A sentence that states the conclusion (not the topic)" (`strategy-deck.md:27`) → every slide title is a claim.
- Agenda after title (`slide-templates.md:14–16`); exec summary with "**bolded lead-in phrase**" (`slide-templates.md:21`).
- Key-finding chart with source note (`slide-templates.md:27`) → six hand-built SVG charts.
- "Label the data directly on the chart" (`chart-selection-guide.md:148`); "always start the value axis at zero" (`chart-selection-guide.md:50`); one message per chart (`:142`).

## Overrides (7)

1. "Resolution: What should the client do?" (`strategy-deck.md:18`) → deck constraint 5: answer box states where evidence stops.
2. "recommendation callout box" (`slide-templates.md:21`) → constraint 5: no recommendation.
3. Next Steps "Action Item | Owner | Deadline" (`slide-templates.md:96`) → constraint 5: slide 20 frames reading choices as options.
4. "blue for recommended" option (`slide-templates.md:33`) → constraint 5: options uncoloured.
5. Title "18-20pt", body "11-12pt" (`slide-templates.md:117–118`) → constraint 8: 25 pt titles, 14–19 pt body.
6. Source note "8pt" and page number "8pt" (`slide-templates.md:119, 123`) → constraint 8: 11 pt footer.
7. "Confidential — prepared for [Client Name]" (`slide-templates.md:124`) → constraint 6 (no codenames) plus research-only: footer carries source kinds instead.

## Storyline changes from brief.md

Tier/grade slide precedes first use (constraint 6); exec summary avoids tier words. Engines split into three slides. Appendix A loses repo paths (constraint 6).

## QA

3 rounds. No PDF rasterizer (pdftoppm absent); checked per-slide Chrome screenshots of the same HTML; PDF confirmed 31 pages, 960×540 pt. Fixed: clipped "Unchecked" labels, 80%-line overlapping labels, clipped chart note, agenda count, glossary heading. No known defect left.
