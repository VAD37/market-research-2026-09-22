# Wayback Machine — archive check, OpenAI "Testing ads in ChatGPT"

```yaml
source:          Internet Archive Wayback Machine (archiving openai.com)
url_or_doc_id:   https://web.archive.org/web/20260211230814/https://openai.com/index/testing-ads-in-chatgpt/
published:       2026-02-09 (page's own "Originally published" date; archive capture timestamp 2026-02-11T23:08:14Z)
pull_date:       2026-09-22
pull_method:     browser extension
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default (platform primary via archive, per channels.md C61)
source_label:    company-stated
lane:            B
sub_market:      paid placement
engine:          ChatGPT — OpenAI
metric_kind:     none
supersedes:      none
captured:        section "originally published" text only — comparison check, not full re-capture
```

## Verbatim

[note: per task instructions this pull checks the archive channel (channels.md C61) for a withdrawn or changed version of `openai.com/index/testing-ads-in-chatgpt/`, the primary target already fully captured verbatim today in `docs/raw/b-openai-testing-ads-chatgpt-2026-09-22.md`. To avoid a second full-page verbatim reproduction of the same OpenAI text, this file records the comparison result rather than repasting the entire archived body.]

Earliest capture found via web.archive.org for this URL close to its stated original-publication date: capture timestamp 2026-02-11T23:08:14Z (page requested at timestamp 20260215000000, archive.org resolved to nearest capture 20260211230814).

The archived 2026-02-11 capture's body — page title "Testing ads in ChatGPT | OpenAI", dated "February 9, 2026" on the page, no update-log entries present — is **word-for-word identical** to the "Originally published on February 9, 2026" section of the live page as captured today in `docs/raw/b-openai-testing-ads-chatgpt-2026-09-22.md` (the paragraphs under "Today, we're beginning to test ads in ChatGPT in the U.S." through "What will always remain true: ChatGPT's answers remain independent and unbiased, conversations stay private, and people keep meaningful control over their experience."). No word-level difference found between the archived original and the live page's retained original section.

The live page's three dated update blocks (March 26, 2026; May 7, 2026; August 11, 2026 — captured in full in `b-openai-testing-ads-chatgpt-2026-09-22.md`) are **absent** from this 2026-02-11 capture, consistent with those updates being appended to the page after this capture date — additive, not a rewrite of the original.

## Pull notes — mechanical only

- Accessed via Chrome extension: `web.archive.org` root and direct snapshot URLs returned 200 to this method; a plain-fetch attempt was not separately retried this pull since channels.md C61 already records "WebFetch refused 2026-09-22 → ext" from the P1-b red-team.
- `archive.org/wayback/available` API returned HTTP 429 (Too Many Requests) on first attempt; direct navigation to a dated snapshot URL (`web.archive.org/web/20260215000000/https://openai.com/index/testing-ads-in-chatgpt/`) succeeded and was redirected by archive.org to its nearest actual capture, 2026-02-11.
- **Finding: no withdrawal, no wording change found for this page.** The page has been edited only by addition (three dated updates appended above the original body over time), not by silent rewording of the original text. This is the only archive check performed in this cluster; the remaining P2-c3 target pages were all live, current, and (where dated) carried visible in-page changelogs (see `b-openai-ad-policies-2026-09-22.md`'s six-version changelog) rather than showing signs of silent withdrawal, so no further archive checks were run against them within this cluster's scope.
