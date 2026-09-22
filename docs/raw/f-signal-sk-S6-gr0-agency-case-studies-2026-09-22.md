# GR0 (agency) — GEO service and skincare/beauty case-study roster

```yaml
source:          GR0 (performance-marketing agency, gr0.com)
url_or_doc_id:   https://gr0.com/case-studies/; https://gr0.com/case-study/luxury-skincare-brand
published:       2026-04-28 (case study, per its own listed date); case-studies index undated
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            6
tier_reason:     dropped from expected tier "3 existence / 6 framing" (demand-signals.md S6) to 6 throughout — no list price or rate card was found on the pricing page for the GEO service line (JS-rendered, static fetch returned no price text), so only the framing/existence claim is usable, not a priced offer
source_label:    vendor-reported
lane:            F
sub_market:      organic recommendation
engine:          n/a — case study names Profound (a third-party AI-visibility measurement vendor) as the tracking tool, not an AI assistant engine itself
metric_kind:     visibility
supersedes:      none
captured:        case-studies index page (title/date list, full text extracted after stripping Framer/JS boilerplate); one full case-study page, same treatment
```

## Query — verbatim

`https://gr0.com/case-studies/` fetched directly (no site: search needed — GR0 was already identified as a GEO-offering agency in `docs/raw/f-agency-census-c5-2026-09-22.md` row 12, which screened the agency but did not pursue a beauty-specific check). This pull greps the fetched page text for `beauty|skincare|cosmetic` case-insensitive.

## Verbatim

Case-study titles matching beauty/skincare, with their listed dates, from the case-studies index (page text, HTML tags stripped):

- "How GR0 Made a Luxury Skincare Brand the #1 AI-Visible Brand in Personal Care" — Apr 28, 2026 — tag "SEO", URL slug `luxury-skincare-brand`
- "How We Took a Celebrity Beauty Brand and Increased Their Conversion Rate by 20%" — Apr 4, 2025 — tags "CREATIVE", slug `celebrity-beauty-brand`
- "Scaling No Makeup Makeup: From Zero to Consistent Growth" — Mar 17, 2025 — tags "PAID SOCIAL GOOGLE ADS SEO"
- "How We More Than Doubled This Skincare Brand's Conversion Rate With An Increase of 140%" — Mar 12, 2025 — tags "GOOGLE ADS CREATIVE", slug `skincare-brand`
- "How GR0 Doubled Lancer Skincare's Revenue on Paid Social and Increased Their ROAS by 58% in One Month" — Nov 11, 2024 — tags "PAID SOCIAL"
- "How GR0 Took This False Lashes Brand's Google Ads to the Next Level in the E-commerce Beauty Vertical" — Jun 5, 2024 — tag "GOOGLE ADS"

Full text of the one case study opened (`https://gr0.com/case-study/luxury-skincare-brand`), body content after Framer/CSS/font boilerplate stripped:

> "How GR0 Made a Luxury Skincare Brand the #1 AI-Visible Brand in Personal Care
> GEO
> #1 Visibility Score Rank in Profound for tracked prompts
> #1 Share of Voice across tracked product categories
> #1 For "best smelling deodorant"
> #2 For "aluminum-free deodorant"
> The Challenge — A leading luxury skincare brand had strong brand recognition in premium personal care, but limited visibility inside AI-generated responses where modern discovery increasingly happens. With competitors pushing for the same high-intent queries about deodorant, body wash, and body mist, the brand needed an advanced strategy that could win in both traditional and AI-driven search.
> Our Strategy — Optimized PDPs for LLM discoverability, including titles, meta descriptions, categories, and metafields on both front and back end. Executed a Reddit content and engagement strategy to influence AI model training signals around the brand's core product categories. Scaled Meta campaigns as a top-of-funnel awareness driver. Built a full-funnel traffic-to-remarketing strategy to retarget Meta-warmed audiences for conversion boosts.
> Our Services — GEO
> Our Results — #1 Visibility Score Rank in Profound for tracked prompts, +5 positions in 7 days. #1 Share of Voice across tracked product categories, +5 positions with share rising ~2%. #1 for "best smelling deodorant". #2 for "aluminum-free deodorant". Top 5 for "body mist," "body wash," and "best smelling body wash".
> Why It Worked — ... By the time it all came together, the client became the brand AI models reached for most when surfacing products to buy.
> Key Takeaways — Reddit is an AI visibility channel — Show up in the right conversations and the models follow. Optimize PDPs for AI — Structured, credible product content is what gets you cited. Channel collaboration always wins..."

Client identity: not named (only "a leading luxury skincare brand" / "A luxury skincare brand"). No revenue, headcount, or other buyer-size proxy disclosed anywhere on the case-study page. No price, fee, or contract value disclosed. GR0's own services menu (footer, same page) lists "GEO" alongside "SEO", "Google Ads", "Paid Social", "Link Building", "Content Creation", "Tik Tok Shop", "Amazon & Marketplace", "Programmatic Advertising" as a standing service line, not a one-off.

`https://gr0.com/pricing` fetched: page is JS-rendered (Framer); static-fetch text extraction returned no visible price figures or "GEO" service-tier text — no list price recovered this pull.

## Pull notes — mechanical only

- Body text extracted by stripping HTML tags with a regex and collapsing whitespace; the page is built on Framer and ships a large amount of font/CSS-in-`<style>` boilerplate before the real body text — the extraction skipped past this by searching for a second occurrence of a title phrase.
- No login wall or paywall. Both pages loaded without JavaScript execution (plain `curl`); the case-studies index page's visible text and structured page-data (a client-side data blob, not equivalent to a JSON API) both rendered enough text to read directly.
- `gr0.com/industries/beauty/` was checked and returned HTTP 404 — GR0 has no dedicated industry-vertical landing page for beauty, only the case-study roster.
- Buyer size: **unassigned** for this cell — the case study names no company, revenue, or headcount, so per `demand-signals.md`'s cell-attribution rule this observation cannot be mapped to SMB / mid-market / enterprise and is recorded against sub-market and vertical only.
- This is an agency's own claim about its own client work (vendor-reported, S6's stated bias: "marketing," "a list price is an asking price, never a purchase" — here there is not even a price, only a service-existence and outcome claim).
