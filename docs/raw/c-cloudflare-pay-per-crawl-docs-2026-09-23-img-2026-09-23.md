# Cloudflare — Pay Per Crawl developer docs — image read (IMG-1b)

```yaml
source:          Cloudflare Docs (developers.cloudflare.com), "What is Pay Per Crawl?" — one in-body image
url_or_doc_id:   https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl/
published:       page "Last updated Jul 28, 2026" (per source raw file)
pull_date:       2026-09-23
pull_method:     image read (IMG-1b) — Read tool on the PNG saved by curl in the source pull
pull_purpose:    evidence about a number
tier:            3
tier_reason:     inherits c-cloudflare-pay-per-crawl-docs-2026-09-23.md
source_label:    vendor-reported (diagram carries no number; label as the page's author)
lane:            C
sub_market:      n/a — publisher / sell-side monetisation
engine:          n/a
metric_kind:     none
supersedes:      none — reads the image referenced in c-cloudflare-pay-per-crawl-docs-2026-09-23.md
captured:        one image, transcribed in full
```

## 01-pay-per-crawl-components

image: docs/raw/img/c-cloudflare-pay-per-crawl-docs-2026-09-23/01-pay-per-crawl-components.png (2400 × 1122 px)

Chart type: architecture / component diagram, three dashed regions, boxes and arrows. No axes, no numbers.

Title printed (bottom-left, capitals): "HOW PAY PER CRAWL WORKS". Bottom-right: Cloudflare logo and wordmark "CLOUDFLARE".

Regions and boxes, left to right:

- Left dashed region (blue, crawler icon): "AI Crawler" (top box) · "Operator" (bottom box).
- Middle dashed region labelled "Cloudflare" (orange), top row: a grouped box holding "WAF: Custom Rules" and, joined by a "+" sign, "AI Audit: Crawler Blocking" → "Bot Solutions" → "AI Audit: Pay Per Crawl" → (exits the region to) "Website Content".
- Middle region, bottom row: "AI Crawler Owner Cloudflare Account" → "Pay Per Crawl Payment Facilitation" ← "Website Owner Cloudflare Account" ← "Owner".
- A downward arrow joins "AI Audit: Pay Per Crawl" (top row) to "Pay Per Crawl Payment Facilitation" (bottom row).
- Right dashed region (blue, browser-window icon): "Website Content" (top box) · "Owner" (bottom box).

Arrows: "AI Crawler" → grouped WAF / Crawler Blocking box; "Operator" → "AI Crawler Owner Cloudflare Account".

Legend: none. Footnote / source line: none. Figures printed as text: none (no price, no 402 code on the image).

Text cross-check: no figure on the image. The text's "HTTP 402 Payment Required", "$0.001 USD per crawl" minimum and "Merchant of Record" do not appear on the diagram.
