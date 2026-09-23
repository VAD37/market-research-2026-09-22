# Lessons from Defending Gemini Against Indirect Prompt Injections

```yaml
source:          Chongyang Shi, Sharon Lin, Shuang Song, Jamie Hayes, Ilia Shumailov, Itay Yona et al.
url_or_doc_id:   arXiv:2505.14534 ; https://arxiv.org/abs/2505.14534
published:       2025-05-20 (arXiv v1; latest listed 2025-05-20)
pull_date:       2026-09-23
pull_method:     fetch (arXiv API + arXiv HTML full text)
pull_purpose:    evidence about a number
tier:            5
tier_reason:     vendor report (Google DeepMind) on defending its own Gemini product; academic table 'vendor-authored measuring own product' = 5, bias flagged. No code
source_label:    company-stated
lane:            D
sub_market:      cross
engine:          Gemini 2.0, Gemini 2.5
metric_kind:     none
supersedes:      none
captured:        abstract (verbatim) + result sentences carrying numbers (verbatim from arXiv HTML)
topic_group:     6
venue_status:    arXiv technical report
code_availability: none (internal adversarial-evaluation framework)
capability_class: adaptive adversarial-evaluation loop hardening Gemini against indirect prompt injection
bias_flag:       Google DeepMind measuring its own Gemini models
```

## Verbatim — abstract

"Gemini is increasingly used to perform tasks on behalf of users, where function-calling and tool-use capabilities enable the model to access user data. Some tools, however, require access to untrusted data introducing risk. Adversaries can embed malicious instructions in untrusted data which cause the model to deviate from the user's expectations and mishandle their data or permissions. In this report, we set out Google DeepMind's approach to evaluating the adversarial robustness of Gemini models and describe the main lessons learned from the process. We test how Gemini performs against a sophisticated adversary through an adversarial evaluation framework, which deploys a suite of adaptive attack techniques to run continuously against past, current, and future versions of Gemini. We describe how these ongoing evaluations directly help make Gemini more resilient against manipulation."

## Pull notes — mechanical only

- Metadata via arXiv API `export.arxiv.org/api/query`; abstract verbatim from the API `summary`.
- Result sentences extracted verbatim from `arxiv.org/html/2505.14534`; math markup stripped, wording unchanged. [note: figures and tables are images/HTML, not captured beyond the sentences above].
- Code-availability line reflects the paper's own statement / links found in the HTML this pull.
