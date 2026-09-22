# Microsoft — Copilot Bounty Program, prompt injection scope clause

```yaml
source:          Microsoft (Microsoft Security Response Center, msrc.microsoft.com)
url_or_doc_id:   https://www.microsoft.com/en-us/msrc/bounty-ai
published:       "Getting Started" section shows "Last Updated: April 7, 2026"
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            3
tier_reason:     Platform primary — Microsoft's own bug-bounty scope page, per trust-rubric.md tier 3 "Platform primary — own docs... reliable on existence, biased on framing." Last updated 2026-04-07, before the plan.md 2026-06-22 recency cutoff — flagged stale as surface-state evidence.
source_label:    company-stated
lane:            D
sub_market:      organic recommendation
engine:          Microsoft Copilot (copilot.microsoft.com, copilot.ai, Microsoft Edge, iOS/Android apps, Windows OS integration, WhatsApp/Telegram) — priority-2 engine per plan.md engine matrix
metric_kind:     none
supersedes:      none
captured:        section "out-of-scope submissions and vulnerabilities" plus program scope/award table, via WebFetch verbatim-extraction prompt
```

## Verbatim

Program name, as extracted: Microsoft Copilot Bounty Program.

Eligible products, as extracted: Copilot experiences on copilot.microsoft.com, copilot.ai, Microsoft Edge (Windows), iOS/Android apps, Windows OS integration, and WhatsApp/Telegram.

Out-of-scope clause, quoted (listed under "OUT-OF-SCOPE SUBMISSIONS AND VULNERABILITIES"): "AI prompt injection attacks that do not have a security impact on users other than the attacker."

Adjacent out-of-scope AI items, as extracted: system/meta prompt leakage attempts; model hallucination scenarios; content-related issues (routed separately as "AI derived harm").

Award range, as extracted: $250-$30,000 USD for Critical/Important/Moderate severity vulnerabilities.

Last-updated stamp, as extracted: "Last Updated: April 7, 2026" (Getting Started section).

## Pull notes — mechanical only

- Fetched via WebFetch against `www.microsoft.com/en-us/msrc/bounty-ai`; loaded without a 403, so no browser-extension fallback was needed for this source. An earlier attempt at `msrc.microsoft.com/bounty/ai-bounty` returned HTTP 404 and is not the canonical URL — recorded, not used.
- This is Microsoft's engine statement for Pass 5 question (4): a named security-impact carve-out for prompt injection, not a blanket exclusion — a prompt-injection report against Copilot is scoped **out** only when it "does not have a security impact on users other than the attacker," implying a prompt-injection report that does harm a user other than the reporter would be in scope. The page as extracted does not give a worked example distinguishing the two cases.
- No numeric bounty-payout history, report volume, or measured attack-success figure for Copilot specifically is stated on this page.
