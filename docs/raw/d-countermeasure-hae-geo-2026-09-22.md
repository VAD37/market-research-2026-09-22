# Bi, Wang, Jiang, Ding, Xiong, Meng, Gao, Lin, Jiang, Chen, Yao, Wang, Ma & Dong — Evaluating Deep-Search Agents under Hierarchical Web Evidence Poisoning (HAE-GEO benchmark)

```yaml
source:          Zhongan Bi, Qiwen Wang, Jianrong Jiang, Jigang Ding, Wenwen Xiong, Changhua Meng, Xuanang Gao, Kepeng Lin, Changjiang Jiang, Yiang Chen, Huan Yao, Wei Wang, Zhenyu Ma, Wenhui Dong
url_or_doc_id:   arxiv.org/abs/2609.06027 (abstract page); arxiv.org/html/2609.06027 (full-text HTML, v2)
published:       arXiv:2609.06027 — abstract page states submission 5 September 2026; full-text HTML page states "v2" dated September 17, 2026
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            4
tier_reason:     preprint with code released — academic table row "preprint with code and prompt set"; code repository confirmed in the paper's own text (see Verbatim)
source_label:    analyst-derived
lane:            D
sub_market:      organic recommendation
engine:          n/a — the paper evaluates ten named third-party/open models as search agents against a poisoning benchmark; it is not any single AI-assistant vendor's own statement
metric_kind:     none
supersedes:      none
captured:        abstract, evaluated-model list, code-repository link, and "defense prompting" mitigation findings and trade-offs, as returned by the fetch tool
technique:       defense literature — measures a specific mitigation ("defense prompting") against Generative Engine Optimization poisoning of search-agent evidence, with a stated limited/mixed effect
models_tested:   Ten agents: "Claude-Opus-4.8, GPT-5.6-sol, Kimi-K3, GLM-5.2, GLM-4.7-Flash, MiniMax-M3, Qwen3.8-27B, Qwen3.6-35B-A3B, Qwen3.5-397B-A17B, DeepSeek-V4-Flash"
date_window:     n/a — no experiment date range stated beyond the arXiv submission/revision dates above
measured_effect: yes — see Verbatim (a measured, and explicitly limited, defense effect)
vertical:        n/a — framed as general "consumer decisions," no single vertical named in captured passages
```

## Verbatim

Abstract framing, quoted as returned by the fetch tool:

"Search-augmented LLM agents are increasingly used for consumer decisions, making them vulnerable to Generative Engine Optimization (GEO) poisoning." The paper introduces the HAE-GEO benchmark, measuring "whether an agent verifies suspicious evidence, revises adopted claims, or recovers before producing its final recommendation" across three attack levels — described by the fetch tool as testing for a "corroboration trap."

Key findings, quoted as returned by the fetch tool:

"Evidence recognition degrades under the corroboration trap; agentic search improves final resistance without improving evidence recognition or utility; and defense prompting increases verification, yet rarely converts verification into recovery."

Defense-prompting mitigation, measured effect, quoted as returned by the fetch tool:

"Defense prompting therefore provides substantial gains for some systems but only marginal improvements for others." Cost of the mitigation: "Defense adds 1.82 tool calls per query on average and raises within-model token consumption by a macro-average of 24.5%." Trade-off stated: "Defense moves all ten models toward higher robustness, but also toward lower utility."

Evaluated models, quoted as returned by the fetch tool:

"Claude-Opus-4.8, GPT-5.6-sol, Kimi-K3, GLM-5.2, GLM-4.7-Flash, MiniMax-M3, Qwen3.8-27B, Qwen3.6-35B-A3B, Qwen3.5-397B-A17B, DeepSeek-V4-Flash."

Code repository, quoted as returned by the fetch tool:

"https://github.com/ant-research/HAE-GEO/tree/main"

## Pull notes — mechanical only

- Fetched via WebFetch. Located through the Semantic Scholar citation-trail pull for the assigned seed paper (2605.21948) — see `docs/raw/d-countermeasure-semanticscholar-citation-trail-2026-09-22.md`. Abstract page (200); full-text HTML (`arxiv.org/html/2609.06027`, 200) gave the model list, defense-prompting quantitative findings, and code link. The fetch tool reported no dedicated limitations section in the captured content.
- **This paper is the weakest-effect defense result in this task's set, by its own reporting**: "defense prompting" — the one mitigation it tests — "rarely converts verification into recovery," i.e., agents notice something is suspicious more often under the mitigation but frequently still act on the poisoned evidence anyway. This is recorded as-is, not interpreted further, per this repo's no-interpretation-in-raw rule; the census table carries this row specifically because a measured-but-limited defense effect is itself evidence relevant to H5/H13, not because it is a success story.
- The ten evaluated model names (e.g., "GPT-5.6-sol," "Kimi-K3") are the paper's own naming; not cross-checked against any vendor's own model-naming page in this pull.
