# OpenAI Developers — Agentic Commerce Protocol (landing page)

```yaml
source:          OpenAI (developers.openai.com)
url_or_doc_id:   https://developers.openai.com/commerce/ (redirects to https://developers.openai.com/commerce)
published:       undated — no date on page
pull_date:       2026-09-22
pull_method:     browser extension
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default (platform primary, publisher/merchant-facing wording)
source_label:    company-stated
lane:            C
sub_market:      agentic commerce
engine:          ChatGPT — OpenAI
metric_kind:     none
supersedes:      none
captured:        full page
```

## Verbatim

Agentic Commerce Protocol

The infrastructure between merchants and shoppers in ChatGPT.

Agentic Commerce Protocol (ACP) is an open standard that serves as the connective layer between merchants and ChatGPT users. It enables ChatGPT to ingest structured catalog data, understand merchant inventory, and surface relevant products in context.

Build with the Agentic Commerce Protocol

Start with the essentials, deepen your understanding, and prepare for production with focused ACP resources.

Get started

Stand up your first ACP integration with a guided walkthrough and sample payloads.

Dive in

Best practices

Improve feed quality with guidance on product copy, variant modeling, and attribution.

Dive in

## Pull notes — mechanical only

- Loaded via Chrome extension. URL requested `https://developers.openai.com/commerce/`; page resolved/rendered at `https://developers.openai.com/commerce` (trailing slash dropped, no explicit redirect notice from the browser, tab title and URL bar both show the no-slash form).
- Landing/index page only — "Get started" and "Best practices" are further linked pages (hrefs not resolved by get_page_text) not pulled in this file. Domain is `developers.openai.com`, part of the OpenAI developer-docs family that `platform.openai.com/docs/bots` redirects into (see `WebFetch` redirect confirmed earlier this pull: `platform.openai.com/docs/bots` → `developers.openai.com/api/docs/bots`), included here as the OpenAI product-feed/merchant-docs target named in the task and in `shortlist.md` P2-c3.
- No pricing, fee, or country information on this landing page.
- Cross-reference: P2-c7 (a separate Pass 2 cluster) owns the Agentic Commerce Protocol spec itself (github.com/agentic-commerce-protocol, docs.stripe.com/agentic-commerce) — this file is filed here only because it is OpenAI's own merchant-facing commerce doc, named in P2-c3's target list ("OpenAI product-feed / merchant docs"), not a duplication of P2-c7's protocol-spec pull.
