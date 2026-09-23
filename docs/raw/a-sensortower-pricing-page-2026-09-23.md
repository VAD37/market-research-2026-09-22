# Sensor Tower — pricing / demo page and Pathmatics product page: no disclosed price

```yaml
source:          Sensor Tower (sensortower.com)
url_or_doc_id:   https://sensortower.com/pricing ; https://sensortower.com/pathmatics
published:       undated — no date on page
pull_date:       2026-09-23
pull_method:     fetch (curl, User-Agent "market-research-bot contact: research@example.invalid"; HTML tag-stripped)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary (own pages); carries no price
source_label:    vendor-reported
lane:            A
sub_market:      paid placement (ad intelligence incl. ChatGPT ads tracking)
engine:          OpenAI — ChatGPT (named on the Pathmatics page)
metric_kind:     none
supersedes:      none — complements raw/b-sensortower-chatgpt-ads-tracking-2026-09-23.md
captured:        pricing page headline block; Pathmatics page sentence naming ChatGPT advertising
```

## Verbatim

sensortower.com/pricing:

> Sensor Tower Demo | App, Web, Ad & Gaming Intelligence
> Solutions · Products · Blog · Resources · Company · Contact Sales · Log In
> Sensor Tower's MCP Server is Live! Explore MCP Integrations
> Gain a competitive edge in the global digital economy
> Measure consumer behavior and market performance across mobile app, ads, web, audience, and gaming. Get the insights you need to outsmart your competition and grow your business with Sensor Tower.
> [note: no plan names, no currency figures anywhere on the page; the only call to action is "Contact Sales"]

sensortower.com/pathmatics:

> US digital ad spend hit $200 billion between August 2025 and July 2026 as brands increasingly leveraged generative AI, ChatGPT advertising, and OTT streaming to drive performance.
> [note: sentence is a promotional lead for a Sensor Tower report; no method, n or window beyond the months stated; other ChatGPT references on the page: none]

## Pull notes — mechanical only

- `sensortower.com/product/digital-advertising` returned HTTP 404; the ad-intelligence product page is `/pathmatics`.
- The sitemap (`en-US-page-sitemap.xml`) lists no page with "chatgpt", "genai" or "ai-ad" in the path; ChatGPT ads tracking is described only in the 2026-08 blog post pulled earlier.
