# Hacker News (madanparas) — "Reddit and Perplexity got us leads faster than Google ever did"

```yaml
source:          madanparas, Hacker News post
url_or_doc_id:   https://news.ycombinator.com/item?id=44737677 (HN Algolia API: https://hn.algolia.com/api/v1/items/44737677)
published:       2025-07-30
pull_date:       2026-09-22
pull_method:     fetch (HN Algolia API, raw JSON, via curl)
pull_purpose:    evidence about a number
tier:            6
tier_reason:     Self-authored practitioner post promoting the author's own tool (FireGEO, named in body). No n stated for most figures ("8 early-stage AI startups" is the only sample-size figure given); no absolute date window (relative phrasing only: "3 days later", "in last 30 days"); no named brand/site; no third-party measurement. Vendor-measuring-what-it-sells pattern per trust-rubric.md discard-on-sight list, kept at tier 6 (not discarded) because it also functions as community-attention evidence for S5 and is explicitly in scope as a Pass 4 negative/thin-case candidate.
source_label:    vendor-reported
lane:            F
sub_market:      organic recommendation
engine:          ChatGPT (with Browsing), Perplexity — no model version stated
metric_kind:     traffic
supersedes:      none
captured:        full page (post text) plus the one top-level comment HN Algolia returned
vertical:        none named (aggregated across "8 early-stage AI startups, Series A or earlier" — no named vertical, no named brand)
evidence_grade:  Fools gold. Bar items present: intervention (switch to "LLM-first" content strategy, Reddit posting, Q&A blocks, ai-sitemap.xml — all named); some sample size ("8 early-stage AI startups"). Bar items missing: no brand or credibly specified single profile (aggregated across 8 unnamed companies); no absolute date window (only relative: "3 days later", "in last 30 days", "~94 days" for the Google baseline); no baseline stated with a date; who measured is the author, who is also the operator of the product being promoted (FireGEO) — not paid-by-outcome disclosure, but a direct commercial conflict of interest on the same claims.
artefacts_published: none — no prompt set, no dataset, no linked spreadsheet or export
direction:       positive (as claimed by author; unverified)
```

## Verbatim

**Post title:** Reddit and Perplexity got us leads faster than Google ever did
**Author:** madanparas
**Points:** 8
**Created:** 2025-07-30T18:15:35.000Z

We used to play the SEO game.

Write blog
Wait 3 months
Maybe rank
Maybe convert

What actually happened at 8 early-stage AI startups (Series A or earlier):

-Google Page 1 took ~94 days
- Organic CTR: 2.6%
- First qualified lead: 6–8 weeks

So we ditched the playbook.

We asked one question:

How fast can we show up when someone asks ChatGPT or Perplexity what tool to use?

Turns out… faster than Google.

And yeah, it brought pipeline.

What changed when we went LLM-first:

- Perplexity picked up our content in under 48 hours
- ChatGPT (with Browsing) indexed feature pages in 3 days
- 18.2% of sessions now come from LLM-originated paths
- Those leads convert 2.4x better than blog traffic

Then Reddit unlocked another level.

We posted no-link, technical breakdowns here.

One of them (about how we automated an AI agent pipeline) got quoted by Perplexity in:

- "UX AI Agent"
- "Best Firecrawl alternatives"
- "How to track LLM bots"

No push. No SEO. Just built in public.

3 days later:

- 9 Perplexity query quotes
- 2 inbound leads mentioned us directly

Reddit is training data goldmine for LLMs.

Here's what worked for us:

1. Add Q&A blocks to product pages (all <40 words)

Example:
Q: How does FireGEO detect ClaudeBot?
A: It fingerprints known Anthropic headers and reverse-DNS matches IP blocks like 2600:1f18::/32

- Indexed by Perplexity in <48 hours
- 11 bot hits in 5 days
- 1 lead → trial signup in <1 week

2. Build an ai-sitemap.xml

Only high-signal pages:
- API docs
- Feature comparisons
- Pricing breakdowns
- Tech specs

Crawl rate = 2.3x higher than default sitemap.

GPTBot, ClaudeBot, and PerplexityBot show up daily in logs.

3. Treat Reddit as an input layer

We post raw content here before it hits our blog.
In last 30 days:

- ~30,000 views across Reddit
- 9 quotes in Perplexity answers
- 2 leads directly from those mentions

If you're shipping something real, try this:

- Install FireGEO or track LLM bots via reverse DNS + ASN logs
- Create llm.txt for structured answers
- Tag LLM traffic with UTMs and route to CRM

Curious to know what's working for you around LLM visibility?

Any tactics or insights others here are seeing?

---

### Top-level comment

**romanhn:**
Please keep broetry[0] on LinkedIn, let's try to stick to human-like communication here.
[0] https://www.fenwick.media/all-blog-posts/mastery/broetry-dea...

## Pull notes — mechanical only

- Retrieved via `https://hn.algolia.com/api/v1/items/44737677` (Hacker News Algolia API), which returns the post's full submitted text (HN "Ask/Show/text" posts store the full text; this was a self-text post with no external URL) plus its full comment tree.
- Only one top-level comment existed at pull time (0 points shown by Algolia for this item; HN's own site shows a live point/comment count that may have since changed — not re-checked against the live page).
- "FireGEO" is confirmed as the author's own product from context ("Install FireGEO or track LLM bots"); no separate landing page was pulled to independently verify FireGEO is madanparas's product — inferred from the post's first-person framing ("what worked for us") alongside the install recommendation.
- No linked dataset, spreadsheet, or prompt set found in the post body or the one comment.
