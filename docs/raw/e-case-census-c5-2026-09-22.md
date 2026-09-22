# Census — Pass 4, cluster P4-c5: practitioner write-ups

```yaml
source:          this repository's own Pass 4 cluster P4-c5 intake process
url_or_doc_id:   n/a — census/summary of the cluster's own pulls
published:       2026-09-22
pull_date:       2026-09-22
pull_method:     manual (compiled from this session's own queries and pulls)
pull_purpose:    evidence about a number
tier:            n/a — this file is a summary/index over the raw pulls it cites, not itself a source pull
tier_reason:     n/a
source_label:    n/a
lane:            A, F
sub_market:      organic recommendation, paid placement
engine:          ChatGPT, Perplexity, Google AI Overviews — as named per candidate below
metric_kind:     none
supersedes:      none
captured:        n/a
```

No interpretation below beyond what the task requires (grading, tagging, counting). Per root `CLAUDE.md`: absolute dates, conflicting figures kept side by side, `unknown — checked <channel> <date>` recorded where nothing was found.

## Blocker recorded first — Reddit access

**Reddit (reddit.com, old.reddit.com, api.reddit.com — all subdomains) was unreachable by every method available this session, checked 2026-09-22:**

1. `mcp__MCP_DOCKER__fetch` (plain HTTP fetch): blocked by `robots.txt` (`Disallow: /` for the tool's own user-agent) on both `www.reddit.com` and `old.reddit.com`.
2. `WebFetch` (built-in): returned `Claude Code is unable to fetch from old.reddit.com` — a hardcoded restriction, not a network error.
3. `claude-in-chrome` (browser extension, connected this session): `navigate` to `old.reddit.com` and `www.reddit.com` both returned "This site is not allowed due to safety restrictions" — an extension-level domain block, not a login or network issue.
4. `mcp__MCP_DOCKER` Playwright browser: `old.reddit.com` (search and individual thread URLs) redirected to `old.reddit.com/login/?reason=lor2...` (soft login wall). `www.reddit.com`, `www.reddit.com/r/SEO/comments/1fk6eq0.json`, and `api.reddit.com/r/SEO/comments/1fk6eq0` all returned Reddit's own "You've been blocked by network security" interstitial with a "File a ticket" link — a hard network-level block, consistent with the shared-session-IP aggregate-traffic pattern already recorded elsewhere in `docs/method/STATE.md` for this date (Perplexity and Google AI Mode panel blocks, same 2026-09-22 session).
5. `r.jina.ai` reader proxy (`https://r.jina.ai/https://www.reddit.com/...`), tried as a fallback text-extraction route: `mcp__MCP_DOCKER__fetch` was itself refused by jina.ai's own `robots.txt` (it allows only a named allowlist of user-agents — `Claude-User`, `ChatGPT-User`, etc. — that this tool does not present as). `WebFetch` reached jina.ai but the underlying Reddit fetch inside it still returned a 403.
6. DuckDuckGo HTML search-result **snippets** (via `html.duckduckgo.com/html/`, per this task's instruction to use DDG "sparingly") were reachable and used throughout for *discovery* (titles, URLs, one- or two-sentence snippets), but never gave enough text to satisfy the raw-pull template's "Verbatim" requirement for a Reddit thread's post body or comments — so no Reddit thread could be pulled to `docs/raw/` as a fully verbatim file this session, only found and logged as an unopened candidate.

**Consequence:** no `docs/raw/` file with `source:` a Reddit thread was produced this cluster. All 10 write-ups pulled instead come from Hacker News (fully accessible via `hn.algolia.com/api/v1/`, no blocker) and from personal/professional blogs (gauravtiwari.org, veonib.com, LinkedIn articles, GitHub) discovered via DuckDuckGo HTML search, per the shortlist.md "floor not ceiling" substitution rule — the substitution is recorded here rather than silently. Where a Reddit thread was found by title/snippet only and never opened, it is logged in the "Reddit threads found but not pulled" table below for S5's thread-count purpose and as an unresolved lead for a future pull with Reddit access.

## Discovery log

### Hacker News Algolia queries (`hn.algolia.com/api/v1/search`), all run 2026-09-22

| Query | Hits reviewed | Notable results |
|---|---|---|
| `generative engine optimization` (tags=story) | 20 | a16z GEO explainer, GEO tool launches, `arxiv.org/abs/2509.08919`, "Ask HN: How does ChatGPT decide..." (46907123) |
| `AI visibility ChatGPT traffic` | 20 | Sitefire launch (47457472), "Reddit and Perplexity got us leads" (44737677) |
| `AEO answer engine optimization` | 11 | "After writing over 10k+ blogs... AEO" (43751004, screened — thin, no n) |
| `ChatGPT referral traffic case study` | 1 | Sitefire launch (47457472) again |
| `llms.txt results` | 20 | Mostly unrelated Show HN posts; no case-study-shaped result |
| `GEO test results months` | 10 | No relevant hits — all off-topic (Gitea, YouTube growth, herd immunity) |
| `brand mentions ChatGPT tracked dataset` | 1 | `[dead]` post, not usable |
| `AI search visibility experiment prompt set` | 1 | Unrelated (Roo Code release notes) |
| `AI Overviews traffic drop case study` | 0 direct hits | — |
| `GEO experiment results` | 20 | No relevant hits |
| `AI search referral revenue` | 13 | No relevant hits |
| `zero click AI traffic experiment` | 2 | No relevant hits |
| Item fetch: `43751004`, `44136897`, `44737677`, `46907123`, `47457472`, `47349948`, `46642490` (Aventos), `47349948` | — | Full text and comment trees pulled for the items that cleared screening; see raw files |

HN thread volume for S5 (threads found carrying any GEO/AEO/AI-visibility content, this session's query set, all dated as shown in each raw file): **8 distinct Hacker News threads** directly reviewed in full (44737677, 46907123, 47349948, 44136897, 47457472, 43438190, 46642490, 43751004), spanning 2025-04-21 to 2026-03-20. Hacker News does not publish a subreddit-style aggregate count; the 8 is a count of this session's own reviewed threads, not a platform-reported total.

### DuckDuckGo HTML queries (`html.duckduckgo.com/html/`), all run 2026-09-22, used sparingly per task instruction and rate-limited by the endpoint itself (several queries returned HTTP 403 after repeated use — recorded, not retried past one failure)

| Query | Result |
|---|---|
| `site:reddit.com/r/SEO "AI visibility" results` | 0 results |
| `site:reddit.com/r/bigseo generative engine optimization test` | 8 results, all pre-2022 tooling threads, none about AI-assistant visibility |
| `site:reddit.com/r/PPC "ads in ChatGPT"` | 0 results |
| `site:reddit.com "AI Overviews" traffic drop data` | 3 results — none in r/SEO, r/bigseo, or r/PPC (r/marketing, r/RealSEO, r/AIOverviews instead — out of this cluster's named-subreddit scope, logged below, not pulled) |
| `site:reddit.com "ChatGPT traffic" "no change" OR "nothing moved"` | 0 results |
| `site:reddit.com/r/SEO "AI Overviews" case study results` | 2 results, neither about AI-assistant visibility specifically (Google I/O reaction thread; a schema-markup tip thread) |
| `site:reddit.com/r/SEO ChatGPT referral traffic increase percent` | 7+ results (list truncated by the fetch tool's length cap before a full count was obtained); most were off-topic (ChatGPT-authored-content-for-Google-ranking threads, a different question from AI-assistant visibility); one on-topic title found and logged below (`1fk6eq0`, "We just started seeing chatgpt referrals to our...") but never opened — see blocker above |
| `site:reddit.com/r/SEO "ChatGPT" traffic "before and after"` | 0 results |
| `site:reddit.com/r/SEO "GEO" "nothing moved" OR "no lift" OR "waste of money"` | Query failed (HTTP 403, endpoint rate limit) — not retried |
| `"GEO is overhyped" AI search` | 0 results |
| `"nothing moved" AI visibility traffic` | 0 results |
| `llms.txt experiment "no traffic" blog` | 0 results |
| `"ChatGPT citations" experiment "did not"` | 0 results |
| Various non-Reddit discovery queries (AI Overviews traffic, ChatGPT ads results, prompt-set dataset, etc.) | Surfaced the blog and LinkedIn candidates pulled to `docs/raw/`, and the screened-out items below |

### Reddit threads found (title/snippet only) but not pulled — logged for S5 and as unresolved leads

| Subreddit | Thread title (as indexed) | URL | Notes |
|---|---|---|---|
| r/SEO | "We just started seeing chatgpt referrals to our..." | `www.reddit.com/r/SEO/comments/1fk6eq0/we_just_started_seeing_chatgpt_referrals_to_our/` | Title suggests exactly the before/after claim this cluster wants; DDG's own snippet for this result was suppressed ("We would like to show you a description here but the site won't allow us"), giving no usable text; every fetch/browser method in the blocker list above failed on this specific URL |
| r/marketing (outside named scope) | "Did AI Overviews Tank Your Traffic?" | `www.reddit.com/r/marketing/comments/1dfa5a4/did_ai_overviews_tank_your_traffic/` | DDG snippet quotes a specific figure ("down 30%" per Fathom Analytics on one site) — a strong candidate, but r/marketing is outside this cluster's three named subreddits (r/SEO, r/bigseo, r/PPC) and the thread itself was never opened (same blocker); flagged for a future pull if Reddit access is restored |
| r/RealSEO (outside named scope) | "Study Shows AI Overviews are Highly Correlated to Lower Traffic from... [an] 8.9% Decline in Clicks" | `www.reddit.com/r/RealSEO/comments/1d23kpi/...` | Same — outside named scope, not opened |

## Candidate table — every write-up screened on intake

| # | Author / platform | Date | Engine(s) | Metric | Figure (verbatim) | Vertical (as named) | Direction | Grade (missing items) | Artefacts published | Raw path |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | madanparas, Hacker News | 2025-07-30 | ChatGPT (Browsing), Perplexity | traffic | "18.2% of sessions now come from LLM-originated paths"; "9 Perplexity query quotes"; "~30,000 views across Reddit" | none named | positive | Fools gold — missing: named/single brand, absolute dates, disinterested measurer | none | `docs/raw/e-case-practitioner-hackernews-firegeo-reddit-perplexity-leads-2026-09-22.md` |
| 2 | nworley + thread, Hacker News | 2026-02-05 | ChatGPT | none | n/a — discussion, no figure claimed | none named | null | Not a case — method write-up | none | `docs/raw/a-practitioner-hackernews-chatgpt-recommend-discussion-2026-09-22.md` |
| 3 | marcosviladomiu (self-ID'd Bang & Olufsen EMEA Marketing Director), Hacker News | 2026-03-12 | ChatGPT, Perplexity, Claude | visibility | "results were uncomfortable" (unquantified) | none named ("premium audio" quoted) | negative | Fools gold, thin — missing: dates, n, any figure at all | none | `docs/raw/e-case-practitioner-hackernews-bando-geo-experiment-2026-09-22.md` |
| 4 | keploy, Hacker News | 2025-05-30 | ChatGPT, Perplexity, Claude | none | "got no results" (unquantified) | none named | negative | Below bar — missing: brand, dates, n, engine-specific result | none | `docs/raw/e-case-practitioner-hackernews-llmstxt-no-results-2026-09-22.md` |
| 5 | Gaurav Tiwari, personal blog | 2026-08-31 | Google AI Overviews | traffic | "22% CTR drop"; "20-40%" and separately "down 22% average CTR" for informational queries (three figures, kept side by side); "18 [of 50 queries checked] triggered AI Overviews. My CTR dropped on 14 of those 18... the other 32 queries were unaffected"; opinion queries "up 8%" | none named | mixed — negative (informational), positive (opinion/comparison) | **Silver** — missing: absolute date window, independent/disinterested measurer | none | `docs/raw/e-case-practitioner-blog-gauravtiwari-ai-overviews-ctr-2026-09-22.md` |
| 6 | Umar Tazkeer, via VEONIB video summary | 2026-09-14 (summary date) | ChatGPT Ads | traffic | "123 impressions and 38 clicks but zero conversions over two days" | none named | negative | Fools gold — missing: baseline, absolute dates, primary-source verbatim (third-party summary) | none | `docs/raw/e-case-practitioner-blog-veonib-chatgpt-ads-india-2026-09-22.md` |
| 7 | vincko (Sitefire) + thread, Hacker News | 2026-03-20 | ChatGPT, Gemini, Google AI Mode | none | n/a — vendor launch + methodology discussion, no figure claimed | none named | null | Not a case — vendor launch + method write-up | none | `docs/raw/a-practitioner-hackernews-sitefire-launch-discussion-2026-09-22.md` |
| 8 | Muneeb Ahmad, LinkedIn | 2026-06-20 | ChatGPT Ads | traffic | "DTC campaigns take off. B2B campaigns plateau within days." (unquantified); "lower CPAs and higher click through rates" for DTC (unquantified) | none named | mixed — positive (DTC), negative (B2B) | Fools gold — missing: any numeric figure at all, dates, sample size | none | `docs/raw/e-case-practitioner-linkedin-muneeb-ahmad-chatgpt-ads-b2b-dtc-2026-09-22.md` |
| 9 | Shivam S Srivastava, LinkedIn | 2026-09-10 | ChatGPT Ads | none | n/a — critique of missing attribution data, no figure claimed | none named | null | Not a case — method write-up | none | `docs/raw/a-practitioner-linkedin-shivam-srivastava-chatgpt-ads-gap-2026-09-22.md` |
| 10 | ShaunM89 / "Wayfinder AI", GitHub | undated | Ollama, OpenAI, Anthropic, HuggingFace (user-configurable) | none | n/a — tool/method README, no tracked-brand result published | none named | null | Not a case — method/tool write-up | **method + code** (Wilson CIs, adaptive sampling, structured prompt generation) | `docs/raw/a-practitioner-github-open-prompt-visibility-tool-2026-09-22.md` |

## Trust-raising subset (published a prompt set or dataset, per trust-rubric.md "Trust rises when... prompt set, raw data, or method appendix is published")

**1 of 10** — candidate #10 (ShaunM89 `open-prompt-visibility`, GitHub). Publishes open-source code and a documented method (structured prompt generation across 4 classification dimensions with phrasing variations; Wilson-confidence-interval statistical analysis; adaptive sampling), MIT-licensed. Caveat, stated in the raw file itself: this publishes the *method and code* for generating a prompt set and running a tracker — it does not publish a populated *results dataset* for any real tracked brand. No other candidate in this cluster publishes a prompt set, raw data export, or method appendix; the screened-out GitHub repo (`henu-wang/geo-case-studies`, below) *claims* a documented method ("11 distinct signals... assigns an overall grade") but the grading tool itself (GEOScore AI) is not open — its scoring code is not published, only marketing copy about it — so it does not qualify for this subset and was screened out on separate grounds (vendor marketing) as well.

## Write-ups describing corpus seeding or manipulation techniques (for Pass 5 citation, not graded here)

None found in this cluster's discovery. No candidate reviewed described deliberately seeding citations, gaming AI recommendation through fabricated mentions, or comparable manipulation technique in enough detail to route to Pass 5. (The screened-out `henu-wang/geo-case-studies` repo describes legitimate technical GEO changes — robots.txt, schema markup, llms.txt — not manipulation, and is not routed to Pass 5 on that basis either.)

## Screened-out list

| Item | Reason screened out |
|---|---|
| `github.com/henu-wang/geo-case-studies` — "GEO Case Studies: Real-World AI Search Visibility Optimization" | Vendor marketing dressed as an open-source repository: every case study is anonymised ("SaaS Documentation Site", "E-commerce Product Pages") with no credibly specified profile beyond an industry label; every case is graded solely by the vendor's own unpublished proprietary tool (GEOScore AI, whose scoring method is not itself open); the README funnels directly into a network of the same vendor's SEO-linkbait repos (`awesome-geo`, `geo-badge-generator`, `llms-txt-examples`, etc.) — a classic content-marketing link-farm pattern. Trust-rubric.md "Vendor measuring the thing it sells, no third-party replication." Not pulled to `docs/raw/`. |
| `allaboutai.com/ai-seo/ai-visibility-checkers/` — "I Tested 10 AI Visibility Checkers and the Results Shocked Me" | Listicle/roundup (tier 7 per trust-rubric.md); per task instruction, listicles are screened, not pulled |
| `explodingtopics.com/blog/ai-visibility-guide`; `semrush.com/blog/ai-search-visibility-study-findings`; `amplitude.com/blog/ai-visibility-explained`; `www.conductor.com/academy/how-to-maximize-ai-visibility` | Company/vendor blogs, not individual practitioner write-ups — overlaps this programme's P4-c2 (agency posts) / P4-c4 (vendor case studies) clusters, out of this cluster's practitioner-forum remit |
| `jarodthornton.com/2026/07/ai-overviews-killed-traffic/` | Reads as agency/consultant marketing content ("Jarod Thornton Studio") rather than a personal practitioner account; no quantified before/after figure specific to the author's own data, only generic industry claims |
| `autorank-ai.com/...case-study...`; `ecommercegermany.com/blog/generative-engine-optimization-case-study/`; `www.hashmeta.ai/en/blog/case-study-...`; `www.aicited.org/case-analyses/...` | Vendor/agency "Client X"-style anonymised case studies surfaced while searching for practitioner content — same P4-c2/P4-c4 overlap as above, and several show signs of templated/AI-generated marketing copy (round percentage figures, no named brand, no linked source data) |
| `searchsentry.io/blog/...`, `digiencode.com/...`, `pressgazette.co.uk/...`, `asquaresolution.com/blog/...`, `www.all-eo.com/hub/articles/...`, `contently.com/2026/04/27/...` | Further "AI Overviews killed your traffic" company/agency blog posts found in the same search batch as the Gaurav Tiwari post that was pulled; screened for the same reason (agency/company marketing content, not an individual practitioner's own measured data) — not opened in full, screened on title/snippet and domain pattern alone |
| `43751004` "After writing over 10k+ blogs, here's what I learned about AEO" (Hacker News) | Reviewed in full (via HN Algolia item fetch) — thin generic SEO-tips content, no n, no dates, no measured figure; comment thread adds only unrelated tips. Below the discard-on-sight line even for a thin negative-result case |
| `46642490` "Show HN: Aventos – An experiment in cheap AI SEO" | Reviewed via HN Algolia search-result metadata (19 points, 16 comments) but not opened to full text/comments in this session — a vendor product launch, same shape as the Sitefire thread already pulled; not pulled a second time in the interest of the 8-12 write-up budget |
| `43438190` "Ask HN: Is LLMs.txt a REAL thing now?" | Reviewed in full — 2 comments, neither carries a figure; both are "unclear how much traffic" hedges. Thinner than the llms.txt item that was pulled (44136897), which at least states a definite (if unquantified) negative outcome; not pulled a second time |
| `www.linkedin.com/pulse/i-ran-chatgpt-ads-b2b-dtc-only-one-audience-actually-converts-ahmad-c5vgf` sidebar item "Spent $161 → Generated $1,996 in Med Spa Appointment Value" (same author, Jun 17 2026) | Title gives no indication of AI-assistant relevance (general PPC/med-spa funnel); not opened |
| Reddit threads found by title/snippet only (`1fk6eq0` r/SEO; `1dfa5a4` r/marketing; `1d23kpi` r/RealSEO) | Could not be opened by any available method this session — see "Reddit threads found but not pulled" table above, not screened out on merit, screened out on access |
| Bing web search (`www.bing.com/search?q=...`) | Blocked by `robots.txt` disallow on `/search` path for the fetch tool's user-agent; not retried via browser (task instructs DDG, not Bing, as the fallback engine) |

## Counts

- **Write-ups pulled to `docs/raw/`: 10** (6 graded as cases — `e-case-practitioner-...` — and 4 filed as method write-ups with no result claim — `a-practitioner-...`), within the task's 8-12 target.
- **Screened total: 24** distinct items reviewed beyond the 10 pulled (13 named in the screened-out table above as discrete items/domains, plus 3 Reddit threads found but blocked from opening, plus the ~8 HN queries and ~9 DDG queries that returned zero on-topic hits, each representing a screening pass even where no single item is separately named).
- **Screened per vertical:** Skincare and beauty — 0. B2B SaaS — 0. High-CPA regulated — 0. **None named — 34** (all 10 pulled write-ups plus all 24 screened items named a vertical the source itself did not tie to one of the three tracked verticals, or named no vertical at all; per `demand-signals.md`'s cell-attribution rule, nothing is inferred, so every item here reads `none named` rather than being force-fit to a vertical).
- **Cleared per vertical:** all three tracked verticals — **0 cleared** (no candidate in this cluster named skincare/beauty, B2B SaaS, or high-CPA regulated as its own vertical). Cleared, ungated by vertical: 6 (the 6 `e-case-practitioner-...` files; "cleared" here means "graded as a case," not "cleared the full seven-item evidence bar" — none reached Silver-or-better on every bar item; see the grade column above, where the single Silver (#5) is still missing an absolute date window and a disinterested measurer).
- **Negative results: 3** — #4 (llms.txt, "got no results"), #6 (ChatGPT Ads India, zero conversions), and the negative half of #8 and #5's mixed reads (not counted twice; #5 and #8 are recorded as "mixed" in the candidate table, not double-counted into this negative tally).
- **Positive results: 1 pure positive** (#1) **+ 2 mixed with a positive component** (#5, #8).
- **Unknowns recorded: 2** — (a) whether Reddit thread `1fk6eq0` ("We just started seeing chatgpt referrals to our...") in fact carries a before/after figure, `unknown — checked DuckDuckGo snippet only, Reddit itself blocked, 2026-09-22`; (b) whether "Wayfinder AI" (credited in candidate #10's page title) is the author's own company or an unrelated third party, `unknown — checked the repository's rendered README only, 2026-09-22`.

## Caveats

- This cluster's headline finding is methodological, not substantive: **Reddit — the primary named channel for this cluster (r/SEO, r/bigseo, r/PPC) — was completely inaccessible this session** across five distinct access methods (see Blocker section). Every write-up pulled is a substitution under the shortlist.md "a pull that surfaces a better primary supersedes the listed one" rule, applied here in reverse (no primary was available, so a secondary channel — Hacker News, personal blogs, LinkedIn, GitHub — stood in). A re-run of this cluster once Reddit access is restored should be expected to surface additional, likely stronger, candidates — starting with the three leads logged in "Reddit threads found but not pulled" above.
- No candidate in this cluster reaches Gold. The single Silver (#5, Gaurav Tiwari) is an observational before/after of Google's own AI Overviews rollout, not a case of a deliberate brand *intervention* — bar item 5 ("the intervention itself") is genuinely absent from that case, a structural gap distinct from a missing-evidence gap, noted in the raw file itself.
- Three of six graded cases (#1, #6, #8) rest on a practitioner who is also selling a related product or service (FireGEO's operator; a paid-media agency founder; a media buyer) — a direct commercial-interest overlap flagged in each raw file's `tier_reason`, not resolved here.
- Two of the ten pulls (#8, #9, the two LinkedIn articles) could not be fetched by the standard `fetch` tool at all (LinkedIn's `robots.txt` disallows every crawler user-agent this session could present as, including several explicitly-named AI-company bots) and were instead pulled via the MCP_DOCKER Playwright browser reading rendered DOM text — a different, browser-based pull method recorded in each file's `pull_method` field.
- "Screened per vertical: 0 / 0 / 0" is a real absence, not an oversight: no query run this cluster was vertical-scoped (per shortlist.md, vertical tagging in Pass 4 is "a cluster scope, not a query" — but P4-c5's own query set, per query-book.md, does not carry the vertical overlay tokens the way a vertical-scoped cluster would), and no candidate found on its own named one of the three tracked verticals. This is recorded as the finding, not compensated for by inference.
