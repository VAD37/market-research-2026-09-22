# IAB — "Digital Ad Revenue Climbs to Nearly $300B as IAB Celebrates 30 Year Anniversary" (IAB/PwC Internet Advertising Revenue Report: Full Year 2025)

```yaml
source:          Interactive Advertising Bureau (IAB), press release on iab.com; report conducted by PwC
url_or_doc_id:   https://www.iab.com/news/digital-ad-revenue-climbs-to-nearly-300b-as-iab-celebrates-30-year-anniversary/ ; report landing https://www.iab.com/insights/internet-advertising-revenue-report-full-year-2025/
published:       2026-04-16
pull_date:       2026-09-23
pull_method:     fetch (curl with contact User-Agent; HTML stripped; the press release rendered in full; the report landing page is gated behind a free IAB account after two paragraphs)
pull_purpose:    evidence about a number
tier:            4
tier_reason:     trade-association benchmark compiled by PwC from company-reported data; the method section sits in the gated report, not on the release — held at tier 4 (industry aggregate with a named preparer), not 2 (not filed) and not 5 (not a vendor selling the measurement)
source_label:    analyst-derived
lane:            E (Pass 16 c1 — industry baseline), B
sub_market:      paid placement (US search and commerce-media baselines)
engine:          n/a ("Search revenues (including AI search)")
metric_kind:     sales (US digital ad revenue, USD)
supersedes:      none
captured:        press release body through the Project Eidos paragraph; table reproduced; report landing-page intro
```

## Verbatim

Headline: "Digital Ad Revenue Climbs to Nearly $300B as IAB Celebrates 30 Year Anniversary". Sub-headline: "Overall Revenue Grew +13.9% YoY; Video, Social, and Commerce Media Drive Growth as AI Reshapes the Ecosystem". "Creator Advertising is Now a Core Media Channel, with Spend Reaching $37B". Dateline: "New York, NY – April 16, 2026".

> "Now in its 30th year, IAB released its 2025 Internet Advertising Revenue Report, conducted by PwC, which was first issued in 1996 and continues to serve as the industry's definitive benchmark."

> "Despite concerns about economic and geopolitical uncertainty, the industry drove record revenue, reaching $294.6 billion in 2025, reflecting a 13.9% year-over-year increase. These results were particularly notable given that 2025 lacked major cyclical events such as the Olympics, FIFA World Cup, or elections, which historically drive increased ad spending across the digital ecosystem."

> "'This revenue growth reflects a market that has reoriented around performance channels. As expectations for measurable outcomes rise, investment is concentrating in areas that can directly correlate spend to business results,' said David Cohen, CEO, IAB. 'At the same time, artificial intelligence is rapidly moving from theory into practice, emerging as a meaningful driver of efficiency and effectiveness across the ecosystem.'"

Growth by Advertising Category (table as printed):

| Ad Category | Revenue | % of YoY Growth | % of Total Digital Ad Revenue |
|---|---|---|---|
| Social | $117.7B | 32.6% | 40.0% |
| Digital Video | $78B | 25.4% | 26.5% |
| Commerce Media | $63.4B | 18% | 21.5% |
| Search | $114.2B | 11% | 38.8% |
| Podcast | $2.9B | 17.6% | 1% |
| Display | $81.6B | 9.8% | 27.7% |

[note: the category shares sum to more than 100% as printed; categories overlap by the report's construction — recorded as printed]

> "Programmatic advertising rose 20.5% YoY to $162.4 billion, gaining $27.6 billion in new spend as automated buying scales and lays the groundwork for agentic AI-driven media buying."

> "Commerce media grew 18.0% YoY to $63.4 billion, reinforcing its role as a core performance channel powered by first-party data."

> "Search is still important, but growth is slowing. Search revenues (including AI search) continue to hold the largest share of revenue dollars, reaching $114.2 billion in 2025. While search grew 11% YoY, its growth rate slowed considerably vs. 2024 (15.9%)."

> "AI is becoming advertising's infrastructure layer. It is redefining discovery, creative production, execution, and monetization. Specifically, it will mean deeper first-party data, integrated commerce ecosystems, proprietary measurement infrastructure, and the ability to offer end-to-end buying. AI is redefining the entire value chain, including agent buying and selling, creative production, AI-driven commerce to both humans and agents, and more."

> "Creator advertising spend reached $37B in 2025. Creator is growing faster than the broader advertising market, with spending projected to reach $44B in 2026."

> "'The lesson of our 30-year history is that measurement, standards, and interoperability — as mundane as those things can sometimes sound — are what got this industry from zero to just shy of $300 billion,' continued Cohen. 'And with the disruption and opportunity that AI is bringing into the ecosystem, there is still lots of vital work ahead.'"

Report landing page (public portion):
> "Just released: IAB Internet Advertising Revenue Report: Full Year 2025. The digital advertising industry reached nearly $300 billion in revenue in 2025, the highest level in the report's history. This 13.9% year-over-year increase underscores the industry's continued evolution toward performance-driven, AI-powered growth."
> "Now in its 30th year, this highly anticipated report is considered the industry benchmark for U.S. advertising revenue across digital media platforms and publishers. This year's report offers a comprehensive view across video, social, search, commerce media, and the creator economy ..."
> "Claim your free account to continue reading. Log In or Create Account"

[note: report body and PDF gated behind a free IAB account — not registered, per rules; no breakout of "AI search" inside the $114.2B search figure on the release; the hero image on the release is a banner, not a data chart — no image saved]

## Pull notes — mechanical only

- Release URL found through a Brave Search result list (search.brave.com; one successful curl before the engine walled with a CAPTCHA). Both iab.com pages returned HTTP 200 to plain curl.
- The table is HTML on the release page; reproduced cell by cell.
