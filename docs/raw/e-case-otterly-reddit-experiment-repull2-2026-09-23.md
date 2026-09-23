# OtterlyAI — Reddit GEO engagement experiment, embedded chart images (re-pull)

```yaml
source:          OtterlyAI (otterly.ai) blog
url_or_doc_id:   https://otterly.ai/blog/reddit-geo-ai-search-citations/
published:       2026-06-19 (last updated)
pull_date:       2026-09-23
pull_method:     fetch (curl, browser User-Agent) for the page HTML and each wp-content image URL
pull_purpose:    evidence about a number
tier:            5
tier_reason:     vendor-published case or experiment with n/dates/method stated; vendor measuring with its own product, no third-party replication — bias flagged (same as text pull)
source_label:    vendor-reported
lane:            E
sub_market:      organic recommendation
engine:          ChatGPT, Google AI Overviews, Google AI Mode, Perplexity, Gemini, Microsoft Copilot
metric_kind:     visibility (AI citations); Google rankings
supersedes:      none — supplements e-case-otterly-reddit-experiment-2026-09-23.md (text pull did not capture in-article chart images; this pull retrieves four)
captured:        four in-article chart/screenshot images (of the WordPress "image-2" through "image-5" set); cover image and unrelated related-post thumbnails not saved (decorative)
```

## Verbatim

Not applicable — image pull. Images filed at `docs/raw/img/e-case-otterly-reddit-experiment-repull2-2026-09-23/`, transcribed in `docs/raw/e-case-otterly-reddit-experiment-repull2-2026-09-23-img-2026-09-23.md`.

[image: docs/raw/img/e-case-otterly-reddit-experiment-repull2-2026-09-23/01-reddit-mod-insights-dashboard.png]
[image: docs/raw/img/e-case-otterly-reddit-experiment-repull2-2026-09-23/02-top-social-media-channels-cited-ai-search.png]
[image: docs/raw/img/e-case-otterly-reddit-experiment-repull2-2026-09-23/03-does-engagement-drive-ai-citations-methodology.png]
[image: docs/raw/img/e-case-otterly-reddit-experiment-repull2-2026-09-23/04-organic-search-version-a-vs-b.png]

## Pull notes — mechanical only

- Page HTML fetched with a browser User-Agent (curl), HTTP 200; images are WordPress lazy-load (`data-src`), full-resolution URLs (`.../uploads/2026/06/image-N.png`, no size suffix) extracted from `data-srcset` and fetched directly, all HTTP 200.
- Four images saved (`image-2.png` 36,893 B, `image-3.png` 290,166 B, `image-4.png` 408,393 B, `image-5.png` 758,340 B, as served). Cover photo (`GEO-Experiment-Reddit-Citation-Experiment-2-1024x777.jpg`), social-share image (`Reddit-OtterlyAI-1024x1024.jpg`) and related-post thumbnails not saved — decorative, no data.
