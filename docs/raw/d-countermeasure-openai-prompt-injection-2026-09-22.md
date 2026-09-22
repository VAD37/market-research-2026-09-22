# OpenAI — Safety best practices (prompt injection mitigation guidance)

```yaml
source:          OpenAI (developers.openai.com API documentation)
url_or_doc_id:   https://platform.openai.com/docs/guides/safety-best-practices -> resolved 301 to https://developers.openai.com/api/docs/guides/safety-best-practices
published:       undated — no date shown on page
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary, own developer documentation
source_label:    company-stated
lane:            D
sub_market:      organic recommendation
engine:          ChatGPT — OpenAI (page is API/developer-facing guidance for third parties building on OpenAI's models, not a statement about ChatGPT's own consumer-surface defenses)
metric_kind:     none
supersedes:      none
captured:        the prompt-injection passage only, located via targeted fetch prompt; full page not captured verbatim beyond this passage
technique:       prompt injection embedded in indexed content
models_tested:   n/a — guidance page, not a measurement
date_window:     n/a
measured_effect: n/a — no measured attack-success-rate or detection-rate figure stated on this page
vertical:        n/a
```

## Verbatim

Passage located on the page under adversarial-testing guidance, quoted as returned by the fetch tool:

"Can someone easily redirect the feature via prompt injection, e.g. 'ignore the previous instructions and do this instead'?"

Stated mitigation, quoted as returned by the fetch tool:

"Limiting the amount of text a user can input into the prompt helps avoid prompt injection."

The document emphasizes adversarial testing and input constraints as preventive measures against this attack vector.

## Pull notes — mechanical only

- Fetched via WebFetch. The original `platform.openai.com/docs/guides/safety-best-practices` URL returned a 301 redirect to `developers.openai.com/api/docs/guides/safety-best-practices`, which was then fetched directly (200).
- This page addresses prompt injection as a risk to guard against when **building** a product on OpenAI's API (a question a developer should ask themselves: "can someone easily redirect the feature via prompt injection") — it is developer-facing best-practice guidance, not a statement of what ChatGPT's own consumer-facing product does to detect or block prompt injection in content it retrieves from the web. This scope distinction is load-bearing for the census cell and is not resolved by this pull alone.
- No numeric detection rate, block rate, or attack-success-rate figure appears in the captured passage — contrast with Anthropic's and Microsoft's countermeasure pulls in this cluster, which do carry such figures.
- `unknown — checked` on this pull: whether ChatGPT Atlas (the browsing/agentic surface) applies a distinct, consumer-surface prompt-injection classifier of its own — `help.openai.com/en/articles/11146633-atlas-security-and-privacy-faq` returned HTTP 403 to plain fetch this task (channels.md's `403→ext` expectation for `help.openai.com` held); `openai.com/index/prompt-injections/` also returned HTTP 403 to plain fetch. Both routed to the browser backlog (this task is fetch-only, no Chrome extension).
