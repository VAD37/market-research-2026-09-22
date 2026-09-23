# Google — "Google Marketing Live 2026: Search ads" blog post — media inventory (ad-format examples are videos, not images)

```yaml
source:          Google (The Keyword blog, Ads & Commerce)
url_or_doc_id:   https://blog.google/products/ads-commerce/google-marketing-live-search-ads/
published:       2026-05-20 (as recorded in the substitute; the page's TTS audio asset is stamped 2026_05_20)
pull_date:       2026-09-23
pull_method:     fetch (curl, HTTP 200, static HTML) — media URLs read from the HTML
pull_purpose:    evidence about a number
tier:            3
tier_reason:     platform primary — table default
source_label:    company-stated
lane:            B
sub_market:      paid placement
engine:          Google AI Mode, Google Search (AI Overviews)
metric_kind:     none
supersedes:      b-google-gml2026-search-ads-2026-09-22.md (text complete; ad-format example media not captured)
captured:        media inventory only — the six ad-format example assets and the page's static images; body text is in the substitute and not duplicated
```

## Verbatim

Ad-format example media on the page (all `video/mp4`, sizes from HTTP HEAD, 2026-09-23):

| Section caption in the substitute | Asset URL | Bytes |
|---|---|---|
| "Conversational Discovery Ads" | https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/Conversational_Discovery.mp4 | 8,348,170 |
| "Highlighted Answers" | https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/Highlighted_Answers_1.mp4 | 8,590,967 |
| "AI-powered Shopping ads" | https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/AI-powered_Shopping_ads.mp4 | 4,232,087 |
| "Business Agent for Leads" | https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/Business_Agent_for_Leads.mp4 | 11,386,373 |
| "Promotional bundling + native checkout" | https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/Direct_Offers_1_ctwprdX.mp4 | 22,444,793 |
| "Travel deals" | https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/Direct_Offers_2_winReP3.mp4 | 15,363,045 |

[note: image not saved — the six ad-format examples are mp4 videos (≈70 MB in total), not chart or table images; URLs recorded here and in docs/raw/img/INDEX.csv, files not downloaded]

Static images in the HTML: the post's header card (`images/Search_ZAu2ZP1.width-*.format-webp.webp`, alt "\"Google Marketing Live\" text with the YouTube logo, Google G, and a 3-D sparkle"), the social card (`images/GML_Search_social.width-1300.png`) and related-story thumbnails — decorative, not saved.

## Pull notes — mechanical only

- curl with the bot user agent: HTTP 200 (301,104 bytes); the ad-format examples are `<video>` sources on `storage.googleapis.com`, which is why the 2026-09-22 text pull recorded captions but no images. No wall; the bypass extension was not involved.
- Sizes from `curl -I` on each asset (HTTP 200, `video/mp4`).
