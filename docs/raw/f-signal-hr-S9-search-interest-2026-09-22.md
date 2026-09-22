# Search-interest tools — S9, high-CPA regulated vertical, method record

```yaml
source:          Google Trends (trends.google.com)
url_or_doc_id:   https://trends.google.com/trends/explore
published:       n/a
pull_date:       2026-09-22
pull_method:     none attempted — see below
pull_purpose:    evidence about category noise (method-availability record only; no content pulled)
tier:            n/a — nothing retrieved
tier_reason:     n/a
source_label:    n/a
lane:            A
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        nothing — this file records why nothing was captured
vertical:        high-CPA regulated
cell:            n/a
query:           n/a
```

## Method record

The task assigning this cluster states explicitly: "S9 search interest (browser-only — record method or unknown)." This agent is fetch-only for the duration of this task — no Chrome extension, no Playwright (per the task's own scope line: "Fetch-only agent: no Chrome extension, no Playwright"). Google Trends' `/explore` interface is a JavaScript-rendered single-page application; its interest-over-time and interest-by-subregion data is not exposed through a documented, stable, unauthenticated JSON or REST endpoint that a plain `curl` reaches reliably (the historically-used unofficial `trends.google.com/trends/api/...` endpoints require a session token minted by the rendered page itself). No attempt was made to reverse-engineer or brute-force that token-minting flow this pull, consistent with the task's fetch-only scope and with `channels.md` C45's own entry for Google Trends, which assumes normal (200, browser-renderable) access rather than a token-gated API.

`channels.md` C21–C24 (Similarweb, Datos, SparkToro, StatCounter) are the repo's other S9 channels; none of them publishes a per-vertical, per-term breakdown for "AI search visibility," "GEO," or "AEO" specifically inside credit cards, insurance, or supplements — their published material (already pulled at Pass 2, `docs/raw/a-*-share-*-2026-09-22.md`) is engine-market-share content, not category-term search-interest content, and none of the four channels' free content includes a vertical cut of search-interest data even where it is reachable.

## Result

**`unknown — checked trends.google.com/trends/explore (requires browser rendering, this task is fetch-only, no extension held) 2026-09-22`** for S9 in the high-CPA regulated vertical.

## Caveats

- This is a genuine capability gap for this cluster's access, not a search that returned zero — S9 requires a different agent (one holding the browser-extension slot) to close, per the task's own routing note.
- No fabricated or remembered Google Trends figure is recorded here or anywhere in this file, per root `CLAUDE.md`'s evidence rules.
