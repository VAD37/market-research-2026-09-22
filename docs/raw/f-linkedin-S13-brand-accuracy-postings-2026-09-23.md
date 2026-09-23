# LinkedIn Jobs (guest search API) — S13 brand-accuracy job-posting sweep, worldwide, three queries

```yaml
source:          LinkedIn Jobs, public guest search endpoint (no login)
url_or_doc_id:   https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=<term>&location=Worldwide&start=0 — terms: "AI reputation" ; "\"brand accuracy\" AI" ; "LLM misinformation brand"
published:       posting dates per card (datetime attribute), 2026-06-06 to 2026-09-21
pull_date:       2026-09-23
pull_method:     fetch (curl, paced 12 s between calls); first result page only (10 cards max)
pull_purpose:    evidence about a number (S13 job-posting signal)
tier:            3
tier_reason:     employer's own posting via the platform's public listing (demand-signals.md S1 default 3); first-page relevance sort, not a count
source_label:    company-stated
lane:            F
sub_market:      n/a
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        card fields (title | employer | location | posted date | URL) for every card returned
```

## Verbatim — cards returned

Query `AI reputation` (10 cards):
```
Head of AI & Innovation Communications, APAC | Meta | Singapore, Singapore | 2026-09-11
Communications Lead (KR) | FuriosaAI | Seoul, Seoul, South Korea | 2026-09-11
负面舆情业务专家 - AI Builder | Wisers Information Limited | Beijing, Beijing, China | 2026-06-06
负面舆情业务专家 - AI Builder | Wisers Information Limited | Shanghai, Shanghai, China | 2026-06-06
PR & Communication Lead(A163386) | AI Rudder | Greater Kuala Lumpur | 2026-09-18
Chargé de veille | Opinion Act by JIN | Greater Lyon Area | 2026-09-21
Trust & Safety Specialist (Content Moderator) with Russian and English | Accenture Poland | Cracow, Małopolskie, Poland | 2026-09-18
GenAI Content Trust and Safety Experts – German speaker | TP | Athens, Attiki, Greece | 2026-09-11
Trust & Safety Specialist (Content Moderator) with English and Estonian | Accenture Poland | Cracow, Małopolskie, Poland | 2026-09-03
Social Escalations Manager | Anthropic | New York, NY | 2026-09-10
```

Query `"brand accuracy" AI` (6 cards):
```
PE-Digital Content Services | Cognizant | Kuala Lumpur, Malaysia | 2026-09-09
Operations Specialist, AI Enablement [Content Moderation] | Bumble Inc. | London, England, United Kingdom | 2026-09-21
AI Model Evaluation & Quality Strategy Specialist Graduate (AI Data Service Operations) - 2027 Start | TikTok | Kuala Lumpur, Malaysia | 2026-09-21
AI Labeling & Evaluation Agent (German-Speaking) | Concentrix | Lisboa, Lisbon, Portugal | 2026-09-19
AI Quality Engineer | Rootly | Toronto, Ontario, Canada | 2026-06-16
Senior AI Evaluation & RLHF Specialist | Innodata Inc. | Philippines | 2026-09-15
```

Query `LLM misinformation brand` (6 cards):
```
Head of AI Safety | Moonshot | Toronto, Ontario, Canada | 2026-08-07
Operations Specialist, AI Enablement [Content Moderation] | Bumble Inc. | London, England, United Kingdom | 2026-09-21
Head of AI Safety | Moonshot | Canada | 2026-08-07
Senior AI Engineer, AI Systems (India) | Credo AI | India | 2026-06-10
Vice President, Artificial Intelligence | Mitchell International, Inc. | United States | 2026-08-05
Safety Operations Lead | Thinking Machines Lab | San Francisco, CA | 2026-09-01
```

[note: none of the 22 cards is a brand-side marketing, communications or SEO role whose title names correcting or monitoring how AI assistants describe the employer's brand. The cards are AI-lab, trust-and-safety, content-moderation, data-labelling and PR roles. "Chargé de veille" at Opinion Act by JIN (a French media-monitoring agency) is the nearest to reputation monitoring and is sell-side. Job descriptions were not opened for this sweep.]

## Pull notes — mechanical only

- All three calls HTTP 200; card counts 10 / 6 / 6 (LinkedIn returns fewer than 10 when the query has few matches). Relevance-sorted first page; no pagination.
- Same endpoint and pacing as `docs/raw/f-signal-bs-S1-linkedin-jobs-guest-api-2026-09-22.md`.
