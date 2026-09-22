# Greshake et al. — foundational indirect prompt injection paper

```yaml
source:          arXiv (Kai Greshake, Sahar Abdelnabi, Shailesh Mishra, Christoph Endres, Thorsten Holz, Mario Fritz)
url_or_doc_id:   https://arxiv.org/abs/2302.12173
published:       2023-02-23 (v1); last revised 2023-05-05 (v2)
pull_date:       2026-09-22
pull_method:     fetch
pull_purpose:    evidence about a number
tier:            5
tier_reason:     No "Comments:" / venue field and no code-or-data link were found on the arXiv abstract page as fetched 2026-09-22 (checked explicitly); treated as preprint without confirmed code per trust-rubric.md academic table default. Academic sources are exempt from the plan.md recency/staleness filter.
source_label:    analyst-derived
lane:            D
sub_market:      organic recommendation
engine:          Bing's GPT-4-powered Chat (named in abstract); also code-completion engines and synthetic GPT-4 applications
metric_kind:     none
supersedes:      none
captured:        section "abstract" only, via WebFetch verbatim-extraction prompt against the arXiv abs page
```

## Verbatim

Title, as printed: "Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection"

Authors, as printed: Kai Greshake, Sahar Abdelnabi, Shailesh Mishra, Christoph Endres, Thorsten Holz, Mario Fritz

Submission history, as printed: [v1] Thu, 23 Feb 2023 17:14:38 UTC (5,052 KB); [v2] Fri, 5 May 2023 14:26:17 UTC (10,831 KB)

Subjects, as printed: Cryptography and Security (cs.CR); Artificial Intelligence (cs.AI); Computation and Language (cs.CL); Computers and Society (cs.CY)

Abstract, verbatim:

"Large Language Models (LLMs) are increasingly being integrated into various applications. The functionalities of recent LLMs can be flexibly modulated via natural language prompts. This renders them susceptible to targeted adversarial prompting, e.g., Prompt Injection (PI) attacks enable attackers to override original instructions and employed controls. So far, it was assumed that the user is directly prompting the LLM. But, what if it is not the user prompting? We argue that LLM-Integrated Applications blur the line between data and instructions. We reveal new attack vectors, using Indirect Prompt Injection, that enable adversaries to remotely (without a direct interface) exploit LLM-integrated applications by strategically injecting prompts into data likely to be retrieved. We derive a comprehensive taxonomy from a computer security perspective to systematically investigate impacts and vulnerabilities, including data theft, worming, information ecosystem contamination, and other novel security risks. We demonstrate our attacks' practical viability against both real-world systems, such as Bing's GPT-4 powered Chat and code-completion engines, and synthetic applications built on GPT-4. We show how processing retrieved prompts can act as arbitrary code execution, manipulate the application's functionality, and control how and if other APIs are called. Despite the increasing integration and reliance on LLMs, effective mitigations of these emerging threats are currently lacking. By raising awareness of these vulnerabilities and providing key insights into their implications, we aim to promote the safe and responsible deployment of these powerful models and the development of robust defenses that protect users and systems from potential attacks."

[note: this pull captured only the arXiv abstract page (title, authors, submission history, subjects, abstract). The full-text methodology, threat-model detail, and any reproduced injection strings were not fetched, and per the Lane D hard constraint no payload text is reproduced here beyond what the abstract itself states.]

## Pull notes — mechanical only

- Fetched via WebFetch against `arxiv.org/abs/2302.12173`; the fetch tool renders HTML to markdown and summarizes through a small model, so the abstract above is the model's verbatim-instructed transcription of the page text, not a raw HTML dump.
- A second WebFetch call specifically asked for the "Comments:" field; the tool reported none was visible in the content it received. This is recorded as a pull limitation, not as confirmation the page carries no such field.
- No PDF or full-text HTML version was fetched in this pull.
- This is the paper that coins "Indirect Prompt Injection" (IPI) as a named attack class and is the earliest item in this cluster (submitted 2023-02-23) among the eight raw pulls landed for P5-c6.
