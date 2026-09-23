# Evaluating Brand Retrieval and Ranking in Large Language Model Recommendations

```yaml
source:          Edward Malthouse, Kun-Yu Lee, Jing Yang, Sanchary Pal, Xueyan Feng
url_or_doc_id:   arXiv:2609.16304 ; https://arxiv.org/abs/2609.16304
published:       2026-09-14 (arXiv v1; latest listed 2026-09-14)
pull_date:       2026-09-23
pull_method:     fetch (arXiv API + arXiv HTML full text)
pull_purpose:    evidence about a number
tier:            5
tier_reason:     preprint; open-source software and data stated (anonymous.4open.science link); academic table 'preprint with code' would be 4, but venue unconfirmed and repo anonymised â€” kept at 5 pending
source_label:    analyst-derived
lane:            D
sub_market:      organic recommendation
engine:          six LLMs incl. Claude Opus 4.7, Claude Sonnet 4.6, GPT-5.4, GPT-5.5, Gemini 2.5 Flash, Gemini 3.1 Pro
metric_kind:     visibility
supersedes:      none
captured:        abstract (verbatim) + result sentences carrying numbers (verbatim from arXiv HTML)
topic_group:     4
venue_status:    arXiv preprint
code_availability: https://anonymous.4open.science/r/LLM-Monitor-CF9F
capability_class: measurement framework (BRP@k, MRR@k) treating LLM brand recommendation as stochastic retrieval; diagnostic cues restore omitted brands
```

## Verbatim — abstract

"Large language models (LLMs) are increasingly used for product recommendation, but evaluating their recommendations presents challenges that differ from conventional information retrieval and recommender systems. LLMs can generate recommendations without an explicit candidate set, and repeated responses to the same query can produce different brands and rankings. We introduce a framework for evaluating open-ended LLM brand recommendations that defines the competitive set independently of model outputs and estimates recommendation prevalence and prominence through repeated sampling. We operationalize these constructs using Brand Recommendation Probability (BRP@$k$) and Mean Reciprocal Rank (MRR@$k$), and apply the framework to six LLMs across five product categories. Category-only queries reveal substantial omission of established brands and limited evidence that recommendation prominence follows conventional brand popularity. Instead, prominence is associated with broader marketplace-visibility signals, particularly search interest and online brand conversation. Needs-based queries show that contextualizing users' goals and constraints changes which brands are retrieved, while diagnostic positioning probes demonstrate that brands omitted from ordinary recommendations can remain conditionally retrievable when distinctive cues are supplied. These findings highlight the need to evaluate LLM recommendation as a stochastic retrieval-and-ranking process rather than from individual generated lists. We provide open-source software and data to support reproducible evaluation of LLM-generated brand recommendations."

## Verbatim — result sentences (from arXiv HTML full text)

- "Neither Craftsman nor L.L.Bean appeared in the category-only recommendations (MRR = 0; BRP@5 = 0%)."
- "Under the detailed needs-based prompts, Craftsman achieved an MRR = .108 and a BRP@5 = 35.4%, whereas L.L.Bean achieved an MRR = .025 and a BRP@5 = 5.4%."
- "When supplied with these diagnostic cues, however, BRP@5 increased to 81.3% for Craftsman and 88.5% for L.L.Bean."

## Pull notes — mechanical only

- Metadata via arXiv API `export.arxiv.org/api/query`; abstract verbatim from the API `summary`.
- Result sentences extracted verbatim from `arxiv.org/html/2609.16304`; math markup stripped, wording unchanged. [note: figures and tables are images/HTML, not captured beyond the sentences above].
- Code-availability line reflects the paper's own statement / links found in the HTML this pull.
