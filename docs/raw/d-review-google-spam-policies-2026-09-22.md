# Google Search — spam policies (scaled content abuse) and reviews guidance

```yaml
source:          Google (Google Search Central developer documentation)
url_or_doc_id:   https://developers.google.com/search/docs/essentials/spam-policies ; https://developers.google.com/search/docs/fundamentals/creating-helpful-content
published:       spam-policies page last-updated 2026-08-28 UTC (per page's own timestamp); creating-helpful-content page last-updated 2025-12-10 UTC (per page's own timestamp)
pull_date:       2026-09-22
pull_method:     fetch (WebFetch)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary, own documentation
source_label:    company-stated
lane:            D
sub_market:      organic recommendation
engine:          Google Search (the spam-policies page governs Google Search generally, which per this repo's Pass 2 pulls includes AI Overviews and AI Mode as surfaces built on the same index and ranking systems; the page does not itself distinguish AI-surface ranking from classic web ranking)
metric_kind:     none
supersedes:      none
captured:        the "Scaled content abuse" definition and examples from the spam-policies page; the one product-review-relevant sentence located on the creating-helpful-content page. Both captured via WebFetch (a tool that converts the page to markdown and answers a prompt against it — see pull notes for what this means for verbatim fidelity)
technique:       review and listicle manufacture
models_tested:   n/a
date_window:     n/a
measured_effect: no — this is a policy page, not a measurement
vertical:        none named — the policy applies to all content categories indexed by Google Search
```

## Verbatim

### "Scaled content abuse" (spam-policies page)

Definition, quoted by the fetch tool as verbatim page text:

"Scaled content abuse is when many pages are generated for the primary purpose of manipulating search rankings and not helping users."

Examples listed under this policy, quoted by the fetch tool as verbatim page text:

"Using generative AI tools or other similar tools to generate many pages without adding value for users"

"Scraping feeds, search results, or other content to generate many pages (including through automated transformations like synonymizing, translating, or other obfuscation techniques), where little value is provided to users"

"Stitching or combining content from different web pages without adding value"

"Creating multiple sites with the intent of hiding the scaled nature of the content"

"Creating many pages where the content makes little or no sense to a reader but contains search keywords"

[note: the fetch tool reported the page "does not contain dedicated sections on 'review abuse' or 'content farms'" as separately named policies — scaled content abuse, as quoted above, is the closest named policy to mass-produced listicle/comparison content, and does not use the words "review", "listicle", or "best-of" anywhere in what was captured]

### Product-review guidance (creating-helpful-content page)

The one sentence the fetch tool located specifically about review content, quoted as verbatim page text:

"For product reviews, it can build trust with readers when they understand the number of products that were tested, what the test results were, and how the tests were conducted"

Per the fetch tool's summary, the page's overall framing is that content should be "people-first" (created to help actual visitors) rather than "search engine-first" (created primarily to manipulate rankings), and it separately warns against content "summarizing others' work without substantial value addition" — stated by the tool to apply broadly rather than as a named rule specific to listicles or comparison pages.

## Pull notes — mechanical only

- Both pages were retrieved via `WebFetch`, which fetches the page, converts it to markdown, and runs a prompt against the converted content with a smaller model before returning a result — this is not a byte-for-byte HTML capture. The quoted strings above are reported by that tool as direct quotes from the page (the tool was explicitly instructed to "quote verbatim" and returned text inside quotation marks); they are recorded here as given, but this pull method carries a layer of processing that the browser-extension pulls elsewhere in this cluster do not.
- A companion, more specifically-titled page for product-review content — guessed URLs `developers.google.com/search/docs/appearance/writing-high-quality-reviews` and `developers.google.com/search/docs/appearance/product-reviews` — both returned HTTP 404. The correct current path for Google's dedicated product-review guidance (if one exists as of 2026-09-22) was not located within this task's time budget. `unknown — checked the two guessed URLs above via WebFetch only, 2026-09-22`.
- This pull did not check whether AI Overviews or AI Mode apply the "scaled content abuse" spam policy identically to classic web results, or whether either surface has a separate, AI-specific content-abuse policy naming listicles or reviews. `unknown — checked developers.google.com/search/docs/essentials/spam-policies and .../fundamentals/creating-helpful-content only, 2026-09-22`.
