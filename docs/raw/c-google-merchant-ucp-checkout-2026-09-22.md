# Google Merchant Center Help — About the Universal Commerce Protocol (UCP) and UCP-powered checkout feature on Google

```yaml
source:          Google Merchant Center Help
url_or_doc_id:   https://support.google.com/merchants/answer/16837055?hl=en
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
captured:        full page, FAQ rendered expanded by default
```

## Verbatim

Page title: "About the Universal Commerce Protocol (UCP) and UCP-powered checkout feature on Google - Google Merchant Center Help"

"This article only applies to products with eligibility in the United States, Canada, and Australia, and for participating merchants and partners. You may see this checkout experience soon on specific surfaces such as AI Mode in Search and Gemini."

"Note: The checkout feature enabled by UCP is available for select merchants at this time. If you'd like to express interest in participating, make sure you meet the following requirements and then fill out the form here."

### About the Universal Commerce Protocol (UCP)

"The Universal Commerce Protocol is a new open standard for agentic commerce that enables agents and systems to work together across the commerce ecosystem. It works across the entire shopping journey from discovery and buying to post-purchase support. UCP establishes a common language for agents and systems to operate together across consumer surfaces, businesses, and payment providers. The protocol is compatible with major industry protocols such as Agent2Agent (A2A), Agent Payments Protocol (AP2), and Model Context Protocol (MCP)."

### About the checkout feature powered by UCP

"By integrating with UCP, you can implement a checkout button on eligible product listings in AI Mode in Google Search and on Gemini."

"You will remain the seller of record and may be able to customize the integration to preserve your specific checkout requirements and needs. Customers can checkout quickly with Google Pay, using payment methods and shipping information already saved in Google Wallet. Customers will remain in the secure Google Pay flow, which eliminates additional steps in the checkout process and may help boost confidence and reduce cart abandonment."

### Frequently asked questions (verbatim)

**Q: How can I implement the Universal Commerce Protocol (UCP)?**
A: "The protocol will be available in phases. To participate in the early access program, make sure that you meet the following requirements. Then, submit this interest form, and complete the required technical implementation. Only product listings using the native_commerce(checkout_eligibility) product attribute will display the "Buy" button for this checkout experience. See detailed product data implementation. Learn more about how to onboard to the Universal Commerce Protocol in Merchant Center"

**Q: How does UCP relate to the agentic checkout feature?**
A: "Google's agentic checkout feature buys things on the customer's behalf directly on a merchant's website at the customer's direction. UCP is the open protocol which standardizes the programmatic exchange of information (via API, MCP or A2A) between the AI Agent and the Merchant's backend to enable a broad set of commerce journeys including product discovery and checkout on Google AI Mode and Gemini."

**Q: What is the difference between the existing checkout button and this new checkout experience?**
A: "With the existing checkout button, the transaction occurs on your site. With the new checkout experience enabled, the checkout happens directly on Google's surfaces while keeping you the merchant of record."

**Q: What kind of payment credentials are supported by UCP?**
A: "Currently, the feature uses standard Funding Primary Account Numbers (FPANs) that users have stored on their Google Wallet. More forms of payments may become available in the future."

**Q: Do I need to enable the Google Pay API buy button to participate?**
A: "No, you do not need to include the Google Pay button on your own checkout surfaces to participate. You do need to create a Google Pay & Wallet Console account. If your PSP is not integrated with the Google Pay API, the PSP can follow the steps here to onboard. If you require processing payments direct integration (without a PSP) you will also need to configure encryption and upload PCI compliance documentation. You can find guidance for this integration here."

**Q: What changes do I need to make to my Merchant Center account?**
A: "Merchant Center will continue to be the central hub to prepare your product data to show ads and listings on Google surfaces. The best preparation is to ensure all your data in the Merchant Center - from product feeds to brand assets - is as robust and up-to-date as possible. Review the guidelines for full UCP implementation guide"

## Pull notes — mechanical only

- Loaded via Chrome extension `get_page_text`; FAQ answers rendered directly in the extracted text on this page (unlike the two other Google FAQ pulls in this cluster, where the accordion had to be forced open via page script) — no script intervention needed here.
- No visible "last updated" date on the page.
- **Country list, this specific feature**: "United States, Canada, and Australia" — explicitly narrower than the "eligible U.S. retailers" wording in `c-google-ucp-merchant-agentic-2026-09-22.md` (2026-01-11) and narrower than the no-country-stated `developers.google.com/merchant/ucp` guide (`c-google-ucp-merchant-guide-2026-09-22.md`). The three Google pages give three different country statements for the same UCP checkout feature; none reconciled here.
- Gating language: "available for select merchants at this time," "early access program," "The protocol will be available in phases" — this is not a generally-available, self-serve feature as of the pull date per this page's own wording.
- Required attribute for the "Buy" button named explicitly: "Only product listings using the native_commerce(checkout_eligibility) product attribute will display the "Buy" button for this checkout experience."
- No pricing, fee, or take-rate language anywhere on this page.
