# Chen, Wang, Chen & Koudas (arXiv) — Generative Engine Optimization: How to Dominate AI Search

```yaml
source:          Mahe Chen, Xiaoxuan Wang, Kaiwen Chen, Nick Koudas
url_or_doc_id:   arxiv.org/abs/2509.08919
published:       2025-09-10 — stale, published before 2026-06-22 per query-book.md date rule; re-checked against arxiv.org/html/2509.08919 on pull date, no newer revision surfaced
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            5
tier_reason:     preprint, no code/data/query-set release statement found on abs page or html full text (checked 2026-09-22) — academic table row "preprint without code"
source_label:    analyst-derived
lane:            D
sub_market:      organic recommendation
engine:          "ChatGPT, Perplexity, and Gemini" named in the abstract as the AI Search systems studied; aggregate "AI Search" figures not broken out per engine in the extracted passages
metric_kind:     visibility
supersedes:      none
captured:        abstract, experimental-scale and results passages (via arxiv.org/html/2509.08919 full-text extraction)
technique:       corpus seeding — this paper's central finding ("dominate earned media") is the mechanism the cluster targets: placing/earning content in third-party authoritative outlets that AI Search disproportionately cites over brand-owned content
models_tested:   not individually named per engine in extracted passages; aggregate "AI Search" vs. Google comparison
date_window:     Reddit data collection "in August of 2025"; no other date range stated
measured_effect: yes — earned-media citation share, AI Search vs. Google: Automotive/Canada — Google 36.6% Brand / 22.8% Social / 40.6% Earned vs. AI Search 69.1% Earned / 30.9% Brand / 0% Social; Consumer Electronics/USA — Google 32.9% Brand / 15.4% Social / 54% Earned vs. AI Search 92.1% Earned / negligible Social / 22.1% Brand (figures as extracted; note Brand+Earned+Social does not sum to 100% in the AI Search rows as reported — recorded verbatim, not corrected)
vertical:        none of the three fixed verticals named; source uses automotive and consumer electronics as its own vertical examples
```

## Verbatim

### Abstract

"The rapid adoption of generative AI-powered search engines like ChatGPT, Perplexity, and Gemini is fundamentally reshaping information retrieval, moving from traditional ranked lists to synthesized, citation-backed answers. This shift challenges established Search Engine Optimization (SEO) practices and necessitates a new paradigm, which we term Generative Engine Optimization (GEO). This paper presents a comprehensive comparative analysis of AI Search and traditional web search (Google). Through a series of large-scale, controlled experiments across multiple verticals, languages, and query paraphrases, we quantify critical differences in how these systems source information. Our key findings reveal that AI Search exhibit a systematic and overwhelming bias towards Earned media (third-party, authoritative sources) over Brand-owned and Social content, a stark contrast to Google's more balanced mix. We further demonstrate that AI Search services differ significantly from each other in their domain diversity, freshness, cross-language stability, and sensitivity to phrasing. Based on these empirical results, we formulate a strategic GEO agenda. We provide actionable guidance for practitioners, emphasizing the critical need to: (1) engineer content for machine scannability and justification, (2) dominate earned media to build AI-perceived authority, (3) adopt engine-specific and language-aware strategies, and (4) overcome the inherent 'big brand bias' for niche players. Our work provides the foundational empirical analysis and a strategic framework for achieving visibility in the new generative search landscape."

### Experimental scale (extracted, html full text)

"1,000 consumer ranking prompts (10 categories × 100 each)" in the Regional and Vertical Experiment. "100 base queries" across 10 consumer verticals for language and paraphrase sensitivity studies. 5 additional languages tested (Chinese, Japanese, German, French, Spanish) plus English. 8 paraphrase templates tested.

### Results (verbatim figures, as extracted)

Automotive, Canada: "Google: 36.6% Brand, 22.8% Social, 40.6% Earned" vs. "AI Search: 69.1% Earned, 30.9% Brand, 0% Social."

Consumer Electronics, USA: "Google: 32.9% Brand, 15.4% Social, 54% Earned" vs. "AI Search: 92.1% Earned, negligible Social, 22.1% Brand."

Date: Reddit data collection occurred "in August of 2025."

### Limitations

Section 7, titled "Assumptions and Limitations of the Study" — full text truncated in the extraction tool's returned content; not captured verbatim. [note: limitations section present in the source but not retrievable through the extraction method used on this pull]

## Pull notes — mechanical only

- Fetched via WebFetch (arxiv.org/abs/2509.08919 for metadata; arxiv.org/pdf/2509.08919 failed with "maxContentLength size of 10485760 exceeded"; arxiv.org/html/2509.08919 succeeded, 200).
- Limitations section (§7) could not be retrieved verbatim through the html-extraction tool; recorded as a capture gap rather than omitted from the source.
- No vendor or company affiliation is stated on the abs page or in the extracted html text for any of the four authors; filed as analyst-derived on that basis (absence of a stated commercial affiliation), not from any outside knowledge of the authors.
