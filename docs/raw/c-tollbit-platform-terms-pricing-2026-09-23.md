# TollBit — platform terms, rate model, network size (site, docs, Publisher Platform Agreement)

```yaml
source:          TollBit (Novoscribe, Inc.) — tollbit.com, docs.tollbit.com
url_or_doc_id:   https://tollbit.com/ ; https://tollbit.com/network ; https://docs.tollbit.com/docs/setting-rates.md ; https://tollbit.com/legal/publisher-platform-agreement ; https://tollbit.com/press ; https://tollbit.com/state-of-the-bots
published:       docs "Enabling Monetization" updatedAt 2026-06-25; Publisher Platform Agreement "Last Updated October 29, 2025"; site pages undated (© 2026)
pull_date:       2026-09-23
pull_method:     fetch (curl, User-Agent "market-research-bot contact: research@example.invalid"; HTML tag-stripped; docs pulled as the site's own .md variant)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary, own docs and terms; the "Over 10,000 sites" count is vendor-reported with no method
source_label:    vendor-reported
lane:            C
sub_market:      n/a — publisher / sell-side monetisation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        homepage product list and logo carousel; network page count line; docs "Enabling Monetization" full; Publisher Platform Agreement §Content License Agreements and §Additional Service Fees; press page item titles 2025-09 to 2026-03; State of the Bots page shell
```

## Verbatim

### tollbit.com (homepage)

> TollBit - Your complete web stack for the agentic internet
> Products: Licensed RAG access · Bot & agent paywall · Content controls · Agent Site · MCP · NLWeb · Portfolio analytics · TollBit Analytics
> Solutions: Digital Publishers · Agentic commerce
> Resources: Platform Docs · API & Integrations Docs · Scraper Index · Bot Index · State of the Bots Q2 2025 · State of the Bots Q1 2025 · State of the Bots Q4 2024
> Unified solution for the AI-powered web. Your complete web stack for the agentic internet. Future-proof your content for any AI protocol with TollBit. Control access, analyze traffic, and monetize as the agent economy grows.
> Get started free · Book a demo
> Compliance — Licensed RAG access: License content for AI retrieval. Bot & agent paywall: Custom pricing for AI access. Content controls: Filter what agents can access.
> Logo carousel (domains as printed): reuters.com, huffpost.com, jpost.com, firstpost.com, invezz.com, futurism.com, pagesix.com, motorsport.com, harpersbazaar.com, timeanddate.com, economist.com, goldderby.com, timesnownews.com, heavy.com, watchuseek.com, apnews.com, buzzfeed.com, scmp.com, outlookindia.com, coinjournal.net, ign.com, empireonline.com, si.com, townandcountrymag.com, rockpapershotgun.com, mirror.co.uk, delish.com, trustedreviews.com, the-sun.com, howlongtobeat.com, forbes.com, pbs.org, bangkokpost.com, abplive.com, stocktwits.com, rollingstone.com, tvline.com, healthline.com, womansday.com, nationalpost.com, goodhousekeeping.com, countryliving.com, autosport.com, zeit.de, 1911forum.com, time.com, pewresearch.org, nzz.ch, hindustantimes.com, ted.com, billboard.com, radiotimes.com, webmd.com, popsugar.com, biography.com, zdnet.com, apartmenttherapy.com, bringatrailer.com, heraldsun.com, cardesignnews.com [note: carousel truncated at tool output limit after cardesignnews.com]

### tollbit.com/network

> The bot CDN trusted by leading sites
> Over 10,000 sites, from major brands to niche sites, use TollBit to manage how bots and agents access their content. Want to learn more about the network? Contact us
> [named sites with access-method tags:] USA Today (API, MCP) · AP News (API, MCP) · Newsweek (API, NLWeb, MCP, Direct access) · TIME (API, NLWeb, MCP, Direct access) · HuffPost (API, MCP, Direct access) · Popular Mechanics (API, MCP) · Forbes (API, NLWeb, MCP, Direct access) · Goal (API, MCP) · TED (API, MCP, Direct access, NLWeb)
> Copyright © 2026 Novoscribe, Inc. All rights reserved. Long live the programmable web. Made in New York, NY.
> Publisher Platform Agreement · Developer Platform Agreement · Privacy Policy

### docs.tollbit.com — "Enabling Monetization" (updatedAt: 2026-06-25T16:00:33.000Z)

> Introduction to rate types and how to activate them on TollBit
> At the moment there are a few ways to set rates. You can set global rates which apply to all your content across all subdirectories and pages. To enable rates, you must assign them to a license.
> # Licenses
> There are three types of licenses:
> 1. **Summarization License** - Allows AI customers to access your content to create a summary, grounding, or citation with a single use license. Simply, set your rate per 1000 pages accessed and click activate and allow AI customers interested to view rates and pay for your content, you can consider [truncated at 300 characters in this pull]
> 2. **Full Display License** - Allows AI customers to display the complete text of an article once. Set your rate per 1000 pages accessed and click activate to begin generating revenue, you can consider your syndication rates as a benchmark when determining this rate.
> 3. **Custom License** - For any partners that you have struck deal with, you can upload a custom license to the user agents of that specific partner. Any requests made to TollBit with that partner's user agents will include the license that you uploaded in the transactions.
> Within both types of licenses you can also set custom rates according to the following hierarchy: `bot` -> `page` -> `keyword` -> `time` -> `subdirectories`.
> TollBit doesn't take a percentage of your rates or revenue share. We simply charge AI customers a small transaction fee on top of the rates you set. Your payments reflect your rates completely; if you set a rate of $0.001 per page, AI customers will pay that and you will receive that amount complete [truncated at 300 characters in this pull]
> ## Types of Rates — Bot Rates [...] Directory / Page Rates [...] Keyword Rates: [...] This rate is still in beta.
> When activating rates, you are agreeing to the standard license terms. These license terms will apply each time an AI company uses your content.
> Pro Tip: When you first onboard onto the platform, your rates will *not* be active and demand side users will not be able to fetch your content through TollBit.
> ## Transactions — This page provides an audit trail where you can see all the requests that have been made to your website through TollBit. For each request, you are able to see the user agent that made the request, the page they hit, and the price they paid for that page.

### docs.tollbit.com — Getting Started (Content Owners)

> TollBit allows you to quickly set up an Agent Site, separate from your existing website, in as little as 15 minutes with no coding. This effectively puts your data behind an API and/or Markdown, and allows you to immediately start charging bots or allowing them optimized content for on demand access.
> Integrations listed: General Route, Akamai, Arc XP, AWS (S3, CloudFront, ALB), CloudFlare, Datadome, Fastly, Google (GCP, CDN), Microsoft (Azure, Front Door), Vercel, WordPress VIP, Imperva.
> Developers: Introduction · Quickstart · Developer Dashboard Overview · Response Formatting · Licensed Search · Search to Content Workflow · Tokens · Rates · Content · Webhooks

### Publisher Platform Agreement (Last Updated October 29, 2025)

> Content License Agreements. Using the TollBit Platform, you may enter into agreements ("Content License Agreements") with purchasers ("Developers") to monetize and use the content, data, and information (collectively, "Publisher Data") that you have made available via the TollBit Platform. You will be able to set the specific fees associated with the Publisher Data using the TollBit Platform in your Tollbit Platform account portal. You agree and acknowledge that each Content License Agreement is an agreement solely between you and the applicable Developer. TollBit is not a party to any Content License Agreement and TollBit does not license content to the Developer or guarantee Publisher Data will be monetized. [...] TollBit has no control over and does not guarantee that Developers will actually pay amounts owed for the Publisher Data or use the Publisher Data in compliance with any applicable Content License Agreement.
> Additional Service Fees; Taxes. From time to time, TollBit may make additional services available to you via the TollBit Platform. If you elect to use such services, you will pay the fees set in your account portal, if any, without offset or deduction. You shall make all payments hereunder in US dollars [...]

### tollbit.com/press — item titles (selection, as printed)

> March 12, 2026 — DPCMO — "DPCMO Partners with TollBit to Offer Solutions to Support its Members"
> February 5, 2026 — WIRED — "AI Bots Are Now a Significant Source of Web Traffic"
> February 5, 2026 — The Media Copilot — "'The pipes are leaky': New report shows AI scrapers bypassing publisher protections at scale"
> February 5, 2026 — TechBuzz — "AI Bots Now Drive 2% of Web Traffic as Publishers Fight Back"
> December 22, 2025 — PR Newswire — "TNL Mediagene Announces Early Success in AI Content Licensing Revenue Model via TollBit Marketplace Integration and Strategic Partnership"
> September 29, 2025 — Business Wire — "VerticalScope Taps TollBit to Unlock AI License Revenue and Protect Community Content"
> September 16, 2025 — EIN Presswire — "Nota News Launches with Microsoft and TollBit to Restore Local Journalism and Expand Civic Access"
> September 6, 2025 — Axios — "AI marketplaces multiply to scale publisher deals"
> July 29, 2025 — Yahoo Finance — "DataDome Brings Real-Time Control & Monetization Of AI Agents in New Partnership with TollBit at Black Hat USA 2025"
> June 20, 2025 — Yahoo Finance (video) — "How this startup is helping publishers profit from AI scraping"

### tollbit.com/state-of-the-bots

> Issues listed: "2026 Q1 & Q2, The Bad Bots" · "2025 Q3 & Q4, The Leaky Pipes" · "2025 Q2, Good Net Citizens" · "2025 Q1, The Rise of RAG Bots" · "2024 Q4, The First Issue"
> Section 1: The Scraper Ecosystem & Proxy Networks · Section 2: The Scale of AI Scraping · Section 3: Referral Traffic · Section 4: Robots.txt and the Bypassing Problem
> [note: report body is script-rendered; no figures captured by fetch]

## Pull notes — mechanical only

- `tollbit.com/pricing`, `/faq`, `/solutions/digital-publishers`, `/products/licensed-rag-access` returned HTTP 404; the FAQ and product content sits under different paths not discovered from the nav.
- No publisher-side price list, no rate benchmark, no transaction-fee amount for AI customers, no publisher payout figure and no revenue figure appears on any page captured. The rate model is per-1,000-pages set by the publisher.
- The docs `setting-rates.md` lines were cut at 300 characters by the pull command; marked inline.
- State of the Bots report bodies render by script; not captured.
