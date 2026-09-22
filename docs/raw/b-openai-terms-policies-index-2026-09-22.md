# OpenAI — Terms & policies (index page)

```yaml
source:          OpenAI
url_or_doc_id:   https://openai.com/policies/
published:       undated — no date on page
pull_date:       2026-09-22
pull_method:     browser extension
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default (platform primary, own framing)
source_label:    company-stated
lane:            B
sub_market:      paid placement
engine:          ChatGPT — OpenAI
metric_kind:     none
supersedes:      none
captured:        full page
```

## Verbatim

Terms & policies | OpenAI

Terms & policies

Legal

Terms of use: Terms that govern use of ChatGPT, DALL·E and OpenAI's other services for individuals.

Privacy policy: Practices with respect to personal information we collect from or about you.

Service terms: Additional terms that govern your use of specific services.

Data processing addendum: Ensuring that personal data is handled appropriately and securely.

Our approach to patents: Information on our use of patents.

Connectors and actions terms: These terms govern the creation and use of your Connectors and Actions in connection with OpenAI Services.

Service credit terms: These terms govern any credits redeemable for our services.

OpenAI services agreement: Terms that govern use of OpenAI's services for businesses, enterprises, or developers.

Teacher Access Terms: Terms that govern use of OpenAI's ChatGPT for Teachers offering.

Unauthorized OpenAI Equity Transactions: All OpenAI equity is subject to transfer restrictions.

Applicant Arbitration Agreement (opens in a new window): Arbitration Agreement for U.S. applicants.

Serving civil subpoenas or other civil requests for user data on OpenAI: Procedures for requesting user data in civil matters.

Advertising Terms: Terms that govern use of OpenAI's Advertising Services.

Ad Tools Terms: Terms that govern use of supplemental ad tools and features.

Ad Tools data processing addendum: Addendum that governs the processing of personal data through certain Ad Tools.

Conversion Terms: Terms that govern use of OpenAI's Conversion Tools.

Merchant Feed Terms: Terms that govern use of merchant product and services feeds in connection with OpenAI Services.

Ad Credit Terms: Terms that govern Ad Credits.

Financial Services Terms: Terms governing Financial Plugins and ChatGPT for Financial Services.

Policies

Usage policies: Ensuring our technology is used for good.

Creating images and videos in line with our policies: Respecting our image and video generation guardrails.

Using Operator in line with our policies: Ensuring responsible use of Operator.

Enterprise privacy: Usage and retention of data submitted for enterprise users.

Sharing & publication policy: On permitted sharing, publication, and research access.

Coordinated vulnerability disclosure policy: Definition of good faith in the context of finding and reporting vulnerabilities.

Outbound coordinated disclosure policy: The policy we follow when disclosing vulnerabilities to third-parties.

UK tax strategy: Tax policy that applies to the UK affiliate of OpenAI.

Your data and model performance: Learn more about how OpenAI uses content from our services to improve and train our models.

How our models are developed: Information about how we develop our models and apply them in products like ChatGPT.

Cookie policy: Describes the kinds of cookies and similar technologies OpenAI uses in connection with our Services, and how you can manage them.

Health Privacy Notice: Supplemental notice that explains additional privacy practices when you use the Health feature in ChatGPT ("Health").

Ad policies: Rules for ad content and placement on OpenAI services.

Commerce policies: Prohibited products and merchant practices.

## Pull notes — mechanical only

- Loaded via Chrome extension (openai.com flagged 403→ext per channels.md C1).
- Index/directory page listing every legal and policy document title with a one-line description. This file records the index; the individual documents ("Advertising Terms", "Ad Tools Terms", "Merchant Feed Terms", "Ad policies", "Commerce policies", "Usage policies") named here are separate further pull targets in this cluster.
- `read_page` interactive extraction only resolved hrefs for the first nine legal links (Terms of use through Education Terms) — the page appears to virtualize/lazy-render lower list items, so hrefs for Advertising Terms, Ad Tools Terms, Merchant Feed Terms, Ad policies, and Commerce policies were not captured by that call. Their slugs are inferred (`/policies/advertising-terms/`, `/policies/ad-policies/`, `/policies/merchant-feed-terms/`, `/policies/commerce-policies/`, `/policies/usage-policies/`) and confirmed or corrected by direct navigation in the companion pull files for each.
- Confirms, by title alone, that OpenAI maintains a **dedicated commercial legal stack**: Advertising Terms, Ad Tools Terms, Ad Tools DPA, Conversion Terms, Merchant Feed Terms, Ad Credit Terms — six distinct named contracts for the paid/merchant side, beyond the general Terms of Use / Services Agreement.
