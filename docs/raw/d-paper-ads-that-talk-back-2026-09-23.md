# Ads that Talk Back: Implications and Perceptions of Injecting Personalized Advertising into LLM Chatbots

```yaml
source:          Brian Jay Tang, Kaiwen Sun, Noah T. Curran, Florian Schaub, Kang G. Shin
url_or_doc_id:   arXiv:2409.15436 ; https://arxiv.org/abs/2409.15436
published:       2024-09-23 (arXiv v1; latest listed 2025-10-04)
pull_date:       2026-09-23
pull_method:     fetch (arXiv API + arXiv HTML full text)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     peer-reviewed (Proc. ACM IMWUT/UbiComp 2025) with code, dataset and a released fine-tuned open model (Phi-4-Ads)
source_label:    analyst-derived
lane:            D
sub_market:      paid placement
engine:          GPT-4o, GPT-4o-mini, GPT-3.5-Turbo; Phi-4-Ads (released)
metric_kind:     visibility
supersedes:      none
captured:        abstract (verbatim) + result sentences carrying numbers (verbatim from arXiv HTML)
topic_group:     2
venue_status:    Proc. ACM IMWUT 2025 (UbiComp)
code_availability: https://github.com/byron123t/chatbot-ads
capability_class: personalised ads embedded in chatbot answers; user detection and trust measured (n=179)
```

## Verbatim — abstract

"Recent advances in large language models (LLMs) have enabled the creation of highly effective chatbots. However, the compute costs of widely deploying LLMs have raised questions about profitability. Companies have proposed exploring ad-based revenue streams for monetizing LLMs, which could serve as the new de facto platform for advertising. This paper investigates the implications of personalizing LLM advertisements to individual users via a between-subjects experiment with 179 participants. We developed a chatbot that embeds personalized product advertisements within LLM responses, inspired by similar forays by AI companies. The evaluation of our benchmarks showed that ad injection only slightly impacted LLM performance, particularly response desirability. Results revealed that participants struggled to detect ads, and even preferred LLM responses with hidden advertisements. Rather than clicking on our advertising disclosure, participants tried changing their advertising settings using natural language queries. We created an advertising dataset and an open-source LLM, Phi-4-Ads, fine-tuned to serve ads and flexibly adapt to user preferences."

## Verbatim — result sentences (from arXiv HTML full text)

- "Our evaluations reveal that prompting LLMs to serve ads while responding to users degrades performance by at most 3% in certain benchmarks compared to the unprompted models."
- "Even with the inclusion of an advertising disclosure, 49.15% of participants did not realize that they were being served an ad."
- "Across the four ad conditions, 66–88% of participants reported noticing products or brands , but only 35.2% believed they could detect an advertisement at all."

## Pull notes — mechanical only

- Metadata via arXiv API `export.arxiv.org/api/query`; abstract verbatim from the API `summary`.
- Result sentences extracted verbatim from `arxiv.org/html/2409.15436`; math markup stripped, wording unchanged. [note: figures and tables are images/HTML, not captured beyond the sentences above].
- Code-availability line reflects the paper's own statement / links found in the HTML this pull.
