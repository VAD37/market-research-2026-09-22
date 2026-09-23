# Space Exploration Technologies Corp. (SpaceX, parent of xAI) — Form S-1/A: Grok and X monthly active users

```yaml
source:          Space Exploration Technologies Corp. (SPCX), CIK 0001181412 — Form S-1/A, File No. 333-296070
url_or_doc_id:   https://www.sec.gov/Archives/edgar/data/1181412/000162828026040364/spaceexplorationtechnologib.htm (accession 0001628280-26-040364)
published:       2026-06-03 (filing date; original S-1 filed 2026-05-20, S-1/A 2026-06-01)
pull_date:       2026-09-23
pull_method:     fetch (curl with contact User-Agent from sec.gov Archives; located via efts.sec.gov full-text search "Grok", forms S-1; HTML stripped to text, sentences matched on "monthly active", "MAU", "Grok")
pull_purpose:    evidence about a number
tier:            2
tier_reason:     table default — SEC filing
source_label:    filed
lane:            E (Pass 13)
sub_market:      n/a — engine user counts
engine:          Grok — xAI (SpaceX subsidiary)
metric_kind:     none (user counts)
supersedes:      none
verbatim:        partial — matched sentences verbatim
captured:        sentence extracts from a 12.1 MB filing
```

## Verbatim

> "'MAU' (or monthly active users) refers to the total number of users who have interacted with Grok or X through web browsers or mobile applications at least once during the 30-day period ending on the date of measurement ('active users')."

> "In presenting combined MAUs across the two platforms, we seek to identify and account for users who access both Grok and X based on sign-in traffic so that such users are not double-counted when measuring MAU."

> "While we believe our methodologies provide a reasonable approximation of MAU based on the number of unique users, they may not fully capture all instances of duplication, and our reported MAU should be viewed as an estimate of unique users across our Grok and X platforms for the applicable period."

> "...[1.]3 billion supported accounts active in the last twelve months ended March 31, 2026 and December 31, 2025, including approximately 550 million and 520 million MAUs as of March 31, 2026 and December 31, 2025, respectively."
[note: the leading digit(s) before "3 billion" were cut by the sentence splitter at a decimal point; exact figure not captured]

> "Of our MAUs, we had approximately 117 million and 89 million MAUs that used Grok's AI features as of March 31, 2026 and December 31, 2025, respectively."

> "Grok increasingly supports this strategy by helping advertisers with campaign creation, creative optimization, and alignment with trending topics and user intent."

> "The increase in AI solutions and infrastructure revenue is mainly due to an increase in X and Grok subscription revenue of $365 million and an increase in revenue from data licensing arrangements of $88 million."

> "...an increase in revenue from our AI segment of $581 million as advertising, Grok and X subscriptions, and data licensing arrangements grew."

[note: two subscriber sentences matched as "...9 million SuperGrok and SuperGrok Heavy paid subscribers." and "...9 million SuperGrok, SuperGrok Heavy and SuperGrok Lite paid subscribers." — leading digits cut at a decimal point by the splitter; figures not captured]

## Pull notes — mechanical only
- efts.sec.gov full-text search returned 2 hits for "Grok" + "monthly active" in S-1 forms (both SpaceX S-1/A); the 2026-06-03 amendment was downloaded (12,116,979 bytes).
- Search-result summary claiming "December 2025 figure of 35 million" is contradicted by the filing's own "89 million" for 2025-12-31; the filing text is recorded.
- Grok-specific advertising revenue: not isolated in the matched sentences.
