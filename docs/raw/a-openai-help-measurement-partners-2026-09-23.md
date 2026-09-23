# OpenAI Help Center — ChatGPT Ads measurement partners, mobile measurement partners, conversion measurement, reporting metrics

```yaml
source:          OpenAI Help Center (help.openai.com), collection "ChatGPT Ads" > "Manage and optimize campaigns"
url_or_doc_id:   https://help.openai.com/en/articles/20001416-set-up-measurement-partner-integrations ; https://help.openai.com/en/articles/20001372-set-up-mobile-measurement-partner-integrations ; https://help.openai.com/en/articles/20001409-conversion-measurement ; https://help.openai.com/en/articles/20001214-measure-results
published:       page stamps at pull: "Updated: 6 days ago" (20001416); "Updated: 11 days ago" (20001372, archive copy); "Updated: last month" (20001409); "Updated: 40 minutes ago" (20001214, archive copy)
pull_date:       2026-09-23
pull_method:     fetch (curl, User-Agent "market-research-bot contact: research@example.invalid"); 20001416 and 20001409 direct after an initial HTTP 403 cleared on retry; 20001372 and 20001214 via web.archive.org `web/2026id_/` because direct fetch returned HTTP 403
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary, own help docs
source_label:    vendor-reported
lane:            A
sub_market:      paid placement
engine:          OpenAI — ChatGPT Ads (Ads Manager Beta)
metric_kind:     none (partner roster and metric definitions)
supersedes:      none — extends raw/b-openai-help-ads-collection-2026-09-23.md, which listed the article titles only
captured:        four articles, full main text
```

## Verbatim

### Set up Measurement Partner Integrations (article 20001416; "Updated: 6 days ago")

> Connect a measurement partner to ChatGPT Ads.
> ChatGPT Ads supports integrations with select measurement partners to help advertisers measure campaign performance and understand actions taken after someone engages with an ad. Depending on the partner, integrations may support capabilities such as conversion tracking, attribution, reporting, and optimization across web, app, and offline activity. Available capabilities and setup options vary by partner; refer to the partner's documentation for current details.
> For specific mobile measurement partner integrations we support, view the setup guides here.
> Before you begin — You'll need: An active Ads Manager account; A Pixel ID and Conversions API key from the Conversions section of Ads Manager; A data source containing the conversion events you want to send; The appropriate permissions in your data partner; A list of the standard or custom events you want to send to ChatGPT Ads.
> See OpenAI's measurement documentation for information about supported events, the JavaScript Pixel, and the Conversions API.
> These are the current measurement partners supported for ChatGPT Ads. We'll update this article as additional partner integrations become available.
> Set up Fospha — Log in to the OpenAI Ads Manager account at ads.openai.com. Navigate to Settings → API Keys. Click Create New Key to create a new key. Copy the Key and share it with your Fospha representative, as well as your UTM set up. For complete instructions, see the Fospha set up guide.
> Set up Hightouch — In Hightouch, open Destinations, click Add destination, and select ChatGPT Ads (OpenAI). Authenticate the destination by entering your ChatGPT Ads Pixel ID and API key. Select the model containing the events you want to send to ChatGPT Ads and create a sync to the OpenAI destination. Configure record matching and map the event properties you want to send to ChatGPT Ads. Make sure the event model uses a truly unique primary key so Hightouch sends every event.
> Set up LiveRamp — Reach out to your LiveRamp rep to request access to the OpenAI integration. If you haven't already, set up a batch file or streaming event feed to LiveRamp. [...] Both offline and online conversions can be either streamed via API or batched in flat files to LiveRamp. Create a destination account for OpenAI using your pixel ID and Conversions API key. Map your events using the "Event Types" section of the document here. Check your OpenAI ads manager to confirm successful receipt of your events.
> Set up Singular — In Singular, go to Partner Configuration and add OpenAI Ads (ChatGPT). Enter your OpenAI Ads Pixel ID and Conversions API key. Map the events you want to send to OpenAI Ads. Under Manage Links, create a Singular Link and use it in the appropriate campaign.
> Set up Triple Whale — In ChatGPT Ads Manager, go to Settings, select General, and create an API key for Triple Whale. In Triple Whale, go to Data > Integrations, find ChatGPT Ads, and click Connect. Enter your ChatGPT Ads API key and click Save. Continue applying Triple Whale UTMs to your ChatGPT Ads campaigns to attribute traffic, orders, and customer journeys in Triple Whale. Note: Triple Whale also offers data enrichment through Sonar Optimize.
> Set up WorkMagic — In WorkMagic, navigate to Integrations Settings, click on Platform Integrations, then the Marketing sub-tab. Within the Marketing integrations sub-tab, look for the ChatGPT Ads card to start the integration and click Connect. Review and agree to the terms and conditions. In ChatGPT Ads Manager, go to Settings, select General, and create an API key for WorkMagic. Back to WorkMagic, paste your ChatGPT Ads API key in the WorkMagic integration screen.

### Set up Mobile Measurement Partner Integrations (article 20001372; archive copy; "Updated: 11 days ago")

> ChatGPT Ads supports integrations with select mobile measurement partners. These integrations can help advertisers measure eligible conversions and share event data for reporting and optimization. Available capabilities and setup options vary by partner; refer to the partner's documentation for current details.
> Before you begin — You'll need: An active Ads Manager account; A Pixel ID and Conversions API key from the Conversions section of Ads Manager; Your app or website configured in your measurement partner; Appropriate permissions in AppsFlyer or Adjust; A list of the standard or custom events you want to send to ChatGPT Ads.
> AppsFlyer and Adjust are the mobile measurement partners currently supported for ChatGPT Ads. We'll update this article as additional mobile measurement partner integrations become available.
> Set up AppsFlyer — In AppsFlyer, open Partner Integrations and find ChatGPT Ads (OpenAI). Activate the integration and enter your ChatGPT Ads Pixel ID and Conversions API key. Map the events you want to send to ChatGPT Ads. For mobile apps, create an attribution link and use it in the appropriate ChatGPT Ads campaign. For websites, configure event forwarding from the AppsFlyer Web SDK to the ChatGPT Ads Conversions API.
> Set up Adjust — In Adjust Campaign Lab, add ChatGPT Ads as a partner. Select your app, enable data sharing, and enter the required ChatGPT Ads credentials. Map the events and optional data you want to share. Configure your attribution settings and campaign link, then use the resulting click URL in the appropriate ChatGPT Ads campaign.
> How attribution works — Attribution for these integrations is click-based. For mobile app measurement, use the attribution link generated by your measurement partner in the corresponding ChatGPT Ads campaign. Attribution windows and event-sharing settings are configured in your measurement partner, so refer to its documentation for available options.
> Reporting — Attributed events appear in the Conversions metric in Ads Manager. Allow 24–48 hours for reporting.

### Conversion Measurement (article 20001409; "Updated: last month")

> Conversion measurement helps you understand the actions people take after clicking an ad in ChatGPT, such as making a purchase, submitting a lead, or completing a registration.
> To measure conversions, create a data source in Ads Manager and send conversion events using the OpenAI Pixel, the Conversions API, or both. OpenAI evaluates those events against the conversion events configured for your campaign and the applicable attribution window.
> How conversions are measured — A conversion can be reported when: OpenAI receives an event from a data source connected to your ad account; The standard or custom event matches a conversion event configured for the campaign; The event occurs within the applicable attribution window; OpenAI can connect the event to an eligible ad click using available measurement signals. These signals may include the OpenAI click reference, eligible advanced matching information, and modeled measurement where available.
> The OpenAI click reference, called oppref, is appended to the end of the landing page URL in the following format: www.openai.com?oppref=gAAAAAb123. The OpenAI Pixel captures oppref and stores it in a first-party cookie so it can be associated with later conversion events. When available, advertisers can include oppref in Conversions API calls.
> For more resilient measurement, you can use the OpenAI Pixel and Conversions API together. When the same conversion is sent through both methods, use the same event ID so OpenAI can deduplicate it.
> Automatic advanced matching (AAM) helps connect website conversions to your ads when a click identifier is unavailable. The OpenAI Pixel automatically detects supported customer information from recognizable forms and other sources on your website. The Pixel normalizes and securely hashes this information in the browser using SHA-256 before including it with conversion events. Raw customer information is not sent to OpenAI through automatic advanced matching.
> Modeled measurement — Where modeled measurement is available, OpenAI may also use aggregated patterns from observed conversions to estimate attribution for otherwise unattributed advertiser-reported conversion events. [...] Reported conversion totals may include modeled conversions where available.
> Why OpenAI and third-party analytics may differ — OpenAI Ads Manager, your analytics provider, and other ad platforms may report different conversion totals. Common reasons include: Different attribution methods or attribution windows; Event timestamps, reporting time zones, or date boundaries; Browser, consent, and storage conditions that affect available measurement information; Different deduplication behavior; Campaign or conversion-event configuration; Modeled conversion reporting, where available. A difference does not necessarily indicate an error.

### Measure Results (article 20001214; archive copy; "Updated: 40 minutes ago")

> In Ads Manager Beta, you can measure campaign performance with reporting tools that help you track delivery and monitor results. As the platform evolves, we'll introduce additional metrics, reporting views, and insights over time.
> Metrics — You can currently track the following metrics across all levels (campaign, ad group, and ad): Impressions: Number of times your ads were shown; Clicks: Number of times users clicked on your ads; Spend: Total amount spent delivering your ads; CTR: Percentage of impressions that resulted in clicks; Avg CPC: Average cost per click; Avg CPM: Average cost per thousand impressions; Conversions: Number of conversion events attributed to your campaigns, if conversion measurement is set up.
> These metrics are available in table view, chart view, and CSV export downloads and can be used to evaluate delivery, engagement, and pacing across your campaigns.
> Ads Manager displays a single Conversions metric for the selected reporting scope and date range. Standard and custom conversion events configured for attribution are included in this total.
> Note: Conversions may not be reflected in Ads Manager immediately. Please allow 24–48 hours for attributed conversions to be included in reporting.
> Insights charts — Select the metric(s) you want to view: impressions, clicks, spend, or any combination of all three.
> How are conversions measured? OpenAI tracks conversions using first-party measurement signals after someone clicks an ad; for details, see Conversion Measurement.
> Can I deploy the Pixel through Google Tag Manager? Yes, as long as your tag manager loads the Pixel snippet on the correct pages and does not block or reorder the initialization and event calls.
> How should I measure Shopify, headless storefront, or server-side purchase events? Use the browser Pixel for browser-side events and the Conversions API for server-side events. If you pass server-side conversions, preserve and send the available click reference values, such as oppref, so events can be attributed correctly.
> Why do Ads clicks differ from Google Analytics sessions or landing-page visits? Ads clicks measure ad interactions. Analytics sessions depend on page load, redirects, consent settings, browser blocking, UTM handling, attribution windows, and time zone settings.

## Pull notes — mechanical only

- help.openai.com is behind a Cloudflare challenge in the Playwright browser ("Just a moment..." did not clear after 10 s); curl with the research User-Agent got HTTP 200 on the collection page and on two articles, HTTP 403 on two others; the 403 articles were taken from web.archive.org (`web/2026id_/` — snapshot timestamps not exposed by the id_ redirect; article "Updated" stamps carried above are the archive copy's).
- Named partners on the two roster articles: Fospha, Hightouch, LiveRamp, Singular, Triple Whale, WorkMagic (measurement); AppsFlyer, Adjust (mobile measurement) — 8 names. The "more than 50 technology and measurement partners" figure appears only in `raw/b-openai-1bn-run-rate-milestone-2026-09-22.md`; no page enumerating 50 was found (checked help collection 20001223, openai.com/index/new-ways-to-buy-chatgpt-ads archive copy, archive availability for openai.com/index/chatgpt-ads-partners — none).
- No prices, no partner counts, no attribution-window values on these pages.
