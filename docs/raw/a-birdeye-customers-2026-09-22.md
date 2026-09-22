# Birdeye — customers / testimonials, graded on intake

```yaml
source:          Birdeye (birdeye.com)
url_or_doc_id:   https://birdeye.com/search-ai (2 testimonials); https://birdeye.com/pricing (3 "Customer results" testimonials, not Search-AI-specific); attempted https://birdeye.com/case-studies (404)
published:       undated
pull_date:       2026-09-22
pull_method:     fetch (MCP_DOCKER fetch tool, plain HTTP — claude-in-chrome extension reported "not connected" this session)
pull_purpose:    evidence about a number
tier:            6
tier_reason:     vendor-selected testimonials, no independent measurer
source_label:    vendor-reported
lane:            A
sub_market:      organic recommendation
engine:          n/a
metric_kind:     traffic
supersedes:      none
captured:        five testimonials verbatim (already captured in full in `a-birdeye-search-ai-product-2026-09-22.md` and `a-birdeye-pricing-2026-09-22.md`, reproduced here for grading); one 404 for a dedicated case-study index
```

## Verbatim

### Search-AI-specific testimonials (from /search-ai)

"'AI Search has been one of those right-tool, right-time moments — helping us lay the foundation to show up better, with the right words in our community descriptions.' — Shannon Novak, Senior Managing Director of Marketing, Arrow Senior Living"

"'Birdeye has helped us tremendously with staying relevant amongst our competition. Our profiles are always updated, ensuring we never miss out on AI visibility.' — Pasjion Savage, Drucker and Falk"

### General "Customer results" testimonials (from /pricing — NOT Search-AI-specific)

"400% increase in social publishing — 'Birdeye Social allows us to post across locations while still connecting with our communities. We can post in bulk while keeping the voice of the practice without the tediousness of posting individually to each account.' — Meghan S. Bingham, CVPM, Senior Operations Manager, Valley Veterinary Care" [product: Birdeye Social, not Search AI]

"86% increase in direction requests — 'Birdeye does the hard work, making our jobs easier, and provides top-notch service to better your business.' — Brandon Wipperfurth, Director of Marketing, Superior Storage" [product not specified as Search AI]

"25% increase in digital interactions in just 6 months — 'Having a platform where everything is monitored in one place makes such a difference and has streamlined our approach to social media. This has such a huge impact on our processes and the amount of manpower it takes to keep up.' — Carly Dodd, Content Manager, Pacifica Senior Living" [context is social media, not Search AI specifically]

## Grading against the seven-item evidence bar

**Search-AI-specific testimonials (Arrow Senior Living, Drucker and Falk): both contain zero quantified metrics** — qualitative only ("show up better," "never miss out on AI visibility"). **Not gradable — screened, no quantified claim present.**

**General "Customer results" testimonials are not Search-AI-specific** (their own quotes reference "Social" and general platform use, not AI search/visibility) — **excluded from this cluster's feature-specific grading, per the task's scope**. For completeness, assessed against the bar anyway: each names a brand (item 1 ✓) and a percentage (implying item 6 as a rate, though no absolute traffic volume is given), but none states an engine (item 2 — not applicable, these aren't AI-search claims), an absolute date window (item 3 — "in just 6 months" is relative), a baseline (item 4), or a named/independent measurer (item 7). Even if these were in-scope, none would clear Bronze on its own product-relevance grounds; the "86% increase in direction requests" and "25% increase in digital interactions" claims would be Bronze-track (traffic/engagement, no revenue link) and "400% increase in social publishing" is an operational/output metric, not visibility/traffic/sales, so ungraded.

**The three homepage-level aggregate percentages on `/search-ai` ("30% AI visibility increase," "53% Increase in lead volume," "74% Recommendations accepted") are discard-on-sight per `trust-rubric.md` ("percentage with no base") — flagged in `a-birdeye-search-ai-product-2026-09-22.md`, not re-graded here.**

## Pull notes — mechanical only

- **Screened / graded summary for this file: 2 Search-AI-specific testimonials screened, 0 gradable (no quantified metric in either). 3 general (non-Search-AI) testimonials screened and excluded as out of scope, assessed hypothetically only. 3 aggregate homepage percentages discarded on sight per trust-rubric. No dedicated case-study index page was reachable (`birdeye.com/case-studies` → 404); the "Read the report" link on `/search-ai` (1,762-brand study) could not be resolved to a working URL either — see `a-birdeye-search-ai-product-2026-09-22.md`.**
- **Best grade found for Birdeye Search AI specifically: none — zero gradable case studies located this pull.** This is recorded as the finding for this incumbent's customer-proof pull, not padded (`plan.md`: "Do not pad the table to avoid it").
