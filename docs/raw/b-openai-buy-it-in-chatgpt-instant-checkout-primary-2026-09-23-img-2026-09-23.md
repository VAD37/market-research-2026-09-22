# OpenAI — "Buy it in ChatGPT" — image read (IMG-1b)

```yaml
source:          OpenAI (Product post on openai.com) — one in-body image
url_or_doc_id:   https://openai.com/index/buy-it-in-chatgpt/
published:       2025-09-29 (page dateline, per source raw file)
pull_date:       2026-09-23
pull_method:     image read (IMG-1b) — Read tool on the PNG saved by curl in the source pull
pull_purpose:    evidence about a number
tier:            3
tier_reason:     inherits b-openai-buy-it-in-chatgpt-instant-checkout-primary-2026-09-23.md
source_label:    company-stated (diagram carries no number; label as the page's author)
lane:            B
sub_market:      agentic commerce
engine:          ChatGPT — OpenAI (Instant Checkout)
metric_kind:     none
supersedes:      none — reads the image referenced in b-openai-buy-it-in-chatgpt-instant-checkout-primary-2026-09-23.md
captured:        one image, transcribed in full
```

## 01-acp-flow-diagram

image: docs/raw/img/b-openai-buy-it-in-chatgpt-instant-checkout-primary-2026-09-23/01-acp-flow-diagram.png (3556 × 3104 px)

Chart type: sequence / swim-lane flow diagram, four vertical lanes, no axes, no numbers.

Title printed: "Agentic Commerce Protocol" — subtitle "Powering Instant Checkout in ChatGPT".

Lane headers, left to right: "User" · "ChatGPT" · "Merchant" · "Payment Processor".

Steps, top to bottom, with arrow direction:

1. User → ChatGPT → Merchant: "User taps "Buy" Confirms payment and shipping address" (User lane) → "Gathers fulfillment options for the item and address" (Merchant lane).
2. Merchant → ChatGPT → User: "Renders options" (ChatGPT lane) → "User selects fulfillment option" (User lane).
3. User → ChatGPT → Merchant: "Calculate sales tax and final price" (Merchant lane).
4. Merchant → ChatGPT → User: "Renders total amount" (ChatGPT lane) → "User confirms with "Pay"" (User lane).
5. User → ChatGPT: "Gathers secure payment token, order and integrity signals" (ChatGPT lane) → Merchant: "Takes order and payment info, accepts or declines order" → Payment Processor: "Charges payment method".
6. Payment Processor → Merchant → ChatGPT → User: green check-mark icon in each of the Merchant, ChatGPT and User lanes (no text).

Legend: none. Footnote / source line on image: none. Figures printed as text: none.

Text cross-check: the source raw file's body carries the same step names in prose ("ChatGPT sends the necessary details to the merchant's backend… The merchant accepts or declines the order, processes the payment via their existing provider"). No figure in the image; nothing to compare. The fee sentence in the text ("Merchants pay a small fee on completed purchases") has no counterpart in the image.
