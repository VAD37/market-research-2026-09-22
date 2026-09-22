# PayPal — Agentic commerce services and ACP integration (developer.paypal.com)

```yaml
source:          PayPal (developer.paypal.com)
url_or_doc_id:   https://developer.paypal.com/agentic-commerce-services/about ; https://developer.paypal.com/agent-ready/agentic-commerce-protocol
published:       both pages state "Last updated: June 10, 2026"
pull_date:       2026-09-22
pull_method:     browser extension (get_page_text)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default (platform primary — PayPal's own developer documentation)
source_label:    company-stated
lane:            C
sub_market:      agentic commerce
engine:          ChatGPT — OpenAI (via ACP integration, Braintree as payment provider); also names Microsoft Copilot as a PayPal Store Sync surface (per c-microsoft-protocol-ucp-adoption-2026-09-22.md, cross-referenced not duplicated)
metric_kind:     none
supersedes:      none
captured:        agentic-commerce-services/about full page text; agent-ready/agentic-commerce-protocol full page text (ACP-to-Braintree integration guide)
```

## Verbatim

### developer.paypal.com/agentic-commerce-services/about (full)

"Agentic commerce services overview

Overview of PayPal's agentic commerce services, which enable merchants to create AI-powered shopping experiences for customers. Last updated: June 10, 2026

Merchants can use PayPal's agentic commerce services to create AI-powered shopping experiences, so customers can shop using everyday language. These services help customers find products, manage their shopping carts, and complete purchases across different online stores and platforms.

**To access and use agentic commerce services, merchants must complete this form to contact the AI team at PayPal and request access. The PayPal AI team will follow up after your form submission to guide you through onboarding.**

## Benefits

- **Easy setup:** Connect your product listings to PayPal's partners like Wix, Cymbio, Commerce (BigCommerce & Feedonomics), and Shopware to make your products easy for customers to find and buy.
- **Better product discovery and more sales:** Help customers find your products through AI shopping assistants that understand what they're looking for.
- **Keep control of your customer relationships:** With Store Sync, which includes product catalog integration and cart operations, you stay in charge of your business. You control your brand appearance and customer communications.
- **Connect once to reach many platforms:** With Store Sync and Agent Ready, you can connect to PayPal once and reach customers across multiple AI shopping platforms.

## Agent Ready

Agent Ready enables merchants to accept payments through AI assistants with minimal changes to their current payment setup. This includes things like accepting payments for customers who are shopping through a store's shopping bot within ChatGPT. Instead of building separate connections for each AI platform, you can use your existing PayPal tools while PayPal handles security and compatibility across different platforms. Agent Ready can grow with your business, supporting both supervised and automatic shopping scenarios.

## Store Sync

Store Sync enables merchants to make their products discoverable by AI shopping assistants and lets customers place orders directly into your existing order management systems. Customers can tell an AI assistant what they want, and the AI can connect to your store to help find products, manage shopping carts, and complete purchases without leaving their chosen AI platform."

### developer.paypal.com/agent-ready/agentic-commerce-protocol (full — ACP-to-Braintree integration guide)

"Agentic Commerce Protocol integration

Last updated: June 10, 2026

Use this guide to build a custom ChatGPT app that accepts payments using the Agentic Commerce Protocol (ACP) and the ChatGPT Apps SDK. This guide walks you through configuring Braintree as your payment provider, processing delegated payment tokens, and testing your integration.

**Prerequisites:** Build your app using the ChatGPT Apps SDK. Implement an MCP server with the `complete_checkout` tool to receive tokens. Call `requestCheckout()` from the app to trigger Instant Checkout. Follow the ACP agentic checkout specification to manage checkout sessions. Specify `braintree` as your payment provider. Process payment tokens using your existing Braintree integration.

## Step 1: Specify Braintree as your payment provider

When your ChatGPT app widget calls `requestCheckout()`, you must construct a checkout session that specifies Braintree as the payment provider according to the ACP Agentic Checkout Specification.

```javascript
const checkoutRequest = {
  id: checkoutSessionId,
  payment_provider: {
    provider: \"braintree\",
    merchant_id: \"your_braintree_merchant_id\",
    supported_payment_methods: [\"card\", \"applepay\", \"googlepay\"],
  },
  status: \"ready_for_payment\",
  currency: \"USD\",
  totals: [{ type: \"total\", display_text: \"Total\", amount: 330 }],
  links: [
    { type: \"terms_of_use\", url: \"https://yoursite.com/terms\" },
    { type: \"privacy_policy\", url: \"https://yoursite.com/privacy\" },
  ],
  payment_mode: \"live\",
};
const order = await window.openai.requestCheckout(checkoutRequest);
```

Available `supported_payment_methods` values today: `card`, `applepay`, `googlepay`. Stated as coming soon: `paypal_wallet`, `venmo_wallet`.

## Step 2: Complete checkout and process payments

Your MCP server must expose a `complete_checkout` tool that receives the token and processes it, using the payment method nonce exactly as with Braintree's `transaction.sale` method or `chargePaymentMethod` GraphQL mutation. The payment token in `payment_data.token` (e.g. `tokencc_bf_abc123_456def_ghijkl_mno789_pqr`) is a one-time-use token — in Braintree, a payment method nonce — bound to your merchant ID, with amount and time restrictions you can configure.

## Allowance validation

Braintree validates the following fields in the allowance when issuing a delegated payment token: `merchant_id` (must match your Braintree public merchant ID); `max_amount` (must be ≥ the transaction amount); `currency` (must match the configured currency); `expires_at`.

## Track AI-initiated transactions

Transaction responses include `transaction.facilitator_details.oauth_application_client_id` and `transaction.facilitator_details.oauth_application_name` (e.g. `\"ChatGPT\"`). Merchants can search transactions by AI platform in the Braintree Control Panel (filter on `facilitator_details.oauth_application_name`) or via a GraphQL API query."

## Pull notes — mechanical only

- Both pages accessed via the Chrome extension, `get_page_text`, in the same tab used for Visa and Mastercard (navigated in sequence, closed after use).
- **Two distinct gates found on the PayPal side, not to be conflated:** (1) PayPal's own broader "agentic commerce services" (Store Sync + Agent Ready, PayPal's product for connecting a merchant catalog across many AI platforms at once) is **access-gated** — "merchants must complete this form to contact the AI team at PayPal and request access" — no self-serve path is documented; (2) the narrower **ACP-to-Braintree integration guide is not gated on this page** — no request-access language appears on `developer.paypal.com/agent-ready/agentic-commerce-protocol` itself; a developer can read the full ACP/Braintree integration guide, including code samples, without an access-request step described on the page. This is a load-bearing distinction for H8's "could a merchant implement from the public text alone" question: yes for the ACP/Braintree integration specifically (ordinary Braintree merchant account plus the published guide); no for PayPal's own broader agentic-commerce-services product (request-access form required).
- No fee, commission, or settlement-cut percentage found on either page. Standard Braintree/PayPal merchant processing terms presumably apply to transactions completed this way, but neither page states a rate specific to agentic/ACP-routed transactions. Recorded `unknown — checked developer.paypal.com/agentic-commerce-services/about, developer.paypal.com/agent-ready/agentic-commerce-protocol 2026-09-22`.
- The ACP integration page's "Next Page" link ("Universal commerce protocol integration") indicates PayPal also publishes a parallel UCP-to-Braintree/PayPal integration guide at a sibling URL under `/agent-ready/` — not fetched in this pull (out of the task's named-target list; noted here as a lead for a future pull, not claimed as content).
- PayPal's separate "Agent Payments Protocol (AP2)" support statement (a PayPal-authored community blog post, per search results: "PayPal announced its support for the Agent Payments Protocol (AP2)... proposed by Google in collaboration with PayPal and other industry partners") was found via web search only and not independently fetched in this pull — recorded `unknown — checked developer.paypal.com/community/blog/PayPal-Agent-Payments-Protocol/ only via search-result snippet, not pulled verbatim, 2026-09-22`.
