# OpenAI Developers — Agentic Commerce: Get Started (onboarding, prohibited products policy)

```yaml
source:          OpenAI (developers.openai.com)
url_or_doc_id:   https://developers.openai.com/commerce/guides/get-started
published:       undated — no date on page
pull_date:       2026-09-22
pull_method:     browser extension
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default (platform primary, merchant-facing wording)
source_label:    company-stated
lane:            C
sub_market:      agentic commerce
engine:          ChatGPT — OpenAI
metric_kind:     none
supersedes:      none
captured:        full page
```

## Verbatim

Onboarding product feeds in ChatGPT is currently available to approved partners. To apply for access, fill out this form here

Overview

Start your ACP integration by sharing a structured product feed with OpenAI. Product feeds give ChatGPT the catalog data it needs to index your products, understand core attributes, and present accurate product information in shopping experiences.

Start with product feeds when you want to:

Make your catalog understandable to ChatGPT.
Share up-to-date product data, including titles, descriptions, images, price, and availability.
Establish a clear integration path based on a documented schema and delivery model.

You can learn more about the Agentic Commerce Protocol at agenticcommerce.dev and on GitHub.

Integration path

Use this sequence to stand up your integration with ACP:

Decide which integration method to use: file upload or API.
It is generally recommended to provide the entire feed once a day via file upload, and then send updates throughout the day via the API.
If your feed is small, you can provide both the entire feed and regular updates via the API.
Promotions data can only be provided via the API.
Review the specs for the chosen integration method, and confirm the required fields, canonical field names, and validation rules.
Validate required fields for every record.
Upload feed data through the chosen integration method.
Keep the feed current based on the integration method:
For file upload, overwrite the same file or shard set with your latest snapshot on a regular cadence.
For the API, upsert products through the API.

Prohibited products policy

To keep ChatGPT a safe place for everyone, we only allow products and services that are legal, safe, and appropriate for a general audience. Prohibited products include, but are not limited to, those that involve adult content, age-restricted products (for example, alcohol, nicotine, gambling), harmful or dangerous materials, weapons, prescription-only medications, unlicensed financial products, legally restricted goods, illegal activities, or deceptive practices.

Merchants are responsible for ensuring their products and content do not violate these restrictions or any applicable law. OpenAI may take corrective actions such as removing a product or banning a seller from being surfaced in ChatGPT if these policies are violated.

Best practices

Review integration best practices for guidance.

## Pull notes — mechanical only

- Loaded via Chrome extension.
- **Eligibility gate stated verbatim**: "Onboarding product feeds in ChatGPT is currently available to approved partners. To apply for access, fill out this form" — this is a gated/partner program, not fully public self-serve, for the merchant product-feed side of agentic commerce (distinct from the paid-ads product-feed self-serve beta in `c-openai-product-feed-campaigns-2026-09-22.md`).
- No checkout fee, no take-rate, no percentage or currency figure for Instant Checkout or merchant-of-record terms found on this page. No pull in this cluster located a stated Instant Checkout fee — recorded per task instructions as `unknown — checked https://help.openai.com/en/articles/11128490-shopping-with-chatgpt-search, https://developers.openai.com/commerce, https://developers.openai.com/commerce/guides/get-started, https://developers.openai.com/commerce/guides/best-practices 2026-09-22`.
- Merchant obligations/liability stated: merchants "responsible for ensuring their products and content do not violate these restrictions or any applicable law"; OpenAI "may take corrective actions such as removing a product or banning a seller."
- Prohibited categories named verbatim: adult content, age-restricted products (alcohol, nicotine, gambling), harmful or dangerous materials, weapons, prescription-only medications, unlicensed financial products, legally restricted goods, illegal activities, deceptive practices.
- External references named but not pulled (out of this cluster's openai.com/help.openai.com/platform.openai.com/archive scope per task instructions): agenticcommerce.dev, GitHub (both covered by the separate P2-c7 cluster per `shortlist.md`).
