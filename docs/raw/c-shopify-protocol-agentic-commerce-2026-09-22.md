# Shopify — Agentic commerce / UCP adoption (shopify.dev)

```yaml
source:          Shopify (shopify.dev)
url_or_doc_id:   https://shopify.dev/docs/agents
published:       undated — no revision date on page
pull_date:       2026-09-22
pull_method:     browser extension (get_page_text)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default (platform primary — Shopify's own developer documentation)
source_label:    company-stated
lane:            C
sub_market:      agentic commerce
engine:          n/a — commerce platform, not an assistant engine; page is built around Google's Universal Commerce Protocol (UCP) and names Claude Code, Codex, Antigravity CLI, Cursor, and VS Code as supported agent tools for its own CLI
metric_kind:     none
supersedes:      none
captured:        full page text (shopify.dev/docs/agents)
```

## Verbatim

### shopify.dev/docs/agents (full)

"Build commerce agents with UCP

Build unified agentic experiences that securely act on behalf of buyers with the **Universal Commerce Protocol (UCP)** and Shopify's UCP-compliant MCP servers.

## Get started

Install the UCP CLI and Shopify AI Toolkit plugin for your supported AI tool. Built for agent workflows, the CLI provides structured commands to search the Catalog, build carts, create checkouts, hand off buyers, and track orders. The toolkit's `ucp` skill helps agents apply UCP best practices against each merchant's live schema.

Before you install, make sure you have Node.js 18 or higher. The toolkit is supported on any agent that supports the skills format. [Tabs for: Claude Code, Codex, Antigravity CLI, Cursor, VS Code]

```
npm install -g @shopify/ucp-cli
claude plugin install shopify-ai-toolkit@claude-plugins-official
```

## Access universal cart

One Cart, every brand. The Universal Cart API lets AI agents collect items from any merchant, on or off Shopify, into a single, unified cart, all via UCP.

**Request access — Join the early access waitlist.**

## Understand how Shopify does UCP

Shopify's MCP tools implement UCP at every step of the buyer journey: **Negotiate and authenticate** — Identify your agent and get the right access tier. **Discover products** — Search across hundreds of millions of Shopify listings. **Carts and checkout** — Build carts, convert them to checkouts, and hand off to the merchant for payment. **Monitor orders** — Receive order webhooks and fetch fresh order state on demand.

### Negotiate and authenticate

Define a profile so Shopify can verify your agent and apply the right rate limits and tool access. **Higher trust tiers unlock broader access, including direct checkout completion.** Profiles are hosted at a well-known URL and referenced on every UCP request.

- *About profiles* — Host a UCP profile for capability negotiation and signed-request verification.
- *Auth and rate limiting* — Trust tiers, capability matrix, and rate limits per tier.

### Discover products

Query products across all Shopify merchants with the **Global Catalog**, or scope results to a single merchant with a **Storefront Catalog**. When buyers pick a product, fetch the variant details you need to build a cart or hand off to a checkout permalink.

### Build carts and convert to checkout

Build carts as buyers iterate. Add line items, apply localization, and estimate totals across multiple turns of conversation. When buyers are ready, convert the cart into a checkout and refer them to the merchant storefront to complete payment. **Trusted agents can complete checkouts directly.**

- *Cart MCP* — Build and iterate on carts with line items, localization, and buyer context.
- *Checkout MCP* — Convert carts into checkouts and complete purchases for trusted agents.

### Monitor orders

After checkout, monitor order lifecycle changes (fulfillment events, refunds, returns, exchanges, and cancellations) with UCP-shaped order webhooks. Fetch fresh order state on demand with the `get_order` MCP tool when the buyer asks 'Where's my order?' or when reconciling a missed webhook.

- *Order MCP* — Fetch fresh order state on demand with the `get_order` tool.
- *Order webhooks* — Subscribe to lifecycle events for fulfillment, returns, refunds, and edits."

## Pull notes — mechanical only

- Accessed via the Chrome extension, `get_page_text`, in the same tab used for Visa/Mastercard/PayPal (navigated in sequence, closed after use).
- Shopify does not publish its own separate agentic-commerce protocol; this page describes Shopify's implementation of Google's UCP, consistent with Google's own UCP announcement naming Shopify as a co-developer (per `c-google-ucp-merchant-agentic-2026-09-22.md`, already landed) and with UCP's own governance file listing four named Shopify individuals across its Shopping, Payments, and Governance Councils (per `c-ucp-protocol-universal-commerce-2026-09-22.md`, this cluster).
- **Two distinct gates found, both named explicitly on this one page:** (1) "Higher trust tiers unlock broader access, including direct checkout completion" — a tiered-trust gate on the UCP profile/authentication layer itself (an agent must negotiate a profile and earn a trust tier; the exact tier criteria are on a linked "Auth and rate limiting" sub-page, not reached in this pull — a direct navigation guess at `shopify.dev/docs/agents/auth` returned a 404, so the correct sub-page URL was not identified in this pull; recorded `unknown — checked shopify.dev/docs/agents, shopify.dev/docs/agents/auth (404) 2026-09-22`); (2) "Access universal cart... Request access — Join the early access waitlist" — an explicit early-access waitlist gate on the cross-merchant "Universal Cart API" feature specifically (distinct from ordinary single-merchant Catalog/Cart/Checkout MCP tools, which the page presents as generally available with no waitlist language).
- No fee, commission, or settlement-cut clause found on this page. Shopify's Checkout MCP hands off to "the merchant storefront to complete payment" (or, for trusted agents, "complete purchases directly") using the merchant's own existing Shopify payment configuration — no agentic-specific fee is stated here. Recorded `unknown — checked shopify.dev/docs/agents 2026-09-22`.
- Did not fetch the linked sub-pages (`About profiles`, `Auth and rate limiting`, `Global Catalog`, `Storefront Catalog`, `Cart MCP`, `Checkout MCP`, `Order MCP`, `Order webhooks`) — their hrefs were present in the rendered text but not resolved by `get_page_text`; recorded as unfetched, not as absent content.
- Cross-reference, not re-pulled: `c-openai-shopify-merchants-2026-09-22.md` (already landed under P2-c3) covers OpenAI's help-center page on Shopify merchants appearing in ChatGPT via the separate "Agentic Storefronts" integration (ACP-side, checkout on the merchant's own Shopify storefront) — a different Shopify integration from the UCP-based one described in this file.
