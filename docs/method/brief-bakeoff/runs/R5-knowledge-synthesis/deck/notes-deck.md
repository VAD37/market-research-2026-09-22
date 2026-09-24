# R5 deck notes

Model `claude-opus-5-5[1m]`, 2026-09-24. BMP = `.claude/skill-candidates/awesome-claude-corporate-skills/01-executive-leadership/board-meeting-prep/SKILL.md`; DV = same root, `10-data-analytics/data-visualization/SKILL.md`.

## What the method made me do
- BMP L75 "Agenda overview": added an agenda slide.
- BMP L138 "Include speaker notes for every slide": `speaker-notes.md`.
- BMP L264 "List 15-20 tough questions directors might ask": questions appendix. Wrote 8.
- BMP L134 "One idea per slide": the brief's proof section became four slides.
- DV L253 "Title states the insight": every title is a finding.
- DV L268 "Bar charts start at zero: Always."
- DV L278 "Never rely on color alone": labels on marks.

## Overrides
1. BMP L71 "25-35 slide deck". Constraint 7: 20 main slides plus 6 appendix slides.
2. BMP L109–110, severity and mitigation. Constraints 5 and 15: "no source states one".
3. BMP L141, red/yellow/green indicators. Constraint 8, plus no source for severity.
4. BMP L55, L292, action items and owners. Constraint 5.
5. BMP L188 "time-bound commitments". Constraint 5.
6. BMP L135 "18pt+ body". Constraints 3 and 7 forced 14.5–16 pt tables. The constraint 8 floor holds.
7. DV L272 "Label your axes": no numeric ticks, because ticks cannot be traced (constraint 1). The scale is stated in words.
8. BMP L74 "logo": build rules allow no images.

## Storyline changes from brief.md
- Added a slide defining tiers and grades before first use (constraint 6).
- Gave audience scale its own slide.
- Renamed readings for a cold reader (Reading 1/2; "as first graded", "strict rule").
- Removed the appendix paths. The sources list became a slide on how the evidence was built.
- Answer and order are unchanged.

## QA
2 rounds. Fixed a clipped "roughly 35×" label, an axis overlapping a label, and 13 pt badges. No known defect remains.
