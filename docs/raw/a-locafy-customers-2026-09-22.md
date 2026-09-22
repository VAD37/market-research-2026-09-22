# Locafy (Poseidon) — customers / case studies

```yaml
source:          Locafy Ltd (locafy.com)
url_or_doc_id:   https://locafy.com/reviews (real customer testimonials); https://locafy.com/ (homepage — illustrative "Apex Roofing Co." demo and "Results That Speak for Themselves" counters)
published:       undated (both pages)
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about category noise (testimonials, no quantified metric) and evidence about a number (customer-count headline claim)
tier:            6
tier_reason:     testimonials on /reviews name a real business and owner but no quantified visibility/traffic/sales metric, no date window, no engine, no measurement method — discard-on-sight per trust-rubric.md ("no n, no date window, or no method"); the homepage's interactive walkthrough (Apex Roofing Co., Austin TX) is an illustrative fictional demo, not a named real customer, and its "+280% increase in inbound calls" and "3.2x / +220%" dashboard figures are unattributed to any real, checkable business — discard-on-sight per trust-rubric.md ("percentage with no base")
source_label:    vendor-reported
lane:            A
sub_market:      organic recommendation
engine:          not tied to any specific testimonial or demo figure
metric_kind:     none
supersedes:      none
captured:        /reviews page, first ~3000 characters (8 of an unknown total number of testimonials); homepage "Proven Results" counter section and "Customer Journey" demo walkthrough, captured as part of the pull already used for `a-locafy-method-2026-09-22.md`
```

## Verbatim

### Real customer testimonials (locafy.com/reviews)

"Our customers. Their own words. Meet the people behind the businesses. Read their experiences and hear what working with Locafy means to them."

"'Great service and always delivering what's discussed on the phone. Mark is always prompt with my business add and always returns my calls. Very pleasant to deal with' — Paula Catalano, Owner, Paula A1 Cleaning"

"'I've been using Locafy to advertise my painting business for around 4-5 years, and I've been very happy with their service... Their advertising has helped me get new enquiries and jobs over the years, which has been valuable for my business.' — Roy, Owner, Sure Roy painting & decorating"

"'5 star service, I have been dealing with Marquis for many years now, always professional, and makes the renewal process seamless.' — Jamie Ciolac, Edies flyscreens"

"'The locafy team has helped me take my business to the next level. From seo, ads and marketing, to AI assistance and automations. As a small business, the tools they have helped me integrate are the equivalent of an entire office of administrators at a fraction of the cost.' — Jake Lusby, Owner/Operator, Air Sense Environmental"

"'We have been dealing with Locafy for over 5 years with Marquis... helped our business achieve not only page 1 Google results but also genuine enquiries...' — Sonja Jones, Owner, Pauls Gutter Cleaning"

"'I have had local running my google listing for about 6 years now, and the experience has been amazing...' — Michael Clubb, Clubby's Pest Control"

"'...I have been with Locafy in the last 5 years and thank you Marquis for looking after my business. Most effective and efficient approach strategy in regards of both maximising the exposure of my Google presence in both organic results and Google maps in a short period of time.' — Arash Behzaoi, Owner, Precision Mobile Tinting"

"'Thank you, Locafy & to Marquis, for all the advice, support and patience you provided throughout our recent website upgrade...' [name truncated before capture ended]"

**Grading**: none of the eight testimonials captured names a quantified visibility, traffic, or sales metric, a date window, an engine, or a sample size — all are qualitative relationship/satisfaction statements, several referencing "Google" and "page 1 results" generically, one referencing "AI assistance" generically (Jake Lusby's quote). **None clears even Bronze; all screened, not individually graded.** These are real, named small businesses (unlike Change Agents Corp's generic demo), useful only as logo/relationship evidence, not as proof claims.

### Homepage headline claim

"10,000+ businesses trust Locafy" — appears in the homepage's top banner, immediately under "Book Your Free Strategy Call." No date, no method, no breakdown by product (Proteus vs. Citations vs. Poseidon/AEO specifically) stated alongside this figure.

### Homepage illustrative demo (not a real customer)

The entire "How It Works" (Take Over / Optimize / Signal / Dominate) and "The Customer Journey" sections use one consistent fictional example throughout — "Apex Roofing Co., Austin, TX" — appearing identically across at least four separate page sections (business-ownership verification mock-up, Google Business Profile optimization mock-up, local map-pack comparison against "Summit Roof Repair" and "AllCity Roofing," and the six-step customer-journey narrative). This is Locafy's own product demo, not a named real customer.

Demo figures attached to this fictional example: "+280% — Increase in inbound calls" (customer-journey section); "12.4K Views +34%, 287 Calls +52%, 1.8K Directions +28%" (Google Business Profile optimization mock-up); "Monthly Views +34% vs last quarter."

"Proven Results — Results That Speak for Themselves — Real outcomes from real businesses using Locafy's AEO platform" header, followed by four counters that rendered as "0+" / "0" placeholders in this pull's static capture (likely JS-animated count-up widgets, values not captured): "0+ Businesses trust Locafy," "0+ Platforms optimized simultaneously," "0 AI engines targeted (ChatGPT, Gemini, Perplexity, Google AI Overviews)," "0/7 Monitoring and signal maintenance." A "Performance Dashboard — Last 8 months" panel beneath these counters shows: "Map Pack Visibility 3.2x +220%," "AI Search Mentions 47+890%," "Inbound Calls 287+16[digit(s) truncated]" — again with no named real business attached in the captured text, immediately adjacent to the "Real outcomes from real businesses" header, which implies these ARE meant to represent aggregate real-customer results rather than the fictional Apex Roofing demo, but no business name, date window, or independent measurement accompanies the figures as captured.

**Grading**: the "Performance Dashboard" figures under "Proven Results" carry a visibility-only claim (Map Pack visibility, AI Search mentions) plus a traffic/lead claim (inbound calls) with a relative window ("Last 8 months") but no named brand, no baseline value (only a multiplier/percent), no sample size, and no stated measurement method — **Fools gold** if read as a revenue-adjacent claim (inbound calls proxy for sales), or discard-on-sight per the "percentage with no base" rule if read strictly. Recorded here as category-noise evidence, not cited as a real-world number.

## Pull notes — mechanical only

- `/reviews` fetched via mcp__MCP_DOCKER__fetch, simplified/markdown rendering, capped at 3000 characters (8 testimonials captured before truncation; the page appeared to continue beyond this point based on the trailing incomplete quote).
- Homepage "Proven Results" section captured as part of the same pull used for `a-locafy-method-2026-09-22.md` (start_index 4000-8000).
- No dedicated `/case-studies` URL was found in the footer nav (Product: How It Works, Pricing, Free Tools, Book a Call; Company: About, Careers, Partners, Reviews, Blog, Contact) — "Reviews" is the closest equivalent and is the page captured above.
