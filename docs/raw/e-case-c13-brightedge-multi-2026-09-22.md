# BrightEdge — five AI-visibility case-study pages, full-page re-grade under grading rule 1 (not covered by P4-c4)

```yaml
source:          BrightEdge (brightedge.com) — five dedicated case-study pages, URLs per section
url_or_doc_id:   https://www.brightedge.com/resources/case-studies/{ninjaone-ai-mentions-case-study,riskonnect-ai-share-of-voice-case-study,bloomfire-agent-edge-case-study,arm-agent-edge-case-study,overdrive-interactive-achieves-ai-overview-growth-brightedge}
published:       undated on all five pages
pull_date:       2026-09-22 (NinjaOne, Riskonnect, Bloomfire pulled by P3-c4 under this same date; Arm and Overdrive Interactive newly opened this pull)
pull_method:     fetch (curl, browser User-Agent header — P3-c4 pull for the first three; WebFetch for Arm and Overdrive Interactive, this pull)
pull_purpose:    evidence about a number
tier:            6
tier_reason:     downgraded from table default 5 — vendor-authored case studies, BrightEdge (the vendor selling the AI-visibility feature) is the measuring party on all five, no independent replication, per trust-rubric.md "vendor measuring the thing it sells"
source_label:    vendor-reported
lane:            E
sub_market:      organic recommendation
engine:          varies per case — see table
metric_kind:     visibility (share of AI mentions/citations, AI Overview rankings/mentions); traffic (AI agent traffic, AI referral traffic)
supersedes:      none
captured:        full page, each of the five
pass3_cluster:   a-vendor-census-c4 (Part A row 1, BrightEdge) — "5 identified / 3 opened and graded, 2 screened-not-opened"
pass3_grade:     Bronze (NinjaOne, Riskonnect, Bloomfire, all three already full-page-graded at P3-c4 with items considered but not itemised as a formal seven-item checklist); screened — not opened (Arm, Overdrive Interactive)
vertical:        none named on any of the five (IT operations for NinjaOne and risk-management software for Riskonnect are named as the client's own business description, not a page-stated vertical label)
paid_by_outcome: unknown — not disclosed on any of the five
prompt_set_disclosed: no — none of the five discloses a fixed prompt set with n
```

No interpretation. This file re-ticks the seven-item bar formally for all five per grading rule 1 (P3-c4's own grading, while full-page, did not present a formal per-item checklist); NinjaOne, Riskonnect, Bloomfire content is carried forward from `docs/raw/a-brightedge-customers-2026-09-22.md` (same pull date), re-confirmed here rather than re-fetched.

## 1. NinjaOne — /resources/case-studies/ninjaone-ai-mentions-case-study

1. Brand — NinjaOne. ✓ 2. Engine(s) — "every AI engine," not itemised. ✗ 3. Absolute date window — "over the course of a year," "in June alone" — no calendar bound. ✗ 4. Baseline — "single digits" (not a figure). ✗ 5. Intervention — prompt grouping by product line/audience, weekly share-of-mentions reporting. ✓ 6. Sample/traffic volume — none stated. ✗ 7. Who measured — BrightEdge (vendor); not independent. ✗

Verbatim: "share of AI mentions grew from single digits to 61%... more than 20 points ahead of the next-closest brand"; "share of AI citations climbed... from single digits to 52%, ahead of every other source tracked, including Reddit, YouTube, and G2."

**evidence_grade: Bronze (same as P3-c4).** Visibility-only, no revenue link. Missing items 2, 3, 4, 6, 7.

## 2. Riskonnect — /resources/case-studies/riskonnect-ai-share-of-voice-case-study

1. Brand — Riskonnect. ✓ 2. Engine(s) — Google AI Overviews, named explicitly. ✓ 3. Absolute date window — "prompt set was created in February 2026," "227 by April," "continuing to grow through May" — partial-absolute (year and months named, no exact days). ~partial 4. Baseline — "earliest baseline" is not a figure. ✗ 5. Intervention — Data Cube X / AI Hyper Cube prompt-universe definition, content build, syndication. ✓ 6. Sample/traffic volume — none disclosed (the "495% Growth in organic traffic" headline carries no baseline period or absolute window of its own). ✗ 7. Who measured — BrightEdge; not independent; no control cohort. ✗

Verbatim: "495% — Growth in organic traffic to AI-optimized pages. 227 — AI Overview rankings tracked in four months."

**evidence_grade: Bronze (same as P3-c4).** Visibility/traffic, no revenue link, no control. Missing items 4, 6, 7.

## 3. Bloomfire — /resources/case-studies/bloomfire-agent-edge-case-study

1. Brand — Bloomfire. ✓ 2. Engine(s) — "AI agents"/"AI experiences," not itemised (ChatGPT/Claude/Gemini not individually named). ✗ 3. Absolute date window — "30% in July 2026, compared to the prior 90 days" — the most complete date+baseline pairing of the three P3-c4 cases. ✓ (partial-absolute: month+year named, exact days not) 4. Baseline — implied by the "prior 90 days" comparison, no absolute prior count stated. ~partial 5. Intervention — Agent Edge phased rollout, baseline measured first, limited pages then expanded. ✓ 6. Sample/traffic volume — none disclosed. ✗ 7. Who measured — BrightEdge; not independent. ✗

Verbatim: "AI referral traffic jumped 30% in July 2026, compared to the prior 90 days. Agent traffic to optimized pages doubled."

**evidence_grade: Bronze (same as P3-c4).** Traffic-only, no revenue link. Missing items 2, 6, 7.

## 4. Arm — /resources/case-studies/arm-agent-edge-case-study (newly opened this pull)

1. Brand — Arm. ✓ 2. Engine(s) — none named specifically ("AI agents," "verified AI agent traffic" generic). ✗ 3. Absolute date window — none stated. ✗ 4. Baseline — none stated. ✗ 5. Intervention — BrightEdge Agent Edge serving a markdown version specifically to verified AI agent traffic while the original page is unchanged for other visitors. ✓ 6. Sample/traffic volume — none disclosed (percentages/multiples only). ✗ 7. Who measured — BrightEdge; Jason Andrews (Arm) gave the testimonial but did not disclose financial relationship. ✗

Verbatim: "2x+ Increase: Sustained lift in AI agent traffic to optimized pages"; "~90% Reduction: Smaller payload served to AI agents"; traffic "more than doubled... in some cases, traffic even tripled."

**evidence_grade: Bronze.** Traffic-only claim, no revenue link. Missing items 2, 3, 4, 6, 7. Grade change: UP from `screened — not opened`.

## 5. Overdrive Interactive — /resources/case-studies/overdrive-interactive-achieves-ai-overview-growth-brightedge (newly opened this pull)

1. Brand — described as "A Leading Digital Marketing Agency" on the case's own headline; page body did not resolve the agency's identity beyond "Overdrive Interactive" in the URL slug. ~partial (name in URL, not confirmed restated in visible body text this pull) 2. Engine(s) — Google AI Overviews implied by "AI Overview Growth," ChatGPT context mentioned generally; not itemised precisely in the excerpt captured. ~partial 3. Absolute date window — "three months," relative; "November publications mentioned" but no calendar window stated for the headline figure. ✗ 4. Baseline — not disclosed numerically. ✗ 5. Intervention — "The Authority Project": author profiles, Person schema markup, enhanced blog architecture using BrightEdge's Generative Parser, Data Cube X, Copilot. ✓ 6. Sample/traffic volume — none disclosed. ✗ 7. Who measured — BrightEdge; not independent. ✗

Verbatim: "+710 AI Overview Growth"; "+66% Monthly Click Increase"; "710% increase in AI Overview mentions in three months."

**evidence_grade: Bronze.** Visibility/traffic, no revenue link. Missing items 3, 4, 6, 7 (and item 1/2 only partially satisfied per the excerpt captured). Grade change: UP from `screened — not opened`.

## Summary

5 of 5 BrightEdge AI-visibility case studies now opened (0 remain unopened for this vendor). All five graded Bronze. Zero Silver, zero Gold. 2 grade changes UP (Arm, Overdrive Interactive, both from `screened — not opened`); 3 same (NinjaOne, Riskonnect, Bloomfire, Bronze at P3-c4, re-confirmed with the formal seven-item checklist this pull).

## Pull notes — mechanical only

- NinjaOne, Riskonnect, Bloomfire verbatim text carried forward unedited from `docs/raw/a-brightedge-customers-2026-09-22.md` (same pull date, 2026-09-22, curl with browser User-Agent); not re-fetched this pull.
- Arm and Overdrive Interactive newly fetched via WebFetch this pull; Overdrive Interactive's extraction returned a shorter excerpt than the other four (see item 1/2 partial marks above) — a fuller re-pull of the raw HTML would resolve the brand/engine ambiguity noted.
