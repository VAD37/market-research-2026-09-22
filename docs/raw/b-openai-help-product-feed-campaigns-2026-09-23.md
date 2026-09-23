# OpenAI Help Center — Create Campaigns from Product Feeds

```yaml
source:          OpenAI Help Center
url_or_doc_id:   https://help.openai.com/en/articles/20001268-create-campaigns-from-product-feeds
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

Product feed campaigns let retail advertisers upload a product feed in Ads Manager and create ads based on that catalog. Product feeds make it easier to bring more of your catalog into ChatGPT ads, create ads at scale, and connect users with relevant products as they explore, compare, and decide. Ads created from product feeds have been among the strongest-performing ads in our program to date.
Why create a campaign from product feeds?
Feed-based campaigns are designed for retail advertisers with broad or frequently changing product catalogs. They can help you:
- Create campaigns from your product catalog at scale with a single feed upload
- Connect users with relevant products when they may be most useful
- Keep product details, availability, and metadata used for ads up to date
Advertisers using product feeds have been among the strongest performers on the platform. Because feed ads are built from structured product data, they can make it easier to run larger, more relevant campaigns and scale performance in Ads Manager.
Before you begin
A few things to be aware of:
- Your product feed must comply with our feed specifications
- Products from your feed will only be eligible for use in ads during this beta. They will not appear in organic ChatGPT conversations, though we may offer that capability in the future
- Product ads use formats designed specifically for showcasing items from your catalog, featuring details such as product images, titles, stars, prices, sales prices, and your brand
Step 1: Create a product feed
- In Ads Manager, navigate to the Tools tab
- Select Feeds
- Click Create Feed
- Follow the prompts to create a new product feed
Step 2: Import Products
- From the feed row, open the three-dot menu
- Select one of:
- Upload CSV or TXT: Best for getting started or making occasional manual updates.
- Hosted URL: Best when your product catalog is available at a stable HTTPS address.
- SFTP connection: Best for technical teams that automate server-to-server uploads.
- SFTP upload guide
- Items expire after 2 weeks thus it is recommended to use hosted URL, or automated SFTP uploads.
Use the feed specification when formatting your feed. Feeds created through Ads Manager make products ads-eligible by default unless an item is explicitly marked false for ads eligibility.
Step 3: Upload and validate your feed
- Wait for Ads Manager to process the feed. This can take anywhere from a few minutes to a few hours depending on the size of the feed
- Check Upload History for processing updates and errors
Step 4: Create a campaign from your feed
- In Ads Manager, navigate to the Campaigns tab
- Create a new campaign
- In the campaign type dropdown, select Product feed
- Complete the campaign settings using Create Campaigns for ChatGPT Ads. New product-feed campaigns support geographic targeting and exclusions only at country level.
Step 5: Create an ad group and choose products
- Create an ad group for the campaign
- Select the product feed you want to use
- Apply product filters to define which products are eligible for the ad group
- Review the product count shown in Ads Manager to confirm how many uploaded products pass your filters
- In the Bid strategy section, select Maximize results, which is selected by default for eligible new ad groups. ChatGPT Ads automatically adjusts your bids to help get as many clicks or conversions as possible within your budget, based on your selected campaign goal. Learn more in Maximize Results Bid Strategy.
If the available filters are not enough for how you want to group products, use the ads_metadata field in your feed. For example, you can add values such as bidding_tier or product_line, then use those values to organize products for ad group setup.
Add custom labels inside each product’s ads_metadata, then apply product filters when creating the ad group to select the products it can use. You can use different filters to select different subsets of the same catalog. For example, a filter matching custom_label_0 to WA selects products carrying that label; the label itself does not restrict delivery to users in Washington. See Product Sets & Filters for developer guidance.
Step 6: Create an Ad Template
- Create an ad template for the group
- The ad template is used as the base for advertising products that are eligible based on the filters for the ad group
- The ad template currently only supports making a selection for your image field
- Only one ad template is necessary per ad group
- Review the sample product preview to confirm that titles and descriptions appear as expected
Step 7: Review and launch
Before submitting your campaign, confirm that:
- The correct feed is selected
- The product count matches the intended set of products
- Product titles, descriptions, images, and landing pages appear as expected
- Your ad template previews correctly
- Your campaign, ad group, budget, bid strategy, and targeting settings are complete.
Once everything looks correct, submit the campaign for review and launch your feed-based campaign.
Understanding the Products tab
The Products tab is a reporting view. It does not show every product that has been uploaded or is eligible for ads. A product appears there after it has delivery data from an active product-feed campaign and that data is available in reporting.
If your campaign has not started, has a future start date, or has not yet delivered, the Products tab may be empty or show fewer products than your feed contains. This does not necessarily mean that your feed upload failed or that the products cannot be selected or served.
During campaign setup, use the product count in the ad-group creation flow to confirm how many uploaded products are ready to serve and pass your selected filters. After delivery begins, allow up to seven hours for product rows to first appear in the Products tab. This initial population window is separate from campaign metrics: impressions, clicks, and CTR typically refresh approximately every 15 minutes, while spend insights are delayed by approximately 7–8 hours.
If expected products are still missing after the campaign has delivered, contact support and include:
- Ad account ID
- Feed ID
- Campaign and ad-group names
- Date range and time zone
- Example product IDs
- Screenshot of the Products tab

## Pull notes — mechanical only

- Pull date 2026-09-23, logged-out, no account. Main-text extraction drops navigation, footers and image content; images, charts and embedded posts are not captured.
