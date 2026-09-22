# Conductor — nine case-study pages, full-page re-grade (not covered by P4-c4)

```yaml
source:          Conductor (conductor.com) — nine dedicated customer case-study pages, URLs per section
url_or_doc_id:   https://www.conductor.com/customer-stories/{hg-insights-trustradius,boston-globe-media,clutch,overdrive,zurich-insurance-uk,parker-hannifin,hr-block,sonos,brunswick}/
published:       undated on all nine pages
pull_date:       2026-09-22
pull_method:     fetch (WebFetch)
pull_purpose:    evidence about a number
tier:            6
tier_reason:     table default — vendor-authored case studies, self-measured by Conductor, no independent third-party replication; bias flagged per trust-rubric.md
source_label:    vendor-reported
lane:            E
sub_market:      organic recommendation
engine:          varies per case — see table; ChatGPT/Perplexity/Gemini recur across most
metric_kind:     visibility (citations, brand mentions, AI market share) — the two graded cases
supersedes:      none
captured:        full page, each of the nine
pass3_cluster:   a-vendor-census-c3 (row 2, Conductor) — customer-stories listing graded 1 of 12 titles on the full page (Title Nine, Bronze/Fools gold, already re-graded by P4-c4); 11 titles left screened-not-opened
pass3_grade:     screened — not opened (all nine)
vertical:        Technology (HG Insights, Clutch, Sonos, per Conductor's own listing tag); Other (Boston Globe Media); Services (Overdrive); Finance (Zurich UK, H&R Block); Manufacturing (Parker Hannifin, Brunswick)
paid_by_outcome: unknown — not disclosed on any of the nine
prompt_set_disclosed: no — none of the nine discloses a fixed prompt set with n
```

No interpretation. Consolidated per this cluster's volume. All 12 titles on Conductor's customer-stories listing are now opened between Pass 3 (1) and this pull (11, all 11 remaining) — 0 titles remain `screened — not opened` for this vendor. Two clear the bar at Bronze; the other seven carry no quantified before/after visibility/traffic/sales metric on their own page and are screened, not graded.

## 1. Zurich Insurance UK — /customer-stories/zurich-insurance-uk/

1. Brand — Zurich Insurance UK. ✓ 2. Engine(s) — ChatGPT, Perplexity, Gemini, named (in the context of Conductor's free tool). ✓ 3. Absolute date window — none stated. ✗ 4. Baseline — not disclosed numerically. ✗ 5. Intervention — indexing adjustments on a technical PDF cited for contextually irrelevant prompts, aligned to existing keyword taxonomy. ✓ 6. Sample/traffic volume — not disclosed. ✗ 7. Who measured — Daniel Hall, Zurich's own Search Marketing Manager, via Conductor's platform; not independent. ✗

Verbatim: "47% reduction in irrelevant citations" after adjusting document indexing.

**evidence_grade: Bronze.** Citation-accuracy (visibility) claim only, no revenue link. Missing items 3, 4, 6, 7.

## 2. H&R Block — /customer-stories/hr-block/

1. Brand — H&R BLOCK. ✓ 2. Engine(s) — ChatGPT, Perplexity, Gemini, named. ✓ 3. Absolute date window — "Since September" — year not stated, no end date. ✗ 4. Baseline — not disclosed numerically (percentages only). ✗ 5. Intervention — Conductor's AI Search Performance monitoring, structural content updates, stronger FAQs. ✓ 6. Sample/traffic volume — not disclosed. ✗ 7. Who measured — Ben Greutman, H&R Block's own Sr. Search Marketing Manager, via Conductor; not independent. ✗

Verbatim: "website citations... double" (2x); "AI brand mentions have increased by a little over 50%"; "AI market share by brand mentions: +125%."

**evidence_grade: Bronze.** Visibility-only (citations, mentions, market share), no revenue link. Missing items 3, 4, 6, 7.

## Screened — no quantified before/after metric on the case's own page (opened, not graded)

- **HG Insights** (/customer-stories/hg-insights-trustradius/): product-launch description (GEO Monitoring Dashboard) with category-level context stats ("63% of tech buyers use AI to research software," "60 million AI-crawler visits a year to TrustRadius") but no before/after outcome for HG Insights itself.
- **Boston Globe Media** (/customer-stories/boston-globe-media/): "Health score increased to 885" from 860 (+3%) and "double-digit organic traffic growth" — a technical site-health score, not one of the three canonical metrics; traffic figure not AI-surface-specific.
- **Clutch** (/customer-stories/clutch/): describes a survey stat ("80% said AI visibility crucial... fewer than half tracking it") and Clutch's own AI Visibility Score product (430,000+ providers, 10,000+ prompts) — a product description, no before/after outcome for Clutch itself.
- **Overdrive** (/customer-stories/overdrive/): "a few hours" to "under 30 minutes" per-client reporting time — an efficiency metric, not visibility/traffic/sales.
- **Parker Hannifin** (/customer-stories/parker-hannifin/): "Increased organic traffic, conversions, and lead generation" stated with no percentage or count anywhere on the page.
- **Sonos** (/customer-stories/sonos/): "among the top five Consumer Discretionary brands by AI brand mention market share" per a third-party 2026 AEO/GEO Benchmarks Report — a ranking claim with no stated prior rank or numeric baseline.
- **Brunswick** (/customer-stories/brunswick/): "meaningful year-over-year traffic growth" for one brand (Harris), no percentage given; a "+125%" figure on the same page belongs to a different company (Taylor Corporation), not Brunswick.

(ASUG — "increased efficiency by 75%," already screened at Pass 3 as an operational, non-visibility/traffic/sales metric — not re-opened this pull, cited from `a-vendor-census-c3-2026-09-22.md`.)

## Summary

9 titles opened this pull (all remaining on Conductor's 12-title listing). 2 graded Bronze (Zurich UK, H&R Block) — both grade changes UP from `screened — not opened`. 7 carry no qualifying quantified metric and are screened, not graded. Zero Silver, zero Gold. Title Nine (already Bronze/Fools gold, P4-c4) and ASUG (screened, Pass 3) complete the 12-title set at 0 remaining unopened.

## Pull notes — mechanical only

- All pages fetched via WebFetch; no browser fallback needed. Each case individually queried for brand/engine/date/baseline/intervention/volume/measurer; verbatim figures quoted back from tool output.
