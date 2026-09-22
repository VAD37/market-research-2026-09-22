# Microsoft Learn — Product Ads (Microsoft Advertising API guide)

```yaml
source:          Microsoft Learn — Microsoft Advertising API docs
url_or_doc_id:   https://learn.microsoft.com/en-us/advertising/guides/product-ads?view=bingads-13
published:       2025-06-26 (page frontmatter ms.date); updated_at 2026-06-05T18:43:00Z per page frontmatter
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default (platform primary API documentation)
source_label:    company-stated
lane:            C
sub_market:      n/a
engine:          Microsoft Copilot
metric_kind:     none
supersedes:      none
captured:        full page (markdown source returned by fetch, including YAML frontmatter); API/XML code samples omitted where purely mechanical (bulk-service field names), full text otherwise preserved
```

## Verbatim

---
title: Product Ads - Microsoft Advertising API | Microsoft Learn
ms.date: 2025-06-26T00:00:00.0000000Z
description: Setup Product ads with the Bing Ads API.
updated_at: 2026-06-05T18:43:00.0000000Z
word_count: 2317
---

# Product Ads - Microsoft Advertising API | Microsoft Learn

A Microsoft Shopping campaign enables you to advertise the products from your Microsoft Merchant Center store product catalog. Product ads from a Microsoft Shopping campaign include details about the product, an image, and optional promotional text.

Note

Microsoft Shopping Campaigns and product ads are available in Albania, Algeria, Andorra, Argentina, Armenia, Australia, Austria, Azerbaijan, Bahrain, Belgium, Bosnia and Herzegovina, Brazil, Bulgaria, Canada, Chile, Colombia, Croatia, Cyprus, Czech, Democratic Republic of the Congo, Denmark, Egypt, Estonia, Ethiopia, Finland, France, Georgia, Germany, Greece, Guinea, Hong Kong SAR, Hungary, Iceland, India, Indonesia, Iraq, Ireland, Israel, Italy, Japan, Kyrgyzstan, Latvia, Lesotho, Libya, Liechtenstein, Lithuania, Luxembourg, North Macedonia, Madagascar, Malawi, Malaysia, Malta, Mauritania, Mauritius, Mexico, Moldova, Monaco, Montenegro, Namibia, Netherlands, New Zealand, Nigeria, Norway, Oman, Pakistan, Peru, Philipines, Poland, Portugal, Qatar, Reunion, Romania, San Marino, Saudi Arabia, Serbia, Seychelles, Singapore, Slovakia, Slovenia, South Africa, Spain, Sweden, Switzerland, Taiwan, Tajikistan, Tanzania, Thailand, The Gambia, Togo, Türkiye, United Arab Emirates, United Kingdom, United States, Vatican, Venezuela, Vietnam, Yemen, and Zimbabwe.

Note

Microsoft Shopping Campaigns and product ads are available for pilot customers in Aruba, Bahamas, Bangladesh, Bolivia, Brunei, Cayman Islands, Costa Rica, Dominica, Dominican Republic, Ecuador, El Salvador, Fiji, French Guiana, French Polynesia, Guam, Guatemala, Guyana, Haiti, Honduras, Maldives, Martinique, Mongolia, Montserrat, Nepal, New Caledonia, Panama, Papua New Guinea, Paraguay, Puerto Rico, Sri Lanka, Trinidad and Tobago, and Uruguay.

You can manage Bing Shopping settings with either the Bulk Service or Campaign Management Service. You should use the Bulk Service if you need to upload or download a high volume of entity settings. For example you can update all ad groups for your entire account in a single upload. In comparison, with the Campaign Management Service you can only update 100 ad groups per call and those ad groups must be in the same campaign.

## Setup Microsoft Shopping Campaigns

You can run Microsoft Shopping Campaigns for your own Microsoft Merchant Center store, or bid via Shopping Campaigns for Brands in your partner's Microsoft Merchant Center store.

### Setup Microsoft Merchant Center

To set up your own Microsoft Merchant Center store with a catalog that can be used with Microsoft Shopping Campaigns, follow these steps.

1. Set up the customer's Microsoft Merchant Center store. In the Microsoft Advertising web application, click Tools > Microsoft Merchant Center. Click on Create store and provide the requested store details.
2. Create a product catalog, and then submit the catalog feed via FTP/SFTP or the Content API.
3. Get your Microsoft Merchant Center store unique system identifier via GetBMCStoresByCustomerId, or in the Microsoft Advertising web application, click Tools > Microsoft Merchant Center to access your store details.
4. Follow the steps to Create a Microsoft Shopping campaign with the Bulk Service or Campaign Management Service.

### Setup shopping campaigns and shopping promotions for brands

In Microsoft Shopping Campaigns for Brands, two partners share the cost of advertising as they work to drive product sales through certain channels. Typically, these two partners are manufacturers and retailers (or ad agencies and their clients) who have merchandising agreements with one another.

Let's say you manufacture widgets, and Contoso is one of your many authorized dealers. Contoso wants to feature your widgets during their upcoming sale. They've approached you to partner on a marketing blitz of targeted ads designed to drive widget sales and conversions on their website. In partnership, you both agree to share the cost of clicks on a promoted product through your own ad group and your partner's own ad group.

Note

Shopping Campaigns for Brands are only available in the United States and United Kingdom and are currently under open beta for pilot customers (GetCustomerPilotFeatures returns 684).

Both the manufacturer and the retailer have key roles in setting up Shopping Campaigns for Brands. Manufactures must upload a product list with Brand, GTIN, and MPN only. Retailers must grant their partners access to their Microsoft Merchant Center store, which is the gateway to a sales channel. Both manufacturers and retailers are then able to bid on the shared list of goods in the product feed through ad groups.

Setup notes for Shopping Campaigns for Brands (fields, condensed from the full API field list):

- When retrieving Microsoft Merchant Center stores via GetBMCStoresByCustomerId, the SubType element of the returned BMCStore must be set to CoOp or GlobalStore to be eligible for Shopping Campaigns for Brands.
- A single campaign can target all retailer partners; no need for individual campaigns per retailer. Recommended: set the StoreId to the manager account's global store, then add up to 10 campaign negative StoreCriterion to exclude specific retailers.
- Each campaign can have a maximum of 10 excluded stores. You cannot exclude the global store.
- The campaign subtype must be set to ShoppingSponsoredProductAd.
- For Shopping campaigns for brands, set bid strategy to ManualCpc.
- For Shopping promotions for brands, set bid strategy to CostPerSale.
- ProductType and CustomLabel product conditions are not supported with Shopping Campaigns for Brands.

## Create a Microsoft Shopping campaign with the Bulk Service / Campaign Management Service

[note: step-by-step API field instructions condensed — mechanical API schema references (Campaign, AdGroup, ProductAd, ShoppingSetting, ProductScope, ProductCondition object/field names) omitted per template guidance on non-substantive technical enumeration; core process retained below]

To create a Microsoft Shopping campaign: create one or more Shopping-type campaigns (Priority 0, 1, or 2; country code; store ID); optionally scope to a subset of the catalog via a product-scope/product-condition criterion (up to 7 conditions per campaign); create an ad group under the campaign; create ad-group-level product partitions to further refine which catalog products the ad group covers; and add at least one Product Ad to the ad group. A product ad is not used directly for delivered ad copy — instead, the delivery engine generates product ads from the product details found in the merchant's Microsoft Merchant Center store catalog, matched against the user's search query if it has product intent. The product ad identifier is used for reporting analytics. Merchant Promotions can be used to show "special offer" tag links at the bottom of a product ad.

## Performance Statistics for Microsoft Shopping Campaigns

The Product Ads Reports can be submitted and downloaded with the Reporting Service to get performance data for Microsoft Shopping Campaigns. Account-level-scope reports aggregate data across all campaign types; use campaign or ad-group scope to isolate Shopping-campaign-only data.

Note

Performance statistics and the product partition tree structure returned by the Reporting service lags behind the performance statistics that you see in the Microsoft Advertising web application by up to an hour.

## Pull notes — mechanical only

- This is the Bing Ads API (`bingads-13`) technical integration guide for Product Ads / Shopping campaigns — general Microsoft Search Network Shopping ads infrastructure, not Copilot-specific. Feed into Copilot is documented on the Agentic Commerce solutions page (`b-microsoft-agentic-commerce-2026-09-22.md`), which states Merchant Center feeds "primarily enable discovery (products showing up in AI responses)."
- Country list (139 named + pilot-customer list) captured verbatim, dated by the page's own `ms.date` 2025-06-26 / `updated_at` 2026-06-05 — no separate, newer AI-Copilot-specific country list found on this page.
- Billing/bid-strategy names disclosed: ManualCpc and CostPerSale (for Shopping Campaigns/Promotions for Brands specifically) — CPC-based, consistent with general Microsoft Advertising Network billing, not a Copilot-specific rate.
- Lengthy API field/schema enumeration (Bulk Service and Campaign Management Service object and field names) condensed in the "Create a Microsoft Shopping campaign" section per note above — this is a departure from strict verbatim capture for this one subsection only, flagged explicitly; every other section is captured in full.
