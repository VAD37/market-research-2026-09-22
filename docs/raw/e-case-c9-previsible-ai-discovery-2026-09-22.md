# Previsible — "2026 State of AI Discovery Report Finds Google Remains the Center of AI Discovery, With ChatGPT Leading Standalone LLMs" (Businesswire press release, mirrored by Workflow magazine)

```yaml
source:          Previsible ("the AI discovery agency for GEO and modern search"), press release distributed via Business Wire; report authored by David Bell, Chief Product Officer and Co-Founder; CEO Jordan Koene also quoted
url_or_doc_id:   https://www.businesswire.com/news/home/20260706755932/en/Previsibles-2026-State-of-AI-Discovery-Report-Finds-Google-Remains-the-Center-of-AI-Discovery-With-ChatGPT-Leading-Standalone-LLMs (primary; returned 403 to both WebFetch and mcp fetch tools, see pull notes) — this file is captured from the verbatim mirror at https://workflowotg.com/previsibles-2026-state-of-ai-discovery-report/, which reproduces the Business Wire release text; a second mirror of the same release was also located at https://mms.businesswire.com/media/20260706755932/en/2845707/1/2026_State_of_AI_Discovery_Report_-_Previsible.pdf (report PDF, not fetched this pull) and https://previsible.com/wp-content/uploads/2026/07/2026-State-of-AI-Discovery-Report-by-Previsible.pdf (publisher's own PDF, not fetched this pull)
published:       2026-07-06
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            5
tier_reason:     vendor-authored aggregate study (Previsible sells GEO/AI-discovery agency services — the category it is measuring); method partially disclosed in the press release (site count, session count, date window, industries covered) but the full report PDF with the complete methodology was not fetched this pull — table default for "vendor or agency study with n, dates, method," not downgraded because the press release itself states n, dates and scope, but flagged bias per trust-rubric.md ("vendor measuring the thing it sells")
source_label:    vendor-reported
lane:            E, F
sub_market:      organic recommendation
vertical:        multiple — the release states the 166 measured websites span "SaaS, e-commerce, finance, legal, health, insurance, education, and publishing industries," naming SaaS explicitly as one of eight covered industries, but does NOT provide a SaaS-only breakout of any figure in the captured text — recorded as multi-vertical aggregate, SaaS named as one covered industry but not isolated
engine:          ChatGPT (92.4% of trackable standalone referral traffic), Perplexity (peaked March 2025, fallen since per the source cited by the secondary write-up, not itemized with a figure in this release itself), Gemini (grew 3.2x), Claude (grew 64x, passed Perplexity March 2026), Copilot (named as a challenger), Google AI Overviews / AI Mode (named as carrying more AI-influenced traffic than every LLM assistant combined, but excluded from the 92.4% trackable-referral figure itself — see caveats)
metric_kind:     traffic
evidence_grade:  not graded — this is an aggregate, cross-website dataset (166 sites, 6.77 million sessions), not a single-brand case. Bar item 1 ("the brand") does not map to one company; bar item 5 ("the intervention") does not map — no single company's action is described, only category-wide referral-traffic trends across the sample. Filed per this repo's precedent for aggregate market-data posts (Pass 4 cluster c2's treatment of Foundation Inc's "AI Citation Fingerprint" study) — cited as demand-signal / category evidence, not run through the Gold/Silver/Bronze/Fools-gold scale.
direction:       positive (ChatGPT and Claude referral growth, e-commerce AI-referral growth); also carries a negative sub-finding (Perplexity and Copilot referral declines)
paid_by_outcome: n/a — aggregate market data, not a client case
supersedes:      none
captured:        full mirrored press-release text (via workflowotg.com); the underlying report PDF was located but not fetched this pull — see pull notes and browser backlog
```

## Verbatim

Headline: "Previsible's 2026 State of AI Discovery Report Finds Google Remains the Center of AI Discovery, With ChatGPT Leading Standalone LLMs"

"SAN FRANCISCO, CA — July 6, 2026 /BUSINESS WIRE/ — Previsible, the AI discovery agency for GEO and modern search, today released the third edition of its AI Traffic Study, the industry's earliest and longest-running look at GEO trends, run and refreshed from November 2024 to May 2026. The latest edition analyzes 6.77 million AI-driven sessions across 166 websites spanning SaaS, e-commerce, finance, legal, health, insurance, education, and publishing industries."

"The study highlights where brands should focus for the second half of 2026 and found that AI discovery happening inside Google, through its AI Overviews and AI Mode, represents more AI-influenced traffic than every LLM assistant combined, and it should remain the priority surface marketers work to win."

"Among the destinations where people query AI LLMs directly, Previsible's study found ChatGPT leads by a wide margin, carrying 92.4% of trackable standalone referral traffic and still climbing. Several challengers are gaining ground, and industry variances have emerged that marketers should use to target content for specific LLM citation visibility. Gemini grew 3.2x with steady consistency and now stands as the second most visible model behind ChatGPT. Claude grew 64x over the tracked period and moved past Perplexity in March 2026, with particular strength among developers, technical buyers, and professional services. Across models, e-commerce content saw AI referral traffic rise 37x as shoppers increasingly arrive on product pages with intent already formed."

Quote: "The foundation brands built in search matters more than ever," said David Bell, Chief Product Officer and report author at Previsible. "Start by becoming a source Google's AI results want to cite by building the site architecture, and content signals AI systems rely on to cite you, then win ChatGPT as the leading standalone surface. The teams that lean in now will be the ones AI chooses to surface." Bell and the Previsible team recommend five core efforts to win in AI search: create citation-worthy evidence, build authority across trusted third-party sources, make websites accessible to AI systems to read and extract, optimize for answer journeys, and measure business impact rather than site-wide visibility alone.

Quote: "David's research brings focus to one of the most important, and often overlooked, parts of AI search: the value of engaged users who visit and interact with brand websites," said Previsible CEO Jordan Koene, recently named to BrightonSEO's Top 100 Most Influential SEOs. "As more brands evaluate the impact of AI-driven discovery, this perspective can help transform how teams measure success, build optimization strategies, and improve the web experiences and messaging they deliver to customers."

## Pull notes — mechanical only

- `https://www.businesswire.com/...` (the Business Wire original) returned a robots.txt-driven connection failure to `mcp__MCP_DOCKER__fetch` and an HTTP 403 to `WebFetch`. Per task instructions ("EDGAR full-text; 403 → record blocked"), recorded as blocked; the verbatim mirror at `workflowotg.com` (a business-press aggregator that republishes Business Wire releases in full) was used instead and is named as the effective source above.
- Two PDF report links were located during discovery (`mms.businesswire.com/media/.../2026_State_of_AI_Discovery_Report_-_Previsible.pdf` and `previsible.com/wp-content/uploads/2026/07/2026-State-of-AI-Discovery-Report-by-Previsible.pdf`) but neither was fetched this pull — the press release text captured above was judged sufficient for this cluster's screening purpose given the 8-12 case target was already in reach. Both PDF URLs are recorded in this cluster's census summary as candidates for a follow-up pull, not as a browser-backlog item (they are plain PDF fetches, not browser-only).
- `workflowotg.com`'s own page carries substantial unrelated boilerplate (site navigation, an unrelated news list) around the release text; only the release text itself is reproduced above.
- No SaaS-specific figure breakout found anywhere in the captured press-release text; the report PDF (not fetched) may carry an industry-by-industry breakdown per the release's framing ("industry variances have emerged that marketers should use to target content").
