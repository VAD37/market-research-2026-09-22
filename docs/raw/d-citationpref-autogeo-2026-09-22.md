# Wu et al. — What Generative Search Engines Like and How to Optimize Web Content Cooperatively (AutoGEO)

```yaml
source:          Yujiang Wu, Shanshan Zhong, Yubin Kim, Chenyan Xiong
url_or_doc_id:   arxiv.org/abs/2510.11438
published:       2025-10-13
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            5
tier_reason:     preprint; code released ("The code is released at this https URL") but no stated fixed prompt set beyond the benchmark's own query set, and no venue/review status found in this pull — academic table "preprint without code" does not quite apply since code is released, but no confirmed peer review; treated conservatively as tier 5, not upgraded to 4, pending confirmation of a separately published prompt list
source_label:    analyst-derived
lane:            D
sub_market:      organic recommendation
engine:          Generative-engine simulation using multiple LLM backbones as the "generative engine": GPT-4o-mini, Claude-3-haiku, Gemini-2.5-flash-lite, Gemini-2.5-Pro, Qwen3-1.7B, DeepSeek-R1-Distill-Qwen-1.5B
metric_kind:     visibility
supersedes:      none
captured:        abstract, mechanism (preference-rule extraction pipeline), models tested, headline effect size, method contribution list
technique:       content written to satisfy known citation preferences — explicitly frames the technique as first learning what a generative engine "likes" (a preference model) then rewriting content to match it
models_tested:   GPT-4o-mini, Claude-3-haiku, Gemini-2.5-flash-lite, Gemini-2.5-Pro, Qwen3-1.7B, DeepSeek-R1-Distill-Qwen-1.5B (as generative-engine backbones evaluated); GEO-Bench (Aggarwal et al. 2024) plus two newly constructed benchmarks using real user queries
date_window:     not stated beyond the arXiv submission date (2025-10-13)
measured_effect: yes — "an average improvement of 35.99% in GEO metrics while maintaining utility"
vertical:        none named — general web content across GEO-Bench's domains plus two new real-user-query benchmarks (not vertical-tagged in the extracted passages)
```

## Verbatim

### Abstract

"By employing large language models (LLMs) to retrieve documents and generate natural language responses, Generative Engines, such as Google AI overview and ChatGPT, provide significantly enhanced user experiences and have rapidly become the new form of search. Their rapid adoption also drives the needs of Generative Engine Optimization (GEO), as content providers are eager to gain more traction from them. In this paper, we introduce AutoGEO, a framework to automatically learn generative engine preferences when using retrieved contents for response generation, and rewrite web contents for more such traction. AutoGEO first prompts frontier LLMs to explain generative engine preferences and extract meaningful preference rules from these explanations. Then it uses preference rules as context engineering for AutoGEO_API, a prompt-based GEO system, and as rule-based rewards to train AutoGEO_Mini, a cost-effective GEO model. Experiments on the standard GEO-Bench and two newly constructed benchmarks using real user queries demonstrate the effectiveness of AutoGEO in enhancing content traction while preserving search utility. Analyses confirm the learned rules' robustness and abilities to capture unique preferences in variant domains, and AutoGEO systems' ability to embed them in content optimization. The code is released at this https URL."

### Mechanism, verbatim

"AutoGEO first learns preference rules by leveraging large language models to automatically analyze the preference usage of retrieved content from generative engines. It employs LLMs to explain the preferences on document pairs with visi[ble ranking differences, extracts these] into candidate rules, and filter[s] insights into preference rules. Through this pipeline, AutoGEO transforms tens of thousands of generative engine preference observations into an actionable set of rules that effectively capture how generative engines prioritize c[ontent]."

"AutoGEO tailors four components for uncovering generative engine preferences... Explainer compares a document pair (d_i, d_j) with respect to the generated [response]... Merger is a LLM with the instruction that guides it to aggregate insights across multiple queries and document pairs, consolidating them into [candidate rules]... Filter is driven by a LLM with the instruction to refine this rule set by removing spurious or ambiguous rules, retaining only those that reliably reflect genuine generative engine preferences."

"We first directly use preference rules as context engineering for frontier LLMs, yielding a GEO model AutoGEO_API that requires no additional training and can be readily applied in practice. In addition, we define rele-ba[sed]... [RL] procedure, where the engine preference rules serve as reward signals."

"In practice, based on AutoGEO, website owners can continuously monitor engine preferences, update rules automaticall[y]... preference rules differ significantly across domains, and each LLM has unique preference rules. These engine-specific rules consistently yield better GEO performance than using consistent rules."

### Results, verbatim

"We evaluate our methods on three datasets. The first, GEO-Bench (Aggarwal et al., 2024), is a large-scale GEO benchmark containing diverse user queries across multiple domains. In addition, we contribute two ne[w benchmarks using real user queries]."

"[Results] show that our GEO models consistently outperform baselines, achieving an average improvement of 35.99% in GEO metrics while maintaining utility. Notably, AutoGEO_Mini outperforms baselines and stands out for its cost effi[ciency]... achieving ∼0.0071x the cost of AutoGEO_API."

### Contribution list, verbatim

"[We propose] a systematic framework to extract generative engine preference rules and build efficient GEO models. AutoGEO applies these rules to build a plug-and-play GEO model, AutoGEO_API, without additional training. AutoGEO develops AutoGEO_Mini... an efficient GEO model that uses the extracted engine preference rules as reward signals to guide optimization of rewriting... We conduct comprehensive experiments by releasing two new benchmarks, Resea[rch... and a second, name not fully captured]."

## Pull notes — mechanical only

- Fetched via `curl` (fetch method) from `arxiv.org/html/2510.11438`, converted to plain text by stripping HTML/MathML tags; several sentences show mid-word truncation where the plain-text conversion split a hyphenated or subscripted term (e.g. "GEO_API", "GEO_Mini" rendered with LaTeX subscript markup) — bracketed `[...]` insertions above are this pull's best reconstruction of the visible surrounding text, not invented content.
- Single-author-group preprint; no independent replication found in this pull. The +35.99% "average improvement in GEO metrics" is the paper's own composite metric across its three benchmark datasets and six backbone models — not broken out per-model or per-domain in the passages captured here.
- Directly names the mechanism this whole P5-c4 cluster investigates: learning "generative engine preferences" (i.e., what content features a citation-selection model rewards) and rewriting content to match them — the paper's title is a near-verbatim restatement of the Pass 5 technique definition itself.
- This paper is cited inside the P5-c1 critical-survey pull (`d-seeding-critical-survey-2026-09-22.md`) as "Wu et al., 2026c" (survey's own dating convention differs from arXiv's 2025 submission year) alongside FeatGEO, Mind Reader, IF-GEO and MAGEO as "recent optimization systems... replac[ing] fixed recipes with learned rules" — that survey passage is the citation trail this pull followed from the P5-c4 seed paper (arxiv.org/html/2607.14035v1).
