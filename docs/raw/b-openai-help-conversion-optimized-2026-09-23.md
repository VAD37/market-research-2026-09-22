# OpenAI Help Center — Conversion-optimized Campaigns (oCPC / oCPM)

```yaml
source:          OpenAI Help Center
url_or_doc_id:   https://help.openai.com/en/articles/20001412-conversion-optimized-campaigns
published:       undated — no date on page
pull_date:       2026-09-23
pull_method:     fetch — python urllib (browser user-agent, no login) + trafilatura main-text extraction; not the Chrome extension
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default
source_label:    company-stated
lane:            B
sub_market:      paid placement
engine:          ChatGPT — OpenAI
metric_kind:     none
supersedes:      none
captured:        full page
verbatim:        full
```

Pass 12, Lane B (task P12-ads). Body below is the page's own text as extracted, unedited.

## Verbatim

Learn how conversion-optimized campaigns work with click billing (oCPC) and impression billing (oCPM).
Use conversion-optimized campaigns when you want ChatGPT Ads to optimize delivery toward a specific conversion event, such as a purchase, sign-up, lead submission, or other supported standard conversion event. You can choose conversion-optimized campaigns with click billing (oCPC) or conversion-optimized campaigns with impression billing (oCPM). For a general overview of campaign objectives, see Create Campaigns for ChatGPT.
oCPC campaigns are billed based on valid clicks and optimize toward conversions that happen after someone clicks your ad. oCPM campaigns are billed based on impressions served and optimize toward conversions while accounting for a broader set of eligible conversion signals, including actions that follow ad clicks and ad views.
oCPM can help advertisers better reflect how people discover, evaluate, and choose products through ChatGPT. Someone may see an ad while exploring an idea, return later, and complete a conversion without a direct ad click. Impression billing lets delivery stay focused on your conversion goal while measurement can include more of the moments that contribute to that outcome.
Before you start
Before creating a conversion-optimized campaign, make sure:
- Conversion tracking is set up for your ad account. You can set it up via Conversions API and/or JavaScript Pixel.
- At least one supported standard conversion event is available. Custom conversion events are not currently supported for conversion-optimized campaigns.
- You know which conversion event you want the campaign to optimize toward.
- You are ready to create a new campaign. Existing CPM, CPC, oCPC, or oCPM campaigns cannot be changed to a different objective or billing model at this time.
1. Create a new campaign
In Ads Manager, create a new campaign. In the Campaign objective field, set the objective to Conversions. This makes conversion optimization available for the campaign.
2. Choose impression billing or click billing
Then select an option for how you're charged for this campaign. Choose Impressions (CPM) for conversion-optimized impression billing (oCPM) when you want impression-based buying that is still optimized toward conversion outcomes. With oCPM, you are billed based on impressions served while delivery remains focused on your selected conversion goal.
oCPM is designed to help the system learn from a broader set of eligible conversion outcomes, including conversions that follow ad clicks and ad views. This can give you a more complete view of how your ads contribute across the customer decision journey.
Choose Clicks (CPC) for conversion-optimized click billing (oCPC) when you want delivery optimized toward conversions that follow an ad click. With oCPC, you are billed for valid clicks.
The campaign objective and billing model cannot be changed after campaign creation. If you need a different objective or billing model later, create a new campaign.
3. Choose a conversion event
After choosing the billing method, choose the Conversion event you want to optimize for. This is the downstream action, such as a purchase, sign-up, lead submission, or other supported standard conversion event, that ChatGPT Ads will use to guide delivery.
Each conversion-optimized campaign uses one selected conversion event. The conversion event cannot be changed after campaign creation. To optimize toward a different event, create a new campaign.
4. Set campaign budget, dates, and locations
Set your campaign budget, start and end dates, and location targeting as you would for other campaign objectives. Choose settings that give the campaign enough time and budget to gather meaningful performance data.
5. Create ad groups and set bid controls
Create ad groups and ads as you normally would. Follow the bid strategy and bid control options shown in Ads Manager for the billing option you selected.
For conversion-optimized campaigns, Bid Cap is the maximum amount you are willing to bid for a conversion. The system uses predicted conversion likelihood to determine an auction bid while optimizing toward your selected conversion event. Billing remains based on your preferred optimization model, and your actual cost per conversion is determined by the auction.
6. Launch and monitor performance
For conversion-optimized campaigns, Ads Manager shows standard delivery and spend metrics alongside conversion reporting. You can review performance across the reporting views available in Ads Manager.
For oCPC, Average CPC is the main cost metric for what you pay per click. Because oCPC optimizes toward your selected conversion event, Conversions is the key outcome metric to monitor.
For oCPM, Average CPM and impressions are important billing and delivery metrics. Because oCPM optimizes toward conversions, monitor conversion volume, cost per conversion, and reporting for click-through and view-through conversions when available.
When evaluating performance, look at conversion volume together with spend, impressions, clicks, and the attribution windows selected for the campaign. You may also calculate cost per conversion by dividing spend by conversions.
Optimization tips
- Choose the conversion event that best represents your campaign goal.
- Use a conversion event with enough signal. Events that happen too rarely can make performance harder to evaluate.
- Keep conversion tracking healthy. Incomplete or misconfigured tracking can make reporting and optimization less effective.
- For oCPM, review both click-through and view-through conversion reporting when available to understand how ad views and clicks contribute to outcomes.
- Monitor performance and adjust your Bid Cap, bid strategy, or available bid controls based on campaign delivery and results. There is no recommended bid amount at this time.
- Review performance over enough volume before making large changes to bids, budgets, or creative.
- Enable automatic advanced matching for your website pixel to help improve conversion matching and provide additional measurement signals for campaign optimization.
FAQ
Which conversion event types are supported for conversion-optimized campaigns?
Conversion-optimized campaigns currently support one standard conversion event per campaign. Custom conversion events are not currently supported.
Can I convert an existing CPM or CPC campaign to oCPC or oCPM?
You cannot modify an existing CPM or CPC campaign to use oCPC or oCPM at this time. Create a new campaign with the Conversions objective in Ads Manager. To use oCPM, you can also clone an existing campaign to create a new oCPM campaign.
Can I switch an existing oCPC campaign to oCPM, or an oCPM campaign to oCPC?
No. The campaign objective, billing model, and conversion event cannot be changed after creation. To use a different conversion-optimized billing option, create a new campaign. If you’re moving to oCPM, you can clone your existing campaign to create a new oCPM campaign.
Does a conversion-optimized campaign mean I pay per conversion?
No. Conversion-optimized campaigns optimize delivery toward your selected conversion event, but billing depends on the option you choose. With oCPC, you are billed for valid clicks. With oCPM, you are billed for impressions served.
What does oCPM mean?
oCPM stands for optimized cost per mille, or optimized cost per 1,000 impressions. The campaign is billed based on ad impressions and optimized toward a selected conversion outcome.
Why use impression billing if my goal is conversions?
A click captures one part of the customer journey, but customers do not always act immediately after encountering a brand. Impression billing supports conversion optimization that can account for eligible ad exposures across more of the decision journey while keeping billing tied to impressions served.
Will clicks still matter for oCPM?
Yes. Clicks remain a valuable signal of interest, and conversions that follow a click continue to matter. oCPM is designed to expand the set of eligible conversion signals that can inform delivery, including conversions after ad views and ad clicks.
How will conversions be counted for oCPM?
Attribution depends on the eligible conversion event and applicable measurement rules. When available, flexible click-through and view-through attribution windows will let you choose reporting settings that best fit your measurement strategy.
How does my Bid Cap affect what I pay?
For an oCPC campaign, Bid Cap is a conversion-oriented bid used to determine how the campaign competes in click auctions; it is not the price charged for a conversion or a guaranteed achieved cost per acquisition. You are billed for valid clicks, and your actual cost per click is determined by the auction.
Next steps
After creating your conversion-optimized campaign, you can:

## Pull notes — mechanical only

- Pull date 2026-09-23, logged-out, no account. Main-text extraction drops navigation, footers and image content; images, charts and embedded posts are not captured.
