# Seer Interactive — case study (Home Depot, screened not graded — source blocked)

```yaml
source:          Search Engine Land (trade press guide, citing Seer Interactive research)
url_or_doc_id:   https://searchengineland.com/guide/enterprise-ecommerce-llm-visibility-case-study
published:       2026-07-20 (as dated in DuckDuckGo's index of the page)
pull_date:       2026-09-22
pull_method:     attempted via fetch (MCP_DOCKER fetch: HTTP 403), WebFetch (HTTP 403), browser (Playwright MCP: Cloudflare "Just a moment..." challenge page), and browser extension (claude-in-chrome: Cloudflare challenge on first navigation, challenge cleared on a second navigation but `get_page_text` and `read_page` both returned an unrelated cached 2018 article, not this page's content) — full text not recoverable by any method attempted this pull
pull_purpose:    evidence about a number
tier:            6
tier_reason:     no verbatim text recovered beyond a search-engine-indexed title/snippet — cannot be tiered as a full source per trust-rubric.md ("no n, no date window, no method" as observed = discard-on-sight for a number claim); recorded at tier 6 (marketing/pointer level) reflecting that only the headline and topic are confirmed, not the substantiating data
source_label:    analyst-derived
lane:            F
sub_market:      organic recommendation
engine:          n/a — not confirmed from recoverable text
metric_kind:     none
supersedes:      none
captured:        search-result title and one-line description only (via DuckDuckGo html snippet); full article body not recovered
evidence_grade:  not graded — screened. The only recoverable text is: title "LLM visibility case study: How Home Depot is winning AI search" and description "Learn how Home Depot dominates AI search and discover six proven strategies ecommerce brands can use to boost LLM visibility, citations, and share of voice." This confirms the case study's existence and its named brand (Home Depot) but supplies none of the other six evidence-bar items (engine, date window, baseline, intervention, sample size, measurer) — per task instructions, a case with fewer than the bar's items beyond the brand is screened, not pulled as graded evidence.
```

## Verbatim

> ## LLM visibility case study: How Home Depot is winning AI search
> searchengineland.com/guide/enterprise-ecommerce-llm-visibility-case-study
> Learn how Home Depot dominates AI search and discover six proven strategies ecommerce brands can use to boost LLM visibility, citations, and share of voice.

[note: this is the full extent of text recoverable this pull. The full article — which per `searchengineland.com/topic/seer-interactive`'s indexed listing draws on Seer Interactive's research — was blocked by a Cloudflare bot-check on every access method attempted.]

## Pull notes — mechanical only

- Four access attempts, in order: (1) `mcp__MCP_DOCKER__fetch` direct — HTTP 403. (2) `WebFetch` tool direct — HTTP 403. (3) `mcp__MCP_DOCKER__browser_navigate` (Playwright, dedicated new tab, distinct from another agent's already-open courtlistener.com tab) — page loaded to a Cloudflare "Performing security verification" / "Just a moment..." interstitial, not the article. (4) `mcp__claude-in-chrome` browser extension, which reconnected mid-session (was reported not connected at task start via `tabs_context_mcp`) — first navigation hit the same Cloudflare interstitial; a second navigation to the same URL returned a page titled correctly ("Seer Interactive Archives - Search Engine Land" — note: this was attempted on the *topic archive* URL, not the case-study guide URL directly, see `f-seer-interactive-sel-topic-2026-09-22.md`) but `get_page_text` and `read_page` (accessibility tree, interactive-elements filter) both returned content that did not match the expected page — `get_page_text` returned a stale/cached unrelated 2018 article ("SearchCap: Google Assistant via Siri..."), and `read_page` returned only generic site-navigation chrome (nav links, an unrelated "TechCrunch" SEO-audit widget), not the Seer-Interactive-tagged article list.
- This matches the pattern other agents recorded this date for `searchengineland.com` (`channels.md` row C57: `403→ext`) and is consistent with a bot-mitigation service (Cloudflare) rather than a page-specific block.
- Per channels.md, trade press is a "pointer channel": pull the primary it links, and file the trade item only when the primary is unreachable. Here neither the trade-press page nor a primary it might point to (a Seer Interactive-hosted version of the same case study) was located or reachable this pull.
