# Google Search Central — AI optimization guide (explicit llms.txt and schema.org statement)

```yaml
source:          Google Search Central (developers.google.com)
url_or_doc_id:   https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
published:       "Last updated 2026-07-10 UTC" (stated at foot of page)
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary, own guidance page, explicitly dated
source_label:    company-stated
lane:            D
sub_market:      organic recommendation
engine:          Google — AI Overviews, AI Mode, generative AI features in Google Search
metric_kind:     none
supersedes:      none
captured:        full page
```

## Verbatim

Page context: navigation confirms this page sits under Google Search Central > Documentation, alongside the existing "AI features and your website" page already in `raw/` (`a-google-ai-features-guidance-2026-09-22.md`) and the full "Structured data" documentation tree (Understand how structured data works, Structured data policies, Generate structured data with JavaScript, All structured data features, Structured data carousels (beta), etc. — listed in the page's own navigation sidebar).

Section: "Next steps: what to focus on"

"As you continue working on your website, remember that plenty of content thrives in Google Search (including generative AI experiences) without any overt SEO at all, and you don't need to accomplish everything at once. Here's how to prioritize: focus on strengthening your site's fundamentals, then build on that foundation as capacity allows. As search evolves to let AI do more, focus on the fundamentals that help both traditional and AI-powered search."

"There's a lot of noise on the internet around generative AI and Google Search. Here are a few things you can ignore for Google Search:"

"**LLMS.txt files and other "special" markup**: You don't need to create new machine readable files, AI text files, markup, or Markdown to appear in Google Search (including its generative AI capabilities), as Google Search itself doesn't use them. Note that Google may discover, crawl, and index many kinds of files in addition to HTML on a website: this doesn't mean that the file is treated in a special way. It's completely fine if you decide to create and maintain LLMS.txt files (or other similar files) for other services or systems that use these files. Doing so will neither harm nor help your site's visibility or rankings in Google Search, as Google Search ignores them."

"**Overfocusing on structured data**: Structured data isn't required for generative AI search, and there's no special schema.org markup you need to add. However, it's a good idea to continue using it as part of your overall SEO strategy [continues into a general recommendation to keep existing structured data, text truncated by this pull's extraction method beyond this point]."

"...you can ignore tactics like "chunking" content, creating unnecessary AI text files (like llms.txt), or pursuing inauthentic mentions."

"**Monitor visibility in Search Console**: Use the Generative AI performance report to see how your content is performing in generative AI features on Google Search."

Footer: "Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates. Last updated 2026-07-10 UTC."

## Pull notes — mechanical only

- Loaded via `curl` (no browser extension needed; static Google Developers documentation page, no login gate, no JS-rendering wall for the body text). Page includes a `schema.org`-typed `BreadcrumbList` JSON-LD block in its own `<head>` — Google's own page is itself marked up with schema.org, illustrating continued first-party use of the vocabulary even on a page that tells site owners not to add *more* of it for AI-specific purposes.
- **This is the single most explicit and most current statement found in this cluster on whether a priority-1 engine reads the llms.txt artefact**: "Google Search itself doesn't use them" / "Google Search ignores them" — twice-stated, unambiguous, dated 2026-07-10 (inside the one-quarter staleness window as of this 2026-09-22 pull). It supersedes the softer, earlier-worded "You don't need to create new machine readable files, AI text files, or markup to appear in these features. There's also no special schema.org structured data that you need to add" already captured (undated) in `a-google-ai-features-guidance-2026-09-22.md` — same substantive claim, this page states it more directly and gives it an explicit last-updated date.
- On schema.org specifically, the statement is narrower than on llms.txt: Google says no *additional/special* schema.org markup is needed for generative AI features, not that schema.org markup in general is ignored — the same page's navigation sidebar links a full, separately-maintained "Structured data" documentation tree, and the "Overfocusing on structured data" heading explicitly recommends *continuing* to use structured data "as part of your overall SEO strategy." This is a "do not over-invest for AI specifically" statement, not a "does not read schema.org" statement — recorded as a distinct, narrower finding from the llms.txt statement in the census.
- Page text was extracted via `sed`-based HTML tag-stripping (not a JS-rendering tool); the "Overfocusing on structured data" bullet's continuation past "as part of your overall SEO strategy" was not fully captured in this extraction pass — marked `[note: bullet continuation past this point not fully captured by this pull's text-extraction method]`. The core sentence ("no special schema.org markup you need to add") is intact and unambiguous.
- No mention of product feeds, Merchant Center, or any per-engine (ChatGPT, Claude, Perplexity, Copilot, Amazon) comparison on this page — Google-only, organic-lane guidance.
