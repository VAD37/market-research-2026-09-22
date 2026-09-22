# Chen, Toyoda, Lai, Leung — IPI-proxy: An Intercepting Proxy for Red-Teaming Web-Browsing AI Agents Against Indirect Prompt Injection

```yaml
source:          arXiv (Chia-Pei (Janet) Chen, Kentaroh Toyoda, Anita Lai, Alex Leung)
url_or_doc_id:   https://arxiv.org/pdf/2605.11868 (abs page fetched: https://arxiv.org/abs/2605.11868) ; code https://github.com/VulcanLab/IPI-Proxy/
published:       2026-05-12
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            4
tier_reason:     Preprint with a published open-source toolkit and an assembled payload library (820 deduplicated attack strings drawn from six published benchmarks) per trust-rubric.md academic table "Preprint with code and prompt set" = 4. No independent peer review or replication confirmed in this pull. Academic sources are exempt from the plan.md recency/staleness filter. Task-designated seed for cluster P5-c6.
source_label:    analyst-derived
lane:            D
sub_market:      organic recommendation
engine:          n/a — tool targets any whitelisted-domain web-browsing agent in a deployer's own test environment; no named production consumer assistant tested in the abstract
metric_kind:     none
supersedes:      none
captured:        section "abstract" plus comments metadata, via WebFetch verbatim-extraction prompt against the arXiv abs page
```

## Verbatim

Title, as printed: "IPI-proxy: An Intercepting Proxy for Red-Teaming Web-Browsing AI Agents Against Indirect Prompt Injection"

Authors, as printed: Chia-Pei (Janet) Chen, Kentaroh Toyoda, Anita Lai, Alex Leung

Submission date, as printed: 12 May 2026

Subjects, as printed: Cryptography and Security (cs.CR); Artificial Intelligence (cs.AI)

Comments, as printed: "code: https://github.com/VulcanLab/IPI-Proxy/"

Abstract, verbatim:

"Web-browsing AI agents are increasingly deployed in enterprise settings under strict whitelists of approved domains, yet adversaries can still influence them by embedding hidden instructions in the HTML pages those domains serve. Existing red-teaming resources fall short of this scenario: prompt-injection benchmarks ship pre-built adversarial pages that whitelisted agents cannot reach, and generic LLM scanners probe the model API rather than its retrieved content. We present IPI-proxy, an open-source toolkit for red-teaming web-browsing agents against indirect prompt injection (IPI). At its core is an intercepting proxy that rewrites real HTTP responses from whitelisted domains in flight, embedding payloads drawn from a unified library of 820 deduplicated attack strings extracted from six published benchmarks (BIPIA, InjecAgent, AgentDojo, Tensor Trust, WASP, and LLMail-Inject). A YAML-driven test harness independently parameterizes the payload set, the embedding technique (HTML comment, invisible CSS, or LLM-generated semantic prose), and the HTML insertion point (6 locations from head_meta to script_comment), enabling parameter-sweep evaluation without mock pages or sandboxed environments. A companion exfiltration tracker logs successful callbacks. This paper describes the threat model, situates IPI-proxy among contemporary IPI benchmarks and red-teaming tools, and details its architecture, design decisions, and configuration interface. By bridging static benchmarks and live deployment, IPI-proxy gives AI security teams a reproducible substrate for measuring and hardening web-browsing agents against indirect prompt injection on the same retrieval surface attackers exploit in production."

[note: no individual attack string from the 820-item library is reproduced here — the abstract names the library's size, sources, and embedding techniques (HTML comment, invisible CSS, LLM-generated semantic prose) as a class, not as printed text.]

## Pull notes — mechanical only

- Fetched via WebFetch against `arxiv.org/abs/2605.11868` on 2026-09-22 (task-given seed URL was the `/pdf/` path; the `/abs/` page carries the same abstract/metadata).
- This is a tooling paper: it packages known injection payloads and embedding techniques (HTML comment, invisible CSS, LLM-generated semantic prose — this last is the closest named mechanism in this cluster's pulls to "text placed in indexed content written to read as natural prose") into a proxy that rewrites a deployer's own whitelisted-domain traffic. The abstract explicitly frames the tool for use "in a deployer's own test environment," consistent with the Lane D constraint against testing on third-party surfaces — this paper's own stated use case is the same constraint this research task operates under.
- No attack-success-rate figure against any named production assistant is stated in the abstract; the paper is a red-teaming substrate, not itself a reported measurement.
