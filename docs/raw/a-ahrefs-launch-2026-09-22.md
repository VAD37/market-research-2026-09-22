# Ahrefs — Brand Radar launch coverage — access attempt (Business Wire blocked)

```yaml
source:          attempted: Business Wire (businesswire.com), "Ahrefs Launches Custom AI Prompt Tracking for Brand Visibility"
url_or_doc_id:   https://www.businesswire.com/news/home/20260120714417/en/Ahrefs-Launches-Custom-AI-Prompt-Tracking-for-Brand-Visibility (cited in `docs/raw/a-vendor-roster-2026-09-22.md` row 15, dated 2026-01-20)
published:       2026-01-20 (per the roster file's citation; not independently confirmed this session — see below)
pull_date:       2026-09-22
pull_method:     fetch (MCP_DOCKER fetch tool) — connection failure, not a bot-block
pull_purpose:    evidence about a number
tier:            n/a — no content retrieved
tier_reason:     access failed; no filing/press text obtained this pull
source_label:    n/a
lane:            A
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        error message only; no separate Ahrefs-owned blog post for the Brand Radar launch was located as a substitute (see notes)
```

## Verbatim

`mcp__MCP_DOCKER__fetch` on the Business Wire URL: `"Failed to fetch robots.txt https://www.businesswire.com/robots.txt due to a connection issue"` — repeated on a second attempt with the identical result. This reads as a transient connectivity failure (the tool could not resolve/reach businesswire.com's robots.txt at all, distinct from the explicit 403 "Undeclared Automated Tool" bot-block pattern seen on sec.gov elsewhere in this cluster), not a deliberate block — but it was not resolved within this session's time budget.

Substitute attempts, both failed: `ahrefs.com/blog/introducing-brand-radar/` → HTTP 404. `ahrefs.com/case-studies` → HTTP 404 (see `a-ahrefs-customers-2026-09-22.md` for the case-study access notes).

## Pull notes — mechanical only

- **Recorded: Brand Radar launch-post verbatim text — unknown — checked businesswire.com (connection failure, two attempts), ahrefs.com/blog/introducing-brand-radar (404) — 2026-09-22.**
- The roster file (`a-vendor-roster-2026-09-22.md` row 15) independently confirms the release's existence, headline, publisher, and date (2026-01-20) via a prior pull; this task's own attempt to retrieve the release body failed. The launch date **2026-01-20** is therefore carried forward from the roster file's citation, not independently re-verified by this pull, and is flagged as such in the census summary.
- Ahrefs's own `/brand-radar` product page (see `a-ahrefs-brand-radar-product-2026-09-22.md`) is undated and does not itself state a launch date — it is not a substitute for the launch post.
- The product/feature framing itself — "Turn SEO into AEO," "Track visibility two ways" (Custom Prompts vs. AI Visibility Index), 454M-prompt index — is fully captured in the sibling product and method files and is not repeated here.
