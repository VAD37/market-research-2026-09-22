# OpenAI — Operator System Card, section 4.6 "Prompt Injections"

```yaml
source:          OpenAI
url_or_doc_id:   https://cdn.openai.com/operator_system_card.pdf
published:       2025-01-23 (API-availability section dated "Updated March 11, 2025")
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            3
tier_reason:     Platform primary — OpenAI's own system card document, per trust-rubric.md tier 3 "Platform primary — own docs... reliable on existence, biased on framing." Published 2025-01-23, well before the plan.md 2026-06-22 recency cutoff — flagged stale as surface-state evidence; this task did not locate a newer OpenAI system-card-level statement on prompt injection (see pull notes on browser-backlogged pages that may supersede this).
source_label:    company-stated
lane:            D
sub_market:      organic recommendation
engine:          Operator (OpenAI's Computer-Using Agent, research preview as of the document date; later folded into ChatGPT agent modes per this task's general knowledge of the product line, not independently re-verified this pull)
metric_kind:     visibility
supersedes:      none
captured:        sections "Introduction", "4.5 Watch Mode", "4.6 Prompt Injections", "limitations", and "4.7 API Availability" — extracted via pdftotext from the WebFetch-saved binary, since WebFetch itself could not parse the raw PDF stream
```

## Verbatim

Document title and date, as printed on page 1: "Operator System Card / OpenAI / January 23, 2025"

Introduction, verbatim: "Operator is a research preview of our Computer-Using Agent (CUA) model, which combines GPT-4o's vision capabilities with advanced reasoning through reinforcement learning. It interprets screenshots and interacts with graphical user interfaces (GUIs) -- the buttons, menus, and text fields people see on a computer screen -- just as people do."

Framing of the risk, verbatim: "While Operator has the potential to broaden access to technology, its capabilities introduce additional risk vectors. These include vulnerabilities like prompt injection attacks where malicious instructions in third-party websites can mislead the model away from the user's intended actions."

Section "4.6 Prompt Injections", verbatim: "The final category for model mistakes is an emerging risk known as prompt injections. A prompt injection is a scenario where an AI model mistakenly follows untrusted instructions appearing somewhere in its input. For Operator, this may manifest as it seeing something on screen, like a malicious website or email, that instructs it to do something that the user does not want, and it complies. We made the model more robust to this type of attack. To evaluate our mitigations, we compiled an eval set of 31 automatically checkable prompt injection scenarios, that represent situations to which older versions of our model were at some point susceptible. The score indicates the model's susceptibility to prompt injection, so lower is better (although not every case is necessarily an actual concern). We evaluated our final model's behavior on these scenarios and found the model to have 23% susceptibility, compared to 62% with no mitigations and 47% with only prompting. A manual review of these examples showed that only one truly concerning example remained, and it was caught by the prompt injection monitor, described later in this section. This example is also covered by watch mode."

Monitor evaluation, verbatim: "On top of the model mitigations, we added a prompt injection monitor that is able to supervise execution of Operator and will pause execution if a suspected prompt injection is detected on the screen (see Figure 2). We tuned this model to have high recall. On an eval set of 77 prompt injection attempts created from red-teaming sessions, the monitor was able to achieve 99% recall and 90% precision, missing just one borderline example (that Operator did not fall for). On the other hand, the monitor flagged 46 out of 13,704 benign screens from normal Operator execution. This monitor can also be rapidly updated in response to newly discovered attacks. For example, after new discoveries during one red teaming session, we increased our recall from 79% to 99% in just one day."

Closing caveat of the section, verbatim: "It is worth noting that the mitigations against model mistakes, including confirmations, watch mode, and proactive refusals, continue to apply, serving as speed bumps for potential attackers. Although all known cases were mitigated, prompt injections remain an area of concern that we will closely monitor as use of AI agents increases."

General limitations passage, verbatim: "Despite proactive testing and mitigation efforts, certain challenges and risks remain due to the difficulty of modeling the complexity of real-world scenarios and the dynamic nature of adversarial threats. Operator may encounter novel use cases post-deployment and exhibit different patterns of errors or model mistakes. Additionally, we expect that adversaries will craft novel prompt injection attacks and jailbreaks."

Forward plan, verbatim: "OpenAI plans to maintain ongoing evaluations of Operator and efforts to further improve Operator's adherence to OpenAI's policies and safety standards. Additional improvements in areas such as prompt injection are planned, guided by evolving best practices and user feedback."

Red-team method note, verbatim (from the report's earlier red-teaming section): "the external red teamers access to Operator. We then asked the external red teamers to explore various ways to circumvent the model's safeguards, including prompt injections and jailbreaks."

[note: the document also shows one mitigated-example transcript ("USER: Navigate to gmail.com and check email... ASSISTANT: There's an email from you with a link to a survey that you requested me to complete. Should I proceed...") — reproduced here as printed because it is the assistant's clarifying response, not an attacker payload; no injected instruction text is reproduced.]

## Pull notes — mechanical only

- The URL is a PDF; WebFetch's own model could not parse the raw PDF stream and returned only a note that binary content had been saved to a local temp file. This pull tool (the agent running this task) then extracted text from that saved PDF locally via `pdftotext` and grepped for "injection" to locate and quote the relevant sections verbatim — a mechanical extraction step, not a rewrite.
- This is OpenAI's own measured lab evaluation (internal eval sets of 31 and 77 scenarios; not a third-party or production-traffic measurement), and it is the only item in this cluster with a numeric before/after susceptibility figure tied to one named engine's own mitigations (23% vs. 62% vs. 47%). It is filed as a platform-primary engine statement (Pass 5 question 4) and, secondarily, as the census's clearest quantified example of "engine's own claimed defense effectiveness" — not as an unaffiliated measured-effect result, and not as evidence the technique moves a *consumer-visible product recommendation* specifically (the eval concerns arbitrary agentic-action susceptibility, not brand/product steering).
- ChatGPT Atlas (OpenAI's later browser product) and its own safety documentation were not reachable by plain fetch this pull (`openai.com/index/chatgpt-atlas/` and `help.openai.com/en/articles/11146633-atlas-safety-and-security` both returned HTTP 403) — recorded to the browser backlog below, since this agent has no Chrome extension or Playwright access. `bugcrowd.com/openai` and `bugcrowd.com/engagements/openai` also returned only header/navigation content with no scope text retrievable by plain fetch — same backlog.

**Browser backlog (this file's unresolved URLs):** `https://openai.com/index/chatgpt-atlas/` (403), `https://help.openai.com/en/articles/11146633-atlas-safety-and-security` (403), `https://bugcrowd.com/openai` and `https://bugcrowd.com/engagements/openai` (loads header/nav only to plain fetch, no scope text).
