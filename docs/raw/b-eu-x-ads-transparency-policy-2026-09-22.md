# X — Ads transparency (help center policy page, Article 39 EU ad repository)

```yaml
source:          X (business.x.com Help Center)
url_or_doc_id:   https://business.x.com/en/help/ads-policies/product-policies/ads-transparency ; repository itself at https://ads.x.com/ads-repository (per web search, not independently fetched — see pull notes)
published:       undated — no date on page
pull_date:       2026-09-22
pull_method:     browser extension
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary, own docs
source_label:    company-stated
lane:            B
sub_market:      paid placement
engine:          Grok / X, model version n/a
metric_kind:     none
supersedes:      none
captured:        full page (main element), get_page_text
```

## Verbatim

"**DSA Ad Transparency:**

In 2023, X launched an Ads Transparency Center for the Digital Services Act (DSA)--the X Ads Repository.

For ads served in the EU, this Ad Transparency center includes the following: Advertiser, Funding Entity, the Advertiser's Main Targeting Parameters for the advertisement, Impression, and Reach of Ad to provide transparency around advertisements on the platform. The Repository also provides information related to ads halted from running on the platform.

To access the repository, search for a particular account, country, and date range using the user interface or the API (instructions below). The request will generate a .csv file containing the information about the applicable advertisement(s). If the CSV file is blank, that may indicate no ads were served by that advertiser in the relevant time period. Note: to balance the privacy interests of natural persons affiliated with our advertisers, you may request the name of the person paying for a particular advertisement via credit card here."

"**Steps for API Access to X Ads Repository:**

Create a X developer account at the X Developer portal
Once you have an account, create an app and get a bearer token
Then you will be able to make a curl request like the one below, which will provide you with an exportId:

curl 'https://api.twitter.com/graphql/e9OJa7fJKHtHftkNzcRkzw/CreateExportReportMutation' \
-H 'authorization: Bearer myToken' \
-H 'content-type: application/json' \
--data-raw '{\"variables\":{\"user\":\"$userIdOfHandle\",\"geoLocation\":\"$GeoCode\",\"deliveryRange\":{\"start_date\":\"YYYY-MM-DD\",\"end_date\":\"YYYY-MM-DD\"}}}' \
--compressed

4. To look up the status of your request, you can make a curl request like the one below:

curl --location --request GET 'https://api.twitter.com/graphql/0RTLTx4DunPS6rVj-1cLCg/GetExportReportStatusQuery' \
--header 'Content-Type: application/json' \
--header 'Authorization: myToken' \
--data '{\"query\":\"e9OJa7fJKHtHftkNzcRkzw\",\"variables\":{\"exportId\":\"$myExportId\"}}'"

## Pull notes — mechanical only

- **Fields named, verbatim**: "Advertiser, Funding Entity, the Advertiser's Main Targeting Parameters for the advertisement, Impression, and Reach of Ad." This is X's own stated field list.
- **Machine-readable: yes, by X's own description** — a GraphQL-based export API with bearer-token auth is documented in full on this page (endpoint, request/response shape).
- This page makes **no mention of Grok** or any conversational AI-answer surface — its framing is entirely "ads served on the platform" (X generally).
- Per the Commission's own non-compliance finding, captured separately in `b-eu-ec-x-fine-120m-2026-09-22.md`: despite this repository existing and being described here with a defined field list and API, the Commission found on 05.12.2025 that "X's ads repository also lacks critical information, such as the content and topic of the advertisement, as well as the legal entity paying for it" and that it "incorporates design features and access barriers, such as excessive delays in processing, which undermine the purpose of ad repositories." The gap between this page's stated field list (which does name a funding entity) and the Commission's finding (that funding-entity/payer information is missing in practice) is recorded here side by side, not reconciled — it may reflect a difference between what the interface is designed to show and what it discloses in practice, or a change between the Commission's evaluation window and this pull date.
- The live repository interface itself (`ads.x.com/ads-repository`, per web search) was not directly fetched in this pull — this file captures X's policy/help-page description of the repository, not a direct observation of the tool's current UI or a live query result.
- No entry, field, or example in this page's text indicates whether any ad shown inside a Grok conversational answer (as distinct from ads shown elsewhere on X) would appear in or be distinguishable within this repository — recorded as `unknown — checked business.x.com/en/help/ads-policies/product-policies/ads-transparency 2026-09-22`.
