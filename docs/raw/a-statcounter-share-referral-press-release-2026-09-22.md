# StatCounter Global Stats — press release: "New Statcounter AI data finds ChatGPT sends 79.8% of all chatbot referrals to websites"

```yaml
source:          StatCounter Global Stats (press release)
url_or_doc_id:   https://gs.statcounter.com/press/new-statcounter-ai-data-finds-chatgpt-sends-79-perc-of-all-chatbot-referrals-to-websites
published:       2025-06-11
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            4
tier_reason:     table default for clickstream/tag-based telemetry with sample size stated (3.8bn page views/mo, 1.5m sites); STALE — published 2025-06-11, more than one quarter before this pull date (`plan.md` staleness rule); filed as a dated historical baseline, re-check required before any compiled file cites it
source_label:    analyst-derived
lane:            A
sub_market:      organic recommendation
engine:          ChatGPT, Perplexity, Microsoft Copilot, Google Gemini, DeepSeek, Claude; Grok explicitly excluded by the source
metric_kind:     traffic
supersedes:      none
captured:        section extract via fetch tool (AI-summarized from source HTML)
```

## Verbatim (as extracted)

### Global Referral Share — May 2025

- ChatGPT: 79.8%
- Perplexity: 11.8%
- Microsoft Copilot: 5.2%
- Google Gemini: 2%
- DeepSeek: 0.8%
- Claude: 0.5%

### Sample Size & Data Collection

"over 3.8 billion page views per month to over 1.5 million websites"

### Methodology (as stated in the release)

The data measures "the number of referrals from individual AI chatbots to websites" and is "updated daily by individual country and region." A complete methodology statement explaining the underlying collection mechanism (panel-based vs. census/tag-based) beyond the page-view/site-network description is not included in this document.

### Notable statements

- DeepSeek leads in China with 89.3% chatbot-referral share, while ChatGPT dominates across all other G20 nations.
- "Grok cannot be included in the data, as unlike the other chatbots, it does not provide referral data in its header." [note: explicit method-driven exclusion, stated by the source]

### Release date vs. data window

Announcement issued 2025-06-11; data window appears to be May 2025.

## Pull notes — mechanical only

- Access: plain fetch succeeded (200).
- This is the same underlying StatCounter chatbot-referral series as the live dashboard pulled in `a-statcounter-share-ai-chatbot-market-share-2026-09-22.md`, at an earlier date — kept as a separate dated file per the re-pull rule (old pull never edited or deleted).
- Grok's structural exclusion from StatCounter's entire chatbot-referral series (source does not receive referral-header data from Grok) is recorded here because it explains an absence in every StatCounter pull in this cluster, not just this one.
