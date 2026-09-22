# Criteo — Homepage banner and Criteo GO product/features pages (ChatGPT ad access)

```yaml
source:          Criteo (criteo.com)
url_or_doc_id:   https://www.criteo.com/ ; https://www.criteo.com/blog/introducing-agentic-audiences/ ; https://www.criteo.com/go/ ; https://www.criteo.com/go/features/
published:       homepage lastmod 2026-05-05T14:34:01Z; "Introducing Agentic Audiences" blog post dated December 10, 2025, "Updated on February 23, 2026"; /go/ lastmod 2026-09-10T10:46:06Z; /go/features/ lastmod 2026-09-08T12:55:01Z — all per criteo.com/*-sitemap.xml
pull_date:       2026-09-22
pull_method:     fetch (mcp fetch tool, plain HTTP, no browser needed)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform/vendor primary, own homepage and product pages
source_label:    vendor-reported
lane:            B
sub_market:      paid placement
engine:          ChatGPT — OpenAI (named directly on Criteo's own homepage banner)
metric_kind:     none
supersedes:      none
captured:        homepage banner text; blog post headline/dek and table-of-contents section headers; /go/ and /go/features/ page excerpts (testimonials, FAQ, feature list)
```

## Verbatim

### criteo.com homepage banner

"Meet Criteo GO: now with access to emerging advertising opportunities inside **ChatGPT**. Learn more" — linked to the blog post below.

Homepage headline: "The Global Commerce Intelligence Platform — AI full-funnel ads reach 2B shoppers beyond search & social, powered by $1T purchase data."

### criteo.com/blog/introducing-agentic-audiences/ (Commerce AI category, December 10, 2025, "Updated on February 23, 2026")

"# Introducing Agentic Audiences — There's a better way to do audience planning. See how Agentic Audiences make audience building smarter, faster, and more streamlined with AI."

Table of contents: "1. Bridging the gap between guessing and knowing; 2. Meet the AI that thinks like a shopper; 3. For the performance marketer: Audience Agent; 4. For agency buyers and curators: Audience Planner; 5. No grunt work. No guesswork. Just great work."

Opening body text: "It's time to talk about the elephant in the room. In marketing and media planning, we all have a 'process'... You stare at a brief that's asking for 'eco-conscious millennials who love hiking', then you glance across as a drop-down menu populated with either Sports Enthusiasts or Green Living."

[note: page body beyond the opening section (the Audience Agent/Audience Planner product detail and any explicit ChatGPT-integration paragraph) could not be captured — a repeated `mcp fetch` call at start_index 10000 returned a transient connection error on this domain (`Failed to fetch robots.txt https://www.criteo.com/robots.txt due to a connection issue`), not retried further in this pull; the homepage banner's own text is the load-bearing ChatGPT-naming quote captured for this file]

### criteo.com/go/ (Criteo GO — self-serve performance advertising)

"Launch campaigns in only 5 clicks — Free, no registration required"

"Real-world performance, proven by GO — The numbers say it all—real campaigns, real results, no hassle." Named case quotes: "+45% Total Sales" — Hedy Huang, Unice; "+50% Increase Revenue" — Duygu Uysal Gülnar, Inbound for Derimond; "+175% Total Click-Through Rate" — Oscar Nativí, Grupo Farsimán.

"Get up to $1500 in free ad credit" (terms apply).

### criteo.com/go/features/

Feature list (verbatim fragments): "Content generation — Let AI help you write engaging headlines for social ads"; "Reporting... Attribution models... Report customization... Placements report... Real-time data... Downloadable reports... User behavior"; "Optimization — GO uses AI to continuously optimize targeting, bidding, and creative to maximize performance across channels"; "Automated campaign recommendations — Available via Advisor, your AI-powered assistant"; "Account Management... User profiles... SSO Login... Billing center... Budget type"; "Support... Knowledge base... Live Chat... Language support — English."

"Where ambitious brands grow — These are the numbers and the stories that show why **thousands of brands** choose Criteo GO." Named case quotes: "+45% Total sales" — Hedy Huang, Unice; "+107% Increase in ROAS" — Łukasz Mirkowski, Denon Store by Audio Forum; "+32% Total Revenue" — Paulo Cantalice, Netshoes.

FAQ, verbatim: "**What is Criteo GO's pricing model?** GO campaigns run on automated budget models using **CPM pricing**, making it easy to optimize spend and performance."

FAQ, verbatim: "**How easy is it get started with Criteo GO?** Launching your first performance campaign with Criteo includes a few steps to import your product catalog (product feed), check that the Criteo OneTag is running on your website, and build your first ad set."

## Pull notes — mechanical only

- Fetched via plain HTTP fetch tool, no browser needed; all pages loaded on first or second attempt except one transient connection error on the blog post's deeper content (see `[note:]` above).
- **Admission-rule role**: this vendor is named as an OpenAI "technology partner" on `docs/raw/b-openai-new-ways-buy-ads-2026-09-22.md` (source 1, already landed under P2-c3) — "We've also added technology partners such as Adobe, Criteo, Kargo, Pacvue, and StackAdapt." Source 2 (independent): `b-criteo-second-source-2026-09-22.md`, this cluster, a StockTitan financial-news aggregator page confirming Criteo S.A. (NASDAQ: CRTO) is a publicly reporting company. Admitted under limb (a).
- Homepage banner is this pull's clearest first-party statement that Criteo's self-serve product (Criteo GO) has "access to emerging advertising opportunities inside ChatGPT" — directly on-topic for this cluster's "AI-ad management tool" target category and independently corroborates the OpenAI partner-page naming.
- No CPC/CPM dollar rate card found on either `/go/` or `/go/features/`; billing model disclosed as CPM. Recorded per task instructions: dollar figure `unknown — checked criteo.com/go/, criteo.com/go/features/ 2026-09-22`.
