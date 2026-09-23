# Image transcription — OtterlyAI llms.txt experiment, four dashboard/chart images

```yaml
source:          OtterlyAI (otterly.ai) blog — image transcription of docs/raw/img/e-case-otterly-llms-txt-experiment-repull2-2026-09-23/
url_or_doc_id:   https://otterly.ai/blog/the-llms-txt-experiment/
published:       2026-02-05 (last updated)
pull_date:       2026-09-23
pull_method:     fetch (image read by agent, Read tool on saved PNGs)
pull_purpose:    evidence about a number
tier:            5
tier_reason:     same as the pull this transcribes — vendor-published, no third-party replication
source_label:    vendor-reported
lane:            E
sub_market:      organic recommendation
engine:          ChatGPT-User On-Demand Fetcher, OpenAI Search Crawler (OAI-SearchBot), OpenAI GPTBot (Training), Perplexity AI Crawler, Claude On-Demand Fetcher, Mistral On-Demand Fetcher, GoogleOther/R&D Fetcher, Gemini Deep Research Fetcher, Google NotebookLM Fetcher
metric_kind:     crawler visits
supersedes:      none
captured:        four images, full transcription each
```

## Transcription

**01 — "Total AI Crawler Bot visits (%) vs. Page Type"** (bar chart, y-axis 0-30%): Homepage ~30.0%, Terms ~25.0%, Guides ~10.2%, Feature pages ~6.7%, Pricing pages ~5.0%, Blogs ~3.2%, Tool pages ~2.5%, robot.txt ~2.1%, Product pages ~4.0%, About ~1.3%, Security ~0.5%, Audience pages ~0.7%, Legal ~0.7%, Case Studies ~0.6%, Booking/demo ~0.5%, Partners ~0.6%, Referral ~0.3%, **llms.txt** — bar drawn in a distinct pink/magenta color, visually near-zero (~0.1%, consistent with the article's own "0.1%" figure), .pdf files ~0.1%, Careers ~0.1%, Referral (second bar, duplicate label as printed) ~0%. [note: values are visual reads off an unlabeled-datapoint bar chart; llms.txt's own bar is confirmed near-bottom, consistent with text].

**02 — Agent-analytics dashboard, four KPI tiles + line chart + pie chart** (undated screenshot, presumably end-of-window snapshot): "Agents Visits Last 30 Minutes: 38" / "Total Agents Page Visits: **62.1K**" / "**Total Agent Vs Human Volume: 12.9%**" ("418.2K human page visits") / "Total Human Referrals: 1.8K". Line chart "Agents Page Visits Over Time" spans dates 06-11 through 02-02 (day-month, undated year), with a sharp spike to ~6,800 around "04-12", tooltip at that point reading: "04-02 / ChatGPT-User On-Demand Fetcher: 676 / OpenAI GPTBot (Training): 5 / Perplexity AI Crawler: 12 / Meta Web Indexer: 53 / GoogleOther / R&D Fetcher: 14 / OpenAI Search Crawler (OAI-SearchBot): 13 / Gemini Deep Research Fetcher: 15 / Google NotebookLM Fetcher: 16 / Claude On-Demand Fetcher: 8 / Perplexity On-Demand Fetcher: 0 / Mistral On-Demand Fetcher: 0". Pie chart "Agents Page Visits Distribution" (no numeric labels visible, largest wedge purple/indigo ≈ half, second largest coral/orange ≈ quarter, remainder split among ~6 smaller slices).

**03 — Per-URL bot breakdown widget, row labeled "/llms.txt"**: ChatGPT-User On-Demand Fetcher 81; OpenAI Search Crawler (OAI-SearchBot) 3. Sum = **84**, matching the article's own headline figure ("just 84 requests targeted the /llms.txt file") exactly, and additionally showing its full per-bot composition (not stated in the article text): 81 of the 84 llms.txt hits are ChatGPT-User, the remaining 3 are OAI-SearchBot — no other named bot (Claude, Perplexity, Gemini, Mistral) requested /llms.txt at all in this breakdown.

**04 — Per-URL bot breakdown widget, row labeled "/robots.txt"**: OpenAI Search Crawler (OAI-SearchBot) 621; Perplexity AI Crawler 335; Claude On-Demand Fetcher 174; Mistral On-Demand Fetcher 7; ChatGPT-User On-Demand Fetcher 3. Sum = 1,140. Not stated in the article's own text (the article names /robots.txt only as a "sitting near the bottom" comparator, at ~2.1% per image 01, with no bot breakdown) — new figure from this image pull.

## New figures not in the text pull (04-signal for compiled append)

1. **62.1K total agent page visits vs. 418.2K human page visits = agent share 12.9%** of combined volume (image 02) — a ratio not stated in the article's own prose.
2. **/llms.txt's 84 hits break down 81 ChatGPT-User + 3 OAI-SearchBot**, zero from Claude/Perplexity/Gemini/Mistral (image 03) — the article's text states only the aggregate 84, not this per-bot split.
3. **/robots.txt received 1,140 total bot hits** across five named bots (image 04), roughly 13.6x llms.txt's 84 — a direct llms.txt-vs-robots.txt bot-count comparator not stated as a ratio in the article text (the article only says llms.txt "hardly performed better than an average .pdf file").

## Pull notes — mechanical only

- Images read via the agent's Read tool directly on the saved PNGs; all labels legible at native resolution except image 01's individual bar percentages, which have no printed data labels and are visual estimates against the gridlines (flagged inline).
- Image 02's date axis uses day-month labels only (no year); not independently datable from the image alone — recorded as shown.
