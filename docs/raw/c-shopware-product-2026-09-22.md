# Shopware — Homepage ("Agentic by design") and pricing page

```yaml
source:          Shopware (shopware.com)
url_or_doc_id:   https://www.shopware.com/en/ ; https://www.shopware.com/en/pricing/
published:       homepage lastmod 2026-09-09T08:36:23Z per shopware.com/en/sitemap.xml; pricing page undated on page
pull_date:       2026-09-22
pull_method:     fetch (mcp fetch tool, plain HTTP, no browser needed)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform/vendor primary, own homepage and pricing page
source_label:    vendor-reported
lane:            C
sub_market:      agentic commerce
engine:          n/a — cross-engine "generative commerce discovery" and "agentic" framing, no single named engine on this page
metric_kind:     none
supersedes:      none
captured:        homepage excerpt (hero, feature blurbs, customer-metric fragments); pricing page excerpt (plan tiers, Shopware Intelligence+ add-on) — both truncated by tool output limit past the captured sections
```

## Verbatim

### shopware.com/en/ (homepage)

"The ecommerce platform to power your online business | Shopware"

"# Open commerce. Full control. **Agentic by design.** Shopware unites enterprise B2B features, modular flexibility, open-source freedom, and agentic intelligence – all built to scale with your business. Build fast and grow with an integrated CMS, SEO, Analytics, and more."

"4.2 — 180+ reviews"

"### Agentic intelligence built in. Shopware Intelligence – Copilot understands your business requirements, responds quickly, and allows you and your team to focus on what matters most."

"### Open Source, extensible platform. Puts your team in the driver's seat, giving them complete control over your technology, your data, and your future."

"### Unified CMS, SEO, GEO and Analytics. **Win visibility across every discovery channel and own the future of generative commerce discovery.**"

Customer-metric fragments (concatenated on the page, individual case attributions not separable from this fetch): "handles 350 product categories... increase ecommerce revenue by 150x and centralized 200,000 products... launched a central customer portal... now handles 60m auto-updating prices... attracted 10,000 new customers and generated €10m in revenue... increase orders by 53%... centralized 400 dealers... uses auto-updating on 16m prices... improved time-to-market... attracted 60,000 omnichannel loyalty members... reached customers in 65 countries... increased visibility by 15%... increased visibility by 700%... automated processes and created an engaging hybrid store for B2C and B2B... handles up to 4k orders per minute... adopted 3D product views to increase interactions by 400%... increased efficiency by 25%." Verticals named: "Industrial & Manufacturing, Wholesale & Distribution, Automotive, Consumer Goods (FMCG), Home, Living & DIY, Retail."

"Enterprise-grade security and compliance peace of mind. Data is encrypted in transit and rest, with support for SOC 2, ISO 27001, and GDPR compliance." SOC-2 and GDPR sub-sections confirmed.

### shopware.com/en/pricing/ (Plans & Pricing)

"Built for ambitious, complex commerce. Performance, agentic commerce intelligence, and enterprise-grade security – fused into one powerful commerce platform backed by first-class support." Prices toggle: "Prices in € Euro (€) / US Dollar ($)."

Plan tiers, verbatim:
- "**Community Edition** — Explore the open-source commerce platform, backed by our global community. **Free, € 0.** Highlights: Open-source core, Modular architecture, Global developer community, Community events."
- "**Rise** (Our bestseller) — For growing businesses ready to scale. Unlock unlimited Sales Channels, and Agentic Commerce capabilities. **From € 600/month, excl. VAT.** Highlights: Shopware Intelligence, 3D capabilities, Unlimited sales channels. Basic Support: 8 hours service reaction time."
- "**Evolve** — For ambitious brands expanding into B2B and B2C. Designed to handle complexity and drive long-term growth. **From € 2,400/month, excl. VAT.** Everything from Rise, plus: B2B Components, Advanced Search, Dynamic Access. Enhanced Support: 4 hours service reaction time, Phone support."
- "**Beyond** — For businesses seeking advanced commerce capabilities, robust compliance, and dedicated 24/7 support. **Custom.** Everything from Evolve, plus: Digital Sales Rooms, Multi-Inventory, Customer-specific pricing, Subscriptions. Advanced 24/7 priority support: 1 hour service reaction time, Personal account manager, Personal onboarding."

Add-on: "**Unlock the full power of Shopware Intelligence** — Unlock Services with Shopware Intelligence+ and get full access to powerful AI tools, and future agentic services. Full access. Zero limits." — "Shopware Intelligence+ for Shopware Community Edition: **€ 29/month, excl. VAT.** Unlimited usage of Copilot – Agentic, Copilot – Data Insights, 3D Preview Generator, CAD to 3D." — "Shopware Intelligence+ for Shopware Rise, Evolve and Beyond: **€ 19/month, excl. VAT.** Unlimited usage of Copilot – Agentic, Copilot – Data Insights, 3D Preview Generator, CAD to 3D."

## Pull notes — mechanical only

- Fetched via plain HTTP fetch tool, no browser needed; both pages loaded on first attempt, content truncated by tool max_length past the captured sections (homepage cut off at the security/compliance section; pricing page cut off mid-"Compare Plans" table).
- **Full dollar/euro pricing disclosed at tier 3** — one of the few vendors in this cluster's census with a genuine public rate card: Community Edition free; Rise from €600/month; Evolve from €2,400/month; Beyond custom; plus a separate "Shopware Intelligence+" AI add-on at €29/month (Community) or €19/month (Rise/Evolve/Beyond). No dollar-figure `unknown` needed for this vendor.
- No dedicated "ChatGPT" or single-named-engine page found — a guessed URL (`shopware.com/en/features/generative-engine-optimization/`) 404'd. The homepage's own "Unified CMS, SEO, GEO and Analytics" section is the closest AI-surface-specific product statement found on Shopware's own domain within this pull's budget; recorded as such. `unknown — checked shopware.com/en/features/generative-engine-optimization/ (404), shopware.com/en/ 2026-09-22, no single-engine-named page found`.
- **Admission-rule role**: this vendor is named on PayPal's own partner page (`docs/raw/c-paypal-protocol-agentic-commerce-2026-09-22.md`, already landed — "Connect your product listings to PayPal's partners like Wix, Cymbio, Commerce (BigCommerce & Feedonomics), and **Shopware**"), source 1. Source 2 (independent): `c-shopware-second-source-2026-09-22.md`, this cluster, a G2 review-site page. Admitted under limb (a).
- Customer-count fragments on the homepage are individual case-study metrics run together by the fetch tool's markdown simplification (no clean separation between cases); none names a date window, baseline, sample size, or named measurer, so none clears the seven-item bar — screened, not individually pulled, per this task's instruction. The aggregate customer count ("55,000+ businesses") comes instead from the independent G2 page, see `c-shopware-second-source-2026-09-22.md`.
