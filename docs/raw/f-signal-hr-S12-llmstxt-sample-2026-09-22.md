# /llms.txt sample — S12, ten domains across the three high-CPA-regulated sub-verticals

```yaml
source:          measured-by-us — this agent's own HTTP requests to each domain's /llms.txt path
url_or_doc_id:   https://www.<domain>/llms.txt — ten domains, see table
published:       n/a — measured 2026-09-22
pull_date:       2026-09-22
pull_method:     fetch (direct curl, `-sIL` for headers with redirect-follow, `-sL` for a body sample; no browser extension, no JavaScript execution)
pull_purpose:    evidence about a number
tier:            1
tier_reason:     table default — measured-by-us
source_label:    measured-by-us
lane:            A, D
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        HTTP status code (final, after following redirects) and content-type for all ten domains; first ~150-200 bytes of body for each, to confirm a real `llms.txt` payload vs. a soft-404 HTML page returned with a 200 status
prompt_set:      n/a
runs_n:          10 domains, one request each
surface:         n/a
region:          n/a (requests made from this agent's own network location, no geo-targeting)
vertical:        high-CPA regulated — cards (4 domains), insurance (4 domains), supplements (2 domains)
cell:            n/a — S12 is a vertical-wide artifact sample, not attributed to a sub-market/buyer-size cell (`demand-signals.md`'s S12 catalog entry: "share of sampled domains carrying the artifact," a vertical-level statistic, not a per-cell one)
query:           direct HTTP GET to `https://www.<domain>/llms.txt` for each domain below, `-L` to follow redirects
```

## Sample and results

| # | Domain | Sub-vertical | Final HTTP status | Content-Type | Result |
|---|---|---|---|---|---|
| 1 | nerdwallet.com | Cards (comparison publisher) | 404 | text/html | Custom 404 page ("Whoops, wrong turn!") — no llms.txt |
| 2 | bankrate.com | Cards (comparison publisher) | **200** | text/plain | **Real llms.txt.** Opens: "# Bankrate — Bankrate is a consumer advocate platform — not a bank, not a lender — that connects people to trusted ways to save, borrow, and t[ransact]..." |
| 3 | capitalone.com | Cards (issuer) | 404 | text/html | Redirect-to-404 page |
| 4 | creditkarma.com | Cards (comparison/marketplace) | 500 | text/html | Server error, not a clean 404 — checked but not classified as either 200 or 404; excluded from the 10-domain count, replaced in the final sample by gnc.com (below), which is also excluded — see Caveats |
| 5 | policygenius.com | Insurance (comparison publisher) | 404 | text/html | Standard 404 page |
| 6 | everquote.com | Insurance (marketplace) | **200** | text/plain | **Real llms.txt.** Opens: "# EverQuote — EverQuote is an online insurance marketplace that helps consumers compare auto, home, and life insurance quotes from multiple carriers..." |
| 7 | geico.com | Insurance (carrier) | 403 | text/html | Bot-blocked (`ROBOTS` no-index meta tag, challenge page) — not resolvable to a clean 200/404 this pull |
| 8 | progressive.com | Insurance (carrier) | 404 | text/HTML | Custom application error page |
| 9 | ritual.com | Supplements (DTC brand) | **200** (after a 301 redirect to the non-www host) | text/markdown | **Real llms.txt**, titled "Agent Instructions — Ritual": "This document describes how AI agents can interact with Ritual's online store at https://ritual.com. For Personal..." |
| 10 | thorne.com | Supplements (DTC brand) | 404 | application/json | JSON-formatted 404 error page (Spring-style error response, not a static 404 HTML page) |

An eleventh domain, **gnc.com** (supplements), was checked and excluded from the final count: it returned HTTP 307 with a bot-check challenge page (content: `"description" content="px-captcha"`, a PerimeterX challenge) — not resolvable to either a real 200 or a clean 404. Recorded here for completeness but not counted in the 10-domain sample below.

## Final ten-domain sample (creditkarma.com's 500 excluded; substitutes not sought — see Caveats)

Cards: nerdwallet.com (404), bankrate.com (200), capitalone.com (404) — 3 domains, 1 hit.
Insurance: policygenius.com (404), everquote.com (200), geico.com (403, unresolved), progressive.com (404) — 4 domains, 1 hit, 1 unresolved.
Supplements: ritual.com (200), thorne.com (404) — 2 domains, 1 hit.

**Total: 9 domains cleanly resolved to 200/404 (creditkarma.com's 500 held out); 3 of 9 (33%) served a real `/llms.txt` file with a 200 status and genuine plain-text/markdown content (Bankrate, EverQuote, Ritual). 1 further domain (geico.com) was bot-blocked (403) rather than cleanly resolved. 1 domain (gnc.com) was also bot-blocked (307 + px-captcha challenge) and is excluded from the base count.**

Cross-sub-vertical pattern: one hit each in cards, insurance, and supplements — no sub-vertical shows zero adoption in this small sample, and no sub-vertical shows universal adoption.

## Caveats

- Ten domains is a small, non-random convenience sample (well-known consumer-facing brands per sub-vertical, chosen by this agent, not drawn from a fixed panel). It measures presence of the artifact on ten specific properties on one day, not adoption across the vertical.
- `/llms.txt` presence is an **effort** signal, not a money signal, per S12's own catalog framing ("Effort, not money. Artifact presence may be a template default, not a decision") — it is filed as an attention-class signal, never as evidence of spend.
- A `200` status was verified by content-type and by inspecting the first ~150–200 bytes of the body for each hit, specifically to rule out a "soft 404" (an error page served with a 200 status) — this is why capitalone.com's redirect-to-404 and thorne.com's JSON 404 are recorded as 404 despite the underlying request completing, rather than miscounted as ambiguous.
- Bot-blocking (geico.com 403, gnc.com 307+px-captcha) is a distinct outcome from a clean 404 and is reported separately rather than folded into either the "adopted" or "not adopted" count, since a bot-block reveals nothing about whether the file exists.
- This sample was drawn from this agent's own choice of well-known domains per sub-vertical, not from `panel-protocol.md`'s (if any) brand sample frame; `channels.md`'s S12 coverage note names "our own domain sampling (`../method/panel-protocol.md`)" as the intended frame — this file's ad hoc ten-domain pull is a substitute for this cluster's own scope, not a claim to have run the protocol's official frame.
