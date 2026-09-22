# Scrunch AI — engines covered, vendor's own statement

```yaml
source:          Scrunch AI (scrunch.com FAQ and pricing page)
url_or_doc_id:   https://scrunch.com/faqs/what-ai-models-and-agents-does-scrunch-currently-track-traffic-for/ ; https://scrunch.com/pricing
published:       undated — no date on page
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary FAQ and pricing page
source_label:    vendor-reported
lane:            A
sub_market:      organic recommendation
engine:          ChatGPT, Claude, Perplexity, Gemini, Meta AI, Google AI Mode, Google AI Overviews (AIO), Copilot, Grok — see verbatim for exact framing and the tier split between the Core and Enterprise pricing plans
metric_kind:     none
supersedes:      none
captured:        FAQ answer in full; pricing-page LLM-count lines reproduced from `a-scrunch-pricing-2026-09-22.md`, not re-quoted in full here
```

## Verbatim

### "What AI models and agents does Scrunch currently track traffic for?"

"Also asked as: Which AI bots can Scrunch detect on my website? / How do I see which AI platforms are crawling my site?

Scrunch currently tracks traffic for these AI platforms: ChatGPT, Gemini, Perplexity, Google AI Overviews, Google AI Mode, Claude, Meta AI, Copilot, and Grok.

## Example

For example, a Scrunch user who connects their CDN or web service provider to the Agent Traffic feature can see all AI bot traffic on their website over time.

Traffic is segmented by model and bot request type (i.e., training, indexer, or retrieval), so users can see which models are most active, what they're doing on the site, which pages they're crawling most often, and how bot activity compares to human traffic.

Scrunch also provides a chronological log of all bot requests.

### Follow-up question: Why does it matter whether a bot is training, indexing, or retrieving?

Different bot request types signal different things. Training bots indicate that AI platforms are collecting content as source material. Indexer bots mean content is being catalogued for future retrieval. And retrieval bots represent the highest intent: A real user just asked an AI a question and it came to the website looking for an answer."

### Cross-reference — pricing-page engine tiering (from `a-scrunch-pricing-2026-09-22.md`)

Core plan ($250/mo): "4 LLMs supported — ChatGPT, Perplexity, Google AIO, Copilot"
Enterprise plan (custom): "9 LLMs supported — ChatGPT, Claude, Perplexity, Gemini, Meta AI, Google AI Mode, Google AIO, Copilot, Grok"

## Pull notes — mechanical only

- FAQ page fetched via mcp__MCP_DOCKER__fetch, simplified/markdown rendering, full answer captured (no truncation on this specific page).
- Two distinct engine lists exist on Scrunch's own site: the FAQ's "traffic tracking" list (9 platforms, not tier-gated — describes the Agent Traffic / crawler-detection feature) and the pricing page's "LLMs supported" list (also 9 at Enterprise, but only 4 at the Core/entry tier — describes the answer-monitoring feature). Both are reproduced verbatim above without reconciling them; the FAQ list is for bot/crawler traffic detection specifically, the pricing list is for prompt-response monitoring specifically — these are stated by Scrunch as two different product capabilities, not necessarily the same underlying engine-coverage claim.
