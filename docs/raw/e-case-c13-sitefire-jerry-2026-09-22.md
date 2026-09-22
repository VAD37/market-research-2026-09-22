# Sitefire — case study — Jerry.ai

```yaml
source:          Sitefire (sitefire.ai)
url_or_doc_id:   https://sitefire.ai/case-studies/jerry
published:       undated — no date on page
pull_date:       2026-09-22
pull_method:     browser extension (claude-in-chrome), dedicated own tab, no other agent's tab touched
pull_purpose:    evidence about a number
tier:            5
tier_reason:     adjusted up from table default 6 — discloses an absolute date window, a stated baseline period, and an explicit unaffected-control comparison (treated vs. untouched pages); still vendor-reported with no independent replication, bias flagged per trust-rubric.md
source_label:    vendor-reported
lane:            E
sub_market:      organic recommendation
engine:          GPT-5.4 (named as the model version behind a traffic disruption); "AI models" generic otherwise
metric_kind:     traffic (AI referral traffic, AI bot traffic); visibility (AI citation share, AI visibility)
supersedes:      none
captured:        full page
pass3_cluster:   a-vendor-census-c1 (row 8, Sitefire)
pass3_grade:     Bronze ("+300% site visits", "+78% AI referral traffic" — teaser only, homepage; this page is Jerry, the second of Sitefire's two Pass 3 Bronze cases, Pointhound already re-graded Silver by P4-c4)
vertical:        none named on this page (Jerry.ai is described as "the first AI-powered advisor to manage all your physical assets" — insurance/asset-management adjacent, not stated as an industry label)
paid_by_outcome: unknown — not disclosed
prompt_set_disclosed: partial — "AI visibility and citation share are measured against a set of prompts fixed at onboarding and never changed" (fixed set confirmed, n and wordings not published)
```

## Evidence bar — seven items ticked

1. **Brand** — Jerry (jerry.ai). Quote: "JERRY.AI — The first AI-powered advisor to manage all your physical assets." — SATISFIED
2. **Engine(s)** — Quote: "In early March, a GPT-5.4 release cut AI bot traffic across the web." GPT-5.4 is named as the model version behind the confound; no other individual engine (ChatGPT/Claude/etc.) is separately named for the headline figures, which are described as "AI models" / "AI answers" generically. — PARTIAL
3. **Absolute date window** — Quote: "Jerry's team shipped the changes in two waves between April and June 2026." Weekly chart runs "March to June" 2026. — SATISFIED
4. **Baseline before intervention** — Quote: "Each figure compares the three months after the first improved pages went live with the three weeks before." Chart baseline: "each group's own level before the March update." — SATISFIED
5. **Intervention** — Quote: "Jerry used Sitefire to improve a selected set of pages, while keeping the rest untouched" — described in detail (diagnose/improve/measure loop). — SATISFIED
6. **Sample size / traffic volume** — No absolute n of pages, prompts, or visits disclosed; only percentages and indices. — NOT SATISFIED
7. **Who measured, paid-by-outcome** — Sitefire (vendor) tracked the figures against its own onboarding-fixed prompt set; Jerry's own GA4/CDN logs implied but not named. No independent third party. Paid-by-outcome not disclosed. — NOT SATISFIED

**Unaffected control cohort** — explicit: Quote: "because Jerry left a comparable set of pages untouched, there's a clean read on how much of the lift was Sitefire's insights and how much was the market moving on its own. The gap between them is the Sitefire effect." Quantified: "the improved pages recovered quickly... and ended up at an average of 112% of their pre-GPT model update level, compared to only 72% for untouched pages."

## Verbatim

"Using Sitefire, Jerry's AI referral traffic rose 78%. Jerry wanted to know where AI models were sending insurance shoppers, and what it would take to get Jerry's own pages into those answers. Sitefire mapped the topics worth competing for, then showed page by page what was keeping Jerry out of them. Jerry's team shipped the changes in two waves between April and June 2026... +78% AI referral traffic (Clicks to jerry.ai from AI answers). +56% AI bot traffic (Requests from AI models fetching Jerry's pages). +27% AI citation share (Jerry's citations as a share of all AI citations). +9% AI visibility (Share of AI answers mentioning Jerry). Each figure compares the three months after the first improved pages went live with the three weeks before."

"In early March, a GPT-5.4 release cut AI bot traffic across the web, and this also affected Jerry. To recover traffic, Jerry used Sitefire to improve a selected set of pages, while keeping the rest untouched... Following the changes in April, the improved pages recovered quickly from the GPT model update, drove up AI traffic and referrals, and ended up at an average of 112% of their pre-GPT model update level, compared to only 72% for untouched pages."

"Sitefire measures visibility and citation share against Jerry's prompt set. The charts run March through July... AI visibility and citation share are measured against a set of prompts fixed at onboarding and never changed, so later comparisons stay meaningful."

Quote: "Sitefire showed us which pages actually mattered for GEO and what each one was missing... we wanted to make the pages we already had get trusted and cited by the LLMs." — Ida Sultan, Chief of Staff, Jerry.

## evidence_grade: **Silver** — grade change UP from Pass 3 Bronze (homepage teaser)

Pre/post baseline plus an explicit unaffected control metric (improved pages 112% of pre-update level vs. untouched pages 72%) clears the Silver bar per `glossary.md`. Missing item 6 (no absolute n) and item 7 (no independent measurer) keep it below Gold (no holdout, geo-split, or switchback). Structurally identical to Sitefire/Pointhound, already graded Silver by P4-c4 — Pointhound's own full page discloses an absolute date window (Feb 23–Jun 29 2026) and the same "new content vs. rest of site" control design.

## Pull notes — mechanical only

- Fetched via `claude-in-chrome` browser extension, `get_page_text`, after confirming `tabs_context_mcp` connectivity; own dedicated tab created and closed, two other agents' tabs observed in the shared group (Google/Capterra searches) and never touched.
- Page rendered in full on one load; no truncation, no paywall, no login wall.
