# Similarweb country cuts and OpenAI DSA per-member-state user counts — channel walls

```yaml
source:          Similarweb (similarweb.com, data.similarweb.com); OpenAI (openai.com policies); web.archive.org
url_or_doc_id:   https://www.similarweb.com/website/chatgpt.com/ ; https://data.similarweb.com/api/v1/data?domain=chatgpt.com ; https://openai.com/policies/dsa-monthly-active-recipients/ ; https://web.archive.org/web/2026id_/https://openai.com/policies/dsa-monthly-active-recipients/ ; http://web.archive.org/cdx/search/cdx?url=openai.com/policies/*&collapse=urlkey&limit=200 ; http://web.archive.org/cdx/search/cdx?url=openai.com/*&filter=original:.*dsa.*
published:       n/a
pull_date:       2026-09-23
pull_method:     fetch (curl)
pull_purpose:    evidence about a number (result: walls; no number obtained)
tier:            n/a — no content captured
tier_reason:     no source text reached; file records access results only
source_label:    n/a
lane:            A
sub_market:      n/a
engine:          ChatGPT
metric_kind:     none
supersedes:      none
captured:        access results only
```

## Verbatim — access results

| URL | HTTP | Body | Result |
|---|---|---|---|
| similarweb.com/website/chatgpt.com/ | 202 | 0 bytes | empty 202 — bot challenge / deferred render; no "Top Countries" block served |
| data.similarweb.com/api/v1/data?domain=chatgpt.com | 403 | CloudFront "ERROR: The request could not be satisfied" | legacy public endpoint refused |
| openai.com/policies/dsa-monthly-active-recipients/ (guessed slug) | 403 | 9,904 bytes | openai.com bot wall on curl (same as earlier pulls in this repo) |
| web.archive.org/web/2026id_/…/dsa-monthly-active-recipients/ | 404 | "The Wayback Machine has not archived that URL." | slug not archived (may not exist) |
| CDX openai.com/policies/* (collapse=urlkey, limit 200) | 200 | 0 rows matching "dsa", "recipient" or "eu" | — |
| CDX openai.com/* filter original:.*dsa.* | connection failed twice (curl wrote no file) | — | not retried further |

## What the repository already holds on this point

- OpenAI's DSA transparency page (`docs/raw/b-eu-openai-dsa-transparency-2026-09-22.md`) states one EU-wide figure only: "For the six-month period ending 31 March 2026, ChatGPT search had approximately 159.1 million average monthly active recipients in the European Union." No per-member-state breakdown on that page.
- The Commission's designated-services list (`docs/raw/b-eu-ec-designated-vlops-vloses-list-2026-09-22.md`) carries the same 159.1 figure for the VLOSE designation of 31.08.2026, EU-wide.
- Microsoft's Bing DSA page (`docs/raw/b-eu-microsoft-dsa-bing-2026-09-22.md`): "approximately 155 million" EU average monthly active users, period ending 2025-12-31, EU-wide only.

Per-member-state ChatGPT / Bing recipient counts: **unknown — checked openai.com (403), web.archive.org (no capture), and the three existing DSA raw files 2026-09-23.** Similarweb per-country assistant traffic share: **unknown — checked similarweb.com (202 empty) and data.similarweb.com (403) 2026-09-23.**

## Pull notes — mechanical only

- No Chrome extension or Playwright used (both slots held by other agents); Similarweb's website pages are known to render country data client-side, so the empty 202 is consistent with a fetch-only boundary rather than a permanent wall.
- The DSA Art. 24(2) duty is an EU-wide average; a per-state split is not required by the Article and none of the three engines' pages already pulled publishes one.
