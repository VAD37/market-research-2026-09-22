# Adthena — ChatGPT Ad Index page (ChatGPT Ads Share of Search Index): UK advertiser count and the leaderboard images

```yaml
source:          Adthena Ltd (adthena.com)
url_or_doc_id:   https://www.adthena.com/resources/blog/chatgpt-ads-share-of-search-index/ (reached from https://www.adthena.com/chatgpt-ads-share-of-search-index/ by redirect)
published:       undated on the page text; images dated by filename 2026-07-22 and 2026-07-23; data "week of Jul 13-20, 2026"
pull_date:       2026-09-23
pull_method:     fetch (curl); three data images saved by curl
pull_purpose:    evidence about a number (UK distinct-advertiser count inside ChatGPT ads; advertiser names per market sit in the images, to be read by IMG-1)
tier:            5
tier_reason:     vendor study with a stated method ("Visibility %: the share of monitored prompts where that brand's ad appeared"), a stated week and a stated market cut; prompt count and panel not stated on this page; the vendor sells the paid product the index promotes — bias flagged
source_label:    vendor-reported
lane:            F
sub_market:      paid placement
engine:          ChatGPT
metric_kind:     visibility
supersedes:      none (PPC Land's relay of the same index is docs/raw/b-ppcland-adthena-7378-advertisers-2026-09-23.md)
captured:        page text verbatim; three data images
```

## Verbatim

> ChatGPT Ad Index: Who's Winning ChatGPT Ads | Adthena
> ChatGPT Ad Index: The free weekly benchmark for advertisers
> Track which brands are advertising inside ChatGPT, how crowded each market is, and how visible different brands are. Free, refreshed weekly.
> Adthena has launched the ChatGPT Ads Share of Search Index, a free weekly benchmark of which brands are advertising inside ChatGPT's sponsored answers. Thousands of distinct advertisers are already active across the US, UK and Australia, and this is the first public index with meaningful UK coverage since ChatGPT ads reached the UK on June 6, 2026. The index shows a ranked visibility leaderboard, per-market saturation, the most contested prompts, and a brand look-up tool.
> The ChatGPT Ads Share of Search Index is Adthena's free weekly benchmark of which brands are advertising inside ChatGPT. It's a top-level weekly cut of the data layer behind ChatGPT Ads Intelligence, our full competitive product: the index shows you the shape of the market, while the full product tracks every ad, every prompt and every competitor in your category, daily.
> A ranked leaderboard of the most visible advertisers — Every advertiser we observe, ranked by Visibility %: the share of monitored prompts where that brand's ad appeared. Filter by market to see who's winning the US, the UK or Australia specifically.

[image: docs/raw/img/f-adthena-S2-eu-paid-agentic-2026-09-23/01-top-chatgpt-advertisers-by-visibility-week-of-july-13.png] — alt "Top ChatGPT advertisers by Visibility %, week of July 13 | ChatGPT Ad Index"

> A market snapshot of competitive saturation — How many distinct advertisers are active in each market, and how visible the leaders already are. This is your "how crowded is my pool" number, and it moves week to week as new entrants arrive.

[image: docs/raw/img/f-adthena-S2-eu-paid-agentic-2026-09-23/02-distinct-advertisers-and-saturation-by-market.png] — alt "Distinct advertisers and competitive saturation by market | ChatGPT Ad Index"

> Type any advertiser's name and get their rank and visibility in seconds.

[image: docs/raw/img/f-adthena-S2-eu-paid-agentic-2026-09-23/03-brand-look-up-tool.png] — alt "Brand look-up tool | ChatGPT Ad Index"

> This is the first public index with meaningful UK coverage — ChatGPT ads only reached the UK on June 6, 2026, the first expansion beyond the US, Canada, Australia and New Zealand. Public trackers of ChatGPT ads exist, but their volume is overwhelmingly concentrated on US queries.
> The index tracks the UK as a first-class market from launch: 1,342 distinct UK advertisers in the week of Jul 13-20, 2026, alongside full US and Australian cuts. If you run UK budgets, this is the first public place you can benchmark the market at all.
> The UK auction is weeks old, the US one is still forming, and the early-mover window in this channel is open. It won't stay open.
> Related on the page: "Pharma in Google AI Mode: 50,000 ads served, zero from prescription brands"; "Google AI Mode ads: Google is rebuilding your search ads for every conversation"; "ChatGPT Ads quietly adds negative phrases: What it means for advertisers"

[note: the leaderboard, the per-market saturation figures and any advertiser names live only in the three images; the page text names no advertiser and no vertical. The index itself is a hosted tool not reachable from this page's static HTML.]

## Pull notes — mechanical only

- Page HTTP 200 (126 KB) after one redirect. Images fetched from the wp-content URLs without the `-1200xNNN` size suffix; PNG 2270×672, 2262×588 and 1218×728, 120,525 / 195,630 / 76,488 bytes.
- INDEX rows appended to docs/raw/img/INDEX.csv with `analysed_in` blank.
