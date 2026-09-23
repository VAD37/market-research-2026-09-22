# OpenAI Help Center — Create Campaigns for ChatGPT Ads (incl. Minimum Campaign Spend table)

```yaml
source:          OpenAI Help Center
url_or_doc_id:   https://help.openai.com/en/articles/20001210-create-campaigns-for-chatgpt-ads
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

Campaigns define your overall advertising objective and budget in ChatGPT Ads Manager Beta. A good campaign groups together ad groups and ads that support a shared business goal.
Each campaign contains:
- Campaign title
- Objective
- Conversion event (for campaigns with the Conversions objective)
- Budget
- Start and end dates
- Countries to target
- Platforms to target (optional)
- Custom audiences to include or exclude (optional)
Choosing a campaign objective
Your campaign objective determines how your ads are priced and how delivery is optimized. Choose Views (CPM), Clicks (CPC), or Conversions.
- Views (CPM): Best for maximizing visibility and exposure. You pay per 1,000 impressions served.
- Clicks (CPC): Best for driving users to click through to your website or product. You pay per valid click.
- Conversions: Best for optimizing toward a selected supported conversion event. Select a billing method: valid clicks (oCPC), billed per valid click, or impressions served (oCPM), billed per 1,000 impressions served. You do not pay per conversion.
For eligibility, setup, and more details, see Conversion-optimized Campaigns.
Setting your budget
Your campaign budget controls how much you are willing to spend across all ads within the campaign. When creating a campaign, choose either a campaign-total budget or a daily budget.
When setting your budget:
- Campaign-total budget: Set the total amount you want to spend over the full duration of the campaign. This is the stricter control for total spend.
- Daily budget: Set the average amount you want the campaign to spend per day over a seven day period. This is a delivery target, so actual spend may fluctuate above or below the selected amount on an individual day. If delivery is below your daily budget on some days, unused amounts may be used later in the same seven day period. Daily spend will not exceed twice your selected daily budget, and spend over the applicable seven day period will not exceed seven times your selected daily budget, subject to applicable proration when a budget changes. See Daily Budgets for details. The current minimum daily budget varies by your ad account’s billing currency. See the Minimum Campaign Spend table below for the applicable amount. The budget week runs from Sunday through Saturday in your ad account’s timezone. Delivery need not be even within a day or across the week. If a campaign uses up its weekly allowance early, it may stop delivering until the next budget week even while marked active.
Distribute your planned spend across campaigns based on priority, and adjust budget amounts over time as you learn what performs best. If you are new to the platform, we recommend starting with a daily budget so you can monitor delivery and performance before committing to a campaign-total budget.
Choosing start and end dates
Your campaign start and end dates control how long your ads are eligible to run.
When choosing dates:
- Give campaigns enough time to gain traction and gather meaningful performance data. Campaigns can always be paused or adjusted later.
- Consider seasonality, including seasonal products, new launches, promotions, holidays, or other time-sensitive campaigns.
- Align campaign timing with your broader marketing budget and business goals.
Choosing countries to target
Country targeting determines where your ads are eligible to appear.
Note: International targeting for new self-serve accounts
Some new self-serve ad accounts can initially advertise only in their home country—the country associated with the ad account. Selecting other countries does not override this restriction.
Your account automatically becomes eligible to advertise in other supported countries once identity verification is approved and you reach the required advertising spend from running campaigns in your home country. Creating a campaign or setting a budget alone is not enough. Normal campaign delivery requirements still apply.
Choosing platforms to target
Use platform targeting to choose where your campaign can deliver. In the Campaign dialog, select one or more supported platforms: Android app, Android web, Desktop web, iOS app, or iOS web. In Insights, segment by Platform to see results for each of those five platforms.
Choosing custom audiences to include or exclude
For campaigns targeting the EEA or Switzerland, avoid custom audiences while ads personalization is unavailable there. Inclusion targeting requires at least 25,000 matched users; exclusions can use smaller audiences. You can add, remove, or replace audience members without recreating the audience or reconfiguring the campaign.
To include or exclude custom audiences from a campaign, see Set up Custom Audiences for your campaign.
Best practices
- Structure campaigns around distinct business goals or initiatives.
- Use separate campaigns for meaningfully different objectives, regions, or product categories.
- Keep campaign naming clear and consistent for easier reporting and management.
- Create multiple ad groups within each campaign to test different themes, value propositions, or messaging approaches.
Campaign setup FAQ
Can I change a campaign objective after creation?
The campaign objective determines pricing and optimization. If you need a different objective, create a new campaign with the objective you want instead of editing an existing campaign into a different objective.
Can I change the budget type after creation?
You can adjust supported budget amounts over time, but some budget type changes are not reversible. For example, if you change a campaign-total budget to a daily budget, you can't change that campaign back to a campaign-total budget. If the budget type is wrong, create a new campaign with the correct setup.
Can I target a state, city, market, or postal code?
New product-feed campaigns support geographic targeting and exclusions only at country level. Existing product-feed campaigns were not automatically changed, so earlier sub-national selections may remain, but new sub-national selections cannot be added. For other campaigns, yes. In addition to country targeting, you can target supported locations such as states or regions, cities, markets, and postal codes where available. Location availability may vary by country. Search for a location during campaign setup to see the options available to you.
To select a subset of your product catalog, use custom feed metadata and ad-group product filters. See Create Campaigns from Product Feeds.
Why is my campaign not serving?
Confirm that your ad account verification and billing are complete, the campaign and ads are active, the campaign dates include today, and the ads have completed review. For troubleshooting guidance, see Troubleshooting.
Next steps
After creating your campaigns, you can:
Minimum Campaign Spend
| Billing currency | Minimum daily budget | 
|---|---|
| AED | 65 AED | 
| AUD | 25 AUD | 
| BRL | 40 BRL | 
| CAD | 25 CAD | 
| CHF | 20 CHF | 
| CZK | 350 CZK | 
| DKK | 110 DKK | 
| EUR | 15 EUR | 
| GBP | 15 GBP | 
| HUF | 5,500 HUF | 
| ILS | 60 ILS | 
| INR | 725 INR | 
| JPY | 2,500 JPY | 
| KRW | 25,000 KRW | 
| MXN | 150 MXN | 
| NOK | 160 NOK | 
| NZD | 25 NZD | 
| PLN | 65 PLN | 
| QAR | 70 QAR | 
| RON | 80 RON | 
| SAR | 50 SAR | 
| SEK | 175 SEK | 
| USD | 25 USD |

## Pull notes — mechanical only

- Pull date 2026-09-23, logged-out, no account. Main-text extraction drops navigation, footers and image content; images, charts and embedded posts are not captured.
