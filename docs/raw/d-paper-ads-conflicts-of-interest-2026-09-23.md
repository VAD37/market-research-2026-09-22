# Ads in AI Chatbots? An Analysis of How Large Language Models Navigate Conflicts of Interest

```yaml
source:          Addison J. Wu, Ryan Liu, Shuyue Stella Li, Yulia Tsvetkov, Thomas L. Griffiths
url_or_doc_id:   arXiv:2604.08525 ; https://arxiv.org/abs/2604.08525
published:       2026-04-09 (arXiv v1; latest listed 2026-08-17)
pull_date:       2026-09-23
pull_method:     fetch (arXiv API + arXiv HTML full text)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     peer-reviewed (COLM 2026) with code published
source_label:    analyst-derived
lane:            D
sub_market:      paid placement
engine:          23 LLMs incl. Grok 4.1 Fast, GPT-5.1, Gemini 3 Pro, Claude 4.5 Opus, Qwen 3 Next, DeepSeek-R1
metric_kind:     visibility
supersedes:      none
captured:        abstract (verbatim) + result sentences carrying numbers (verbatim from arXiv HTML)
topic_group:     2
venue_status:    COLM 2026
code_availability: https://github.com/addisonwu05/LLMs-and-Ads
capability_class: measured LLM behaviour under sponsor incentives (recommending pricier sponsored option, surfacing sponsored alternatives)
```

## Verbatim — abstract

"Large language models (LLMs) are trained to align with user preferences through methods like reinforcement learning. Yet models are beginning to be deployed not solely to satisfy users, but to generate revenue for the companies that created them through advertisements. This creates the potential for LLMs to face conflicts of interest, where the most beneficial response to a user may not be aligned with the company's incentives. For instance, a sponsored product may be more expensive but otherwise equal to another; here, what does (and should) the LLM recommend to the user? In this paper, we provide a framework for categorizing the ways in which conflicting incentives might change how LLMs interact with users, inspired by literature from linguistics and advertising regulation. We then present a suite of evaluations to examine how current models handle these tradeoffs. A majority of LLMs forsake user welfare for company incentives in a multitude of conflict of interest situations, including recommending a sponsored product almost twice as expensive (Grok 4.1 Fast, 83%), surfacing sponsored options to disrupt the purchasing process (GPT 5.1, 94%), and concealing prices in unfavorable comparisons (Qwen 3 Next, 24%). Behaviors vary strongly with levels of reasoning and users' inferred socio-economic status. Our results highlight some hidden risks to users that can emerge when companies begin to subtly incentivize advertisements in chatbots."

## Verbatim — result sentences (from arXiv HTML full text)

- "A majority of LLMs forsake user welfare for company incentives in a multitude of conflict of interest situations, including recommending a sponsored product almost twice as expensive (Grok 4.1 Fast, 83%), surfacing sponsored options to disrupt the purchasing process (GPT 5.1, 94%), and concealing prices in unfavorable comparisons (Qwen 3 Next, 24%)."
- "The highest sponsored recommendation rates came from Grok-4.1 ( 83 % 83% ) and Qwen-3 Next ( 70 % 70% )."
- "GPT-5.1 had a mean rate of 50 % 50% , while Gemini 3 Pro and Claude 4.5 Opus had rates of 37 % 37% and 28 % 28% , demonstrating stronger moral override towards users."
- "On average, LLMs recommended the sponsored option 64.1 ± 6.6 64.1pm 6.6 % of the time to high-SES users, but only 48.6 ± 6.2 48.6pm 6.2 % for low-SES users. 4 4 4 ± pm values reported throughout this section correspond to 95% confidence intervals."

## Pull notes — mechanical only

- Metadata via arXiv API `export.arxiv.org/api/query`; abstract verbatim from the API `summary`.
- Result sentences extracted verbatim from `arxiv.org/html/2604.08525`; math markup stripped, wording unchanged. [note: figures and tables are images/HTML, not captured beyond the sentences above].
- Code-availability line reflects the paper's own statement / links found in the HTML this pull.
