# Profound — OpenAI Ads integration page and "Introducing OpenAI Ads nodes for Profound Agents" (2026-05-06)

```yaml
source:          Profound (tryprofound.com)
url_or_doc_id:   https://www.tryprofound.com/integrations/openai-ads ; https://www.tryprofound.com/blog/introducing-openai-ads-nodes-for-profound-agents
published:       integration page undated; blog "6 May, 2026 / Product", authors Garrett Gomez (Manager, Product Marketing), Jack Traina (Product Manager)
pull_date:       2026-09-23
pull_method:     fetch (curl, User-Agent "market-research-bot contact: research@example.invalid"; HTML tag-stripped)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary (vendor's own product pages); the "1.3% versus 29.2%" CTR figures quoted inside the blog are attributed by the author to unnamed "independent estimates" and are not evidence about a number here
source_label:    vendor-reported
lane:            A
sub_market:      paid placement (reporting on ChatGPT Ads inside an organic-visibility tool)
engine:          OpenAI — ChatGPT Ads (ads.openai.com)
metric_kind:     none (integration scope)
supersedes:      none — extends raw/a-profound-method-2026-09-22.md and raw/a-profound-pricing-2026-09-22.md
captured:        integration page main copy full; blog post full main text
```

## Verbatim

### tryprofound.com/integrations/openai-ads

> OpenAI Ads + Profound: Connect OpenAI Ads and Profound to monitor your ChatGPT ads performance
> OpenAI Ads — ads.openai.com — Categories: Ads — Connect
> How it works: Navigate to the Integrations Center in Profound settings and connect your OpenAI Ads account. Once linked, you can read ad campaigns, ad groups, ads, files, and report directly from Profound.
> Key benefits: By integrating Profound with OpenAI Ads, you can automatically report your ChatGPT ads performance by tying in data from organic AI Search performance and running a holistic AEO strategy in one place.
> [site banner:] Series D — Profound raises a $180M in Series D to build your AI Marketer.
> Get your brand mentioned by ChatGPT Perplexity Claude Gemini Microsoft Copilot DeepSeek Google AI Overviews

### Blog — "Introducing OpenAI Ads nodes for Profound Agents" (6 May, 2026)

> OpenAI shipped its self-serve ChatGPT Ads Manager yesterday, opening up the platform to any U.S. advertiser, dropping the previous $50K minimum spend floor, and introducing CPC bidding alongside the existing CPM model. We shipped four OpenAI Ads nodes for Profound Agents the same day.
> That speed matters. ChatGPT ads are a brand new performance channel, the benchmarks don't exist yet, and the marketers who get instrumentation in place first will be the ones who actually learn what works. Profound customers can now pull OpenAI Ads performance data directly into their Agent workflows on day one of the public rollout.
> What's in OpenAI's announcement — Yesterday's launch is the biggest expansion of ChatGPT advertising since the pilot began in February 2026. The headlines:
> Self-serve Ads Manager (beta). Any verified U.S. advertiser can now register at ads.openai.com, add payment info, set budgets, upload ads, and manage campaigns directly. No agency or holdco required.
> CPC bidding. Previously, ChatGPT ads were CPM-only. Now advertisers can buy on a click basis, with OpenAI recommending starting bids of $3–$5 per click. CPM is still supported in parallel.
> Conversions API and pixel-based measurement. Advertisers can now close the attribution loop between an ad click in ChatGPT and downstream actions on their own properties such purchases, sign-ups, and lead form submissions.
> Expanded partner ecosystem. Agency partners include Dentsu, Omnicom, Publicis, and WPP. Technology partners include Adobe, Criteo, Kargo, Pacvue, and StackAdapt.
> This is OpenAI moving from a closed, high-touch pilot to the kind of standardized advertising infrastructure performance marketers actually expect: self-serve buying, click-based bidding, conversion tracking, and partner integrations. The platform is still early. Independent estimates of ChatGPT ad CTR sit around 1.3% versus Google Search's 29.2%, and aggregated reporting means you don't get conversation-level visibility. But the pieces marketers need to test it as a real channel are now in place.
> The four OpenAI Ads nodes in Profound Agents — Each node targets a different level of the OpenAI Ads hierarchy and returns structured performance data you can route into any downstream node for analysis, reporting, or alerting.
> Get Ad Account Insights — Retrieve top-level performance data across your entire OpenAI Ads account. Configure it by selecting your connected ad account, setting a time range, and choosing an aggregation level: Ad Account, Campaign, Ad Group, or Ad.
> Get Campaign Insights — Retrieve performance data for a specific campaign. Supply a Campaign ID and time range, and the node returns impression, click, spend, CTR, CPC, and CPM data broken out at the cadence you choose, from daily granularity up to the full window.
> Get Ad Group Insights — Go one level deeper, returning performance data for a specific ad group within a campaign.
> Get Ad Insights — Return data at the individual ad level. Useful for creative performance analysis and for identifying which specific ads are driving results within a campaign.
> What this unlocks for marketers — Reporting without the dashboard tax [...] Cross-channel visibility reporting — This is the workflow only Profound can power. Pair OpenAI Ads performance data with Profound's organic AI visibility metrics to see paid and organic ChatGPT presence side by side. Are you spending CPC dollars in a category where your brand already has strong organic citation coverage in ChatGPT answers? Are you investing in campaigns for queries where you're invisible in AI-generated responses? Connecting the two views, in one Agent, in one report, has not been possible until now.
> Anomaly monitoring and automated alerting — Build an Agent that pulls campaign and ad-level performance daily, compares it against a rolling baseline, and fires a Slack alert when CTR drops, CPC spikes, or impression volume falls off a cliff.
> Early-mover benchmarking — ChatGPT ads benchmarks barely exist right now. Pull your impression, CTR, CPC, and CPM data on a regular cadence and you'll be building your own baseline before the rest of the market has theirs.
> Get started — The OpenAI Ads nodes are available today for all customers of Profound. To connect your OpenAI ads account to Profound, simply: Navigate to the Integrations Hub from Settings → Integrations in your account; Locate OpenAI Ads, click 'Connect Account'; Enter your OpenAI Ads API Key and your unique Connection Name (both can be found by admins of OpenAI Ads accounts within the OpenAI Ads platform settings).

## Pull notes — mechanical only

- Sitemap of tryprofound.com lists exactly three ads-related URLs: the two above and `/integrations/google-ads`. No ads-specific SKU or price appears; the integration is stated as available "for all customers of Profound".
- The blog's "$50K minimum spend floor", "$3–$5 per click", "February 2026" and partner names restate OpenAI's 2026-05-05 announcement (`raw/b-openai-new-ways-buy-ads-2026-09-22.md`); they are Profound's relay, not a primary here.
