# Image transcription — OtterlyAI HTML vs Markdown experiment, three images

```yaml
source:          OtterlyAI (otterly.ai) blog — image transcription of docs/raw/img/e-case-otterly-html-vs-markdown-experiment-repull2-2026-09-23/
url_or_doc_id:   https://otterly.ai/blog/geo-experiment-html-vs-markdown/
published:       2026-04-01 (last updated)
pull_date:       2026-09-23
pull_method:     fetch (image read by agent, Read tool on saved JPG/JPEG)
pull_purpose:    evidence about a number
tier:            5
tier_reason:     same as the pull this transcribes — vendor-published, no third-party replication
source_label:    vendor-reported
lane:            E
sub_market:      organic recommendation
engine:          n/a (dashboard UI, no per-bot breakdown shown)
metric_kind:     visibility (citations)
supersedes:      none
captured:        three images, full transcription each
```

## Transcription

**01 — OtterlyAI marketing landing page screenshot**: "Best AI Search Optimization Software in Comparison: Why OtterlyAI Drives 132% More Citations" — badges "Gartner Cool Vendor 2025", "G2 Top SEO Software Q4 2025"; stat tiles "132% — Average Citation Increase", "20,000+ — Marketing Professionals trust OtterlyAI...", "4.9/5 — G2 High Performer Rating"; five numbered "Key Takeaways" cite outside claims not part of this experiment (Princeton University research "15-20% effectiveness", "85% of enterprise searches will be AI-powered by 2026", McKinsey "40% of users trust AI-cited brands more", Gartner "70% of search will be conversational by 2025"). This is the rendered marketing page itself, not an experiment figure — recorded for completeness per its role as the Scenario A "existing HTML page" test subject.

**02 — "Citations" dashboard, Brand Report › OtterlyAI Markdown Control 2 › Citations, filter "Last 14 days"**: table columns URL / Brand Mentioned / Competitors / Domain / Domain Category / Cited.

| URL | Brand Mentioned | Domain | Domain Category | Cited |
|---|---|---|---|---|
| Enterprise AI Search Visibility Tool \| OtterlyAI Platform (otterly.ai/enterprise-ai-search-visibility-tool) | Yes | otterly.ai | Brand | **52** |
| Best AI Search Analytics Tool for SEO Teams: Otterly... (otterly.ai/best-ai-search-analytics-tool-for-seo-teams) | Yes | otterly.ai | Brand | **17** |
| Enterprise AI Search Visibility Tool \| OtterlyAI Platform (...-visibility-tool**.md**) | No | otterly.ai | Brand | **0** |
| Best AI Search Analytics Tool for SEO Teams: Otterly... (...-seo-teams**.md**) | No | otterly.ai | Brand | **0** |

New figure not in the article's own text: the two HTML pages were cited **52 and 17 times respectively** (69 total) in this 14-day citations dashboard, while both `.md` counterparts show **0** — a per-page citation count. The article's text states only the aggregate crawler-visit figure ("7.4% vs 0%... 137 [visits] over 14 days") and "zero .md citations" without per-page counts; this dashboard is a citations-tracking view (a different OtterlyAI product surface — "Brand Report") from the Agentic Analytics crawler-visit view the article's prose describes, so the "52"/"17" figures are citation counts, not crawler visits, and should not be summed against the "137" visit figure.

**03 — Raw Markdown source screenshot** (plain-text rendering, page title "# Best AI Search Optimization Software in Comparison: Why OtterlyAI Drives 132% More Citations"): confirms the `.md` mirror page carries near-identical prose content to image 01's rendered HTML page (same headline, same "132%"/"20,000+"/"4.9/5" stats, same five Key Takeaways headings and body text, formatted in Markdown syntax — `#`, `##`, `###`, `**bold**`, `---` rules). Supports the article's own claim that HTML and `.md` versions held "identical content."

## Pull notes — mechanical only

- Images read via the agent's Read tool directly on the saved JPG/JPEG files; all text legible at native resolution.
- Image 02's "Cited" column counts are a citation-tracking metric (OtterlyAI's own product feature, "Brand Report"), distinct from the article's own "AI bot visits" crawler-analytics metric described in its prose — flagged, not merged into one figure.
