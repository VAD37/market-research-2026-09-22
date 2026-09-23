# OtterlyAI — llms.txt experiment, embedded chart/dashboard images (re-pull)

```yaml
source:          OtterlyAI (otterly.ai) blog
url_or_doc_id:   https://otterly.ai/blog/the-llms-txt-experiment/
published:       2026-02-05 (last updated)
pull_date:       2026-09-23
pull_method:     fetch (curl, browser User-Agent) for the page HTML and each wp-content image URL
pull_purpose:    evidence about a number
tier:            5
tier_reason:     vendor-published case or experiment with n/dates/method stated; vendor measuring with its own product, no third-party replication — bias flagged (same as text pull)
source_label:    vendor-reported
lane:            E
sub_market:      organic recommendation
engine:          AI / LLM user agents named per-bot in image 03/04 (ChatGPT-User, OpenAI Search Crawler/OAI-SearchBot, Perplexity AI Crawler, Claude On-Demand Fetcher, Mistral On-Demand Fetcher, GoogleOther/R&D Fetcher, Gemini Deep Research Fetcher, Google NotebookLM Fetcher)
metric_kind:     crawler visits
supersedes:      none — supplements e-case-otterly-llms-txt-experiment-2026-09-23.md (text pull did not capture the four embedded images; this pull retrieves them, and they carry a per-bot breakdown and an agent-vs-human ratio not present in the article's own text)
captured:        four images (one bar chart, one KPI-tile+line+pie dashboard screenshot, two per-URL bot-breakdown widgets)
```

## Verbatim

Not applicable — image pull. Images filed at `docs/raw/img/e-case-otterly-llms-txt-experiment-repull2-2026-09-23/`, transcribed in `docs/raw/e-case-otterly-llms-txt-experiment-repull2-2026-09-23-img-2026-09-23.md`.

[image: docs/raw/img/e-case-otterly-llms-txt-experiment-repull2-2026-09-23/01-ai-crawler-bot-visits-by-page-type.png]
[image: docs/raw/img/e-case-otterly-llms-txt-experiment-repull2-2026-09-23/02-agents-page-visits-overview-dashboard.png]
[image: docs/raw/img/e-case-otterly-llms-txt-experiment-repull2-2026-09-23/03-llmstxt-bot-breakdown.png]
[image: docs/raw/img/e-case-otterly-llms-txt-experiment-repull2-2026-09-23/04-robotstxt-bot-breakdown.png]

## Pull notes — mechanical only

- Page HTML fetched with a browser User-Agent (curl), HTTP 200; four data-carrying images found via `data-src`/`data-srcset`, fetched directly at full or near-full resolution, all HTTP 200 (44,653 B / 142,598 B / 9,636 B / 18,899 B). Otterly logo, brand icon and unrelated related-post thumbnails not saved — decorative.
