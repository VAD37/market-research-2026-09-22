# Amazon Customer Service — About Alexa for Shopping

```yaml
source:          Amazon Customer Service (amazon.com help center)
url_or_doc_id:   https://www.amazon.com/gp/help/customer/display.html?nodeId=Tvh55TTsQ5XQSFc7Pr
published:       undated — no date on page
pull_date:       2026-09-22
pull_method:     browser extension
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default (platform primary customer-help documentation)
source_label:    company-stated
lane:            A
sub_market:      n/a
engine:          Amazon shopping assistant — page names it "Alexa for Shopping"; states plainly "Amazon is bringing Rufus and Alexa together"
metric_kind:     none
supersedes:      none
captured:        full page
```

## Verbatim

About Alexa for Shopping

Alexa for Shopping is an AI-powered shopping experience that lets you ask all kinds of shopping questions in the Amazon Shopping app and on Amazon.com.

About Alexa for Shopping

Amazon is bringing Rufus and Alexa together to create one AI assistant with shared memory and personalized preferences. In the Amazon store, this appears as Alexa for Shopping. With this experience, you can use everyday language and ask follow-up questions as you shop. Alexa for Shopping is available on both the Amazon Shopping app on your smartphone and on Amazon.com.

Alexa maintains context for the profile you're logged into, and remembers conversations across Amazon's website and app, as well as Alexa on Echo devices, Alexa.com, the Alexa app, Fire tablets, and Fire TV, so you can easily pick up where you left off. Each Alexa experience is tailored to how you engage on different devices, ensuring you get the most relevant assistance in the moment, wherever you are.

Which Alexa capabilities are available in the Amazon Shopping app and Amazon.com?

This experience is designed to help you shop. Not all Alexa functionality is available in the Amazon store. For example, if you ask Alexa to set a timer or turn on your living room lights while in the store, you may be redirected to another Alexa experience (such as alexa.com or the Alexa app) to help you carry out your request.

What data is collected and how is it used?

Alexa is designed to protect your privacy. You can review and manage all of your Alexa interactions — including your shopping conversations with Alexa — on the Review Alexa History page.

We collect and use personal information in accordance with the Amazon.com Privacy Notice. To learn more about Alexa, including how Alexa works across a range of devices and applications, see the Alexa and Alexa Device FAQs. If you do not want Amazon to use certain information, like sensitive personal data, for the purposes described in the Amazon.com Privacy Notice or the Alexa and Alexa Device FAQs, do not share it with Alexa. When you use Alexa, you agree to use it in accordance with the Alexa and Amazon Devices Acceptable Use Policy.

How can I provide feedback?

Alexa for Shopping is an AI-powered shopping experience and may not always get things right. Let us know how it's doing by giving a thumbs up or thumbs down directly in the Alexa for Shopping window.

## Pull notes — mechanical only

- Chrome extension `get_page_text` returned full page on first load, no accordion issues.
- This is the general customer-facing help/FAQ page for the assistant itself (privacy, capabilities, feedback) — not advertiser- or merchant-facing, and carries no ad-format, pricing, or merchant-feed content. Filed to confirm naming and describe the surface, per task's "surface each format appears on" requirement — Amazon Shopping app and Amazon.com (web), explicitly.
- No date anywhere on the page (help-center articles on this domain are typically undated).
- Naming corroboration: third Amazon-domain source (after the two `aboutamazon.com` pulls) independently stating "Amazon is bringing Rufus and Alexa together... In the Amazon store, this appears as Alexa for Shopping" — consistent across all three.
