# R4 deck notes

Model `claude-opus-5-5[1m]`, 2026-09-24T03:21Z. Method: `.claude/skill-candidates/strategyu-skills/strategyu-skills-claude/strategy-slides/SKILL.md` (unlicensed; paraphrased).

## What the method made me do

- L48: titles state the takeaway, never a label.
- L100: no pie charts. All charts are bars.
- L166–168: summary slide, main point plus three insights (slide 2).
- L132: main message three times (slides 1, 2, 20).
- L213–215: risk titles name the risk, not a count.
- L80, L174: no section dividers in short decks.

## Overrides

1. L22, L266–279: ask about audience and style. Can't ask (brief constraint 12); system fonts per Build rule.
2. L108, L146: allows illustrative charts. Overridden by deck constraint 2: charts show traced values only.
3. L206–210: close with actions, owners and deadlines. Overridden by deck constraint 5: the close gives options with evidence.
4. L126, L134: pick an emotional lever and plant action triggers. Overridden by deck constraint 5 and a neutral stance: none used.
5. L398–442: build a .pptx with python-pptx. Overridden by the Build rule: HTML rendered to PDF.

## Storyline changes from brief.md

- "Who is already there" became three slides (ads, checkout, tool vendors). "Proof" became four.
- Added a chart of forecast spreads (slide 7).
- Relabelled R1/R2 as Reading A/B because they read as internal codes (deck constraint 6).
- Replaced "Five of eleven" with the rank numbers, and "Seven of 54" with "a selection". Neither is a repo count.
- Each option on the last slide now carries its evidence.

## QA

Four rounds. Read could not rasterise the PDF (no pdftoppm); checked per-slide Chrome screenshots of the same HTML; PDF confirmed 24 pages, 960×540 pt. Fixed: clipped legend and label (slides 14, 7), sparse type (body to 17 pt), duplicate wording (slide 13), over-reaching "Read" lines. Nothing known is left unfixed.
