# Measured-by-us — /llms.txt on 19 multi-location and franchise brand domains

```yaml
source:          our own HTTP checks against 19 multi-location brand domains (hotels, QSR, fitness, pharmacy, home services, dental, senior care, salons, auto service)
url_or_doc_id:   https://<domain>/llms.txt for: www.choicehotels.com, www.wyndhamhotels.com, www.mcdonalds.com, www.subway.com, www.planetfitness.com, www.anytimefitness.com, www.walgreens.com, www.cvs.com, www.servpro.com, www.ziggis.com, www.aspendental.com, www.heartlanddental.com, www.homeinstead.com, www.regis.com, www.marriott.com, www.hilton.com, www.dominos.com, www.jiffylube.com, www.greatclips.com
published:       undated — live domain checks
pull_date:       2026-09-23
pull_method:     fetch (curl -s -L, browser User-Agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36", redirects followed, 20 s timeout); HTTP status, Content-Type and first 160 bytes of body recorded
pull_purpose:    evidence about a number
tier:            1
tier_reason:     table default — measured-by-us per demand-signals.md S12
source_label:    measured-by-us
lane:            F
sub_market:      organic recommendation
engine:          n/a — artifact readable by any crawler naming itself
metric_kind:     none
supersedes:      none
captured:        HTTP status, Content-Type and first ~160 characters per domain; full bodies not captured
```

prompt_set: n/a — not a panel run
runs_n: 19 domains checked, one request each
surface: n/a — HTTP artifact check
region: n/a — single unauthenticated check per domain from one host

## Query — verbatim

`curl -s -L --max-time 20 -A "<browser UA>" -o <file> -w '%{http_code} %{content_type}' https://<domain>/llms.txt`

## Results

| Domain | Brand, sector | HTTP | Content-Type | Body first bytes (verbatim, truncated) | Read |
|---|---|---|---|---|---|
| www.choicehotels.com | Choice Hotels, hotels | 000 (no response within 20 s) | — | — | not reached |
| www.wyndhamhotels.com | Wyndham Hotels & Resorts, hotels | 200 | text/plain; charset=UTF-8 | `# WyndhamHotels.com llms.txt  *Purpose: A conversational, markdown-style llms.txt to help AI systems understand Wyndham Hotels & Resorts and accurately guide us` | genuine llms.txt |
| www.mcdonalds.com | McDonald's, QSR | 403 | text/html | Akamai "Access Denied" | blocked |
| www.subway.com | Subway, QSR | 404 | text/html | XHTML 404 page | absent |
| www.planetfitness.com | Planet Fitness, fitness | 403 | text/html | Cloudflare "Just a moment..." | blocked |
| www.anytimefitness.com | Anytime Fitness, fitness franchise | 200 | text/plain; charset=utf-8 | `# Anytime Fitness # Version: 1.0 # Last-Modified: 2025-10-24 # Update-Cadence: quarterly  >  Anytime Fitness is a global co-ed gym franchise with 24/7 access, p` | genuine llms.txt |
| www.walgreens.com | Walgreens, pharmacy | 200 | text/html; charset=utf-8 | HTML page (`<!DOCTYPE html> … ruxitagentjs`) | soft 200, not llms.txt |
| www.cvs.com | CVS, pharmacy | 403 | text/html | Akamai "Access Denied" | blocked |
| www.servpro.com | SERVPRO, home services franchise | 404 | text/html; charset=utf-8 | HTML 404 | absent |
| www.ziggis.com | Ziggi's Coffee, coffee franchise | 000 (no response) | — | — | not reached |
| www.aspendental.com | Aspen Dental, dental | 403 | text/html | HTML 403 | blocked |
| www.heartlanddental.com | Heartland Dental, dental | 404 | text/html | HTML 404 | absent |
| www.homeinstead.com | Home Instead, senior care franchise | 404 | text/html; charset=utf-8 | HTML 404 | absent |
| www.regis.com | Regis (Supercuts), salons | 000 (no response) | — | — | not reached |
| www.marriott.com | Marriott, hotels | 404 | text/html; charset=utf-8 | HTML 404 | absent |
| www.hilton.com | Hilton, hotels | 404 | text/html; charset=iso-8859-1 | "Not Found" | absent |
| www.dominos.com | Domino's, QSR franchise | 200 | text/html; charset=utf-8 | HTML page (`<title>Domino's H…`) | soft 200, not llms.txt |
| www.jiffylube.com | Jiffy Lube, auto service franchise | 404 | text/html; charset=utf-8 | Next.js 404 | absent |
| www.greatclips.com | Great Clips, salons franchise | 403 | text/html; charset=UTF-8 | HTML 403 | blocked |

Tally: genuine llms.txt 2 of 19 (Wyndham, Anytime Fitness); absent (404) 8; blocked (403) 5; soft-200 HTML 2; no response 3. Of the 16 domains that answered, 2 serve a genuine file.

## Pull notes — mechanical only

- One request per domain; no retry on the three timeouts (Choice Hotels, Ziggi's, Regis). ziggis.com also returned HTTP 403 on its home page to a later plain fetch and a TLS "unrecognized name" error on www.ziggis.com/about-us/.
- "Soft 200": HTTP 200 with an HTML body — the site serves its front page or a template for unknown paths; not counted as an llms.txt.
- No login, no form.
