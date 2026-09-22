# G2 and Capterra — access attempt (blocked), S4 review-velocity sweep

```yaml
source:          G2; Capterra
url_or_doc_id:   https://www.g2.com/categories/ai-search-visibility ; https://www.capterra.com/p/ai-search-visibility/
published:       n/a — access attempt, not a successful pull
pull_date:       2026-09-22
pull_method:     fetch (curl with a browser User-Agent; WebFetch as a second fetch path; no browser extension, no login)
pull_purpose:    evidence about a number
tier:            n/a — no content retrieved
tier_reason:     access blocked at every path tried, both tools
source_label:    n/a
lane:            F
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        HTTP error responses / bot-challenge pages only
```

## Verbatim

`curl` with a browser User-Agent on `https://www.g2.com/categories/ai-search-visibility`: `403`, body is a Cloudflare/DataDome-style challenge page: `<p id="cmsg">Please enable JS and disable any ad blocker</p>` with an embedded `dd={'rt':'c','cid':'AHrlqAAAAAMADLC...` DataDome token.

`WebFetch` tool on the same G2 URL: `"The server returned HTTP 403 Forbidden."`

`curl` with a browser User-Agent on `https://www.capterra.com/p/ai-search-visibility/`: `403`, body titled `"Just a moment..."` (Cloudflare interstitial).

`WebFetch` tool on the same Capterra URL: `"The server returned HTTP 404 Not Found."` — a different failure mode than the curl 403, suggesting either a different edge response to the WebFetch fetch origin or that the specific path guessed (`/p/ai-search-visibility/`) does not exist as a Capterra category slug even where reachable; the correct category slug was not independently discovered this pull.

## Pull notes — mechanical only

- **Recorded: G2 and Capterra review-velocity data for AI-visibility tools, filtered to reviewers whose stated industry is software — unknown — checked g2.com/categories/ai-search-visibility (curl 403, WebFetch 403) and capterra.com/p/ai-search-visibility/ (curl 403, WebFetch 404) — 2026-09-22.**
- Matches `channels.md` C36 (G2, `403→ext`) and C37/C38 (Capterra, `403→ext`) exactly — both channels were already known to require the browser extension, which this task does not have (both slots held by other agents per the task brief).
- Added to the browser backlog: `https://www.g2.com/categories/ai-search-visibility` and the correct Capterra AI-visibility category URL (to be located by a browser-holding agent, since the guessed slug above 404'd via WebFetch).
- OMR (`omr.com`) was reachable without a browser and is filed separately — see `f-signal-bs-S4-omr-2026-09-22.md`.
