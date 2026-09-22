# RankPrompt — customers / case studies

```yaml
source:          Rank Prompt (rankprompt.com)
url_or_doc_id:   https://rankprompt.com/case-studies
published:       undated — no date on page
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            6
tier_reason:     case studies carry explicit before/after numeric baselines (unusual for this cluster) but no absolute date window, no independent measurer, and no named unaffected control metric — marketing claims without full method disclosure; the existence of the two named customers is a tier-3 vendor-page fact
source_label:    vendor-reported
lane:            A
sub_market:      organic recommendation
engine:          n/a
metric_kind:     visibility
supersedes:      none
captured:        full page
```

## Verbatim

<p>AI Visibility Case Studies | Rank Prompt</p>

Case studies

# The work behind the visibility numbers

Every study here runs on the same weekly reports the product ships: fixed prompts, six AI engines, one score per market.

B2B SaaS · HR technology

## Humand
2 markets · 6 AI engines

Humand raised $66M, part of it to fund a move into the United States, where AI assistants had never named the company once. Twenty-two weekly reports later the new market is at 18%, and the home market has doubled alongside it.

US AI visibility: 0% → 18.0%
Argentina AI visibility: 24% → 48.0%
Argentina citation share: 4.0% → 11.3%

Automotive · Fort Worth, TX

## Owings Auto
141 days · 6 AI engines

Owings Auto runs two lots fourteen miles apart. Assistants recommended one of them constantly and the other almost never. The weekly reports showed why, and in 141 days the weaker market passed the home one.

Fort Worth AI visibility: 13.3% → 54.2%
Rank in the local field: #12 of 247 → #2
Answers naming Owings: 16 of 120 → 65 of 120

Free AI visibility report. No credit card required.

## See where your own markets stand
Track every location, product line or region separately across six AI engines, on prompts that never change.
Start free analysis / View pricing

[footer identical to other RankPrompt pages, omitted here — see `a-rankprompt-pricing-2026-09-22.md`]

## Pull notes — mechanical only

- Fetched via plain fetch tool (raw=false, markdown-simplified HTML). Browser extension unavailable this session.
- Only 2 case studies published on this page — the smallest case-study count of any vendor pulled so far in this cluster, but the most numerically detailed: both give explicit before-and-after figures across multiple named sub-metrics (visibility percentage, citation share, local rank position, count of answers naming the brand out of a stated denominator), unlike every other vendor's case-study pages pulled this session, which give only a single top-line percentage or multiplier with no baseline number.
- "Humand raised $66M" is stated as background context for the case (funding used partly to fund US market entry), not itself part of the AI-visibility claim being measured.
- Duration given as relative counts ("Twenty-two weekly reports", "141 days"), not absolute calendar dates — no start or end date is stated for either case.

## Case studies screened on intake — evidence-bar grading

Per `docs/method/plan.md` evidence bar (seven items: 1 brand, 2 engine, 3 absolute date window, 4 baseline, 5 intervention, 6 sample/traffic size, 7 who measured/paid-by-outcome) and `docs/method/glossary.md` grades.

| Case, as published | Brand | Engine | Date window | Baseline | Intervention | Sample size | Who measured | Missing items | Grade |
|---|---|---|---|---|---|---|---|---|---|
| Humand | Yes | Yes — "6 AI engines" (the platform's standard set: ChatGPT, Perplexity, AI Mode, Claude, Gemini, Grok per the homepage) | No — "Twenty-two weekly reports" is a count/duration, not an absolute start/end date | **Yes, explicit** — 0% → 18.0% (US), 24% → 48.0% (Argentina visibility), 4.0% → 11.3% (Argentina citation share) | Yes — "weekly reports" / Rank Prompt's own tracking product | Partial — "2 markets", no prompt count or n of responses given | Not stated (self-published by Rank Prompt; no named independent auditor) | date window, sample/prompt n, who-measured (3 of 7 — the fewest missing items of any case study graded in this cluster so far); no separately-disclosed unaffected control metric, so short of Silver's explicit bar | Bronze — visibility-only claim; baseline is present (unusually complete for this cluster) but the missing absolute date and missing named control keep it below Silver |
| Owings Auto | Yes | Yes — "6 AI engines" | No — "141 days" is a duration, not an absolute date | **Yes, explicit** — 13.3% → 54.2% (visibility), #12 of 247 → #2 (local rank), 16 of 120 → 65 of 120 (answers naming the brand) | Yes — weekly reports / Rank Prompt | Partial — "2 lots", 120 answers evaluated (a form of n, the most concrete sample size disclosed by any case study in this cluster) | Not stated | date window, who-measured (2 of 7 — the fewest missing items of any case study graded in this cluster) | Bronze — visibility/ranking-only claim; strong baseline+n disclosure but still short of Silver without an absolute date and a named unaffected control metric |

**Totals: 2 case studies screened. 0 cleared Gold. 0 cleared Silver (both are close — explicit baseline and, for Owings Auto, an explicit n — but neither discloses an absolute date window, an independent measurer, or a metric held constant as an explicit control). 2 graded Bronze. 0 screened-not-pulled.**

## Caveats

- These are the most evidence-complete case studies found in this cluster to date (explicit baseline numbers, and for Owings Auto an explicit answer-count denominator) — still graded Bronze, not Silver, strictly because no absolute date window and no independently-measured or explicitly-labelled "unaffected control" metric is disclosed. This is a judgment call applying `plan.md`'s Silver definition ("baseline plus an unaffected control metric") conservatively: Owings Auto's two-lot comparison implies a natural control (the stronger lot, described as staying "constant") but does not give that lot's own before/after numbers, so no control metric is actually disclosed.
- "Humand raised $66M" is recorded as background/company-context in this file; it is not itself graded as a funding record for Humand (Humand is RankPrompt's customer, not one of the eight vendors in this census).
