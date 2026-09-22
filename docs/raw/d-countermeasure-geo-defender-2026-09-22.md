# Li, Shao, Lin, Guan, Zhou & Shi — When Optimization Becomes Manipulation: Defending Generative Search against Malicious Generative Engine Optimization (GEO Defender)

```yaml
source:          Haozhang Li, Yangguang Shao, Xinjie Lin, Zhong Guan, Mi Zhou, Junzheng Shi
url_or_doc_id:   arxiv.org/abs/2609.02964 (abstract page); arxiv.org/html/2609.02964 (full-text HTML)
published:       arXiv:2609.02964v1 [cs.CR], submitted 2 September 2026
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            4
tier_reason:     preprint with code released — academic table row "preprint with code and prompt set"; code repository confirmed in the paper's own text (see Verbatim). No venue/peer-review confirmation found beyond the cs.CR/cs.AI arXiv categories
source_label:    analyst-derived
lane:            D
sub_market:      organic recommendation
engine:          n/a — the paper's defense (GEO Defender) is a reranker/prompting layer tested against five named LLMs, not a statement from any of those LLM vendors about their own production defenses
metric_kind:     none
supersedes:      none
captured:        title, authors, venue, defense-mechanism description, target-model list, judge-model statement, code-repository link, and headline results, as returned by the fetch tool across the abstract page and the HTML full text
technique:       defense literature — GEO/ranking-manipulation defense at the reranking and in-context-guidance layer, evaluated across "seven GEO attacks"
models_tested:   Target ("victim") models: "GPT-5.5 (OpenAI 2026) and Claude Opus 4.8 (Anthropic 2026), and three open-source LLMs, DeepSeek-V4-Pro (DeepSeek-AI 2026), Kimi K2.7 Code (Moonshot AI 2026), and GLM-5.2." Judge model: "GPT-5.5 as an LLM judge" for the ASI (attack success index) and answer-quality metrics
date_window:     n/a — no experiment date range stated beyond the arXiv submission date (2026-09-02)
measured_effect: yes — see Verbatim
vertical:        n/a — no single vertical named in the captured passages
```

## Verbatim

Title, quoted as returned by the fetch tool:

"When Optimization Becomes Manipulation: Defending Generative Search against Malicious Generative Engine Optimization."

Defense mechanism, quoted/reported as returned by the fetch tool. Two components:

1. "Shield Reranker" — "learns preference-based defensive adjustments over a frozen base reranker to demote manipulated documents while maintaining relevance."
2. "Training-Free Shield Generation (TFSG)" — "distills defense outcomes into a natural-language library guiding the LLM's source usage at inference time."

The approach "requires no fine-tuning of the target LLM."

Target models, quoted as returned by the fetch tool:

"GPT-5.5 (OpenAI 2026) and Claude Opus 4.8 (Anthropic 2026), and three open-source LLMs, DeepSeek-V4-Pro (DeepSeek-AI 2026), Kimi K2.7 Code (Moonshot AI 2026), and GLM-5.2."

Measured results, quoted/reported as returned by the fetch tool:

Average attack success rate reduced from "50.32% to 6.20%"; retains "94.12% of benign-evidence use"; tested across "seven GEO attacks"; the defense "generalizes to unseen attacks from construction instances."

Code repository, quoted as returned by the fetch tool:

"Code is available at https://github.com/Ccchi5ato/GEO-Defender"

## Pull notes — mechanical only

- Fetched via WebFetch. Located through the Semantic Scholar citation-trail pull for the assigned seed paper (2605.21948) — see `docs/raw/d-countermeasure-semanticscholar-citation-trail-2026-09-22.md`. Abstract page (200) gave title/authors/venue/date. Full-text HTML (`arxiv.org/html/2609.02964`, 200) gave the target-model list, judge-model statement, code link, and the "no experiment date range" finding — the fetch tool explicitly reported it could not find a specific date range for experiments beyond the submission timestamp, and reported no dedicated limitations section exists in the paper ("the work concludes with a brief conclusion paragraph rather than a formal limitations discussion").
- This is the second-strongest defense-measurement paper this task found: it names a **defended attack-success-rate reduction with a specific starting and ending number** (50.32% -> 6.20%) across a named multi-model, multi-attack test bed, and its code repository is named in the paper's own text (not independently verified reachable by this task — `unknown — checked whether github.com/Ccchi5ato/GEO-Defender resolves, not fetched this pull, 2026-09-22`).
- The paper's target-model list (GPT-5.5, Claude Opus 4.8, DeepSeek-V4-Pro, Kimi K2.7 Code, GLM-5.2) names two of this repo's priority-1 engines' underlying models by vendor attribution (OpenAI, Anthropic) — recorded as the paper's own attribution, not verified against those vendors' own model-naming pages in this pull.
