# Cloudflare — Pay Per Crawl developer docs (price floor, billing lifecycle, beta status)

```yaml
source:          Cloudflare Docs (developers.cloudflare.com), AI Crawl Control product documentation; plus Cloudflare Blog launch post
url_or_doc_id:   https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl/ ; .../faq/ ; .../use-pay-per-crawl-as-site-owner/set-a-pay-per-crawl-price/ ; .../use-pay-per-crawl-as-site-owner/manage-payouts/ ; https://blog.cloudflare.com/introducing-pay-per-crawl/
published:       docs "Last updated Jul 28, 2026" (what-is, set-price), "Last updated Apr 23, 2026" (FAQ, manage-payouts); blog 2025-07-01
pull_date:       2026-09-23
pull_method:     fetch (curl, User-Agent "market-research-bot contact: research@example.invalid"; docs pulled as the site's own "View as Markdown" index.md variants; blog HTML tag-stripped)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary, own docs
source_label:    vendor-reported
lane:            C
sub_market:      n/a — publisher / sell-side monetisation (feeds organic recommendation value chain)
engine:          n/a
metric_kind:     none (price floor only)
supersedes:      none — first pull of the docs; the blog was previously referenced only by tag in raw/a-cloudflare-crawl-refer-ratio-blog-2026-09-22.md
captured:        four docs pages full main text; blog launch post — sentences on beta status, price model and merchant-of-record only
```

## Verbatim

### Page: What is Pay Per Crawl? (Last updated Jul 28, 2026)

> Pay per crawl beta
> Pay per crawl is currently in closed beta.
> To find out how to join the beta program, reach out to us at Pay per crawl signup ↗ (https://www.cloudflare.com/paypercrawl-signup/), or contact your account executive if you are an existing Enterprise customer.

> AI crawlers often consume vast amounts of web content. Some provide mutual benefit to content owners by indexing content for search engines, but others engage in activities such as content scraping without permission.
> The resulting landscape leaves content owners with limited options for managing AI crawlers or receiving compensation for automated access to their intellectual property.

> ## What is Pay Per Crawl?
> Pay per crawl is a feature of AI Crawl Control that enables site owners to control and monetize AI crawler access to content by setting a price per zone.
> Each time an AI crawler requests content, they either present payment intent via request headers for successful `HTTP 200` access, or receive an `HTTP 402 Payment Required` response with pricing. Cloudflare acts as the Merchant of Record for pay per crawl and also provides the underlying technical infrastructure.

> Note
> If you block an AI crawler from a zone via either of Cloudflare's WAF or Bot Management products, those products' rulesets will override pay per crawl's "charge" feature, and the blocked crawler will not have access to the zone.

> Ultimately, pay per crawl enables:
> - Site owners to take control of their content, and charge a fee every time an AI crawler accesses a page in their Cloudflare zone.
> - AI crawler owners to pay to access content on sites protected by pay per crawl.

[image: docs/raw/img/c-cloudflare-pay-per-crawl-docs-2026-09-23/01-pay-per-crawl-components.png] — alt text on page: "Pay per crawl components" (component diagram; no figures).

### Page: Pay Per Crawl FAQ (Last updated Apr 23, 2026)

> ## Frequently asked questions for site owners
> ### Can I set different prices for different AI crawlers?
> No. Pay per crawl allows you to configure different actions (Block, Charge, or Allow) for each crawler, but you can only set a single price that applies to all crawlers configured with the "Charge" option.

> ## Frequently asked questions for AI bot operators
> ### Will I be charged for re-crawling the same page?
> Yes. Every time your AI crawler accesses content on a website protected with pay per crawl, it will incur the cost set by the site owner. You should implement mechanisms within your crawler to track expenditure and enforce any spending limits you want to set.
> Some paths are always free to crawl. These paths are: `/robots.txt`, `/sitemap.xml`, `/security.txt`, `/.well-known/security.txt`, `/crawlers.json`.
> ### Am I charged for error responses?
> No. Charging events are only triggered for successful HTTP response codes. Error responses are not billed, even if you have sent the `crawler-exact-price` or `crawler-max-price` headers.
> ### What user agent should I use?
> Use the standard user agents associated with your AI crawler that you have onboarded to Cloudflare and identified through Web Bot Auth.

### Page: Set a pay per crawl price (Last updated Jul 28, 2026)

> Once your domain's visibility is set to **Visible** in Account Settings, you can set a pay per crawl price and enable pay per crawl for that domain.
> 1. Go to **AI Crawl Control**.
> 2. Go to the **Payments** tab.
> 3. In the **Pay Per Crawl** card, select **Enable**.
> 4. Set your default per crawl price. This is the amount charged for each successful content retrieval (HTTP 200 response) by an AI crawler.
>    - (Optional) To set different prices for different content, select **Enable dynamic pricing**. Refer to Advanced configuration for details.
> 5. Select **Save**.
> After enabling and setting a price, the domain's status in Account Settings will change to **Enabled**.
> Pricing considerations
> The minimum price is $0.001 USD per crawl. Consider your content value and expected crawler volume when setting your price.

### Page: Manage payouts (Last updated Apr 23, 2026)

> When you're ready to receive payments for your accrued crawler activity, connect your Cloudflare account to Stripe. This step can be completed at any time after enabling pay per crawl.
> ## Create a new Stripe account
> A person with **Administrator** or **Super Administrator** access must set up the Stripe connection: [...] 5. Complete Stripe's onboarding process, including: Basic business information; Bank account details for payouts
> Pay Per Crawl Stripe account required
> You must create a dedicated Cloudflare Stripe Connect account through the dashboard. Pre-existing Stripe accounts are not compatible with this feature.
> ## Billing lifecycle
> Cloudflare manages the complete billing lifecycle:
> 1. **Charge initiation**: AI crawlers indicate payment intent via request headers
> 2. **Charge recording**: A charge event is recorded upon successful content delivery (HTTP 200 response)
> 3. **Aggregation**: Cloudflare aggregates and reconciles all recorded charges
> 4. **Payout**: Monthly payments to publishers in good standing
> ### Limitations
> - Your accrued balance is not currently visible in the dashboard. You can request balance updates from your Cloudflare team.
> - Payouts are subject to settlement periods and minimum payout thresholds.

### Blog: "Introducing pay per crawl: enabling content owners to charge AI crawlers for access" (2025-07-01) — excerpts

> Many publishers, content creators and website owners currently feel like they have a binary choice — either leave the front door wide open for AI to consume everything they create, or create their own walled garden.
> After hundreds of conversations with news organizations, publishers, and large-scale social media platforms, we heard a consistent desire for a third path: They'd like to allow AI crawlers to access their content, but they'd like to get compensated.
> Pay per crawl, in private beta, is our first experiment in this area.
> Cloudflare acts as the Merchant of Record for pay per crawl and also provides the underlying technical infrastructure.
> They can define a flat, per-request price across their entire site.
> Charge: Require payment at the configured, domain-wide price.
> While publishers currently can define a flat price across their entire site, they retain the flexibility to bypass charges for specific crawlers as needed. This is particularly helpful if you want to allow a certain crawler through for free, or if you want to negotiate and execute a content partnership outside the pay per crawl feature.
> Should a crawler request a paid URL, Cloudflare returns an HTTP 402 Payment Required response, accompanied by a crawler-price header. [...] The crawler can then decide to retry the request, this time including a crawler-exact-price header to indicate agreement to pay the configured price. [...] Alternatively, a crawler can preemptively include a crawler-max-price header in its initial request.
> Pay per crawl is currently in private beta.

## Pull notes — mechanical only

- Docs pages returned HTTP 200 as markdown via the site's own `index.md` variant; the HTML landing page `/features/pay-per-crawl/` renders only the navigation shell to curl (2,541 characters of text).
- No participating-publisher count, no crawler-operator count, no revenue figure and no Cloudflare take-rate appears on any of the four docs pages or the launch post. Cloudflare's Q2 2026 10-Q was checked separately (`raw/b-sec-cloudflare-10q-q2-2026-pay-per-crawl-absent-2026-09-23.md`).
- Diagram image saved via curl from the docs CDN URL (`/_astro/ai-crawl-control-pay-per-crawl-diagram.51Dvd0Od.png`, 2400×1122 PNG); row added to `docs/raw/img/INDEX.csv`.
- Blog post captured only in the sentences quoted; the full 2025-07-01 post is otherwise tagged in `raw/a-cloudflare-crawl-refer-ratio-blog-2026-09-22.md`.
