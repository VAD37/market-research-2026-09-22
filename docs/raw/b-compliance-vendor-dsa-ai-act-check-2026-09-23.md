# Compliance / disclosure tooling for conversational ad surfaces — vendor site searches (negative check)

```yaml
source:          TrustArc, OneTrust, Didomi, Usercentrics — own-site search pages; Mojeek web search
url_or_doc_id:   https://trustarc.com/?s=digital+services+act ; https://www.onetrust.com/?s=digital+services+act ; https://www.didomi.io/?s=digital+services+act ; https://usercentrics.com/?s=digital+services+act ; https://www.mojeek.com/search?q=Microsoft+%22publisher+content+marketplace%22+Copilot
published:       search-result pages generated at pull time
pull_date:       2026-09-23
pull_method:     fetch (curl, User-Agent "market-research-bot contact: research@example.invalid"; HTML tag-stripped; grep for "services act", "DSA", "Article 39", "ad repositor")
pull_purpose:    evidence about category noise — records a negative check
tier:            3
tier_reason:     vendors' own site-search output; carries no number
source_label:    vendor-reported
lane:            B
sub_market:      paid placement (DSA Art. 39 repository and AI Act Art. 50 labelling tooling)
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        matching result titles and snippets verbatim; CAPTCHA page text
```

## Verbatim

trustarc.com search "digital services act":

> Search results for digital services act
> The Digital Services Act: What to Expect
> In addition to the Digital Market Act, the European Union's Digital Services Act helps create a safer and more open digital space in the EU.

usercentrics.com search "digital services act":

> Digital Services Act Package: Affects On US Businesses — Usercentrics explains how the Digital Services Act and Digital Markets Act will affect US businesses' digital operations, improve competition...
> DMA vs DSA - Similarities and Differences - Usercentrics — What are the key differences between the Digital Markets Act and the Digital Services Act? Usercentrics explores the Digital Services Act...
> [page footer widget:] Ask Claude · Ask Chatgpt · Ask Gemini · Ask Copilot · Ask Perplexity

onetrust.com search "digital services act": [note: HTTP 200, 261,302 bytes; grep for "services act", "DSA", "Article 39", "ad repositor" returned no result line — the page is script-rendered]

didomi.io search "digital services act": [note: HTTP 200, 267,607 bytes; same grep, no result line — script-rendered]

mojeek.com search:

> Captcha
> JavaScript is required to complete this challenge. Please enable it and reload the page.

## Pull notes — mechanical only

- Grep for "Article 39", "ad repositor", "VLOSE" and "conversational" across the four vendor search pages returns no hit. The two vendors with readable results (TrustArc, Usercentrics) publish DSA explainers only; no product page for an Art. 39 ad repository, for ad labelling inside AI answers, or for AI Act Art. 50 marking was surfaced.
- IAB Europe and IAB Tech Lab pages were checked separately (`raw/b-iab-europe-dsa-ads-transparency-2026-09-23.md`): scope is DSA Art. 26 OpenRTB fields, not Art. 39 repositories.
- Search engines walled this session: Mojeek JavaScript CAPTCHA (above); DuckDuckGo html 403; WebSearch tool exhausted. The vendor set is therefore the four named privacy/consent vendors plus the IAB bodies; it is not a census.
- Nothing was submitted; no CAPTCHA was attempted.
