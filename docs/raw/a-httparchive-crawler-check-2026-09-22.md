# HTTP Archive — reports index and discussion forum, checked for AI-crawler content

```yaml
source:          HTTP Archive (httparchive.org reports index; discuss.httparchive.org forum search)
url_or_doc_id:   https://httparchive.org/reports ; https://discuss.httparchive.org/ ; https://discuss.httparchive.org/search?q=bot%20crawler%20declared ; https://discuss.httparchive.org/search?q=llms.txt%20OR%20%22AI%20crawler%22%20OR%20GPTBot%20OR%20ClaudeBot
published:       n/a — index and search-results pages, not a dated report
pull_date:       2026-09-22
pull_method:     browser extension
pull_purpose:    evidence about category noise
tier:            4
tier_reason:     table default per channels.md C28; this pull records an absence, not a measured number — no figure is drawn from it for any compiled claim
source_label:    analyst-derived
lane:            A
sub_market:      n/a
engine:          n/a — no engine-specific content found
metric_kind:     none
supersedes:      none
captured:        full text of the reports index page; full text of the forum landing page's topic list; full text of two forum search-results pages
```

## Verbatim

### `httparchive.org/reports` — full report list (title and one-line description of every report on the index)

"All Reports"

- **State of the Web** — "This report captures a long view of the web, including the adoption of techniques for efficient network utilization and usage of web standards like HTTPS."
- **State of JavaScript** — "JavaScript powers the modern web, enabling rich and interactive web applications. In this report we dive into how JavaScript is used on the web, and its adoption and trends both for mobile and desktop experiences."
- **State of Images** — "Images are the most popular resource type on the web. In this report we analyze how images are being used across the web."
- **Loading Speed** — "Web performance can directly impact business metrics like conversion and user happiness. This report analyzes various performance metrics in the lifecycle of a loading page including those used by many modern progressive web apps."
- **Progressive Web Apps** — "This report examines the state of Progressive Web Apps (PWAs)..."
- **Accessibility** — "This report tracks accessibility of pages as measured by Lighthouse."
- **SEO** — "How websites are built can affect their ranking in search results. This report tracks the adoption of several key Search Engine Optimization (SEO) techniques."
- **Page Weight** — "This report tracks the size and quantity of many popular web page resources..."
- **CrUX** — "Loading and interactivity performance as experienced by real-world Chrome users..."
- **Capabilities** (Project Fugu) — "...a cross-company effort at Google to make it possible for web apps to do anything native apps can..."
- **Core Web Vitals Technology Report** — "...combining the powers of real-user experiences in the Chrome User Experience Report (CrUX) dataset with web technology detections available in HTTP Archive..."

No report on this index is named or described as covering AI crawlers, bot traffic, robots.txt AI-directive adoption, or llms.txt.

### `discuss.httparchive.org` — forum search results

Search `bot crawler declared` (1 result): "Http archive bot/crawler declared? — Uncategorized — Aug 2025 - I'm writing a research paper and need to explain how the http archive crawler declares itself to websites as a bot. can you please explain this to me? I'm particularly interested in learning if it's included on this list: https://iabtechlab.com/what-is-the-iab-tech-lab-spiders-and-bots-list/ ..." — this thread is about **HTTP Archive's own crawler** identifying itself to websites, not about AI-vendor crawlers.

Search `llms.txt OR "AI crawler" OR GPTBot OR ClaudeBot` (50+ results, "No exact matches, but here are some related results"): every one of the fifty-plus results returned is topically unrelated to AI crawlers — results include threads titled "Chapter 2. JavaScript," "Response body is empty in the crawl dataset," "New Release: `httparchive.crawl` Dataset," "Using Wappalyzer to Analyze CPU Times Across JS Frameworks," "Chapter 8. Security," and similar, none mentioning GPTBot, ClaudeBot, PerplexityBot, Amazonbot, llms.txt, or "AI crawler" in their titles or summaries. The search UI itself labels these "related results," confirming no exact match was found.

## Pull notes — mechanical only

- `httparchive.org/reports` loaded via Chrome extension on first navigation (per channels.md C28, "200" access expected and confirmed).
- `discuss.httparchive.org` loaded and its topic list read; then two searches run directly against the forum's own search endpoint (`discuss.httparchive.org/search?q=...`) rather than an external web search, since the task brief names the forum itself as a P2-c2 target.
- **This is a recorded absence, not a failed pull.** As of 2026-09-22, neither the HTTP Archive report index nor its discussion forum's search index surfaces a report or thread specifically about AI-crawler identity, AI-crawler traffic volume, or llms.txt adoption. This matches `shortlist.md`'s own framing: "No cluster asserts that its target exists in the form named; several will return `unknown — checked`." Recorded here: `unknown — checked httparchive.org/reports and discuss.httparchive.org search ("bot crawler declared"; "llms.txt OR \"AI crawler\" OR GPTBot OR ClaudeBot") 2026-09-22`.
- HTTP Archive's **SEO** report (listed above) is the closest adjacent report by title, but its own one-line description names only classical SEO-technique adoption, not AI-crawler or llms.txt adoption specifically — not opened further in this pull since the task's discard rule (referral/traffic/crawl-volume crossing) and cluster scope point to Cloudflare and the platform docs as this cluster's actual crawl-volume sources, not HTTP Archive. An llms.txt-adoption figure, if HTTP Archive publishes one elsewhere (e.g. inside the State of the Web report's full dataset, not summarized on this index page), is scoped to Pass 5 cluster P5-c5 ("Structured data and `llms.txt`-style signalling"), not to this cluster's done condition, per `shortlist.md` P5-c5's own target list naming `httparchive.org` adoption data directly.
- No login wall, no paywall, no truncation on either page type pulled.
