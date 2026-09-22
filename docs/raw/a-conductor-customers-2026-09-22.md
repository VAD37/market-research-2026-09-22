# Conductor — customers / case studies, graded on intake

```yaml
source:          Conductor (conductor.com)
url_or_doc_id:   https://www.conductor.com/customer-stories/ (listing, 11 stories); https://www.conductor.com/customer-stories/title-nine/ (full case study)
published:       listing undated; Title Nine case study undated on-page (no byline date; discusses "In 2024" and "the beginning of the year to the end" as internal date references)
pull_date:       2026-09-22
pull_method:     fetch (MCP_DOCKER fetch tool, plain HTTP — claude-in-chrome extension reported "not connected" this session)
pull_purpose:    evidence about a number
tier:            6
tier_reason:     vendor-authored case study, self-reported, quotes are named individuals at the customer but no independent third-party measurer; default tier 6 per trust-rubric for a vendor case study lacking a disclosed n/method
source_label:    vendor-reported
lane:            A
sub_market:      organic recommendation
engine:          n/a
metric_kind:     traffic
supersedes:      none
captured:        listing page (full, single fetch); Title Nine case study (full, three fetch calls covering the whole page)
```

## Verbatim

### Listing — /customer-stories/ (11 titles, verbatim, with industry tag)

1. "HG Insights Launches AI Search Visibility Platform for B2B Tech Vendors Powered by Conductor" — Technology [no quantified metric in title]
2. "How Boston Globe Media Used Conductor Monitoring to Improve Technical AEO at Scale" — Other [no quantified metric in title]
3. "Title Nine Doubled AI Citations and Drove +1,000% AI Session Growth with Conductor" — Retail — graded in full below
4. "How Clutch Powered AI Search Visibility for 430,000+ B2B Providers with Conductor" — Technology [430,000+ is a scale figure, not a before/after metric]
5. "How Overdrive Powered AI Visibility for 22 Clients with Conductor Data & MCP" — Services [no quantified before/after metric]
6. "How Conductor Quadrupled Content Output YoY and Increased AI Citations +448%" — Technology [subject appears to be Conductor's own use of its product, not a third-party customer]
7. "Zurich UK Improved AI Citation Relevance and Accuracy with Conductor" — Finance [no quantified metric in title]
8. "How Parker Hannifin Tied AEO & SEO to Proven ROI with Conductor" — Manufacturing [no quantified metric in title]
9. "How H&R BLOCK Doubled AI Search Citations with Conductor" — Finance
10. "How Sonos Became a Leader in AI Search with Conductor" — Technology [no quantified metric in title]
11. "Brunswick Unified 6 Brands Under One Strategy with Conductor" — Manufacturing [no quantified metric in title]
12. "ASUG Switched to Conductor and Increased Efficiency by 75%" — Technology [efficiency, not a visibility/traffic/sales metric]

### Full case study — Title Nine (https://www.conductor.com/customer-stories/title-nine/)

Headline stats: "+1,000% growth in AI-driven sessions" / "+100% increase in AI traffic YoY" / "+400% increase in content velocity MoM"

Company: "Title Nine is a women-owned outdoor and athletic apparel company... Emeryville, CA... Company Size < 1,000... Industry Retail."

Before/After table (verbatim rows): "Manual, time-intensive content creation, limiting output to 1-2 articles per month | AI-assisted content creation scaling output to 10+ optimized articles per month, a 400%+ increase" / "No clear visibility into which category pages to create or where competitors outranked them | Data-driven category page strategy identifying net-new opportunities and competitive content gaps" / "Non-branded search visibility growing slowly without a focused strategy | Focused non-branded search strategy driving exponential growth across impressions, clicks, and traffic" / "No tooling or framework to track AI search performance and brand presence | Consistent weekly visibility into AI brand mentions, citations, and market share" / "Reactive, ad hoc technical SEO implementation | Proactive technical SEO roadmap executed in partnership with a dedicated consultant"

"### +18% revenue growth for swim category pages — ...Sports bra category pages saw: +3% growth in sessions, +3% growth in transactions, +11% growth in revenue. Across the broader swim category, the impact was even greater: +13% session growth, +14% transaction growth, +18% revenue growth." Quote: "It's been awesome to tie the work we've been doing with Conductor back to the performance of these categories." — Carlie Burkhard, Senior Manager of eCommerce, Title Nine.

"### +134% non-branded impressions and +30% organic traffic growth YoY — ...'In 2024, we increased our non-branded impressions by 134%, clicks by 50%, and overall organic traffic by 30%.' — Carlie Burkhard, Senior Manager of eCommerce, Title Nine."

"### +1,000% AI session growth and rising brand mentions in AI search — ...The results were significant: +1,000% growth in AI-driven sessions from the beginning of the year to the end. AI traffic up 100%+ YoY on a consistent weekly basis. AI citations increased by 100%+ over the course of the year. Brand mentions increased by 33%+ over the same period." Quote: "Conductor has consistently kept AEO at the forefront of the conversation..." — Sarah Cosentino, Senior eCommerce Specialist, Title Nine.

**Grading against the seven-item evidence bar — split by claim, since the case bundles several metrics:**

**Claim A — "+1,000% growth in AI-driven sessions", "+100% AI traffic YoY", "AI citations increased by 100%+", "brand mentions increased by 33%+":**
1. Brand — Title Nine, named. ✓
2. Engine(s) — not named (generic "AI search", "AI-driven sessions" — no ChatGPT/Perplexity/etc. named for these specific figures). ✗
3. Absolute date window — partial: "from the beginning of the year to the end" / "over the course of the year" — a calendar-year window is implied but no year number or exact dates are stated in the excerpt captured. ✗ (not absolute)
4. Baseline before intervention — ✗ not stated as an absolute count (percentages only)
5. Intervention — Conductor Intelligence / AEO strategy, described. ✓
6. Sample size / traffic volume — ✗ not stated
7. Who measured, paid-by-outcome — ✗ not stated (named customer employees, self-reported via vendor case study; no named independent measurer)

**Grade: Bronze.** This bundle is visibility/traffic-only (sessions, traffic, citations, mentions) with no revenue crossing stated for these specific figures. Missing bar items 2, 3, 6, 7.

**Claim B — "+18% revenue growth" (swim category), "+11% revenue growth" (sports bra category):**
Same gaps as Claim A on items 2, 3, 6, 7, but this claim additionally crosses into revenue. Per `glossary.md`'s crossing rule, an ungraded crossing from visibility/traffic to sales is downgraded to the weaker metric grade — but because this specific figure is a **revenue** number attached to a broader "category page strategy" (not explicitly isolated to AI-search-driven traffic; the case text attributes it to "Conductor Intelligence" category-page work generally, blending SEO and AEO), and it has a partial baseline (the % deltas imply but do not state absolute before/after revenue figures) and no control metric: **Grade: Fools gold** — a revenue claim without a stated absolute baseline or an unaffected control metric, and not cleanly isolated to the AI-search channel this task is scoped to.

**Claim C — "ASUG... Increased Efficiency by 75%" and "Conductor Quadrupled Content Output YoY... +448%" (from the listing, not opened in full):** operational/productivity metrics, not visibility/traffic/sales per `glossary.md` — **not graded** (out of scope for the evidence-bar table; recorded as screened-not-pulled).

## Pull notes — mechanical only

- `/customer-stories/` listing fetched in full, single call, no truncation marker — 12 titles captured (11 distinct "Show more" cards plus the header story), believed complete for this listing page (no pagination control observed in the rendered text).
- Title Nine case study fetched across three calls (0–4000, 4000–7000, 7000–10000+) to reach the end of the visible body; a final "Turn your searc[h]..." CTA section was cut off at the last call's limit — believed to be boilerplate (no further quantified claims expected past that point based on the page's own section structure) but not confirmed complete. `unknown — checked conductor.com/customer-stories/title-nine 2026-09-22` for the final CTA section's exact text.
- **Screened / graded summary for this file: 12 case-study titles screened, of which 1 (Title Nine) was pulled in full and graded across three claim-bundles (Bronze for the AI visibility/traffic bundle; Fools gold for the revenue bundle; 2 operational-metric claims left ungraded as out of scope). The remaining 11 listing entries are screened-not-pulled — several name a brand and a scale or percentage figure in their title (e.g. "430,000+ B2B Providers", "Doubled AI Search Citations", "+448%") but were not opened to check the remaining bar items.** Best grade found in this cluster: **Bronze**. No case screened or graded here clears Silver or Gold.
