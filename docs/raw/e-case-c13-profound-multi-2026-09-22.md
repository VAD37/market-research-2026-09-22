# Profound — eight case-study pages, full-page re-grade (not covered by P4-c4)

```yaml
source:          Profound (tryprofound.com) — eight dedicated customer case-study pages, URLs per section
url_or_doc_id:   https://www.tryprofound.com/customers/{aleph,crs-credit-api,opus-clip,hone,ramp,lake-com,airbyte,1840-co-answer-engine-optimization-case-study}
published:       undated on all eight pages
pull_date:       2026-09-22
pull_method:     fetch (WebFetch)
pull_purpose:    evidence about a number
tier:            6
tier_reason:     table default — vendor-authored case studies, self-measured by Profound, no independent third-party replication on any of the eight; bias flagged per trust-rubric.md
source_label:    vendor-reported
lane:            E
sub_market:      organic recommendation
engine:          varies per case — see table; ChatGPT and Perplexity recur across all eight
metric_kind:     visibility (all eight); traffic (Aleph); sales/revenue sub-claims flagged separately (CRS, OpusClip, Airbyte)
supersedes:      none
captured:        full page, each of the eight (per WebFetch extraction)
pass3_cluster:   a-vendor-census-c1 (row 5, Profound) — customers index page graded 13 cases Bronze on intake from index-teaser text; these 8 are the Bronze cases not already re-graded by P4-c4 (which covered Profound/MongoDB and Profound/Plaid only)
pass3_grade:     Bronze (all eight, on index-teaser text — see `docs/raw/a-profound-customers-2026-09-22.md`)
vertical:        none named on any of the eight dedicated pages (Profound's separate customers-index tags each with an industry label, not repeated on the case's own page — per P4-c4's stated convention, not carried into this column)
paid_by_outcome: unknown — not disclosed on any of the eight
prompt_set_disclosed: no — none of the eight discloses a fixed prompt set with n
```

No interpretation. One consolidated file per this task's own budget, per the precedent set by `docs/raw/a-scrunch-customers-2026-09-22.md` and `a-otterly-customers-2026-09-22.md` (P3-c2) — one file per pull is the norm; consolidation is a documented deviation here to manage volume across eight full-page re-grades in one cluster.

## 1. Aleph — https://www.tryprofound.com/customers/aleph

1. Brand — Aleph (AI-native FP&A platform). ✓
2. Engine(s) — ChatGPT, Perplexity, Claude, named. ✓
3. Absolute date window — "2 months" only, relative. ✗
4. Baseline — citation share 1.5% before, 5.3% after; "5x increase" in AI visibility. ✓
5. Intervention — Profound Pods training, Profound Agents automating brief generation/source identification/internal linking. ✓
6. Sample/traffic volume — no absolute n disclosed. ✗
7. Who measured, paid-by-outcome — Profound measured; no independent party; paid-by-outcome not disclosed. ✗

Verbatim figures: "5x increase" in AI visibility; "253% increase in citation share in 2 months" (1.5% → 5.3%); "82% increase in LLM-attributed website traffic."

**evidence_grade: Bronze.** Visibility and traffic claims only, no revenue link. Missing items 3, 6, 7.

## 2. CRS Credit API — https://www.tryprofound.com/customers/crs-credit-api

1. Brand — CRS Credit API, named. ✓
2. Engine(s) — ChatGPT, Grok, named. ✓
3. Absolute date window — none stated. ✗
4. Baseline — not disclosed numerically. ✗
5. Intervention — Profound Answer Engine Insights connected to Google Analytics/Looker; Agents, FAQ Agent explored. ✓
6. Sample/traffic volume — not disclosed. ✗
7. Who measured — CRS's own analytics integration + Profound; not independent. ✗

Verbatim figures: "20x" increase in AI search visibility; "15%" growth in pipeline attributed to AI search traffic; "8%" increase in weekly traffic from LLM citations.

**evidence_grade: Bronze** for the visibility bundle (20x, no baseline, no revenue link on that specific figure). **A sub-claim — "15% growth in pipeline" — is a revenue/pipeline claim with no baseline and no control: graded Fools gold separately**, not counted toward the Bronze headline.

## 3. OpusClip — https://www.tryprofound.com/customers/opus-clip

1. Brand — OpusClip, named. ✓
2. Engine(s) — ChatGPT, Perplexity, Claude, named. ✓
3. Absolute date window — "30 days" only, relative. ✗
4. Baseline — brand visibility "approximately 30%" before, "more than 45%" after. ✓
5. Intervention — historical-data-driven content optimization, cross-functional. ✓
6. Sample/traffic volume — "50,000 citations and thousands of different answers" analyzed. ✓ (partial — an analysis-corpus size, not a traffic/n-of-results figure for the outcome itself)
7. Who measured — OpusClip's internal team via Profound's platform; not independent. ✗

Verbatim figures: "increase our brand visibility to more than 45% for our core topics"; "#1 ranking for citations in their industry among competitors."

**evidence_grade: Bronze** for the visibility bundle (missing items 3, 7). **A sub-claim — "37% increase in new user signups from Answer Engines" — is a signup/conversion claim with no baseline and no control: graded Fools gold separately.**

## 4. Hone — https://www.tryprofound.com/customers/hone

1. Brand — Hone, named. ✓
2. Engine(s) — Google AI Overview, ChatGPT, named. ✓
3. Absolute date window — "within just a few months" only, relative. ✗
4. Baseline — citation share "nearly 0%" before, "7%" after (10x). ✓
5. Intervention — targeted blog initiative optimized for AI crawling and citation potential. ✓
6. Sample/traffic volume — not disclosed. ✗
7. Who measured — Profound; not independent. ✗

Verbatim figures: "800%" visibility increase; "#1 most cited source"; citation share "grew by 10x (from nearly 0% to 7%)."

**evidence_grade: Bronze.** Visibility-only, no revenue link. Missing items 3, 6, 7.

## 5. Ramp — https://www.tryprofound.com/customers/ramp

1. Brand — Ramp, named. ✓
2. Engine(s) — ChatGPT, Perplexity, Claude, named. ✓
3. Absolute date window — **"12/01/2024 to 2/15/2025."** ✓
4. Baseline — AI visibility 3.2%, citation share 8.1%, competitive ranking 19th among fintech brands. ✓
5. Intervention — targeted content pages ("Accounts Payable Software for Small Businesses" etc.), comparison articles. ✓
6. Sample/traffic volume — "300+ Citations" generated within one month. ✓
7. Who measured — Profound; not independent; no unaffected control cohort named. ✗

Verbatim figure: "7x AI Visibility Improvement: Ramp's AI visibility surged from 3.2% to 22.2% within a month."

**evidence_grade: Bronze.** Clears items 1–6 of the seven — the most complete of the eight on that count — but has no unaffected control metric and no independent measurer (item 7), so per `glossary.md` it does not clear Silver ("baseline plus an unaffected control metric"); visibility-only, no revenue link.

## 6. Lake.com — https://www.tryprofound.com/customers/lake-com

1. Brand — Lake.com, named. ✓
2. Engine(s) — ChatGPT, Perplexity, Google AI Overviews, named. ✓
3. Absolute date window — **"June 24, 2025 to June 30, 2025."** ✓
4. Baseline — visibility score 27.9% (6/30/2025) → 41.2% (6/24/2025, as stated on page — dates as printed, not reconciled by this pull). ✓
5. Intervention — Conversation Explorer / Answer Engine Insights mapping customer journey; event-driven articles, destination content, evergreen guides. ✓
6. Sample/traffic volume — "5x spike in branded organic traffic during peak season," no absolute n. ✗
7. Who measured — Profound; not independent; no control cohort. ✗

**evidence_grade: Bronze.** Visibility/traffic, no revenue link. Missing items 6, 7. [note: the two dates given for the baseline and post figures on this page are not in chronological order as printed — recorded verbatim, not corrected.]

## 7. Airbyte — https://www.tryprofound.com/customers/airbyte

1. Brand — Airbyte, named. ✓
2. Engine(s) — ChatGPT, Perplexity, Google AI Overviews, Copilot, named. ✓
3. Absolute date window — **"April 13, 2025 to June 22, 2025."** ✓
4. Baseline — ChatGPT visibility "9%" before. ✓
5. Intervention — content restructured into direct answers/lists, schema.org markup, llms.txt, authority signals. ✓
6. Sample/traffic volume — "over 500 prompts" analyzed. ✓
7. Who measured — Profound; not independent; no control cohort. ✗

Verbatim figures: "3x" visibility increase in ChatGPT ("from 9% to 26%," one-week change); "+16%" lift across AI platforms.

**evidence_grade: Bronze** for the visibility bundle — clears items 1–6, missing only 7 (and no control cohort, so not Silver). **A sub-claim — "$100,000 deal closed in July 2025," linked to the AI-visibility work — is a revenue claim with no baseline and no control: graded Fools gold separately.**

## 8. 1840 & Co. — https://www.tryprofound.com/customers/1840-co-answer-engine-optimization-case-study

1. Brand — 1840 & Co., named. ✓
2. Engine(s) — ChatGPT, Perplexity, Microsoft Copilot, named. ✓
3. Absolute date window — none; only relative ("1 month," "two weeks"). ✗
4. Baseline — AI visibility 0% before. ✓
5. Intervention — one targeted blog post with AI-optimized formatting (headings, bullets, FAQ). ✓
6. Sample/traffic volume — not disclosed. ✗
7. Who measured — Profound; not independent. ✗

Verbatim figures: "11%" AI visibility achieved after 1 month; intermediate "6%" after two weeks; competitor visibility for context, Toptal "around 74%," Upwork "about 29%." Quote: "Profound has given us actionable insights on how our brand is performing for GEO" — Jay Douglas, Marketing Director, 1840 & Company.

**evidence_grade: Bronze.** Visibility-only, no revenue link. Missing items 3, 6, 7.

## Summary

8 cases opened, 8 graded Bronze on their headline visibility/traffic claim; 3 of the 8 (CRS Credit API, OpusClip, Airbyte) carry a bundled revenue-adjacent sub-claim graded Fools gold separately, consistent with the bundling pattern P4-c4 already established for Conductor/Title Nine and Profound/Plaid. Zero Silver, zero Gold. Ramp, Lake.com and Airbyte carry absolute calendar date windows (a first among Profound's cases pulled across this whole programme); none discloses an unaffected control cohort or an independent measurer, so none clears Silver.

## Pull notes — mechanical only

- All eight pages fetched via WebFetch (Claude-processed extraction), each with an identical extraction prompt (brand, engines, date window, baseline, intervention, sample/volume, measurer). Verbatim figures quoted back from each tool result; no page required a browser fallback.
- Grade changes vs. Pass 3: all eight **same** (Bronze → Bronze) on the headline claim; three now additionally carry a **newly surfaced** Fools-gold sub-claim not distinguished at Pass 3's index-teaser level (CRS, OpusClip, Airbyte) — not counted as up/down since the headline grade is unchanged, per the P4-c4 precedent for Profound/Plaid's own newly-surfaced conversion sub-claim.
