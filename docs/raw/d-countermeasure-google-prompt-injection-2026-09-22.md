# Google — "Google's Defense Against Indirect Prompt Injection Attacks" (Gemini)

```yaml
source:          Google (Google Security Blog)
url_or_doc_id:   https://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html -> resolved 301 to https://blog.google/security/mitigating-prompt-injection-attacks/
published:       2025-06-13
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary, own security blog; stale — published 2025-06-13, before 2026-06-22, per query-book.md date rule. Re-checked: no newer Google post superseding this one's defense-layer description was found in this task's search
source_label:    company-stated
lane:            D
sub_market:      organic recommendation
engine:          Google — Gemini (Workspace-integrated context: email, documents, calendar; page does not scope itself to AI Overviews/AI Mode web-citation content specifically)
metric_kind:     none
supersedes:      none
captured:        definition and five-layer defense description, as returned by the fetch tool
technique:       prompt injection embedded in indexed content
models_tested:   Gemini (no version number named on this page)
date_window:     n/a — descriptive post, not a dated experiment
measured_effect: no — the post describes defense mechanisms, not a quantified attack-success-rate or detection-rate figure
vertical:        n/a
```

## Verbatim

Definition, quoted as returned by the fetch tool:

"Indirect prompt injections involve hidden malicious instructions within external data sources. These may include emails, documents, or calendar invites that instruct AI to exfiltrate user data or execute other rogue actions."

Five stated defense layers, quoted as returned by the fetch tool:

1. **Prompt Injection Content Classifiers** — "content classifiers filter out harmful data containing malicious instructions" when users query Workspace data; example given: a Gmail message with harmful directives is detected and disregarded before a response is generated.
2. **Security Thought Reinforcement** — adds "targeted security instructions surrounding the prompt content to remind the large language model (LLM) to perform the user-directed task and ignore any adversarial instructions."
3. **Markdown Sanitization and Suspicious URL Redaction** — the system "identifies external image URLs and will not render them" and uses Google Safe Browsing to detect unsafe links, replacing them with "suspicious link removed" notifications.
4. **User Confirmation Framework** — Gemini implements "Human-In-The-Loop (HITL)" requiring user confirmation before risky operations, such as calendar event deletion.
5. **End-User Security Notifications** — when a mitigation triggers, users receive "contextual information allowing them to learn more via dedicated help center articles."

## Pull notes — mechanical only

- Fetched via WebFetch. The original `security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html` URL returned a verified 301 redirect (server-supplied `Location` header) to `blog.google/security/mitigating-prompt-injection-attacks/`, which was then fetched directly (200).
- `stale — published 2025-06-13`, more than one quarter before this pull date, per `query-book.md`'s date rule. Not re-checked against a newer live page beyond the search attempts noted below, since this task's remit is the countermeasure check, not a fresh Pass-2-style platform-primary sweep; recorded as the most specific dated Google statement on this technique found this task.
- This post's examples (Gmail, calendar invites, documents) describe Gemini's Workspace-assistant context, not explicitly the AI Overviews/AI Mode web-answer-generation path that this repo's Lane D is centered on. Whether the same five-layer defense (or any of it) applies to content retrieved from the open web and surfaced in an AI Overview or AI Mode answer is `unknown — checked developers.google.com/search/docs/appearance/ai-features (a-google-ai-features-guidance-2026-09-22.md, already in raw, no prompt-injection language found on that page) 2026-09-22`.
- No numeric detection-rate or attack-success-rate figure is given in this post — contrast with Anthropic's and Microsoft's countermeasure pulls in this cluster, both of which carry stated figures.
