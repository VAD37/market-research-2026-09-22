# Anthropic — Claude scale statements: run-rate revenue, customer counts, EU recipients (no consumer user count)

```yaml
source:          Anthropic (anthropic.com newsroom; support.claude.com help center)
url_or_doc_id:   https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation ; https://support.claude.com/en/articles/11595103-designated-point-of-contact-for-users-in-the-eu
published:       2026-02-12 ; help-center page shown as updated 2026-05-26
pull_date:       2026-09-23
pull_method:     fetch (MCP fetch for the newsroom page, full text to 5,000 chars; WebFetch extraction for the help-center section)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary
source_label:    company-stated
lane:            E (Pass 13)
sub_market:      n/a — engine scale, all three sub-markets
engine:          Claude — Anthropic
metric_kind:     none (revenue run rate; customer counts)
supersedes:      none (b-eu-anthropic-dsa-eu-contact-2026-09-22.md holds an earlier pull of the same help-center text; not edited)
verbatim:        partial — relevant paragraphs verbatim
captured:        section extracts
```

## Verbatim

### "Anthropic raises $30 billion in Series G funding at $380 billion post-money valuation" — Feb 12, 2026
> "We have raised $30 billion in Series G funding led by GIC and Coatue, valuing Anthropic at $380 billion post-money."
> "It has been less than three years since Anthropic earned its first dollar in revenue. Today, our run-rate revenue is $14 billion, with this figure growing over 10x annually in each of those past three years."
> "The number of customers spending over $100,000 annually on Claude (as represented by run-rate revenue) has grown 7x in the past year."
> "Two years ago, a dozen customers spent over $1 million with us on an annualized basis. Today that number exceeds 500. Eight of the Fortune 10 are now Claude customers."
> "Today, Claude Code's run-rate revenue has grown to over $2.5 billion; this figure has more than doubled since the beginning of 2026. The number of weekly active Claude Code users has also doubled since January 1."
[note: no absolute count of Claude consumer users — monthly, weekly or daily — appears in the captured text]

### Help center, "Designated point of contact for users in the EU" — shown 2026-05-26
> "Anthropic has calculated its average monthly active recipients in the EU for the six-month period ending 31 October 2025, and has concluded that it falls well below the 45 million threshold set out in Article 33(1) of the DSA."
> "Anthropic will continue to monitor the number of average monthly active recipients of its services in the EU and will publish updated information at least every 6 months."

## Pull notes — mechanical only
- WebSearch restricted to anthropic.com and claude.com for "monthly active" / "weekly active" / "daily active" returned admin-analytics documentation and a customer case (WRTN, "4.5 million monthly active users" of WRTN's own platform) — no Anthropic statement of Claude's own user count.
- Search-result summaries (not pulled, not primaries) relay run-rate figures of "$30 billion" (April 2026), "$47 billion" (May 2026), "$65 billion" (end July 2026) attributed to Anthropic via VentureBeat, simonwillison.net and Sacra; third-party MAU estimates for Claude range "12.48 million" to "245 million" across stats aggregators (tier 7, not pulled).
