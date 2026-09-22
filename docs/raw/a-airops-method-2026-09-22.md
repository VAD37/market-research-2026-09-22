# AirOps — method / how-it-works (AEO scoring + citation tracking)

```yaml
source:          AirOps (airops.com)
url_or_doc_id:   https://www.airops.com/answer-engine-visibility (AEO Readability Score tool + AEO Leaderboard scoring criteria); secondary: https://www.airops.com/blog/new-ai-search-improvements-faster-insights-deeper-visibility-better-decisions (feature-mechanics detail)
published:       /answer-engine-visibility undated (sitemap.xml lastmod 2026-09-20); blog post dated 2026-01-08 ("Amr Shafik, • January 8, 2026")
pull_date:       2026-09-22
pull_method:     fetch (MCP_DOCKER fetch tool, plain HTTP — claude-in-chrome extension reported "not connected" this session)
pull_purpose:    evidence about a number
tier:            6
tier_reason:     vendor's own scoring rubric for a free lead-gen tool, no independent validation, no n or sample disclosed for the "AEO Leaderboard" comparison set beyond "top 50 global SaaS brands" — self-reported methodology, discard-on-sight per trust-rubric does not apply (this is a platform-primary method disclosure, not a proof-of-lift claim) but tiered at 6 because no external check exists
source_label:    vendor-reported
lane:            A
sub_market:      organic recommendation
engine:          n/a
metric_kind:     visibility
supersedes:      none
captured:        first ~6000 characters of /answer-engine-visibility (tool UI + leaderboard scoring for one example company, NinjaOne); full text of the feature-roundup blog post up to its truncation point
```

## Verbatim

### /answer-engine-visibility — "Is Your Content Ready for Answer Engines?"

"Answer engines have raised the content quality bar. See how your top pages stack up—and learn what's costing you visibility."

"### Your AEO Readability Score — Your content needs optimizations to increase visibility. Your average score places you in the lower 40% of our AEO Leaderboard. Sites in this tier often face traffic loss as engines like ChatGPT and even AI Overviews prioritize content that's more agent-friendly: recent, structured, and backed by credible sources. The good news? These gaps are fixable."

"We analyzed a sample of pages and flagged the AEO signals to improve your visibility" — dimensions scored: Overall (0-100), Authority & Evidence, Freshness, Structure, Snippet Extractability [a fifth dimension, "Brand Alignment", appears in the AEO Leaderboard table below but not in the per-page "Top 5/10 pages" table].

Scoring-criteria text, verbatim, per dimension band (example shown is for "Freshness" but the tool displays the same four-band rubric text for each dimension it scores):

"20: No authority signals. 40: Little trust; generic links; vague author. 60: Moderate authority (niche site) or 1 credible citation. 80: Any two of the above. 100: High-authority domain, strong credentials and ≥ 2 reputable citations." [note: this exact rubric text is the "Authority & Evidence" rubric, displayed under a "Freshness" heading in the rendered page — the page's own labelling is internally inconsistent as captured; recorded exactly as it rendered]

"#### ⚠️ Lite Score Limitations
- Only a snapshot of ~10 top URLs—designed to highlight direction, not detail.
- This preview doesn't include brand-specific authority signals (e.g. schema, entity strength)
Contact us for your full scorecard which includes 100+ URLs, deeper diagnostics, and prioritized action plan."

"## AEO Leaderboard — Who's winning in the age of AI answers? We analyzed the top 50 global SaaS brands to uncover which content is built for today's answer engines—ChatGPT, Google AI Overviews/Mode, Gemini, Perplexity—and which is falling behind."

Example row, verbatim (rank #1, NinjaOne): "Overall (0-100) 82 — Authority & Evidence 66 [rubric: 'Roughly half of articles still lack named author bios and ≥2 authoritative outbound citations, limiting trust signals for Google and LLMs.' Score Distribution (83 pages): 5 at <80, 34 at >=80. Scoring Criteria: 20: No authority signals. 40: Little trust; generic links; vague author. 60: Moderate authority (niche site) or 1 credible citation. 80: Any two of the above. 100: High-authority domain, strong credentials and ≥ 2 reputable citations.] — Freshness 90 [rubric: 'While most content has been modified in the last 90 days, ~12% of pages still surface no visible update date or fall outside the freshness window.' Score Distribution (83 pages): 5 at <80, 70 at >=80. Scoring Criteria: 20: No date signals. 40: >365 days. 60: 181-365 days. 80: 91-180 days. 100: ≤90 days.] — Structure 78 [rubric: 'Many pages omit an explicit single H1 tag and rely on partial Article schema, which weakens semantic clarity and rich-result eligibility.' Score Distribution (83 pages): 5 at <80, 74 at >=80. Scoring Criteria: 20: No meaningful structure or schema. 40: Multiple <h1> or messy HTML, minimal schema; avg >30 words. 60: Some hierarchy issues or only basic schema; avg ≤30 words. 80: Minor heading gaps or partial schema; avg ≤25 words. 100: Perfect hierarchy and full Article schema with all properties; avg ≤20 words.] — Snippet Extractability 79 [rubric: 'Long sentences (>25 words) and narrative paragraphs remain on 29% of pages, reducing the likelihood of featured-snippet lifts.' Score Distribution (83 pages): 5 at <80, 59 at >=80. Scoring Criteria: 20: Wall of text; no lists, headings, or question patterns. 40: Long paragraphs with few lists/Q&A; no obvious snippet targets. 60: Some lists or short Q&A lines, but large narrative chunks still dominate; engines can extract, but not effortlessly. 80: At least one strong extractable block plus good list/heading structure; minor issues (e.g., a few long sentences). 100: Multiple direct-answer blocks and most key facts in ≤25-word sentences. Page eligible for featured snippet or FAQ rich result.] — Brand Alignment 85 [rubric: 'Thirteen pages provide generic how-to guidance without weaving in NinjaOne product use-cases, diluting brand reinforcement opportunities.' Score Distribution (83 pages): 5 at <80, 60 at >=80. Scoring Criteria: 20: Completely off-brand. 40: Significant mismatch. 60: Some outdated or missing elements. 80: Minor tone/terminology drift.]"

**Prompt-set / n / method disclosure assessment for this composite score:** the "AEO Readability Score" and "AEO Leaderboard" are rule-based content-quality rubrics (authority signals, content freshness, HTML/schema structure, sentence-length/extractability, brand-term alignment) applied to a **sample of the brand's own pages** — this is not a prompt-run visibility/citation composite (i.e., it does not run a fixed prompt set against AI engines and count mentions/citations). Sample size is disclosed per company ("83 pages" for the NinjaOne example) and the universe is disclosed ("top 50 global SaaS brands"), but no prompt set, prompt count, or per-engine run count is named anywhere on this page. **This page's score is not a prompt-based composite and is out of scope for the H15 prompt-set-disclosure question in the strict sense** — it is recorded here because it is the vendor's only page with an explicit numeric scoring rubric. The separate, prompt-based "visibility, recommendations, citations, sentiment, position" metrics referenced on `/platform` and `/ai-search-visibility` disclose no prompt set, n, or method anywhere pulled — see `a-airops-product-2026-09-22.md`.

### Feature-roundup blog post — mechanics of the citation-tracking feature

Title: "Monthly Feature Roundup: Faster Insights, Deeper Visibility, Better Decisions", byline "Amr Shafik, • January 8, 2026"

"## See where you're cited at a glance, with Citations Matrix — We've introduced a new matrix view in Analytics that makes it easier to understand how often your brand is cited by each AI platform. With the Citations Matrix, you can: Compare citation frequency across AI engines; View performance by Topic, Domain Category, or against competitors; Quickly spot gaps and opportunities without digging through individual prompts. This gives you a clean snapshot of your relative performance."

"## Get a deeper sample set with Multi-Answer Collection — Enterprise customers can now collect multiple AI engine answers per prompt per day to get a larger, more representative sample of responses. Models often vary their recommendations and citations from one response to the next so multiple answers helps you get a more representative snapshot of what's really happening."

"## Know what kind of sites are citing you with Domain Categories" — table of categories: Owned, Competitors, Social, Communities, Reviews, Media, Educational, Marketplaces, Products, Affiliates, Other, each with a description and named examples (e.g. Reviews: "G2, Capterra, NerdWallet, Bankrate, TechRadar"; Media: "TechCrunch, Forbes, The Verge, industry blogs").

"## Prioritize the prompts that matter most with Enhanced Prompt Insights + Tags — The Prompts section now lets you tag and organize prompts based on your priorities."

**n/method note:** "Multi-Answer Collection" confirms AirOps runs **multiple answers per prompt per day** (an explicit, if unquantified, repeated-sampling method) — but no fixed prompt-set name, prompt count, or per-plan n figure is disclosed on this page or on `/pricing` beyond "100 Tracked Prompts & Pages" (Solo) / "250 Tracked Prompts & Pages" (Pro) seen on `/aeo` (see `a-airops-pricing-2026-09-22.md`). **Disclosure verdict: partial — the platform states it tracks a customer-defined, customer-sized prompt set (count disclosed per plan tier) and samples each prompt multiple times per day for Enterprise, but does not disclose the actual prompt wordings, a fixed public prompt-set version, or a run-count (n) methodology page.**

## Pull notes — mechanical only

- `/answer-engine-visibility` fetched with max_length 6000; truncated mid-table (additional leaderboard rows beyond NinjaOne not captured this pull).
- Blog post fetched with max_length 5000; truncated before its concluding section (a partial closing sentence "AirOps helps teams build the content engineering foundations they need, automate structured workflows, strengthen AEO readiness and understand how AI systems surface their brand. AirOps is the partner for this shift, bringing the platform, the media..." was captured and is the cutoff point).
- The internal inconsistency noted above (Authority & Evidence rubric text rendered under a "Freshness" heading) is recorded as found; not corrected.
