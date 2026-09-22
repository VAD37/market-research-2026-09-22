# Google Merchant Center Help — How to use conversational attributes

```yaml
source:          Google Merchant Center Help
url_or_doc_id:   https://support.google.com/merchants/answer/17085370?hl=en
published:       undated — no date on page
pull_date:       2026-09-22
pull_method:     browser extension
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default
source_label:    company-stated
lane:            C
sub_market:      agentic commerce
engine:          Google — AI Mode, Merchant Center
metric_kind:     none
supersedes:      none
captured:        full page
```

## Verbatim

Page title: "How to use conversational attributes - Google Merchant Center Help"

"Conversational attributes help AI systems and conversational agents better understand your products' specific nuances. They are completely optional, and designed to complement your primary Merchant Center product data specification. By submitting these attributes, you can help customers discover information about your products across AI-driven surfaces, like AI Mode in Search and more while also enhancing traditional search experiences."

On this page: Get started with conversational attributes / How to use / Examples / Links to detailed attribute specification

### Get started with conversational attributes

"You can reference our TSV template example file as you submit conversational attributes."

"The following conversational attributes are available as part of the Google Merchant Center product data specification:"

- "Question and answer [question_and_answer]"
- "Document link [document_link]"
- "Related product [related_product]"
- "Item group title [item_group_title]"
- "Variant option [variant_option]"
- "Popularity rank [popularity_rank]"

"You can add these attributes directly into your existing product data setup, by either using a supplemental data source (recommended) or by adding them to your primary data source. You can also use the Merchant API to submit these attributes. Including them won't impact the approval status of your existing products. Use these attributes to convey descriptive information about your products including variants data."

"Note: If you already submit specific details in the description [description], product highlight [product_highlight], or product detail [product_detail] attributes - you don't need to duplicate that data again in the conversational attributes."

### How to use (table, reproduced as table)

| Attribute | How to use | Example value |
|---|---|---|
| Question and answer [question_and_answer] | Add questions and answers or FAQs about a product under [question_and_answer] | "Does it have a headphone jack?":"This version doesn't have a headphone jack.", "Does it support Bluetooth?":"It has full Bluetooth 6.0 support." |
| Document link [document_link] | Add related document (PDF) under [document_link] | https://example.com/manual.pdf — To submit more than one PDF file, separate each URL with a comma ( , ): https://example.com/manual.pdf, https://example.com/assembly_instructions.pdf |
| Related product [related_product] | Add related products under [related_product]. Group attribute with 3 sub-attributes: Relationship type [relationship_type]; Identifier type [identifier_type]; Identifier [identifier] | required_part:id:AZ7B, accessory:gtin:811571013579 |
| Item group title [item_group_title] | Add [item_group_title] attribute in combination with the item group ID [item_group_id] attribute to assign a title to a product with multiple variants | Organic Cotton Men's T-Shirt |
| Variant option [variant_option] | Use the variant option [variant_option] attribute in combination with the item group title [item_group_title] and item group ID [item_group_id] attributes to specify all variant-identifying properties of a product when it's available in different variants. Group attribute with 2 sub-attributes: name [name]; value [value] | Shoe width:narrow,size:8 |
| Popularity rank [popularity_rank] | The popularity rank [popularity_rank] attribute indicates the popularity of your product, ranked as a percentage of total inventory. The higher the value the better performing your product is compared to other products you're selling. | 95.5 |

### Examples — full product data for one variant of a mobile phone using conversational attributes (table, reproduced as table)

| Attribute | Value |
|---|---|
| ID [id] | pixel9-Pro_XL_512GB_Moonstone |
| Item group ID [item_group_id] | pixel9 |
| Title [title] | Google Pixel 9 Pro 512GB Moonstone |
| Item group title [item_group_title] | Google Pixel 9 |
| Variant option [variant_option] | display:XL,memory:512GB,color:moonstone |
| Question and answer [question_and_answer] | "Does it have a headphone jack?":"This version doesn't have a headphone jack.","Does it support Bluetooth?":"It has full Bluetooth 6.0 support." |
| Product highlight [product_highlight] | "Supports thousands of apps", "1080x2424 pixel display resolution", "Supports both 2.4 Ghz, 5 Ghz, and 6 Ghz Wi-Fi networks" |
| Product detail [product_detail] | General:Protection:"Scratch-resistant display", Connectivity:Wireless Technology:"BuiltIn; 802.11b/g/n with NFC", Connectivity:Number of USB-C ports:1 |
| Related product [related_product] | often_bought_with:id:AZ7B,often_bought_with:id:AZ7C, accessory:gtin:811571013579 |
| Popularity rank [popularity_rank] | 95.5 |
| Document link [document_link] | https://example.com/manual_pixel9.pdf |
| Link [link] | https://example.com/pixel9pro_xl |
| Image link [image_link] | https://example.com/product/pixel9_pro_xl.jpg |
| Availability [availability] | in_stock |
| Price [price] | 995.00 USD |
| Brand [brand] | Google |
| GTIN [gtin] | 840353925693 |
| MPN [mpn] | GA10376-GB |
| Condition [condition] | new |
| Color [color] | Moonstone |
| Shipping [shipping] | 0.00 USD |

### Links to detailed attribute specification (as listed, not followed in this pull)

Question and answer [question_and_answer]; Document link [document_link]; Related product [related_product]; Item group title [item_group_title]; Variant option [variant_option]; Popularity rank [popularity_rank]

## Pull notes — mechanical only

- Loaded via Chrome extension `get_page_text`; static content, tables rendered cleanly, no accordion.
- No visible "last updated" date on the page.
- This page names six conversational attributes total. Web-search snippets ahead of this pull (not filed as raw evidence, used only to route the pull) indicated four of the six ("Document link," "Question and answer," "Related product," "Product detail" — the last is a pre-existing, non-conversational attribute per this page's own "Note") each carry the sentence "This attribute is primarily intended for use in conversational experiences such as AI Mode in Google Search" on their own individual attribute-detail pages; those six individual attribute pages were not each pulled separately in this cluster — recorded as a gap, see summary file.
- No country list, no pricing, no CPC/CPA language on this page — this is a data-feed spec page, not a paid-placement page.
