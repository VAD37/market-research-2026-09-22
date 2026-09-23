# OtterlyAI — HTML vs Markdown GEO experiment, embedded images (re-pull)

```yaml
source:          OtterlyAI (otterly.ai) blog
url_or_doc_id:   https://otterly.ai/blog/geo-experiment-html-vs-markdown/
published:       2026-04-01 (last updated)
pull_date:       2026-09-23
pull_method:     fetch (curl, browser User-Agent) for the page HTML and each wp-content image URL
pull_purpose:    evidence about a number
tier:            5
tier_reason:     vendor-published case or experiment with n/dates/method stated; vendor measuring with its own product, no third-party replication — bias flagged (same as text pull)
source_label:    vendor-reported
lane:            E
sub_market:      organic recommendation
engine:          ChatGPT, Perplexity, Google AI Overviews named; AI crawlers
metric_kind:     visibility (citations); crawler visits
supersedes:      none — supplements e-case-otterly-html-vs-markdown-experiment-2026-09-23.md (text pull did not capture three embedded images; this pull retrieves them, one carries per-page citation counts not in the article's own text)
captured:        three images: one screenshot of a test HTML page, one Citations-dashboard screenshot (new figures), one screenshot of raw Markdown source
```

## Verbatim

Not applicable — image pull. Images filed at `docs/raw/img/e-case-otterly-html-vs-markdown-experiment-repull2-2026-09-23/`, transcribed in `docs/raw/e-case-otterly-html-vs-markdown-experiment-repull2-2026-09-23-img-2026-09-23.md`.

[image: docs/raw/img/e-case-otterly-html-vs-markdown-experiment-repull2-2026-09-23/01-otterly-marketing-page-unrelated.jpg]
[image: docs/raw/img/e-case-otterly-html-vs-markdown-experiment-repull2-2026-09-23/02-citations-dashboard-html-vs-md-pages.jpeg]
[image: docs/raw/img/e-case-otterly-html-vs-markdown-experiment-repull2-2026-09-23/03-markdown-version-of-html-page-source.jpg]

## Pull notes — mechanical only

- Page HTML fetched with a browser User-Agent (curl), HTTP 200; three images found via `data-src`, fetched directly, all HTTP 200 (72,665 B / 37,570 B / 157,218 B). Otterly logo, brand icon and unrelated related-post thumbnails not saved — decorative.
- Image 01 ("HTML-vs-Markdown-versions...jpg") renders as a full-page screenshot of an OtterlyAI marketing landing page ("Best AI Search Optimization Software in Comparison: Why OtterlyAI Drives 132% More Citations"), not a chart — kept because its filename and position in the article associate it with the "existing HTML page" used as a test subject (`https://otterly.ai/enterprise-ai-search-visibility-tool`, per the article's own Scenario A description), but the screenshot itself carries no experiment figure.
