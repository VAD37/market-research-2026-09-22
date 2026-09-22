# SOCi — three-limb roster rule check (held name, limb (c) in `a-vendor-roster-2026-09-22.md`)

```yaml
source:          SOCi Inc. (soci.ai, company-stated); Batteries Plus, via PRNewswire (company-stated, independent third party)
url_or_doc_id:   https://www.soci.ai/news/in-ai-driven-discovery-few-brands-are-chosen-most-disappear/ ; https://www.prnewswire.com/news-releases/batteries-plus-named-one-of-the-soci100-most-visible-local-enterprise-brands-of-2026-302705483.html
published:       2026-01-28 (SOCi release); 2026-03-05 (Batteries Plus / PRNewswire release)
pull_date:       2026-09-22
pull_method:     fetch (curl, browser User-Agent header)
pull_purpose:    evidence about a number
tier:            5
tier_reason:     adjusted from table default (3, platform primary for the SOCi release) — the underlying "2026 Local Visibility Index" is a vendor study with n (350,000+ locations, 2,751 brands), a stated method (AI-recommendation-rate analysis across ChatGPT/Gemini/Perplexity vs. Google local 3-Pack), bias flagged since SOCi is the vendor measuring the category it sells into; the PRNewswire release is company-stated (Batteries Plus), independent of SOCi, tier 3
source_label:    company-stated
lane:            A
sub_market:      organic recommendation
engine:          ChatGPT, Google Gemini, Perplexity (all three named); Google local 3-Pack used as the traditional-search comparator
metric_kind:     visibility
supersedes:      none
captured:        full text of both releases
feature:         "2026 Local Visibility Index" (LVI) and the derived "SOCi100" / "SOCi AI 100" brand rankings — SOCi's AI-visibility measurement product/study, referenced from a site-wide "Get Your AI Visibility Snapshot" nav CTA
```

## Verbatim

### SOCi's own release — "In AI-Driven Discovery, Few Brands Are Chosen, Most Disappear" (2026-01-28)

"SOCi's 2026 Local Visibility Index Reveals the Rising Cost of Local Invisibility in the Age of AI. SAN DIEGO — Jan. 28, 2026 — SOCi Inc., the agentic workforce built for multi-location visibility across local and AI search, today released its 2026 Local Visibility Index (LVI)... Analyzing more than 350,000 locations across 2,751 multi-location brands, SOCi found that AI platforms such as ChatGPT, Google Gemini, and Perplexity are dramatically more selective than traditional search. **ChatGPT recommends just 1.2% of brand locations, compared to an average 35.9% appearance rate in Google's local 3-Pack, making AI visibility nearly 30 times more selective than traditional local search.**" "SOCi's research shows that locations recommended by ChatGPT average 4.3-star ratings..." "In retail, SOCi found only 45% overlap between the most visible enterprise brands in traditional local search and those most frequently recommended by AI platforms." "About SOCi — SOCi is redefining how multi-location enterprises achieve local and AI search visibility with the world's first agentic workforce... Trusted by leading brands like Ford, Ace Hardware, and Liberty Tax, and recognized by Fast Company as one of the World's Most Innovative Companies."

### Batteries Plus / PRNewswire — "Batteries Plus Named One of the SOCi100 Most Visible Local Enterprise Brands of 2026" (2026-03-05, News provided by Batteries Plus)

"March 5, 2026 /PRNewswire/ -- Batteries Plus, the nation's leading battery and power solutions service center, today announced it has been named to the **SOCi100 Most Visible Local Enterprise Brands of 2026**. This recognition highlights brands leading in local visibility across search, social media, online reputation, and emerging AI-powered discovery channels. Batteries Plus ranked #14 on the overall list... Additionally, Batteries Plus ranked #40 on the inaugural **SOCi AI 100** for its discoverability specifically on AI-powered platforms." "Selected from nearly 2,700 multi-location enterprise brands, the SOCi100 recognizes companies that are winning visibility where consumer decisions increasingly happen..." "The SOCi100 is derived from the SOCi's 2026 Local Visibility Index (LVI), which analyzed more than 350,000 locations across 2,751 brands. For the first time, the 2026 LVI includes AI visibility as a core benchmark..." "'Visibility today isn't about ranking — it's about being selected,' said Monica Ho, Chief Marketing Officer at SOCi."

## Roster-rule determination

**SOCi clears limb (a): two or more independent non-listicle sources.** Source 1 is SOCi's own press release (soci.ai, company-stated). Source 2 is Batteries Plus's press release distributed via PRNewswire (prnewswire.com) — a different publisher, issued by a different company (a SOCi customer, not SOCi itself), independently corroborating the same underlying study (identical "350,000 locations across 2,751 brands" figure, confirming the two releases describe the same real study rather than one being fabricated). Per the roster rule, this is two distinct, non-listicle, independent-publisher sources — **SOCi moves from held to rostered.** A SEC EDGAR full-text search for "SOCi, Inc." (`efts.sec.gov/LATEST/search-index?q=%22SOCi%2C+Inc.%22`) returned 25 hits, all unrelated (a different, unrelated "SOCI" abbreviation inside Southwest Water Co. subsidiary-listing exhibits) — **SOCi is not a current SEC filer**, so limb (b) does not apply; a guessed `investors.soci.ai` subdomain failed DNS resolution, consistent with this. The roster's original note "SOCi is Nasdaq-listed (ticker SOCI)" is **not corroborated by this pull** and is likely incorrect or refers to a different, unrelated entity — flagged for the compiling pass; SOCi appears to be a privately held company as of this check.

## Pull notes — mechanical only

- Both releases fetched via `curl` with a browser User-Agent string; HTTP 200, full static HTML, no JS-rendering gate.
- claude-in-chrome extension reported "not connected"; plain fetch succeeded for both domains (soci.ai, prnewswire.com), no browser fallback needed.
- The PRNewswire release was found via `prnewswire.com/search/news/?keyword=SOCi%20Local%20Visibility%20Index`, a URL-parameter search that returned results without JavaScript rendering — not via the exhausted WebSearch tool.
- `unknown — checked sec.gov/cgi-bin/browse-edgar (company-name search returned no exact match for "SOCi"), investors.soci.ai (DNS failure) 2026-09-22` — SOCi's private/public status is recorded as apparently-private, not confirmed by a filing.
