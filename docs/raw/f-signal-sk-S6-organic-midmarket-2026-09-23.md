# Passionfruit — GEO agency roundup for DTC beauty brands, mid-market pricing tier and named case (S6, organic)

```yaml
source:          Passionfruit (GEO/AI-search agency, getpassionfruit.com)
url_or_doc_id:   https://www.getpassionfruit.com/blog/best-geo-agencies-for-dtc-beauty-brands
published:       2026, undated on page (page references "2026" repeatedly as current year)
pull_date:       2026-09-23
pull_method:     fetch (curl, no browser; WebSearch run once first per task instruction, this URL was its top hit)
pull_purpose:    evidence about a number
tier:            3 on existence (agency roster and its own client case exist), 6 on framing (marketing copy, comparison table is the agency's own positioning of itself and competitors)
tier_reason:     demand-signals.md S6 default — "3 on existence, 6 on framing"
source_label:    vendor-reported
lane:            F
sub_market:      organic recommendation
engine:          ChatGPT, Perplexity, Gemini, Claude, Google AI Overviews (Passionfruit Labs' own tracking platform, named generically)
metric_kind:     visibility (named case only; not independently verified)
supersedes:      none
captured:        full article body after HTML/CSS stripped
```

## Verbatim

> "A DTC beauty founder at $10M to $50M needs different things than an enterprise beauty conglomerate, and the existing lists rarely separate the two."

> "Named beauty outcome: our Solawave GEO case study documents 1,400% AI search traffic growth for the beauty tech brand across the major AI platforms. No other agency in the SERP for 'best GEO agencies for beauty' has a comparable published beauty result."

> Comparison table (agency × self-described "growth-stage DTC fit" column, verbatim cell text): "Passionfruit ... Strong" / "Onely ... Enterprise-skewed" / "Siege Media ... Mid-market" / "NoGood ... Strong" / "Stella Rising ... Mid-market beauty" / "Single Grain ... Generalist" / "Pilothouse ... Paid-social-first" / "Amsive Digital ... Established brands"

> Stella Rising entry: "Stella Rising is a NYC-based agency with deep beauty industry expertise across mass, prestige, and luxury segments. The agency reports search drives 60% of traffic and 40% of conversions for its beauty clients. ... The honest gap: limited public evidence of GEO services or multi-platform AI monitoring."

> Pricing: "The honest range is wide. Boutique GEO engagements start around $5,000 to $10,000 per month. Mid-market integrated GEO and SEO retainers sit between $12,000 and $30,000 per month. Enterprise omnichannel programs run $50,000 to $100,000-plus per month. The right number depends on your revenue, the channels in scope, and whether AI search is the lead or part of a wider engagement."

## Pull notes — mechanical only

- One `WebSearch` query run first ("GEO AEO agency case study mid-size beauty brand client 'employees'") per this task's instruction to try WebSearch once before direct fetch; this article was the top and only beauty-specific hit. Article fetched directly by curl, HTML tags stripped with a regex, no JavaScript rendering needed.
- "Mid-market" and "Mid-market beauty" in the comparison table are Passionfruit's own positioning of itself against competitor agencies — a target-customer / growth-stage descriptor, not a disclosed client roster. Per `demand-signals.md`'s cell-attribution rule ("Nothing is inferred from a vendor's target-customer page — sell-side claim"), this framing is recorded as existing (S6 checked) but **moves no cell** — it names no actual mid-market beauty buyer.
- The one named beauty case (Solawave) sits inside Passionfruit's own stated target band "$10M to $50M" revenue, which per `demand-signals.md`'s buyer-size table is the **SMB** revenue fallback (under 50M USD annual), not mid-market. Solawave's own headcount was not checked in this pull (out of scope — the SMB skincare cell already reads attention on a different signal per `customers/skincare-beauty.md`). Not applied to the mid-market cell.
- No client, case, or pricing tier on this page names a mid-market-banded beauty buyer by name. Recorded as `blank — unattributed` for the Organic/Mid-market cell's S6 column: the mid-market pricing tier and agency-fit label exist and are vertical-relevant, but per the boundary rule attribute to no company this repo can band.
- No login, no paywall, no CAPTCHA.
