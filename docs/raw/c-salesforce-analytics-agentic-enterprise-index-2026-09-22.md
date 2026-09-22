# Salesforce — Agentic Enterprise Index: Agent Deployments More Than Double Year over Year

```yaml
source:          Salesforce (Salesforce News; quote attributed to Joe Inzerillo, Salesforce President of Enterprise AI and Technology)
url_or_doc_id:   https://www.salesforce.com/news/stories/agentic-enterprise-index-insights-2026/
published:       2026-08-07
pull_date:       2026-09-22
pull_method:     browser extension
pull_purpose:    evidence about a number
tier:            5
tier_reason:     table default for Salesforce (P2-c8 shortlist row) — vendor study with method stated (Agentforce platform usage-data analysis, see Verbatim), cohort inclusion rule stated, no independent replication
source_label:    vendor-reported
lane:            C
sub_market:      agentic commerce
engine:          n/a — measures usage of Salesforce's own Agentforce platform (retailers' own branded/owned agents), not third-party AI-assistant (ChatGPT/Perplexity/etc.) referral
metric_kind:     sales
note:            the retail "4x higher sales growth rate" figure is a measured before/after comparison between two self-selected retailer cohorts (deployed vs. did-not-deploy Agentforce agents), not an AI-referral-traffic attribution figure — no third-party AI-assistant referral traffic/conversion/order figure appears in this file. Population is retailers running Salesforce's own Agentforce agents on their own properties, not the AI-assistant-referral population this P2-c8 pull otherwise targets. Retained because it was surfaced directly by the P2-c8 query and is a Salesforce shopping-index-family post.
supersedes:      none
captured:        full page (article body, stat callouts, methodology section)
```

## Verbatim

"Salesforce Agentic Enterprise Index: Agent Deployments More Than Double Year over Year

An analysis of Agentforce usage among businesses consistently leveraging agents from February 2025 to April 2026 shows how different industries deploy AI agents while building trust and recognizing ROI.

August 7, 2026
9 min read
Quick stats:
Organizations increased activated agents by nearly 3x by the end of this fiscal year and reduced the average creation time by 53%.
Agents are becoming highly versatile, and their skill set can expand by up to 350% to handle complex tasks during peak demand.
Deploying agents resulted in 4x higher retail online sales growth.
Trust is deepening, with weekly employee usage tripling and customer escalation rates holding steady even at massive scale.

...

Retail and Travel Dominate AWU Volume
Retail represents 22% of total monthly output; 18x AWU growth Feb 2025 - April 2026
Travel represents 10% of total monthly output; 7x AWU growth Feb 2025 - April 2026

...

Businesses that leverage AI agents also see stronger sales growth compared with those that don't. This trend is particularly strong in retail and consumer industries during holiday shopping.

The Shopper Agent Advantage

Retailers that deployed AI agents during the holiday shopping season saw a 4x higher sales growth rate.

4x higher sales growth rate
8% YoY Sales Increase (With AI Agents)
2% YoY Sales Increase (Without AI Agents)

'Whether you're spinning up agents to operate at massive scale or orchestrating them through deep, multistep pipelines, the bottom line is they're shipping real value.' said, Joe Inzerillo, Salesforce President of Enterprise AI and Technology. 'That ROI isn't just showing up on the top line in sales numbers but execution efficiency. We are moving from passive chatbots and predictive models to execution-driven agents that actually roll up their sleeves and drive real value.'

...

Customers trust agents too. Over the past five quarters, agents handled 170 times more customer service chats than previous years and consistently solved 7 out of 10 of them without needing human help.

Escalation rates from AI agents to human agents are holding steady at 32%

In fact, a recent study found that 77% of shoppers who engaged with onsite, branded shopper agents felt more confident with their purchase than those who didn't.

...

Methodology:

Powered by Agentforce and other Salesforce products, Salesforce analyzed and aggregated usage data of a cohort of businesses to uncover the true story of agents in the workforce. Looking at trends from February 2025 to April 2026, The Salesforce Agentic Enterprise Index analyzes the activity and engagement of real businesses leveraging the power of AI agents to drive ROI. To qualify for inclusion in the dataset, businesses needed to have activated agents in production every month across the analysis period. These results are not indicative of Salesforce performance."

## Pull notes — mechanical only

- Full page loaded and captured in a single `get_page_text` call, no retry needed.
- No paywall, login wall, or truncation encountered.
- This report measures Agentforce (Salesforce's own agent product, deployed by retailers on their own sites) usage and its correlation with sales growth — it is not a measurement of third-party AI-assistant (ChatGPT/Perplexity/Gemini/etc.) referral traffic, conversion, or orders. Flagged clearly in the header `note:` field; excluded from the summary table's AI-referral rows and listed there separately as out-of-population.
