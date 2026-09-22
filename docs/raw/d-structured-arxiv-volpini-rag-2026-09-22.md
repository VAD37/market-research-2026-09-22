# arXiv 2603.10700v1 — Structured Linked Data as a Memory Layer for Agent-Orchestrated Retrieval

```yaml
source:          arXiv preprint, authors Andrea Volpini, Elie Raad, Beatrice Gamba, David Riccitelli
url_or_doc_id:   https://arxiv.org/abs/2603.10700v1 ; PDF https://arxiv.org/pdf/2603.10700v1
published:       2026-03-11
pull_date:       2026-09-22
pull_method:     fetch (arXiv API for metadata; arxiv.org/html/2603.10700v1 for full text)
pull_purpose:    evidence about a number
tier:            5
tier_reason:     academic table override — "paper measuring a vendor's own product, vendor-authored" takes precedence over the "preprint with code and prompt set" tier-4 default. Lead author Andrea Volpini is founder/CEO of WordLift, a structured-data/schema.org SEO vendor; one of the four test domains ("WordLift Blog") is the vendor's own property. Bias flagged per trust-rubric.md
source_label:    vendor-reported
lane:            D
sub_market:      organic recommendation
engine:          Google Agent Development Kit (ADK) agent orchestrating Vertex AI Vector Search 2.0; generation model Gemini 2.5 Flash; evaluation/LLM-judge model Gemini 3.0 Flash Preview; embeddings gemini-embedding-001 / text-embedding-005. Not a test of any priority-1/2 consumer chat assistant directly — a RAG pipeline built on Google Cloud infrastructure
metric_kind:     visibility
supersedes:      none
captured:        full text (HTML rendering; tables 2, 3, 5 and the qualitative Table 3 comparison captured; some per-domain table rows partially captured, see pull notes)
```

## Verbatim

### Abstract (from the arXiv listing)

"Retrieval-Augmented Generation (RAG) systems typically treat documents as flat text, ignoring the structured metadata and linked relationships that knowledge graphs provide. In this paper, we investigate whether structured linked data, specifically Schema.org markup and dereferenceable entity pages served by a Linked Data Platform, can improve retrieval accuracy and answer quality in both standard and agentic RAG systems. We conduct a controlled experiment across four domains (editorial, legal, travel, e-commerce) using Vertex AI Vector Search 2.0 for retrieval and the Google Agent Development Kit (ADK) for agentic reasoning. Our experimental design tests seven conditions: three document representations (plain HTML, HTML with JSON-LD, and an enhanced agentic-optimized entity page) crossed with two retrieval modes (standard RAG and agentic RAG with multi-hop link traversal), plus an Enhanced+ condition that adds rich navigational affordances and entity interlinking. Our results reveal that while JSON-LD markup alone provides only modest improvements, our enhanced entity page format, incorporating llms.txt-style agent instructions, breadcrumbs, and neural search capabilities, achieves substantial gains: +29.6% accuracy improvement for standard RAG and +29.8% for the full agentic pipeline. The Enhanced+ variant, with richer navigational affordances, achieves the highest absolute scores (accuracy: 4.85/5, completeness: 4.55/5), though the incremental gain over the base enhanced format is not statistically significant. We release our dataset, evaluation framework, and enhanced entity page templates to support reproducibility."

### Conditions tested (seven, C1–C6+)

"C1 Plain HTML, Standard RAG, H1 baseline. C2 HTML + JSON-LD, Standard RAG, H1 treatment. C3 Enhanced entity, Standard RAG, H3 baseline. C4 Plain HTML, Agentic RAG, H2 baseline. C5 HTML + JSON-LD, Agentic RAG, H2 treatment. C6 Enhanced entity, Agentic RAG, H2+H3 treatment. C6+ Enhanced+ entity, Agentic RAG, H4 treatment."

"Our four hypotheses are: H1: Adding Schema.org JSON-LD to HTML documents improves RAG accuracy and completeness (C2 vs. C1). H2: Agentic RAG with link traversal outperforms standard RAG on the same document format (C5 vs. C2). H3: Enhanced entity pages, designed for agentic discoverability, yield the highest [accuracy/completeness — sentence truncated in this extraction]."

### Dataset

"Entities were collected from four Linked Data Platforms using GraphQL-based entity search, yielding structured data in JSON-LD format with Schema.org typing... WordLift Blog (editorial): 16 entities, 22 queries. Blog articles about SEO, knowledge graphs, and AI content. Express Legal Funding (legal): 32 entities, 111 queries. Legal concepts including pre-settlement funding, personal injury, structured settlements, and regulatory topics. SalzburgerLand (travel): 54 entities, 79 queries. Restaurants, alpine huts, and tourist establishments in the Salzburg region of Austria. BlackBriar (e-commerce): 56 entities, 137 queries. Outdoor gear... pricing, and product specifications. In total, the dataset comprises 158 entities and 349 test queries."

"Test queries were generated using template-based generation for three query types: factual (direct attribute lookup), relational (requiring link traversal to related entities)... All seven conditions are evaluated on the identical set of 349 queries, ensuring fair apples-to-apples comparison."

### Evaluation

"All responses are evaluated by an independent LLM judge (Gemini 3.0 Flash)..." "We executed the full experiment: 349 queries × 7 conditions = 2,443 individual evaluations, yielding 2,439 valid results after excluding error cases (1 in C4, 3 in C5)."

### Table 2 — mean accuracy and completeness by condition (± values are standard deviation)

| Condition | Accuracy | Completeness |
|---|---|---|
| C1 Plain HTML, Std. | 3.62 ± 1.82 | 3.01 ± 1.94 |
| C2 HTML+JSON-LD, Std. | 3.89 ± 1.70 | 3.33 ± 1.85 |
| C3 Enhanced, Std. | 4.69 ± 0.95 | 4.45 ± 1.25 |
| C4 Plain HTML, Agent. | 4.36 ± 1.33 | 3.98 ± 1.60 |
| C5 HTML+JSON-LD, Agent. | 4.40 ± 1.21 | 4.00 ± 1.54 |
| C6 Enhanced, Agent. | 4.70 ± 0.82 | 4.38 ± 1.20 |
| C6+ Enhanced+, Agent. | 4.85 ± 0.50 | 4.55 ± 1.06 |

"Figure 3: Mean accuracy and completeness scores by experimental condition. Enhanced entity pages (C3, C6, C6+) dramatically outperform plain HTML and JSON-LD conditions. C6+ achieves the highest scores. Error bars show 95% confidence interval[s]."

### Key results (Section 4)

"...enhanced entity pages (C3) yield dramatic improvements: accuracy 4.69 vs. 3.62 (Δ=+1.04, p<10⁻²¹, d=0.60), representing a +29.6% improvement with a medium effect size."

"4.3 H2: Agentic RAG Amplifies Structured Data Gains — Comparing agentic RAG (C5) with standard RAG (C2) on the same HTML+JSON-LD documents: Accuracy: C5 (4.40) vs. C2 (3.89), Δ=+0.50, t=-5.22, p_adj=4.0×10⁻⁶, d=0.30. Completeness: C5 (4.00) vs. C2 (3.33), Δ=+0.74..."

"...our enhanced entity page format—incorporating llms.txt-style agent instructions, breadcrumbs, and neural search capabilities—achieves substantial gains: +29.6% accuracy improvement for standard RAG (p<10⁻²¹, d=0.60) and +29.8% for the full agentic pipeline (p<10⁻²¹, d=0.61). The Enhanced+ variant, with richer navigational affordances, achieves the highest absolute scores (accuracy: 4.85/5, completeness: 4.55/5) though the incremental gain over the base enhanced format is not statistically significant [attributed to a paired comparison, not separately quoted with its own p-value in the extracted text]."

### Per-query-type breakdown (Table 5, referenced)

"Factual queries benefit most from enhanced pages: C3 (4.57) vs. C1 (2.74), a +66.8% improvement... C6+ achieves the highest factual accuracy (4.81). Relational queries show consistently high scores across conditions (C1: 4.48, C6+: 4.85)..."

### Per-domain results and domain-composition caveat (authors' own words)

"Domain composition caveat. Our dataset is not uniformly distributed: BlackBriar accounts for 39% of queries (n=137) yet contributes virtually no improvement due to its ceiling-level baseline, while WordLift Blog represents only 6% (n=22)..."

"BlackBriar (e-commerce, n=137) achieves near-perfect scores across all conditions (C1: 4.92, C3: 4.91, C6+: 4.99, Δ=+0.07). This is expected under the li[mitation that ceiling effects suppress measurable gains where the baseline is already near-maximal]."

"SalzburgerLand (travel, n=79) shows the most dramatic improvement from enhanced pages: C3 (4.92) vs. C1 (2.19), Δ=+2.47 for C6+..."

"WordLift Blog (editorial, n=22) benefits most from enhanced pages: C3 (4.55) and C6+ (4.64) dramatically outperform plain HTML conditions (C1: 1.91, C2: 1.73)... We note that this domain has the smallest sample size (n=22) and its results should be interpreted with appropriate caution."

"Express Legal Funding (legal, n=111) benefits substantially from t[he enhanced format — sentence continuation not fully captured]."

### Reproducibility

"We release our dataset, evaluation framework, and enhanced entity page templates to support reproducibility" (abstract); arXiv comment field: "33 pages, 7 figures, reproducibility appendix, dataset/evaluation framework/enhanced entity page templates released with the paper."

## Pull notes — mechanical only

- Retrieved via arXiv API (search `abs:"llms.txt"`, which this paper matched on its "llms.txt-style agent instructions" phrasing) for discovery/metadata, then full text via `arxiv.org/html/2603.10700v1`, tag-stripped with `sed`. PDF not separately parsed. Some table rows (Express Legal Funding's full per-domain sentence; the H3/H4 hypothesis-statement tail; the C6+ vs. C6 significance-test figure) were truncated by this extraction pass and are marked incomplete inline above; the core headline figures (+29.6%, +29.8%, the full Table 2 condition means, p-values, effect sizes, n=349 queries / 158 entities / 4 domains) were captured in full.
- **Vendor-authorship bias, flagged per trust-rubric.md**: lead author Andrea Volpini is the founder/CEO of WordLift, a commercial structured-data/schema.org/knowledge-graph SEO product; co-authors Elie Raad, Beatrice Gamba and David Riccitelli are also WordLift-affiliated per public professional profiles (not independently re-verified in this pull, noted as the authors' stated institutional affiliation is not printed on the arXiv abstract page itself). One of the four test domains, "WordLift Blog," is literally the vendor's own property, and the paper's "enhanced entity page" treatment format is a structured-data product design very close to what WordLift sells. This is the trust-rubric discard-on-sight pattern "Vendor measuring the thing it sells" — **not discarded** here because the method, n, dates, effect sizes and a released dataset/eval-framework are all present (the rubric excludes such a paper only when it is *also* a listicle), but downgraded to tier 5 with bias flagged rather than the tier-4 "preprint with code" default, per the academic table's explicit vendor-authored override.
- No date window is separately stated for when the 2,443 evaluations were actually run (only the arXiv submission date, 2026-03-11, and the "we executed the full experiment" language, undated) — recorded as `unknown — checked arxiv.org/abs/2603.10700v1 2026-09-22` for a distinct experiment-run date apart from the publication date.
- **This is the strongest published "before/after, with prompt set and n" measured-effect evidence found in this cluster for H5** ("Corpus seeding measurably moves an answer" — here, structured-data/llms.txt-style formatting measurably moves RAG answer accuracy). It measures a **controlled RAG pipeline the authors built** (Google ADK + Vertex AI Vector Search 2.0 + Gemini-family models), not a live priority-1/2 consumer chat assistant's production answer surface — the census records this distinction: it is evidence that the underlying *mechanism* (retrieval systems reward richer structured/agent-readable pages) works in a controlled academic RAG setup, not direct evidence that ChatGPT, Claude, Gemini, Perplexity, Copilot, or Amazon's production surfaces behave identically.
- The domain-composition caveat and the explicit "smallest sample size... interpreted with appropriate caution" line are the authors' own words, carried here per trust-rubric.md's "Trust rises when... uncertainty is quantified, or its absence is admitted."
