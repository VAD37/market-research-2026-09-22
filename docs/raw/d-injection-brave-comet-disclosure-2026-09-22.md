# Brave — prompt injection vulnerability disclosure against Perplexity's Comet browser

```yaml
source:          Brave (brave.com/blog)
url_or_doc_id:   https://brave.com/blog/comet-prompt-injection/
published:       2025-08-20
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            4
tier_reason:     Named security researchers, a working proof-of-concept, and a dated disclosure timeline are published (method disclosed) — closest fit is trust-rubric.md's "Panel, clickstream, infrastructure telemetry... usable if method published" tier band. Bias flagged: Brave is a competing browser vendor with a commercial interest in portraying a rival agentic browser (Perplexity's Comet) as insecure; this is a third-party security disclosure about another company's product, not the affected vendor's own report. Published 2025-08-20, before the plan.md 2026-06-22 recency cutoff — flagged stale as surface-state evidence and re-checked below via the pull method, not re-dated.
source_label:    company-stated
lane:            D
sub_market:      organic recommendation
engine:          Perplexity Comet (browser agent), priority-2 engine per plan.md engine matrix
metric_kind:     none
supersedes:      none
captured:        section "abstract-equivalent summary" via WebFetch verbatim/quote-extraction prompt against the Brave blog post
```

## Verbatim

Publication date, as extracted: August 20, 2025.

Vulnerability mechanism, quoted: "Comet feeds a part of the webpage directly to its LLM without distinguishing between the user's instructions and untrusted content from the webpage."

Demonstration surface, as extracted: the vulnerability was demonstrated via a Reddit post containing a comment with injection instructions hidden behind a spoiler tag.

Triggered actions, as extracted: the injected prompt commanded the AI to extract the user's email address, log into the user's Perplexity account using a spoofed domain, retrieve a one-time password from Gmail, and exfiltrate both credentials by replying to the Reddit comment.

Disclosure timeline, as extracted:
- July 25, 2025: vulnerability discovered and reported
- July 27, 2025: Perplexity acknowledged and implemented an initial fix
- July 28, 2025: researchers found the fix incomplete
- August 11, 2025: one-week public disclosure notice sent
- August 13, 2025: testing suggested patching was complete
- August 20, 2025: public disclosure, with a note that further testing revealed the vulnerability persisted

Perplexity's own statement: none was found in the article by this pull.

[note: no injected-prompt string is reproduced here — the extraction above describes the demonstrated actions (email extraction, spoofed-domain login, OTP exfiltration) without printing the hidden instruction text itself.]

## Pull notes — mechanical only

- Fetched via WebFetch against `brave.com/blog/comet-prompt-injection/`, a URL reconstructed for this pull rather than obtained from a search index (WebSearch budget exhausted per task instruction); the fetch succeeded without a 403, so no browser-extension fallback was needed for this source.
- The fetch tool's own summary characterized the demonstration surface as "researcher-controlled" rather than a live public attack, but the source text as extracted does not itself state whether the Reddit post was newly created by the researchers or an existing public post — recorded as `unknown — checked this pull only 2026-09-22, not independently resolved`. Either way this is a real, currently-shipping consumer product (Perplexity Comet) being driven to take unintended actions by content on a real-world page type (a Reddit comment), which is the setting distinction the census records it under: **in-the-wild-style security disclosure against a consumer surface**, as opposed to a paper's self-built lab harness.
- This disclosure demonstrates data exfiltration and account compromise, not brand/product-recommendation steering specifically — it is filed under Pass 5 question (2) ("who is documented doing it... security disclosures... researcher audits of live pages") and question (3) ("setting: in-the-wild / consumer-surface lab"), not under a measured product-recommendation shift.
