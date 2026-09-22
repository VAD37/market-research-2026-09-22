# Rankscale — Austrian Optical Retail Chain case study

```yaml
source:          Rankscale — case study "Austrian Optical Retail Chain Claims Dominant AI Search Visibility in 5 Months"
url_or_doc_id:   https://rankscale.ai/case-studies/optical-retail-chain-ai-visibility
published:       undated — no date on page
pull_date:       2026-09-22
pull_method:     browser extension (claude-in-chrome, own dedicated tab)
pull_purpose:    evidence about a number
tier:            5
tier_reason:     discloses explicit numeric baseline, named engines with a per-engine/per-prompt-type breakdown table, and a sample-size figure (185 mentions, 372 citations) — adjusted up from table default 6, capped at 5: no absolute date window, no independent third-party measurer, and both Rankscale (the vendor) and ithelps Digital (a paying partner agency in Rankscale's referral program per `docs/raw/a-rankscale-careers-facts-2026-09-22.md`) had a commercial stake in the outcome, per trust-rubric.md "vendor measuring the thing it sells"
source_label:    vendor-reported
lane:            E
sub_market:      organic recommendation
engine:          ChatGPT, Perplexity, Copilot, Google AI Mode — all four named explicitly, with a per-engine, per-prompt-type percentage breakdown table
metric_kind:     visibility — AI Visibility (%), Recognition Rate (%), Top-3 Rate (%), mentions/citations counts. No traffic or sales figure on this page
supersedes:      none
captured:        full page — single call, reached the closing testimonial and CTA, no truncation (this pull captures the closing testimonial that Pass 3's own pull of this same URL recorded as cut off mid-quote at a 4000-character limit)
vertical:        Optical retail / Multi-location retail — the page's own category tags ("CASE STUDY / OPTICAL RETAIL / MULTI-LOCATION RETAIL")
evidence_grade:  Bronze (full-page, on this pull). All seven bar items evaluated below.
pass3_grade:     Bronze (from `docs/raw/a-vendor-census-c2-2026-09-22.md`, sourced from this same URL, captured to ~4000 characters and truncated mid-testimonial — `docs/raw/a-rankscale-customers-2026-09-22.md`)
paid_by_outcome: unknown — no fee structure (flat, retainer, or performance-based) disclosed for ithelps Digital's engagement with the client, or for Rankscale's relationship with ithelps Digital
prompt_set_disclosed: partial — individual prompt wordings are given as examples ("optiker bregenz", "Welcher Optiker ist der beste in Graz?"), and the prompt categories (brand-, category-, location-specific) are named, but no total n of tracked prompts is stated
```

## Verbatim

Category tags: "CASE STUDY / OPTICAL RETAIL / MULTI-LOCATION RETAIL"

Title: "Austrian Optical Retail Chain Claims Dominant AI Search Visibility in 5 Months"

"How ithelps Digital used Rankscale to grow a national eyewear retailer's AI visibility from 14.7% to 75.3% across ChatGPT, Perplexity, Copilot, and Google AI Mode. Partner agency: ithelps Digital · Vienna, Austria."

"Partner agency: ithelps Digital · Author: Florian Prohaska"

Headline stat tiles: "412% — AI Visibility growth in 5 months" / "85% — Recognition Rate across tracked prompts" / "38% — Top-3 Rate"

**THE CLIENT:** "A multi-location optical retail chain operating across Austria, competing in a category where 'best optician near me' and 'best glasses for [need]' style questions increasingly get answered directly by AI assistants before a shopper ever visits a store."

**THE ASK:** "Could a regional retailer build AI search authority fast enough to matter — not just nationally, but store-by-store, in dozens of local markets — in a category dominated by long-established national chains? The client asked ithelps Digital to establish and grow AI visibility across ChatGPT, Perplexity, Copilot, and Google AI Mode, and to track it against category-leading competitors in real time."

**STEPS TAKEN IN RANKSCALE:**

"01 Audit & Benchmark — Brand-, category-, and location-specific prompts were configured in Rankscale's Search Terms module (e.g. 'optiker [city]' patterns across dozens of Austrian towns, plus 'who is the best optician in [city]?' comparison prompts), establishing a baseline AI Visibility of 14.7%."

"02 Competitive Research — Rankscale's Competitor Analysis module benchmarked the client weekly against the market's established optical chains across all four major AI engines, surfacing the highest-opportunity local markets and topics."

"03 Execution & Reporting — ithelps Digital produced AI-optimized, location-specific content to close the identified gaps, using Rankscale's monthly dashboard exports as the basis for client reporting and strategy calls."

**RESULTS:**
- "AI Visibility grew from a 14.7% baseline to 75.3% in 5 months, with a Recognition Rate of 85% across all tracked prompts."
- "The client reached a 38% Top-3 Rate, appearing among the top 3 cited sources for over a third of all tracked prompts."
- "Total tracked engagement reached 185 mentions and 372 citations across ChatGPT, Perplexity, Copilot, and Google AI Mode."

**Search Terms Module — Local Market Dominance table (verbatim):**

| Prompt type | Copilot | Google AI Mode | ChatGPT | Perplexity |
|---|---|---|---|---|
| "optiker [smaller town]" (4 example markets) | 71–83% | 77–100% | 77–83% | 83–91% |
| "Welcher Optiker ist der beste in [major city]?" (2 example cities) | – | 67–83% | 63–67% | 91–100% |

"Across dozens of Austrian towns and cities, location-specific optician prompts now average 82% Found Rate across all four tracked AI engines. Example: 'optiker dornbirn' reaches 100% Found Rate on Google AI Mode; 'Welcher Optiker ist der beste in Graz?' reaches 100% on Perplexity."

"Rankscale Search Terms module — location-specific optician prompts tracked across ChatGPT, Perplexity, Copilot, and Google AI Mode in Austria: Local — 'optiker bregenz'; Local — 'optiker bruck an der mur'; Local — 'optiker dornbirn' (100% Found Rate on Google AI Mode); Local — 'optiker landeck'; Comparison — 'Welcher Optiker ist der beste in Graz?' (100% Found Rate on Perplexity); Comparison — 'Welcher Optiker ist der beste in Salzburg?'"

**Testimonial (captured in full — Pass 3's pull of this URL was truncated mid-quote):** "We run GEO campaigns for clients across half a dozen industries — from opticians to medical specialists to B2B software — and Rankscale is the only tool that scales with that. One dashboard, consistent methodology across every client, and reporting our team can hand straight to a client without extra work. It's become core infrastructure for how we deliver GEO as an agency, not just a nice-to-have add-on." — Florian Prohaska, Co-Founder, ithelps Digital.

Closing CTA: "Ready to make AI search your next growth channel? Start tracking your AI visibility with Rankscale today."

## Pull notes — mechanical only

- Fetched via `claude-in-chrome` browser extension (connected this session), `get_page_text` on a dedicated new tab (tabId 1697684063) opened for this task. Full page captured in one call, reached the closing CTA, no truncation.
- Pass 3's own pull of this same URL (`docs/raw/a-rankscale-customers-2026-09-22.md`) used plain fetch capped at ~4000 characters and was cut off mid-testimonial; this pull captures the full testimonial from Florian Prohaska, Co-Founder of ithelps Digital, in full for the first time.
- "412% AI Visibility growth" (headline stat tile) and "14.7% → 75.3%" (results prose) are the same underlying change expressed two ways — 14.7% to 75.3% is a ~412% relative increase — not a discrepancy, both figures reconciled on this page.
- No absolute calendar date anywhere on the page — only the relative "in 5 months."
- No statement of whether ithelps Digital was paid by the client on a performance basis, or of Rankscale's own commercial relationship with ithelps Digital beyond the general "Agency Program" structure described in a separate Rankscale page (`docs/raw/a-rankscale-careers-facts-2026-09-22.md`, not re-verified on this page).

## Evidence bar — seven items, evaluated against this full page

| # | Item | Present / Absent | Quote |
|---|---|---|---|
| 1 | Brand, or credibly specified anonymised profile | **Present (anonymised)** | "A multi-location optical retail chain operating across Austria" — not named, but geographically and categorically specific, with a named partner agency and author |
| 2 | The engine or engines | **Present** | "across ChatGPT, Perplexity, Copilot, and Google AI Mode" — with a full per-engine breakdown table |
| 3 | The date window, absolute | **Absent** | "in 5 months" — relative duration only, no start/end calendar date |
| 4 | The baseline before intervention | **Present** | "AI Visibility grew from a 14.7% baseline to 75.3% in 5 months" |
| 5 | The intervention itself | **Present** | Three-step "Steps Taken in Rankscale": Audit & Benchmark, Competitive Research, Execution & Reporting (location-specific content) |
| 6 | The sample size, or the traffic volume | **Present** | "Total tracked engagement reached 185 mentions and 372 citations" |
| 7 | Who measured, and whether they were paid by the outcome | **Partial** | Measurer: Rankscale's own Search Terms and Competitor Analysis modules, plus partner agency ithelps Digital. No statement anywhere of whether ithelps Digital (or Rankscale) was paid by the outcome |

**Full-page grade: Bronze.** Present: an anonymised but credibly specified client, four named engines with a detailed breakdown table, an explicit numeric baseline, a described three-step intervention, and disclosed sample volume (185 mentions, 372 citations) — the strongest-evidenced Bronze case in Rankscale's own Pass 3 cluster and, per that cluster's own summary, "the strongest-evidenced Bronze of the six vendors and 40 total case studies reviewed" in Pass 3's P3-c2. Still Bronze, not Silver: no absolute date window is disclosed anywhere, and no unaffected control metric (a competitor tracked at a constant level, or an untreated location) is given — the case reports only this client's own before/after, with competitors mentioned only as the benchmark target, not as a control series with its own numbers.

**Grade change vs. Pass 3: same (Bronze → Bronze).** Pass 3 graded this case Bronze from the same URL, already noting explicitly it was "the strongest-evidenced Bronze... clears 5 of 7 bar items, missing only an absolute date window and independent/paid-by-outcome measurement" (`docs/raw/a-rankscale-customers-2026-09-22.md`). This full-page pull, no longer truncated, confirms that assessment and completes the previously-cut-off testimonial quote — no new bar item is disclosed beyond what Pass 3's truncated pull already found.
