# Scrunch AI — five case-study pages, full-page re-grade under grading rule 1 (not covered by P4-c4)

```yaml
source:          Scrunch AI (scrunch.com) — five dedicated case-study pages, URLs per section
url_or_doc_id:   https://scrunch.com/case-studies/{akamai-5x-brand-presence-in-ai-search-results,strapi-customer-story,2026-01-stratabeat-ai-visibility-gains-for-clients,tinybird-ai-search-case-study,2025-04-from-underdog-to-powerhouse-bairesdevs-78-ai-search-surge}/
published:       Akamai 04.02.2026; Strapi 11.18.2025; Stratabeat 01.22.2026; Tinybird 10.29.2025; BairesDev 04.15.2025
pull_date:       2026-09-22
pull_method:     fetch (MCP_DOCKER fetch, P3-c2 pull, same date) — verbatim carried forward, each already individually fetched to its own dedicated page (2500-4000 characters, per-case)
pull_purpose:    evidence about a number
tier:            5 with n where stated, 6 without — mixed, per case
tier_reason:     no case discloses an unaffected control metric alongside a full date window and sample size; several disclose no n at all
source_label:    vendor-reported
lane:            E
sub_market:      organic recommendation
engine:          varies per case — see table; not itemised on 3 of 5 (Strapi, Stratabeat, Tinybird — captured excerpt truncated before engine list)
metric_kind:     visibility (brand presence, citations, mentions) on all five
supersedes:      none
captured:        each page captured to ~3500-4000 characters (per the original P3-c2 pull's per-call limit); full headline and body sections present, closing sections truncated
pass3_cluster:   a-vendor-census-c2 (row 1, Scrunch AI) — "11 screened, 8 graded, 3 screened-out-as-no-claim... 5 Bronze, 3 Fools gold, 0 Silver, 0 Gold" — each of the 11 case pages was individually fetched (not index-teaser only)
pass3_grade:     Bronze (all five)
vertical:        none named on any of the five dedicated pages
paid_by_outcome: unknown — not disclosed on any of the five
prompt_set_disclosed: no — none of the five discloses a total n of tracked prompts
```

No interpretation. All five verbatim excerpts and grading carried forward unedited from `docs/raw/a-scrunch-customers-2026-09-22.md` (same pull date, 2026-09-22) — that file already fetched each case's own dedicated page individually (not an index teaser), satisfying grading rule 1's "own full page" requirement even though truncated by the original pull's per-call character limit. This file re-ticks the seven items formally per case, consolidating per this task's own volume-management practice.

## 1. Akamai — /case-studies/akamai-5x-brand-presence-in-ai-search-results/ — By Eric Wendt, 04.02.2026

1. Brand — Akamai. ✓ 2. Engine(s) — "AI search" generic on the captured excerpt; not itemised. ✗ 3. Absolute date window — not stated in the captured excerpt. ✗ 4. Baseline — comparator is "comparable non-AXP webpages" (a treatment/control page comparison, not a pre/post time baseline). ~partial 5. Intervention — Scrunch's AXP serving AI-optimized content directly to AI agents without altering the human-facing page. ✓ 6. Sample/traffic volume — not stated in the captured excerpt (truncated before the numeric outcome section). ✗ 7. Who measured — Scrunch (vendor); no independent party. ✗

Verbatim: "5x'd brand presence"; per a separate Sitecore acquisition press release restating the same case: "364% increase in brand presence for non-branded prompts, 218% increase in citations," AXP-enabled pages vs. comparable non-AXP webpages.

**evidence_grade: Bronze.** Visibility-only (brand presence, citations), no revenue link. Missing items 2, 3, 6, 7. [note: the page's own numeric outcome section was cut by the original pull's truncation at 4000 characters; the 364%/218% figures come from a separate Sitecore press release describing the same case, cross-referenced not duplicated verbatim.]

## 2. Strapi — /case-studies/strapi-customer-story/ — By Kevin White, 11.18.2025

1. Brand — Strapi (headless CMS). ✓ 2. Engine(s) — not named in the captured excerpt (ChatGPT referenced generically: "then ChatGPT launched"). ~partial 3. Absolute date window — not stated. ✗ 4. Baseline — not stated. ✗ 5. Intervention — Scrunch competitive monitoring and GEO/AEO content work (with agency GrowthX). ✓ 6. Sample/traffic volume — not stated in the captured excerpt. ✗ 7. Who measured — Scrunch/customer self-report. ✗

Verbatim: "grew AI search citations 226%."

**evidence_grade: Bronze.** Visibility-only (citations), no revenue link. Missing items 2 (specific engine), 3, 4, 6, 7.

## 3. Stratabeat — /case-studies/2026-01-stratabeat-ai-visibility-gains-for-clients/ — By Kevin White, 01.22.2026

1. Brand — Stratabeat (B2B marketing agency). ✓ 2. Engine(s) — not named in the captured excerpt. ✗ 3. Absolute date window — "under 2 months," relative. ✗ 4. Baseline — not stated numerically. ✗ 5. Intervention — Scrunch used to unlock AI-search intel for agency clients at scale. ✓ 6. Sample/traffic volume — "somewhere around 50-100 non-branded prompts" per client (approximate, agency-stated). ~partial 7. Who measured — Scrunch/agency self-report. ✗

Verbatim: "260%+ AI visibility gains for clients in under 2 months."

**evidence_grade: Bronze.** Visibility-only, no revenue link. Missing items 2, 3, 4, 7.

## 4. Tinybird — /case-studies/tinybird-ai-search-case-study/ — By Kevin White, 10.29.2025

1. Brand — Tinybird (serverless real-time analytics platform). ✓ 2. Engine(s) — not named in the captured excerpt ("LLM responses" generic). ✗ 3. Absolute date window — not stated. ✗ 4. Baseline — "practically zero visibility" before (qualitative). ✗ 5. Intervention — Scrunch used to monitor performance across AI platforms for commercial-intent prompts. ✓ 6. Sample/traffic volume — not stated in the captured excerpt. ✗ 7. Who measured — Scrunch/customer self-report. ✗

Verbatim: "3x'd brand mentions."

**evidence_grade: Bronze.** Visibility-only (mentions), no revenue link. Missing items 2, 3, 4, 6, 7.

## 5. BairesDev — /case-studies/2025-04-from-underdog-to-powerhouse-bairesdevs-78-ai-search-surge/ — By Wil Armstrong, 04.15.2025

1. Brand — BairesDev, vs. named competitors Cognizant, Toptal. ✓ 2. Engine(s) — ChatGPT, Perplexity, named. ✓ 3. Absolute date window — "two months," relative. ✗ 4. Baseline — qualitative only ("limited visibility... AI Search platforms weren't mentioning them"), no numeric starting figure. ✗ 5. Intervention — 10 blog posts identified/updated with AI-visibility-targeted changes (brand-forward language, FAQs, structured data, external authoritative links). ✓ 6. Sample/traffic volume — "10 blog posts" (n of pages updated, not of prompts/traffic). ~partial 7. Who measured — Scrunch/customer self-report. ✗

Verbatim: "78% AI Search surge"; "seeing measurable results in just two months."

**evidence_grade: Bronze.** Visibility-only, no revenue link. Missing items 3, 4, 7 — the strongest-disclosed of the five on engine specificity (both ChatGPT and Perplexity individually named).

## Summary

5 of 5 Scrunch Bronze cases re-ticked against the formal seven-item bar this pull; all five confirmed **Bronze, same as Pass 3**. No grade changes. Zero Silver, zero Gold — no Scrunch case discloses an unaffected control cohort or an independent measurer. (Scrunch's remaining 6 titles — Proper Propaganda, AlchemyLeads, Runpod ×2, Big Leap, Clapping Dog Media — are already graded/screened at Pass 3 from their own full pages and are not re-opened here; see `a-scrunch-customers-2026-09-22.md`.)

## Pull notes — mechanical only

- No new fetch this pull — verbatim and grading basis carried forward from `docs/raw/a-scrunch-customers-2026-09-22.md`, itself dated 2026-09-22 and already satisfying "own full page" per case (not an index teaser), consistent with grading rule 1. This file adds the formal seven-item-by-item tick that the original consolidated pull's summary table did not itemise line-by-line.
