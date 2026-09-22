# llms-txt.io blog — "Is Llms.txt Dead? The Current State of Adoption in 2025"

```yaml
source:          llms-txt.io (blog; a llms.txt-tooling site — vendor/tool operator, no individual byline found on the page)
url_or_doc_id:   https://llms-txt.io/blog/is-llms-txt-dead
published:       undated on the page itself; surfaced via Hacker News submission dated 2025-12-18 (HN Algolia), content references events through 2025-12 and forward-looking scenarios for "2026-2028"
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            6
tier_reason:     vendor blog, no byline, no disclosed method for its own headline claims ("over 784 websites," the Jan/Mar/Jun-2025 timeline); most figures are secondhand pointers to other sources rather than this site's own measurement. Individual cited figures carry their own tier where independently traceable — see pull notes
source_label:    vendor-reported
lane:            D
sub_market:      organic recommendation
engine:          n/a — cross-engine adoption commentary, with a secondhand Google (John Mueller) quote and secondhand references to unnamed AI systems generally
metric_kind:     none
supersedes:      none
captured:        full page (blog post body; comment/generator/sidebar chrome not captured)
```

## Verbatim

"A critical question looms: Is llms.txt actually being used by the AI systems it was designed for? The answer is complicated. While over 784 websites have implemented llms.txt files, creating a thriving grassroots [ecosystem]..."

"When Jeremy Howard introduced llms.txt in September 2024, the prob[lem it targeted was that] LLMs struggle with messy HTML... specifically designed for AI systems, complemented by llms-full.txt, which contains your complete documentation in a single consumable file."

"[Timeline of adoption, directory-tracked:] January 2025: 0 sites with llms.txt. March 2025: 0 sites with llms.txt. June 2025: 3 sites (0.3%) with llms.txt. Zero major consumer platforms like Google, Facebook, Amazon, or mainstream news sites have adopted it."

"But community-maintained directories tell a completely different story, as seen h[ere:] llmstxthub.com: Over 500 sites. directory.llmstxt.cloud: Approximately 684 implementations. NerdyData: 951 domains as of July 2025. An independent crawl of the Majestic Million dataset found just 15 sites in February 2025 growing to 105 sites by May—a 600% increase from a near-zero base. These seemingly contradict[ory statistics are both accurate—they're just measuring different] populations... Adoption is growing explosively in percentage terms but remains negligible in absolute numbers across the broader internet."

"Some companies report tangible benefits. Vercel claims 10% of their signups now come from ChatGPT, attributing this to [llms.txt / AI-referral factors — full attribution chain not further quoted]... Vercel's file resembled a 400,000-word novel."

"By mid-2025, community-maintained directories were listing over 784 websites with llms.txt implementations, with growth continuing steadily month over mo[nth]."

### "Google Says No (Very Publicly)"

"The most damaging development for llms.txt came in June 2025 when Google's John Mueller stated bluntly: "No AI system currently uses llms.txt. It's super-obvious if you look at your server logs. The consumer LLMs/chatbots will fetch your pages—for training and grounding, but none of them fetch the llms.txt file." Mueller went further, comparing llms.txt to the discredited keywords meta tag—a feature where site owners claimed what their content was about rather than letting systems determine it objectively. His argument cuts to a fundamental trust issue: if AI system[s could be told what content is about via a self-published file, that creates an incentive to game it, the same failure mode that killed the keywords meta tag — reasoning paraphrased/continued past this exact quote, not further quoted verbatim]."

"Multiple publishers with large domain portfolios have confirmed Mueller's observations. One hosting provider managing 20,000 domains reported that no mainstream AI agents or bots download llms.txt files—only niche crawlers like BuiltWith."

"Redocly tested extensively and found that unless you explicitly paste the llms.txt URL into an LLM, "it doesn't do anything... No model we tested spontaneously 'read' or respected llms.txt on its own.""

"Michael O'Neill at the University of Iowa checked too — same conclusion: don't lose sleep over llms.txt."

### Structured-data comparison (schema.org named as an alternative)

"A study by Data World found that LLMs grounded in knowledge graphs achieve 300% higher accuracy versus unstructured data. Schema.org enables creating these knowledge graphs through embedded JSON-LD in HTML, providing a single source of truth rather than requiring manual markdow[n duplication — sentence continuation not fully captured]."

### Scenarios for 2026-2028 (the post's own forward-looking, non-evidentiary framing — recorded as the source's own words, not as a forecast this repo endorses)

"Scenario 1: Gradual Official Adoption (40% probability) One major platform announces official support in 2026, others follow incrementally, and by 2027-2028 it becomes a standard similar to Open Graph Protocol's adoption curve... Scenario 2: Evolution and Absorption (30% probability) llms.txt merges with or is superseded by the Model Context Protocol... Scenario 3: Gradual Fade (20% probability) llms.txt remains a niche tool used manually by developers but never achieves crawler support from major platforms... Scenario 4: Fragmentation (10% probability) Different AI companies develop competing standards without universal adoption..."

## Pull notes — mechanical only

- Discovered via Hacker News Algolia search (`hn.algolia.com/api/v1/search?query=llms.txt+adoption`), then fetched directly with `curl`; static content, no login gate.
- **Per trust-rubric.md, this whole page is tier 6** (vendor blog, no disclosed author, and its own headline "784 websites" figure and the Jan/Mar/Jun-2025 timeline carry no linked source or stated method on this page) — filed as evidence about category noise and as a pointer to better-sourced claims, not as a number in its own right.
- Individual pointer figures, assessed separately:
  - **NerdyData ("951 domains as of July 2025")** — linked to `nerdydata.com` (a code/technology-search tool); not independently re-verified in this pull, recorded as a secondhand pointer, tier 5 at best (no date/method visible from the link alone as fetched).
  - **Majestic Million crawl ("15 sites in February 2025... 105 sites by May")** — described as "an independent crawl" but **no link or named author found on this page** for this specific figure. Per trust-rubric.md's discard rule ("'Studies show' with no link"), this specific figure is **not usable as a number** — recorded here only as what the blog post claims, not cited as evidence in the census adoption table.
  - **Vercel's own `llms-full.txt` ("resembled a 400,000-word novel")** — linked directly to `vercel.com/llms-full.txt`, i.e. verifiable as Vercel's own artefact; the separate "10% of signups from ChatGPT" claim is not sourced to a link on this page and is recorded as an unverified vendor claim, not a number.
  - **John Mueller quote ("No AI system currently uses llms.txt...")** — attributed to a named, real Google Search Advocate, but **no link to a primary source (post, video, or transcript) was found on this page**, and this pull did not independently locate the primary statement. Recorded as a **secondhand, unlinked quote** — corroborative in direction with this cluster's own tier-3 finding (`d-structured-google-ai-optimization-guide-2026-09-22.md`, "Google Search itself doesn't use them") and tier-4 measured finding (`d-structured-arxiv-borysenko-http-fingerprints-2026-09-22.md`, zero llms.txt requests observed), but **not itself promoted above tier 6** for lack of a traceable primary source.
  - **Redocly quote** — corroborated directly in `d-structured-redocly-overhyped-2026-09-22.md`, pulled separately from Redocly's own blog.
  - **"One hosting provider managing 20,000 domains"** — anonymous, unnamed, unlinked; not usable as a number per trust-rubric.md ("No n, no date window, or no method" — here no *named source* at all).
  - **Data World "300% higher accuracy" knowledge-graph study** — no link found on this page; not independently pulled or verified in this cluster, recorded as an unverified secondhand claim only.
- The four labelled "Scenarios" at the end are explicitly the blog's own speculative framing with assigned probabilities and no stated basis for those percentages — this is forecast-shaped content. Per `trust-rubric.md` ("A forecast presented as a measurement. When found, downgrade the whole author") this is additional reason the page sits at tier 6 overall; recorded here as the source's own words and excluded entirely from the census's adoption and measured-effect tables.
