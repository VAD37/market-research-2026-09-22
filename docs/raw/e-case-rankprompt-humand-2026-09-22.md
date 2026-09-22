# RankPrompt — Humand case study

```yaml
source:          Rank Prompt — case study page "The work behind the visibility numbers" (Humand entry)
url_or_doc_id:   https://rankprompt.com/case-studies/
published:       undated — no date on page
pull_date:       2026-09-22
pull_method:     browser extension (claude-in-chrome, own dedicated tab)
pull_purpose:    evidence about a number
tier:            6
tier_reason:     discloses an explicit numeric baseline and a stated engine count, but no absolute date window and no independent measurer — vendor case study without full method disclosure; this IS RankPrompt's dedicated case-study page (not a separate customers-overview page), captured in full by Pass 3 as well, re-pulled today independently per this task's instructions
source_label:    vendor-reported
lane:            E
sub_market:      organic recommendation
engine:          "6 AI engines" stated as the fixed set the product tracks (RankPrompt's homepage names ChatGPT, Perplexity, Google AI Mode, Claude, Gemini, Grok as its standard six per `docs/raw/a-rankprompt-customers-2026-09-22.md`'s note; this specific case page names only "6 AI engines" as a count, not itemized per-case)
metric_kind:     visibility — AI visibility rate and citation share (both vendor-defined sub-metrics, tracked per market)
supersedes:      none
captured:        full page (the entire case-studies page, which is itself the dedicated case-study format — two case narratives on one URL, no separate per-case URL exists on this vendor's site)
vertical:        B2B SaaS · HR technology — RankPrompt's own tag on the page
evidence_grade:  Bronze (full-page, on this pull). All seven bar items evaluated below.
pass3_grade:     Bronze (from `docs/raw/a-vendor-census-c1-2026-09-22.md`, sourced from this same URL — `docs/raw/a-rankprompt-customers-2026-09-22.md`, which already captured this as the full page)
paid_by_outcome: unknown — quote below
prompt_set_disclosed: no — "fixed prompts" is stated as the method but no n of prompts and no prompt wordings are published
```

## Verbatim

Page header: "CASE STUDIES — The work behind the visibility numbers — Every study here runs on the same weekly reports the product ships: fixed prompts, six AI engines, one score per market."

**B2B SaaS · HR technology**

"Humand — 2 markets · 6 AI engines"

"Humand raised $66M, part of it to fund a move into the United States, where AI assistants had never named the company once. Twenty-two weekly reports later the new market is at 18%, and the home market has doubled alongside it."

Stat blocks (verbatim, before → after):
- "US AI visibility: 0% → 18.0%"
- "Argentina AI visibility: 24% → 48.0%"
- "Argentina citation share: 4.0% → 11.3%"

Page footer CTA: "FREE AI VISIBILITY REPORT. NO CREDIT CARD REQUIRED. — See where your own markets stand — Track every location, product line or region separately across six AI engines, on prompts that never change."

## Pull notes — mechanical only

- Fetched via `claude-in-chrome` browser extension (connected this session), `get_page_text` on a dedicated new tab (tabId 1697684063) opened for this task. Full page captured in one call, reached the footer CTA, no truncation.
- This URL (`rankprompt.com/case-studies/`) is RankPrompt's own dedicated case-study page — there is no separate, deeper per-case URL for Humand on this vendor's site (confirmed by the page's own structure: two case narratives, no "read more" links to individual case pages). Pass 3 (`docs/raw/a-rankprompt-customers-2026-09-22.md`) already captured this same page in full; this pull independently re-fetched it today via the browser extension (Pass 3 used plain fetch, browser extension unavailable in that session) and confirms identical content.
- "Humand raised $66M" is background context (why the company entered the US market), not itself part of the AI-visibility claim.
- Duration given only as a count ("Twenty-two weekly reports"), not an absolute calendar date range.
- No named measurer beyond RankPrompt's own weekly-report product; no statement of whether RankPrompt or Humand was paid by, or measuring, this outcome on any performance basis.

## Evidence bar — seven items, evaluated against this full page

| # | Item | Present / Absent | Quote |
|---|---|---|---|
| 1 | Brand, or credibly specified anonymised profile | **Present** | "Humand raised $66M, part of it to fund a move into the United States..." |
| 2 | The engine or engines | **Partial** | "6 AI engines" — a count is given, but not itemized by name on this specific case page |
| 3 | The date window, absolute | **Absent** | "Twenty-two weekly reports later" — a count of reports, not a start/end calendar date |
| 4 | The baseline before intervention | **Present** | "US AI visibility: 0% → 18.0%"; "Argentina AI visibility: 24% → 48.0%"; "Argentina citation share: 4.0% → 11.3%" |
| 5 | The intervention itself | **Partial** | Implied — RankPrompt's weekly tracking reports are described as revealing the visibility gap, but no separate content or optimization intervention is described beyond "twenty-two weekly reports" of tracking itself |
| 6 | The sample size, or the traffic volume | **Absent** | "2 markets", no prompt count or count of AI responses evaluated given for this case |
| 7 | Who measured, and whether they were paid by the outcome | **Absent** | Not stated — self-published by Rank Prompt, no named independent auditor, no statement on paid-by-outcome |

**Full-page grade: Bronze.** Visibility-only claim (AI visibility percentage, citation share), with an explicit numeric baseline — unusually complete for this category — but missing an absolute date window, a disclosed sample size, and any named or independent measurer. No unaffected control metric is disclosed (no untreated market or competitor tracked as a constant comparison), so this does not clear Silver despite the explicit before/after numbers.

**Grade change vs. Pass 3: same (Bronze → Bronze).** Pass 3 graded this case Bronze from the same URL (`docs/raw/a-rankprompt-customers-2026-09-22.md`), already treating it as the full case-study page. This independent re-pull via the browser extension confirms identical content and the same grade.
