# Yext — customer stories index and seven featured multi-location case pages (Brookdale, Cox Communications, Domino's, Fazoli's, FedEx, IHG Hotels & Resorts, Samsung): location counts and AI-search mentions

```yaml
source:          Yext (yext.com) customer-stories pages
url_or_doc_id:   https://www.yext.com/customers ; https://www.yext.com/customers/brookdale ; /customers/cox-communications ; /customers/dominos ; /customers/fazolis ; /customers/fedex ; /customers/ihg-hotels-resorts ; (/customers/samsung linked, not opened)
published:       undated — live pages
pull_date:       2026-09-23
pull_method:     fetch (curl / python urllib, User-Agent "market-research-bot contact: research@example.invalid"); HTML stripped by script
pull_purpose:    evidence about a number
tier:            5
tier_reason:     vendor case pages naming customers (demand-signals.md S2: "logos are not contracts"); no n or metric on the pages opened
source_label:    vendor-reported
lane:            F
sub_market:      organic recommendation
engine:          n/a — engines appear only in a site-navigation blog link, not in any story body
metric_kind:     none
supersedes:      none — extends docs/raw/a-yext-customers-2026-09-22.md
captured:        story links on the index; per story, lines naming locations, AI or engines
verbatim:        partial
```

## Index — https://www.yext.com/customers (HTTP 200, 118,674 bytes)

Story links in the static HTML (7): brookdale, cox-communications, dominos, fazolis, fedex, ihg-hotels-resorts, samsung. [note: the index is script-rendered; only the featured seven appear in the fetched HTML.]

Navigation text on every page (verbatim, site-wide): "Scout — Monitor AI search visibility and track competitors in real time" · "Listings — Manage & optimize your location information across the web" · "Publishers … OpenAI — Deliver natural language responses to user queries." · "Industries: Financial Services — From branch to advisor—see and shape your brand visibility. Healthcare — Connect patients to care faster—across AI, search, and digital channels. Retail — AI-ready visibility and insights to grow every retail location. Food — Stay visible and competitive—every store, every search, every meal. Hospitality — From search to stay—Yext helps hospitality brands win locally." · blog link "Same Search, Different Results? Why Google, ChatGPT, Claude, and Perplexity Deliver Different Answers".

## Story pages — lines naming locations or AI

| Story | Line, verbatim | AI-search line in story body |
|---|---|---|
| Brookdale | "Out of our 65 offices, we physically move about 10-15% of those locations annually. We need to have a single source of truth be able to cleanly say, 'OK we've made this change, we know it's been brand verified by us and we know it's been changed everywhere'." | none |
| Domino's | "Domino's updates listings and pages for nearly 7,000 local franchise locations in the U.S. with Yext's platform." · "Today, over 98% of Domino's locations are franchise-owned. And with their number one priority being delivering top-tier food and service, many store owners don't have time for marketing initiatives like maintaining online listings." · ""Being able to update information like holiday hours through the Yext platform has been crucial - otherwise we would have to go through multiple vendors, or even update the information manually, which we know can force human error a lot of the time," Morris ex[plained]" | none |
| FedEx | "FedEx uses Yext to improve discoverability and manage the reputation of its 725+ locations throughout Latin America and the Caribbean." | none |
| IHG Hotels & Resorts | "IHG Hotels & Resorts is one of the world's leading hotel companies. They represent some of the most iconic hospitality brands, including Holiday Inn, Intercontinental Hotels & Resorts, and more." | none |
| Fazoli's | no location or AI line captured in the static HTML | none |
| Cox Communications | no location or AI line captured in the static HTML | none |

Engine-name counts per story page: ChatGPT 1, Perplexity 1, Claude 1 on every page — all from the navigation blog link above, none from story text.

## Pull notes — mechanical only

- Every page HTTP 200, no wall. Story bodies are partly script-rendered; the quotes above are what the static HTML carries.
- Samsung story not opened (outside the local / multi-location cut).
- No login, no form.
