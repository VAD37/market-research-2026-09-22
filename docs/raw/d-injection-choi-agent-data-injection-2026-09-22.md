# Choi, Kim, Kang, Jeong, Xing, Lee — Agent Data Injection Attacks are Realistic Threats to AI Agents

```yaml
source:          arXiv (Woohyuk Choi, Juhee Kim, Taehyun Kang, Jihyeon Jeong, Luyi Xing, Byoungyoung Lee)
url_or_doc_id:   https://arxiv.org/pdf/2607.05120 (abs page fetched: https://arxiv.org/abs/2607.05120)
published:       2026-07-06
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            5
tier_reason:     No venue field and no code/data-release statement in the abstract or the "Comments" field ("19 pages, 19 figures, 7 tables") as fetched 2026-09-22 — treated as preprint without confirmed code per trust-rubric.md academic table default. Academic sources are exempt from the plan.md recency/staleness filter. Task-designated seed for cluster P5-c6.
source_label:    analyst-derived
lane:            D
sub_market:      organic recommendation
engine:          Claude in Chrome, Antigravity, Nanobrowser (named web agents); Claude Code, Codex, Gemini CLI (named coding agents)
metric_kind:     none
supersedes:      none
captured:        section "abstract" plus subject/comments metadata, via WebFetch verbatim-extraction prompt against the arXiv abs page
```

## Verbatim

Title, as printed: "Agent Data Injection Attacks are Realistic Threats to AI Agents"

Authors, as printed: Woohyuk Choi, Juhee Kim, Taehyun Kang, Jihyeon Jeong, Luyi Xing, Byoungyoung Lee

Submission date, as printed: Submitted on 6 Jul 2026

Subjects, as printed: cs.CR; cs.AI

Comments, as printed: "19 pages, 19 figures, 7 tables"

Abstract, verbatim:

"AI agents act on behalf of user prompts, consuming external data and taking actions based on the agent context. Prior research on AI agent security has primarily focused on indirect prompt injection (IPI). Its most well-studied category is instruction injection, where attacker-controlled untrusted data is interpreted as an instruction. In response, many mitigations have been proposed to prevent instruction injection attacks. In this paper, we introduce a new category of IPI, agent data injection attacks (ADI). ADI injects malicious data disguised as trusted data, such as security-critical metadata (e.g., resource identifiers or data origins) or agent context data (e.g., tool call and response formats). As a result, agents unknowingly execute unintended actions based on attacker-controlled data. ADI has similar attack impacts as instruction injection attacks, because it causes agents to misbehave and execute unintended actions. Despite the similar impact, ADI remains underexplored and easily bypasses existing IPI defenses. We found several critical vulnerabilities in real-world agents that allow an attacker to launch various attacks: arbitrary click attacks on web agents (Claude in Chrome, Antigravity, and Nanobrowser), and remote code execution and supply-chain attacks on coding agents (Claude Code, Codex, and Gemini CLI). We evaluate ADI vulnerabilities across off-the-shelf models and AI agents, and find that ADI is effective in both standalone LLMs and AI agent settings. ADI exposes a critical gap in agent security, signifying that current AI agents do not employ a fundamental security principle: current agents do not isolate trusted data from untrusted data."

[note: no injected-data payload text is reproduced here — the abstract names the vulnerability class and the affected products without printing attack strings.]

## Pull notes — mechanical only

- Fetched via WebFetch against `arxiv.org/abs/2607.05120` on 2026-09-22 (the task-given seed URL was the `/pdf/` path; the `/abs/` page was fetched instead since it carries the same abstract/metadata and is more reliably parsed than a raw PDF).
- Mechanism class named here (agent data injection, ADI) is a variant of indirect prompt injection distinct from the classic "instruction injection into retrieved text" mechanism the other papers in this cluster document — ADI disguises malicious data as trusted metadata rather than as an instruction. Recorded in the census as a distinct mechanism sub-class.
- The named vulnerable products (Claude in Chrome, Antigravity, Nanobrowser, Claude Code, Codex, Gemini CLI) are real, currently-shipping agent products, not synthetic test harnesses — this is a researcher audit of live products' handling of untrusted data, not a test against a third-party production brand-recommendation surface. No product-recommendation or brand-steering outcome is claimed in this abstract; the demonstrated impacts are clicks, RCE, and supply-chain compromise.
- No numeric attack-success rate, n, or date window beyond the July 2026 submission date is given in the abstract itself.
