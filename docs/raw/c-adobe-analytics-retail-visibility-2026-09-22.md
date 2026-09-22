# Adobe blog — AI traffic grows but retail sites lag in AI search visibility

```yaml
source:          Adobe Digital Insights / business.adobe.com blog (author: Vivek Pandya)
url_or_doc_id:   https://business.adobe.com/blog/ai-traffic-surge-retail-sites-not-machine-readable
published:       2026-04-16
pull_date:       2026-09-22
pull_method:     browser extension
pull_purpose:    evidence about a number
tier:            4
tier_reason:     method stated in body (see Verbatim) — trust-rubric.md tier-4 default for panel/clickstream/infrastructure telemetry with published method
source_label:    vendor-reported
lane:            C
sub_market:      agentic commerce
engine:          n/a — traffic sourced from generative AI tools/browsers generally, not broken out by engine
metric_kind:     traffic
note:            body also carries sales-metric_kind figures (conversion rate). Not an "influenced revenue" composite.
supersedes:      none
captured:        full page
```

## Verbatim

"Adobe report: U.S. retailers see surge in AI traffic, but many websites are not entirely readable by machines.

Vivek Pandya
04-16-2026

AI is quickly becoming the primary interface between consumers and their favorite brands. This is particularly true in the ecommerce space, where the use of AI-powered chat services and browsers continues to rise. Consumers are engaging with large language models (LLMs) to find specific products or locate the best deals, while receiving links to relevant retail websites.

However, not all retailers are seeing the same benefit. New Adobe data shows that major portions of U.S. retail websites are not entirely readable by machines, which limits their visibility across AI search results. As the internet continues to be reintermediated by AI, there is increased urgency for retailers to revamp their digital properties and ensure their products remain top of mind with shoppers.

Adobe's insights are based on direct transactions online, covering over 1 trillion visits to U.S. retail sites — more than any other technology company or research organization. A companion survey of more than 5,000 U.S. respondents provides additional context on how consumers are leveraging AI in their online shopping journeys.

AI traffic to U.S. retail sites remains elevated.

In the first three months of 2026 (Jan. to Mar. 2026), traffic from AI sources to U.S. retail sites grew 393% year over year (YoY). In March 2026, it was up 269% YoY. This continues the momentum that was observed during the most recent holiday season (Nov. to Dec. 2025) where AI traffic was up 693% YoY.

In Adobe's survey, 39% of consumers say they have used AI before for online shopping, with 85% of them saying it improved their experience. These figures highlight the durable value that AI is delivering in the ecommerce space, shortening the time it takes for consumers to find what they need or locate relevant discounts.

Notably, AI traffic continues to convert better (visits that result in purchases) than non-AI traffic, which covers channels such as paid search and email marketing. In March 2026, AI traffic converted 42% better (a new record high). This is a major reversal from a year ago, where in March 2025, AI traffic converted 38% worse. Rising consumer trust has played a factor, with Adobe's survey showing that 66% of respondents believe AI tools provide accurate results. This is giving shoppers confidence and driving more transaction activity.

The rise in AI conversion is reinforced by Adobe's data on engagement and bounce rates. Data from March 2026 showed that once an individual lands on a U.S. retail site (from an AI source), the engagement rate is 12% higher compared to non-AI traffic. These shoppers are essentially spending more time on the website (48% longer per Adobe's data) and browsing more pages (13% more pages per visit).

Many U.S. retail sites have not been revamped for AI visibility.

Last year, we unveiled an AI Content Visibility Checker, a diagnostic tool that can analyze any web page and identify what LLMs can or cannot read. Adobe is releasing new data today that profiles the U.S. retail sector overall, looking at pages across retail websites and creating a benchmark on AI visibility. The AI Content Visibility Checker assigns a score out of 100%. So, if a webpage receives a score of 50%, this means half of its content is not readable by machines.

Across the U.S. retail sector, the average score for homepages came in at 75%. This means roughly a quarter of the content on homepages has not been optimized for LLMs. Category-level pages (such as appliances or men's apparel) came in at a similar level at 74%. One area of challenge is individual product pages, which came in at 66%. Retailers have thousands of SKUs, and our data shows that much of the content is currently invisible to LLMs.

Other pages of note include:

Store locator (73%)
Customer service/help center (79%)
Contact us (81%)
Returns/exchanges (82%)
Loyalty/membership (78%)
FAQ (80%)

This highlights the different areas that retailers will want to update and ensure they can be read by machines.

Additionally, while the average score for homepages is 75% (as noted previously), it comes in at 82.5% for the best-performing U.S. retail sites and 54.2% for the lowest-performing. This gap between the two sets of brands shows that some retailers have moved on this trend with greater speed, updating content across their webpages.

Overall, Adobe's data shows that while U.S. retailers have built a good foundation when it comes to AI visibility, there are glaring changes that need to be made. Consumer adoption of these AI tools is not slowing down, and businesses need to ensure their digital front doors are optimized for AI to remain relevant in today's environment.

Vivek is the director of Adobe Digital Insights who has worked with some of the largest CPG and Technology organizations in the world to drive key digital marketing and data science initiatives. As the Director for Adobe Digital Insights (ADI), he launched and spearheads the popular Adobe DEI (Digital Economy Index) and Holiday Retail reports, as well as other industry reports that profile emerging technology, creativity, and travel trends."

[note: this page's "AI Content Visibility Checker" score is the source's own use of the word "visibility" — it measures whether a page's own content is machine-readable, not whether the brand appears in a generated AI answer. This is a different sense from this repo's glossary.md "visibility" (appearances in generated answers). Kept as the source's own word per channels.md/glossary.md convention; not counted as a glossary-sense visibility figure.]

## Pull notes — mechanical only

- Page loaded and rendered fully on first navigation; `get_page_text` succeeded after one retry (initial call returned "No text content found," likely queried before client-side render completed).
- No paywall, login wall, or truncation encountered.
