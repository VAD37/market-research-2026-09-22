# Yext — launch/expansion press release (Scout AI-visibility expansion, GoShine), graded

```yaml
source:          Yext, Inc. Investor Relations (investors.yext.com), distributed via Business Wire
url_or_doc_id:   https://investors.yext.com/news-events/press-releases/detail/392/yext-expands-agentic-capabilities-to-grow-ai-visibility-for ; secondary: https://investors.yext.com/news-events/press-releases/detail/391/yext-announces-second-quarter-fiscal-2027-results
published:       2026-09-01, 8:00 am EDT (both releases)
pull_date:       2026-09-22
pull_method:     fetch (MCP_DOCKER fetch tool, plain HTTP — claude-in-chrome extension reported "not connected" this session)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     platform primary — company's own Investor Relations site, Business Wire distribution named explicitly in the body ("NEW YORK--(BUSINESS WIRE)--"); the two customer-metric claims embedded within it (186% citations, doubled leads) are vendor-selected, unnamed/anonymised customers with no independent measurer — graded below at their own standard, not elevated to tier 3
source_label:    company-stated
lane:            A
sub_market:      organic recommendation
engine:          n/a
metric_kind:     traffic
supersedes:      none
captured:        full text of detail/392 up to its truncation point (~6000 characters); bullet list and opening paragraphs of detail/391 (the same-day earnings release naming the completed GoShine acquisition)
```

## Verbatim

### Press release — "Yext Expands Agentic Capabilities to Grow AI Visibility for Enterprise Brands and Small Businesses"

"September 01, 2026 8:00 am EDT ... Yext adds brand-level AI visibility and AEO optimization to Scout and launches a new product purpose-built for SMBs

NEW YORK--(BUSINESS WIRE)-- Yext (NYSE: YEXT) today announced that it has expanded its agentic marketing platform to optimize more sources that AI cites and also launched an early version of a new SMB product: Corvo AI is a proactive agent purpose-built for small business owners. The announcements accompany Yext's results for its second quarter of fiscal 2027, issued today, and will also be featured at Envision, its customer conference on September 30, 2026."

"Many businesses are still observing the problem of AI visibility without a proven path to improve their visibility across these new AI answer surfaces. According to a Corporate Ink survey, 88% of CMOs and VP-level marketers are being asked by leadership or their board about AI visibility. Yet, only 34% of all marketers surveyed say they have a defined AI visibility strategy." [note: survey n, date window, and method not given in this release — third-party survey cited without its own methodology; not independently pulled this session]

"Scout is Yext's comprehensive answer to this problem for enterprises. **Scout has proven to help multi-location brands increase AI visibility at the local-level by increasing citations by 186% for one hearing care provider.** Now, Yext is expanding to offer brand and location-level AI visibility optimization across more sources that AI cites to capture intent at critical times in the consideration process. **In early use, the new capabilities have been shown to double inbound leads for a programmatic advertising platform.** **Yext used its own product to grow its AI visibility by 147% and win share of voice against two leading competitors in only two weeks.** Yext is currently piloting it with a small number of enterprise customers ahead of broader availability on September 30."

"Yext is also continuing to advance Action Center, which reached general availability for all customers on August 5. Action Center allows brands to manage and govern all Yext agents in one place. It now triggers and completes agentic actions surfaced by Scout across listings, reviews, social, and the Yext Knowledge Graph. New social actions include localizing brand posts and turning 5-star reviews into social content."

"Corvo AI is Yext's new small business agent harness... Corvo AI is available for free today at askcorvo.com."

"...We look forward to showcasing our rapidly expanding capabilities at upcoming customer events." Visit Yext.com to request a demo of the new Scout capabilities or visit AskCorvo.com for free access."

### Same-day earnings release — "Yext Announces Second Quarter Fiscal 2027 Results" (bullet list, verbatim)

"- Revenue of $111.1 million
- Net Income Per Share, basic, of $0.13; non-GAAP Net Income Per Share of $0.21
- Adjusted EBITDA of $34.0 million; Adjusted EBITDA margin of 31%
- ARR of $440.8 million
- **Completed acquisition of GoShine, expanding the Yext platform to brand-level visibility optimization for AI search**
- Released working prototype of Corvo AI (askcorvo.com) in August, a conversational platform that brings Yext's marketing agents to small business owners"

"Related Documents [on the earnings-release page]: 10-Q Filing (HTML, PDF, XBRL, ZIP); Shareholder Letter (PDF); Q&A (PDF)" — confirming this earnings release is the exhibit accompanying an SEC 10-Q/8-K filed the same day, 2026-09-01 — see `a-yext-filing-2026-09-22.md` for the direct-SEC-access attempt (blocked).

## Grading against the seven-item evidence bar

**Claim A — "increasing citations by 186% for one hearing care provider":**
1. Brand — "one hearing care provider" is anonymised but industry-specified; a borderline fit for "a credibly specified anonymised profile" (no size, geography, or other distinguishing detail beyond industry). ~partial 2. Engine — not named. ✗ 3. Absolute date window — not stated. ✗ 4. Baseline — not stated (percentage only). ✗ 5. Intervention — Scout, named. ✓ 6. Sample/traffic volume — not stated. ✗ 7. Who measured — not stated (Yext's own release, presumably Yext-measured). ✗
**Grade: Bronze** — a citations (visibility) claim only, no revenue crossing; missing items 3, 4, 6, 7 and a weak fit on item 1.

**Claim B — "shown to double inbound leads for a programmatic advertising platform":**
Same gaps as Claim A on items 2–4, 6, 7 (anonymised profile is if anything vaguer here — "a programmatic advertising platform," no further detail). This claim crosses into leads (revenue-adjacent). **Grade: Fools gold** — a revenue-adjacent claim with no baseline and no control.

**Claim C — "Yext used its own product to grow its AI visibility by 147% and win share of voice against two leading competitors in only two weeks":**
This is **Yext measuring its own product on itself** — explicitly named in `docs/method/trust-rubric.md`'s "Discard on sight" list as "Vendor measuring the thing it sells, no third-party replication." **Not graded against the evidence bar; recorded per trust-rubric's "pulled only as evidence about the category's noise level" rule (tier 6 for this specific claim), not cited as evidence of a number for Scout's effectiveness.**

**Claim D — "88% of CMOs... asked about AI visibility... 34%... have a defined AI visibility strategy" (Corporate Ink survey):** a third-party survey statistic cited without n, date window, or method disclosed in this release — fails trust-rubric's "no n, no date window, or no method" discard-on-sight test as cited here. **Not graded; recorded as category-attention context only, per trust-rubric's tier-6/7 "evidence about category noise" allowance. The Corporate Ink survey itself was not independently pulled this session — `unknown — checked investors.yext.com only 2026-09-22`.**

## Pull notes — mechanical only

- `detail/392` fetched with max_length 6000; the page's full visible body was captured (ends at the standard IR-site footer boilerplate, not mid-sentence).
- `detail/391` fetched separately (see `a-yext-filing-2026-09-22.md` for its full pull record); only the bullet list and opening paragraphs are reproduced here for the GoShine-completion date context.
- The original GoShine **acquisition-announcement** date (as opposed to this September 1 "completed acquisition" disclosure) was not independently located this session — `unknown — checked investors.yext.com/news-events/press-releases (10 most recent releases listed, none titled specifically "GoShine") 2026-09-22`. The roster file (`docs/raw/a-vendor-roster-2026-09-22.md` row 14) cites this same Q2 FY27 earnings release as its GoShine source, consistent with this pull.
