# Franchise and restaurant trade press — site-search probes for "ChatGPT" (franchising.com, Franchise Times, QSR Magazine, Restaurant Business, 1851 Franchise), and G2 / Capterra category pages to plain fetch

```yaml
source:          site search endpoints of franchising.com, franchisetimes.com, qsrmagazine.com, restaurantbusinessonline.com, 1851franchise.com; g2.com and capterra.com category pages
url_or_doc_id:   https://www.franchising.com/search/?q=ChatGPT ; https://www.franchisetimes.com/search/?q=ChatGPT ; https://www.qsrmagazine.com/?s=ChatGPT ; https://www.restaurantbusinessonline.com/search?keys=ChatGPT ; https://1851franchise.com/search?q=ChatGPT ; https://www.g2.com/categories/answer-engine-optimization-aeo ; https://www.capterra.com/ai-search-visibility-software/
published:       n/a — access probes
pull_date:       2026-09-23
pull_method:     fetch (curl, User-Agent "market-research-bot contact: research@example.invalid"); HTML stripped by script where reached
pull_purpose:    evidence about category noise (channel reachability); no number carried
tier:            n/a — access log
tier_reason:     no content pulled that carries a figure
source_label:    n/a
lane:            F
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        HTTP status, body size, and whether a result list rendered
```

## Results

| Channel | URL | HTTP | Bytes | What rendered |
|---|---|---|---|---|
| franchising.com site search | /search/?q=ChatGPT | 200 | 187,730 | Page headings "Franchise Search »", "Subscribe to our Newsletters"; no article result list in the static HTML; no anchor text containing "ChatGPT" or "AI" |
| Franchise Times site search | /search/?q=ChatGPT | 429 | 62 | rate-limited on first request |
| QSR Magazine site search | /?s=ChatGPT | 403 | 5,540 | bot wall |
| Restaurant Business site search | /search?keys=ChatGPT | 200 | 117,268 | 198 text lines; 0 lines matching ChatGPT / AI search / AI Overviews / Gemini / Perplexity — result list script-rendered or empty |
| 1851 Franchise site search | /search?q=ChatGPT | 200 | 15,919 | 77 text lines; one line matching "AI": "DOG TRAINING ELITE" (brand name in a nav block); no result list |
| Localogy home | / | 200 | 35,861 | 127 text lines, none matching AI / ChatGPT / LLM / agent |
| G2 AEO category | /categories/answer-engine-optimization-aeo | 403 | 1,704 | DataDome challenge (as on 2026-09-22) — history taken from Wayback instead, e-wayback-g2-capterra-category-counts-2026-09-23.md |
| Capterra AI Search Visibility | /ai-search-visibility-software/ | 403 | 5,604 | Cloudflare interstitial |

## Pull notes — mechanical only

- One request per channel; no retry; no CAPTCHA attempted; no login.
- Franchise trade press for S8 / S5-adjacent signals therefore reads `unknown — checked franchising.com, franchisetimes.com (429), qsrmagazine.com (403), restaurantbusinessonline.com, 1851franchise.com 2026-09-23` for the local vertical.
