# Notes — R8 assumption-audit

Model: claude-opus-5-5[1m]. Timestamp: 2026-09-23T18:11Z (machine clock).
Fresh run; evidence read only from the fact pack and the failed brief at snapshot 8badc05.

## What the method made me do

Method file (unlicensed; paraphrase only): `.claude/skill-candidates/strategy-skills-for-claude/skills/01-diagnosis-and-framing/assumption-audit.md`, cited below by line.
- `:18`, name the plan under audit: framed a hypothetical product as the proposition.
- `:19–20`, extract assumptions and sort by category: register table with a Category column.
- `:22`, pick the load-bearing ones: three picked, not scored.
- `:51`, include unstated assumptions: added the two engine-behaviour rows.

## Overrides (constraint wins)

1. `:21` and `:34`, score importance: dropped. Constraint 15; the column shows repo tier instead.
2. `:34`, risk column: dropped from the register. Constraint 15; risks use the repo's own ranking, with "no source states one".
3. `:23`, `:41–43`, `:53`, test plan with owner and trigger: dropped. Constraints 6 and 15; replaced by "where the evidence stops".
4. `:45–46`, verdict to proceed, pause or redesign: replaced by the evidential answer. Constraints 7 and 11.
5. `:54`, action if an assumption fails: dropped. Constraints 6 and 7.

## Method silent on

Dating, source labels, conflicting figures, sizing, "why now", word budget, and who the reader is. Handled by constraints 4, 5, 9, 14.

## Audience assumptions (constraint 12)

- Stance neutral; no decision wanted; no priorities. Asked nothing of the reader.
- Reader knows no acronyms or project terms; glossary in the appendix.
- Reader wants the six questions in the order given; section order follows them.
- Figures stay in the currency and units the source used.
- A figure without its own date carries the pull date (2026-09-22 or 2026-09-23), stated in the header.

## Other

Trace kinds marked "(assigned)" were absent from the pack row; assigned from its source.
