# Amazon Ads Advanced Tools Center — Prompt Ad Extension reports (API/reporting docs)

```yaml
source:          Amazon Ads Advanced Tools Center (advertising.amazon.com)
url_or_doc_id:   https://advertising.amazon.com/API/docs/en-us/guides/reporting/v3/report-types/prompt-ad-extension
published:       undated — no date on page; sample API calls carry date ranges 2025-11-01 to 2026-01-23 and 2026-04-13 to 2026-04-16
pull_date:       2026-09-22
pull_method:     browser extension
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default (platform primary API/reporting documentation)
source_label:    company-stated
lane:            B
sub_market:      paid placement
engine:          Amazon shopping assistant — page does not name "Rufus" or "Alexa for Shopping" directly; describes prompts as surfacing "through conversational experiences on Amazon"
metric_kind:     none
supersedes:      none
captured:        full page
```

## Verbatim

Prompt Ad Extension reports

Prompt Ad Extension reports contain performance data for Sponsored Products and Sponsored Brands ads that include metrics for AI-powered prompt ads. Prompts are designed to help shoppers discover products through conversational experiences on Amazon by surfacing relevant product information through intelligent suggestions and guiding questions.

About Prompts

Prompts are a new ad format that integrates into your existing Sponsored Products and Sponsored Brands campaigns with zero additional setup required. They enhance product discovery at crucial shopper decision points by:

Showcasing your product expertise at scale during critical shopper decision moments
Engaging high-intent shoppers with relevant product information
Anticipating and answering shopper questions about your products

Prompts with clicks will show in your existing Sponsored Products or Sponsored Brands reporting, and you can pause individual prompts through the Amazon Ads console.

Configurations

| Configuration | Sponsored Products | Sponsored Brands |
|---|---|---|
| reportTypeId | spPromptAdExtension | sbPromptAdExtension |
| Maximum date range | 90 days | 90 days |
| Data retention | 95 days | 95 days |
| timeUnit | SUMMARY or DAILY | SUMMARY or DAILY |
| groupBy | promptAdExtension | promptAdExtension |
| format | GZIP_JSON or XLSX | GZIP_JSON or XLSX |

Sponsored Products — Base metrics: date, startDate, endDate, campaignId, campaignName, adGroupId, adGroupName, marketplaceId, advertisedSku, advertisedAsin, adId, creativeExtensionId, creativeExtensionType, promptText, impressions, clicks, clickThroughRate, costPerClick, cost, spend, viewableImpressions, acosClicks7d, acosClicks14d, roasClicks7d, roasClicks14d, purchases1d, purchases7d, purchases14d, purchases30d, purchasesSameSku1d, purchasesSameSku7d, purchasesSameSku14d, purchasesSameSku30d, purchasesOtherSku1d, purchasesOtherSku7d, purchasesOtherSku14d, purchasesOtherSku30d, unitsSoldClicks1d, unitsSoldClicks7d, unitsSoldClicks14d, unitsSoldClicks30d, unitsSoldSameSku1d, unitsSoldSameSku7d, unitsSoldSameSku14d, unitsSoldSameSku30d, unitsSoldOtherSku1d, unitsSoldOtherSku7d, unitsSoldOtherSku14d, unitsSoldOtherSku30d, sales1d, sales7d, sales14d, sales30d, attributedSalesSameSku1d, attributedSalesSameSku7d, attributedSalesSameSku14d, attributedSalesSameSku30d, salesOtherSku1d, salesOtherSku7d, salesOtherSku14d, salesOtherSku30d, purchaseClickRate7d, purchaseClickRate14d, portfolioName, campaignBudgetCurrencyCode

Group by promptAdExtension. Additional metrics: N/A. Filters: marketplaceId (values: US)

Sponsored Brands — Base metrics: date, startDate, endDate, campaignId, campaignName, adGroupId, adGroupName, marketplaceId, adId, adName, creativeExtensionId, creativeExtensionType, portfolioName, campaignBudgetCurrencyCode, promptText, impressions, clicks, clickThroughRate, costPerClick, cost, spend, viewableImpressions, acosClicks7d, acosClicks14d, roasClicks7d, roasClicks14d, purchases1d, purchases7d, purchases14d, purchases30d, purchasesSameSku1d, purchasesSameSku7d, purchasesSameSku14d, purchasesSameSku30d, purchasesOtherSku1d, purchasesOtherSku7d, purchasesOtherSku14d, purchasesOtherSku30d, unitsSoldClicks1d, unitsSoldClicks7d, unitsSoldClicks14d, unitsSoldClicks30d, unitsSoldSameSku1d, unitsSoldSameSku7d, unitsSoldSameSku14d, unitsSoldSameSku30d, unitsSoldOtherSku1d, unitsSoldOtherSku7d, unitsSoldOtherSku14d, unitsSoldOtherSku30d, sales1d, sales7d, sales14d, sales30d, attributedSalesSameSku1d, attributedSalesSameSku7d, attributedSalesSameSku14d, attributedSalesSameSku30d, salesOtherSku1d, salesOtherSku7d, salesOtherSku14d, salesOtherSku30d, purchaseClickRate7d, purchaseClickRate14d, newToBrandPurchases, newToBrandPurchasesPercentage, newToBrandUnitsSold, newToBrandUnitsSoldPercentage, newToBrandSales, newToBrandSalesPercentage

Group by promptAdExtension. Additional metrics: N/A. Filters: marketplaceId (values: US)

Sample calls — Sponsored Products:
```
curl --location 'https://advertising-api.amazon.com/reporting/reports' \
--header 'Content-Type: application/vnd.createasyncreportrequest.v3+json' \
--header 'Amazon-Advertising-API-ClientId: amzn1.application-oa2-client.xxxxxxxxx' \
--header 'Amazon-Advertising-API-Scope: xxxxxxx' \
--header 'Authorization: Bearer Atza|xxxxxxxxxxx' \
--data '{
"name":"SP prompt ad extension report 11/1-1/23",
"startDate":"2025-11-01",
"endDate":"2026-01-23",
"configuration":{
"adProduct":"SPONSORED_PRODUCTS",
"groupBy":["promptAdExtension"],
"columns":["date","campaignId","campaignName","adGroupId","adGroupName","adId","creativeExtensionId","promptText","impressions","clicks","cost","purchases7d","sales7d"],
"reportTypeId":"spPromptAdExtension",
"timeUnit":"DAILY",
"format":"GZIP_JSON"
}
}'
```

Sample calls — Sponsored Brands:
```
curl --location 'https://advertising-api.amazon.com/reporting/reports' \
--header 'Content-Type: application/vnd.createasyncreportrequest.v3+json' \
--header 'Amazon-Advertising-API-ClientId: amzn1.application-oa2-client.xxxxxxxxx' \
--header 'Amazon-Advertising-API-Scope: xxxxxxx' \
--header 'Authorization: Bearer Atza|xxxxxxxxxxx' \
--data '{
"name":"SB prompt ad extension report 4/13-4/16",
"startDate":"2026-04-13",
"endDate":"2026-04-16",
"configuration":{
"adProduct":"SPONSORED_BRANDS",
"groupBy":["promptAdExtension"],
"columns":["date","campaignId","campaignName","adGroupId","adGroupName","adId","adName","creativeExtensionId","promptText","impressions","clicks","cost","purchases7d","sales7d","newToBrandPurchases","newToBrandSales"],
"reportTypeId":"sbPromptAdExtension",
"timeUnit":"DAILY",
"format":"GZIP_JSON"
}
}'
```

## Pull notes — mechanical only

- Page initially loaded as "Loading..." (client-side-rendered SPA); a repeat `get_page_text` call on the same tab (no re-navigation) returned the fully rendered article content.
- **API-level confirmation of billing basis**: the `costPerClick` and `cost` fields in the base-metrics column list confirm CPC billing at the individual-prompt level, corroborating the plain-language "we will begin to charge for these ads as part of your CPC bidding and billing parameters" statement in `b-amazon-sponsored-prompts-ga-2026-09-22.md`.
- **Internal API identifier for the ad unit**: `reportTypeId` values `spPromptAdExtension` / `sbPromptAdExtension`; `creativeExtensionType` field name implies prompts are modeled internally as a "creative extension" attached to an existing Sponsored Products/Sponsored Brands ad, not a standalone campaign type — consistent with "integrates into your existing Sponsored Products and Sponsored Brands campaigns with zero additional setup required" stated on this same page.
- Reporting window limits: 90-day maximum date range, 95-day data retention — both fields explicitly stated for this report type, both Sponsored Products and Sponsored Brands.
- Marketplace filter restricted to `US` only for both ad products, corroborating the "North America: United States" geography stated in `b-amazon-sponsored-prompts-ga-2026-09-22.md`.
- No CPC dollar figure or rate card disclosed — this is a schema/reporting reference page, not a pricing page.
- Sample cURL API keys/tokens are placeholder values (`xxxxxxxxx`, `Atza|xxxxxxxxxxx`) as printed on the documentation page itself, not live credentials.
