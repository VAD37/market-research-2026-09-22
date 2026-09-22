# AthenaHQ — Grüns case study

```yaml
source:          AthenaHQ — case study "How Grüns achieved 6x Share of Voice Lift in 60 Days"
url_or_doc_id:   https://athenahq.ai/case-studies/10-6pp-sov-gruns-ai-search-case-study
published:       undated — no publish date on page; case covers "Q3 2025" and "Jul 17 → Sep 20" (year inferred as 2025 from the Q3 2025 reference in the same case)
pull_date:       2026-09-22
pull_method:     browser extension (claude-in-chrome, own dedicated tab)
pull_purpose:    evidence about a number
tier:            5
tier_reason:     discloses explicit numeric before/after baselines for three named metrics, a near-absolute date window (Jul 17 - Sep 20, year inferable from the case's own "Q3 2025" statement), and named engines — adjusted up from table default 6, but capped at 5, no unaffected control metric and no independent third-party measurer, per trust-rubric.md "vendor measuring the thing it sells" (AthenaHQ and its partner agency Boring Ecom both had a commercial stake in the outcome)
source_label:    vendor-reported
lane:            E
sub_market:      organic recommendation
engine:          ChatGPT, Perplexity, Google AI Overviews — named explicitly as the set AthenaHQ's Prompt Planner tracked; not broken out per-engine in the before/after table (all three figures are pooled across the tracked prompt set)
metric_kind:     visibility — three sub-metrics per `glossary.md`: Share of Voice (a vendor composite, not one of mention/citation/recommendation), Brand Mention Rate, Citation Rate. No traffic or sales figure on this page beyond an estimated-impressions count
supersedes:      none
captured:        full page — single call, reached the "Keep Reading / More case studies" footer, no truncation
vertical:        none named as an industry-vertical label on the page itself; Grüns is described as a supplement/wellness snack brand ("Grüns reimagines daily greens as convenient, great-tasting snack packs"); AthenaHQ's own homepage carousel groups this case under "Winning AI Recommendations in Wellness" (per `docs/raw/a-athenahq-customers-2026-09-22.md`, a different, unnamed vignette on that page, not confirmed as the same case)
evidence_grade:  Bronze (full-page, on this pull). All seven bar items evaluated below.
pass3_grade:     Bronze (from `docs/raw/a-vendor-census-c1-2026-09-22.md`, graded off the homepage-carousel teaser — `docs/raw/a-athenahq-customers-2026-09-22.md`, which did not open this dedicated page)
paid_by_outcome: unknown — quote below; AthenaHQ and named partner agency Boring Ecom both had a commercial relationship with Grüns, but no fee structure (flat, retainer, or performance-based) is stated
prompt_set_disclosed: no — "tracked prompts" and "Prompt Planner" are named as the method but no n of prompts, no prompt wordings, and no fixed panel version are disclosed
```

## Verbatim

Title: "How Grüns achieved 6x Share of Voice Lift in 60 Days"

Headline stat tiles: "6x share of voice lift in 60 days" / "15 targeted articles drove the lift" / "~70% of citations from Athena content"

**Customer Story:** "Grüns partnered with Athena and Boring Ecom (founded by Joseph Siegel, former Director Ecommerce Marketing at Feastables) to transform their AI Search presence with a data-driven content strategy. Over Q3 2025, Grüns executed a prompt-led pillar-and-cluster plan that rapidly improved citations, brand mentions, and Share of Voice across tracked prompts." — Connor Dault, CMO.

**Executive Summary table (verbatim):**

| Metric | Before | After | Change |
|---|---|---|---|
| Share of Voice | 2.0% | 12.6% | ~6x |
| Brand Mention Rate | 4.0% | 25.0% | +19% |
| Citation Rate | 0.3% | 7.0% | ~23x |
| LLM Impressions | — | 10,500+ est. | — |
| Content Output | — | 15 posts | ~70% citations from Athena content |

**The Sequence We Ran:** "1) Identified high monthly search prompts using AthenaHQ's Prompt Planner (volume + mention intelligence) across ChatGPT, Perplexity, and AI Overviews. 2) Created a pillar page as the authoritative, AI-readable hub (definitions, comparisons, specs, use cases, FAQs, schema). 3) Published target articles (cluster) interlinked to the pillar and optimized for entity clarity and AI extraction. 4) Citations increased as structure and entity completeness improved. 5) Brand mentions increased as citation velocity compounded authority signals. 6) Share of Voice increased 6x (2.0% → 12.6%)."

**Timeline:** "Month 1: Shipped a single high-leverage blog and saw immediate movement — early lifts in citations and brand mentions validated topic-entity fit. Month 2: Programmatically shipped targeted content using AthenaHQ Content and Shopify Integration with human-in-the-loop proof reading along with continuous prompt refinement. Result: 6x SoV, 23x citation rate, +19% brand mentions."

**Citation Rate Performance:** "From Jul 17 → Sep 20, citation rate rose from 0.3% to 7.0% (~23x), generating 10,500+ estimated impressions from LLM responses. ~70% of citations were attributed to Athena-created content."

**Brand Mention Rate Growth:** "Overall brand mention rate increased from 4.0% to 25.0% (+19%), with strongest gains in Alternatives, Super Greens, and Gummy vs Powder prompt clusters."

**Why It Worked:** "Prompt-led planning, pillar-and-cluster architecture, and entity-first writing, aligned with AI extraction, makes Grüns easy to parse, cite, and recommend for AI Search."

**Testimonial:** "Athena is our OS for AI Search. Their prompt intelligence and editorial pipeline turn answers into a reliable channel. Month after month, they surface the next best moves and ship content the market and the models trust. It's why we consider Athena a long-term partner. Athena Enterprise gives us peace of mind; the platform largely runs itself. Growing GEO is a huge focus of ours and the full org is energized by the success we're seeing in the space with Athena." — Connor Dault, CMO.

**Quick Grüns Shoutout:** "Grüns reimagines daily greens as convenient, great-tasting snack packs — and the market noticed. They reached a $500M valuation about two years after launch with ARR > $100M, sell direct-to-consumer and through Sprouts, Target, and Walmart, and ship roughly 4M gummies per day. Each gummy includes 60 whole-food–derived ingredients — essential vitamins, minerals, adaptogens, and prebiotics — and is sugar-free while retaining great taste. Grüns holds an average 4.6/5 from 1,000+ Trustpilot reviews, with customers citing improved well-being and the ease of integrating nutrients into daily routines."

## Pull notes — mechanical only

- Fetched via `claude-in-chrome` browser extension (connected this session), `get_page_text` on a dedicated new tab (tabId 1697684063) opened for this task. Full page captured in one call, reached the "Keep Reading / More case studies" footer (three other case-study teasers — Cozy Earth, Rootly, Lago — recorded in Pull notes only, not graded, since they were not this pull's target case).
- The only absolute date fragment is "From Jul 17 → Sep 20" (no year stated in that sentence); the case's own header sentence states the campaign ran "Over Q3 2025", from which the year is inferred but not directly stated alongside the day-level dates. Recorded as a **partial** absolute date window, stronger than most cases pulled in this cluster but not a fully self-contained absolute date.
- No sample size (n of tracked prompts) is disclosed — "tracked prompts" and "Prompt Planner" describe the method, and "15 posts" / "10,500+ est. impressions" are volume figures, but no count of how many prompts were tracked is given.
- No statement anywhere on the page of who was paid by the outcome. Two commercial parties are named as delivering the work — AthenaHQ (the vendor, whose case study this is) and Boring Ecom (a named partner content agency) — with no fee structure (flat, retainer, or performance-based) disclosed for either.
- No unaffected control metric (a competitor, a different channel, or an untreated product line held constant) is disclosed anywhere on the page — every figure in the Executive Summary table is a before/after for Grüns' own tracked-prompt set, with no comparison group.

## Evidence bar — seven items, evaluated against this full page

| # | Item | Present / Absent | Quote |
|---|---|---|---|
| 1 | Brand, or credibly specified anonymised profile | **Present** | "Grüns partnered with Athena and Boring Ecom..." |
| 2 | The engine or engines | **Present** | "Identified high monthly search prompts using AthenaHQ's Prompt Planner ... across ChatGPT, Perplexity, and AI Overviews" |
| 3 | The date window, absolute | **Partial** | "From Jul 17 → Sep 20" (no year in that sentence); "Over Q3 2025" (quarter-level, in a separate sentence, from which the year is inferred) |
| 4 | The baseline before intervention | **Present** | "Share of Voice 2.0% → 12.6%"; "Brand Mention Rate 4.0% → 25.0%"; "Citation Rate 0.3% → 7.0%" |
| 5 | The intervention itself | **Present** | Six-step "Sequence We Ran": prompt identification, pillar page, cluster articles, interlinking, entity-first writing |
| 6 | The sample size, or the traffic volume | **Partial** | "15 targeted articles"; "10,500+ est." LLM impressions; no count of tracked prompts given |
| 7 | Who measured, and whether they were paid by the outcome | **Partial** | Measurer: AthenaHQ's own Prompt Planner tooling, with partner agency Boring Ecom executing content. No statement of whether either party was paid by the outcome |

**Full-page grade: Bronze.** Present or partial on six of seven items — the most evidence-complete case among the AthenaHQ pages pulled this task, including named engines and a near-absolute date window that the homepage-carousel teaser Pass 3 graded from did not carry at all. Still Bronze, not Silver: every metric (Share of Voice, Brand Mention Rate, Citation Rate) is a visibility sub-metric with no unaffected control cohort disclosed — the case reports only Grüns' own before/after, with no comparison group held constant, so it does not clear Silver's "baseline plus an unaffected control metric" bar. No revenue or traffic figure is claimed on this page.

**Grade change vs. Pass 3: same (Bronze → Bronze), but with substantially more of the seven-item bar satisfied.** Pass 3 graded this case Bronze from the homepage-carousel teaser text alone (`docs/raw/a-athenahq-customers-2026-09-22.md`: "engine, date, baseline, n, measurer" all listed as missing, 5 of 7). This full-page pull finds the engine, baseline, and a near-absolute date window are in fact disclosed on the dedicated case-study page — narrowing the missing-items count from 5 of 7 (teaser) to effectively 1-2 of 7 (full page: date-window precision and full measurer/paid-by-outcome disclosure). The grade itself does not change because the case still lacks an unaffected control metric, which is what the Silver bar in `glossary.md` requires.
