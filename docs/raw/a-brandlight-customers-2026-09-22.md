# Brandlight AI — customers / case studies

```yaml
source:          Brandlight AI (brandlight.ai)
url_or_doc_id:   https://brandlight.ai/ (homepage testimonials); https://brandlight.ai/product/visibility-insights (repeated testimonials); https://brandlight.ai/ai-visibility-for-iconic-brands ("Trusted by Iconic Brands" section, empty of names in captured render); https://pulse2.com/brandlight-30-million-series-a-raised-for-enterprise-ai-visibility-platform/ (named customer list); https://brandlight.ai/blog/brandlight-named-leader-in-cb-insights-esp-ranking-for-generative-engine-optimization (named customer list)
published:       Pulse2 article 2026-02-11; CB Insights blog post 2025-12-03 (byline "03 Dec 2025"); homepage/product pages undated
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about category noise (testimonials, no n) and evidence about a number (named logos)
tier:            6 for the testimonial quotes (no n, no method); 5 for the named-customer-list claims (company-stated, no case-study metric attached)
tier_reason:     testimonial quotes carry no date, no metric, no method — discard-on-sight per trust-rubric.md's "no n, no date window, or no method" unless recorded as category-noise evidence, which is how they are filed here; the named-logo lists are treated separately as customer-count evidence, not as case-study proof claims
source_label:    vendor-reported (testimonials, logos); analyst-derived pointer (CB Insights ESP ranking, methodology not independently pulled)
lane:            A
sub_market:      organic recommendation
engine:          not named in any customer-facing claim
metric_kind:     none
supersedes:      none
captured:        homepage testimonial block (3 quotes, repeated twice on the page); "iconic brands" page testimonial section header (form-gated, no names rendered); named-customer sentences from two third-party-hosted but company-sourced pages
```

## Verbatim

No dedicated `/customers` or `/case-studies` URL exists in Brandlight's own `sitemap.xml` (checked in full, 2026-09-22). Customer evidence on Brandlight's own domain is limited to three repeated homepage/product-page testimonial quotes and one gated "Trusted by Iconic Brands and the CMO's who lead them" section heading with no names rendered in this pull (likely a logo carousel requiring JS execution not captured by simplified fetch).

### Testimonial quotes (homepage and `/product/visibility-insights`, identical text on both, repeated twice per page)

"The Brandlight platform has been essential in providing the visibility we needed and we're highly impressed with the ongoing development of new capabilities and modules within the platform." — Garrett Tubbs, Director, Digital Marketing

"With Brandlight, we gain full clarity into our AI visibility - transforming insights into measurable growth, smarter positioning, and stronger customer reach." — Kady Srinivasan, CMO

"With Brandlight, we can finally measure and improve our AI-driven visibility - turning discovery into revenue, competitive edge, and expansion." — Aaron Goldman, CMO [Aaron Goldman is separately named as "Chief Marketing Officer at Mediaocean" on Brandlight's own `/about` page, Advisory Board section]

None of the three names a company beyond a title, a metric, an engine, a date window, or a baseline. **Graded: none clear even Bronze — no quantified claim of any kind, not even a visibility percentage. Screened, not pulled as individual case-study files.**

### Named customers (company-sourced content hosted on third parties)

Pulse2, 2026-02-11, reporting Brandlight's own Series A announcement: "Brandlight said it has worked with hundreds of large brands and that its platform is used by Fortune 500 companies, including Kimberly-Clark, LG, The Hartford, and Estée Lauder, to guide decision-making in AI-driven discovery and media."

Brandlight's own blog, "Brandlight Named Leader in CB Insights ESP Ranking for Generative Engine Optimization," Rosario Cutuli (Head of Marketing), 03 Dec 2025: "With clients including Estée Lauder, Kimberly-Clark, Samsung, and Aetna, Brandlight's enterprise-first architecture and comprehensive data infrastructure enable organizations to scale as this channel matures..."

Combined named-customer set across both company-sourced pulls: Kimberly-Clark, LG, The Hartford, Estée Lauder, Samsung, Aetna (6 named logos). Neither source attaches a metric, date window, baseline, or engine to any named customer — these are logo/name mentions only, not case studies. **No individual claim here clears even Bronze; recorded as a logo count for the census, not graded as case studies.**

### CB Insights "Leader" ranking (analyst-derived pointer, not independently pulled)

"CB Insights has recognized Brandlight as a Leader in their latest Emerging Service Provider (ESP) ranking for Generative Engine Optimization (GEO) monitoring platforms... Access the full report here [link, not followed this pull]." This is a third-party analyst ranking cited by the vendor; CB Insights' own methodology page was not pulled this task (out of scope — not a Brandlight-domain page). Recorded as a positioning claim, tier 6 on this vendor's own retelling (no n, no scoring criteria disclosed on Brandlight's page), pull_purpose evidence about category noise.

## Pull notes — mechanical only

- Homepage, `/ai-visibility-for-iconic-brands`, and `/product/visibility-insights` fetched via mcp__MCP_DOCKER__fetch, simplified/markdown rendering; the "Trusted by..." logo sections rendered as empty headers with no logo/name text in the simplified markdown output on all three pages — likely a client-side logo carousel or image-based section not captured by text extraction. [note: logo carousel content not captured — page uses images or JS-rendered names not present in the simplified text extraction]
- Pulse2 and Brandlight's own CB Insights blog post fetched in full (Pulse2) and to 3500 characters (blog post, truncated after the "Strategic Imperative" section).
- No case-study or customer-story page exists on brandlight.ai as of this pull — the entire customer-evidence surface on this vendor's own site is testimonial quotes plus named-logo mentions in funding/award announcements, none of which name a metric.
