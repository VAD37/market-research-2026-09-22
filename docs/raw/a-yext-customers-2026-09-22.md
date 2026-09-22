# Yext — customers / testimonials for Scout, graded on intake

```yaml
source:          Yext (yext.com)
url_or_doc_id:   https://www.yext.com/platform/scout (4 testimonials, quoted in full); https://www.yext.com/customers (general case-study listing, 3 items, not Scout-specific)
published:       undated
pull_date:       2026-09-22
pull_method:     fetch (MCP_DOCKER fetch tool, plain HTTP — claude-in-chrome extension reported "not connected" this session)
pull_purpose:    evidence about a number
tier:            6
tier_reason:     vendor-selected testimonials, no independent measurer, no quantified metric in any of the four Scout-specific quotes (see grading below) — default tier 6
source_label:    vendor-reported
lane:            A
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        four testimonials verbatim (from `/platform/scout`, already captured in full in `a-yext-scout-product-2026-09-22.md`, reproduced here for grading); three case-study titles/snippets from `/customers`
```

## Verbatim

### Four Scout-specific testimonials (from /platform/scout)

"'With AI shaping how people find us, it's important to understand our online presence. Scout shows us exactly what the public sees, eliminating guesswork and improving our strategy.' — Austin Robinson, Sr. Website Manager, MidFirst Bank"

"'From understanding how customers and competitors show up in search to identifying gaps in visibility across locations, Scout gives us the clarity and tools to improve fast.' — Senior Marketer, Automotive [brand and individual name not given, industry only]"

"'Scout's a big part of how we can understand how locations are showing up in local search — both in AI and in Google. It helps us to understand what they're showing up for, and, more importantly, what they're not showing up for. Then, Scout is showing us how to optimize content on the knowledge graph so Sorbet can speak to those unbranded searches and appear for them.' — Leanne Levine, Local Digital Lead [company named elsewhere on the Yext homepage as Sorbet, a franchise brand]"

"'Scout allows us to be even more engaged with our network owners and their performance. The insights provided allow for constant optimization which, ultimately, drives more traffic to our clinics.' — Leonard Sullivan, Digital Marketing Manager, Beltone"

### Three general case studies (from /customers — NOT Scout/AI-visibility specific)

"Case Study: Samsung Increases Customer Satisfaction and Streamlines the Resolution Journey with Yext Help Site Search — Within just a few months, Samsung experienced a significant lift in NPS and CSAT by launching a Yext-powered Help Site." [product: Yext Search/Help Site, not Scout]

"Case Study: Fazoli's Uses Yext to Triple Online Sales — Fazoli's sees 3.6x growth in online sales after kicking off a Yext-assisted digital transformation." [product not specified as Scout; general "digital transformation"]

"Case Study: Cox Communications Provides Direct Answers to Customer Questions With Yext — Using Yext Search, Cox Communications experienced a 51% increase in site search conversion rate and a 59% decrease in repeat on-site searches." [product: Yext Search, not Scout]

## Grading against the seven-item evidence bar

**All four Scout-specific testimonials (MidFirst Bank, Automotive, Sorbet, Beltone) contain zero quantified metrics.** Each names a role and a qualitative benefit ("clarity", "eliminating guesswork", "drives more traffic") with no number, percentage, date, or baseline of any kind. **None can be graded against the evidence bar — all four fail on their face at item 6 (no traffic volume or sample size stated) and item 3 (no date window), in addition to lacking a named engine (item 2) and a named/independent measurer (item 7).** These are recorded as **screened, not gradable — no quantified claim present**, distinct from "screened-not-pulled" (which implies a metric existed but the source wasn't opened further).

**The three /customers listing items are about Yext Search/Help Site and general "digital transformation," not about Scout or AI-visibility specifically — out of scope for this cluster's feature-specific case-study requirement, and not graded here.** (Fazoli's "3.6x growth in online sales" would otherwise be a strong Fools-gold-or-better candidate — revenue claim, no engine, no absolute date, no control — but it is not a Scout/AEO claim on its face and was not opened further to check.)

**The strongest quantified Scout-specific claims found for Yext are not on this page at all — they are the three claims embedded in the launch press release, graded in `a-yext-launch-2026-09-22.md`: Bronze (186% citation increase, hearing care provider), Fools gold (doubled leads, programmatic ad platform), and one discard-on-sight vendor-self-measurement (Yext's own 147% visibility growth).**

## Pull notes — mechanical only

- Both source pages were fetched in full for other purposes this cluster (`/platform/scout` fully captured in `a-yext-scout-product-2026-09-22.md`; `/customers` fetched fresh for this file, single call, no truncation marker, 3 items — no pagination control observed, page appears to show its complete current roster).
- **Screened / graded summary for this file: 4 Scout-specific testimonials screened, 0 gradable (no quantified metric in any). 3 general (non-Scout) case studies screened and excluded as out of scope for the feature-specific requirement. Combined with the 3 claims graded in `a-yext-launch-2026-09-22.md` (Bronze, Fools gold, and 1 discard-on-sight), Yext's overall best grade across this cluster's two customer-evidence files is Bronze.**
