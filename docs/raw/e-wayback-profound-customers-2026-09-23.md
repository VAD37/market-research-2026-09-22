# Wayback Machine — Profound /customers page: customer-story count and logo count per capture, 2025-01 to 2026-09

```yaml
source:          web.archive.org captures of https://www.tryprofound.com/customers, plus the live page
url_or_doc_id:   http://web.archive.org/cdx/search/cdx?url=www.tryprofound.com/customers&output=json&filter=statuscode:200&collapse=timestamp:6 ; captures at http://web.archive.org/web/<timestamp>id_/https://www.tryprofound.com/customers ; https://www.tryprofound.com/customers (live)
published:       each capture's own timestamp; live 2026-09-23
pull_date:       2026-09-23
pull_method:     fetch (curl, User-Agent "market-research-bot contact: research@example.invalid"); per capture, count of distinct `href="/customers/<slug>"` links (case-study pages) and of `alt="…"` image labels other than "Profound"/"logo" (customer logos), plus the first h1–h3 headings; counted by script
pull_purpose:    evidence about a number
tier:            5
tier_reason:     the page is the vendor's own claim of who uses it at that date (demand-signals.md S2, "logos are not contracts"); Wayback capture is that claim as of the capture date; counts are ours over what the archived HTML rendered
source_label:    vendor-reported (page content); measured-by-us (counts)
lane:            E
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none — extends docs/raw/a-profound-customers-2026-09-22.md with dated history
captured:        CDX list; per capture, byte size, story-link count, logo-alt count, first headings; live-page stat callouts
verbatim:        headings and callouts verbatim; counts computed
```

## CDX capture list — one per month, status 200 (18 captures)

20250124125415 (16342), 20250216104642 (18449), 20250326032024 (16249), 20250428011615 (16292), 20250530215914 (18109), 20250627020408 (18636), 20250806130003 (19818), 20250902191921 (16813), 20251007233706 (23239), 20251126152539 (29125), 20251209004415 (26519), 20260221050725 (27850), 20260306014209 (28153), 20260409060819 (31328), 20260514043841 (32793), 20260701111457 (28862), 20260803125134 (28815), 20260903150404 (28888). [note: bracketed value is CDX `length`, the compressed record length.]

Also in CDX: www.tryprofound.com/ (home) 27 monthly captures from 20240713034739 to 20260901081027 — listed, not fetched.

CDX returned no captures (empty response) for peec.ai/customers, otterly.ai/customers, scrunchai.com/customers, scrunch.com/customers, athenahq.ai/customers.

## Per-capture counts — 8 captures fetched (7 archived + live)

| Capture (UTC) | Bytes (decompressed) | Distinct `/customers/<slug>` story links | Customer logo `alt` labels | First headings, verbatim |
|---|---|---|---|---|
| 2025-01-24 12:54:15 | 85,030 | 1 | 9 | "Meet the teams who are using Profound"; "From Invisible to Top 5: How 1840 & Co. Achieved 11% AI Visibility"; "Rho is a business banking platform, purpose-built for startups."; "MongoDB is the world's most versatile developer data platform."; "Indeed is the global job matching and hiring platform." |
| 2025-04-28 01:16:15 | 85,220 | 2 | 0 | "Meet the teams who are using Profound"; "From Invisible to Top 5: How 1840 & Co. Achieved 11% AI Visibility"; "How Ramp Increased AI Brand Visibility 7x in Accounts Payable"; "We help every company understand and control their AI presence"; "The teams we empower" |
| 2025-08-06 13:00:03 | 114,348 | 5 | 0 | "Meet the teams who are using Profound"; "How Statsig Took Control of Their AI Presence In Less Than a…"; "How Ramp Increased AI Brand Visibility 7x in Accounts Payable"; "How Lake.com 5x'ed Branded Traffic by Tapping Into AI Search" |
| 2025-11-26 15:25:39 | 177,838 | 7 | 1 | "Meet the teams who are using Profound"; "Hone Boosts Visibility by 800% Using AI-Optimized Content Wo…"; "From Invisible to Unmissable: One Identity's Rise to #1 in C…"; "How Statsig Took Control of Their AI Presence In Less Than a…" |
| 2026-03-06 01:42:09 | 179,518 | 10 | 3 | "Meet the teams who are using Profound"; "How Omnilux Tripled AI-Attributed Revenue"; "How CRS Credit API Increases AI Visibility 20x with Profound"; "How OpusClip achieved 45% brand visibility and #1 citation s…" |
| 2026-07-01 11:14:57 | 203,947 | 18 | 4 | "Meet the teams who are using Profound"; "How Kiteworks Outranked Microsoft in AI Search with Profound"; "How Arizona College of Nursing Increased AI-Referred Traffic…"; "Alchemy Drives a 7x Higher Signup Rate From AI-Referred Traf…" |
| 2026-09-03 15:04:04 | 212,886 | 20 | 4 | "Meet the teams who are using Profound"; "How MongoDB increased AI Search visibility by 50% while savi…"; "How WHOOP turned AI accuracy monitoring into a correction en…"; "How Optro measured and accelerated their rebrand with Profou…" |
| 2026-09-23 live | 223,813 | 21 | 21 | "Meet the visionary teams using Profound"; "The impact so far"; "All stories"; "How Plaid grew Answer Engine referral traffic 300% with Profound"; "How MongoDB increased AI Search visibility by 50% while saving time with Profound"; "How WHOOP turned AI accuracy monitoring into a correction engine" |

Live page stat callouts ("The impact so far"), verbatim: "50% — increase in Plaid's AI Search visibility while saving time w[ith Profound]"; "30% — Time saved using Profound Agents"; "100x — Increase in monthly revenue from AI systems for one client."; "4x — More referrals from Answer Engines".

[note: the logo `alt` count is not comparable across captures — the page's logo markup changed (0 labelled logos in three captures where logos were images without alt text or rendered by script). The story-link count is the more stable series. Headings are truncated at 60 characters by the extraction step where marked "…".]

## Pull notes — mechanical only

- Two captures (2025-01-24, 2025-04-28) came in the first batch as gzip bodies and were decompressed; five more fetched on a retry after the first attempt timed out (curl exit 000) for 2025-08-06, 2025-11-26, 2026-03-06, 2026-07-01, 2026-09-03.
- The live page was fetched once, same UA, HTTP 200.
- Counts by script: `href="(/customers/[^"#?]+)"` distinct; `alt="([^"]{2,60})"` distinct excluding "profound", "logo", "profound logo", empty.
- No login, no form.
