# Google Search — spam policies (expired domain abuse, site reputation abuse)

```yaml
source:          Google (Google Search Central developer documentation)
url_or_doc_id:   https://developers.google.com/search/docs/essentials/spam-policies
published:       last-updated 2026-08-28 (per page's own timestamp)
pull_date:       2026-09-22
pull_method:     fetch (WebFetch)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary, own documentation
source_label:    company-stated
lane:            D
sub_market:      organic recommendation
engine:          Google Search (the page governs Google Search generally; does not itself distinguish AI Overviews/AI Mode ranking from classic web ranking — same scope caveat as the already-landed scaled-content-abuse pull from this page)
metric_kind:     none
supersedes:      none — this is a new pull of the same URL already landed as `docs/raw/d-review-google-spam-policies-2026-09-22.md` (P5-c2) and `docs/raw/d-seeding-google-spam-policies-2026-09-22.md` (P5-c1), each capturing a different section; this file captures the "Expired domain abuse" and "Site reputation abuse" sections neither prior pull captured. Filed as a distinct topic pull under the raw-pull template's re-pull rule, not a supersession
captured:        the "Expired domain abuse" and "Site reputation abuse" policy definitions and examples, via a targeted WebFetch query against the same URL two prior clusters already pulled for different sections
technique:       comparison-page farming
models_tested:   n/a
date_window:     n/a
measured_effect: no — this is a policy page, not a measurement
vertical:        none named — policy applies to all content categories indexed by Google Search
```

## Verbatim

### "Expired domain abuse" (quoted as returned by WebFetch)

"Expired domain abuse is where an expired domain name is purchased and repurposed primarily to manipulate search rankings by hosting content that provides little to no value to users."

Illustrative examples, quoted as returned: "Affiliate content on a site previously used by a government agency; Commercial medical products being sold on a site previously used by a non-profit medical charity; Casino-related content on a former elementary school site."

[note: this directly names "affiliate content" as an illustrative example of expired-domain abuse — the task's "rented domains" framing for comparison-page farming matches this policy's own "repurposed" framing, though the policy's own examples do not name comparison or "vs" pages specifically]

### "Site reputation abuse" (quoted as returned by WebFetch)

"The site reputation policy applies where third-party content is published on a host site mainly because of that host's already-established ranking signals, which it has earned primarily from its first-party content."

On affiliate links specifically, quoted as returned: the policy treats "Using affiliate links throughout a page" as **not** inconsistent with the policy "when links [are] treated appropriately" — i.e. affiliate-linked comparison/review content is not automatically a violation under this clause on its own.

[note: neither clause, as captured by this pull, names "comparison pages," "best X" pages, or dedicated review/listicle content as a distinct category]

## Pull notes — mechanical only

- Fetched via `WebFetch` against `developers.google.com/search/docs/essentials/spam-policies`, same URL two prior Pass 5 clusters (P5-c1, P5-c2) already pulled for the "scaled content abuse" section and one review-guidance sentence. This pull ran a separate, targeted query against the same page for the "expired domain abuse" and "site reputation abuse" sections specifically, per this cluster's (P5-c3) task instruction to check for "site reputation abuse, expired-domain-abuse clauses."
- As with the two prior pulls of this page, `WebFetch` converts the page to markdown and answers a prompt against the converted content with a smaller model rather than returning byte-for-byte HTML; quoted strings above are reported by that tool as direct quotes, carrying the same processing caveat noted in the two prior pulls of this URL.
- Whether AI Overviews or AI Mode apply "expired domain abuse" and "site reputation abuse" identically to classic web results was not checked by this pull, consistent with the same unresolved question recorded in the two prior pulls of this page. `unknown — checked developers.google.com/search/docs/essentials/spam-policies only, 2026-09-22`.
