# OpenAI Help Center — Publishers and Developers FAQ (citation, crawler access, UTM referral tagging)

```yaml
source:          OpenAI Help Center
url_or_doc_id:   https://help.openai.com/en/articles/12627856-publishers-and-developers-faq
published:       undated — no date on page; page states "Updated: 24 days ago" relative to pull time
pull_date:       2026-09-22
pull_method:     browser extension
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default (platform primary, publisher-facing wording)
source_label:    company-stated
lane:            A
sub_market:      organic recommendation
engine:          ChatGPT — OpenAI
metric_kind:     none
supersedes:      none
captured:        full page
```

## Verbatim

Publishers and Developers - FAQ

Learn how publishers and developers can manage website discovery, crawler access, and ChatGPT app compatibility.

Updated: 24 days ago

Publisher FAQs

How can I get my website to appear in ChatGPT search results in the browser?

Any public website can appear in ChatGPT search. To help ensure your content can be discovered, surfaced, and clearly cited and linked, follow these guidelines:

For your site content to be included in summaries and snippets in ChatGPT, make sure you aren't blocking OAI-SearchBot. If necessary, you may need to update your robots.txt file, to ensure OAI-SearchBot has access.

Note, if we obtain the URL of a disallowed page from a third-party search provider or by crawling other pages and have signals the page is relevant to a user's query, we may surface just the link and page title in ChatGPT Atlas.

If you do not want this to happen, use the noindex meta tag. Note, in order for our crawler to read a meta tag, it must be allowed to crawl the relevant page(s).

Publishers who allow OAI-SearchBot to access their content can track referral traffic from ChatGPT using analytics platforms such as Google Analytics. ChatGPT automatically includes the UTM parameter utm_source=chatgpt.com in referral URLs, enabling clear tracking and analysis of inbound traffic from ChatGPT search results.

Does ChatGPT Atlas train on my web page content?

Publishers should disallow the GPTBot user-agent from sites and pages they wish to exclude from potential training. We respect this signal for content acquired via users' interactions in Atlas.

Note: if users opt-in to training, webpages that opt out of GPTBot will not be trained on.

Developer FAQs

What can I do to improve my website performance with ChatGPT agent in Atlas?

Making your website more accessible helps ChatGPT Agent in Atlas understand it better.

ChatGPT Atlas uses ARIA tags—the same labels and roles that support screen readers—to interpret page structure and interactive elements. To improve compatibility, follow WAI-ARIA best practices by adding descriptive roles, labels, and states to interactive elements like buttons, menus, and forms. This helps ChatGPT recognize what each element does and interact with your site more accurately.

How do apps built with the Apps SDK work in Atlas?

Apps in ChatGPT work in Atlas in the same way they might work in ChatGPT on the web. When you start a message to ChatGPT with the name of an available app, like "Spotify, make a playlist for my party this Friday," ChatGPT can automatically surface the app in your chat and use relevant context to help. The first time you use an app, ChatGPT will prompt you to connect so you know what data may be shared with the app. We recommend testing how your apps work within the Chat sidebar to ensure they work well at smaller widths.

We are also working on ways to help users more easily access apps in ChatGPT while in Atlas. For developers that are interested in deeper integrations in Atlas, we hope to share more details soon.

## Pull notes — mechanical only

- Loaded via Chrome extension (help.openai.com flagged 403→ext per channels.md C2). This is the exact page named in `query-book.md`'s exclusion-scope correction note: "the page carrying OAI-SearchBot access and the utm_source=chatgpt.com referral tag."
- **Citation/attribution mechanism confirmed verbatim**: "ChatGPT automatically includes the UTM parameter utm_source=chatgpt.com in referral URLs, enabling clear tracking and analysis of inbound traffic from ChatGPT search results" — this is company-stated confirmation of the standing UTM tag publishers can use to attribute ChatGPT-search referral traffic (glossary.md "Traffic" metric, referrer-host / UTM measurement method).
- Two distinct crawler controls named: OAI-SearchBot (search/citation inclusion — disallow it to be excluded from summaries/snippets/citation) and GPTBot (training-data acquisition — separate opt-out). robots.txt is the control surface for both; noindex meta tag is a further control specifically to prevent link/title-only surfacing in ChatGPT Atlas even when crawl is allowed.
- No price, country, or ad information on this page — pure publisher/developer technical guidance, confirming lane A scope (organic/citation), not lane B/C.
