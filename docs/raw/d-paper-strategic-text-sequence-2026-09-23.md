# Manipulating Large Language Models to Increase Product Visibility

```yaml
source:          Aounon Kumar, Himabindu Lakkaraju
url_or_doc_id:   arXiv:2404.07981 ; https://arxiv.org/abs/2404.07981
published:       2024-04-11 (arXiv v1; latest listed 2024-09-02)
pull_date:       2026-09-23
pull_method:     fetch (arXiv API + arXiv HTML full text)
pull_purpose:    evidence about a number
tier:            4
tier_reason:     preprint with code released (github.com/aounon/llm-rank-optimizer); academic table 'preprint with code'
source_label:    analyst-derived
lane:            D
sub_market:      organic recommendation
engine:          Llama-2 (optimisation target); GPT-4 referenced
metric_kind:     visibility
supersedes:      none
captured:        abstract (verbatim) + result sentences carrying numbers (verbatim from arXiv HTML)
topic_group:     1
venue_status:    arXiv preprint, no venue stated
code_availability: https://github.com/aounon/llm-rank-optimizer
capability_class: appended optimised text on a product page raises the product's LLM top-recommendation rate
```

## Verbatim — abstract

"Large language models (LLMs) are increasingly being integrated into search engines to provide natural language responses tailored to user queries. Customers and end-users are also becoming more dependent on these models for quick and easy purchase decisions. In this work, we investigate whether recommendations from LLMs can be manipulated to enhance a product's visibility. We demonstrate that adding a strategic text sequence (STS) -- a carefully crafted message -- to a product's information page can significantly increase its likelihood of being listed as the LLM's top recommendation. To understand the impact of STS, we use a catalog of fictitious coffee machines and analyze its effect on two target products: one that seldom appears in the LLM's recommendations and another that usually ranks second. We observe that the strategic text sequence significantly enhances the visibility of both products by increasing their chances of appearing as the top recommendation. This ability to manipulate LLM-generated search responses provides vendors with a considerable competitive advantage and has the potential to disrupt fair market competition. Just as search engine optimization (SEO) revolutionized how webpages are customized to rank higher in search engine results, influencing LLM recommendations could profoundly impact content optimization for AI-driven search services. Code for our experiments is available at https://github.com/aounon/llm-rank-optimizer."

## Verbatim — result sentences (from arXiv HTML full text)

- "In about 40 % 40% of the evaluations, the rank of the target product is higher due to the addition of the optimized sequence."
- "In about 60 % 60% of the evaluations, there is no change in the rank of the target product."
- "The percentage advantage significantly increases, and the percentage disadvantage is negligible. (a) Target product rank vs iterations. (b) Rank distribution before and after adding the STS for 200 independent evaluations of the LLM (1 dot ≈ 5 % approx 5% )."

## Pull notes — mechanical only

- Metadata via arXiv API `export.arxiv.org/api/query`; abstract verbatim from the API `summary`.
- Result sentences extracted verbatim from `arxiv.org/html/2404.07981`; math markup stripped, wording unchanged. [note: figures and tables are images/HTML, not captured beyond the sentences above].
- Code-availability line reflects the paper's own statement / links found in the HTML this pull.
