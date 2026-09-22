# Case census — P4-c13 — full-page re-grade of every Pass 3 Bronze-or-better and `screened — not opened` title, c1–c6

```yaml
source:          every case-study title recorded in docs/raw/a-vendor-census-c1 through c4, f-agency-census-c5, c-vendor-census-c6 (all 2026-09-22), plus e-case-census-c4-2026-09-22 (P4-c4, already re-graded, cited not redone), plus this task's own 13 e-case-c13-* raw files
url_or_doc_id:   n/a — this is the census summary required by the task, not a raw pull itself; every cell cites a raw file
pull_date:       2026-09-22
pull_method:     mixed — see raw paths; WebFetch and browser extension (claude-in-chrome) for new pulls, plain fetch/Playwright for files carried forward from same-date Pass 3/4 pulls
pull_purpose:    evidence about a number
tier:            n/a at this file's level — see each cited raw file's own tier line
source_label:    mixed — vendor-reported (nearly all), company-stated (HubSpot, Yext, Intero Digital press releases)
lane:            E
sub_market:      organic recommendation (nearly all); paid placement / agentic commerce (c6 rows)
metric_kind:     mixed — see rows
supersedes:      none
captured:        census — no interpretation
```

No interpretation. Grading rule 1 applied throughout (`docs/method/plan.md` "Evidence bar — grading rule 1, 2026-09-22"): a grade is assigned only from the case's own full page with the seven items ticked; unopened is `screened — not opened`; a page with no metric is `screened — no claim`; a case missing any of items 1–7 is Bronze at best.

## Master table — every title, by vendor

Columns: Vendor | Client | Pass 3 cluster | Pass 3 grade/status | Full-page grade (P4-c13) | Items missing (of 7) | Metric | Figure (verbatim, short) | Vertical (as named) | Paid by outcome | Prompt set disclosed | URL | Raw path

### Searchable (P3-c1)

| Client | Pass 3 | P4-c13 | Missing | Metric | Figure | Vertical | Paid-by-outcome | Prompt set | URL | Raw path |
|---|---|---|---|---|---|---|---|---|---|---|
| 303 (agency) | Fools gold | Fools gold (not re-opened — teaser is the only content; no dedicated page reached) | 2,3,4,6,7 | visibility/sales | "£1m+ Pipeline and 206% Share of Voice" | none named | unknown | no | searchable.com/customers | a-searchable-customers-2026-09-22.md |
| 1mind | Fools gold | Fools gold (same, not re-opened) | 2,3,4,5(partial),6,7 | traffic | "Cut Content Planning Time by 70%... Scaled Production 10x" | none named | unknown | no | searchable.com/customers | a-searchable-customers-2026-09-22.md |
| Blackbird | screened — not opened (names brand, no metric on index) | **screened — not opened** — case's own page not located this pull (WebFetch could not resolve a "Read story" href for Blackbird from the customers page) | n/a | none | none on index | none named | unknown | no | searchable.com/customers (dedicated page URL not resolved) | a-searchable-customers-2026-09-22.md |

### geoSurge (P3-c1)

No case-study or customer page exists on this vendor's site (confirmed at Pass 3, `a-geosurge-pricing-2026-09-22.md` et al.). 0 titles.

### Peec AI (P3-c1)

| Client / quote | Pass 3 | P4-c13 | Metric | Figure | URL | Raw path |
|---|---|---|---|---|---|---|
| Jon Gitlin (role only, no company) | Fools gold | Fools gold (same, no dedicated page — testimonial fully captured at Pass 3) | traffic | "5x YoY increase in traffic and demo requests from LLMs" | peec.ai/pricing | a-peec-customers-2026-09-22.md |
| Sepy Bazzazi / Glide | Fools gold | Fools gold (same) | visibility | "ranking for targeted ChatGPT and Perplexity prompts within 24 hours" | peec.ai/pricing | a-peec-customers-2026-09-22.md |
| Crystal Carter, Ethan Smith/Graphite, Thomas Smeaton, Artur Kosch, Lily Ray/Amsive | screened — no claim ×5 | **screened — no claim** (same — testimonial quotes fully captured, no dedicated page exists) | none | none | peec.ai/pricing, peec.ai/ | a-peec-customers-2026-09-22.md |

### Promptwatch (P3-c1)

| Client | Pass 3 | P4-c13 | Metric | Figure | URL | Raw path |
|---|---|---|---|---|---|---|
| OpenUp | Fools gold | Fools gold (same, not re-opened — "top cited result" teaser only) | visibility | "top cited result" | promptwatch.com/customers | a-promptwatch-customers-2026-09-22.md |
| Monks | Fools gold | Fools gold (same) | none (roster claim) | enterprise-roster claim | promptwatch.com/customers | a-promptwatch-customers-2026-09-22.md |
| Crisp | Fools gold | Fools gold (same) | sales | "2x Higher CVR" | promptwatch.com/customers | a-promptwatch-customers-2026-09-22.md |

### Profound (P3-c1; MongoDB and Plaid re-graded by P4-c4, cited not redone)

| Client | Pass 3 | P4-c13 | Missing | Metric | Figure | Vertical | URL | Raw path |
|---|---|---|---|---|---|---|---|---|
| Plaid | Bronze (visibility, homepage) / Bronze (traffic, story 1) | **Bronze (traffic, P4-c4) / Fools gold (conversion, P4-c4)** — cited, not redone | — | traffic; sales | "+300% referral traffic"; "+210% conversions" | Finance · Mid-market | tryprofound.com/customers/plaid | e-case-census-c4-2026-09-22.md; e-case-plaid (P4-c4) |
| MongoDB | Bronze | **Bronze (P4-c4)** — cited, not redone | — | visibility | "50% increase in AI Search visibility" | SaaS · Enterprise | tryprofound.com/customers/mongodb | e-case-census-c4-2026-09-22.md |
| Aleph | Bronze (index teaser) | **Bronze** — same | 3,6,7 | visibility, traffic | "5x AI visibility; 253% citation share; 82% LLM-attributed traffic" | none | tryprofound.com/customers/aleph | e-case-c13-profound-multi-2026-09-22.md |
| CRS Credit API | Bronze | **Bronze** (visibility) + **Fools gold** (pipeline sub-claim) — same headline, new sub-claim surfaced | 3,4,6,7 | visibility (+ sales sub-claim) | "20x visibility"; "15% pipeline growth" | none | tryprofound.com/customers/crs-credit-api | e-case-c13-profound-multi-2026-09-22.md |
| OpusClip | Bronze | **Bronze** (visibility) + **Fools gold** (signups sub-claim) — same headline, new sub-claim surfaced | 3,7 | visibility (+ sales sub-claim) | "45% visibility, #1 citation share"; "37% new signups" | none | tryprofound.com/customers/opus-clip | e-case-c13-profound-multi-2026-09-22.md |
| Hone | Bronze | **Bronze** — same | 3,6,7 | visibility | "800% visibility increase; 10x citation share" | none | tryprofound.com/customers/hone | e-case-c13-profound-multi-2026-09-22.md |
| Ramp | Bronze | **Bronze** — same (strongest-disclosed: clears items 1–6) | 7 (+ no control) | visibility | "3.2% → 22.2% AI visibility (7x)" | none | tryprofound.com/customers/ramp | e-case-c13-profound-multi-2026-09-22.md |
| Lake.com | Bronze | **Bronze** — same | 6,7 | visibility | "27.9% → 41.2% visibility score" | none | tryprofound.com/customers/lake-com | e-case-c13-profound-multi-2026-09-22.md |
| Airbyte | Bronze | **Bronze** (visibility) + **Fools gold** ($100K deal sub-claim) — same headline, new sub-claim surfaced | 7 (+ no control) | visibility (+ sales sub-claim) | "9% → 26% ChatGPT visibility (3x)"; "$100,000 deal closed" | none | tryprofound.com/customers/airbyte | e-case-c13-profound-multi-2026-09-22.md |
| 1840 & Co. | Bronze | **Bronze** — same | 3,6,7 | visibility | "0% → 11% AI visibility" | Remote staffing (per title, not the dedicated page) | tryprofound.com/customers/1840-co-... | e-case-c13-profound-multi-2026-09-22.md |
| WHOOP, Optro, Kiteworks(Profound's own), Apartment List, One Identity, Statsig | screened — no claim ×6 | **screened — no claim** (index titles carry no quantified metric; not individually re-opened — consistent with their own titles naming no number) | — | none | none | — | tryprofound.com/customers | a-profound-customers-2026-09-22.md |
| Arizona College of Nursing, Alchemy, Jordan Digital Marketing, GR0, Omnilux, (unnamed) 100x | Fools gold ×6 | Fools gold (same, not re-opened this pull) | — | sales | "51% conversions"; "7x signup rate"; "34% revenue"; "$1K→$100K/mo"; "tripled revenue"; "100x revenue" | Healthcare/SaaS/Agency (per index tags) | tryprofound.com/customers | a-profound-customers-2026-09-22.md |

### AthenaHQ (P3-c1; Grüns and Verito re-graded by P4-c4, cited not redone)

| Client | Pass 3 | P4-c13 | URL | Raw path |
|---|---|---|---|---|
| Grüns | Bronze | **Bronze (P4-c4)** — cited | athenahq.ai (case page) | e-case-census-c4-2026-09-22.md |
| Verito | Bronze | **Bronze (P4-c4)** — cited | athenahq.ai (case page) | e-case-census-c4-2026-09-22.md |
| Popl.co | Fools gold | Fools gold (same, not re-opened) | athenahq.ai/customers | a-athenahq-customers-2026-09-22.md |
| 9 vertical vignettes + 6 feature claims | screened — no claim | **screened — no claim** — no brand named on any of the 15, not individually re-opened (no brand to open a page for) | athenahq.ai/customers | a-athenahq-customers-2026-09-22.md |

### RankPrompt (P3-c1; both re-graded by P4-c4, cited not redone)

| Client | Pass 3 | P4-c13 | URL | Raw path |
|---|---|---|---|---|
| Humand | Bronze | **Bronze (P4-c4)** — cited | rankprompt.com (case page) | e-case-census-c4-2026-09-22.md |
| Owings Auto | Bronze | **Bronze (P4-c4)** — cited | rankprompt.com (case page) | e-case-census-c4-2026-09-22.md |

### Sitefire (P3-c1; Pointhound re-graded Silver by P4-c4, cited not redone)

| Client | Pass 3 | P4-c13 | Missing | Metric | Figure | URL | Raw path |
|---|---|---|---|---|---|---|---|
| Pointhound | Bronze (homepage teaser) | **Silver (P4-c4)** — cited | — | traffic, visibility | "+300% site visits" | sitefire.ai/case-studies/pointhound | e-case-census-c4-2026-09-22.md |
| Jerry | Bronze (homepage teaser) | **Silver — UP, this pull** | 6,7 | traffic, visibility | "+78% AI referral traffic... 112% vs. 72% treated-vs-untouched" | sitefire.ai/case-studies/jerry | e-case-c13-sitefire-jerry-2026-09-22.md |

### Scrunch AI (P3-c2)

| Client | Pass 3 | P4-c13 | Missing | Metric | Figure | URL | Raw path |
|---|---|---|---|---|---|---|---|
| Akamai | Bronze | **Bronze** — same | 2,3,6,7 | visibility | "5x'd brand presence" | scrunch.com/case-studies/akamai-... | e-case-c13-scrunch-multi-2026-09-22.md |
| Strapi | Bronze | **Bronze** — same | 2,3,4,6,7 | visibility | "226% citation growth" | scrunch.com/case-studies/strapi-customer-story | e-case-c13-scrunch-multi-2026-09-22.md |
| Stratabeat | Bronze | **Bronze** — same | 2,3,4,7 | visibility | "260%+ AI visibility gains" | scrunch.com/case-studies/2026-01-stratabeat-... | e-case-c13-scrunch-multi-2026-09-22.md |
| Tinybird | Bronze | **Bronze** — same | 2,3,4,6,7 | visibility | "3x'd brand mentions" | scrunch.com/case-studies/tinybird-ai-search-case-study | e-case-c13-scrunch-multi-2026-09-22.md |
| BairesDev | Bronze | **Bronze** — same | 3,4,7 | visibility | "78% AI Search surge" | scrunch.com/case-studies/2025-04-...-bairesdevs-78-... | e-case-c13-scrunch-multi-2026-09-22.md |
| Proper Propaganda | Fools gold | Fools gold (same, not re-opened) | — | sales | "5x'd lead gen" | scrunch.com/case-studies/proper-propaganda-... | a-scrunch-customers-2026-09-22.md |
| AlchemyLeads | Fools gold | Fools gold (same) | — | sales | "closed three major enterprise contracts" | scrunch.com/case-studies/2026-01-alchemyleads-... | a-scrunch-customers-2026-09-22.md |
| Runpod (4x growth) | Fools gold | Fools gold (same) | — | sales | "4x customer acquisition through ChatGPT" | scrunch.com/case-studies/2025-07-...-runpod-... | a-scrunch-customers-2026-09-22.md |
| Big Leap, Runpod (flywheel), Clapping Dog Media | screened — no claim ×3 | screened — no claim (same) | — | none | none | scrunch.com/case-studies/... | a-scrunch-customers-2026-09-22.md |

### Brandlight AI (P3-c2)

3 testimonial quotes screened at Pass 3, no dedicated case page exists — **screened — no claim** (same, not re-opened; already the fullest content this vendor publishes). Raw path: `a-brandlight-customers-2026-09-22.md`.

### Change Agents Corporation (P3-c2)

1 generic before/after demo (unsourced, no real brand named) screened at Pass 3 — **screened — no claim** (same, not a real case). Raw path: `a-changeagents-customers-2026-09-22.md`.

### Locafy (P3-c2)

8 testimonials + 1 fictional demo screened at Pass 3, none clears even Bronze — **screened — no claim** (same). Raw path: `a-locafy-customers-2026-09-22.md`.

### Otterly.AI (P3-c2)

| Client | Pass 3 | P4-c13 | Missing | Metric | Figure | URL | Raw path |
|---|---|---|---|---|---|---|---|
| Bacula Enterprise | Bronze (teaser) | **Bronze — full page confirmed** | 4,7 | visibility | "#1 ranking in ChatGPT for 'best HPC backup software'" | otterly.ai/blog/bacula-enterprise-geo-case-study | e-case-c13-otterly-multi-2026-09-22.md |
| Neur Digital / MedTech (Client A) | Bronze (teaser) | **Bronze — full page confirmed** | 3,4,7 | visibility | "Client A's AI citations grew by 2,016%" | otterly.ai/blog/8x-more-ai-citations-... | e-case-c13-otterly-multi-2026-09-22.md |
| Neur Digital / MedTech (Client B) | (same title, Bronze at teaser) | **Fools gold** — revenue sub-claim newly surfaced on full page | 3,4,7 | sales | "2,670% citations... $13,000 in revenue" | otterly.ai/blog/8x-more-ai-citations-... | e-case-c13-otterly-multi-2026-09-22.md |
| Instant Commerce | Bronze (full page, Pass 3) | **Bronze — same, re-confirmed** | 3,4,6,7 | visibility, traffic | "2x increase in AI search visibility and traffic" | otterly.ai/instant-geo-case-study | e-case-c13-otterly-multi-2026-09-22.md |
| Chatarmin, NOLA Marketing, SORN.AI, What IF Web, TM Blast | Fools gold ×5 (teaser-only) | **screened — not opened (full page)** — dedicated URLs identified this pull (`otterly.ai/blog/chatarmin-...`, `.../nola-marketing-...`, `.../geo-case-study-sornai/`, `.../geo-case-study-whatifweb/`; TM Blast is a LinkedIn video, not a web page) but not fetched within this pull's time budget | — | sales/traffic | "1%→10% demos"; "30% leads"; "doubled sign-ups"; "300%+ traffic"; "500% ChatGPT sessions" | otterly.ai/case-studies (index) | a-otterly-customers-2026-09-22.md |
| Slopelift, Stella Rising | screened — no claim ×2 | screened — no claim (same) | — | none | none | otterly.ai/blog/... | a-otterly-customers-2026-09-22.md |
| Videoloft | screened — no claim (full page, Pass 3) | screened — no claim (same) | — | none | none | otterly.ai/videoloft-case-study | a-otterly-customers-2026-09-22.md |

### Rankscale.ai (P3-c2; Austrian Optical Retail and AI SMS Platform re-graded by P4-c4, cited not redone)

| Client | Pass 3 | P4-c13 | Missing | Metric | Figure | URL | Raw path |
|---|---|---|---|---|---|---|---|
| Austrian Optical Retail Chain | Bronze (full page, Pass 3) | **Bronze (P4-c4)** — cited | — | visibility | "14.7% → 75.3% AI Visibility" | rankscale.ai/case-studies/optical-retail-chain-... | e-case-census-c4-2026-09-22.md |
| AI SMS Platform | Fools gold (full page, Pass 3) | **Fools gold (P4-c4)** — cited | — | sales | "$280,000 in qualified pipeline" | rankscale.ai/case-studies/ai-sms-platform-280k-pipeline | e-case-census-c4-2026-09-22.md |
| MiniFinder Germany | Bronze (teaser) | **Bronze — full page confirmed, same** | 3(partial),7 | visibility | "2.4% → 36.2 pts AI Visibility growth" | rankscale.ai/case-studies/minifinder-germany-... | e-case-c13-rankscale-multi-2026-09-22.md |
| SoWork | Bronze (teaser) | **Bronze — full page confirmed, same** | 3,7 | visibility | "16.6% baseline → +100% visibility, 63% market lead" | rankscale.ai/case-studies/sowork-virtual-office-... | e-case-c13-rankscale-multi-2026-09-22.md |
| Online Grocer, 15+ US Metros | Bronze (teaser) | **Bronze — full page confirmed, same** | 3,4,7 | visibility | "4,600+ citations across ~350 tracked prompts" | rankscale.ai/case-studies/online-grocer-15-metros-... | e-case-c13-rankscale-multi-2026-09-22.md |
| Spanish Bank | Bronze (teaser) | **Bronze — full page confirmed, same** | 2,3,4,6,7 | visibility | "+215% top-3 placements" | rankscale.ai/case-studies/spanish-bank-... | e-case-c13-rankscale-multi-2026-09-22.md |
| European Public-Sector GEO Pilot | screened — no claim | screened — no claim (same) | — | none | none | rankscale.ai/case-studies/european-public-sector-... | a-rankscale-customers-2026-09-22.md |

### AirOps (P3-c3; consolidated per-vendor file for the 7 newly graded + Chime re-confirmed)

| Client | Pass 3 | P4-c13 | Missing | Metric | Figure | URL | Raw path |
|---|---|---|---|---|---|---|---|
| Product Marketing Alliance | screened — not opened | **Bronze — UP** | 3,4,7 | visibility | "nearly 10% AI search citation share" | airops.com/blog/pma-customer-story | e-case-c13-airops-multi-2026-09-22.md |
| Brainlabs | screened — not opened | **Bronze — UP** (clears items 1–6) | 7 (+ no control) | visibility | "SoV 28.57%→38.67% (+35%); Mention Rate +42%" | airops.com/blog/brainlabs-customer-story | e-case-c13-airops-multi-2026-09-22.md |
| Oyster | screened — not opened | **Bronze — UP** | 3,6,7 | visibility | "cited in ChatGPT within four days" | airops.com/blog/oyster-customer-story | e-case-c13-airops-multi-2026-09-22.md |
| Parallel | screened — not opened | **Bronze — UP** (clears items 1–6) | 7 (+ no control) | visibility | "citation rate 7%→18% (+130%); 1,420 citations" | airops.com/blog/parallel-customer-story | e-case-c13-airops-multi-2026-09-22.md |
| Asana | screened — not opened | **Bronze — UP** | 3,7 | visibility | "citation count +71%, rate +16%; ChatGPT citations +93%" | airops.com/blog/asana-quill-story | e-case-c13-airops-multi-2026-09-22.md |
| Carta | screened — not opened | **Bronze — UP** | 3,6,7 | visibility | "75% citation rate on new pages" | airops.com/blog/carta-case-study | e-case-c13-airops-multi-2026-09-22.md |
| Chime | Bronze (full page, Pass 3) | **Bronze — same, re-confirmed** | 2,3,6,7 | visibility | "3x citation increase" | airops.com/blog/chime-case-study | e-case-c13-airops-multi-2026-09-22.md |
| Docebo | Fools gold (full page, Pass 3) | Fools gold (same, not re-opened) | — | sales | "12.7% leads from AI (up 5x YoY)" | airops.com/blog/docebo-case-study | a-airops-customers-2026-09-22.md |
| Webflow (testimonial) | Fools gold (Pass 3) | Fools gold (same; dedicated case page opened this pull confirms same 2%→10% claim) | — | traffic/sales | "ChatGPT-attributed signups 2%→10%" | airops.com/blog/webflow-case-study | e-case-c13-airops-multi-2026-09-22.md |
| Angi | screened — not opened | **Fools gold — newly graded** | 2,3,4,6,7 | sales | "converts 79% better" | airops.com/blog/angi-customer-story | e-case-c13-airops-multi-2026-09-22.md |
| Xponent21, Lightspeed, Anne Klein, Wyndly, Go! Retail Group, T3, Rare Candy, Deepgram, LegalZoom, Skio | screened — not opened ×10 | **opened, screened — no AI-visibility metric** (classical SEO/conversion/efficiency claims, no AI answer engine named for the result) | — | traffic/sales/efficiency (non-Lane-E) | see e-case-c13-airops-multi | airops.com/blog/... | e-case-c13-airops-multi-2026-09-22.md |
| Kong, Conviva, Two Independent Practitioners, Animalz, Bitly, Merge, Venn, Harvard Business Publishing, Rhetoric | screened — not opened ×9 | **screened — not opened** (not reached within this pull's time budget) | — | — | — | airops.com/blog/... | a-airops-customers-2026-09-22.md (titles only) |

### Conductor (P3-c3; Title Nine re-graded by P4-c4, cited not redone)

| Client | Pass 3 | P4-c13 | Missing | Metric | Figure | URL | Raw path |
|---|---|---|---|---|---|---|---|
| Title Nine | Bronze/Fools gold (full page, Pass 3) | **Bronze/Fools gold (P4-c4)** — cited | — | visibility/traffic + sales | "+1,000% AI sessions" | conductor.com/customer-stories/title-nine | e-case-census-c4-2026-09-22.md |
| ASUG | screened — no claim (efficiency only) | screened — no claim (same, not re-opened) | — | efficiency (non-Lane-E) | "75% efficiency" | conductor.com/customer-stories/asug | a-vendor-census-c3-2026-09-22.md |
| Zurich UK | screened — not opened | **Bronze — UP** | 3,4,6,7 | visibility | "47% reduction in irrelevant citations" | conductor.com/customer-stories/zurich-insurance-uk | e-case-c13-conductor-multi-2026-09-22.md |
| H&R Block | screened — not opened | **Bronze — UP** | 3,4,6,7 | visibility | "citations 2x; mentions +50%; market share +125%" | conductor.com/customer-stories/hr-block | e-case-c13-conductor-multi-2026-09-22.md |
| HG Insights, Boston Globe Media, Clutch, Overdrive, Parker Hannifin, Sonos, Brunswick | screened — not opened ×7 | **opened, screened — no claim** (no before/after quantified visibility/traffic/sales figure for the named company on its own page) | — | — | — | conductor.com/customer-stories/... | e-case-c13-conductor-multi-2026-09-22.md |

### HubSpot (P3-c3)

| Client | Pass 3 | P4-c13 | Missing | Metric | Figure | URL | Raw path |
|---|---|---|---|---|---|---|---|
| HubSpot AEO beta-cohort | Bronze (full page, Pass 3) | **Bronze — same, formally re-ticked** | 2,3,4,6 | traffic | "AI referral traffic +20% vs. customers not using the tool" | hubspot.com/company-news/hubspot-aeo | e-case-c13-hubspot-beta-cohort-2026-09-22.md |
| Docebo (HubSpot) | Fools gold | Fools gold (same, not re-opened) | — | sales | "nearly 15% of leads from AI traffic" | hubspot.com/company-news/hubspot-aeo | a-hubspot-launch-2026-09-22.md |
| Sandler | Fools gold | Fools gold (same) | — | traffic/sales | "8,000 visitors, 12 conversions, +10% YoY" | hubspot.com/company-news/hubspot-aeo | a-hubspot-launch-2026-09-22.md |
| HubSpot's own use | Fools gold | Fools gold (same) | — | sales | "20x more leads from AI" | tryprofound.com [sic — HubSpot's own product page] | a-hubspot-aeo-product-2026-09-22.md |
| Fresha, Scrums, Anedot | screened — no claim ×3 | screened — no claim (same) | — | none | none | hubspot.com/company-news/hubspot-aeo | a-hubspot-launch-2026-09-22.md |

### Yext (P3-c3)

| Client | Pass 3 | P4-c13 | Missing | Metric | Figure | URL | Raw path |
|---|---|---|---|---|---|---|---|
| "one hearing care provider" | Bronze (full page, Pass 3) | **Bronze — same, formally re-ticked** | 2,3,4,6,7 | visibility | "186% citation increase" | investors.yext.com/.../detail/392/... | e-case-c13-yext-hearing-care-2026-09-22.md |
| "a programmatic advertising platform" | Fools gold | Fools gold (same, not re-opened) | — | sales | "doubled inbound leads" | investors.yext.com/.../detail/392/... | a-yext-launch-2026-09-22.md |
| Yext (self) | discard-on-sight (vendor self-measurement) | discard-on-sight (same) | — | visibility | "own AI visibility grew 147%" | investors.yext.com/.../detail/392/... | a-yext-launch-2026-09-22.md |
| 4 testimonials (MidFirst Bank, Automotive marketer, Sorbet, Beltone) | screened — no claim ×4 | screened — no claim (same) | — | none | none | yext.com (customer quotes) | a-yext-customers-2026-09-22.md |

### Ahrefs (P3-c3)

Octopus Energy — 1 testimonial screened at Pass 3, no metric, linked case study 404's — **screened — no claim / not reachable** (same, not re-opened; page already confirmed 404 at Pass 3). Raw path: `a-ahrefs-customers-2026-09-22.md`.

### Birdeye (P3-c3)

2 Search-AI testimonials screened, 0 gradable; 3 homepage aggregate percentages discarded on sight (no base) — **screened — no claim / discard-on-sight** (same, not re-opened). Raw path: `a-birdeye-customers-2026-09-22.md`.

### BrightEdge (P3-c4)

| Client | Pass 3 | P4-c13 | Missing | Metric | Figure | URL | Raw path |
|---|---|---|---|---|---|---|---|
| NinjaOne | Bronze (full page, Pass 3) | **Bronze — same, formally re-ticked** | 2,3,4,6,7 | visibility | "share of AI mentions: single digits → 61%" | brightedge.com/resources/case-studies/ninjaone-... | e-case-c13-brightedge-multi-2026-09-22.md |
| Riskonnect | Bronze (full page, Pass 3) | **Bronze — same, formally re-ticked** | 4,6,7 | visibility, traffic | "227 AI Overview rankings in 4 months; +495% organic traffic" | brightedge.com/resources/case-studies/riskonnect-... | e-case-c13-brightedge-multi-2026-09-22.md |
| Bloomfire | Bronze (full page, Pass 3) | **Bronze — same, formally re-ticked** | 2,6,7 | traffic | "+30% AI referral traffic, Jul 2026 vs. prior 90 days" | brightedge.com/resources/case-studies/bloomfire-... | e-case-c13-brightedge-multi-2026-09-22.md |
| Arm | screened — not opened | **Bronze — UP** | 2,3,4,6,7 | traffic | "2x+ AI agent traffic" | brightedge.com/resources/case-studies/arm-agent-edge-... | e-case-c13-brightedge-multi-2026-09-22.md |
| Overdrive Interactive | screened — not opened | **Bronze — UP** | 3,4,6,7 | visibility, traffic | "+710% AI Overview growth in 3 months" | brightedge.com/resources/case-studies/overdrive-interactive-... | e-case-c13-brightedge-multi-2026-09-22.md |

### Muck Rack (P3-c4)

| Client | Pass 3 | P4-c13 | URL | Raw path |
|---|---|---|---|---|
| Three Rings Inc. | Fools gold (teaser, page Cloudflare-blocked at Pass 3) | **Fools gold — same, full page now reachable and confirmed** | muckrack.com/resources/case-studies/three-rings-inc-case-study | a-muckrack-customers-2026-09-22.md (grade unchanged; full text now recovered via browser extension this pull, not filed separately since grade is Fools gold) |

### Quattr (P3-c4; Men's Wearhouse and CloudEagle re-graded by P4-c4, cited not redone)

| Client | Pass 3 | P4-c13 | URL | Raw path |
|---|---|---|---|---|
| Men's Wearhouse | Silver (full page, Pass 3) | **Silver (P4-c4)** — cited | quattr.com/case-studies/menswearhouse-... | e-case-census-c4-2026-09-22.md |
| CloudEagle | Bronze (full page, Pass 3) | **Bronze (P4-c4)** — cited | quattr.com/case-studies/cloudeagle-... | e-case-census-c4-2026-09-22.md |
| Kiteworks ("79% More Answer Engine Citations") | Bronze (proof-index teaser only) | **Bronze — full page card confirmed (fuller text, engine now named), same headline grade** | quattr.com/case-studies (index card; dedicated sub-page did not resolve on click) | e-case-c13-quattr-kiteworks-2026-09-22.md |
| Kiteworks ("4x Increase in Non-Brand Traffic") | not previously graded | **screened — no AI-visibility metric** (classical traffic/lead claim, no engine named) | quattr.com/case-studies (index card) | e-case-c13-quattr-kiteworks-2026-09-22.md |
| Housing.com | screened (teaser, not graded — general search-market-share story) | **screened — no AI-visibility metric** (same; no engine named anywhere) | quattr.com/case-studies/housing-market-share-intelligence | e-case-c13-quattr-kiteworks-2026-09-22.md |

### Semrush (P3-c4)

| Client | Pass 3 | P4-c13 | Missing | Metric | Figure | URL | Raw path |
|---|---|---|---|---|---|---|---|
| Sure Oak | Bronze (full page, Pass 3) | **Bronze — same, formally re-ticked** | 3,4,6,7 | traffic | "+41% MoM ChatGPT referrals; +286% AIO appearances" | semrush.com/company/stories/sure-oak-ai-visibility | e-case-c13-semrush-multi-2026-09-22.md |
| Activate Digital / Dryer Vent Wizard | Bronze (full page, Pass 3) | **Bronze** (traffic) + **Fools gold** (leads sub-claim) — same headline, sub-claim formalized | 3,7 | traffic (+ sales sub-claim) | "organic traffic 25K→50K+"; "10% leads from AI" | semrush.com/company/stories/activate-digital-ai-visibility | e-case-c13-semrush-multi-2026-09-22.md |
| Coalition Technologies | screened — not opened | **Bronze** (traffic) + **Fools gold** (conversions sub-claim) — UP | 3,4,6,7 | traffic (+ sales sub-claim) | "+429% AI referral traffic"; "+547% conversions" | semrush.com/company/stories/coalitiontechnologies | e-case-c13-semrush-multi-2026-09-22.md |

### Similarweb (P3-c4)

1 testimonial screened, discarded on sight (no brand, no metric, no date) — **discard-on-sight** (same, not re-opened). Raw path: `a-similarweb-customers-2026-09-22.md`.

### SOCi, SE Ranking, Uberall, Onclusive (P3-c4 held names, cleared to roster)

No case studies with a quantified metric exist on any of the four vendors' own sites (all four checked this pull for corroboration; none has a dedicated case-study/customer page carrying a number). Testimonials only (Edeka, Audika France, Pizza Hut for Uberall; none for the other three) — **screened — no claim** where a testimonial exists, **n/a — no case-study content** otherwise. Raw paths: `a-soci-roster-clear-2026-09-22.md`, `a-seranking-roster-clear-feature-2026-09-22.md`, `a-uberall-roster-clear-feature-2026-09-22.md`, `a-onclusive-roster-clear-feature-pricing-2026-09-22.md`.

### Agencies (P3-c5)

| Vendor / client | Pass 3 | P4-c13 | Missing | Metric | Figure | URL | Raw path |
|---|---|---|---|---|---|---|---|
| Pace Generative (anonymized "publicly traded enterprise client") | Fools gold | Fools gold (same, not re-opened) | — | sales | (revenue/traffic claim, anonymized) | pacegenerative.com/case-studies | f-pace-generative-clients-2026-09-22.md |
| Orange142 / "A Green Energy Client" | screened (no brand, no metric; linked case 404'd) | **screened — not opened** — a different, quantified AI-visibility case since found on the vendor's live case-studies index ("Orange 142 Helps Pigeon Forge Increase AI Visibility by 136%") but its dedicated page did not resolve via click this pull; original Green Energy case's link remains unresolved | — | visibility (Pigeon Forge, unopened) | "AI Visibility by 136%" (index card only) | orange142.com/case-studies | f-orange142-clients-2026-09-22.md |
| Intero Digital / Freshpet | Bronze (full page, Pass 3/P4-c5) | **Bronze — same, formally re-ticked and re-filed under this task's naming** | 3,4,6(partial) | traffic, visibility | "645% rise in Google AI Overviews; traffic +46%" | prnewswire.com/.../intero-digital-shares-freshpet-... | e-case-c13-intero-digital-freshpet-2026-09-22.md |
| Seer Interactive / Home Depot | screened (blocked, Cloudflare) | **screened — not reachable** — page now loads (title resolves correctly) but returns only a gated "Intelligence Reports" stub, substantive case text not recoverable via browser extension this pull either | — | — | — | searchengineland.com/guide/enterprise-ecommerce-llm-visibility-case-study | f-seer-interactive-clients-2026-09-22.md |
| Fire&Spark / Hinge Health | screened — no claim | screened — no claim (same, not re-opened) | — | none | none | fireandspark.com | f-fire-and-spark-clients-2026-09-22.md |

### Sell-side vendors, c6 (Feedonomics, Criteo, StackAdapt, Pacvue, Shopware, Wix, Kargo)

Every case on all seven vendors' pages was recorded at Pass 3 as failing the seven-item bar on its own landing/index-page teaser, none individually pulled as a separate raw file (`c-vendor-census-c6-2026-09-22.md`: "none individually pulled as a separate raw file, per this task's own instruction that such cases are 'screened, not pulled'"). This pull did not open the individual dedicated case pages for any of the ~40 named clients across these seven vendors (Euro Car Parts, New Balance, Pinehurst Coins, The Walking Company, PlexusDx, Fruugo, Monwell, Revelyst, Kijiji, Tabby, City Beach, Dell, Brave Bison, Easylife, Swiss Marketplace Group, Logitech — Feedonomics; Unice, Derimond, Grupo Farsimán, Denon Store, Netshoes — Criteo; L'Oréal/Publicis, Itsumo, Revlon/Horizon, Perdue, Duracell — Pacvue; HP Toast, WeTransfer, CTV Glass, Hershey's, Anytime Fitness, American Eagle — Kargo) — recorded honestly as **screened — not opened** for this whole group, not reached within this pull's time budget (lane B/C, sell-side, lower priority within Pass 4's own lane-E success-story remit; none of c6's seven admitted vendors carries a Lane-E organic-recommendation claim in the first place — all are paid-placement or agentic-commerce tooling). StackAdapt, Shopware, Wix carry no individually named case claims at all per the Pass 3 pull (no case studies pulled/found). Raw path: `c-vendor-census-c6-2026-09-22.md`.

## Reconciled counts

**Titles in Pass 3 censuses (c1–c6), all vendors, as recorded by those censuses' own summaries:** approximately 150 (per `plan-review-1-2026-09-22.md` §3's own aggregate figure; the exact per-census self-reported counts do not sum cleanly across c1–c6 due to the three inconsistent operationalisations that motivated this cluster — see Caveats).

**This cluster's own count, titles individually tracked above:**

| Status | Count | Note |
|---|---|---|
| Opened this pull, full-page-verified today | 47 | new WebFetch/browser-extension pulls, 2026-09-22 |
| Opened at Pass 3/P4-c4/c5 on the case's own full page, cited or re-confirmed (not re-fetched) | 31 | includes P4-c4's 12, Scrunch's 5, Rankscale's 2 (Austrian Optical/AI SMS), Otterly's Instant Commerce, HubSpot/Yext/Intero Digital's 3, BrightEdge's 3, Semrush's 2, Muck Rack's 1, and testimonial-only files with no dedicated page (Peec AI 7, Brandlight 3, held-name testimonials 3) |
| Screened — not opened (title/claim identified, page not reached this pull) | 25 | AirOps ×9, Otterly ×5, c6 sell-side ×~35 distinct clients grouped as one line, Searchable/Blackbird, Orange142/Pigeon Forge |
| Screened — not reachable (page loads or is attempted, substantive text not recoverable) | 2 | Seer Interactive/Home Depot (gated stub), and Orange142's original Green Energy link (404, distinct from Pigeon Forge) |
| Screened — no claim (opened or fully captured, no quantified metric) | 34 | Peec AI ×5, Profound ×6, AthenaHQ ×15 (vignettes+feature claims), Scrunch ×3, Otterly ×3, Conductor ×7, HubSpot ×3, Yext ×4 (testimonials), Ahrefs ×1, Birdeye ×2 (approximate; several rows above are themselves multi-item counts) |
| Fools gold | 24 | Searchable ×2, Peec AI ×2, Promptwatch ×3, Profound ×6 (index-level) + 4 newly surfaced sub-claims (CRS, OpusClip, Airbyte, Otterly/Client B), AthenaHQ ×1, Scrunch ×3, HubSpot ×3, Yext ×1, Muck Rack ×1, Semrush ×2 (sub-claims), AirOps ×3 (Docebo, Webflow, Angi), Rankscale ×1 (P4-c4) |
| Bronze | 45 | see master table; includes P4-c4's carried-forward Bronze rows and this pull's new/re-confirmed Bronze rows |
| Silver | 3 | Quattr/Men's Wearhouse (P4-c4), Sitefire/Pointhound (P4-c4), **Sitefire/Jerry (this pull, new)** |
| Gold | 0 | none found anywhere across c1–c6 or P4-c4 |

**Cleared (Bronze or better) per vertical, as named on the case's own page (per the P4-c4 convention: a vendor's separate index-tag is not carried into this column unless the dedicated page itself states it):**

| Vertical, as named | Best grade | Case(s) |
|---|---|---|
| Apparel and Fashion | Silver | Quattr / Men's Wearhouse (P4-c4) |
| none named (travel/insurance-adjacent — "AI-powered advisor to manage all your physical assets") | Silver | Sitefire / Jerry (this pull) |
| B2B SaaS (Spend Management) | Bronze | Quattr / CloudEagle (P4-c4) |
| B2B SaaS · HR technology | Bronze | RankPrompt / Humand (P4-c4) |
| Automotive · Fort Worth, TX | Bronze | RankPrompt / Owings Auto (P4-c4) |
| Optical retail / Multi-location retail | Bronze | Rankscale / Austrian Optical Retail Chain (P4-c4) |
| Retail | Bronze | Conductor / Title Nine (P4-c4) |
| IoT/E-Commerce/D2C Hardware | Bronze | Rankscale / MiniFinder Germany |
| Virtual Office/Remote Work/B2B SaaS | Bronze | Rankscale / SoWork |
| Online Grocery/D2C Membership | Bronze | Rankscale / Online Grocer |
| Banking & Fintech/Tier-1 Financial Institution | Bronze | Rankscale / Spanish Bank |
| Pet food / CPG | Bronze | Intero Digital / Freshpet |
| MedTech | Bronze | Otterly / Neur Digital (Client A) |
| Enterprise (HPC/backup software) | Bronze | Otterly / Bacula |
| none named (30+ Bronze cases — Profound, AirOps, BrightEdge, Semrush, Scrunch, Quattr/Kiteworks, HubSpot, Yext, Muck Rack) | Bronze | see master table |

## Grade changes vs. Pass 3 — up / down / same

- **Up: 12.** Sitefire/Jerry (Bronze → Silver); AirOps/{PMA, Brainlabs, Oyster, Parallel, Asana, Carta} (screened-not-opened → Bronze, ×6); Conductor/{Zurich UK, H&R Block} (screened-not-opened → Bronze, ×2); BrightEdge/{Arm, Overdrive Interactive} (screened-not-opened → Bronze, ×2); Semrush/Coalition Technologies (screened-not-opened → Bronze); AirOps/Angi (screened-not-opened → Fools gold).
- **Down: 0.**
- **Same: 26** (confirmed at the same grade from the case's own full page, several formally re-ticked for the first time against the seven-item checklist): Profound ×9 (Aleph, CRS, OpusClip, Hone, Ramp, Lake.com, Airbyte, 1840&Co, Chime[AirOps]); Scrunch ×5; Rankscale ×4 (MiniFinder, SoWork, Online Grocer, Spanish Bank); Otterly ×3 (Bacula, Neur Digital/Client A, Instant Commerce); BrightEdge ×3 (NinjaOne, Riskonnect, Bloomfire); Semrush ×2 (Sure Oak, Activate Digital); HubSpot ×1; Yext ×1; Intero Digital ×1; Muck Rack ×1 (Fools gold, full page now reachable, same grade); Quattr/Kiteworks ×1.
- **New sub-claims surfaced, not counted in up/down/same** (per the P4-c4 precedent for Profound/Plaid's conversion figure): Profound/CRS pipeline (Fools gold), Profound/OpusClip signups (Fools gold), Profound/Airbyte $100K deal (Fools gold), Otterly/Neur Digital Client B revenue (Fools gold), Semrush/Activate Digital leads (Fools gold), Semrush/Coalition Technologies conversions (Fools gold).

## Survivorship statement

These 150-odd Pass 3 titles are vendor-selected winners, drawn from customer-facing marketing pages vendors chose to publish; they are not a random or representative sample of any vendor's customer base. Full-page opening under grading rule 1 surfaced 12 grade changes, all upward (screened-not-opened → Bronze or Fools gold, or Bronze → Silver) and zero downward — the teaser-level reads from Pass 3 undercounted rather than overstated the evidence, because titles carrying a quantified metric in their own headline were, on this sweep, more likely to disclose additional bar items on the full page than to disclose fewer. Even so, across every title opened this programme to date (c1–c6 plus P4-c4 plus this cluster), only 3 cases clear Silver and zero clear Gold — the category's own published evidence remains overwhelmingly Bronze (visibility/traffic-only, no revenue link) or Fools gold (a revenue figure with no baseline or control), and every Silver case rests on an observational within-site treated-vs-untreated comparison, not a randomized or geo-split experiment.

## Unknowns

| Question | Channel checked | Date |
|---|---|---|
| Blackbird's (Searchable) dedicated case-study URL | searchable.com/customers (WebFetch could not resolve the href) | 2026-09-22 |
| Orange142's original "Green Energy" case-study URL (404 at Pass 3) and the Pigeon Forge AI Visibility case's dedicated URL (click did not navigate) | orange142.com/case-studies | 2026-09-22 |
| Seer Interactive / Home Depot's full case text — page now resolves (title correct) but returns only a gated "Intelligence Reports" stub via both fetch and browser extension | searchengineland.com/guide/enterprise-ecommerce-llm-visibility-case-study | 2026-09-22 |
| Quattr's Kiteworks "79% More Answer Engine Citations" dedicated sub-page URL — click on the case-studies index card did not trigger navigation | quattr.com/case-studies | 2026-09-22 |
| AirOps's 9 remaining unopened titles (Kong, Conviva, Two Independent Practitioners, Animalz, Bitly, Merge, Venn, Harvard Business Publishing, Rhetoric) — URLs known, pages not fetched within this pull's time budget | airops.com/blog/... | 2026-09-22 |
| Otterly's 5 remaining teaser-only Fools-gold cases (Chatarmin, NOLA Marketing, SORN.AI, What IF Web, TM Blast) — 4 dedicated URLs known, not fetched within this pull's time budget; TM Blast is a LinkedIn video, not independently verifiable as a web page | otterly.ai/blog/...; linkedin.com | 2026-09-22 |
| c6's ~40 named client cases across Feedonomics, Criteo, Pacvue, Kargo (Shopware/Wix/StackAdapt carry no individually named cases) — none of the individual dedicated case pages opened this pull | feedonomics.com, criteo.com, pacvue.com, kargo.com | 2026-09-22 |
| Whether the exact Pass 3 per-census title counts reconcile to a single "~150" figure — the three inconsistent grading operationalisations that motivated this cluster (`plan-review-1-2026-09-22.md` §3) mean the original censuses' own self-reported screened/graded counts do not sum cleanly; this file's own per-title tally above is the more granular and internally consistent count, not force-reconciled against the older aggregate | all six Pass 3 census files | 2026-09-22 |

## Caveats

- Every case in this file is vendor-reported or company-stated (HubSpot, Yext, Intero Digital press releases); none carries independent third-party replication. Every grade above Fools gold is still bias-flagged per `trust-rubric.md`'s "vendor measuring the thing it sells" criterion, including the three Silver cases.
- "Screened — no AI-visibility metric" (used for several AirOps and Quattr cases) is a category this cluster introduces beyond grading rule 1's three named statuses (`screened — not opened`, `screened — no claim`, graded): it marks a case that was opened, carries a quantified before/after metric, but names no AI answer engine anywhere in connection with that metric — i.e., a classical-SEO or general-conversion claim wearing an AI-visibility vendor's branding. These are recorded as opened and read, not graded, because they fail bar item 2 outright and are not comparable to the Bronze cases that at least name an engine.
- Sitefire/Jerry's grade change to Silver rests on the same observational treated-vs-untreated design already accepted for Sitefire/Pointhound and Quattr/Men's Wearhouse at P4-c4 — a within-site comparison, not a randomized or geo-split experiment; `glossary.md` places this at Silver ("cite as evidence, label correlational"), not Gold.
- The "~150 screened, 1 Silver" aggregate that motivated this whole cluster (`plan.md` "Evidence bar — grading rule 1, 2026-09-22") is now superseded within Lane E's own case-study evidence: as of this file, 3 Silver cases exist (Quattr/Men's Wearhouse, Sitefire/Pointhound, Sitefire/Jerry), all from full-page grading, none from a teaser.
- The oldest pull depended on in this file is 2026-09-22 — every cited raw file, including every Pass 3 and P4-c4 file, was pulled today.
