# Technique census — P5-c3: comparison-page farming

```yaml
source:          compiled from the 7 raw pulls listed below (all pulled 2026-09-22) plus 5 pre-existing raw pulls read, not re-pulled
url_or_doc_id:   n/a — census of docs/raw/d-comparison-*-2026-09-22.md (7 files) plus b-openai-usage-policies-2026-09-22.md, b-anthropic-usage-policy-2026-09-22.md, d-review-google-spam-policies-2026-09-22.md, d-review-arxiv-geo-at-scale-2026-09-22.md, d-seeding-what-gets-cited-2026-09-22.md
published:       n/a — compiled 2026-09-22
pull_date:       2026-09-22
pull_method:     manual (compiled from this session's own raw pulls; no new fetch beyond what each cited file records)
pull_purpose:    evidence about a number
tier:            n/a — inherits the tier of each cited row, stated per row below
source_label:    n/a — mixed, per row
lane:            D
sub_market:      organic recommendation
engine:          n/a — cross-engine
metric_kind:     none
supersedes:      none
captured:        four question tables (mechanism, actors, measured-effect, engine statements), the H14 per-vertical density table, screened-out list, counts, pull-blockers/browser-backlog, unknowns. No text beyond what the cited raw files already carry
technique:       comparison-page farming
task:            P5-c3
hypotheses:      H5, H13, H14
```

## Headline finding, stated once

This cluster's searches — arXiv API (11 distinct queries), Semantic Scholar not attempted (429 seen elsewhere today per task brief; not queried this cluster to avoid it), ACL Anthology not separately queried, HN Algolia (9 distinct queries), and direct vendor/platform fetches — found **no academic paper that studies "X vs Y," "best X for Y," or "alternatives to" pages as a named, distinct content format**, and **no published case of a named brand running such pages at scale with a measured before-and-after AI-citation result**. The technique-specific literature is thinner than the adjacent techniques P5-c1 (corpus seeding) and P5-c2 (review/listicle manufacture) found in this same programme — this is recorded as the finding, not padded with off-topic items. What this cluster did find: one academic paper studying "competitor-aware" GEO in the abstract (not comparison pages specifically), one AI-generated-commercial-content detection paper evidencing production at scale, three vendor/tooling pages selling scaled content generation (two explicitly marketing AI-engine citation), and one specimen of the "best X for Y" format itself pulled as category-noise evidence.

## (1) Mechanism — how it works, per source

| Source | Raw path | Mechanism as the source describes it |
|---|---|---|
| Beyond the Vacuum (Sourirajan et al., Capital One AI Foundations) | `d-comparison-arxiv-beyond-vacuum-2026-09-22.md` | Formalizes GEO as a "competitor-aware strategy selection problem": as more competing documents get optimized, the optimal rewriting strategy for any one document changes — closest indexed academic framing to content competing head-to-head, though the paper does not isolate comparison-page structure itself |
| SlopShape (Madler, Sitefire) | `d-comparison-arxiv-slopshape-2026-09-22.md` | Documents the production mechanism's scale rather than the technique itself: 268 company domains' worth of commercial blog content matched against AI mirrors from five frontier models, evidencing that AI-generated commercial content at the volume comparison-page farming requires is now common enough to build a labeled corpus from |
| SeoBot (vendor) | `d-comparison-seobot-vendor-2026-09-22.md` | Automated generation of "listicles, how-to guides, roundups, and Q&A content" at ~3,000-4,000 words per article, with "Google Scraping & Research" as an input step; one sample article title is itself "vs"-formatted |
| Koala AI (vendor) | `d-comparison-koala-vendor-2026-09-22.md` | "SEO agent" that reads Search Console data for "content gaps" and drafts articles at volume via "KoalaWriter," marketed explicitly as built to "Get cited by Google AI Overviews, ChatGPT, and Perplexity" |
| onvoyage-ai/gtm-engineer-skills (open-source) | `d-comparison-gtm-engineer-skills-2026-09-22.md` | Open-source workflow skills including `build-resource-pages` and `write-seo-geo-content`, framed as producing "AI-citable" pages with "direct answers, clear structure, sources, and quotable passages" |
| Google spam policies — expired domain abuse, site reputation abuse | `d-comparison-google-spam-policies-2026-09-22.md` | Names the "rented domain" half of the technique directly: a purchased expired domain "repurposed... to manipulate search rankings," with "affiliate content" as a named illustrative example; separately states affiliate links are not, on their own, inconsistent with the site-reputation policy "when treated appropriately" |
| What Gets Cited (Vishwakarma et al., Sprinklr) — pre-existing, cited | `d-seeding-what-gets-cited-2026-09-22.md` | Controlled two-document RAG test: "topical relevance and list position are the biggest drivers of being cited first" — directly informs why comparison/listicle page structure (which source appears first in a ranked format) would matter to an AI answer's citation choice |
| GEO at Scale / Ranqo (Kumar) — pre-existing, cited | `d-review-arxiv-geo-at-scale-2026-09-22.md` | States the leverage point directly: "the highest-leverage page is the ranked 'best-of' listicle, the most-cited content format at about 21% of all citations" across a 100K+-response corpus |

## (2) Who is documented doing it — per source, actor type

| Source | Raw path | Actor type | What the source documents |
|---|---|---|---|
| SeoBot | `d-comparison-seobot-vendor-2026-09-22.md` | SaaS vendor | Sells automated listicle/roundup/how-to generation at volume ("200k articles," no independently verified n); no named customer's AI-citation result |
| Koala AI | `d-comparison-koala-vendor-2026-09-22.md` | SaaS vendor | Sells volume content generation explicitly marketed as built for citation by Google AI Overviews, ChatGPT, and Perplexity ("4M+ articles generated," "20,000+ paid creators"); no named customer's AI-citation result |
| onvoyage-ai (GitHub user) | `d-comparison-gtm-engineer-skills-2026-09-22.md` | Independent/open-source tooling author | Publishes reusable GEO-content-architecture workflows; no measured outcome documented |
| Capital One, AI Foundations (via Beyond the Vacuum's author affiliation) | `d-comparison-arxiv-beyond-vacuum-2026-09-22.md` | Named company's internal research team | Publishes competitor-aware GEO research; the paper itself does not test the company's own credit-card content, so this is affiliation evidence only, not a documented campaign |
| Sitefire, via Jochen Madler (SlopShape author) | `d-comparison-arxiv-slopshape-2026-09-22.md` | AI-search-visibility vendor (detection/monitoring side) | Studies detectability of AI-generated commercial content at scale; this is evidence of the defensive/detection side of the technique, not an actor running it |
| Zapier | `d-comparison-zapier-best-crm-noise-2026-09-22.md` | Named company, B2B SaaS | Runs a "best X app" listicle content operation on its own domain across product categories (per a screened, not independently verified, third-party characterization — see Unknowns); this one page discloses a hands-on editorial testing methodology, not an automated/template-stuffed production process, so it is not itself proof of "farming" in the pejorative sense |

No source in this cluster documents a named brand running true "X vs Y" or "alternatives to X" pages at scale **with a measured before-and-after AI-citation result** — the same absence pattern P5-c1 (corpus seeding) and P5-c2 (review/listicle manufacture) each recorded for their own techniques. This absence is recorded, not filled by inference.

## (3) Measured-effect table — before-and-after with prompt set, n, models, date window (H5 test)

| Source | Raw path | Models tested | Date window | Prompt set published | n | Effect verbatim | Replicated by | Tier |
|---|---|---|---|---|---|---|---|---|
| Beyond the Vacuum | `d-comparison-arxiv-beyond-vacuum-2026-09-22.md` | gpt-oss-120b, gpt-oss-20b, Llama-3.3-70B-Instruct, gemma-4-31B-it, gemma-4-E2B-it | Not stated beyond 2026-08-27 submission | No release found in abstract or full-text check | Not stated (benchmark sizes not disclosed in what this pull captured) | "We achieve state-of-the-art performance across several impression metrics over existing agentic and single-heuristic methods on both geo-bench and our synthetically augmented competitive dataset geo-bench_comp" — a benchmark-vs-baseline result, not a before/after test of one real page | Not stated | 5 |
| SlopShape | `d-comparison-arxiv-slopshape-2026-09-22.md` | Detector LLM (unnamed) over 214 structural features; AI-mirror generators: five unnamed frontier models | Human corpus pre-ChatGPT (before 2022-11-30); AI mirrors generated 2026, no narrower window stated | Code published (github.com/pulse-energy-eu/slopshape); dataset release not confirmed | 2,250 human posts / 268 companies vs. 11,250 AI mirrors | "detects AI posts from its 187 structural features alone at 98.0 macro-F1 on held-out companies, unchanged (98.1) when every AI post is reworded" — a detection-accuracy result, not an AI-answer citation-rate effect; out of scope for H5 on its own | Replicates StoryScope (Russell et al., 2026) on a different domain (fiction to commercial content) | 4 |
| What Gets Cited (pre-existing, cited) | `d-seeding-what-gets-cited-2026-09-22.md` | Gemini-2.5-Flash, GPT-5-Nano, GPT-5-Mini, GPT-5.2, Claude-3.5-Sonnet, Kimi-K2-Thinking | Not stated (paper dated 2026-05-25) | Abstract claims release; no URL found on inspection | 252,000 trials, 18 factors | "topical relevance and list position are the biggest drivers of being cited first" — a controlled two-document lab factor-attribution result, not a before/after test of a real comparison/listicle page | Not stated | 5 (vendor-authored, flagged) |
| GEO at Scale / Ranqo (pre-existing, cited) | `d-review-arxiv-geo-at-scale-2026-09-22.md` | ChatGPT, Claude, Perplexity, Gemini | March-May 2026 | Not confirmed in the prior pull | 100K+ prompt responses, 100+ brands | "the highest-leverage page is the ranked 'best-of' listicle, the most-cited content format at about 21% of all citations" — a cross-sectional snapshot of what already gets cited most, not a before/after test of manufacturing more listicles | Not stated | 5 (vendor-authored, Ranqo, flagged) |

**H5 read from this table, factually stated, not scored here (scoring is Pass 9's):** every row is either a controlled benchmark comparing methods against baselines, a content-detection accuracy result, or a cross-sectional citation-share snapshot. **None** is a true before-and-after test of the specific act of publishing a comparison/listicle/alternatives page on an owned or rented domain, with a baseline measured before that page existed and again after — the H5 bar this cluster's task instruction is checking for. This mirrors P5-c1's and P5-c2's own H5 reads for their techniques: `unresolved — checked arXiv (11 queries), HN Algolia (9 queries), Semantic Scholar (not queried, avoiding the 429 already seen today), engine/vendor pages, 2026-09-22`, not a kill — Pass 9 makes the cross-cluster call.

## (4) Engine statements — per engine, page and date, or unknown

| Engine | Statement | Page | Date | Raw path |
|---|---|---|---|---|
| Google | Names "scaled content abuse" (generic mass-page-generation prohibition, no comparison/listicle-specific wording — pre-existing pull), plus, newly captured this cluster, "expired domain abuse" (names "affiliate content" as an illustrative example of the abuse) and "site reputation abuse" (explicitly states affiliate links are **not**, on their own, inconsistent with the policy "when treated appropriately") | developers.google.com/search/docs/essentials/spam-policies | Last updated 2026-08-28 | `d-review-google-spam-policies-2026-09-22.md` (scaled content abuse, pre-existing); `d-comparison-google-spam-policies-2026-09-22.md` (expired domain / site reputation abuse, this cluster) |
| OpenAI | Usage Policies prohibit "deceit, fraud, scams, spam, or impersonation" generically under "Empower people." No passage names comparison pages, listicles, or scaled-content production as a distinct category (finding carried over from P5-c1's read of the same page) | openai.com/policies/usage-policies/ | Effective 2025-10-29 | `docs/raw/b-openai-usage-policies-2026-09-22.md` (pre-existing Pass 2 pull, read not re-pulled) |
| Anthropic | Usage Policy (AUP) prohibits "spammy behavior" via automation and "promot[ing] or facilitat[ing] the generation or distribution of spam," generically. No passage names comparison pages, listicles, or scaled-content production as a distinct category (finding carried over from P5-c1's read of the same page) | anthropic.com/legal/aup | Effective 2025-09-15 | `docs/raw/b-anthropic-usage-policy-2026-09-22.md` (pre-existing Pass 2 pull, read not re-pulled) |
| Perplexity | `unknown — checked perplexity.ai/hub/legal/publisher-guidelines (403, needs browser extension) and perplexity.ai/hub (403) 2026-09-22`. Routed to `docs/sources/shortlist.md` P5-c7 (dedicated engine-countermeasure cluster, queued) — same routing P5-c1 and P5-c2 used | — | — | — |
| Microsoft Copilot / Bing | `unknown — checked bing.com/webmasters/help/webmaster-guidelines-30fba23a (returns a page title only, JavaScript-rendered, empty to plain fetch) and learn.microsoft.com/en-us/bingwebmaster/webmaster-guidelines (404) 2026-09-22`. Routed to P5-c7 | — | — | — |
| Amazon (Rufus / Alexa for Shopping) | `unknown — checked amazon.com/gp/help/customer/display.html?nodeId=GLHXEX85MENUE4XF (503) and advertising.amazon.com/library/guides/what-is-amazon-dsp (404, wrong path) 2026-09-22`. Routed to P5-c7 | — | — | — |

**H13 read from this table, factually stated:** of the three engines this cluster reached (Google, OpenAI, Anthropic), only Google names anything specific to the rented/expired-domain half of this technique ("expired domain abuse," naming "affiliate content" as an example) and to the owned-third-party-content half ("site reputation abuse"), and explicitly carves out ordinary affiliate linking as not itself a violation. Neither Google clause names "comparison pages," "vs" pages, or "best X" pages as a distinct category. OpenAI and Anthropic's policies are generic anti-spam language with no technique-specific wording, matching P5-c1's finding on the same two pages. Perplexity, Microsoft Copilot, and Amazon were not reachable by this fetch-only cluster (browser-extension-gated or 403/404/503) and are recorded as `unknown — checked`, not as an absence, per the same three-engine gap P5-c1 and P5-c2 both recorded and routed to P5-c7.

## Per-vertical density — for H14

| Vertical | Items naming it | Raw paths / basis |
|---|---|---|
| Skincare and beauty | 0 | No item in this cluster's 7 new pulls or 5 cited pulls names this vertical. Two dedicated arXiv searches this cluster ran (`abs:"skincare" OR abs:"cosmetics" AND abs:"generative"`, and a "best serum skincare affiliate SEO" HN search) each returned 0 relevant hits (10 off-topic arXiv hits, 0 HN hits) |
| B2B SaaS | 1 (specimen) + 2 adjacent, screened not pulled | `d-comparison-zapier-best-crm-noise-2026-09-22.md` (tier-7 specimen, CRM named directly); adjacent, screened-out-not-pulled: `guptadeepak.com` "Programmatic SEO as Early-Growth Infrastructure for B2B SaaS Startups" and `gracker.ai` "Programmatic SEO for B2B SaaS" — both name B2B SaaS but neither names comparison/alternatives pages specifically nor any AI-citation result, so neither cleared this cluster's bar for a full raw pull |
| High-CPA regulated (cards, insurance, supplements, loans, personal injury) | 1, adjacent — author affiliation only, not tested content | `d-comparison-arxiv-beyond-vacuum-2026-09-22.md` — all six authors affiliated with Capital One (credit cards), but the paper's own tested content (geo-bench, geo-bench_comp, E-Commerce, Researchy-GEO) does not itself carry a credit-card, insurance, or supplements label. Recorded per the cell-attribution rule: affiliation is source-stated, tested-vertical is not. Two dedicated searches for pulled specimens in this vertical (`forbes.com/advisor/credit-cards/best-credit-cards/`, `investopedia.com/best-credit-cards-4842373`) were both blocked (403, outright block) — see Pull-blockers |
| None named | 6 | `d-comparison-arxiv-slopshape-2026-09-22.md`, `d-comparison-seobot-vendor-2026-09-22.md`, `d-comparison-koala-vendor-2026-09-22.md`, `d-comparison-gtm-engineer-skills-2026-09-22.md`, `d-comparison-google-spam-policies-2026-09-22.md` (both the new pull and the pre-existing scaled-content-abuse pull), `d-seeding-what-gets-cited-2026-09-22.md` (pre-existing, cited) |

**H14 read from this table, factually stated, not scored here:** at the screen effort this cluster actually ran (dedicated searches attempted for all three verticals, not just reported for two), B2B SaaS is the only vertical with a directly-pulled specimen (1, tier 7), and high-CPA regulated has one adjacent, affiliation-only data point rather than a tested-content match; skincare and beauty returned zero at every route tried, including two dedicated searches. This does not show the regulated vertical exceeding the anchor vertical in cleared, on-topic items — it shows B2B SaaS ahead of both on this cluster's own count, which cuts against H14's directional claim rather than confirming it. Recorded as this cluster's own data point only; Pass 9 rolls it up against P5-c1's and P5-c2's density tables, which found different, also-thin patterns.

## Screened-out — candidates examined, not pulled

**arXiv, 11 distinct queries run, none returning a squarely on-topic new paper beyond the two pulled (Beyond the Vacuum, SlopShape):**

- `abs:"comparison page" AND abs:"large language model"` — 0 results.
- `abs:"programmatic SEO"` — 0 results.
- `abs:"buying guide" OR abs:"best-of" AND abs:"language model"` — 20 results, only one on-topic-adjacent (2212.10770, ImPaKT, a 2022 knowledge-base-extraction dataset paper using shopping buying-guide text; not about AI-citation or scaled production; screened out).
- `abs:"affiliate" AND abs:"citation" AND abs:"generative"` — 15 results, all off-topic (bibliometrics, academic self-citation, unrelated domains); closest, 2601.17109 "Authority Signals in AI Cited Health Sources," examined separately below and screened out.
- `abs:"vs" AND abs:"purchase intent" AND abs:"retrieval"` — 0 results.
- `abs:"product comparison" AND abs:"large language model"` — 6 results, all product-attribute-extraction papers (e.g. ExtractGPT 2310.12537, WDC-PAVE 2403.02130) — extraction/normalization research, not comparison-page production or citation; screened out.
- `abs:"content farm" AND abs:"search"` — 0 results.
- `abs:"doorway pages" OR abs:"spam pages" OR abs:"SEO spam"` — 6 results, all pre-2017 classical web-spam-detection papers (link/content spam, PageRank-era), pre-dating generative-engine citation entirely; screened out as off-era.
- `abs:"scaled content" OR abs:"mass-produced" AND abs:"search engine"` — 3 results, all off-topic (recommendation-system retrieval, ensemble-LLM content-analysis method, domain-credibility-prediction method); screened out.
- `abs:"competitor comparison" AND abs:"SEO"` — 0 results.
- Re-checked six already-screened-off-cluster GEO papers from P5-c1's own screen (2609.02316, 2608.11390, 2604.19113, 2604.19516, 2609.07559, 2609.06811) plus 2603.29979 for this cluster's narrower question ("does the paper study comparison/vs/best-X/alternatives pages as a distinct format") — confirmed none does; see the "Relevant Finding: No" table returned by this cluster's own targeted re-query.

**One paper examined and screened out on inspection:** arXiv 2601.17109, "Authority Signals in AI Cited Health Sources" (7 US-university-affiliated authors, submitted 2026-01-23) — studies ChatGPT's health-source citation authority signals (100 health questions, ">75% of cited sources from established institutional sources"), a real vertical-adjacent finding for health/supplements, but does not name or study comparison pages, listicles, buying guides, or affiliate content as such. Not pulled as a raw file; recorded here as the closest near-miss for the high-CPA regulated vertical this cluster's arXiv searches found.

**HN Algolia, 9 distinct queries run:**

- `programmatic SEO AI citation` — 0 hits.
- `comparison pages ChatGPT cited` — 4 hits, 2 tangential (Sitefire launch post — led to the SlopShape pull; a 2022 unrelated ChatGPT-search comment), 2 off-topic (arithmetic benchmark discussion); none on comparison pages specifically.
- `programmatic SEO` — 20 hits, listed and screened individually below.
- `"best X for Y" GEO pages AI search` — 0 hits.
- `"vs" page template AI search citation` — 0 hits.
- `comparison page generator SEO` — 12 hits, 1 tangential (an AI-essay-writer listicle-generation tool, off-target), rest off-topic (hardware, games, storage systems, luxury goods).
- `credit card comparison site SEO affiliate` — 0 hits.
- `best serum skincare affiliate SEO` — 0 hits.
- `insurance comparison page programmatic` — 0 hits.
- `"alternatives to" page SaaS AI search GEO` — 0 hits.

Of the 20 `programmatic SEO` hits, pulled: SeoBot (via its own site, not the HN post) and the onvoyage-ai GTM-engineer-skills repo. Screened, not pulled (thin, off-technique, or no AI-citation/comparison-page claim): Zapier's own programmatic-SEO blog post (2023-07-04, general explainer, not itself a specimen — the specimen pulled is a Zapier output page, found via a different route); `allisonseboldt.com` experiment write-up (2021, pre-dates generative-engine citation as a concern); `withdaydream.com` "Almost all SEO will become programmatic SEO" and its companion product page; `coinerella.com` "Generating 100k+ Pages That Rank" (wiki-style car-reference pages, not comparison pages, no AI-citation claim — fetched and read, not filed as a raw pull for this reason); Ask HN "go-to strategy for programmatic SEO in 2025"; "Programmatic SEO is just noise based on my last 5 years experience" (HN discussion, negative practitioner sentiment, no n); `guptadeepak.com` and `blog.gracker.ai`/`gracker.ai` B2B SaaS posts (fetched and read; see H14 table — named the vertical but not the technique specifically enough to clear the bar); `arnjen.com` "225 pages, Google indexed 18%" (fetched and read — earnings-content pages, not comparison pages; no AI-citation claim); "How I Made $10M Using Programmatic SEO" (YouTube video, not text-fetchable within this task's method); `github.com/agamm/pseo-next` Next.js template (no claims, tooling existence only); `commenze.com`, `yilore.app`, `sammyseo.com`, `thebuilderjr.substack.com`, `everlist.dev` (all thin vendor/practitioner pages, no comparison-page or AI-citation claim in the HN listing itself, not individually fetched).

## Counts

| Count | Value |
|---|---|
| Raw pulls landed this cluster | 7 (`d-comparison-*-2026-09-22.md`) |
| Pre-existing raw pulls read, cited, not re-pulled | 5 (`b-openai-usage-policies-2026-09-22.md`, `b-anthropic-usage-policy-2026-09-22.md`, `d-review-google-spam-policies-2026-09-22.md`, `d-review-arxiv-geo-at-scale-2026-09-22.md`, `d-seeding-what-gets-cited-2026-09-22.md`) |
| arXiv queries run, distinct | 11, plus 1 targeted re-check of 7 previously-screened GEO papers from P5-c1 |
| HN Algolia queries run, distinct | 9 |
| Vendor/platform pages fetched (pulled or attempted) | 14 (7 landed as raw files; 7 blocked or off-target — see Pull-blockers and screened-out) |
| Items with a measured effect (any kind) | 4 of 7 new pulls (Beyond the Vacuum, SlopShape) plus 2 of 5 cited pulls (What Gets Cited, Ranqo) — 4 distinct measured-effect rows total in table (3) above; the Google-policy and Zapier-specimen pulls carry no measurement |
| Items with a true before-and-after design on a real comparison/listicle page | 0 — same finding as P5-c1 and P5-c2 for their own techniques |
| Highest tier reached | 4 (SlopShape — preprint with code) |
| Vendor-authored items (flagged) | 4 — SeoBot, Koala AI (both existence-tier vendor pages, tier 6), What Gets Cited (Sprinklr, tier 5, cited), Ranqo GEO at Scale (tier 5, cited) |
| Engines with a stated clause bearing on this technique | 1 of 6 (Google: expired domain abuse, site reputation abuse, scaled content abuse) — OpenAI and Anthropic checked, generic-only; Perplexity, Microsoft, Amazon not reached, routed to P5-c7 |
| Tier-7 category-noise specimens pulled | 1 (`d-comparison-zapier-best-crm-noise-2026-09-22.md`), against the task's "one or two" allowance — a second attempt (high-CPA regulated) was blocked, not substituted |

## Unknowns

- `unknown — checked perplexity.ai/hub/legal/publisher-guidelines and perplexity.ai/hub 2026-09-22`, both 403 to plain fetch, browser-extension-gated. Routed to P5-c7.
- `unknown — checked bing.com/webmasters/help/webmaster-guidelines-30fba23a (JavaScript-rendered, empty to plain fetch) and learn.microsoft.com/en-us/bingwebmaster/webmaster-guidelines (404) 2026-09-22`. Routed to P5-c7.
- `unknown — checked amazon.com/gp/help/customer/display.html?nodeId=GLHXEX85MENUE4XF (503) and advertising.amazon.com/library/guides/what-is-amazon-dsp (404) 2026-09-22`. Routed to P5-c7.
- `unknown` whether any named brand has run and published a comparison/alternatives-page campaign with a measured before-and-after AI-citation result — no such case surfaced in this cluster's 20 arXiv-adjacent papers examined, 20+ HN hits examined, and 14 vendor/platform pages fetched or attempted; recorded as an absence with the screened counts above, not asserted as a category-wide absence.
- `unknown` whether Zapier's "best X app" content operation is produced at the scale a companion practitioner source (guptadeepak.com) characterizes it as ("millions of long-tail keywords") — this pull independently verified only the one page fetched, which discloses a hands-on editorial testing methodology, not an automated production process. `unknown — checked one Zapier page and one third-party characterization only, 2026-09-22`.
- `unknown` whether G2's and Capterra's own programmatically-generated "Compare" and "Alternatives" pages (the single clearest real-world specimen of this technique this researcher is aware exists as a channel, per `docs/sources/channels.md` C36/C37) show any measured AI-citation effect — both domains returned 403 to plain fetch and are browser-extension-gated, which this fetch-only task cannot use. Recorded as the largest gap this cluster leaves open, not filled by inference.

## Pull-blockers / browser backlog encountered this cluster

Fetch-only constraint (no Chrome extension, no Playwright per this task's instructions) — the following are handed to the browser backlog rather than pulled:

- `g2.com/compare/*` — G2's own templated "X vs Y" comparison pages (403 to plain fetch; the single most directly on-technique real-world specimen this cluster identified and could not reach).
- `capterra.com/alternatives/*` — Capterra's templated "alternatives to X" pages (404 on the specific path tried; general domain is 403→ext per `channels.md` C37).
- `saashub.com/compare/*` — a third programmatic-comparison directory (403).
- `alternativeto.net/software/*` — community-driven "alternatives" directory (404 on the path tried).
- `forbes.com/advisor/credit-cards/best-credit-cards/` — high-CPA-regulated-vertical "best X" specimen attempt (403).
- `investopedia.com/best-credit-cards-4842373` — same vertical, second attempt (outright domain block, not extension-gated: "Claude Code is unable to fetch from www.investopedia.com").
- `perplexity.ai/hub/legal/publisher-guidelines`, `perplexity.ai/hub` — engine statement, Q4 (403).
- `bing.com/webmasters/help/webmaster-guidelines-30fba23a` — engine statement, Q4 (JavaScript-rendered, empty to plain fetch).
- `amazon.com` review/content policy page — engine statement, Q4 (503).
- `html.duckduckgo.com/html/` and `lite.duckduckgo.com/lite/` — both returned 403 to `WebFetch` on both attempts made this cluster; not retried further per the task's "use sparingly" instruction on this surface.
- Semantic Scholar API — not queried this cluster at all, to avoid repeating the 429 rate-limit this task's brief states was "seen today."

## Caveats

- This cluster's four-question tables answer Pass 5's questions for the "comparison-page farming" technique only; they do not score H5, H13, or H14 — scoring against `docs/method/hypotheses.md` decision conditions is Pass 9's task, against this file, its 7 new raw pulls, and the 5 cited pre-existing pulls.
- The single largest evidentiary gap this cluster leaves is G2's and Capterra's own comparison/alternatives pages — programmatic, at-scale, on owned domains, matching the technique definition closely — both blocked to fetch and requiring the browser extension this task could not use. A browser-capable pass should prioritize these two before any other item on the backlog list above.
- Every vendor page pulled (SeoBot, Koala AI) is tier 6: existence and claimed-capability evidence only, never cited here as proof any AI-citation outcome occurred.
- Both academic pulls (Beyond the Vacuum, SlopShape) are single preprints, tier 4-5, not independently replicated within this cluster's own pulls, per the academic tier table in `docs/method/trust-rubric.md`. Beyond the Vacuum is additionally bias-flagged for its authors' employer (Capital One, a credit-card issuer) even though the paper does not test the company's own content.
- No test was run against any third-party production answer surface, brand, or engine by this task, per the Lane D hard constraint in `docs/method/plan.md`. No page was created and no engine was queried.
- Oldest pull depended on: 2026-09-22 (all 7 new raw files in this cluster, plus all 5 cited pre-existing files, were pulled or landed on this date).
