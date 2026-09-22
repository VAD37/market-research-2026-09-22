# Nimase, Chen, Qi, Zhao & Hu (arXiv) — GEO-Bench: Benchmarking Ranking Manipulation in Generative Engine Optimization

```yaml
source:          Ojas Nimase, Zhe Chen, Gengpei Qi, Yue Zhao, Xiyang Hu
url_or_doc_id:   arxiv.org/abs/2605.29107
published:       2026-05-27 (v1); revised 2026-05-30 (v2)
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            4
tier_reason:     preprint, code and benchmark datasets released at github.com/glad-lab/geobench — no venue/peer-review stated — academic table row "preprint with code and prompt set"
source_label:    analyst-derived
lane:            D
sub_market:      organic recommendation
engine:          Llama-3.1-8B-Instruct (target ranking LLM); Vicuna-7B (perplexity reference model)
metric_kind:     visibility
supersedes:      none
captured:        abstract, results table and code-release statement (via arxiv.org/html/2605.29107v2 full-text extraction)
technique:       corpus seeding / ranking manipulation — unifies adversarial content-rewriting attacks (incl. an "Authoritative" rewriting strategy) and defenses under one benchmark protocol
models_tested:   Llama-3.1-8B-Instruct, Vicuna-7B
date_window:     not stated in extracted passages
measured_effect: yes — Normalized Rank Gain (NRG) by method/dataset; "Authoritative" rewriting reaches NRG 0.83 on C-SEO Bench (16,360 items, 6 domains), tying the top "LLM Guidance" method, "with zero keyword violations and a 0.74 perplexity ratio"
vertical:        none named (datasets span books, debate, news, retail, videogames, web)
```

## Verbatim

### Abstract (paraphrase-extracted framing, confirmed against page)

GEO-Bench "evaluat[es] ranking-manipulation attacks under one protocol," unifying adversarial and defensive strategies. Tests five datasets against Llama-3.1-8B-Instruct, measuring attack effectiveness and stealth using metrics including NRG (Normalized Rank Gain) and perplexity ratios. Findings: "black-box content rewriting matches or exceeds gradient-based attacks" while producing more natural text, and "access model does not predict attack strength."

### Datasets

Ragroll: 399 products across 50 categories. STSData: 30 products across 3 categories. RewriteToRank: 10,000 items (evaluated on a 20-category, 10-item-per-category subsample). LLM Rank Optimizer: 40 items across 4 categories. C-SEO Bench: 16,360 items across 6 domains (books, debate, news, retail, videogames, web).

### Results table (NRG, representative rows)

| Method | Ragroll | STSData | RewriteToRank | C-SEO Bench |
|---|---|---|---|---|
| TAP | 0.49 | 0.57 | 0.33 | 0.47 |
| Authoritative | 0.60 | 0.37 | 0.22 | 0.83 |
| StealthRank | 0.43 | 0.43 | 0.05 | 0.08 |
| STS | 0.45 | 0.60 | 0.06 | 0.18 |

"Authoritative rewriting ties LLM Guidance for the highest NRG (0.83) while reaching zero keyword violations and a 0.74 perplexity ratio" on C-SEO Bench.

### Code release

"The code is available at https://github.com/glad-lab/geobench"

## Pull notes — mechanical only

- Fetched via WebFetch (arxiv.org/abs/2605.29107 for metadata, arxiv.org/html/2605.29107v2 for full text), both 200.
- "Authoritative" here names one of the benchmark's attack strategies (content rewritten to sound authoritative) rather than literal placement in a third-party high-citation source; filed as academic mechanism/technique evidence per `query-book.md` academic set row "GEO-Bench" mapped to P5-c1.
- No Comments field with venue information was surfaced in this pull; recorded as preprint on the strength of the code release alone, per tier_reason.
