# Anthropic Help Center — How Claude suggests connected apps (no paid placement)

```yaml
source:          Claude Help Center (support.claude.com)
url_or_doc_id:   https://support.claude.com/en/articles/14730684-how-claude-suggests-connected-apps
published:       undated — no visible revision date on page
pull_date:       2026-09-22
pull_method:     browser extension
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary, consumer-facing help article
source_label:    company-stated
lane:            A
sub_market:      organic recommendation
engine:          Claude — Anthropic (no model version named)
metric_kind:     none
supersedes:      none
captured:        full page
```

## Verbatim

Title: "How Claude suggests connected apps | Claude Help Center"

"When you connect an app like Spotify or Instacart to Claude, you don't have to ask for it by name every time. Claude can bring up a connected app on its own when it fits what you're doing. This article covers when that happens, how Claude picks between apps, and how you stay in control.

Connected apps are available on Claude, Claude Desktop, and Claude for iOS/Android. Installing an app on mobile is currently in beta."

**When Claude suggests an app**

"Claude pays attention to what you're asking about in the conversation. When a connected app matches that context, Claude suggests it in the thread without you having to name it.

For example, if you've connected AllTrails and ask about a weekend hike, Claude can pull up trails nearby. If you've connected Instacart and ask for help putting together a dinner, Claude can start building a cart.

Claude also uses context you've shared in earlier conversations—through memory—to make the suggestion more relevant. If you've told Claude you have a dog, a trail search can filter for dog-friendly options by default."

**Stay in control**

"Before Claude books, buys, or reserves something on your behalf, it checks with you first. For connected apps with a booking or purchase flow, you confirm the details before anything is finalized. Claude doesn't transact on its own.

Connecting an app gives Claude access on your behalf. Your data from that app isn't used to train Claude's models, and the connected app can't see your other conversations. You can disconnect at any time."

**When more than one app could help**

"Sometimes more than one of your connected apps can handle what you're asking for. If you have both Booking.com and TripAdvisor connected and ask for help planning a trip, Claude shows both and lets you pick. Claude doesn't silently default to one over the other; you choose which app to use, and Claude proceeds from there."

**No paid placements**

"Claude doesn't take payment to recommend any connected app. There are no sponsored rankings, no paid placements, and no advertising. When Claude brings up an app, it's because the app matches what you're asking for.

When more than one app could help, the order you see them in reflects what's likely useful to you, not partnership arrangements."

**Turn off suggestions or disconnect an app**

"You control which of your connected apps Claude can bring into a conversation.

Disable an app for one conversation: Click the "+" in the lower left of the chat, hover over Connectors, and toggle the app off. Claude won't use it for that conversation.

Disconnect an app entirely: Go to Customize > Connectors, find the app, and disconnect it. Claude stops accessing it immediately.

For more on managing connected apps, see Use connectors to extend Claude's capabilities."

## Pull notes — mechanical only

- Loaded via Chrome extension `get_page_text` on `support.claude.com`; full `<article>` captured, no login gate, no accordion.
- This is the most explicit, company-stated, existence-answering sentence found in this cluster on whether Claude's app/product recommendations are commercially influenced: "Claude doesn't take payment to recommend any connected app. There are no sponsored rankings, no paid placements, and no advertising." Directly on-point for `hypotheses.md` HE2 (organic recommendation) and the query-book's B x Claude absence check, though sourced from the Help Center rather than a news post.
- No visible "last updated" date on the article; not flagged stale since platform primary is exempt from the recency filter per `query-book.md`.
- Article is about Claude's Connectors feature (third-party app integrations like Spotify, Instacart, AllTrails, Booking.com, TripAdvisor) recommending which *app* to invoke, not about brand/product recommendation inside a generated answer in the glossary's strict sense — recorded as the closest primary-source statement found, not conflated with the glossary's "recommendation" sub-metric (brand named as an answer to a buying-shaped prompt).
