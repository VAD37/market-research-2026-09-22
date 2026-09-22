# Anthropic — "Use Claude in Chrome safely" (prompt injection detection and action)

```yaml
source:          Anthropic (support.claude.com Help Center)
url_or_doc_id:   https://support.claude.com/en/articles/12902428-use-claude-in-chrome-safely
published:       "Last Updated: August 12, 2026" (per page's own timestamp)
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary, own Help Center documentation
source_label:    company-stated
lane:            D
sub_market:      organic recommendation
engine:          Claude — Anthropic (Claude in Chrome, an agentic browser-use surface; page states testing was against "Claude Opus 4.8")
metric_kind:     none
supersedes:      none
captured:        the prompt-injection definition, detection-method, response, and measured-robustness passages, as returned by the fetch tool
technique:       prompt injection embedded in indexed content
models_tested:   Claude Opus 4.8 (named on the page as the model behind the stated robustness figure); prior models referenced comparatively but not named
date_window:     n/a — the page states a last-updated date (2026-08-12), not a test-run date window
measured_effect: yes — "less than 0.08% against our internal testing" attack success rate for Claude Opus 4.8, stated as an improvement over "previous models" (unnamed)
vertical:        n/a
```

## Verbatim

Definition, quoted as returned by the fetch tool:

"Malicious instructions hidden in web content (websites, emails, documents) could trick Claude into taking unintended actions" — the page's framing of what prompt injection is, in the context of Claude in Chrome.

Detection method, quoted as returned by the fetch tool:

"One checks incoming content for injection attempts, and another checks every action Claude takes before it runs" — two automatic classifiers.

Response on detection, quoted as returned by the fetch tool:

"Actions are either blocked or paused for your approval when a classifier flags a risk."

Additional stated layers, quoted as returned by the fetch tool:

- Model training using reinforcement learning to recognize malicious instructions
- Content scanning of "all untrusted content entering Claude's context"
- Automatic action screening that "blocks or stops for anything that looks unsafe"

Measured robustness, quoted as returned by the fetch tool:

"Claude Opus 4.8 demonstrates significantly stronger prompt injection robustness than previous models," with attack success rates reduced to "less than 0.08% against our internal testing."

The fetch tool notes human review is not described as the standard response; instead, "users are prompted to approve flagged actions" when a classifier pauses an action.

## Pull notes — mechanical only

- Fetched via WebFetch, 200, no login gate.
- "Against our internal testing" is Anthropic's own, undisclosed test method and dataset — this is a company-stated, self-measured figure (source_label: company-stated), not an independently measured or published-method result; it does not carry the weight of a tier-1-to-3 measured evidence row under `trust-rubric.md`'s "vendor measuring what it sells" caution, though it is not excluded — recorded and bias-flagged here per that rubric's instruction to pull and flag rather than discard.
- This page's scope is **Claude in Chrome** (an agentic browser-automation product where Claude reads and acts on live web pages), not Claude's core chat-answer generation or citation behavior. It is the closest Anthropic primary document found this task naming prompt injection with a detection method and a stated action; whether an equivalent classifier applies to Claude's web-search/citation path outside the Chrome extension is `unknown — checked support.claude.com search results for "prompt injection" 2026-09-22`, which surfaced nine other articles (Claude Cowork, Claude in Chrome permissions guide, file creation/editing, Compliance API, troubleshooting) all describing the same family of Chrome/Cowork/computer-use classifiers, none naming the core chat/citation path specifically.
- Located via `support.claude.com/en/search?q=prompt+injection` (help-centre search endpoint, per this task's allowed-tools list), then fetched directly by its resolved article URL.
