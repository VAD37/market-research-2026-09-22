# Anthropic — Computer use documentation, prompt injection risk section

```yaml
source:          Anthropic (platform.claude.com docs, redirected from docs.anthropic.com)
url_or_doc_id:   https://platform.claude.com/docs/en/docs/agents-and-tools/computer-use (redirected from https://docs.anthropic.com/en/docs/agents-and-tools/computer-use)
published:       undated — no date on page
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            3
tier_reason:     Platform primary — Anthropic's own product documentation, per trust-rubric.md tier 3 "Platform primary — own docs, changelog, pricing page... reliable on existence, biased on framing." No page date is shown, so the plan.md staleness flag cannot be dated; recorded as undated rather than assumed current.
source_label:    company-stated
lane:            D
sub_market:      organic recommendation
engine:          Claude (computer use / agentic tool-use surface) — priority-1 engine per plan.md engine matrix
metric_kind:     none
supersedes:      none
captured:        section on prompt injection risk and mitigations, via WebFetch verbatim-extraction prompt against the redirected docs page
```

## Verbatim

Risk description, quoted: "In some circumstances, Claude will follow commands found in content even when they conflict with your instructions. For example, instructions on webpages or contained in images might override your instructions or cause Claude to make mistakes."

Model-level defense, quoted: "Anthropic has trained the model to resist these prompt injections and has added an extra layer of defense. If you use the computer use tools, classifiers will automatically scan what the tools return, such as screenshots, to flag potential prompt injections. When these classifiers identify a potential prompt injection, they will automatically steer the model to check whether the instruction really came from you before acting on it."

Opt-out caveat, quoted: "This extra protection won't be ideal for every use case (for example, use cases without a human in the loop), so if you'd like to opt out and turn it off, contact support. The precautions above remain important even with these classifiers in place."

Operator-level precautions recommended, quoted: (1) "Using a dedicated virtual machine or container with minimal privileges to prevent direct system attacks or accidents"; (2) "Avoiding giving the model access to sensitive data, such as account login information, to prevent information theft"; (3) "Limiting internet access to an allowlist of domains to reduce exposure to malicious content"; (4) "Asking a human to confirm decisions that might result in meaningful real-world consequences and any tasks requiring affirmative consent, such as accepting cookies, completing financial transactions, or agreeing to terms of service."

User-notification requirement, quoted: "Inform end users of relevant risks and obtain their consent prior to enabling computer use in your own products."

## Pull notes — mechanical only

- Original URL requested was `docs.anthropic.com/en/docs/agents-and-tools/computer-use`; the fetch tool reported a 301 redirect to `platform.claude.com/docs/en/docs/agents-and-tools/computer-use`, which was then fetched directly and is the URL recorded above.
- No update or publication date is shown on the page as fetched; this is recorded as `undated — no date on page` per the raw-pull template rather than assumed to be within the recency window.
- This documentation names classifier-based detection plus a set of deployer-side operational precautions (VM isolation, domain allowlisting, human confirmation for consequential actions), but states no measured detection rate, false-positive rate, or attack-success figure — contrast with the OpenAI Operator system card pulled alongside it in this cluster, which does report such numbers for its own monitor.
- Separately, `www.anthropic.com/responsible-disclosure-policy` (last updated 2025-02-14) was checked for whether prompt injection is named in the bug-bounty scope: it is not named explicitly in scope or exclusions; the policy states only "We welcome reports concerning safety issues, 'jailbreaks,' and similar concerns" routed to a dedicated email rather than the standard vulnerability-submission process. `hackerone.com/anthropic-vdp` returned HTTP 403 to plain fetch — browser backlog.

**Browser backlog (this file's unresolved URL):** `https://hackerone.com/anthropic-vdp` (403).
