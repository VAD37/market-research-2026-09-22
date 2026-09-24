# R1 deck notes

Model claude-opus-5-5[1m]; 2026-09-24T03:18Z.

## Method made me

- Put the governing thought on its own early slide: "State the governing thought before evidence." (`pyramid-presentation/SKILL.md:50`)
- Make every title a claim: "Can the audience agree or disagree with it?" (`references/slide-headline-rules.md:23`)
- Group by inference: "Section dividers name the inference, not the data source." (`references/storyline-patterns.md:159`). Body slides carry "Finding n" tags.
- Skip speaker notes: "Do not add design, speaker notes, or framework commentary unless requested." (`SKILL.md:42`)

## Overrides (3)

1. "Implications" and "Recommended next steps" (`storyline-patterns.md:153,155`); "Which decision, recommendation, or finding" (`SKILL.md:31`). Constraint 5: the closing slide states what the evidence supports and where it stops. It asks for nothing.
2. "SECTION DIVIDER | Finding 1: full assertion" (`storyline-patterns.md:147`). Constraint 7: dividers would break the 20-slide cap, so tags replace them.
3. "appending the packet's claim ID to every factual or evaluative headline" (`SKILL.md:62`). Constraints 1, 4, 6: no IDs on slides; trace lives in trace.md plus trace-deck.md.

Tension: the governing thought keeps "shows", which `slide-headline-rules.md:86` calls weak. "Preserve the cleared claim." (`SKILL.md:51`) wins.

## Storyline vs brief.md

- Why-now moved before the governing thought as the Complication. Its tier labels are dropped because tiers are defined on slide 5.
- R1/R2 renamed experimental/observational reading because R1 collides with the run id (constraint 6).
- Appendix without repo paths or census codes; source-file appendix cut.
- Closing question/evidence/limit slide added.
- QA removed unsupported "largest" and "weaker tiers dominate".

## QA

3 rounds. Read could not render the PDF (no pdftoppm), so I checked Chrome screenshots of the same HTML at the same page size. PDF has 21 pages. Nothing is left unfixed beyond spare whitespace on some slides.
