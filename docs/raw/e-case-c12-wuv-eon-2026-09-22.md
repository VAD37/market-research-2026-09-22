# W&V (wuv.de) — E.ON interview, paywalled (screened — not opened)

```yaml
source:          W&V / wuv.de (Ebner Media Group), interview by Christiane Treckmann
url_or_doc_id:   https://www.wuv.de/themen/marke/ki-veraendert-sichtbarkeit-wie-e.on-kommunikation-neu-denkt
published:       2026-01-26
pull_date:       2026-09-22
pull_method:     fetch (curl, direct)
pull_purpose:    evidence about a number
tier:            n/a — not opened past the paywall; not tiered
source_label:    company-stated (subject: Ulrike Schiermeister, SVP Communications & Regulation, E.ON)
lane:            E, F
sub_market:      organic recommendation
engine:          not visible past the paywall
metric_kind:     unknown — teaser carries no number
supersedes:      none
captured:        section "teaser only" — full page paywalled ("Du willst weiterlesen? Mit bestehendem Abo einloggen")
language:        German
country:         Germany (E.ON SE is a German energy company; wuv.de is a German trade-press outlet)
vertical:        none named (energy sector, not one of the three programme verticals)
evidence_grade:  screened — not opened (per grading rule 1: paywall blocks the full page; teaser alone is not gradable)
paid_by_outcome: unknown
```

## Verbatim

Titel: „KI verändert Sichtbarkeit: Wie E.ON Kommunikation neu denkt"

Autorin: Christiane Treckmann, 26. Jan 2026, Lesedauer 9 Min., Interview

„KI wird zum neuen Gatekeeper der Energiewirtschaft und verändert, wie Marken sichtbar werden. Ulrike Schiermeister, SVP Communications & Regulation bei E.ON, sieht darin eine Chance – auch für andere Branchen."

„„KI sollten wir nicht nur als Tool betrachten, sondern als neuen Stakeholder." sagt Ulrike Schiermeister, Senior Vice President Communications und Regulation bei E.ON."

„Die Energiewirtschaft befindet sich mitten in einer der größten Transformationen unserer Zeit. Die Energiezukunft wird digitaler, vernetzter – und komplexer. Gleichzeitig verändern KI-Systeme, neue Suchumgebungen und steigende Informationsgeschwindigkeit die Art, wie Menschen Informationen finden, Entscheidungen treffen und Marken wahrnehmen. Für die Kommunikation bedeutet das: Sie muss strategischer werden, verlässlicher – und vor allem anschlussfähig an diese neuen digitalen Gatekeeper."

„Du willst weiterlesen? Mit bestehendem Abo einloggen — Noch kein Abo? Hol dir jetzt dein W&V Abo! 3 Monate testen für nur 19,90 €"

[note: paywall after the fourth paragraph — the rest of the 9-minute interview, including any figures Schiermeister may cite, is inaccessible without a W&V subscription. No login credential is held by this task.]

## gloss (agent translation):

E.ON's SVP Communications & Regulation, Ulrike Schiermeister, frames AI as a new "stakeholder," not just a tool, for the energy sector's communications strategy — a strategic/framing statement, no metric. Everything past this teaser is paywalled.

## Evidence bar — seven items, evaluated against this full page

Not applicable — per grading rule 1, "a case not opened is `screened — not opened`." The visible teaser carries no metric of any kind; the full interview (9-minute read) is behind W&V's subscription wall.

## Pull notes — mechanical only

- Fetched via direct `curl` GET, HTTP 200 (page loads, but content is paywall-gated server-side — the teaser and subscription upsell are the only body content returned, confirmed by full-text extraction of the raw HTML).
- wuv.de is one of the four required C64 outlets (`channels.md`). Every wuv.de article opened this session (this one; the Seowerk/Niko Steeb interview at `e-case-c12-wuv-seowerk-2026-09-22.md`; and a Reddit-and-AI-citations piece checked but not separately filed) hit the identical paywall pattern after 3–4 paragraphs — recorded here as a channel-level finding, not a one-off.
- No browser extension or Playwright was used to attempt a paywall bypass, per this task's fetch-only boundary; flagged in the census `browser backlog` as a channel that may be reachable with the extension in a future pass.
