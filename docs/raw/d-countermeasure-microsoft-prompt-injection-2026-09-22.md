# Microsoft — Azure AI Content Safety: Prompt Shields (document / indirect prompt injection)

```yaml
source:          Microsoft (Microsoft Learn — Azure AI Content Safety documentation)
url_or_doc_id:   https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection
published:       ms.date (page metadata) 2026-08-28; updated_at (page metadata) 2026-09-18
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary, own product documentation
source_label:    company-stated
lane:            D
sub_market:      organic recommendation
engine:          Microsoft Copilot (priority-2) — page documents Prompt Shields, a shared Azure AI Foundry / Content Safety guardrail feature; the page itself is written for the Foundry/Content-Safety product surface, not a Copilot-branded page. Whether Copilot's own consumer chat surface uses this exact feature is not stated on this page (see pull notes)
metric_kind:     none
supersedes:      none
captured:        full page as returned by the fetch tool (front-matter metadata, body text, attack-type tables, configuration and troubleshooting sections)
technique:       prompt injection embedded in indexed content
models_tested:   n/a — this is a guardrail/classifier product applied in front of a deployed model, not a paper measuring specific target LLMs
date_window:     n/a
measured_effect: no numeric detection-rate or attack-success-rate figure stated on this page (the page documents feature mechanics, examples, and configuration, not a benchmark result)
vertical:        n/a
```

## Verbatim

Page front-matter (captured verbatim, includes real dates):

"description: Learn about User Prompt injection attacks and document attacks and how to prevent them with the Prompt Shields feature."
"ms.date: 2026-08-28T00:00:00.0000000Z"
"updated_at: 2026-09-18T22:15:00.0000000Z"

Definition, quoted as returned by the fetch tool:

"Prompt Shields detects and blocks adversarial inputs to large language models (LLMs). It analyzes user prompts and documents before content is generated to help prevent harmful, unsafe, or policy-violating output."

Two attack types named, quoted as returned by the fetch tool:

"**User prompt attacks** are malicious prompts that attempt to bypass system instructions or safety training... **Document attacks** are hidden instructions in third-party content, such as documents, emails, and web pages, that attempt to take control of the model session."

Comparison table (document attacks row, quoted as returned by the fetch tool):

| Type | Attacker | Entry point | Method | Objective or impact | Resulting behavior |
|---|---|---|---|---|---|
| Document attacks | Third party | Third-party content, such as documents and emails | Causes the model to misinterpret third-party content as instructions | Gain unauthorized access or control | Execute unintended commands or actions |

Document-attack subtype naming closest to on-page content manipulation, quoted as returned by the fetch tool:

"**Manipulated content** | Commands to falsify, hide, manipulate, or promote specific information."

Stated action mechanism, quoted as returned by the fetch tool:

"The annotations for a request contain `detected` and `filtered` Boolean values" — i.e., the system can detect an attack without necessarily filtering/blocking it, depending on configuration (block vs. annotate mode, per the Troubleshooting section: "Adjust from **block** to **annotate** mode to log without filtering").

Additional defense layer, "Spotlighting (preview)," quoted as returned by the fetch tool:

"Spotlighting tags input documents with special formatting that identifies them as lower-trust content. The service transforms the document content by using base64 encoding, and the model treats it as less trustworthy than direct user and system prompts."

## Pull notes — mechanical only

- Fetched via WebFetch, 200. Page metadata (front-matter YAML) was returned along with body content; the two real dates above (`ms.date`, `updated_at`) are taken directly from that metadata, not inferred.
- **Engine-attribution caveat, load-bearing:** this page documents Prompt Shields as a feature of Azure AI Content Safety / Azure AI Foundry — Microsoft's cross-product AI-safety infrastructure layer — not a page branded to or scoped specifically to Microsoft Copilot or Bing Chat. This repo's own already-landed Pass 2 pulls (`docs/raw/b-microsoft-copilot-advertising-platform-2026-09-22.md`, `docs/raw/b-microsoft-amazon-platform-summary-2026-09-22.md`) were not re-checked in this pull for an explicit statement that Copilot's consumer surface runs on this exact guardrail; recorded as `unknown — checked learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection only for this specific linkage 2026-09-22`. The census records this as Microsoft's own primary document naming and describing document/indirect prompt injection defenses, with this scope caveat carried forward rather than resolved.
- `learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/prompt-injection-content-safety` (a guessed, more Copilot-specific URL) returned HTTP 404 and was not found by another route this pull.
- `www.bing.com/webmasters/help/webmaster-guidelines-30fba23a` and `learn.microsoft.com/en-us/bingwebmaster/webmaster-guidelines-30fba23a` were both attempted for Bing's general spam/content guidelines (relevant to techniques other than prompt injection) and both failed — the first returned only a page-title shell (client-side-rendered app, no server-rendered body reachable by plain fetch), the second 404. Both routed to the browser backlog (see census).
