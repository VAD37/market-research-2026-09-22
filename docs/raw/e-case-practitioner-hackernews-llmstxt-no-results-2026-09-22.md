# Hacker News (keploy) — "Is anyone seeing results from LLMSTXT files, or is it just hype?"

```yaml
source:          keploy, Hacker News post
url_or_doc_id:   https://news.ycombinator.com/item?id=44136897 (HN Algolia API: https://hn.algolia.com/api/v1/items/44136897)
published:       2025-05-30
pull_date:       2026-09-22
pull_method:     fetch (HN Algolia API, raw JSON, via curl)
pull_purpose:    evidence about category noise
tier:            6
tier_reason:     No n, no date window, no method beyond "I made one personally" — meets trust-rubric.md's discard-on-sight criterion ("No n, no date window, or no method") almost exactly. Kept at tier 6 and filed only as category-noise / negative-result evidence per pull_purpose and the task's explicit instruction to include thin negative results as cases, never as a number.
source_label:    company-stated
lane:            A
sub_market:      organic recommendation
engine:          ChatGPT, Perplexity, Claude — named as the crawlers targeted, no model version stated, no engine-specific result given
metric_kind:     none
supersedes:      none
captured:        full page (post text); 0 comments returned by the API
vertical:        none named
evidence_grade:  Below the evidence bar on every item except intervention. Bar items present: intervention named (created an llms.txt file). Bar items missing: no brand/profile (fully anonymous, "I made one personally"); no engine-specific result; no date window; no baseline; no sample size; no named measurer beyond the anonymous author. This is the thinnest possible form of the negative-result case the task explicitly asks to include ("tested GEO for 3 months, nothing moved") — here compressed to a single unquantified sentence with no time period stated at all.
artefacts_published: none
direction:       negative ("I made one personally... but got no results")
```

## Verbatim

**Post title:** Is anyone seeing results from LLMSTXT files, or is it just hype?
**Author:** keploy
**Points:** 1
**Created:** 2025-05-30T14:59:36.000Z

I've been seeing a lot of chatter about using llmstxt files (the so-called "SEO cheat code" for LLMs) to get better backlinks, visibility, and even organic traffic.

The theory is that these files make your site friendlier to LLM crawlers like ChatGPT, Perplexity, and Claude—kind of like an XML sitemap for generative AI models. But I haven't come across any hard data or case studies showing that this actually works.

Is there anyone here who has implemented an llmstxt file and can share real results? Like:

Any noticeable change in traffic?

LLM-generated summaries including your content?

Better placement in AI search tools?

Or is this just another hype train with no real engine behind it?

Curious to hear from the community. Let's separate signal from noise!

I made one personally to extract unlimited urls but got no results

## Pull notes — mechanical only

- Retrieved via `https://hn.algolia.com/api/v1/items/44136897` (Hacker News Algolia API), raw JSON, decoded HTML entities (`&#x27;`, `&quot;`) and stripped `<p>` paragraph tags manually to reconstruct plain-text paragraph breaks.
- `children` array was empty (0 comments) — confirmed no replies exist for this item as of the pull.
- The final sentence ("I made one personally... but got no results") is the entirety of the author's own negative result; no further detail (which pages, what traffic metric, what time period) is given anywhere in the post.
