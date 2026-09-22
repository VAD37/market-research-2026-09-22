# Wen, Liu, Liu, Jiao, Yang, Wu & Tang (arXiv) — SafeGEO: Understanding Generative Engine Optimization Risks in Recommendation Agents

```yaml
source:          Qianfeng Wen, Yifan Simon Liu, Xin Liu, Difan Jiao, Blair Yang, Junda Wu, Zhenwei Tang
url_or_doc_id:   arxiv.org/abs/2606.28356
published:       2026-06-08 (v1); last revised 2026-09-04 (v2)
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            4
tier_reason:     preprint, code (Apache 2.0, github.com/QianfengWen/SafeGEO) and dataset (CC-BY 4.0, huggingface.co/datasets/wieeii/SafeGEO) released — no venue/peer-review stated — academic table row "preprint with code and prompt set"
source_label:    analyst-derived
lane:            D
sub_market:      organic recommendation
engine:          Gemma 4 31B IT, Qwen3.6-27B, Devstral Small 2 24B Instruct, DeepSeek-V4-Flash
metric_kind:     visibility
supersedes:      none
captured:        abstract, results passages, code/data release statement (via arxiv.org/html/2606.28356v2 full-text extraction)
technique:       corpus seeding adjacent — content rewritten to game recommendation-agent citation/selection ("22 GEO attack variants across 600 recommendation cases")
models_tested:   Gemma 4 31B IT, Qwen3.6-27B, Devstral Small 2 24B Instruct, DeepSeek-V4-Flash (described as "frontier-scale validation")
date_window:     not stated in extracted passages
measured_effect: yes — attacked products' top-3 inclusion rate rises "by up to 83.2 percentage points" vs. truthful-rewrite controls; hard-constraint violations rise "by up to 63.8 percentage points"; best single defense (evidence breakdown) reduces target promotion "by up to 39.2 pp" but "does not restore recommendations to the No GEO level"
vertical:        none named
```

## Verbatim

### Abstract (extracted)

The paper "examines how generative engine optimization enables content rewriting to boost visibility in AI systems." SafeGEO is "a testing framework containing 22 GEO attack variants across 600 recommendation cases," measuring whether recommendation agents maintain user-aligned decisions when sources undergo such optimization. "Attacks can elevate flawed products' inclusion rates by up to 83.2 percentage points." Agent-side design mitigations "reduced harmful promotion by up to 39.2 percentage points," but GEO "remains a serious risk despite mitigation."

### Results (verbatim figures)

"up to 83.2 percentage points" increase in flawed-product top-3 inclusion vs. truthful-rewrite controls.

"up to 63.8 percentage points" increase in hard-constraint violations.

Best single defense (evidence breakdown): "up to 39.2 pp" reduction in target promotion. "Even the strongest mitigation does not restore recommendations to the No GEO level."

Model generalization note: "although DeepSeek-V4-Flash is the most recent frontier-scale model we evaluate, it remains highly vulnerable to GEO attacks."

### Code and data release

"Code and the dataset are available." GitHub: https://github.com/QianfengWen/SafeGEO. Dataset: https://huggingface.co/datasets/wieeii/SafeGEO. Code under Apache License 2.0; data under Creative Commons Attribution 4.0 International license.

## Pull notes — mechanical only

- Fetched via WebFetch (arxiv.org/abs/2606.28356 for metadata, arxiv.org/html/2606.28356v2 for full text), both 200.
- The paper studies content-rewriting attacks evaluated inside a recommendation-agent testbed the researchers control, not placement into third-party high-citation platforms; filed per `docs/sources/query-book.md` academic set row "recommendation agents GEO risk / SafeGEO" mapped to P5-c1 (and P5-c7 for the defense/countermeasure angle).
- Comments field on arXiv page: "41 pages, 22 figures" — no venue named.
