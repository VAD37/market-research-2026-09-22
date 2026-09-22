# Google Merchant Center Help — Native commerce [native_commerce]

```yaml
source:          Google Merchant Center Help
url_or_doc_id:   https://support.google.com/merchants/answer/17251586?hl=en
published:       undated — no date on page
pull_date:       2026-09-22
pull_method:     browser extension
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default
source_label:    company-stated
lane:            C
sub_market:      agentic commerce
engine:          Google — AI Mode, Gemini app, Merchant Center
metric_kind:     none
supersedes:      none
captured:        full page
```

## Verbatim

Page title: "Native commerce [native_commerce] - Google Merchant Center Help"

"The native commerce [native_commerce] attribute enables you to opt your eligible product listings into the "Buy Now" flow (also known as native checkout) on Google surfaces. When this attribute is correctly configured, customers can discover products and complete a purchase directly within interfaces such as Gemini and AI Mode in Google Search without being redirected to an external website."

On this page: Benefits / When to use / Format / Best practices

### Benefits

"Providing the native commerce [native_commerce] attribute offers several key benefits:"

- "Enhanced Transactability: Opt your products into checkout on high-intent surfaces like Gemini and AI Mode in Search."
- "Seamless Integration: Easily managed through supplemental feeds without disrupting primary data."

### When to use

"Optional for all products."

"Native commerce [native_commerce] is a group attribute that contains the sub-attribute checkout eligibility [checkout_eligibility], a boolean value that dictates whether the "Buy" button is displayed for a specific item."

- "true: This value enables the "Buy" button on supported Google surfaces."
- "false (or leave empty): This value disables the "Buy" button, keeping the item as a standard product listing."

### Format

"To enable native checkout for your products, you must add the native commerce [native_commerce] group attribute and its checkout eligibility [checkout_eligibility] sub attribute to your product data source in Google Merchant Center. Follow these formatting guidelines to make sure Google understands the data you're submitting. Learn when and how to Submit attributes and attribute values."

**Formatting specifications** (table, reproduced as table)

| Field | Value |
|---|---|
| Technical name | native_commerce |
| Type | Group attribute with 1 sub-attribute |
| Sub-attributes | Checkout eligibility [checkout_eligibility]. Boolean. Supported values: true, false |
| Repeated field | No |

**Formatting Guidelines**

"To ensure your attribute is recognized correctly, use the formatting specific to your data source type."

- Text (TSV or CSV) data sources — For Feed (tab-separated text) and Google Sheet Files: `ID native_commerce(checkout_eligibility)` — example rows: `11111 true`, `22222 true`, `33333 false`
- XML data sources — example:
```
<item>
<g:id>11111</g:id>
<g:native_commerce>
<g:checkout_eligibility>true</g:checkout_eligibility>
</g:native_commerce>
<g:consumer_notice>
<g:consumer_notice_type>prop_65</g:consumer_notice_type>
<g:consumer_notice_message>
This product can expose you to chemicals...
</g:consumer_notice_message>
</g:consumer_notice>
</item>
<item>
<g:id>22222</g:id>
<g:native_commerce>
<g:checkout_eligibility>true</g:checkout_eligibility>
</g:native_commerce>
</item>
<item>
<g:id>33333</g:id>
<g:native_commerce>
<g:checkout_eligibility>false</g:checkout_eligibility>
</g:native_commerce>
</item>
```
- Merchant API: "Provide the attributes as custom attributes. You can add them to your existing accounts.productInputs.insert, or update them directly using accounts.productInputs.patch." Example for insert:
```
"customAttributes": [
{
"name": "native_commerce",
"groupValues": [
{
"name": "checkout_eligibility",
"value": "true"
}
]
},
```

### Best practices

"Recommended Methodology: Supplemental Feeds — We strongly recommend using a supplemental feed to implement this attribute. Supplemental feeds allow you to add or update specific attributes for existing products without modifying your primary product feed, which ensures your existing Ads campaigns and core product data remain undisturbed."

"Troubleshooting and Verification — After uploading your updated feed, check the "Data sources" tab in Google Merchant Center to confirm that the native commerce [native_commerce] attribute has been successfully ingested. Look for any processing errors related to custom attributes or supplemental feed updates."

"For detailed technical specifications and API documentation, you can refer to the official UCP Developer Guide."

## Pull notes — mechanical only

- Loaded via Chrome extension `get_page_text`; static content, no accordion, formatting examples rendered as plain text/pseudo-code in the DOM (not a real code block widget) — reproduced verbatim above.
- No visible "last updated" date on the page.
- This is the required feed attribute confirmed by `c-google-merchant-ucp-checkout-2026-09-22.md`'s FAQ answer ("Only product listings using the native_commerce(checkout_eligibility) product attribute will display the "Buy" button for this checkout experience").
- No country list, no pricing/fee language on this page.
