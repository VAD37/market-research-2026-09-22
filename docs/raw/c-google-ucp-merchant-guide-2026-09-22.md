# Google for Developers — Google Universal Commerce Protocol (UCP) Guide (Merchant Center)

```yaml
source:          Google for Developers (developers.google.com/merchant)
url_or_doc_id:   https://developers.google.com/merchant/ucp
published:       undated — no date on page
pull_date:       2026-09-22
pull_method:     browser extension
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default
source_label:    company-stated
lane:            C
sub_market:      agentic commerce
engine:          Google — AI Mode, Gemini app, Merchant Center
metric_kind:     none
supersedes:      none
captured:        full page including FAQ (FAQ text present in DOM but visually collapsed — extracted via page script reading the FAQ container's textContent, not innerText)
```

## Verbatim

Page title: "Google Universal Commerce Protocol (UCP) Guide | Google for Developers"

Banner: "UCP is expanding to new industries, starting with Lodging and Food" — "Join the waitlist: Lodging | Food"

### Getting started with Universal Commerce Protocol on Google

"The Universal Commerce Protocol (UCP) is an open standard designed for the future of commerce, empowering you to turn AI interactions into instant sales. Adopt UCP to enable agentic actions on AI Mode in Google Search and Gemini, starting with direct buying."

### Why implement UCP on Google?

- "Maintain full control of your brand — You remain the Merchant of Record. Keep all of your customer data and relationships."
- "Ready-made reach — Use your existing Merchant Center account shopping feeds to capture high-intent customers during discovery. UCP unlocks access to users on surfaces like AI Mode in Google Search and Gemini web (app coming soon)."
- "Build shopper confidence at scale — Rely on a system designed for trust. UCP creates a transparent accountability trail between merchants, credential providers, and payment services, helping to ensure each transaction is secure, every time."

### Flexible integration options to meet your needs

- "Native checkout — Integrate checkout logic directly with AI Mode in Google Search and Gemini. This default integration will unlock full agentic potential as UCP product offering expands."
- "Embedded checkout (optional customization) — An additional optional path for specific, approved merchants. Best for those with highly bespoke branding or complex checkout flows that require an iframe-based solution."

### Learn more about Universal Commerce Protocol

"By adopting the Universal Commerce Protocol, you enable seamless, agentic commerce actions across Google's AI surfaces."

- "Explore the standard — Review the open-source interface that standardizes integrations between consumer surfaces and ecosystem players." [links to GitHub]
- "Check the roadmap — See upcoming features like multi-item carts, account linking for loyalty programs, and post-purchase support for tracking and returns."
- "Partner with us — Join the waitlist to become part of an ecosystem of industry leaders adopting the protocol to drive the next generation of commerce."

### Frequently asked questions (verbatim, extracted from DOM)

**Q: What is the Universal Commerce Protocol (UCP)?**
A: "UCP is a new open standard that unifies digital commerce. It enables direct, instant purchases across AI surfaces like AI Mode in Google Search and the Gemini app, reducing friction and cart abandonment."

**Q: What can I expect when I integrate with UCP?**
A: "Expanded reach: Connect with high-intent shoppers directly within Google's AI surfaces, including AI Mode in Google Search and the Gemini app. Reduced checkout friction: Enable direct purchases within the interaction flow to keep users engaged. Control: You remain the Merchant of Record, maintaining full control over your customer relationships and data. Flexibility: Choose between different integration paths (Native and Embedded) to suit your brand and technical stack. Readiness for agentic experiences: Use core features like multi-item carts and account linking designed to support upcoming agentic capabilities. Compatibility across the ecosystem: Benefit from a protocol that is interoperable with major industry standards (Agent Payments Protocol (AP2), Agent2Agent (A2A) and Model Context Protocol (MCP)) and built to handle the full end-to-end shopping journey."

**Q: Will I lose control of my customer data?**
A: "No. You remain the Merchant of Record for all transactions. You retain full ownership of your customer relationships, data, and the post-purchase experience. Our standard security and privacy practices apply to the interaction, but you own the transaction."

**Q: What makes UCP different?**
A: "Modular and extensible: UCP is designed to be modular and extensible to support rich commerce experiences using capabilities and extensions. Fast and easy to implement: UCP allows merchants the choice to select the set of capabilities & extensions they want to support and the communication medium that best suits their development needs such as APIs, MCP or A2A. Co-designed with industry leaders: UCP is open source and is designed directly by a collaboration of industry leaders, to support the diverse needs of a rich commerce ecosystem. Secure and seamless payments: UCP supports secure payments using tokenization and allows merchants to use existing payment integrations using payment handlers."

**Q: Is it compatible with my tech stack?**
A: "UCP is fully compatible with protocols such as AP2, A2A, and MCP. It supports transport REST API and MCP binding. We provide adapters to ensure compliance if you are using other protocols. UCP primitives map 1:1 to standard retail operations such as checkout. UCP was designed in collaboration with industry leaders to ensure a low-lift integration that aligns with your existing business logic. We have also deployed native SDKs for better language bindings, allowing you to integrate UCP faster within your existing development environment."

## Pull notes — mechanical only

- Loaded via Chrome extension. FAQ content is present in the DOM (`.ucp-faq-inner`, 5,063 characters of `textContent`) but not exposed by `get_page_text` (which follows rendered/visible text and returned only the six question headers with no answers, same collapsed-accordion behavior seen on `support.google.com`). Answer text was recovered with a page script (`javascript_tool`) reading `textContent` (which ignores CSS visibility) on the FAQ container, in slices to fit output limits; reassembled here in original order. No wording altered — only whitespace collapsed.
- No visible "last updated" date on the page.
- Ready-made-reach bullet states UCP "Use[s] your existing Merchant Center account shopping feeds" — this page names no specific new/required Merchant Center feed attribute (contrast: `c-google-ucp-merchant-agentic-2026-09-22.md`, which names "dozens of new data attributes in Merchant Center" without listing them). Neither company page pulled in this cluster lists the individual attribute names; a dedicated Merchant Center attribute-reference page was not located under this cluster's pull list and is recorded as `unknown — checked developers.google.com/merchant, support.google.com/merchants 2026-09-22` — see summary file.
- No pricing, fee, or take-rate language anywhere on this page for UCP integration.
- Geography: no country list stated on this page. `c-google-ucp-merchant-agentic-2026-09-22.md` (2026-01-11) states checkout launches for "eligible U.S. retailers" with globally expansion "in the coming months" — this page does not repeat or update that scope.
