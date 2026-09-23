# Perplexity Trap: PLM-Based Retrievers Overrate Low Perplexity Documents

```yaml
source:          Haoyu Wang, Sunhao Dai, Haiyuan Zhao, Liang Pang, Xiao Zhang, Gang Wang et al.
url_or_doc_id:   arXiv:2503.08684 ; https://arxiv.org/abs/2503.08684
published:       2025-03-11 (arXiv v1; latest listed 2025-03-11)
pull_date:       2026-09-23
pull_method:     fetch (arXiv API + arXiv HTML full text)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     peer-reviewed (ICLR 2025) with code published
source_label:    analyst-derived
lane:            D
sub_market:      organic recommendation
engine:          PLM retrievers (BERT/RoBERTa/Contriever/TAS-B); corpora from Llama2-7B-chat, GPT-3.5, GPT-4
metric_kind:     visibility
supersedes:      none
captured:        abstract (verbatim) + result sentences carrying numbers (verbatim from arXiv HTML)
topic_group:     1
venue_status:    ICLR 2025
code_availability: https://github.com/WhyDwelledOnAi/Perplexity-Trap
capability_class: retrievers over-rank low-perplexity LLM-like text (source bias); inference-time debiasing method
```

## Verbatim — abstract

"Previous studies have found that PLM-based retrieval models exhibit a preference for LLM-generated content, assigning higher relevance scores to these documents even when their semantic quality is comparable to human-written ones. This phenomenon, known as source bias, threatens the sustainable development of the information access ecosystem. However, the underlying causes of source bias remain unexplored. In this paper, we explain the process of information retrieval with a causal graph and discover that PLM-based retrievers learn perplexity features for relevance estimation, causing source bias by ranking the documents with low perplexity higher. Theoretical analysis further reveals that the phenomenon stems from the positive correlation between the gradients of the loss functions in language modeling task and retrieval task. Based on the analysis, a causal-inspired inference-time debiasing method is proposed, called Causal Diagnosis and Correction (CDC). CDC first diagnoses the bias effect of the perplexity and then separates the bias effect from the overall estimated relevance score. Experimental results across three domains demonstrate the superior debiasing effectiveness of CDC, emphasizing the validity of our proposed explanatory framework. Source codes are available at https://github.com/WhyDwelledOnAi/Perplexity-Trap."

## Verbatim — result sentences (from arXiv HTML full text)

- "The majority of the retrieval performance degradation was generally less than 2 percentage points, revealing that our debiasing CDC has acceptable impact on ranking performance, see detailed significance test in Appendix Table 7 ."

## Pull notes — mechanical only

- Metadata via arXiv API `export.arxiv.org/api/query`; abstract verbatim from the API `summary`.
- Result sentences extracted verbatim from `arxiv.org/html/2503.08684`; math markup stripped, wording unchanged. [note: figures and tables are images/HTML, not captured beyond the sentences above].
- Code-availability line reflects the paper's own statement / links found in the HTML this pull.
