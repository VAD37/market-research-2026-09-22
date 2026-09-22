# Similarweb (aisearch.similarweb.com) — Zero-Click Marketing: Statistics on AI/Search Engine Traffic & Referrals

```yaml
source:          Similarweb (aisearch.similarweb.com blog)
url_or_doc_id:   https://aisearch.similarweb.com/blog/zero-click-marketing/
published:       2026-06-10
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            4
tier_reason:     table default for clickstream panel; some figures in this article are sourced from OTHER publishers (Pew Research, Cloudflare Radar, Google official, Jumpshot-era historical) rather than Similarweb's own panel — each figure below is labeled with its own attributed source, per the source's own words, not normalised to Similarweb
source_label:    vendor-reported
lane:            A
sub_market:      organic recommendation
engine:          Google (AI Overviews / AI Mode); ChatGPT (session/conversion detail); n/a for category rows
metric_kind:     traffic
supersedes:      none
captured:        section extract via fetch tool (AI-summarized from source HTML)
```

## Verbatim (as extracted, tables reconstructed from the fetch summary)

### Zero-Click Rates

| Metric | Figure | Date window | Population | Source/Method (as stated) |
|---|---|---|---|---|
| Overall zero-click rate | 68% | 2026 | Google searches | Similarweb clickstream panel |
| Zero-click rate (2016 baseline) | ~45% | 2016 | Google searches | Jumpshot clickstream panel |
| Zero-click rate (2019) | ~49% | 2019 | Google searches | Jumpshot clickstream panel |
| Zero-click rate (2020) | ~65% | 2020 | Google searches | Similarweb clickstream panel |
| Zero-click rate (2024) | ~60% | 2024 | Google searches | Datos clickstream panel |
| Mobile zero-click rate | 54.8% | 2026 | Mobile users | Similarweb clickstream panel |
| Desktop zero-click rate | 80% | 2026 | Desktop users | Similarweb clickstream panel |

### AI-Specific Traffic & Referral Data

| Metric | Figure | Date window | Population | Source/Method (as stated) |
|---|---|---|---|---|
| AI Overviews coverage | 20%+ | 2026 | Google searches | Google data |
| Click rate with AI Overview present | 8% | 2026 | Searches with AI Overview | Pew Research |
| Click rate without AI Overview | 15% | 2026 | Searches without AI Overview | Pew Research |
| Google AI Mode query share | 0.34% | Jan–Apr 2026 | All Google searches | Similarweb research data |
| Google AI Mode referral rate | 1.6–2.5% | 2026 | AI Mode queries | Similarweb data |
| Traditional Google referral rate | 17–19% | 2026 | Standard search | Similarweb data |
| AI platform traffic growth YoY | 76% | H2 2025 | Worldwide | Similarweb AI traffic data |
| ChatGPT avg. session duration | 15 minutes | Sept 2025 | US transactional sites | Similarweb Gen AI Landscape report |
| Google avg. session duration | 8 minutes | Sept 2025 | US transactional sites | Similarweb Gen AI Landscape report |
| ChatGPT conversion rate | 7% | Sept 2025 | US transactional sites | Similarweb Gen AI Landscape report |
| Google conversion rate | 5% | Sept 2025 | US transactional sites | Similarweb Gen AI Landscape report |
| ChatGPT pages per session | 12 | Sept 2025 | US transactional sites | Similarweb Gen AI Landscape report |
| Google pages per session | 9 | Sept 2025 | US transactional sites | Similarweb Gen AI Landscape report |
| Google AI Mode monthly users | 1 billion+ | I/O 2026 announcement | Global | Google official (company-stated, not Similarweb panel) |
| AI Mode queries growth | "doubling every quarter" | Q1–Q2 2026 | Global | Google I/O 2026 (company-stated) |
| ClaudeBot crawler traffic share | 20% | May 2026 | Global AI crawlers | Cloudflare Radar [note: crawler telemetry, not assistant usage/referral share — out of this cluster's scope, left as context only] |
| GPTBot crawler traffic share | ~10% | May 2026 | Global AI crawlers | Cloudflare Radar [note: same as above] |
| Repeat search rate increase | +7.2 percentage points | 2024–2026 | Google searchers | Similarweb clickstream panel |

### SERP Click Distribution Shifts (Paid vs. Organic) — context, not assistant share

| Category | Metric | Jan 2025 | Jan 2026 | Source |
|---|---|---|---|---|
| Headphones | Paid clicks share | 16% | 36% | Similarweb / Aleyda Solis analysis |
| Jeans | Paid clicks share | 18% | 34% | Similarweb / Aleyda Solis analysis |

### Methodology Notes (source's own statement)

"Similarweb's clickstream panel" is named as the primary data source, described as continuously tracking "the clicked-versus-zero-click split at the keyword level since 2019." Data collection combines panel-based clickstream measurement with public announcements and third-party research (Pew Research, Cloudflare Radar). No panel size or recruitment method stated in this article.

[note: extracted via WebFetch's AI-summarization; table rows above are as returned by that extraction, not copy-pasted from raw HTML markup.]

## Pull notes — mechanical only

- Access: plain fetch succeeded (200).
- This page mixes Similarweb's own clickstream figures with figures attributed to Pew Research, Cloudflare Radar and Google's own announcements — each row above keeps the source the article itself names, per the "conflicting figures sit side by side, never averaged" rule.
- The two Cloudflare Radar crawler-share rows (ClaudeBot, GPTBot) are crawl telemetry, not assistant usage/referral share — flagged, not claimed as this cluster's evidence; the crawler-telemetry cluster (P2-c2) owns that lane.
- The Google AI Mode 0.34%/1.6–2.5% figures here should be read against the Datos-sourced AI Mode share figures in `a-ppc-land-share-datos-q1-2026-2026-09-22.md`; the two do not agree and are kept side by side per the summary table, not averaged.
