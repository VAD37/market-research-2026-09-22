# EMARKETER (relaying Axios) — "OpenAI projects $2.5 billion in ad revenues this year and $100 billion by 2030"

```yaml
source:          EMARKETER (article author: Marisa Jones), relaying Axios reporting on OpenAI investor presentations
url_or_doc_id:   https://www.emarketer.com/content/openai-projects--2-5-billion-ad-revenues-this-year--100-billion-by-2030 ; underlying report Axios, https://www.axios.com/2026/04/09/openai-100-billion-in-ad-revenue (attempted direct fetch this pull, returned HTTP 403 — not independently confirmed against Axios's own text)
published:       2026-04-09
pull_date:       2026-09-22
pull_method:     fetch (mcp fetch tool; emarketer.com fetched cleanly this specific article page, unlike the paywalled report pages in the companion pulls in this cluster; axios.com returned 403 to plain fetch)
pull_purpose:    evidence about a number
tier:            5
tier_reason:     news relay of an unpublished, unofficial figure — OpenAI itself did not publish this projection; per the source's own wording it comes from "a source familiar with recent presentations to investors" (Axios's sourcing, relayed by EMARKETER), not a company-published statement or filing. No independent confirmation from OpenAI. Per trust-rubric.md this sits at tier 5 (agency/press relay with a named date and a specific, internally consistent multi-year figure set) but is explicitly a leak, not a disclosure — bias flagged
source_label:    company-stated
lane:            B
sub_market:      paid placement
engine:          ChatGPT — OpenAI
metric_kind:     none
supersedes:      none
captured:        full short-form EMARKETER "news" item, truncated by the fetch tool's per-call limit at the final sentence (mid-way through a reference to OpenAI's ChatGPT ads pilot revenue and its anticipated IPO) — the year-by-year figures were captured in full before the cut-off
```

## Verbatim

Headline: "OpenAI projects $2.5 billion in ad revenues this year and $100 billion by 2030." Byline: "Article by Marisa Jones | Apr 9, 2026."

The size and forecast figure (the sentence carrying the number, and the year-by-year path):

> "The news: OpenAI anticipates $2.5 billion in ad revenues this year, Axios reports. The company estimates that this figure will skyrocket to $100 billion by 2030.
>
> Investors have been told that ad revenues will increase to $11 billion in 2027, $25 billion in 2028, and $53 billion in 2029. This projection assumes OpenAI products will have 2.75 billion weekly users by 2030."

Context sentence, linking this projection to a separate, already-measured figure (see `docs/raw/b-openai-1bn-run-rate-milestone-2026-09-22.md` for that measured milestone, cited here for contrast, not re-pulled):

> "Zooming out: The news comes shortly after OpenAI claimed that its US ChatGPT ads pilot exceeded $100 million in annualized revenues six weeks after launching—and ahead of the company's highly anticipated IPO, which could happen as early..." [note: sentence truncated by the fetch tool's per-call character limit at this point]

## Pull notes — mechanical only

- `emarketer.com` fetched cleanly for this specific short-form "news" article (contrast with the two full "Report" pages pulled elsewhere in this cluster, `e-market-size-emarketer-aiads-paid-2026-09-22.md` and the paid-placement summary row for "US Search Advertising Forecast 2026," both of which returned only a paywalled landing shell). This item rendered in full as a short news brief, not a gated long-form report.
- `axios.com/2026/04/09/openai-100-billion-in-ad-revenue`, the originating primary named in EMARKETER's own text, returned HTTP 403 to plain fetch this pull — not independently confirmed against Axios's own wording. EMARKETER's relay is the best-available capture this pull.
- This figure is explicitly sourced by Axios (per EMARKETER's own text) to "a source familiar with recent presentations to investors" — an unofficial leak, not an OpenAI press release or filing. Recorded as `source_label: company-stated` because the projection describes OpenAI's own internal figures relayed to investors, but flagged as unconfirmed by OpenAI directly.
- No independent OpenAI-published confirmation of this $100B/2030 figure was found or attempted beyond this relay chain in this task.
