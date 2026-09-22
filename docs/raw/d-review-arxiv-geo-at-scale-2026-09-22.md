# arXiv 2606.20065 — Generative Engine Optimization at Scale: Measuring Brand Visibility Across AI Search Engines

```yaml
source:          arXiv preprint; author Pratyush Kumar (Ranqo)
url_or_doc_id:   https://arxiv.org/abs/2606.20065
published:       2026-06-18 (v1 submission date)
pull_date:       2026-09-22
pull_method:     fetch (WebFetch)
pull_purpose:    evidence about a number
tier:            5
tier_reason:     "Paper measuring a vendor's own product, vendor-authored" per trust-rubric.md's academic table — the sole named author is affiliated with Ranqo, the AI-visibility tracking platform whose own tracked-brand data ("Ranqo" named explicitly as the data source) the paper analyzes. Bias flagged: this paper measures the category the author's own company sells into.
source_label:    vendor-reported
lane:            D
sub_market:      organic recommendation
engine:          ChatGPT, Claude, Perplexity, Gemini (named in the abstract as the engines/context the "100K+ prompt responses" were drawn from); one worked example inside the paper separately names "all five engines" for a CRM sub-study (five, not four — the fifth is not resolved in this pull)
metric_kind:     visibility — citation share and mention/citation rate by content-format and brand-tier, not traffic or sales
supersedes:      none
captured:        full abstract; a search of the HTML full text for vertical/industry breakdowns and brand examples
technique:       review and listicle manufacture
models_tested:   ChatGPT, Claude, Perplexity, Gemini (general corpus); the CRM sub-study separately names ten CRM brands (Salesforce, HubSpot, Zoho, Pipedrive, Freshsales, Monday Sales CRM, Copper, Insightly, Capsule, Close) sampled "ten times" across "all five engines" in January 2026
date_window:     "between March and May 2026" (general 100K+ response corpus); the CRM sub-study is dated separately, "in January 2026"
measured_effect: yes (visibility-only, correlational, not before/after) — headline figure verbatim: "the highest-leverage page is the ranked 'best-of' listicle, the most-cited content format at about 21% of all citations." This is a snapshot measurement of what AI engines already cite most, not a before/after test of whether manufacturing more listicles increases citation of a specific brand — it does not meet the H5 bar (published before-and-after with prompt set and n) on its own
vertical:        none of this research programme's three verticals (skincare/beauty, B2B SaaS, high-CPA regulated) is named as such. The paper's own methodological caveat, quoted verbatim below, states the tracked-brand sample "skew[s] toward SaaS, retail-execution, fintech, and Indian DTC" — SaaS is named; skincare/beauty, and high-CPA-regulated (cards, insurance, supplements) are not named anywhere the search below reached
```

## Verbatim

### Abstract (arxiv.org/abs/2606.20065)

"People increasingly get answers straight from AI search engines like ChatGPT, Claude, Perplexity, and Gemini rather than scrolling search results. Brands that once focused on search engine optimization (SEO) must now optimize for how these engines represent, cite, and recommend them -- a shift variously called Generative Engine Optimization (GEO), Answer Engine Optimization (AEO), and AI Search Visibility. We treat AEO and AI Visibility as part of GEO, and study how to measure brand visibility across AI engines: what they value when they cite a brand, which sources they rely on, and what content large language models surface. The hard case is everyone outside the already-authoritative top brands -- SMEs, D2C brands, creators, and early-stage startups. We analyze 100K+ prompt responses across 100+ brands tracked on Ranqo between March and May 2026. First visibility runs form a clear three-tier brand-stature ladder: global household names (e.g., Stripe, Nike) appear in 73% of relevant AI answers on their first run; established mid-market and regional brands (e.g., Olipop, Klaviyo) in 44%; niche and small brands in just 11% -- about 30 percentage points per step. When engines cite sources, about 78% go to corporate websites; among non-corporate sources YouTube leads, ahead of Reddit, editorial media, and Wikipedia. The highest-leverage page is the ranked 'best-of' listicle, the most-cited content format at about 21% of all citations. Sentiment is the unstable signal: whether a brand is framed positively or negatively flips about 6.7 times more often than whether it is mentioned at all. These findings provide a first large-scale baseline for measuring GEO: AI brand visibility can be measured, differs by platform, and varies strongly by brand maturity. We close by proposing seven v1.1 protocols to test whether specific recommendations can causally improve AI visibility."

### CRM sub-study passage (located by a targeted full-text search, quoted as returned)

"50 unbranded prompts across the six categories, sent to all five engines ten times (2,500 responses, 9,600+ brand mentions), tracking ten CRM brands (Salesforce, HubSpot, Zoho, Pipedrive, Freshsales, Monday Sales CRM, Copper, Insightly, Capsule, and Close), in January 2026."

### Vertical-skew caveat, quoted as returned

"The brands skew toward SaaS, retail-execution, fintech, and Indian DTC, so we do not claim category representativeness."

## Pull notes — mechanical only

- Retrieved via `WebFetch` against the arXiv abstract page and, separately, the HTML full-text page with a targeted prompt asking specifically for vertical/industry breakdowns and named brand examples — the tool reported "the paper does not provide a detailed industry breakdown table or comprehensive categorization of all 102 tracked brands", so the vertical read above rests on the one skew sentence quoted, not a full per-brand industry tally.
- The 21%-listicle-citation figure is the strongest single measured data point this cluster found bearing on the review-and-listicle-manufacture technique's *effect* (Q3), but it measures listicles' existing share of citations in a snapshot corpus, not a causal or before/after test of manufacturing new listicles to move a specific brand's citation rate — the paper's own close ("seven v1.1 protocols to test whether specific recommendations can causally improve AI visibility") states in its own words that the causal test has not yet been run. Recorded against H5 as visibility-only evidence, not as a confirm.
- Whether code, the 100K-response dataset, or the "Ranqo" tracking methodology are published beyond this paper was not confirmed in this pull. `unknown — checked arxiv.org/abs and one full-text HTML query only, 2026-09-22`.
- "All five engines" (CRM sub-study) versus "ChatGPT, Claude, Perplexity, and Gemini" (four, main abstract) is the paper's own inconsistency as captured by this pull — the fifth engine in the CRM sub-study was not identified within this pull's search. `unknown — checked the abstract and one full-text query only, 2026-09-22`.
