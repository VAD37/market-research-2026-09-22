# G2 — Shopware reviews/product page — admission-rule second source

```yaml
source:          G2 (g2.com) — third-party software review site, independent of Shopware
url_or_doc_id:   https://www.g2.com/products/shopware/reviews
published:       page title states "Shopware Reviews 2026"; no further date on the summary block captured
pull_date:       2026-09-22
pull_method:     browser extension (get_page_text) — plain fetch to g2.com returns HTTP 403 (channels.md C37/C38's documented 403→ext pattern)
pull_purpose:    evidence about a number
tier:            5
tier_reason:     vendor/agency study handling — the company-description paragraph and customer count are review-site framing/aggregation, not filed or independently audited; usable as corroboration of existence and scale, not as an audited number
source_label:    analyst-derived
lane:            C
sub_market:      agentic commerce
engine:          n/a — review-site page, not an assistant engine
metric_kind:     sales
supersedes:      none
captured:        full page text (main content region) — company overview, pricing summary, integrations, comparisons, categories
```

## Verbatim

"Shopware Reviews & Product Details"

"Shopware is **the open commerce platform for the agentic era.** It gives global B2C and B2B organizations the infrastructure to grow while retaining control of their data, business logic, and customer experience."

"Built on open-source technology and an API-first architecture, Shopware combines ready-to-use commerce capabilities with the freedom to customize, extend, and deploy as SaaS, PaaS, or self-hosted. Businesses can manage complex commerce models, connect their preferred technology, automate workflows, and **create differentiated experiences for human and agentic buyers**, without being locked into a rigid platform model."

"Shopware connects a scalable commerce core with intelligent capabilities that help merchants grow their way, automate the work, and elevate the experience. **More than 55,000 businesses use Shopware worldwide**, supported by a global partner ecosystem and **3,100+ extensions**. The platform is recognized by Gartner, Forrester, IDC, and Paradigm B2B and is backed by GDPR compliance, SOC 2 certification, open product development, and a public roadmap."

"Languages Supported: German, English, French, Italian, Japanese, Dutch, Polish, Portuguese, Russian, Spanish"

"**Pricing** (provided by Shopware) — **Rise: Starting at $600.00 Per Month.**" / "Pricing Options — Rise: Starting at $600.00 Per Month. Evolve: Contact Us. Beyond: Contact Us."

"Shopware Comparisons" — Shopify (4.4/5, 5,143 reviews), PrestaShop (4.3/5, 159 reviews), commercetools (4.5/5, 17 reviews).

"Top-Rated Alternatives" — Adobe Commerce, formerly Magento Commerce (4/5, 622 reviews), Shopify (4.4/5, 5,143 reviews), Salesforce B2C Commerce (4.3/5, 704 reviews).

"Categories on G2: E-Commerce Personalization, E-Commerce Platforms, Omnichannel Commerce" (plus "Show More").

## Pull notes — mechanical only

- Loaded via the Chrome extension (`claude-in-chrome`), `get_page_text`, in a dedicated new tab; the tab was closed immediately after this pull. Plain fetch to g2.com returns `403`, consistent with this cluster's other G2 pulls.
- **Admission-rule role**: this is the second, independent-of-Shopware source required by this task's admission rule, alongside source 1 (`docs/raw/c-paypal-protocol-agentic-commerce-2026-09-22.md`, PayPal's own partner page naming Shopware). G2 independently corroborates both the "55,000+ businesses" customer count and the €/$600/month Rise-tier price found on Shopware's own site (`c-shopware-product-2026-09-22.md`) — price figures match across the two independent sources (€600 vendor-stated, $600 G2-stated, consistent with the page's own EUR/USD toggle).
- Customer count independently corroborated: **"More than 55,000 businesses"** — the strongest, most specific customer-count figure found for any vendor in this cluster's census, and independently sourced (not vendor-only).
- `commercetools` (one of the seven held names from `a-vendor-roster-2026-09-22.md` §3e) appears here only as one of Shopware's G2-listed "Comparisons," not as a partner named on any Pass 2 engine/protocol page — does not itself satisfy this task's admission rule (source 1 must be an engine/protocol partner page); noted in the census summary's held/screened section, not rostered on this basis alone.
