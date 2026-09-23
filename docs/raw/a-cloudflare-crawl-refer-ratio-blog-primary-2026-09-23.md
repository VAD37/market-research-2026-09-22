# Cloudflare — "AI search crawl-to-refer ratio on Radar" (2025-07-01) — chart images saved

```yaml
source:          Cloudflare (blog.cloudflare.com; authors David Belson, Sam Rhea)
url_or_doc_id:   https://blog.cloudflare.com/ai-search-crawl-refer-ratio-on-radar/
published:       2025-07-01 (as recorded in the substitute; page dateline)
pull_date:       2026-09-23
pull_method:     fetch (curl, HTTP 200); images by curl from blog.cloudflare.com/_emdash/api/media/file/
pull_purpose:    evidence about a number
tier:            4
tier_reason:     infrastructure telemetry (Cloudflare Radar) with the metric definition published on the page; as graded in the substitute
source_label:    analyst-derived
lane:            A
sub_market:      n/a
engine:          multiple — Anthropic (Claude), OpenAI, Perplexity, Microsoft, Yandex, Google, ByteDance, Baidu, DuckDuckGo, Mistral (as in the substitute)
metric_kind:     traffic
supersedes:      a-cloudflare-crawl-refer-ratio-blog-2026-09-22.md (text complete; referral and crawling time-series charts not captured)
captured:        the twelve in-body images (ratio table, Radar time-series charts, referral-share charts, crawler-activity charts, bot cards); body text is in the substitute and not duplicated
```

## Verbatim

In-body images, in page order, with the sentence that follows each on the page (alt text on the page is the generic "BLOG-2836 Image N"):

- [image: docs/raw/img/a-cloudflare-crawl-refer-ratio-blog-primary-2026-09-23/01-blog-2836-image-1.png] — followed by "When a user clicks on a link on a website or application, the client will often send a Referer: header…"
- [image: docs/raw/img/a-cloudflare-crawl-refer-ratio-blog-primary-2026-09-23/02-blog-2836-image-2.png] — followed by "Observations — Reviewing the ratios — The new metric is presented as a simple table, comparing the number…"
- [image: docs/raw/img/a-cloudflare-crawl-refer-ratio-blog-primary-2026-09-23/03-blog-2836-image-3.png] — followed by "Of course, due in part to changes in crawling patterns, these ratios will change over time. The table…"
- [image: docs/raw/img/a-cloudflare-crawl-refer-ratio-blog-primary-2026-09-23/04-blog-2836-image-4.png] — (no caption text; sits between the ratio-table paragraphs and the Data Explorer paragraph)
- [image: docs/raw/img/a-cloudflare-crawl-refer-ratio-blog-primary-2026-09-23/05-blog-2836-image-5.png] — followed by "Radar’s Data Explorer includes a time series view of how these ratios change over time, such as in…"
- [image: docs/raw/img/a-cloudflare-crawl-refer-ratio-blog-primary-2026-09-23/06-blog-2836-image-7.png] — followed by "Clear diurnal patterns are also visible in the referral request shares of other search platforms…" (the page numbers its images 1–13 with no "Image 6")
- [image: docs/raw/img/a-cloudflare-crawl-refer-ratio-blog-primary-2026-09-23/07-blog-2836-image-8.png] — followed by "Throughout June, the share of traffic referred by AI platforms was significantly lower, even in aggregate…"
- [image: docs/raw/img/a-cloudflare-crawl-refer-ratio-blog-primary-2026-09-23/08-blog-2836-image-9.png] — followed by "Changes in crawling traffic — As noted above, the change in ratio values over time can be driven by…"
- [image: docs/raw/img/a-cloudflare-crawl-refer-ratio-blog-primary-2026-09-23/09-blog-2836-image-10.png] — followed by "In addition, it appears that OpenAI’s GPTBot saw multiple periods where little-to-no crawling activity…"
- [image: docs/raw/img/a-cloudflare-crawl-refer-ratio-blog-primary-2026-09-23/10-blog-2836-image-11.png] — followed by "What this means for content providers — These ratios directly impact the viability of content publication…"
- [image: docs/raw/img/a-cloudflare-crawl-refer-ratio-blog-primary-2026-09-23/11-blog-2836-image-12.png] — followed by "Clicking on a bot name within a card brings up a bot-specific page that includes metadata about the…"
- [image: docs/raw/img/a-cloudflare-crawl-refer-ratio-blog-primary-2026-09-23/12-blog-2836-image-13.png] — last in-body image (end of post)

Hero image ("BLOG-2836 Hero Image") and author photos skipped as decorative.

## Pull notes — mechanical only

- curl HTTP 200 (327,170 bytes); the page's `<img>` elements wrap the originals in an `/_image?href=…` resizer; the original `_emdash/api/media/file/<id>.png` URLs were extracted and fetched directly (HTTP 200, 51,612–133,898 bytes each). Rows in `docs/raw/img/INDEX.csv`. No wall; the bypass extension was not involved.
- Which images are charts, tables or product screenshots is not judged here (IMG-1).
