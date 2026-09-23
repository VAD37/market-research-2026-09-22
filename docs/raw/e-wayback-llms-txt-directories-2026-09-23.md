# Wayback Machine and live — llms.txt directory sizes over time (llmstxt.site, directory.llmstxt.cloud); HTTP Archive and Common Crawl checked

```yaml
source:          llmstxt.site ("llms.txt sites directory") and directory.llmstxt.cloud ("llms.txt directory"), live pages and web.archive.org captures
url_or_doc_id:   https://llmstxt.site/ ; https://directory.llmstxt.cloud/ ; http://web.archive.org/cdx/search/cdx?url=llmstxt.site/&output=json&filter=statuscode:200&collapse=timestamp:6 ; same for directory.llmstxt.cloud/ ; captures at http://web.archive.org/web/<timestamp>id_/<url>
published:       each capture's own timestamp; live pages 2026-09-23
pull_date:       2026-09-23
pull_method:     fetch (curl, User-Agent "market-research-bot contact: research@example.invalid"); per capture, the count of distinct hostnames matching `<host>/llms.txt` in the HTML (measured by script), and any count string the page prints
pull_purpose:    evidence about a number
tier:            5
tier_reason:     each directory is a self-submitted list ("Add yours now!", "Submit your llms.txt"), not a crawl; the number of sites it lists is that directory's claim at that date; our host count is a count of what the archived page rendered, which for directory.llmstxt.cloud is a subset after its 2026 redesign
source_label:    vendor-reported (directory-stated counts); measured-by-us for the distinct-host counts read off each archived page
lane:            E
sub_market:      organic recommendation
engine:          n/a — artifact readable by any crawler
metric_kind:     none
supersedes:      none
captured:        capture lists; per capture, byte size, distinct-host count and printed totals; live-page printed totals
verbatim:        full for printed strings; host counts are computed
```

## Live pages, 2026-09-23

### https://llmstxt.site/ — HTTP 200, 2,659,098 bytes

> "llms.txt directory - Find llms.txt files across the web" · "llms.txt sites directory" · "A list of all llms.txt file locations across the web with stats, derived from the llmstxt.org standard." · "Add yours now!"
> Column headers: "Product · Website · llms-txt · -tokens · llms-full-txt · -tokens"
> First rows rendered: "Hotel in Santa Barbara, CA · www.hotelcalifornian.com/ · www.hotelcalifornian.com/llms.txt · 0"; "Hotel in Sonoma, CA · www.farmhouseinn.com/"; "Hotel in Palm Beach, FL · www.eaupalmbeach.com/"; "Resort in Tahiti · thebrando.com/"; "Hotel in Dundee, OR · www.foleywinesdundeehills.com/"; "Hotel in Healdsburg, CA · www.hotel27north.com/"; "ListDefender · listdefender.com/ · 722 · listdefender.com/llms-full.txt · 2510"; …

Measured: occurrences of the string `llms.txt` 5,469; distinct hostnames before `/llms.txt` **1,497**. The page prints no total.

### https://directory.llmstxt.cloud/ — HTTP 200, 87,279 bytes

> "llms.txt directory" · "Directory · 3,830" · "Websites · 1,813" · "Products · 825" · "Developer tools · 531" · "AI · 386" · "Finance · 275" · "Submit your llms.txt" · "Sponsor us"
> "Websites listed · 3,830" · "Total llms.txt tokens · 47M" · "Total llms-full.txt tokens · 388M"
> "Featured · Get featured · Zapier … Cursor …"

Measured: distinct hostnames on the rendered page 9 (the page shows a featured subset; the 3,830 total is the page's own statement).

## Wayback captures — one per month, status 200

### llmstxt.site/ — 20 captures in CDX (2024-11-27 to 2026-08-27); 7 fetched

| Capture (UTC) | Bytes | `llms.txt` occurrences | Distinct hosts (measured) |
|---|---|---|---|
| 2024-11-27 16:23:16 | 110,984 | 173 | 56 |
| 2025-03-02 22:29:34 | 160,713 | 247 | 89 |
| 2025-06-15 23:12:24 | 444,400 | 829 | 224 |
| 2025-09-09 10:20:26 | 1,230,834 | 2,478 | 683 |
| 2025-12-13 22:51:25 | 2,657,176 | 5,469 | 1,491 |
| 2026-04-01 02:27:33 | 2,657,176 | 5,469 | 1,491 |
| 2026-08-27 15:13:52 | 2,657,176 | 5,469 | 1,491 |
| 2026-09-23 live | 2,659,098 | 5,469 | 1,497 |

[note: the three 2025-12 to 2026-08 captures are byte-identical in length and host count although the CDX digests differ (6GHYNXS3…, 5URJS7EX…, VWMJ4FLO…); the live page adds 6 hosts. Whether the directory stopped growing or the archive replayed one copy cannot be told from this pull.]

Full CDX list (timestamp, length): 20241127162316 6317; 20241209012218 7957; 20250130193438 8870; 20250219152422 9802; 20250302222934 10261; 20250408070743 12230; 20250522181925 12039; 20250615231224 31869; 20250701121017 39363; 20250807101842 83539; 20250909102026 82585; 20251006205025 82586; 20251213225125 176161; 20260107200917 177604; 20260207140429 176154; 20260401022733 177635; 20260504182651 180626; 20260606050447 176151; 20260715201102 177620; 20260827151352 180628. [note: CDX `length` is the compressed WARC record length, not the page size.]

### directory.llmstxt.cloud/ — 20 captures in CDX (2024-11-17 to 2026-06-05); 7 fetched

| Capture (UTC) | Bytes | Distinct hosts (measured) | `<li` count | Printed total |
|---|---|---|---|---|
| 2024-11-17 23:40:42 | 164,885 | 51 | 73 | none printed |
| 2025-03-05 14:30:28 | 425,540 | 107 | 142 | none printed |
| 2025-06-06 09:13:27 | 518,016 | 583 | 61 | none printed |
| 2025-09-04 17:11:37 | 518,018 | 583 | 61 | none printed |
| 2025-12-11 04:52:01 | 517,514 | 583 | 61 | none printed |
| 2026-03-17 11:31:54 | 184,261 | 68 | 0 | none printed on the archived HTML |
| 2026-06-05 22:46:38 | 184,261 | 68 | 0 | none printed on the archived HTML |
| 2026-09-23 live | 87,279 | 9 (featured subset) | 32 | "Websites listed 3,830" |

[note: from 2026-03 the site renders a featured subset and states its total as a number; the 68- and 9-host counts are the rendered subset, not the directory size. The 2025-06 to 2025-12 captures are near-identical (583 hosts each).]

Full CDX list (timestamp, length): 20241117234042 11574; 20241208075714 26308; 20250102002700 26527; 20250201055644 28487; 20250305143028 31748; 20250408070935 51439; 20250513193645 74671; 20250606091327 73205; 20250709001040 74684; 20250801211203 66480; 20250904171137 74363; 20251008161100 74525; 20251104232525 73825; 20251211045201 66187; 20260116061154 74504; 20260214063754 10236; 20260317113154 10269; 20260407213151 8471; 20260511001213 11089; 20260605224638 10291.

## Other adoption-count channels checked

- HTTP Archive: no llms.txt report or almanac chapter known to this pull; `findings/unknowns.md` already records "HTTP Archive has no AI-crawler report" (checked httparchive.org 2026-09-22). Not re-fetched 2026-09-23.
- Common Crawl index: a path-only wildcard (`*/llms.txt`) is not a supported CDX query shape; not attempted.
- Cloudflare Radar: no llms.txt statistic recorded in `raw/` as of 2026-09-22; not re-fetched.

## Pull notes — mechanical only

- First-batch captures arrived gzip-encoded (magic 1f8b) and were decompressed before parsing; second batch used `--compressed`.
- Host count regex: `([a-z0-9][a-z0-9.-]+\.[a-z]{2,})/llms\.txt` over the raw HTML, case-sensitive, set of distinct matches. A host listed with both `/llms.txt` and `/llms-full.txt` counts once.
- One capture per month selected by CDX `collapse=timestamp:6`; seven of twenty fetched per site (roughly quarterly plus the newest).
- No login, no form submitted.
