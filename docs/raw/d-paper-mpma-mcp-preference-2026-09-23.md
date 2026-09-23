# MPMA: Preference Manipulation Attack Against Model Context Protocol

```yaml
source:          Zihan Wang, Rui Zhang, Yu Liu, Wenshu Fan, Wenbo Jiang, Qingchuan Zhao et al.
url_or_doc_id:   arXiv:2505.11154 ; https://arxiv.org/abs/2505.11154
published:       2025-05-16 (arXiv v1; latest listed 2025-11-11)
pull_date:       2026-09-23
pull_method:     fetch (arXiv API + arXiv HTML full text)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     peer-reviewed (AAAI; arXiv is the extended version) with code published
source_label:    analyst-derived
lane:            D
sub_market:      agentic commerce
engine:          GPT-4o, Claude 3.7, Gemini 2.5 Flash, Qwen3-235B-A22B, Grok-3, DeepSeek
metric_kind:     visibility
supersedes:      none
captured:        abstract (verbatim) + result sentences carrying numbers (verbatim from arXiv HTML)
topic_group:     1
venue_status:    AAAI (extended version on arXiv)
code_availability: https://github.com/hanbaoergogo/MPMA
capability_class: tool name/description wording biases an LLM's choice among competing MCP servers
```

## Verbatim — abstract

"Model Context Protocol (MCP) standardizes interface mapping for large language models (LLMs) to access external data and tools, which revolutionizes the paradigm of tool selection and facilitates the rapid expansion of the LLM agent tool ecosystem. However, as the MCP is increasingly adopted, third-party customized versions of the MCP server expose potential security vulnerabilities. In this paper, we first introduce a novel security threat, which we term the MCP Preference Manipulation Attack (MPMA). An attacker deploys a customized MCP server to manipulate LLMs, causing them to prioritize it over other competing MCP servers. This can result in economic benefits for attackers, such as revenue from paid MCP services or advertising income generated from free servers. To achieve MPMA, we first design a Direct Preference Manipulation Attack (DPMA) that achieves significant effectiveness by inserting the manipulative word and phrases into the tool name and description. However, such a direct modification is obvious to users and lacks stealthiness. To address these limitations, we further propose Genetic-based Advertising Preference Manipulation Attack (GAPMA). GAPMA employs four commonly used strategies to initialize descriptions and integrates a Genetic Algorithm (GA) to enhance stealthiness. The experiment results demonstrate that GAPMA balances high effectiveness and stealthiness. Our study reveals a critical vulnerability of the MCP in open ecosystems, highlighting an urgent need for robust defense mechanisms to ensure the fairness of the MCP ecosystem."

## Verbatim — result sentences (from arXiv HTML full text)

- "The following conclusions can be drawn: The Best Description strategy consistently achieves a 100% ASR across almost all settings."
- "And the Best Name strategy also attains a 100% ASR in most cases and outperforms the baseline, except for a few scenarios under the GPT-4o model where its ASR falls below the baseline."
- "We can draw the following conclusions: Most advertising strategies achieve much higher ASR than the baseline."

## Pull notes — mechanical only

- Metadata via arXiv API `export.arxiv.org/api/query`; abstract verbatim from the API `summary`.
- Result sentences extracted verbatim from `arxiv.org/html/2505.11154`; math markup stripped, wording unchanged. [note: figures and tables are images/HTML, not captured beyond the sentences above].
- Code-availability line reflects the paper's own statement / links found in the HTML this pull.
