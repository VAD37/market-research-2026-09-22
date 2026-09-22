# Puerto et al. — C-SEO Bench: Does Conversational SEO Work?

```yaml
source:          Haritz Puerto, Martin Gubri, Tommaso Green, Seong Joon Oh, Sangdoo Yun
url_or_doc_id:   arxiv.org/abs/2506.11097 (v3); accepted NeurIPS 2025 Datasets & Benchmarks Track
published:       2025-06-06 (v1); last revised 2025-10-20 (v3)
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            4
tier_reason:     preprint with code and data released ("Our code and data are available at this https URL and this https URL"), accepted at NeurIPS 2025 Datasets & Benchmarks Track (peer-reviewed venue) — academic table "preprint with code and prompt set" / borders "peer-reviewed, data or code published"; treated as tier 4 pending confirmation the camera-ready proceedings version differs from the preprint text captured here
source_label:    analyst-derived
lane:            D
sub_market:      organic recommendation
engine:          Conversational Search Engines generically; ranker models tested: GPT-4o-mini, Claude Haiku 3.5 (named "Haiku 3.5" in the paper's own results tables)
metric_kind:     visibility
supersedes:      none
captured:        abstract, method (datasets, ranker models, statistical test), results tables for the nine white-hat C-SEO methods (Authoritative, Statistics, Citations, Fluency, Unique Words, and others) across six domains, limitations
technique:       content written to satisfy known citation preferences — direct replication test of the foundational GEO paper's own nine content-rewrite methods, under a harder multi-actor, multi-domain protocol
models_tested:   GPT-4o-mini (primary ranker); Claude Haiku 3.5 (second ranker, separate results table); GPT-4o and GPT-4o-mini also used for query generation/expansion
date_window:     data collection window not separately stated beyond the arXiv submission/revision dates above (2025-06-06 to 2025-10-20)
measured_effect: yes — mixed/mostly-null: "Out of 54 cases, we uncover only three where the ranking improvements are statistically significant"; several C-SEO methods (e.g., Statistics) show statistically significant NEGATIVE effects in specific domains
vertical:        none named — six domains: Retail (e-commerce, "General e-commerce products from the Amazon website"), Games, Books, Web (Google Search user queries), News, Debate
```

## Verbatim

### Abstract

"Large Language Models (LLMs) are transforming search engines into Conversational Search Engines (CSE). Consequently, Search Engine Optimization (SEO) is being shifted into Conversational Search Engine Optimization (C-SEO). We are beginning to see dedicated C-SEO methods for modifying web documents to increase their visibility in CSE responses. However, they are often tested only for a limited breadth of application domains; we do not know whether certain C-SEO methods would be effective for a broad range of domains. Moreover, existing evaluations consider only a single-actor scenario where only one web document adopts a C-SEO method; in reality, multiple players are likely to competitively adopt the cutting-edge C-SEO techniques, drawing an analogy from the dynamics we have seen in SEO. We present C-SEO Bench, the first benchmark designed to evaluate C-SEO methods across multiple tasks, domains, and number of actors. We consider two search tasks, question answering and product recommendation, with three domains each. We also formalize a new evaluation protocol with varying adoption rates among involved actors. Our experiments reveal that most current C-SEO methods are not only largely ineffective but also frequently have a negative impact on document ranking, which is opposite to what is expected. Instead, traditional SEO strategies, those aiming to improve the ranking of the source in the LLM context, are significantly more effective. We also observe that as we increase the number of C-SEO adopters, the overall gains decrease, depicting a congested and zero-sum nature of the problem. Our code and data are available at this https URL and this https URL."

### Method — the nine content-rewrite methods tested (reused from the foundational GEO paper)

"[The] methods introduced by Aggarwal et al. (2024): 1. Authoritative: Modifies the text to enhance its authority and persuasiveness. 2. Statistics: Introduces statistical elements to increase the perceived technical [depth]... 4. Fluency: Polishes the text to improve grammar and coherence. 5. Unique Words: Incorporates less common words to increase the perceived uniqueness of the te[xt]..." [note: extraction of the full nine-item list was truncated by the plain-text conversion; the remaining named methods visible in the results tables are Citations and Keyword Stuffing, matching the foundational paper's original nine]

### Method — statistical test

"This test allows us to evaluate whether the rank after applying a C-SEO method is statistically significantly smaller than the original rank... We adjust the p-values using the Holm-Bonferroni correction (Holm, 1979) to prevent the multiple comparison problem and to be able to compare multiple C-SEO method[s]."

"C-SEO Bench results GPT-4o-mini. Average and standard deviation of the rank improvements. Bold values are statistically significant (p < 0.05) using Holm–Bonferroni correction. Results in red are significantly negative."

### Results table — GPT-4o-mini ranker, Product Recommendation task (rank-improvement mean ± SD, positive = better)

Method | Retail | Games | Books
---|---|---|---
Authoritative | 0.11 ±1.18 | 0.07 ±1.25 | 0.11 ±0.94
Statistics | -0.07 ±1.00 | 0.00 ±1.11 | -0.11 ±1.04
Fluency | 0.06 ±1.11 | 0.07 ±1.27 | 0.07 ±1.05
Unique Words | 0.09 ±1.09 | 0.02 ±1.20 | 0.04 ±1.04

### Results table — GPT-4o-mini ranker, Question Answering task (rank-improvement mean ± SD)

Method | Web | News | Debate
---|---|---|---
Authoritative | -0.04 ±0.89 | -0.04 ±1.03 | 0.01 ±1.55
Statistics | -0.53 ±1.27 | -0.05 ±1.31 | -0.80 ±1.70
Fluency | 0.03 ±0.89 | -0.01 ±1.08 | 0.32 ±1.64
Unique Words | -0.07 ±0.92 | -0.10 ±1.03 | -0.08 ±1.66

### Results table — Claude Haiku 3.5 ranker, Product Recommendation task (rank-improvement mean ± SD)

Method | Retail | Games | Books
---|---|---|---
Authoritative | -0.53 ±1.29 | -0.20 ±1.05 | -0.34 ±1.06
Statistics | -0.82 ±1.47 | -0.10 ±1.01 | -0.60 ±1.34
Fluency | -0.48 ±1.30 | -0.08 ±1.08 | -0.37 ±1.18
Unique Words | -0.52 ±1.26 | -0.22 ±0.91 | -0.43 ±1.11

[note: results-table cells for "Citations" and "Keyword Stuffing" methods, and the Haiku 3.5 Question-Answering-task table, were present in the source but not fully captured in this extraction pass — the plain-text conversion of the arXiv HTML interleaves multiple result tables without clear boundaries; the rows and domains captured above are representative, not exhaustive, of the full nine-method × six-domain × two-ranker grid]

### Key findings, verbatim

"Out of 54 cases, we uncover only three where the ranking improvements are statistically significant. As detailed in section 4.2, we apply the Wilcoxon signed-rank test to check the statistical significance of positive ranking boosts. Among all evaluated methods, only LLM guidance and content impro[vement methods reach significance]... None of the LLM Document Optimization methods achieve significant gains. Best SEO is always statistically significant."

"SEO remains essential. We show that the ranking of the documents in the LLM context is much more influential than any current C-SEO method to determine the document['s citation.]"

"This finding challenges the core assumptions of Aggarwal et al. (2024) that traditional SEO will be outdated by C-SEO. Our results show that sophisticated content modifications are often outweighed by improvements in document ordering in the [retrieval stage]... Therefore, C-SEO methods must be considered as a complement and not a replacement for traditional SEO."

### Limitations, verbatim

"[We] do not examine the potential interplay between traditional SEO and C-SEO methods. Future work could explore new text modification strategies that explicitly target both SEO and C-SEO to explore possible synergist[ic effects]."

## Pull notes — mechanical only

- Fetched via `curl` (fetch method) from `arxiv.org/html/2506.11097` (v3, the same version as the abs page's "last revised" date), then converted to plain text by stripping HTML/MathML tags with a Python regex; this loses exact table cell alignment in a few places, noted above.
- This is the exact paper the foundational GEO survey (Martinez, already in `docs/raw/d-seeding-critical-survey-2026-09-22.md`, P5-c1) calls "the principal empirical corrective" to the foundational GEO paper's claimed gains, citing "only three of 54 method–domain combinations" as statistically significant — the survey's own summary of this paper's finding is confirmed verbatim against the primary source here.
- The paper directly re-tests the SAME nine content-rewrite methods (Authoritative, Statistics, Citations, Fluency, Unique Words, Keyword Stuffing, and others) that the foundational GEO paper (Aggarwal et al. 2024, cited in `d-seeding-geo-foundational-2026-09-22.md`) reported as producing up to +40% visibility gains — this paper's replication under a harder multi-domain, multi-actor protocol finds the opposite for most methods, including statistically significant NEGATIVE effects for Statistics in several domains.
- Code and data release confirmed in the abstract text ("Our code and data are available at this https URL and this https URL") — the underlying anchor tags resolve to `github.com/parameterlab/c-seo-bench` (recovered from the raw HTML's link attributes, not the plain-text-stripped body); the second linked URL (data) was not separately isolated in this pull.
