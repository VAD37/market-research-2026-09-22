# Digital Commerce 360, pointer to McKinsey & Company — "McKinsey forecasts up to $5 trillion in agentic commerce sales by 2030"

```yaml
source:          Digital Commerce 360 (pointer, author Mark Brohan), primary McKinsey & Company, "The Agentic Commerce Opportunity" (October 2025)
url_or_doc_id:   https://www.digitalcommerce360.com/2025/10/20/mckinsey-forecast-5-trillion-agentic-commerce-sales-2030/ ; McKinsey primary at mckinsey.com/industries/retail/our-insights/ (attempted direct fetch this pull, connection failure to mckinsey.com robots.txt — not independently confirmed against the primary)
published:       2025-10-20 (Digital Commerce 360 article); McKinsey's own report dated October 2025 per this article's framing ("McKinsey's 'The Agentic Commerce Opportunity' (October 2025)" — this framing itself comes from a second pointer, stellagent.ai, see `e-market-size-stellagent-agentic-2026-09-22.md` in this cluster, not independently confirmed against McKinsey's own page)
pull_date:       2026-09-22
pull_method:     fetch (mcp fetch tool; digitalcommerce360.com fetched cleanly, no 403, no paywall on this specific article; mckinsey.com direct fetch attempted, failed on a robots.txt connection error, not a 403 — recorded as blocked either way)
pull_purpose:    evidence about a number
tier:            5
tier_reason:     trade-press pointer to a named consulting-firm report ("The Agentic Commerce Opportunity") with a named McKinsey partner quoted, but no sample size, survey instrument, or method statement relayed anywhere in this article; per trust-rubric.md "5 pointer" for trade press linking primary data where the primary itself was not independently reachable this pull
source_label:    analyst-derived
lane:            C
sub_market:      agentic commerce
engine:          n/a — describes "AI agents" and named protocols (MCP, A2A, AP2, ACP) generically, no named-assistant revenue breakout
metric_kind:     none
supersedes:      none
captured:        full article up to the fetch tool's per-call truncation point (article continues into a "Sign up" newsletter CTA and "Related Stories" list — not captured further, not load-bearing for the headline figures already captured)
```

## Verbatim

Headline: "McKinsey forecasts up to $5 trillion in agentic commerce sales by 2030." By-line: "Mark Brohan | Oct 20, 2025." Sub-headline (deck): "AI agents shop, negotiate and transact on behalf of humans — and could generate as much as $1 trillion in orchestrated U.S. retail revenue by 2030, McKinsey estimates."

The size and forecast figures (the sentence carrying the numbers — two figures, US and global, given together):

> "According to new research from management consulting firm McKinsey & Company, agentic commerce — a model in which artificial intelligence (AI) agents shop, negotiate and transact on behalf of humans — could generate as much as $1 trillion in orchestrated U.S. retail revenue by 2030, and as much as $3 trillion to $5 trillion globally."

Framing quote, defining the term as McKinsey uses it:

> "McKinsey describes agentic commerce as a 'seismic shift' that will transform shopping from a series of discrete steps — searching, browsing, comparing and buying — into a continuous, intent-driven flow powered by autonomous AI systems... 'This is not just an evolution of ecommerce,' McKinsey's analysis notes. 'It's a rethinking of shopping itself.'"

Named-partner quote:

> "Becca Coggins, a McKinsey senior partner and global leader for the firm's retail and consumer packaged goods practices, described agentic commerce as a fundamental reconfiguration of the customer journey. 'Instead of users visiting a site or app,' she explained, 'autonomous agents do the legwork — searching, filtering, comparing and even purchasing on behalf of the customer.'"

Named protocols the report cites as the technical substrate (context, not a size figure):

> "Among the frameworks gaining traction are: Model Context Protocol (MCP), Agent-to-Agent Protocol (A2A), Agent Payments Protocol (AP2), Agentic Commerce Protocol (ACP)."

## Pull notes — mechanical only

- `digitalcommerce360.com` fetched cleanly, no 403, no paywall encountered on this specific article (the site's own homepage/nav elsewhere shows a "Sign Into... Not a member? Join for free" prompt, but this article's body rendered in full to plain fetch).
- `mckinsey.com/industries/retail/our-insights/the-agentic-commerce-opportunity` (a guessed URL slug, not independently confirmed as McKinsey's actual published URL for this report) returned a connection failure at the robots.txt-fetch step — recorded as blocked, entered on the **browser backlog**: `mckinsey.com` — needs a browser-capable tool to locate and fetch McKinsey's own report page for "The Agentic Commerce Opportunity."
- No sample size, survey method, or model methodology relayed in this article for either the $1T US or $3T-$5T global figure — both are presented as McKinsey firm estimates.
- This is the largest figure of any agentic-commerce forecast pulled in this cluster (global $3T-$5T by 2030), roughly 8-16x Morgan Stanley's high case ($385B) and 6-10x Bain's high case ($500B) for the comparable US-only figure ($1T McKinsey US vs. those two) — kept side by side, not averaged, per root `CLAUDE.md`.
