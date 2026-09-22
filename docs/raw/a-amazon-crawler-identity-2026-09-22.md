# Amazon Developer — crawler identity (Amazonbot, Amzn-SearchBot, Amzn-User)

```yaml
source:          Amazon (developer.amazon.com)
url_or_doc_id:   https://developer.amazon.com/amazonbot
published:       "Published Date: September 04, 2026" (stated at foot of page)
pull_date:       2026-09-22
pull_method:     browser extension
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary, own crawler documentation
source_label:    company-stated
lane:            A
sub_market:      n/a
engine:          Amazon Rufus / Alexa (priority-2)
metric_kind:     none
supersedes:      none
captured:        full page
```

## Verbatim

Title: "About AmazonBot"

"This page describes how webmasters can control Amazonbot, Amzn-SearchBot, and Amzn-User interactions with their site. Each user agent setting is independent of the others, and may take ~24 hours for our systems to reflect changes."

**Amazonbot** — "Amazonbot is used to improve our products and services. This helps us provide more accurate information to customers and may be used to train Amazon AI models."
Example User Agent String: `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Amazonbot/0.1) Chrome/W.X.Y.Z Safari/537.36`
Published IP Addresses: https://developer.amazon.com/amazonbot/ip-addresses/

**Amzn-SearchBot** — "Amzn-SearchBot is used to improve search experiences in Amazon products and services. By permitting Amzn-SearchBot access to your website, your content is eligible to appear in search experiences such as Alexa. If robots.txt files don't mention Amzn-SearchBot but allow other search bots, Amzn-SearchBot will crawl in accordance with the robots.txt directives given to other search bots. Amzn-SearchBot does not crawl content for generative AI model training."
Example User Agent String: `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Amzn-SearchBot/0.1) Chrome/W.X.Y.Z Safari/537.36`
Published IP Addresses: https://developer.amazon.com/amazonbot/searchbot-ip-addresses/

**Amzn-User** — "Amzn-User supports user actions, such as responding to Alexa queries that require up-to-date information. For example, when a customer asks a question, Amzn-User may fetch live information from the web to provide accurate answers on the user's behalf. Because actions taken by Amzn-User can be initiated by a user, it may not follow all robots.txt directives. Amzn-User does not crawl content for generative AI model training."
Example User Agent String: `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Amzn-User/0.1) Chrome/W.X.Y.Z Safari/537.36`
Published IP Addresses: https://developer.amazon.com/amazonbot/live-ip-addresses/

"Our Approach to Robots.txt — Automated crawling from these listed user agents respects the Robots Exclusion Protocol, honoring the user-agent and the allow/disallow directives. They will fetch host-level robots.txt files or use a cached copy from the last 30 days. When a file can't be fetched, they will behave as if it does not exist. These user agents attempt to read robots.txt files at the host level (for example example.com), so they look for robots.txt at example.com/robots.txt. If a domain has multiple hosts, then they will honor robots rules exposed under each host. For example, if there is also a site.example.com host, they will look for robots.txt at site.example.com/robots.txt. When these user agents access web pages they respect the link-level rel=nofollow directive, and page level robots meta tags of noarchive (do not use the page for model training), noindex (do not index the page) and none (do not index the page). They do not support the crawl-delay directive."

"Contact Us — If you are a content owner or publisher and have questions, please contact us at amazonbot@amazon.com. Always include any relevant domain names in your message."

"Explore more — If you allow Amazonbot on your robots.txt, you may be eligible for benefits with Amazon Content Partners. Amazon Content Partners gives independent content creators a +1% affiliate commission boost on eligible sales, free hosting credits, and AI traffic management tools — all in one program. Learn more at contentpartners.amazon.com."

"Published Date: September 04, 2026"

## Pull notes — mechanical only

- Navigated directly (`developer.amazon.com/amazonbot`); loaded via Chrome extension on first navigation, no redirect, no sign-in wall for this page's content.
- Three user agents named, roles split identically to OpenAI's and Anthropic's three-way split: training/product-improvement (Amazonbot — explicitly "may be used to train Amazon AI models"), search-indexing (Amzn-SearchBot — explicitly does not train models), user-initiated action (Amzn-User — explicitly does not train models).
- Page carries an explicit publish date, "September 04, 2026" — inside the one-quarter staleness window as of this 2026-09-22 pull, not flagged stale.
- No crawl-volume or crawl-to-refer figures on this page — identity and policy only.
