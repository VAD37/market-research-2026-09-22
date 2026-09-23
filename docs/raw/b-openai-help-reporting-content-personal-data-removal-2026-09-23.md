# OpenAI Help Center — "Reporting Content in ChatGPT and OpenAI Platforms" and "Right to be forgotten and personal data removal from ChatGPT" (Wayback copies)

```yaml
source:          OpenAI Help Center (help.openai.com), via web.archive.org
url_or_doc_id:   https://web.archive.org/web/2026id_/https://help.openai.com/en/articles/10245791-reporting-content-in-chatgpt-and-openai-platforms ; https://web.archive.org/web/20260423234609id_/https://help.openai.com/en/articles/20001057-right-to-be-forgotten-and-personal-data-removal-from-chatgpt ; CDX: http://web.archive.org/cdx/search/cdx?url=help.openai.com/en/articles/*&collapse=urlkey
published:       article 10245791 shows "Updated: 6 days ago" relative to the Wayback capture served for the 2026 request (capture timestamp not printed by the id_ endpoint; latest CDX row 2026-03-18); article 20001057 capture 2026-04-23
pull_date:       2026-09-23
pull_method:     fetch (curl --compressed) of Wayback `id_` copies; help.openai.com direct returned HTTP 403 (bot wall) and its sitemap 403
pull_purpose:    evidence about a number (existence and scope of a correction channel; no number)
tier:            3
tier_reason:     platform primary (engine's own help docs), table default; archive copy, not live
source_label:    company-stated
lane:            B
sub_market:      n/a
engine:          ChatGPT
metric_kind:     none
supersedes:      none
captured:        full article text for both articles (navigation stripped)
```

## Verbatim — article 10245791, "Reporting Content in ChatGPT and OpenAI Platforms"

> Learn how to report content across conversations, shared links, GPTs, and forums that may violate OpenAI's Terms of Use or applicable laws. Updated: 6 days ago
>
> You can report conversations, shared links, responses, GPTs, and forum posts that may violate OpenAI's Terms of Use or applicable laws via our content reporting webform. Reported domains and other content may be reviewed by OpenAI's Model Quality team, which may apply filters or other mitigations to help prevent ChatGPT from relying on unreliable sources in future responses. You may also be able to make a report in-product; see below for how to report across platforms. If you are a UK user and wish to opt out of future communications once you have submitted your report, please use the content reporting form so you can elect to opt-out.
>
> Reporting Intellectual Property concerns — If you believe content on an OpenAI product infringes your intellectual property rights, you can report it using the relevant form below: Copyright infringement: https://openai.com/form/copyright-disputes/ — Trademark infringement or counterfeit goods: https://openai.com/form/trademark-counterfeit-disputes/ — In-product reporting may also be available. However, using the relevant form above will help ensure that your report includes the information required for review.
>
> Conversations with ChatGPT — You can report a ChatGPT conversation directly from the message in question on both mobile (iOS and Android) and web (chatgpt.com). Tap thumbs down (👎) under a ChatGPT message. Tap Select an issue. Select "Safety or Legal concern". Follow the prompts to submit your feedback.
>
> [Shared Links, Conversations with GPTs, GPTs — in-product "Report" paths per platform; omitted here, no brand-relevant wording]
>
> Ads content — Web — To report an ad in ChatGPT: On the ad, click ⋯ (top right). Select Report this ad. In the pop-up, choose why you're reporting it. (Optional) Provide additional details in the text box. Click Submit. You can submit without entering any additional details.
>
> ChatGPT Sites — ChatGPT Sites do not currently have an in-product reporting option. To report a Site, use the Report Contact Form.
>
> OpenAI Forums — OpenAI Community Forum: Go to openai.com/form/report-content. Submit your report with a link to the content in question. … OpenAI Developer Forum: Navigate to openai.com/form/report-content, or click "Report illegal content" from the footer of any thread.

## Verbatim — article 20001057, "Right to be forgotten and personal data removal from ChatGPT" (excerpts)

> …may be able to ask OpenAI to stop certain personal information about you from appearing in ChatGPT responses. This may apply where the information is inaccurate, excessive, irrelevant, or no longer appropriate. This type of request is sometimes referred to as an "erasure", "right to be forgotten" or "objection" request. If you'd like to make one of these requests, you can submit a "Remove my personal data from ChatGPT responses" request via our Privacy P[ortal]…
>
> …whether or not you have a ChatGPT account, you can ask OpenAI to prevent information about you from appearing in ChatGPT responses if you believe that it is inaccurate, excessive, irrelevant, or no longer appropriate. Requests are typically submitted by the person concerned, but requests may also be made by a legally authorised representative acting on someone else's behalf. In such cases, we may ask for documentation confirming that authority.
>
> [What to include:] …chats referencing your personal details — Detailed reasons why you believe the information should be removed (i.e. precise reasons for the data being inaccurate, excessive, irrelevant or no longer appropriate) — Proof of identity (e.g. government-issued ID) — Contact email — Submit the request. We may contact you for clarification or additional information if needed.
>
> How we review requests — … a person's public or professional activities may be more likely to remain relevant. Accuracy and truthfulness — We consider whether the information is inaccurate, misleading, incomplete, or omits important context. Where you believe information is incorrect, you should explain why and provide reliable supporting evidence. We assess accuracy based on the information provided with your request and cannot independently investigate disputed facts.

[note: the personal-data article is framed for "information about you" as a natural person ("Proof of identity (e.g. government-issued ID)"); the page text captured carries no wording about a business, brand, organisation or product. The reporting-content article's business-relevant channels are the trademark/counterfeit form and the "Safety or Legal concern" thumbs-down path; the phrase "prevent ChatGPT from relying on unreliable sources in future responses" is the only source-correction mechanism named.]

## Pull notes — mechanical only

- help.openai.com direct: HTTP 403 for the sitemap and articles (bot wall). Wayback `id_` copies returned gzip-compressed bodies; a first fetch without `--compressed` produced binary, the second with `--compressed` returned the HTML (53,791 and 58,924 bytes).
- CDX listing of help.openai.com/en/articles/* (3,000-row cap, collapse=urlkey) was pattern-searched for inaccur|report|remov|hallucin|defam|wrong; the two articles above and "12461090-blocking-and-reporting-on-the-sora-app" were the only matches. No article titled for businesses or brands reporting inaccurate answers was found in the listing.
