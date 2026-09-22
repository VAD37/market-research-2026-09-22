# arXiv 2601.00912 — The Discovery Gap: How Product Hunt Startups Vanish in LLM Organic Discovery Queries

```yaml
source:          arXiv preprint; author Amit Prakash Sharma (Indian Institute of Technology Patna)
url_or_doc_id:   https://arxiv.org/abs/2601.00912
published:       2026-01-01 (v1 submission date)
pull_date:       2026-09-22
pull_method:     fetch (WebFetch)
pull_purpose:    evidence about a number
tier:            5
tier_reason:     preprint without code/prompt-set publication confirmed in this pull, per trust-rubric.md's academic table. Solo-authored, university-affiliated; no vendor relationship found on the page, so no vendor-authored bias flag applied.
source_label:    analyst-derived
lane:            D
sub_market:      organic recommendation
engine:          ChatGPT (gpt-4o-mini), Perplexity (sonar with web search)
metric_kind:     visibility — brand-name recognition rate versus discovery-style recommendation rate, not traffic or sales
supersedes:      none
captured:        full abstract, including all stated statistics and correlation coefficients
technique:       review and listicle manufacture (tested here as one hypothesized lever within "Generative Engine Optimization" broadly — the paper does not isolate review/listicle manufacture from other GEO tactics; see pull notes)
models_tested:   ChatGPT (gpt-4o-mini), Perplexity (sonar with web search)
date_window:     sample drawn from "the 2025 Product Hunt leaderboard"; query-run date not separately stated beyond the 2026-01-01 arXiv submission date — unknown — checked arxiv.org/abs only, 2026-09-22
measured_effect: yes (negative result) — headline figures verbatim: name-recognition queries scored "99.4% for ChatGPT and 94.3% for Perplexity", but discovery-style queries ("What are the best AI tools launched this year?") "collapsed to 3.32% and 8.29% respectively" -- "a gap of 30-to-1 for ChatGPT". Central finding verbatim: "Generative Engine Optimization (GEO)... showed no correlation with actual discovery rates. Products with high GEO scores were no more likely to appear in organic queries than products with low scores." What did correlate: for Perplexity, "referring domains (r = +0.319, p < 0.001) and Product Hunt ranking (r = -0.286, p = 0.002)"; after data cleaning, "community presence also emerged as significant (r = +0.395, p = 0.002)"
vertical:        none named — sample is Product Hunt-listed startups generally (software/tech products), not mapped to skincare/beauty, B2B SaaS, or high-CPA regulated as such; many Product Hunt launches are software/SaaS-adjacent by the platform's own nature, but the paper does not itself use a "B2B SaaS" or any other of this programme's vertical labels
```

## Verbatim

### Abstract (arxiv.org/abs/2601.00912)

"When someone asks ChatGPT to recommend a project management tool, which products show up in the response? And more importantly for startup founders: will their newly launched product ever appear? This research set out to answer these questions. I randomly selected 112 startups from the top 500 products featured on the 2025 Product Hunt leaderboard and tested each one across 2,240 queries to two different large language models: ChatGPT (gpt-4o-mini) and Perplexity (sonar with web search). The results were striking. When users asked about products by name, both LLMs recognized them almost perfectly: 99.4% for ChatGPT and 94.3% for Perplexity. But when users asked discovery-style questions like 'What are the best AI tools launched this year?' the success rates collapsed to 3.32% and 8.29% respectively. That's a gap of 30-to-1 for ChatGPT. Perhaps the most surprising finding was that Generative Engine Optimization (GEO), the practice of optimizing website content for AI visibility, showed no correlation with actual discovery rates. Products with high GEO scores were no more likely to appear in organic queries than products with low scores. What did matter? For Perplexity, traditional SEO signals like referring domains (r = +0.319, p < 0.001) and Product Hunt ranking (r = -0.286, p = 0.002) predicted visibility. After cleaning the Reddit data for false positives, community presence also emerged as significant (r = +0.395, p = 0.002). The practical takeaway is counterintuitive: don't optimize for AI discovery directly. Instead, build the SEO foundation first and LLM visibility will follow."

Methodology as stated in the abstract: 112 startups sampled from the Product Hunt top-500 leaderboard (2025); 2,240 total queries; two models (ChatGPT gpt-4o-mini, Perplexity sonar with web search).

## Pull notes — mechanical only

- Retrieved via `WebFetch` against the arXiv abstract page. The full abstract is quoted in full above (arXiv abstract pages are static HTML; low risk of paraphrase by the fetch tool for this short a passage).
- This paper tests "Generative Engine Optimization" as a composite "GEO score" and does **not** isolate review-and-listicle manufacture as a distinct independent variable from other GEO tactics (on-page content, structured data, backlinks, etc.) — it is cited in this cluster as the closest available evidence bearing on H5's kill condition ("no Pass 5 technique with published before-and-after"), not as a technique-specific before/after test of review or listicle manufacture in particular. Recorded as a negative correlational result on GEO broadly, with the caveat that "GEO score" as the paper defines it is not disclosed in the abstract to include or exclude review/listicle seeding specifically. `unknown — checked the abstract only, not the full methodology section defining "GEO score", 2026-09-22`.
- What did predict discovery for Perplexity — referring domains, Product Hunt ranking, and (after cleanup) "community presence" from Reddit — sits closer to classical SEO/backlink and community-mention signals than to review/listicle manufacture specifically.
- No figure is given for ChatGPT's correlate-of-visibility results (the abstract states the correlation findings "for Perplexity" only) — whether the same or different signals predicted ChatGPT discovery is not stated in the abstract. `unknown — checked the abstract only, 2026-09-22`.
- Whether code, the 2,240-query prompt list, or per-startup GEO scores are published was not confirmed in this pull. `unknown — checked arxiv.org/abs only, 2026-09-22`.
