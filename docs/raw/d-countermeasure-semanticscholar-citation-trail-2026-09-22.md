# Semantic Scholar Graph API — citation trail for the seed defense paper (arXiv:2605.21948)

```yaml
source:          Semantic Scholar (Allen Institute for AI), Graph API
url_or_doc_id:   https://api.semanticscholar.org/graph/v1/paper/arXiv:2605.21948?fields=title,year,venue,citationCount,references.title,references.externalIds,citations.title,citations.externalIds
published:       n/a — live API query, not a dated publication
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default per trust-rubric.md channel C49 (Semantic Scholar) — "citation graph, replication trails, venue metadata"; API response itself, not a paper
source_label:    analyst-derived
lane:            D
sub_market:      organic recommendation
engine:          n/a
metric_kind:     none
supersedes:      none
captured:        API JSON response as summarized by the fetch tool: paper metadata, full citing-paper list (3), and a selection of referenced papers (of 25 total) with arXiv external IDs
technique:       defense literature — citation-trail discovery method for the seed paper this task was assigned, per task instructions ("its citation trail — Semantic Scholar API; 429 seen today — back off")
models_tested:   n/a
date_window:     n/a
measured_effect: n/a
vertical:        n/a
```

## Verbatim

Query result, as returned by the fetch tool:

Paper: "SCI-Defense: Defending Manipulation Attacks from Generative Engine Optimization," Year 2026, Venue "arXiv.org," Citation Count 3.

Citing papers (3 of 3 returned):

1. "Evaluating Deep-Search Agents under Hierarchical Web Evidence Poisoning" (arXiv:2609.06027) — pulled as `docs/raw/d-countermeasure-hae-geo-2026-09-22.md`
2. "When Optimization Becomes Manipulation: Defending Generative Search against Malicious Generative Engine Optimization" (arXiv:2609.02964) — pulled as `docs/raw/d-countermeasure-geo-defender-2026-09-22.md`
3. "SIREN (Luring LLMs onto the Rocks): PAIR-Driven Preference Manipulation in Web-RAG Recommenders" (arXiv:2607.21951) — screened, not pulled as a defense-table row (see Pull notes)

Referenced papers (selection of the 25 total returned, with arXiv IDs, as returned by the fetch tool):

"DataSentinel: A Game-Theoretic Detection of Prompt Injection Attacks" (2504.11358); "Adversarial Search Engine Optimization for Large Language Models" (2406.18382); "JailbreakZoo: Survey, Landscapes, and Horizons in Jailbreaking Large Language and Vision-Language Models" (2407.01599); "Ranking Manipulation for Conversational Search Engines" (2406.03589); "GEO: Generative Engine Optimization" (2311.09735); "Poisoning Retrieval Corpora by Injecting Adversarial Passages" (2310.19156); "A Watermark for Large Language Models" (2301.10226); "Ignore Previous Prompt: Attack Techniques For Language Models" (2211.09527).

## Pull notes — mechanical only

- Fetched via WebFetch against the Semantic Scholar Graph API endpoint directly (not the web UI), 200 — **no 429 was encountered on this call**, contrary to the task briefing's warning ("429 seen today — back off") and contrary to this repo's P5-c2 cluster's own experience the same day (`docs/raw/d-technique-census-c2-2026-09-22.md` Pull-blockers: "Semantic Scholar API... returned HTTP 429 on both attempts across the session"). Recorded as a single successful observation, not a contradiction of that earlier finding — rate limits are commonly time-windowed and per-caller.
- Both citing papers with a code repository were pulled as full raw files (GEO Defender, HAE-GEO). The third citing paper, SIREN (arXiv:2607.21951), was screened by abstract only and **not** pulled as a defense-table row: its own abstract states "This paper describes only an attack; it does not measure defensive countermeasures" — it tests rank manipulation against "two production Claude models" using "Anthropic's web tools," reaching rank 1 in 62 of 124 trials (mean reproduction success rate 0.805 in fresh sessions). Recorded here as a screened-out item, not filed as its own raw pull, per this task's remit being defense literature specifically.
- Only 8 of 25 referenced papers were returned in the API response's visible selection (the tool's own summarization, not a field limit set by this task); the remaining ~17 references were not itemized by the tool and are not claimed here.
- This file itself constitutes the "citation trail" deliverable named in the task briefing; the census (`d-technique-census-c7-2026-09-22.md`) cites it directly rather than duplicating its content.
