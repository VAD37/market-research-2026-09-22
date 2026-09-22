# PPC Land — "UK advertisers face zero ChatGPT ad share, Adthena data show" — pointer (primary unreachable)

```yaml
source:          PPC Land (Luis Rijo)
url_or_doc_id:   https://ppc.land/uk-advertisers-face-zero-chatgpt-ad-share-adthena-data-show/
published:       2026-07-08
pull_date:       2026-09-22
pull_method:     fetch (mcp fetch tool; ppc.land fetches cleanly)
pull_purpose:    evidence about a number
tier:            5
tier_reason:     table default — trade press pointer, per trust-rubric.md/channels.md C56 "5 pointer"
source_label:    vendor-reported (as characterized by the trade item; primary itself not independently confirmed)
lane:            B
sub_market:      paid placement
engine:          ChatGPT — OpenAI; Google (AI Overviews, comparator)
metric_kind:     traffic
supersedes:      none
captured:        full article (partial — truncated by fetch tool length limit; the headline claim and method description captured in full)
```

## Primary this item links, and why it was not pulled

The article states its source is: "Adthena's Monthly AI Data Pulse for June 2026," described in the article as "an eleven-page document and summarized in a LinkedIn post from the company." A LinkedIn post carrying that title was located (`www.linkedin.com/posts/adthenas-monthly-ai-data-pulse-ugcPost-7477737887086862336-G6Dv/`) and was reachable via the Chrome extension (logged in as the session's own LinkedIn account), but its content — AIO frequency 54.92% in AU / 39.53% in UK, a $200K-minimum-gone self-serve announcement, "580 ads" analyzed — does **not** match the figures this PPC Land article attributes to the June 2026 edition (169,560 UK ChatGPT scrapes, 0.00% UK ad frequency, 23% UK AI Overview frequency, 29,237 total ad items). This is evidently a **different, later monthly edition** of the same recurring Adthena LinkedIn series, not the June 2026 edition the article cites. The specific June 2026 edition's own LinkedIn post URL was not located within this session's search budget.

Separately, `linkedin.com/robots.txt` disallows autonomous fetching for essentially all paths (`User-agent: *` / `Disallow: /`), confirmed by a direct fetch attempt this session, so even had the correct post URL been found, a plain-fetch pull would have been blocked; only the Chrome extension (logged-in session) can reach LinkedIn content at all, and only for a URL correctly identified in advance.

Adthena's own public blog (`adthena.com/resources/blog/`) was checked for a June-2026-specific "AI Data Pulse" post and for a page reproducing the 169,560-scrape / 0.00%-UK figures; no matching post was found among the resource hub's listed titles as of this pull.

**Reason unreachable:** the specific June 2026 edition of the primary (a LinkedIn-distributed 11-page document) could not be located at a stable URL within this session; the one same-titled LinkedIn post that was found carries different, later data and is not the same primary; LinkedIn itself blocks autonomous (non-extension) fetching per its own `robots.txt`.

## Verbatim (trade item, partial)

> "Search intelligence platform Adthena today circulated its Monthly AI Data Pulse for June 2026, and the headline figure sits inside a single row of a data table: zero. Across 169,560 scrapes of ChatGPT conducted in the United Kingdom throughout June, the company's monitoring recorded no ad placements whatsoever, a 0.00 percent ad frequency rate and zero of the 29,237 total ad items Adthena catalogued that month across all markets. That number sits awkwardly next to a separate finding in the same report: Google's AI Overviews appeared in 23 percent of UK searches during June, three percentage points ahead of the 18 percent frequency Adthena measured in the United States."

> "Adthena's report, distributed as an eleven-page document and summarized in a LinkedIn post from the company, breaks its findings into several sections: AI Overview frequency and ad penetration, query-length patterns behind AI Overview ads, sector-level ad exposure, ChatGPT ad frequency by country, a UK-specific ChatGPT ads analysis, the highest-frequency ChatGPT ad categories, and PPC market share tables for the sports and outdoors category across three countries."

> "On the Google side, the US AIO frequency rate stood at 18 percent in June, with an AIO ad penetration rate of just 0.16 percent, meaning only 16 in every 10,000 AI Overviews carried a paid placement. The UK rate came in higher at 23 percent, and Australia higher still at 24 percent."

> "A separate query-length analysis, covering AI Overview ad appearances specifically, recorded 160,010 total US ad appearances in June. Of those, 57.4 percent occurred on three-to-four-word searches..."

[note: article continues beyond what the fetch tool returned in a single call (5000-character limit reached mid-paragraph); not re-fetched with a continuation call since the headline claim, the primary's identity, and the method description above were already captured in full.]

## Pull notes — mechanical only

- PPC Land itself fetched cleanly (tier-5-pointer channel, C56, "fetches cleanly" per task instructions).
- Chrome extension used (dedicated tab, tabId 1697684069) to attempt the LinkedIn primary; reached a LinkedIn post of the right title-pattern but wrong month's data, confirmed by content mismatch, not by URL mismatch alone.
- Adthena's public blog checked (`adthena.com/resources/blog/`) via plain fetch — no June-2026-specific post found among listed titles.
