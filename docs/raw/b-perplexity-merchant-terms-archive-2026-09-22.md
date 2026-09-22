# Wayback Machine — Perplexity Merchant Program Terms of Service (prior state, now 404 live)

```yaml
source:          Internet Archive Wayback Machine (archived capture of perplexity.ai)
url_or_doc_id:   https://web.archive.org/web/20250716051449/https://www.perplexity.ai/hub/legal/merchant-program-terms-of-service
published:       undated on the archived page itself (capture indicates the live page existed as of the capture date below)
pull_date:       2026-09-22
pull_method:     browser extension
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary via archive; C61 in channels.md
source_label:    company-stated
lane:            B
sub_market:      paid placement
engine:          Perplexity
metric_kind:     none
supersedes:      none
captured:        capture-calendar metadata only; page body could not be recovered (see pull notes)
archive_capture_date: 2025-07-16 (Wayback timestamp 20250716051449)
```

## Verbatim

**Wayback CDX/calendar lookup for `https://www.perplexity.ai/hub/legal/merchant-program-terms-of-service`:**

"Saved 1 time July 16, 2025"

**Archived snapshot page metadata (browser tab title after navigating to the capture):**

"Perplexity Merchant Terms of Service"

**Wayback toolbar banner text, as injected into the archived page (mechanical, not page content):**

"1 capture
16 Jul 2025"

## Pull notes — mechanical only

- Queried via `web.archive.org` calendar view (`web.archive.org/web/2026*/<url>`, resolved by the Wayback UI to a full calendar showing "Saved 1 time July 16, 2025") and the plain-text CDX API (`web.archive.org/cdx/search/cdx?url=...&output=text`), both loaded via the Chrome extension after an initial denial on a differently-formed `http://` CDX request ("Permission denied for reading page content on this domain") — the `https://` form of the same endpoint worked.
- Navigated to the single capture at `https://web.archive.org/web/20250716051449/https://www.perplexity.ai/hub/legal/merchant-program-terms-of-service`. The browser tab's `<title>` resolved to "Perplexity Merchant Terms of Service," confirming the page existed under that title on the capture date, but **the page body rendered blank**: `get_page_text` returned "No text content found," and a direct JavaScript check found `document.body.innerText.length === 0` while `document.body.innerHTML.length === 7841` — i.e., markup was present in the DOM but no text had hydrated into it.
- Root cause, read from the captured markup: the live site is built on Framer (`<script ... src="https://events.framer.com/script/v2" data-fid="...">` present in the archived HTML), a client-side-rendered site whose page content is populated by JavaScript after load. The Wayback Machine's single crawl of this URL captured the empty pre-hydration HTML shell, not the rendered legal text — a known Wayback limitation for JS-rendered single-page applications, not a site-specific block.
- **No verbatim text of the former Merchant Program Terms of Service could be recovered from this or any other channel available to this pull.** This is recorded as `unknown — checked web.archive.org (1 capture, blank render), Google cache (not attempted — deprecated), site's own current pages 2026-09-22 — prior wording of the Merchant Program Terms of Service is not recoverable`.
- What **is** established, combining this file with the live-404 file: the URL existed under the title "Perplexity Merchant Terms of Service" as of 2025-07-16 (one Wayback crawl only — a single crawl is a lower bound on the page's actual lifespan, not a measurement of it) and returns a 404 as of the 2026-09-22 pull date. The window in which it was removed is bounded only as "after 2025-07-16, on or before 2026-09-22" — no finer resolution obtained.
- No other Perplexity ad- or publisher-programme path returned a "not found" result requiring an archive check in this cluster: `why-we-re-experimenting-with-advertising` (still live, see paired raw file) and `introducing-comet-plus` (still live, see paired raw file) needed no withdrawal check.
