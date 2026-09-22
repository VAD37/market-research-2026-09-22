# Muck Rack — "What is AI Reading?" method/report page

```yaml
source:          Muck Rack (Generative Pulse microsite)
url_or_doc_id:   https://generativepulse.ai/report
published:       2026-05 (page banner "MAY 2026"); press release (`a-muckrack-launch-2026-09-22.md`) separately cites a "What is AI Reading? December 2025" research wave — two distinct dated waves of the same report series, not reconciled
pull_date:       2026-09-22
pull_method:     browser (Playwright MCP, MCP_DOCKER)
pull_purpose:    evidence about a number
tier:            5
tier_reason:     adjusted down from table default (3, platform primary) — this is a vendor-authored study of its own product's data corpus ("we prompted AI systems... to find out"), n and date window are stated but the prompt set and per-provider breakdown are gated behind a lead-capture download not completed this pull; tiered as vendor study with partial n/date disclosure, bias flagged
source_label:    vendor-reported
lane:            A
sub_market:      organic recommendation
engine:          "every provider" implied by "the number of citations varies by provider" — no engine individually named on the ungated portion of the page
metric_kind:     visibility
supersedes:      none
captured:        ungated landing-page text only; the full report itself sits behind a form-gated download not completed this pull (`[note: full report PDF not retrieved — lead-capture form not submitted, per task rules against creating accounts or submitting forms without explicit user permission]`)
feature:         Generative Pulse / AI Visibility Badges — the corpus behind both features' citation-based metrics
```

## Verbatim

Product
Solutions
Resources
About
Request Demo
MAY 2026
WHAT IS
AI READING?

AI IS TALKING ABOUT YOU. WE ANALYZED MILLIONS OF PROMPTS TO FIND OUT WHAT IT'S SAYING.

↓
Our prompts asked everything from "which meal kit service is worth signing up for?"...
...to "which travel rewards card should I get?"
We looked at every source AI cited
We found earned media is driving AI responses
But the number of citations varies by provider
And that one news outlet gets cited for most industries
We also found a few things that will change how you think about your media coverage strategy
Download the report for more
For details specific to Education, download the full report
Loading...
© 2026 Muck Rack. All rights reserved. Privacy • Terms

Separately, the Generative Pulse homepage (`generativepulse.ai/`, captured in `a-muckrack-generativepulse-product-2026-09-22.md`'s sibling homepage pull, reproduced here for the method figures it carries) states: "We prompted AI systems over 25 million times since July 2025 to analyze what sources they cite," and gives three top-line figures: "84% of citations in AI answers come from earned media"; "7 days — AI disproportionately cites content updated in the past week"; "2% overlap between journalists most pitched and most cited by AI."

## Pull notes — mechanical only

- claude-in-chrome extension reported "not connected"; pulled via the Playwright MCP fallback, same dedicated tab used for the product-page pull, no other agent's tab touched.
- The report's underlying prompt set, its exact size, its per-engine breakdown, and its exact date window are gated behind a "Download the report" form; this pull did not submit that form (no login, no account creation, no form submission without the user's explicit request, per the task's own constraints), so those specifics are recorded as not retrieved, not as absent.
- **Prompt-set/n/method disclosure answer for Muck Rack: partial.** The homepage/report landing page discloses an n ("over 25 million" prompts since July 2025) and a general method (prompting AI systems and analyzing cited sources) at the corpus level, but not the specific prompt set, its version, or a per-prompt breakdown, and the full report with provider-level detail sits behind an ungated-this-session lead form.
- The report's own stated month (May 2026) does not match the "December 2025" wave the launch press release cites for the same "What is AI Reading?" title — recorded side by side, not reconciled; either two separate editions of the same recurring report, or the landing page has been updated to promote a newer edition since the March 2026 press release.
