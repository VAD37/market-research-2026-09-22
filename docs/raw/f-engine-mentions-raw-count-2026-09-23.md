# Measured-by-us — engine-name mention counts per vertical over raw files already pulled (skincare, B2B SaaS, high-CPA, local / multi-location, Indeed cards)

```yaml
source:          our own regex count over docs/raw/ files on disk at 2026-09-23 (files listed below); no external fetch
url_or_doc_id:   docs/raw/ file globs listed per group below
published:       n/a — count made 2026-09-23 over files dated 2026-09-22 and 2026-09-23
pull_date:       2026-09-23
pull_method:     python re.findall over each file's full text (headers, query strings, quoted text and pull notes included); patterns listed below; counted mentions and files-with-at-least-one-mention
pull_purpose:    evidence about a number
tier:            1
tier_reason:     measured-by-us on the count itself; each counted mention keeps the tier of the raw file it sits in, which ranges 2–6 across the groups
source_label:    measured-by-us
lane:            F
sub_market:      organic recommendation (files span paid and agentic where their headers say so)
engine:          ChatGPT; Gemini / AI Mode / AI Overviews; Perplexity; Copilot; Claude; Rufus / Alexa for Shopping; Grok
metric_kind:     none
supersedes:      none
captured:        counts only; no text
```

## Patterns (case-sensitive, word-bounded)

| Engine | Regex |
|---|---|
| ChatGPT | `\bChatGPT\b` |
| Gemini / AI Mode / AI Overviews | `\bGemini\b|\bAI Mode\b|\bAI Overviews?\b` |
| Perplexity | `\bPerplexity\b` |
| Copilot | `\bCopilot\b` |
| Claude | `\bClaude\b` |
| Rufus / Alexa for Shopping | `\bRufus\b|Alexa for Shopping` |
| Grok | `\bGrok\b` |

## Counts — mentions (files with ≥1 mention)

| Group | Files | ChatGPT | Gemini / AI Mode / AIO | Perplexity | Copilot | Claude | Rufus | Grok |
|---|---|---|---|---|---|---|---|---|
| skincare | 26 | 91 (18) | 51 (13) | 8 (4) | 2 (1) | 16 (6) | 17 (3) | 0 (0) |
| b2b-saas | 38 | 104 (22) | 63 (16) | 30 (10) | 17 (5) | 29 (10) | 0 (0) | 0 (0) |
| high-cpa | 22 | 49 (10) | 35 (7) | 15 (6) | 0 (0) | 7 (3) | 0 (0) | 2 (2) |
| local-existing (vendor profiles and cases on disk before this pass) | 24 | 60 (13) | 74 (12) | 42 (12) | 4 (2) | 15 (5) | 0 (0) | 3 (2) |
| local-new (this pass's pulls) | 6 | 37 (4) | 28 (3) | 10 (4) | 2 (2) | 10 (4) | 0 (0) | 5 (2) |
| local total | 30 | 97 (17) | 102 (15) | 52 (16) | 6 (4) | 25 (9) | 0 (0) | 8 (4) |
| indeed-mixed | 1 | 1 (1) | 1 (1) | 1 (1) | 1 (1) | 0 (0) | 0 (0) | 0 (0) |

[note: the local-existing count was run with a wider ChatGPT pattern (`\bChatGPT\b|\bOpenAI\b`) and a Gemini pattern that also matched `\bAIO\b`; the other groups and local-new were run with the patterns in the table above. The local-existing row is therefore an upper bound relative to the others by the `OpenAI` and `AIO` matches; not re-run.]

## File lists

- skincare: e-case-c8-beautymatter-emarketer-ai-visibility-index-2026-09-22.md, e-case-c8-beautymatter-stella-rising-geo-webinar-2026-09-22.md, e-case-c8-beautymatter-ulta-google-agentic-2026-09-22.md, e-case-c8-cosmeticsbusiness-estee-lauder-profound-2026-09-22.md, e-case-c8-elf-beauty-chopra-llm-discovery-2026-09-22.md, e-case-c8-estee-lauder-profound-partnership-2026-09-22.md, e-case-c8-glossy-5w-ai-beauty-citations-2026-09-22.md, e-case-c8-glossy-beauty-briefing-sephora-ulta-ai-2026-09-22.md, e-case-c8-glossy-sephora-google-ai-2026-09-22.md, e-case-census-c8-2026-09-22.md, e-case-emarketer-ai-visibility-index-beauty-q1-2026-primary-2026-09-23.md, e-case-wwd-beauty-ai-search-coverage-primary-2026-09-23.md, f-signal-census-sk-2026-09-22.md, f-signal-sk-S1-jobs-linkedin-indeed-upwork-freelancer-2026-09-22.md, f-signal-sk-S10-procurement-2026-09-22.md, f-signal-sk-S11-price-paid-2026-09-22.md, f-signal-sk-S12-llms-txt-beauty-domains-2026-09-22.md, f-signal-sk-S4-omr-reviews-2026-09-22.md, f-signal-sk-S5-hn-algolia-reddit-2026-09-22.md, f-signal-sk-S6-agentic-alhena-tatcha-2026-09-23.md, f-signal-sk-S6-gr0-agency-case-studies-2026-09-22.md, f-signal-sk-S6-paid-agencies-2026-09-23.md, f-signal-sk-S7-coty-10k-2026-09-22.md, f-signal-sk-S7-coty-8k-q4-fy2026-2026-09-23.md, f-signal-sk-S8-conference-agendas-2026-09-22.md, f-signal-sk-S9-google-trends-2026-09-22.md
- b2b-saas: e-case-airops-chime-case-study-2026-09-23.md, e-case-airops-chime-quill-2026-09-23.md, e-case-airops-merge-2026-09-23.md, e-case-airops-unopened-multi-2026-09-23.md, e-case-airops-venn-2026-09-23.md, e-case-c9-deeploi-radyant-2026-09-22.md, e-case-c9-demandbase-labs-2026-09-22.md, e-case-c9-g2-traffic-momentum-2026-09-22.md, e-case-c9-heyflow-mrr-radyant-2026-09-22.md, e-case-c9-heyflow-youtube-radyant-2026-09-22.md, e-case-c9-hubspot-omr-podcast-2026-09-22.md, e-case-c9-optimist-b2b-tech-aeo-2026-09-22.md, e-case-c9-peec-ai-radyant-heyflow-2026-09-22.md, e-case-c9-previsible-ai-discovery-2026-09-22.md, e-case-census-c9-2026-09-22.md, e-case-chime-careers-airops-2026-09-23.md, e-case-fortune-hubspot-blog-traffic-loss-2026-09-23.md, e-case-fortune-hubspot-blog-traffic-loss-primary-2026-09-23.md, e-case-hubspot-aeo-data-cohort-2026-09-23.md, f-signal-bs-S1-indeed-2026-09-22.md, f-signal-bs-S1-linkedin-jobs-guest-api-2026-09-22.md, f-signal-bs-S1-upwork-freelancer-2026-09-22.md, f-signal-bs-S10-procurement-2026-09-22.md, f-signal-bs-S11-price-paid-2026-09-22.md, f-signal-bs-S12-llms-txt-domains-2026-09-22.md, f-signal-bs-S2-S3-vendor-census-citation-2026-09-22.md, f-signal-bs-S4-g2-capterra-2026-09-22.md, f-signal-bs-S4-omr-2026-09-22.md, f-signal-bs-S5-S6-paid-agentic-2026-09-23.md, f-signal-bs-S5-hn-algolia-2026-09-22.md, f-signal-bs-S5-reddit-2026-09-22.md, f-signal-bs-S6-flow-agency-2026-09-22.md, f-signal-bs-S7-earnings-calls-citation-2026-09-22.md, f-signal-bs-S7-hubspot-10k-xfunnel-2026-09-23.md, f-signal-bs-S7-techtarget-10k-2025-2026-09-23.md, f-signal-bs-S8-conference-sessions-citation-2026-09-22.md, f-signal-bs-S9-google-trends-2026-09-22.md, f-signal-census-bs-2026-09-22.md
- high-cpa: e-case-aicited-national-insurance-carrier-primary-2026-09-23.md, e-case-c10-sitefire-jerry-2026-09-22.md, e-case-census-c10-2026-09-22.md, e-case-fireandspark-supplement-citations-2026-09-23.md, f-signal-census-hr-2026-09-22.md, f-signal-hr-S1-indeed-upwork-freelancer-2026-09-22.md, f-signal-hr-S1-linkedin-2026-09-22.md, f-signal-hr-S10-procurement-2026-09-22.md, f-signal-hr-S11-price-paid-2026-09-22.md, f-signal-hr-S12-llmstxt-sample-2026-09-22.md, f-signal-hr-S2-paid-agentic-check-2026-09-23.md, f-signal-hr-S4-review-sites-2026-09-22.md, f-signal-hr-S5-community-2026-09-22.md, f-signal-hr-S6-agency-pages-2026-09-22.md, f-signal-hr-S7-ehealth-10k-2025-2026-09-23.md, f-signal-hr-S7-ehealth-10q-q2-2026-2026-09-23.md, f-signal-hr-S7-legalzoom-10q-q2-2026-2026-09-23.md, f-signal-hr-S7-p4c1-crossref-2026-09-22.md, f-signal-hr-S7-primerica-10k-2026-09-22.md, f-signal-hr-S8-conferences-2026-09-22.md, f-signal-hr-S9-search-interest-2026-09-22.md, f-signal-hr-band-attribution-2026-09-23.md
- local-existing: a-birdeye-customers-2026-09-22.md, a-birdeye-launch-2026-09-22.md, a-birdeye-pricing-2026-09-22.md, a-birdeye-search-ai-product-2026-09-22.md, a-locafy-careers-2026-09-22.md, a-locafy-customers-2026-09-22.md, a-locafy-docs-2026-09-22.md, a-locafy-engines-2026-09-22.md, a-locafy-funding-filing-2026-09-22.md, a-locafy-method-2026-09-22.md, a-locafy-pricing-2026-09-22.md, a-soci-product-pricing-2026-09-22.md, a-soci-roster-clear-2026-09-22.md, a-uberall-pricing-2026-09-22.md, a-uberall-roster-clear-feature-2026-09-22.md, a-yext-8k-q2-fy2027-goshine-2026-09-23.md, a-yext-customers-2026-09-22.md, a-yext-filing-2026-09-22.md, a-yext-launch-2026-09-22.md, a-yext-method-2026-09-22.md, a-yext-pricing-2026-09-22.md, a-yext-scout-product-2026-09-22.md, e-case-birdeye-arrow-senior-living-2026-09-23.md, e-case-boily-dental-geo-comparison-2026-09-23.md
- local-new: f-edgar-fts-local-multilocation-S7-2026-09-23.md, f-birdeye-multilocation-ai-search-S2-S6-2026-09-23.md, f-yext-customer-stories-local-S2-2026-09-23.md, f-localfalcon-brightlocal-whitespark-local-ai-S6-S8-2026-09-23.md, f-llms-txt-multilocation-domains-S12-2026-09-23.md, f-linkedin-guest-api-local-S1-2026-09-23.md
- indeed-mixed: f-indeed-S1-repull2-2026-09-23.md

## Pull notes — mechanical only

- Counts include YAML headers (`engine:` lines), URLs and query strings, so a file that pulled a "ChatGPT ads" query contributes mentions without a buyer behind them.
- "Google" alone, "AI search", "LLM" and "answer engine" were not counted as engines.
- Group membership is by filename glob; a file can belong to one group only as listed.
