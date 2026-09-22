# Aggarwal, Murahari, Rajpurohit, Kalyan, Narasimhan & Deshpande (arXiv/KDD 2024) — GEO: Generative Engine Optimization

```yaml
source:          Pranjal Aggarwal, Vishvak Murahari, Tanmay Rajpurohit, Ashwin Kalyan, Karthik Narasimhan, Ameet Deshpande
url_or_doc_id:   arxiv.org/abs/2311.09735
published:       2023-11-16 (v1); revised 2024-05-28 (v2), 2024-06-28 (v3, current)
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            3
tier_reason:     peer-reviewed (Comments field: "Accepted to KDD 2024") and code/data released at generative-engines.com/GEO/ and github.com/GEO-optim/GEO — academic table row "peer-reviewed, data or code published"; not raised to tier 2 because no independent replication of this paper's own causal claim was found in this pull (the critical survey pulled separately, `d-seeding-critical-survey-2026-09-22.md`, critiques rather than replicates it)
source_label:    analyst-derived
lane:            D
sub_market:      organic recommendation
engine:          answer generation: GPT-3.5-turbo (OpenAI, 2022); evaluation: G-Eval per Liu et al. 2023a, sub-metrics scored by GPT-3.5; real-world validation on Perplexity.ai
metric_kind:     visibility
supersedes:      none
captured:        abstract, methodology, results and limitations passages (via arxiv.org/html/2311.09735 full-text extraction)
technique:       corpus seeding adjacent — this is the field's foundational paper; two of its nine optimization methods, "Cite Sources" and "Quotation Addition," are the closest fit to citing/drawing on external authoritative sources, though the technique operates on the content creator's own page rather than a third-party platform
models_tested:   GPT-3.5-turbo (2022-era snapshot; exact model version date not further specified) — stale per query-book.md date rule; recorded as evidence about 2024, not about 2026-09
date_window:     paper spans 2023-11-16 to 2024-06-28 (final revision); no narrower experiment-run date window stated in extracted passages
measured_effect: yes — "GEO can boost visibility by up to 40%"; by method (Position-Adjusted Word Count): Quotation Addition +41%, Statistics Addition +33%, Cite Sources +28%, Fluency Optimization +29%; real-world Perplexity.ai test: +37% Subjective Impression, +22% Position-Adjusted Word Count over baseline
vertical:        none named (25 general domains, e.g. Arts, Health, Games)
```

## Verbatim

### Methodology (extracted passages)

Query corpus: "10000 queries from diverse domains and sources, adapted for generative engines," spanning "25 diverse domains such as Arts, Health, and Games." Sources drawn from "nine different sources" including MS Marco, ORCAS-1, Natural Questions, AllSouls, LIMA, Davinci-Debate, Perplexity.ai Discover, ELI5, and GPT-4 Generated Queries.

Answer generation: GPT-3.5-turbo (OpenAI, 2022). Evaluation: "G-Eval (Liu et al., 2023a), the current state-of-the-art for evaluation with LLMs"; "Each sub-metric is evaluated using GPT-3.5."

### Results

Headline: "GEO can boost visibility by up to 40% in generative engine responses."

By method (Position-Adjusted Word Count): Quotation Addition 41%, Statistics Addition 33%, Cite Sources 28%, Fluency Optimization 29%.

Technique description: "Cite Sources & 5. Quotation Addition: Adds relevant citations and quotations from credible sources respectively." "Including citations, quotations from relevant sources, and statistics can significantly boost source visibility, with an increase of over 40%."

Real-world validation (Perplexity.ai): "37% on Subjective Impression" and "22% improvement over baseline" on Position-Adjusted Word Count.

### Limitations (verbatim)

"While we rigorously test our proposed methods on two generative engines, including a publicly available one, methods may need to adapt over time as GEs evolve, mirroring the evolution of SEO. Additionally, despite our efforts to ensure the queries in our GEO-bench closely resemble real-world queries, the nature of queries can change over time, necessitating continuous updates. Further, owing to the black-box nature of search engine algorithms, we didn't evaluate how GEO methods affect search rankings. However, we note that changes made by GEO methods are targeted changes in textual content, bearing some resemblance with SEO methods, while not affecting other metadata such as domain name, backlinks, etc, and thus, they are less likely to affect search engine rankings. Further, as larger context lengths in language models become economical, it is expected that future generative models will be able to ingest more sources, thus reducing the impact of search rankings. Lastly, while every query in our proposed GEO-bench is tagged and manually inspected, there may be discrepancies due to subjective interpretations or errors in labeling."

### Code/data release

Publicly released at https://generative-engines.com/GEO/ and https://github.com/GEO-optim/GEO.

## Pull notes — mechanical only

- Fetched via WebFetch (arxiv.org/abs/2311.09735 for metadata, arxiv.org/html/2311.09735 for full-text extraction), both 200.
- Model-staleness flag applied per `docs/sources/query-book.md` date rules: GPT-3.5-turbo (2022) has since been superseded; this paper's 40% figure is evidence about generative-engine behavior circa 2023-2024, not a claim about 2026-09 engines. Retained per root CLAUDE.md: "A 2024 result on a retired model is evidence about 2024."
- This paper's own "GEO-bench" (10,000 queries, 25 domains, nine sources) is a different artifact from the unrelated "GEO-Bench" benchmark pulled separately in this cluster (arXiv:2605.29107, `d-seeding-geo-bench-2026-09-22.md`); the name collision is recorded here mechanically and not resolved.
