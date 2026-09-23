# EcoGEO: Trajectory-Aware Evidence Ecosystems for Web-Enabled LLM Search Agents

```yaml
source:          Hengwei Ye, Jiasheng Mao, Zhenhan Guan, Zheng Tian
url_or_doc_id:   arXiv:2605.12887 ; https://arxiv.org/abs/2605.12887
published:       2026-05-13 (arXiv v1; latest listed 2026-07-01)
pull_date:       2026-09-23
pull_method:     fetch (arXiv API + arXiv HTML full text)
pull_purpose:    evidence about a number
tier:            5
tier_reason:     preprint; paper states experimental code will NOT be released ('For safety reasons, we will not publicly release the complete experimental code'); academic table 'preprint without code'
source_label:    analyst-derived
lane:            D
sub_market:      organic recommendation
engine:          GPT-5.1, GPT-5.4, GPT-5.4-mini (web-enabled agents)
metric_kind:     visibility
supersedes:      none
captured:        abstract (verbatim) + result sentences carrying numbers (verbatim from arXiv HTML)
topic_group:     1
venue_status:    arXiv preprint
code_availability: none released (withheld by authors)
capability_class: a coordinated multi-page evidence environment steers a web-agent's product recommendation
```

## Verbatim — abstract

"Web-enabled LLM agents are changing how online information influences search outcomes. Existing Generative Engine Optimization (GEO) studies mainly focus on individual webpages. However, agentic web search is not a single-document setting: an agent may issue queries, crawl pages, follow links, reformulate searches, and synthesize evidence across multiple browsing steps. Influence therefore depends not only on page content, but also on how pages are organized, connected, and encountered along the agent's browsing trajectory. We study this shift through Ecosystem Generative Engine Optimization (EcoGEO), which treats GEO as an environment-level influence problem for web-enabled LLM agents. To instantiate this perspective, we propose TRACE, a Trajectory-Aware Coordinated Evidence Ecosystem. Given a recommendation query and a fictional target product, our method builds a controlled evidence environment that coordinates an agent-facing navigation entry page with heterogeneous support pages. These pages use shared terminology, internal links, and consistent product attributes to introduce, verify, and reinforce the target product. We evaluate our method on OPR-Bench, a benchmark for open-ended product recommendation. Experiments show that it consistently outperforms page-level GEO baselines in final target recommendation. Trajectory-level metrics further show increased initial target-result crawls, target-specific follow-up searches, and internal-link crawls, suggesting that the gains come from shaping the agent's evidence-acquisition process rather than merely adding more target-related content. Overall, our findings support an ecosystem research paradigm for GEO, where web-enabled LLM agents are studied in relation to the broader evidence environments that guide search, browsing, and answer synthesis."

## Verbatim — result sentences (from arXiv HTML full text)

- "TRACE achieves the highest final recommendation rate on all three datasets, reaching 67.2% on SafeSearch, 71.9% on E-Commerce, and 73.9% on E-GEO."
- "Compared with the strongest baseline in each dataset, the absolute gains are 31.3, 15.7, and 14.9 percentage points, respectively."

## Pull notes — mechanical only

- Metadata via arXiv API `export.arxiv.org/api/query`; abstract verbatim from the API `summary`.
- Result sentences extracted verbatim from `arxiv.org/html/2605.12887`; math markup stripped, wording unchanged. [note: figures and tables are images/HTML, not captured beyond the sentences above].
- Code-availability line reflects the paper's own statement / links found in the HTML this pull.
