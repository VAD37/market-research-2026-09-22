# UK ASA/CAP — Disclosure of AI in Advertising

```yaml
source:          Advertising Standards Authority (ASA) / Committee of Advertising Practice (CAP)
url_or_doc_id:   https://www.asa.org.uk/news/disclosure-of-ai-in-advertising-striking-the-balance-between-creativity-and-responsibility.html
published:       2025-05-29
pull_date:       2026-09-22
pull_method:     browser extension (also cross-checked via WebFetch, which matched every quote independently extracted)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — regulator's own guidance page (own framing, no third-party verification), not a codified rule or an ASA ruling/adjudication
source_label:    company-stated
lane:            B, D
sub_market:      paid placement
engine:          n/a — general advertising guidance, not engine-specific
metric_kind:     none
supersedes:      none
captured:        the "To disclose or not to disclose?" section (full); the two-question disclosure test (full); the ISBA/IPA industry-principle reference (partial)
```

## Verbatim

### Title, source, date

"Disclosure of AI in Advertising: Striking the Balance Between Creativity and Responsibility
CAP News
29 May 2025"

### "To disclose or not to disclose?" — the core statement of the rule (or its absence)

"Read on for some (human generated) advice on the disclosure of AI in advertising and marketing.

To disclose or not to disclose?

Whilst the CAP and BCAP Codes do not contain AI-specific rules, our existing rules apply regardless of how content is generated, edited, or targeted. Marketers should, therefore, ensure that their use of AI doesn't generate an issue with the existing Codes.

There is no blanket legal requirement in the UK to disclose the use of AI in ads and there are many schools of thought, around the world, on the suitability and effectiveness of regulators insisting on such disclosure in all circumstances. There are, however, varying requirements and rules in other countries, now o[note: truncated at tool output limit — sentence continues, not captured]"

### The two-question disclosure test

"In the absence of ASA precedent, it's important to focus on why there may be a need to be disclose the use of AI. It's easy to get caught up ticking an 'AI disclosure' box without really thinking about what harm you're seeking to address and whether it's effective at addressing that harm.

We recommend you ask yourselves two key questions:

Is the audience likely to be misled if the use of AI is not disclosed? In other words, what's the mischief, if any, that the disclosure is mitigating?

If there is a danger of the audience being misled, is the disclosure clarifying the ad's message or contradicting it?"

### Industry-principle reference (ISBA/IPA)

"...advertisers and agencies should ensure that their use of AI is transparent where it features prominently in an ad and is unlikely to be obvious to consumers." [quoted by ASA/CAP as an industry principle, attributed by the WebFetch cross-check to ISBA and IPA; this attribution was not independently re-confirmed against the page's own text within this pull's tool-output-truncation budget]

## Pull notes — mechanical only

- Page loaded directly via both `WebFetch` and the Chrome extension without any 202/redirect/gating behaviour (unlike eur-lex.europa.eu and ecfr.gov earlier in this cluster); the two methods' extracted quotes matched on every sentence checked.
- Page size (~20,018 characters via `document.body.textContent`) was small enough that no offset-instability was observed across repeated same-tab JS evaluations, unlike the much larger EU legislative pages pulled earlier in this cluster.
- Same tool-output truncation as the rest of this cluster: quotes above are cut at `[note: truncated at tool output limit]` where the JS-execution tool's ~1000-1100 character return cap was hit, rather than filled from memory.
- The explicit statement "There is no blanket legal requirement in the UK to disclose the use of AI in ads" and "In the absence of ASA precedent..." together are this task's clearest answer for the UK jurisdiction: as of this page's 2025-05-29 publication date, and as of this 2026-09-22 pull with no newer ASA/CAP statement found superseding it, the UK has **no** codified, AI-specific ad-disclosure rule — general CAP/BCAP Code misleadingness rules apply instead, and the ASA had (as of the article's own admission) no ruling precedent specifically on AI disclosure to draw a bright line from.
- Individual ASA rulings found by search but not pulled in this session (out of time budget, and each concerns AI-generated *image content* rather than AI-assistant-surfaced paid or sponsored recommendations specifically): "ASA Ruling on Optimize Business Ltd t/a SoulTalk" (`asa.org.uk/rulings/optimize-business-ltd-a26-1334631-optimize-business-ltd.html`) and "Rusto AI-AI Photo Toolbox" (`asa.org.uk/rulings/rusto-ai-ai-photo-toolbox.html`). Also found but not pulled: `asa.org.uk/news/ai-and-deepfakes-four-things-advertisers-need-to-know-before-they-hit-run.html`; `asa.org.uk/news/generative-ai-advertising-decoding-ai-regulation.html`; `asa.org.uk/news/ai-advertising-and-the-policy-landscape-cap-proactive-monitoring.html`; `asa.org.uk/advice-and-resources/research-at-the-asa-and-cap/ai-research-and-practices.html`; a PDF report "AI as a Marketing Term" at `asa.org.uk/static/eb77bee0-a147-49b8-81856c3c83586bf2/AI-as-a-Marketing-Term-Report.pdf`.
- No ASA ruling naming an AI assistant, AI search engine, or AI chatbot specifically surfacing a paid/sponsored recommendation was found or pulled in this session. Recorded as `unknown — checked asa.org.uk news/rulings via WebSearch "site:asa.org.uk AI generated ad ruling chatbot" 2026-09-22` in the summary file.
