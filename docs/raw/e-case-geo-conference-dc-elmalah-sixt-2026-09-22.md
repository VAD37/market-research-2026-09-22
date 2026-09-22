# GEO Conference Washington DC (June 2026) — "320% More LLM Citations in 14 Days" (Hadeer ElMalah, Sixt)

```yaml
source:          LinkedIn — Dr. Hadeer ElMalah (Senior SEO & GEO, Sixt), personal recap post of her own conference talk
url_or_doc_id:   https://www.linkedin.com/posts/hadeerelmalah_aaaand-thats-a-wrap-on-the-geo-conference-ugcPost-7475938734862065664-KfcP/ (also indexed under the slug .../aaaand-thats-a-wrap-on-the-geo-conference-activity-7475940877794738176-MIOS)
published:       page states "2mo" / "3mo" (relative labels shown inconsistently across the same page load — see pull notes), not an absolute date; conference itself dated "Jun 2026" (Washington DC edition) per `docs/raw/f-conference-geo-conference-nyc-2026-agenda-2026-09-22.md`'s events-index pull
pull_date:       2026-09-22
pull_method:     browser (claude-in-chrome, dedicated tab) — found via `html.duckduckgo.com/html/?q=Hadeer+ElMalah+Sixt+"320%"+LLM+citations`; get_page_text on the LinkedIn post returned a stale cached DuckDuckGo results page rather than the live LinkedIn content (repeatedly, across two calls), so javascript_tool (`document.body.innerText`, sliced) was used instead and returned the actual post text
pull_purpose:    evidence about a number
tier:            6
tier_reason:     downgraded from the trust-rubric's tier-5 default for a vendor/agency claim with no third-party corroboration — this is the speaker's own social-media recap of her own conference talk about her own employer's results; no baseline figure, no absolute date window, no measurement method, and no independent source were found. The percentage ("320%") is stated with no base number given anywhere in the captured text — trust-rubric.md's discard-on-sight list names this exact pattern ("Percentage with no base — plus 1200 percent from 3 to 39")
source_label:    company-stated
lane:            F
sub_market:      organic recommendation
engine:          n/a (talk references "LLM citations" and "AI Visibility and Share of Voice category" generically; no specific engine named in the captured text)
metric_kind:     visibility
vertical:        none named
evidence_grade:  Fools gold — bar items present: (1) brand named (Sixt, the speaker's employer). Bar items missing or unclear: (2) no specific engine named in the captured text (generic "LLM citations", "AI search"), (3) no absolute date window (only "14 Days" as a relative duration, and the conference itself only dated to the month "Jun 2026" on the events-index page, not a specific date), (4) no baseline figure disclosed anywhere in the captured text — "320% More LLM Citations" has no stated starting count, matching the trust-rubric's named discard pattern for a percentage with no base, (6) no sample size or traffic volume, (7) measured by the speaker herself (Sixt's own SEO/GEO lead) presenting her own employer's results at a no-recordings, closed-door event — no independent measurer named, and the conference explicitly has no public recording of the talk itself for cross-checking what was said on stage
paid_by_outcome: not applicable — in-house employee (Sixt) presenting her own company's results, not a paid agency engagement disclosed as such
supersedes:      none
captured:        full LinkedIn post text (javascript_tool, `document.body.innerText`, sliced across three reads to cover the full post plus its top comments); the post's photo/slide images were not OCR'd
```

## Verbatim

### LinkedIn post, Dr. Hadeer ElMalah ("Senior SEO & GEO @ SIXT | Speaker & IR Researcher | I engineer off-page entity stacks to grow brand visibility in AI | Agentic automations & AI adoption")

> Aaaand that's a wrap on the GEO Conference in Washington, D.C. 🎤 sponsored by Anthropic, OpenAI, Google, and more.
>
> My session, "320% More LLM Citations in 14 Days," walked the audience through the exact playbook that got SIXT to win the AI Visibility and Share of Voice category, and stay there.
>
> I've been to many conferences, but this one has been truly different. 15 sessions from industry-leading speakers, a Fortune 500 panel, and 150 brilliant minds in one closed room, all coming together to discuss how we're navigating the evolving space of AI search. The open conversations and discussions were incredibly refreshing.
>
> Some of my favorite talks:
> 💠 Daniel Shin Un Kang, How GEO Became Expedia's Fastest-Growing Channel
> 💠 Guy Yalif, Expanding from SEO to GEO: Actionable Playbook
> 💠 Vishvak Murahari (the inventor of the term "GEO"), Where It Started and Where It's Headed
> 💠 Fernando Angulo, What the Numbers Actually Show: Data on AI Search
> 💠 Fortune 500 & GEO Panel moderated by Aaron Poynton (American Society for AI)
>
> [closing lines about networking, and a closing joke about a Google AI Mode ad, not quoted here as not substantive to the claim]

Engagement stats shown on the post: 93 reactions, 10 comments.

Top comment exchange (from the post's own commenters, not independent verification of the figures):

> 👋🏼Thiago Pojda: "Oh this girl is going places. Super happy to have you on the team and of what you've accomplished so far..."
> Keige Tom (SEO Manager, U.S. at Philip Morris International — also named as a Fortune 500 panelist in the same conference's sample agenda): "Great pic!"

## Pull notes — mechanical only

- `get_page_text` on the LinkedIn post URL returned a stale cached DuckDuckGo search-results page (the exact same content as the prior DuckDuckGo query's `get_page_text` output) across two separate calls, despite the tab having navigated to linkedin.com per `location.href`. `javascript_tool` (`document.body.innerText`) was used instead and correctly returned the live LinkedIn page content.
- The post's relative-time label was inconsistent across reads of the same loaded page: "2mo" in one `javascript_tool` read, "3mo" in a later read of the same DOM element region — recorded verbatim as observed, not reconciled; no absolute date is shown anywhere on the page.
- LinkedIn navigation redirected the URL from the `.../activity-7475940877794738176-MIOS` slug found via search to `.../ugcPost-7475938734862065664-KfcP/` — both recorded above as the same post.
- No independent, non-LinkedIn source for the "320%" figure was found this pull (not separately searched beyond the one DuckDuckGo query that surfaced this post itself).
- Did not navigate to chatgpt.com, claude.ai, gemini.google.com, google.com/search, perplexity.ai, copilot.microsoft.com or amazon.com's assistant.
