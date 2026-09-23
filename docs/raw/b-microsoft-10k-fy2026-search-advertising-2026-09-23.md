# Microsoft Corp. — Form 10-K FY2026: Search advertising (formerly Search and news advertising) revenue, dollar row

```yaml
source:          Microsoft Corporation, CIK 0000789019 — Form 10-K, fiscal year ended 2026-06-30
url_or_doc_id:   https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm (accession 0001193125-26-323660)
published:       2026-07-29 (EDGAR file_date)
pull_date:       2026-09-23
pull_method:     fetch (curl, sec.gov Archives, contact User-Agent; HTML stripped to text; lines matched by pattern; the revenue-by-product table reassembled from nested cells)
pull_purpose:    evidence about a number
tier:            2
tier_reason:     table default — SEC filing
source_label:    filed
lane:            B (search-ad baseline beyond Google), E (Pass 16 c1)
sub_market:      paid placement (baseline market the AI surfaces draw from)
engine:          Microsoft — Bing, Copilot
metric_kind:     sales (revenue, USD millions)
supersedes:      none — same-day pull `b-sec-microsoft-10k-2026-07-29-2026-09-23.md` (other agent) captured Item 7 growth rates only; this pull adds the Note 18 dollar row, the KPI definition and the product-family definition
captured:        Note 18 table row "Search advertising"; Item 7 KPI definition; Item 1 product-family sentences; MD&A sentences
```

## Verbatim

Product-family definition (Item 1, repeated in Note 18):
> "Search advertising (formerly Search and news advertising), comprising Bing, Copilot, Microsoft News, Microsoft Edge, and third-party affiliates."

> "Our Search advertising business is designed to deliver relevant search, native, and display advertising to a global audience. Microsoft Copilot is a digital companion designed to inform, entertain, and inspire. Our Microsoft Edge browser and Bing search engine with Copilot are key tools to enable user acquisition and engagement, while our technology platform enables accelerated delivery of digital advertising solutions. In addition to first-party tools, we have several partnerships with companies through which we provide and monetize search offerings. Growth depends on our ability to attract new users, understand intent, and match intent with relevant content on advertising offerings."

Note 18 — "Revenue, classified by significant product and service offerings, was as follows:" (In millions), Year Ended June 30 — columns 2026, 2025, 2024, as reassembled:
- "Search advertising 15,176 13,878 12,306"
- adjacent rows for scale: "LinkedIn 19,817 17,812 16,372"; "XBOX 21,790 23,455 21,503"; "Server products and cloud services $ 129,425 $ 98,435 $ 79,828"

Key metric definition (Item 7, More Personal Computing):
> "Search advertising revenue (ex TAC) growth — Revenue from search advertising excluding traffic acquisition costs ("TAC") paid to Bing Ads network publishers and content partners"

Item 7:
> "Search advertising (formerly Search and news advertising) revenue excluding traffic acquisition costs increased 12%."
> "Search advertising revenue increased $1.3 billion or 9%. Search advertising revenue excluding traffic acquisition costs increased 12% driven by higher search volume and revenue per search, as well as benefit from third-party partnerships."
> "More Personal Computing revenue decreased driven by XBOX (formerly Gaming), offset in part by growth in Search advertising."

[note: no Copilot-specific advertising revenue figure appears in the matched text; Copilot is named only inside the Search advertising product family]

## Pull notes — mechanical only

- EDGAR full-text search for "Search and news advertising", forms 10-K, 2026-01-01 to 2026-09-23, returned 1 hit (this filing). Filing index via browse-edgar atom feed; HTTP 200, 8,585,611 bytes.
- The Note 18 table renders one cell per line in the stripped text; the row above was reassembled by joining lines in order. Column header reads "2026 2025 2024".
