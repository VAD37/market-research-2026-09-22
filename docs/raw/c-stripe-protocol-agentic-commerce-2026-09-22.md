# Stripe — Agentic commerce docs (docs.stripe.com/agentic-commerce and related pages)

```yaml
source:          Stripe (docs.stripe.com)
url_or_doc_id:   https://docs.stripe.com/agentic-commerce ; https://docs.stripe.com/agentic-commerce/for-sellers ; https://docs.stripe.com/payments/machine/x402 ; https://docs.stripe.com/payments/machine/mpp
published:       undated — no revision date on page; the for-sellers page uses live preview API version "2026-08-26.preview" and "2026-05-27.preview", dating the content to mid-2026
pull_date:       2026-09-22
pull_method:     fetch (curl with the .md markdown-source suffix Stripe docs support, and Accept-Language: en-US to avoid the default ja-JP locale)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default (platform primary — payment processor's own integration docs; Stripe is co-maintainer of ACP and a reference implementer of UCP, MPP and x402)
source_label:    company-stated
lane:            C
sub_market:      agentic commerce
engine:          n/a — payments rail, not an assistant engine; names ChatGPT (via ACP), Google AI Mode/Gemini (via UCP), and machine-payment clients generally
metric_kind:     none
supersedes:      none
captured:        full page (docs.stripe.com/agentic-commerce.md, /agentic-commerce/for-sellers.md, /payments/machine/x402.md — each fetched via Stripe's own ".md" markdown-source URL suffix)
```

## Verbatim

### docs.stripe.com/agentic-commerce (overview)

"# Agentic commerce

Sell through agents, or embed commerce into your AI interface.

Agentic commerce uses AI agents to support transactions between buyers and sellers, and to let agents transact on behalf of the people they serve. Stripe provides integrations for sellers to make their products and services available through agents, and for agent builders to embed commerce into their AI interfaces.

Buyers can browse products, get personalized recommendations, and complete purchases without leaving the conversation. Agents can also act on behalf of the people who use them, making purchases with a customer-controlled wallet and retrieving permissioned financial insights from connected accounts.

## Sellers

Stripe supports sellers who sell goods, subscriptions, digital content, or APIs. Learn how your business can sell products on agent platforms, or monetize your API or service using machine payments directly to personal agents like Claude Code.

## Agents (Private preview)

Agents act as intermediaries between buyers and sellers. They present product feeds, manage carts and checkout, and accept payments.

> This feature is in private preview. Join the waitlist: https://go.stripe.global/agentic-commerce-contact-sales."

**Choose your integration — Sellers: Sell through agents**

| | Sell through agents | Accept machine payments |
| --- | --- | --- |
| Share product catalog with agents | Supported | Unsupported |
| Enable agent to complete checkout | Supported | Supported |
| Receive payment credentials from agents | Supported | Supported |
| Process payments off-Stripe | Custom integration | Unsupported |
| **Protocol used** | UCP (ucp.dev) or ACP (agenticcommerce.dev) | MPP (Machine Payments Protocol) or x402 |

**Choose your integration — Agents: Embed commerce into your AI interface**

| | Embed products | Redirect to sellers | Fund your agent | Link CLI |
| --- | --- | --- | --- | --- |
| Browse seller product catalogs | Supported | Supported | Unsupported | Unsupported |
| Embed checkout flows in chats or advertisements | Supported | Unsupported | Unsupported | Unsupported |
| Share payment credentials with sellers | Supported | Unsupported | Unsupported | Unsupported |
| Create a wallet for your agent to use | Unsupported | Unsupported | Link or Crypto | Supported |
| Provide funds to your agent | Unsupported | Unsupported | Shared payment tokens or Crypto | Supported |
| Give your customers financial insights from their accounts | Unsupported | Unsupported | Unsupported | Supported |

"## See also
- Agents and AI on Stripe
- How agents work with Stripe"

### docs.stripe.com/agentic-commerce/for-sellers (excerpt — onboarding, feeds, checkout, fees/monitoring)

"# Sell through agents

Sell your products through AI agents using Agentic Commerce Suite.

Use Agentic Commerce Suite (ACS) to start selling through agents with a single integration. ACS helps you make your products discoverable and accept agentic payments across multiple commerce protocols. It lets you share product, price, and availability information with agents while minimizing changes to your existing commerce systems. **ACS is available in the US, Canada, and select European countries.**"

Full country list stated on the page (`View all supported countries`): AT, BE, BG, CA, CH, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GI, GR, HR, HU, IE, IT, LI, LT, LU, LV, MT, NL, NO, PL, PT, RO, SE, SI, SK, US.

"## Set up your Stripe account

To get set up for agentic commerce:
1. First, you need a Stripe account. Create an account.
2. After you create an account: Verify your email. Activate payments by providing business and personal information. Connect a bank account for payouts. Set up two-factor authentication.
[Then, in the Dashboard's Agentic commerce page:] Get started on 'Agentic commerce for retail', then choose to onboard as a seller. ... Configure tax. Stripe calculates tax at checkout using the values in your catalog feed, and incomplete configuration can cause checkouts to fail."

"## Create a catalog feed

Create a catalog feed to share your product and inventory data with agents. Format your feed as a CSV where each row is a product or variant..."

| Feed type | Frequency | Purpose |
| --- | --- | --- |
| Product data | Once per day | Titles, descriptions, images, and categories |
| Inventory | Every 15 minutes | Prevents agents from showing out-of-stock items |
| Pricing | Every 15 minutes | Helps keep the checkout price aligned with the quoted price |
| Promotions | As needed | Offers discount codes, deals, and free shipping to drive conversion |

"## Enable sales on an AI chat agent

When you're ready to sell through an AI interface:
1. Go to the Agentic commerce page in the Dashboard.
2. Find the agent you want to sell through and review its terms.
3. Click the overflow menu, then select **Request connection**.

We send the agent an approval request that the agent must accept. When the connection succeeds, the agent's Status column shows Enabled."

"## Respond to purchases and fulfill orders

Stripe sends `checkout.session.completed` after the agent completes an order. ... View orders on the Transactions page in the Dashboard, where they're tagged with the originating agent. You can also filter transactions by agent names."

No fee, commission, or take-rate figure for agentic-commerce transactions is stated anywhere on this page. Standard Stripe account/processing setup (bank account for payouts, tax configuration) is described, but the page states no agentic-specific fee percentage or flat fee.

### docs.stripe.com/payments/machine/x402 (Stripe's x402 implementation guide, excerpt)

"# x402 payments

Use x402 for machine-to-machine payments.

x402 (https://x402.org) is a protocol for internet payments. When a client requests a paid resource, your server returns an HTTP 402 response with payment details, including a Stripe deposit address. The client pays, then retries the request with authorization. After the facilitator settles the payment on-chain, Stripe records it as a PaymentIntent. **This feature is available to businesses with physical locations in all US states except New York, and in more than 30 countries.**"

"## Before you begin

> Stablecoin payments are available to businesses in all US states, except New York. For businesses operating outside of the US, email machine-payments@stripe.com with your Stripe account ID to request access to stablecoin payments in more than 30 countries.

1. Set up your Stripe account.
2. Go to your Payment methods settings in the Dashboard and request the **Stablecoins and Crypto** payment method. ...
3. Stripe reviews your access request and contacts you for more details if necessary. The payment method appears as **Pending** while we review your request.
4. After we approve your request, the **Stablecoins and Crypto** payment method becomes active in the Dashboard."

"x402 mainnet payments settle through the Coinbase Developer Platform (CDP) facilitator. Sign up for a Coinbase Developer Platform account, then create API keys..."

Token/network support table (verbatim): PaymentIntents with the `crypto` payment method in `mode: transaction_verification` support USDC on Tempo, Base, and Solana, each with its stated token contract address.

## Pull notes — mechanical only

- `docs.stripe.com` serves a locale-negotiated page; a plain `curl` without an `Accept-Language` header returned the `ja-JP` locale (title "エージェント型ワークフロー"). Adding `-H "Accept-Language: en-US,en;q=0.9"` returned the English page. Stripe's docs platform also serves a clean markdown source at the same path with a `.md` suffix appended (e.g. `https://docs.stripe.com/agentic-commerce.md`), used for the excerpts above — confirmed to return the same content as the rendered HTML page, via a direct `WebFetch` cross-check of the rendered page against the `.md` fetch.
- `docs.stripe.com/en-us/agentic-commerce` (an explicit locale path) returned 404; the locale is controlled by the `Accept-Language` header, not a URL segment.
- The comparison table's "✓ Supported" / "- Unsupported" symbols are reproduced as "Supported" / "Unsupported" for table-rendering; no other wording changed.
- **Gating language found:** the "Agents (Private preview)" section is explicitly gated — "This feature is in private preview. Join the waitlist" — this is the agent-builder side of Stripe's own integration (embedding third-party commerce into an AI interface), distinct from the seller-side "Sell through agents" flow, which is self-serve via an ordinary Stripe account (no waitlist language on the for-sellers page). The x402/stablecoin payment method is also gated behind a Stripe review-and-approval step ("Pending" state) before activation, and non-US businesses must separately email `machine-payments@stripe.com` to request access.
- No fee/commission/settlement percentage found on any of the three pages fetched. Standard Stripe processing likely applies to agentic-commerce checkout sessions (they use ordinary Stripe `checkout.session` objects per the for-sellers page's webhook example), but no page in this pull states a rate — recorded as `unknown — checked docs.stripe.com/agentic-commerce, /agentic-commerce/for-sellers, /payments/machine/x402, /payments/machine/mpp 2026-09-22`.
- `docs.stripe.com/payments/machine/mpp.md` (Machine Payments Protocol) and `docs.stripe.com/agentic-commerce/for-agents.md` were fetched but are thin (449 bytes for for-agents; MPP page describes Stripe's own card-based machine-payment protocol, distinct from x402/ACP/UCP/AP2) — not reproduced verbatim here as they add no further overview/scope/licence/governance/fee content beyond what is captured above; both files are locally saved (`/tmp/stripe_payments_machine_mpp.md`, `/tmp/stripe_agentic-commerce_for-agents.md`) but not part of this repo.
- Did not touch `dashboard.stripe.com` (requires login) or any `chatgpt.com`/`claude.ai`/`perplexity.ai`/`gemini.google.com`/`copilot.microsoft.com` surface.
