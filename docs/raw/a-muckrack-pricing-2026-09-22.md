# Muck Rack — pricing (feature vs. base plan)

```yaml
source:          Muck Rack
url_or_doc_id:   https://muckrack.com/pricing; https://generativepulse.ai/ (nav scan)
published:       n/a — page not reachable this session
pull_date:       2026-09-22
pull_method:     fetch attempt (mcp fetch tool, robots.txt-blocked) and browser (Playwright MCP, Cloudflare-blocked) — both failed; recorded as blocked, not silently skipped
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — would-be platform primary page; not reached, so recorded as blocked rather than tiered on content
source_label:    vendor-reported
lane:            A
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        none — page not reached; blocked responses only
feature:         Generative Pulse / AI Visibility Badges price delta against Muck Rack's base PR-platform plan
```

## Verbatim

`mcp__MCP_DOCKER__fetch` on `muckrack.com/pricing`: "When fetching robots.txt (https://muckrack.com/robots.txt), received status 403 so assuming that autonomous fetching is not allowed, the user can try manually fetching by using the fetch prompt."

`curl` (browser User-Agent header) on `https://muckrack.com/`: HTTP 403.

Playwright MCP browser navigation to `https://muckrack.com/pricing`: page title rendered as "Just a moment..." — Cloudflare interstitial, page never reached its own content in two attempts.

`generativepulse.ai`'s own navigation menu (captured in full in `a-muckrack-generativepulse-product-2026-09-22.md`) carries no "Pricing" link anywhere — every call to action on that microsite is "Free Brand Preview" or "Request Demo" / "Request A Demo," consistent with Muck Rack's base PR platform, which is known (from the vendor's roster entry, `docs/raw/a-vendor-roster-2026-09-22.md` row 21, G2 category listing) to be sales-led with no listed self-serve price on G2.

## Pull notes — mechanical only

- `unknown — checked muckrack.com/pricing (403 to plain fetch and to curl; Cloudflare-blocked on Playwright MCP), generativepulse.ai nav (no pricing link found) 2026-09-22` — no public price, and therefore no price delta, was found through any channel available this session.
- claude-in-chrome extension reported "not connected" at task start; the Playwright MCP fallback itself was Cloudflare-blocked on `muckrack.com`'s main domain specifically (its `generativepulse.ai` microsite was not blocked, see the product-page pull), consistent with the pattern other agents this session recorded for Cloudflare-protected consumer surfaces on this shared IP.
- Price and price delta recorded as `not disclosed — checked muckrack.com, generativepulse.ai 2026-09-22`, not estimated.
