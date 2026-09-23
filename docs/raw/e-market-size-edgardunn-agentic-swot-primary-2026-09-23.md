# Edgar, Dunn & Company — "SWOT Assessment of Agentic Commerce for Retailers" (January 2026): global agentic commerce $2.9 trillion by 2030

```yaml
source:          Edgar, Dunn & Company (EDC), report contributors Mark Beresford (Director), Davide Villa (Manager), Elisabetta Nadal (Consultant), Reuben Joseph (Business Analyst)
url_or_doc_id:   https://www.edgardunn.com/reports/swot-assessment-of-agentic-commerce-for-retailers (landing page); PDF at https://cdn.prod.website-files.com/6348568f7fba2909538d12b9/6981c30662c0de92b7d956f6_Agentic%20Commerce%20SWOT%20for%20retailers%20-%20FINAL%202026.pdf
published:       2026-01 ("January 2026" on the cover)
pull_date:       2026-09-23
pull_method:     fetch (curl, bot user agent) — landing page HTML and the PDF it links; text extracted with pdftotext
pull_purpose:    evidence about a number
tier:            5
tier_reason:     consultancy study with a stated method (top-down share cross-checked with bottom-up use-case model, generation × region split, World Bank and Statista inputs) but no published data appendix; a payments consultancy sizing a market it advises on — bias flagged
source_label:    analyst-derived
lane:            E
sub_market:      agentic commerce
engine:          n/a
metric_kind:     sales
supersedes:      e-market-size-stellagent-agentic-2026-09-22.md (Edgar Dunn rows only)
captured:        Executive Summary; contributors; "Headline agentic commerce market sizing estimates for retail" (p.11); "Sizing the Agentic Commerce Market for retail — Introduction, Methodology" (p.12); "Agentic Commerce as a Proportion of Total e-commerce, Global, 2026 & 2030" (p.14); regional 2030 shares (p.15). SWOT body (pp.16 ff.) not transcribed
verbatim:        partial
```

## Verbatim

Cover: "SWOT Assessment of Agentic Commerce for Retailers" — "January 2026". Every page footer: "CONFIDENTIAL".

Executive Summary (p.2), sizing sentence as printed:

> "Agentic commerce represents a substantial disruption within digital retail, with the global opportunity estimated at approximately USD 2.9 billion by 2030. Unlike the gradual shift from physical stores to e-commerce in the late 1990s and early 2000s, agent-led shopping is expected to cannibalise traditional e-commerce at a materially faster rate, as AI agents increasingly intermediate product discovery, comparison, and checkout."

[note: "USD 2.9 billion" is as printed on p.2; p.11 and p.14 print "$2.9billion" and "$2,916,789 mn" for the same 2030 figure — recorded as printed, not reconciled here]

p.11 — "Headline agentic commerce market sizing estimates for retail":

> "$2.9billion — Total value of retail sales conducted via AI agents by 2030"
> "29% — Proportion of global retail e-commerce will be completed via AI agents by 2030"
> "Retailers in North America and Asia Pacific will be early adopters"

[image: docs/raw/img/e-market-size-edgardunn-agentic-swot-primary-2026-09-23/01-edc-agentic-commerce-swot-retailers-2026.pdf — pages 11, 14, 15 carry the sizing charts; PDF saved whole, no page renderer available]

p.12 — "Sizing the Agentic Commerce Market for retail":

> "Agentic commerce is widely acknowledged as a subset of e-commerce, representing autonomous AI-driven transactions (discovery, negotiation, purchase) within the broader online retail ecosystem rather than a standalone category. This positioning clarifies market sizing by framing it as a channel shift, projected to capture 15-25% of e-commerce volume by 2030, thus avoiding any inflated total addressable market (TAM) estimates."

> "Methodology — Within this report EDC has cross-checked top-down estimates (share of online retail flowing through agents) with bottom-up use-case modelling (e.g., general retail, grocery, electronics, specialty, etc.) to test whether the numbers are plausible and to avoid over-inflation."

> "The consumer population has been split into the following 5 generations: Gen Alpha, Gen Z, Millenial, Gen X, and Baby Boomer. Each generation has differing AI usage, based on age and openness to AI. Data has been extracted from World Bank to forecast the proportion of each generation for the 5 major regions (North America, Europe, Asia-Pacific, Latin America and Caribbean, and Middle East and Africa)."

> "Globally, 2025 was the first year of agentic commerce, however it was an emerging technology, and so the proportion of e-commerce transaction volume was estimated at less than 5% for all generations. By 2030, these proportions are expected to increase massively, driven by the high adoption from Gen Alpha and Gen Z."

p.14 — "Agentic Commerce as a Proportion of Total e-commerce, Global, 2026 & 2030" (chart labels as extracted):

| | 2026 | 2030 |
|---|---|---|
| Agentic commerce | $44,321 mn (0.6% of e-commerce) | $2,916,789 mn (29% of e-commerce) |
| e-commerce | $7.3 trillion | $10.1 trillion (8% CAGR) |

> "Note 1: 185% CAGR due to very low agentic commerce market share in 2026. CAGRs taken from the following years (2027, 2028, 2029), plateau at 13%, reflecting the large growth expected in the first full year of agentic commerce"
> "Sources: EDC Analysis, World Bank"

p.15 — "Agentic Commerce as a Proportion of Total e-commerce, by Region, 2030": North America 27%, EU 26%, APAC 31%, MEA 30%, LAC 30% (labels as extracted; region-to-value pairing read from layout order). > "global market share is at least 26% in all regions by 2030". "Sources: EDC Analysis, Statista, World Bank".

Not found in the PDF: any "$1.7 trillion" or "narrow / broad" pair. grep of the extracted text for "1.7", "1,7", "narrow", "broad" returns no sizing line; the only global 2030 figure is the $2.9 trillion (printed "2.9 billion" / "$2,916,789 mn").

## Pull notes — mechanical only

- Landing page fetched by curl (HTTP 200). The report is offered behind a "Fill in the form to get instant access" download form; the form was not submitted. The PDF URL is present in the landing page's static HTML (a public Webflow CDN link) and was fetched directly by curl (HTTP 200, 1,299,545 bytes, application/pdf).
- pdftotext -layout; 2,033 lines. Page numbers are the PDF's own footer numbers.
- No PDF page renderer on this machine (pdftoppm absent); the whole PDF is saved under `docs/raw/img/` in place of page images; INDEX row added.
- Comparison with substitute (Stellagent tier-6 comparison table): substitute lists Edgar Dunn "Global 2030 $1.7T (narrow) / $2.9T (broad), Total retail transaction flows". The primary carries $2.9T (as "$2,916,789 mn", 29% of global e-commerce, 2030); the $1.7T figure is not in this report. The substitute's "eMarketer $144B 2029" row is not checked here.
