# RankPrompt — Owings Auto case study

```yaml
source:          Rank Prompt — case study page "The work behind the visibility numbers" (Owings Auto entry)
url_or_doc_id:   https://rankprompt.com/case-studies/
published:       undated — no date on page
pull_date:       2026-09-22
pull_method:     browser extension (claude-in-chrome, own dedicated tab)
pull_purpose:    evidence about a number
tier:            6
tier_reason:     discloses explicit numeric baselines across three separate sub-metrics including an answer-count denominator (a form of sample size), but no absolute date window and no independent measurer — vendor case study without full method disclosure; this IS RankPrompt's dedicated case-study page, captured in full by Pass 3 as well, re-pulled today independently per this task's instructions
source_label:    vendor-reported
lane:            E
sub_market:      organic recommendation
engine:          "6 AI engines" stated as the fixed set tracked; not itemized by name on this specific case page
metric_kind:     visibility — AI visibility rate, local ranking, and a mention-count/denominator metric ("answers naming Owings")
supersedes:      none
captured:        full page (the entire case-studies page, which is itself the dedicated case-study format — two case narratives on one URL)
vertical:        Automotive · Fort Worth, TX — RankPrompt's own tag on the page
evidence_grade:  Bronze (full-page, on this pull). All seven bar items evaluated below.
pass3_grade:     Bronze (from `docs/raw/a-vendor-census-c1-2026-09-22.md`, sourced from this same URL — `docs/raw/a-rankprompt-customers-2026-09-22.md`, which already captured this as the full page)
paid_by_outcome: unknown — quote below
prompt_set_disclosed: no — "fixed prompts" is stated as the method but no n of prompts and no prompt wordings are published
```

## Verbatim

Page header: "CASE STUDIES — The work behind the visibility numbers — Every study here runs on the same weekly reports the product ships: fixed prompts, six AI engines, one score per market."

**Automotive · Fort Worth, TX**

"Owings Auto — 141 days · 6 AI engines"

"Owings Auto runs two lots fourteen miles apart. Assistants recommended one of them constantly and the other almost never. The weekly reports showed why, and in 141 days the weaker market passed the home one."

Stat blocks (verbatim, before → after):
- "Fort Worth AI visibility: 13.3% → 54.2%"
- "Rank in the local field: #12 of 247 → #2"
- "Answers naming Owings: 16 of 120 → 65 of 120"

Page footer CTA: "FREE AI VISIBILITY REPORT. NO CREDIT CARD REQUIRED. — See where your own markets stand — Track every location, product line or region separately across six AI engines, on prompts that never change."

## Pull notes — mechanical only

- Fetched via `claude-in-chrome` browser extension (connected this session), `get_page_text` on a dedicated new tab (tabId 1697684063) opened for this task, in the same call that captured the Humand case above. Full page captured in one call, reached the footer CTA, no truncation.
- This URL (`rankprompt.com/case-studies/`) is RankPrompt's own dedicated case-study page — there is no separate, deeper per-case URL for Owings Auto on this vendor's site. Pass 3 (`docs/raw/a-rankprompt-customers-2026-09-22.md`) already captured this same page in full; this pull independently re-fetched it today via the browser extension and confirms identical content.
- "141 days" is a duration, not an absolute start/end calendar date.
- "16 of 120" and "65 of 120" is the most concrete sample-size disclosure of any case pulled in this task — a denominator (120 answers evaluated) is explicit, even though the prompt wordings behind those 120 answers are not published.
- The "two lots fourteen miles apart" framing implies a natural comparison (the stronger lot, described as staying roughly constant) but the page never gives that lot's own before/after numbers — so no control metric is actually disclosed, only implied by the narrative.
- No named measurer beyond RankPrompt's own weekly-report product; no statement of whether RankPrompt or Owings Auto was paid by, or measuring, this outcome on any performance basis.

## Evidence bar — seven items, evaluated against this full page

| # | Item | Present / Absent | Quote |
|---|---|---|---|
| 1 | Brand, or credibly specified anonymised profile | **Present** | "Owings Auto runs two lots fourteen miles apart..." |
| 2 | The engine or engines | **Partial** | "6 AI engines" — a count is given, but not itemized by name on this specific case page |
| 3 | The date window, absolute | **Absent** | "141 days" — a duration, not a start/end calendar date |
| 4 | The baseline before intervention | **Present** | "Fort Worth AI visibility: 13.3% → 54.2%"; "Rank in the local field: #12 of 247 → #2"; "Answers naming Owings: 16 of 120 → 65 of 120" |
| 5 | The intervention itself | **Partial** | "The weekly reports showed why" — RankPrompt's tracking is described as revealing the visibility gap between the two lots; no separate named content or optimization intervention beyond the tracking itself |
| 6 | The sample size, or the traffic volume | **Present** | "16 of 120" / "65 of 120" — 120 answers evaluated is an explicit denominator, the most concrete n of any case pulled this task |
| 7 | Who measured, and whether they were paid by the outcome | **Absent** | Not stated — self-published by Rank Prompt, no named independent auditor, no statement on paid-by-outcome |

**Full-page grade: Bronze.** Visibility/ranking-only claim, with explicit before/after numbers across three sub-metrics and the strongest sample-size disclosure (120 evaluated answers) of any case pulled in this task. Still Bronze, not Silver: no absolute date window is disclosed, and while a natural comparison group is implied ("the stronger lot"), its own before/after numbers are never given — so no unaffected control metric is actually disclosed, only implied by the narrative framing.

**Grade change vs. Pass 3: same (Bronze → Bronze).** Pass 3 graded this case Bronze from the same URL (`docs/raw/a-rankprompt-customers-2026-09-22.md`), already treating it as the full case-study page and noting explicitly that it came closest to Silver of any case in that cluster without clearing it. This independent re-pull via the browser extension confirms identical content and the same grade and reasoning.
