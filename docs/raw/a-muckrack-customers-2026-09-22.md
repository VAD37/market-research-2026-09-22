# Muck Rack — Generative Pulse customer / case study (Three Rings)

```yaml
source:          Muck Rack (Generative Pulse microsite homepage teaser; full case-study page blocked)
url_or_doc_id:   https://generativepulse.ai/ (case-study teaser); https://muckrack.com/resources/case-studies/three-rings-inc-case-study (full case study, blocked)
published:       undated — no date on the teaser; full page not reached
pull_date:       2026-09-22
pull_method:     browser (Playwright MCP) for the teaser; browser (Playwright MCP, Cloudflare-blocked) for the full case study
pull_purpose:    evidence about a number
tier:            6
tier_reason:     downgraded from table default — the only content captured is a short vendor-written teaser with no baseline, no date window, no sample size, and no named engine; the full case study that might carry more detail was not reachable (Cloudflare block on muckrack.com)
source_label:    vendor-reported
lane:            A
sub_market:      organic recommendation
engine:          n/a — not named in the teaser
metric_kind:     sales (pipeline value claimed, ungraded — see below)
supersedes:      none
captured:        homepage teaser text only; full case-study page not captured (blocked)
feature:         Generative Pulse
```

## Verbatim

CASE STUDY
From AI insight to six figures in pipeline
Three Rings, a B2B tech marketing agency, used Generative Pulse to analyze real prompts and uncover content gaps in AI-generated answers. They created targeted content, pitched the right journalists, and secured coverage in relevant outlets—improving how their client appeared in AI answers.
Read The Case Study

Attempt to open the full case study at `muckrack.com/resources/case-studies/three-rings-inc-case-study` via the Playwright MCP browser returned page title "Just a moment..." — the same Cloudflare interstitial recorded for `muckrack.com/pricing` — on two navigation attempts; the full case study's baseline, date window, sample size, and measurement party (if any beyond Muck Rack itself) were not recoverable this session.

**evidence_grade: Fools gold** (on intake, from the teaser text alone). "Six figures in pipeline" is a revenue-adjacent claim (sales-proximate — pipeline value, not closed revenue) with no baseline, no control, no date window, no sample size, and no named measurer beyond the vendor's own headline — meets the Fools gold description exactly ("revenue claim, no baseline or no control"). Filed here as evidence of category noise, per `trust-rubric.md`, not as sales proof. If the full case study page becomes reachable in a later pull, this grade is subject to revision from the fuller text — this file is not edited after the fact per `templates/raw-pull.md`; a re-pull would land in a new file.

## Pull notes — mechanical only

- claude-in-chrome extension reported "not connected"; Playwright MCP fallback used throughout, dedicated tab, no other agent's tab touched.
- This is the only customer/case-study content found for Muck Rack's AI-visibility feature this session — no aggregate customer or logo count for Generative Pulse or AI Visibility Badges specifically was found anywhere reached (the general "Thousands of companies" figure in the launch release's boilerplate describes Muck Rack's whole PR platform, not this feature, and is not counted here).
- `unknown — checked muckrack.com/resources/case-studies (Cloudflare-blocked), generativepulse.ai (no case-study index page found beyond the one homepage teaser) 2026-09-22` — full case-study text, and any further AI-specific case studies beyond this one, not recoverable this session.
