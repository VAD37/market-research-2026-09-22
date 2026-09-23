# Microsoft — publisher content partnership and Copilot ads measurement-partner pages: negative check (channels searched, nothing found)

```yaml
source:          Microsoft — news.microsoft.com site search, blogs.microsoft.com site search, about.ads.microsoft.com blog listing, help.ads.microsoft.com; web.archive.org availability API
url_or_doc_id:   https://news.microsoft.com/?s=publisher+content+marketplace ; https://blogs.microsoft.com/?s=publisher+content+marketplace ; https://about.ads.microsoft.com/en/blog ; https://about.ads.microsoft.com/en/blog?q=copilot ; https://help.ads.microsoft.com/apex/index/3/en/60111 ; http://archive.org/wayback/available?url=www.microsoft.com/en-us/microsoft-advertising/publisher-content-marketplace
published:       search-result pages generated at pull time
pull_date:       2026-09-23
pull_method:     fetch (curl, User-Agent "market-research-bot contact: research@example.invalid"; HTML tag-stripped)
pull_purpose:    evidence about category noise — records a negative check
tier:            3
tier_reason:     Microsoft's own site-search output; carries no number
source_label:    vendor-reported
lane:            C
sub_market:      n/a — publisher / sell-side monetisation; paid placement (Copilot ads measurement)
engine:          Microsoft — Copilot
metric_kind:     none
supersedes:      none
captured:        result headings and counts verbatim
```

## Verbatim

news.microsoft.com search "publisher content marketplace":

> You searched for publisher content marketplace - Source
> publisher content marketplace Results Page
> Microsoft PlayReady Helps Expand Digital Content Economy With New Adoption for Mobile and In-Home Entertainment Scenarios
> February 16, 2009 Microsoft Reveals New Windows® Phones With Marketplace and My Phone Services
> February 3, 2009 Global Content Solution Professionals Back New Microsoft Education Platform for Rich Media
> November 13, 2008 Games for Windows — LIVE Levels Up PC Gamers With New In-Game Display, Marketplace and Upcoming Premium Downloadable Content
> December 19, 2007 Viacom and Microsoft Announce Long-Term Digital Content and Advertising Partnership

blogs.microsoft.com search "publisher content marketplace":

> 3 Results for publisher content marketplace
> Apr 22, 2025 | Alysa Taylor - Chief Marketing Officer, Commercial Cloud & AI — Explore AI-powered success stories of customer transformation and innovation
> May 9, 2012 — The Midweek Download: May 9th Edition [...]
> Mar 9, 2010 | Microsoft blog editor - Microsoft News Center Staff — Game Developers Have a Great Opportunity with Windows Phone 7 Series

about.ads.microsoft.com/en/blog (listing, first page, with and without `?q=copilot`) — headings containing "partner" or "measure":

> Prepare your brand for AI-driven holiday shopping by strengthening four foundations: product feeds, measurement, campaign performance, and AI visibility.
> Announcing the 2026 Microsoft Advertising Partner Awards Finalists: North America
> Announcing the 2026 Microsoft Advertising Partner Awards Finalists: APAC & Japan
> Announcing the 2026 Microsoft Advertising Partner Awards Finalists: EMEA and LATAM
> [nav items:] Find a partner · MCP Server · Agentic commerce · Deal curation

help.ads.microsoft.com/apex/index/3/en/60111:

> Oops... Hmm... We don't have anything that matches your search. Check your spelling and try another search.

archive.org availability API:

> {"url": "www.microsoft.com/en-us/microsoft-advertising/publisher-content-marketplace", "archived_snapshots": {}}
> {"url": "news.microsoft.com/source/2026/02/publisher-content-marketplace", "archived_snapshots": {}}
> {"url": "blogs.microsoft.com/blog/2026/02/publisher-content-marketplace", "archived_snapshots": {}}

## Pull notes — mechanical only

- No Microsoft page naming a publisher content marketplace, a Copilot publisher revenue share, or a Copilot ads measurement-partner roster was reached through the channels above. Existing raws `raw/b-microsoft-ads-copilot-formats-blog-2026-09-23.md`, `raw/b-microsoft-ads-in-copilot-2026-09-22.md` and `raw/b-microsoft-copilot-advertising-platform-2026-09-22.md` were grepped for "measurement partner", "DoubleVerify", "IAS", "third-party" — no hits.
- General search engines were walled this session (Mojeek returned a JavaScript CAPTCHA page; DuckDuckGo html 403; WebSearch tool exhausted), so the check is limited to Microsoft's own site searches and the archive availability API. The URLs passed to the archive API are guesses, not known pages.
