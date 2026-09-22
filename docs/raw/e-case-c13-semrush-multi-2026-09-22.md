# Semrush — three AI-visibility case-study pages, full-page re-grade under grading rule 1 (not covered by P4-c4)

```yaml
source:          Semrush — three dedicated customer story pages, URLs per section
url_or_doc_id:   https://www.semrush.com/company/stories/{sure-oak-ai-visibility,activate-digital-ai-visibility,coalitiontechnologies}/
published:       undated on all three pages
pull_date:       2026-09-22
pull_method:     browser (Playwright MCP) for Sure Oak and Activate Digital, P3-c4 pull under this same date; browser extension (claude-in-chrome), own dedicated tab, for Coalition Technologies, this pull
pull_purpose:    evidence about a number
tier:            6
tier_reason:     downgraded from table default 5 — some numeric figures disclosed but no absolute calendar dates, no independent measurer on any of the three; per trust-rubric.md "vendor measuring the thing it sells," bias flagged
source_label:    vendor-reported
lane:            E
sub_market:      organic recommendation
engine:          Sure Oak: ChatGPT, Google AI Overviews. Activate Digital: ChatGPT, AI Mode, Perplexity, "SearchGPT" (customer's own term). Coalition Technologies: ChatGPT named; "LLMs" generic otherwise
metric_kind:     traffic (referral growth, AI referral traffic); visibility (AI Overview appearances); sales (lead share, conversions — flagged separately)
supersedes:      none
captured:        full page, each of the three
pass3_cluster:   a-vendor-census-c4 (Part A row 4, Semrush) — "3 identified / 2 opened and graded" (Sure Oak, Activate Digital); Coalition Technologies "screened via teaser only"
pass3_grade:     Bronze (Sure Oak, Activate Digital, full-page-graded at P3-c4 without a formal seven-item checklist); screened — not opened (Coalition Technologies)
vertical:        none named on any of the three pages
paid_by_outcome: unknown — not disclosed on any of the three
prompt_set_disclosed: no — none of the three discloses a fixed prompt set with n
```

No interpretation. Sure Oak and Activate Digital verbatim carried forward from `docs/raw/a-semrush-customers-2026-09-22.md` (same pull date), formally re-ticked against the seven-item bar here per grading rule 1. Coalition Technologies newly opened this pull.

## 1. Sure Oak — /company/stories/sure-oak-ai-visibility/

1. Brand — Sure Oak (real agency, not anonymized). ✓ 2. Engine(s) — ChatGPT, Google AI Overviews, named. ✓ 3. Absolute date window — month-over-month comparisons named ("July vs. June," "May–June vs. July–August") but no year stated anywhere on the undated page. ✗ 4. Baseline — none numeric (percentages only). ✗ 5. Intervention — schema implementation, HTML/heading architecture, TOCs, topic-cluster content, E-E-A-T enhancement. ✓ 6. Sample/traffic volume — none disclosed (no underlying referral or lead counts). ✗ 7. Who measured — Semrush wrote and published the story; not independent. ✗

Verbatim: "+41% MoM growth in ChatGPT referrals (July vs. June); +286% growth in Google AI Overviews appearances (May–June vs. July–August); 40% of all new leads now come directly through LLM visibility."

**evidence_grade: Bronze (same as P3-c4).** Traffic/visibility claims graded; the "40% of leads through AI visibility" figure is a referral-attribution read, flagged per trust-rubric.md's "referral traffic reported as influence," kept and graded consistent with this cluster's treatment elsewhere, not discarded outright. Missing items 3 (absolute), 4, 6, 7.

## 2. Activate Digital / Dryer Vent Wizard — /company/stories/activate-digital-ai-visibility/

1. Brand — Activate Digital Media / Dryer Vent Wizard (Neighborly Corporation). ✓ 2. Engine(s) — ChatGPT, AI Mode, Perplexity, "SearchGPT" (customer's own term, kept verbatim). ✓ 3. Absolute date window — "within two months," "in 60 days," relative; no calendar dates. ✗ 4. Baseline — organic traffic "sitting flat at 25,000–26,000 new organic users per month" before. ✓ 5. Intervention — AI Visibility tool surfaced customer questions; content built for "dryer error codes" opportunity, localized across 100+ franchise sites. ✓ 6. Sample/traffic volume — "over 120 franchise locations," a competitor's estimated "12,000 monthly visits" cited for context. ~partial 7. Who measured — Jonathan Banks, Activate Digital's own Director, via Semrush; not independent. ✗

Verbatim: "#1 rankings on ChatGPT and AI Mode for priority queries"; "10% increase in leads from AI visibility"; "Organic traffic doubled, jumping from 25K to over 50K monthly users"; "10% of all franchise leads now coming from AI search engines."

**evidence_grade: Bronze.** Traffic claim (organic traffic doubling, with a genuine before/after pair) graded Bronze; the "10% of leads... from AI visibility" and "10% increase in leads" sub-claims are lead-share/conversion-adjacent with no baseline or control — graded **Fools gold** separately, not counted toward the Bronze headline. Missing items 3, 7 on the traffic claim.

## 3. Coalition Technologies — /company/stories/coalitiontechnologies/ (newly opened this pull)

1. Brand — client is a "San Francisco-based restaurant group," anonymized but industry- and geography-specified (agency Coalition Technologies is named). ~partial 2. Engine(s) — ChatGPT named explicitly ("tracking how ChatGPT represented clients"); "LLMs" generic otherwise. ✓ 3. Absolute date window — none stated. ✗ 4. Baseline — none numeric. ✗ 5. Intervention — content restructured for AI fan-out, brand-sentiment monitoring and correction, preferred-publisher targeting, product-nuance content for ecommerce clients. ✓ 6. Sample/traffic volume — none disclosed. ✗ 7. Who measured — Jordan Brannon, Coalition's own President, via Semrush's AI Visibility Toolkit; not independent. ✗

Verbatim: "429% increase in AI referral traffic and visibility for a San Francisco-based restaurant group"; "547% increase in conversions from that AI referral traffic, with bottom-of-funnel pages generating leads after multi-step AI interactions."

**evidence_grade: Bronze** for the traffic claim (429% AI referral traffic). **The "547% increase in conversions" sub-claim is a revenue/conversion claim with no baseline and no control: graded Fools gold separately.** Missing items 3, 4, 6, 7 on the traffic claim. Grade change: UP from `screened — not opened`.

## Summary

3 of 3 titles now opened (0 remain unopened for this vendor). 3 graded Bronze on their headline traffic/visibility claim (Sure Oak, Activate Digital, Coalition Technologies); 2 of the 3 (Activate Digital, Coalition Technologies) carry a bundled lead/conversion sub-claim graded Fools gold separately. Zero Silver, zero Gold. 1 grade change UP (Coalition Technologies, from `screened — not opened`); 2 same (Sure Oak, Activate Digital, Bronze at P3-c4).

## Pull notes — mechanical only

- Sure Oak and Activate Digital text carried forward unedited from `docs/raw/a-semrush-customers-2026-09-22.md` (same pull date). Coalition Technologies fetched fresh via `claude-in-chrome` `get_page_text` after a `WebFetch` attempt on the same URL returned only navigation chrome (JS-rendered SPA, consistent with the other two Semrush stories' own pull notes) — browser fallback used per task instruction.
