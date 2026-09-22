# arXiv 2608.27631 — Beyond the Vacuum: Combinatorial Strategy Selection for Competitor-Aware Generative Engine Optimization

```yaml
source:          arXiv preprint; Vaibhav Sourirajan, Yao Zhang, Himanshu Kumar, Sahil Wadhwa, Mann Patel, Amirfarrokh Iranitalab — all affiliated Capital One, AI Foundations (email domain capitalone.com, per full-text check)
url_or_doc_id:   https://arxiv.org/abs/2608.27631 ; full text https://arxiv.org/html/2608.27631
published:       2026-08-27 (v1 submission date)
pull_date:       2026-09-22
pull_method:     fetch (WebFetch)
pull_purpose:    evidence about a number
tier:            5
tier_reason:     "Preprint without code" per trust-rubric.md academic table — no GitHub/HuggingFace link or data-availability statement found in abstract or full-text check. Additionally bias-flagged: all six authors are affiliated with Capital One (a credit-card issuer), a company with a direct commercial interest in how its own products are represented by AI engines, though the paper itself does not test on a named credit-card or financial-services dataset — academic table's "vendor-authored" caveat applied by analogy, reason stated explicitly rather than assumed
source_label:    vendor-reported (bias-flagged per tier_reason; not a study of Capital One's own product, but authored inside a company with a direct commercial stake in the technique's outcome)
lane:            D
sub_market:      organic recommendation
engine:          Rewriting/evaluation models named in full text: gpt-oss-120b, gpt-oss-20b, Llama-3.3-70B-Instruct, gemma-4-31B-it (teacher), gemma-4-E2B-it (student selector). Not a consumer-chat-surface test — a controlled benchmark using open-weight models as the GEO-optimization and scoring substrate
metric_kind:     visibility — "impression metrics" (citation/appearance rate under a fixed scoring benchmark), not traffic or sales
supersedes:      none
captured:        abstract; full-text sections on data/code availability, author affiliation, evaluation datasets, and baseline comparisons, via a targeted WebFetch query
technique:       comparison-page farming — closest available academic proxy: the paper formalizes GEO as a "competitor-aware strategy selection problem," i.e. optimizing content in the presence of competing/comparison content, which is the closest indexed academic work this cluster's searches found to comparison-page or competitor-aware content production. It does not study "X vs Y" or "best X" pages as a named content format
models_tested:   gpt-oss-120b, gpt-oss-20b, Llama-3.3-70B-Instruct, gemma-4-31B-it, gemma-4-E2B-it
date_window:     not stated as a data-collection window beyond the 2026-08-27 submission date
measured_effect: yes (benchmark comparison, not a before/after on a real page) — headline claim verbatim: "We achieve state-of-the-art performance across several impression metrics over existing agentic and single-heuristic methods on both geo-bench and our synthetically augmented competitive dataset geo-bench_comp. Our method also transfers to multiple out-of-distribution datasets, proving effective across domains, queries, and document types." This is a benchmark-vs-baseline result, not a published before-and-after test of one specific comparison page against a real AI answer surface — does not meet the H5 bar on its own
vertical:        none named in the tested content. Author affiliation only (Capital One, AI Foundations) sits in the high-CPA regulated space (credit cards) per this programme's vertical list, but the paper's own experiments run on geo-bench, geo-bench_comp, an "E-Commerce" out-of-distribution dataset, and "Researchy-GEO" — none of which the paper itself labels as credit cards, insurance, or supplements. Recorded as "author affiliation only, not tested vertical" per the cell-attribution rule — not assigned to the regulated-vertical cell by inference
```

## Verbatim

### Abstract (arxiv.org/abs/2608.27631)

"Generative Engine Optimization (GEO) has emerged as a novel paradigm for transforming content to increase visibility in Large Language Model (LLM) responses. Traditional GEO methods, however, select rewriting strategies in isolation, ignoring a critical externality: as adoption of content optimization grows, optimal strategies for rewriting content change. We formalize GEO as a competitor-aware strategy selection problem and propose a two-phase pipeline to solve it: (1) We use Bayesian Optimization of Combinatorial Structures (BOCS) to efficiently search the space of rewriting strategies, (2) We generate preference pairs and grounded reasoning traces from the BOCS black-box observations to fine-tune a language model to analyze a document corpus and propose optimal rewriting strategy combinations. We achieve state-of-the-art performance across several impression metrics over existing agentic and single-heuristic methods on both geo-bench and our synthetically augmented competitive dataset geo-bench_comp. Our method also transfers to multiple out-of-distribution datasets, proving effective across domains, queries, and document types."

### Author affiliation (from full-text check via WebFetch on arxiv.org/html/2608.27631, reported verbatim as found)

"All authors are affiliated with Capital One, AI Foundations... Email domain: capitalone.com"

### Baselines and comparison framing (from full-text check, reported as returned)

The paper "explicitly compares against: '15 single-strategy and 2 agentic baselines' including AutoGEO and AgenticGEO, claiming 'state-of-the-art performance' and 'outperforms all baselines.'"

### Evaluation datasets named (from full-text check, reported as returned)

"geo-bench (original dataset, general queries/documents); geo-bench_comp (augmented competitive version); E-Commerce dataset (out-of-distribution transfer); Researchy-GEO dataset (out-of-distribution transfer)." No specific brand examples or product names were reported as found in the experiments section by this pull's queries.

## Pull notes — mechanical only

- Fetched via `WebFetch` against `arxiv.org/abs/2608.27631` (metadata pass) and `arxiv.org/html/2608.27631` (targeted full-text pass), both 200.
- The abstract page alone, on first fetch, returned no code/data availability information; a second, full-text-targeted fetch was needed to surface the author-affiliation line, which does not appear on the abstract page.
- No GitHub, HuggingFace, or other code/data release URL was located by either fetch. `unknown — checked arxiv.org/abs and one arxiv.org/html query only, 2026-09-22` on whether a release exists elsewhere (e.g. a linked project page not surfaced by this query).
- Whether "geo-bench_comp" (the competitive/comparison-augmented dataset) itself contains anything resembling "X vs Y" or "best X" page structures, as opposed to generic competing-document pairs, was not resolved by this pull's two queries. `unknown — checked two targeted WebFetch queries only, 2026-09-22`.
