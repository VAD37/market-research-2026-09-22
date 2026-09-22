# Google — "Mitigating prompt injection attacks" (Google Security blog)

```yaml
source:          Google (blog.google/security, mirrored from security.googleblog.com which 301-redirects to this URL)
url_or_doc_id:   https://blog.google/security/mitigating-prompt-injection-attacks/
published:       2025-06-13
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            3
tier_reason:     Platform primary — Google's own security blog, per trust-rubric.md tier 3 "Platform primary — own docs, changelog... reliable on existence, biased on framing." Published 2025-06-13, before the plan.md 2026-06-22 recency cutoff — flagged stale as surface-state evidence; this pull did not locate a newer Google statement specifically on indirect prompt injection.
source_label:    company-stated
lane:            D
sub_market:      organic recommendation
engine:          Gemini (including Gemini in Google Workspace and the Gemini app) — priority-1 engine per plan.md engine matrix
metric_kind:     none
supersedes:      none
captured:        full page, via WebFetch verbatim-extraction prompt (301 redirect from security.googleblog.com followed to blog.google)
```

## Verbatim

Products named, as extracted: Gemini, including "Gemini in Google Workspace and the Gemini app."

Mechanism, quoted: "Indirect prompt injections involve hidden malicious instructions within external data sources. These may include emails, documents, or calendar invites that instruct AI to exfiltrate user data or execute other rogue actions."

Layer 1, quoted: Prompt Injection Content Classifiers — "detect malicious prompts and instructions within various formats, such as emails and files," to filter harmful data.

Layer 2, quoted: Security Thought Reinforcement — adds "targeted security instructions surrounding the prompt content to remind the large language model (LLM) to perform the user-directed task and ignore any adversarial instructions."

Layer 3, quoted: Markdown Sanitization and URL Redaction — the system "will not render" external image URLs and uses "suspicious URL detection based on Google Safe Browsing" to redact unsafe links.

Layer 4, quoted: User Confirmation Framework — requires explicit user approval "for certain actions" such as deleting calendar events, "to prevent undetected or immediate execution."

Layer 5, quoted: End-User Security Notifications — when defenses activate, users receive "contextual information allowing them to learn more via dedicated help center articles."

## Pull notes — mechanical only

- Original URL requested was `security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html`; the fetch tool reported a 301 redirect to `blog.google/security/mitigating-prompt-injection-attacks/`, which was then fetched directly and is the URL recorded above.
- This post names a five-layer defense architecture but does not state measured attack-success or false-positive/recall numbers for any layer (contrast with the OpenAI Operator system card pulled alongside it in this cluster, which does report such numbers) — recorded as a gap, not filled by inference.
- The post addresses indirect prompt injection generally (data exfiltration, rogue actions from emails/documents/calendar invites); it does not name product-recommendation or brand-steering outcomes specifically, and does not name AI Overviews, AI Mode, or Search directly — only Gemini and Gemini in Workspace. This is recorded as a scope limit on what this source can support for the engine-statement table.
