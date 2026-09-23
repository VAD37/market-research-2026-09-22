# OpenAI — "Buy it in ChatGPT: Instant Checkout and the Agentic Commerce Protocol" (2025-09-29; full post reached)

```yaml
source:          OpenAI (Product post on openai.com)
url_or_doc_id:   https://openai.com/index/buy-it-in-chatgpt/
published:       2025-09-29 ("September 29, 2025" on page)
pull_date:       2026-09-23
pull_method:     fetch (curl, HTTP 200, 431,445 bytes; body in static HTML) — openai.com was 403 to fetch on 2026-09-22 and on the earlier 2026-09-23 pull; curl with the bot user agent returned 200 on this pull
pull_purpose:    evidence about a number
tier:            3
tier_reason:     platform primary — the engine vendor's own launch post; reliable on existence and stated terms, biased on framing; table default
source_label:    company-stated
lane:            B
sub_market:      agentic commerce
engine:          ChatGPT — OpenAI (Instant Checkout)
metric_kind:     none
supersedes:      e-engine-user-count-checks-2026-09-23.md (openai.com/index/buy-it-in-chatgpt/ listed as 403 to fetch; not opened)
captured:        full post: intro, "How Instant Checkout works", "The Agentic Commerce Protocol", "Built for trust", "Just the start", one partner quote (Stripe) rendered in the extract; one diagram image saved
```

## Verbatim

OpenAI · September 29, 2025 · Product

Buy it in ChatGPT: Instant Checkout and the Agentic Commerce Protocol

We’re taking first steps toward agentic commerce in ChatGPT with new ways for people, AI agents, and businesses to shop together.

More than 700 million people turn to ChatGPT each week for help with everyday tasks, including finding products they love. Starting today, we’re taking the first steps toward ChatGPT helping people buy them too—beginning with Instant Checkout, powered by the Agentic Commerce Protocol, built with Stripe.

U.S. ChatGPT Plus, Pro, and Free users can now buy directly from U.S. Etsy sellers right in chat, with over a million Shopify merchants, like Glossier, SKIMS, Spanx and Vuori, coming soon. Today, Instant Checkout supports single-item purchases. Next, we’ll add multi-item carts and expand merchants and regions.

We’re also open-sourcing the technology that powers Instant Checkout, the Agentic Commerce Protocol, so that more merchants and developers can begin building their integrations. The Agentic Commerce Protocol is an open standard for AI commerce that lets AI agents, people, and businesses work together to complete purchases. We co-developed it with Stripe and leading merchant partners to be powerful, secure, and easy to adopt.

This marks the next step in agentic commerce, where ChatGPT doesn’t just help you find what to buy, it also helps you buy it. For shoppers, it’s seamless: go from chat to checkout in just a few taps. For sellers, it’s a new way to reach hundreds of millions of people while keeping full control of their payments, systems, and customer relationships.

We’re making this protocol and our documentation available today so interested merchants and developers can begin building integrations. When you’re ready to make your products available for purchase through ChatGPT, you can apply here.

How Instant Checkout works

When someone asks a shopping question—“best running shoes under $100” or “gifts for a ceramics lover” — ChatGPT shows the most relevant products from across the web. Product results are organic and unsponsored, ranked purely on relevance to the user.

If a product supports Instant Checkout, users can tap “Buy,” confirm their order, shipping, and payment details, and complete the purchase without ever leaving the chat. Existing ChatGPT subscribers can pay with their card on file, or other card and express payment options.

Orders, payments, and fulfillment are handled by the merchant using their existing systems. ChatGPT simply acts as the user’s AI agent—securely passing information between user and merchant, just like a digital personal shopper would.

Merchants pay a small fee on completed purchases, but the service is free for users, doesn’t affect their prices, and doesn’t influence ChatGPT’s product results. Instant Checkout items are not preferred in product results. When ranking multiple merchants that sell the same product, ChatGPT considers factors like availability, price, quality, whether a merchant is the primary seller, and whether Instant Checkout is enabled, to optimize the user experience.

The Agentic Commerce Protocol

At the core of this experience is the Agentic Commerce Protocol which provides the language that lets AI agents and businesses work together to complete a purchase for a user.

[image: docs/raw/img/b-openai-buy-it-in-chatgpt-instant-checkout-primary-2026-09-23/01-acp-flow-diagram.png] — Agentic Commerce Protocol diagram (Contentful asset "ACP_-_POR__1_.png"; no alt text in HTML)

We built the Agentic Commerce Protocol with Stripe and leading merchants to: Work across platforms, payment processors, and business types. Integrate quickly without changing their backend systems. Keep merchants in control of the customer relationship as the merchant of record across the purchase journey–from fulfillment and returns to support and communication.

When someone places an order, ChatGPT sends the necessary details to the merchant’s backend using Agentic Commerce Protocol. The merchant accepts or declines the order, processes the payment via their existing provider, and handles fulfillment and customer support exactly as they do today.

If a merchant already processes payments with Stripe, they can enable agentic payments in as little as one line of code. If they use another payment processor, they can still participate in Instant Checkout and accept agentic payments either by using Stripe’s new Shared Payment Token API or adopting the Delegated Payments Spec in the Agentic Commerce Protocol—all without changing their existing payment processor.

Built for trust

We believe agentic commerce should be built for trust. In this early stage of the AI commerce future: Users stay in control — they explicitly confirm each step before any action is taken. Payment is secure — encrypted payment tokens are only authorized for specific amounts and specific merchants with the user’s permission. Data sharing is minimal — only the information required to complete the order is shared with the merchant, with the user’s permission.

Partner perspectives (Stripe · Etsy · Shopify — tabbed; only the Stripe quote rendered in the extract):

> "Stripe is building the economic infrastructure for AI. That means re-architecting today’s commerce systems and creating new AI-powered experiences for billions of people. We’re proud to power Instant Checkout in ChatGPT and co-develop the Agentic Commerce Protocol to help businesses and AI platforms build the future of commerce." – Will Gaybrick, President, Technology and Business, Stripe

[note: the Etsy and Shopify partner quotes sit in tabs not rendered in the static extract — not captured]

Just the start

This launch is just the beginning. As AI becomes a key interface for how people discover, decide, and buy, the Agentic Commerce Protocol provides a foundation that connects people and businesses for the next era of commerce.

## Pull notes — mechanical only

- curl HTTP 200 with the bot user agent; body in static HTML. The bot wall recorded on 2026-09-22 (403) did not recur on this pull. The bypass extension was not involved.
- One in-body image (Contentful `images.ctfassets.net/.../ACP_-_POR__1_.png`) saved by curl; the cover image and "Keep reading" thumbnails skipped as decorative.
- The fee sentence — "Merchants pay a small fee on completed purchases" — states a fee exists but no rate; recorded as printed.
- No login, no form.
