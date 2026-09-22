# Schema.org — About page (mechanism, origin, governance)

```yaml
source:          Schema.org
url_or_doc_id:   https://schema.org/docs/about.html
published:       undated on this page — continuously maintained; page notes it is "viewing the development version of Schema.org"
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary, the vocabulary's own governance page
source_label:    company-stated
lane:            D
sub_market:      organic recommendation
engine:          n/a — the artefact spec itself, not engine-specific; founding companies named below
metric_kind:     none
supersedes:      none
captured:        full page
```

## Verbatim

Page meta description: "Schema.org is a set of extensible schemas that enables webmasters to embed structured data on their web pages for use by search engines and other applications."

"Note: You are viewing the development version of Schema.org. See how we work for more details."

### About Schema.org

"Schema.org is a collaborative, community activity with a mission to create, maintain, and promote schemas for structured data on the Internet. In addition to people from the founding companies (Google, Microsoft, Yahoo and Yandex), there is substantial participation by the larger Web community, through public mailing lists such as public-vocabs@w3.org and through GitHub. See the releases page for more details, and the FAQ for supporting information."

"Since April 2015, the W3C Schema.org Community Group is the main forum for schema collaboration, and provides the public-schemaorg@w3.org mailing list for discussions. Schema.org issues are tracked on GitHub."

"The day to day operations of Schema.org, including decisions regarding the schema, are handled by a steering group, which includes representatives of the founding companies, a representative of the W3C and a small number of individuals who have contributed substantially to Schema.org. Discussions of the steering group are public."

### People (selected, roles bearing on which companies actually consume the vocabulary)

- "Dan Brickley runs the daily operations for schema.org. He is on the steering group and Google's representative."
- "Jason Douglas coordinates the integration of schema.org into Google's search products."
- "R.V.Guha of Google initiated schema.org and is one of its co-founders. He currently heads the steering group."
- "Vicki Tardif of Google has worked on vocabularies for a lot of major topics on Schema.org. Together with Dan Brickley, she serves on the steering group and takes care of much of the day to day running of schema.org."
- "Martin Hepp, author of GoodRelations has worked closely with the community to integrate GoodRelations into schema.org. He served on the steering group 2014-2017."
- "Steve Macbeth is one of the co-founders of schema.org and serves as Microsoft's executive sponsor."
- "Peter Mika led Yahoo's involvement in schema.org from 2011 to 2016."
- "Alex Shubin has led Yandex's involvement in schema.org since 2011."
- "Aneesh Chopra, as Whitehouse CTO helped create and promote the Job Postings vocabulary."

## Pull notes — mechanical only

- Loaded via `curl`; static HTML, no login gate, no JS rendering wall.
- Page is explicitly labelled a "development version" with no separate dated "stable" snapshot linked from this page itself.
- This page establishes mechanism and governance only — origin (Google, Microsoft, Yahoo, Yandex as founding companies), current operating structure (W3C Community Group since 2015), and that Google's own search-product integration is coordinated by a named Google steering-group member (Jason Douglas, Vicki Tardif). It carries no adoption figures, no per-engine reading statement, and no product-feed-specific detail — those are covered by the already-landed Merchant Center pulls (`c-google-merchant-conversational-attributes-2026-09-22.md`, `c-google-merchant-native-commerce-2026-09-22.md`) and by `d-structured-google-ai-optimization-guide-2026-09-22.md` for Google's explicit statement on whether extra schema.org markup is required for AI features.
- No mention of ChatGPT, Claude, Perplexity, Copilot, or Amazon anywhere on this page — schema.org's founding-company list (Google, Microsoft, Yahoo, Yandex) predates the AI-assistant category by roughly a decade; no AI-lab-specific consumption statement is made here, only "search engines and other applications" generically in the meta description.
