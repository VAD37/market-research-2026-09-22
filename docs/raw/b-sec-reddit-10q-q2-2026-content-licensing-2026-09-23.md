# Reddit, Inc. — Form 10-Q, quarter ended 2026-06-30: "Other revenue" line, content-licensing concentration, remaining performance obligations

```yaml
source:          Reddit, Inc., CIK 0001713445 — Form 10-Q, quarterly period ended June 30, 2026, accession 0001713445-26-000100
url_or_doc_id:   https://www.sec.gov/Archives/edgar/data/1713445/000171344526000100/rddt-20260630.htm
published:       2026-07-31 (EDGAR file date)
pull_date:       2026-09-23
pull_method:     fetch (curl, User-Agent "market-research-bot contact: research@example.invalid", sec.gov Archives HTTP 200; HTML tag-stripped, table cells joined with " | ")
pull_purpose:    evidence about a number
tier:            2
tier_reason:     table default — filed
source_label:    filed
lane:            B
sub_market:      n/a — publisher / sell-side monetisation (content licensing to AI companies)
engine:          n/a — names Google, Meta, OpenAI, Anthropic as LLM competitors
metric_kind:     none
supersedes:      none — complements raw/b-reddit-10q-q2-2026-advertising-revenue-2026-09-23.md (advertising line only) and raw/b-reddit-10k-2025-advertising-revenue-2026-09-23.md
captured:        revenue disaggregation table; deferred revenue and remaining-performance-obligation sentences; revenue-recognition sentence on content licensing; risk-factor paragraphs on content licensing
```

## Verbatim

Revenue table (Note — Revenue):

> Three months ended June 30, | Six months ended June 30, |
> 2026 | 2025 | 2026 | 2025 |
> (in thousands) |
> Advertising revenue | $ | 761,625 | $ | 464,785 | $ | 1,386,295 | $ | 823,415 |
> Other revenue | 43,280 | 34,842 | 82,021 | 68,573 |
> Total revenue | $ | 804,905 | $ | 499,627 | $ | 1,468,316 | $ | 891,988 |

> Deferred revenue was $ 38.6 million and $ 18.1 million as of June 30, 2026 and December 31, 2025, respectively. Revenue recognized during the six months ended June 30, 2026 and 2025 included substantially all of the deferred revenue balance at the beginning of each respective period.
> As of June 30, 2026, the aggregate amount of remaining performance obligations in contracts with an original expected duration exceeding one year was $ 92.1 million. This amount consists primarily of long-term content licensing contracts and [sentence continues past page break; remainder not captured]

Revenue recognition:

> We also generate revenue from content licensing and products sold directly to users. In our content licensing arrangements, we provide customers with the right to access content from our platform over the contractual period. We recognize content licensing revenue as our content partners consume and benefit from their use of the licensed content, which is generally ratably [truncated at 900 characters in this pull]

Strategy bullets (MD&A):

> • strategies to expand revenue from non-advertising sources, like content licensing;
> • We are exploring business opportunities in content licensing, but the market is relatively new and evolving rapidly.

Risk factors:

> In addition, we face competition from large language models ("LLMs") and other AI models and features that retrieve and synthesize information, such as those built by Google, Meta, OpenAI, and Anthropic.
> We also continue to explore reasonable content licensing opportunities as another possible source of revenue where those opportunities do not conflict with our values and the rights of our Redditors and have only recently generated revenue from this opportunity.
> We have explored, and will continue to explore, business opportunities in content licensing for purposes including machine learning, business analysis, display, and training generative AI models. The market for content licensing is rapidly evolving, and there is no assurance that we will be able to sustain revenues from these efforts.
> The licensing of content for machine learning and AI training purposes is a novel business model without an established track record, which makes it difficult to evaluate our future prospects and the risks and challenges we may encounter in seeking to execute on this opportunity. Although we have negotiated content licensing agreements with a number of partners that are medium-term in length, to date, substantially all of the contract value associated with our licensing revenue is derived from two of our partners, and these arrangements may not be renewed, or they may be renewed based on less favorable terms, such as using fewer services at lower pricing. Our content licensing agreements are subject to terms and conditions, including API performance requirements, that we may be unable to meet. In addition, our existing content licensing agreements may be terminated, not renewed, or renewed on less favorable terms. The commercial market for LLMs may not develop or may be limited by regulation or other factors, and accordingly, the value of content for AI training purposes may be reduced over time [...]
> Given the novel nature of these technologies and commercial arrangements, we have received and expect to continue to receive inquiries regarding our content licensing efforts from regulators. For example, the Dutch data protection authority, the Autoriteit Persoonsgegevens (the "Dutch AP"), has inquired into and ordered access to information about our content licensing efforts, which we are contesting.

## Pull notes — mechanical only

- "Other revenue" is the only line where content licensing sits; the filing does not break content licensing out from "products sold directly to users". No partner is named; "two of our partners" is the concentration statement.
- The remaining-performance-obligation sentence is cut by the page-break marker "12 / Table of Contents" in the stripped text; the figure ($92.1 million) and its lead clause are complete.
- EDGAR full-text search (efts.sec.gov) returned `{"message":"Forbidden"}` to curl with the research User-Agent and an "Undeclared Automated Tool" page to the Playwright browser; filings were located via data.sec.gov/submissions JSON (HTTP 200) and pulled from Archives.
