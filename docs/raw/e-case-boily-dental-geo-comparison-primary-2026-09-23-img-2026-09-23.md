# Boily — "GEO 정비 전후 AI 검색 노출률 비교" (dental clinic GEO comparison) — image read (IMG-1b)

```yaml
source:          boily.co.kr (Korean GEO vendor guide page) — the inline SVG chart
url_or_doc_id:   https://boily.co.kr/guide/geo-repair-case-2026-06
published:       2026-06 (URL slug; per source raw file)
pull_date:       2026-09-23
pull_method:     image read (IMG-1b) — SVG markup read as text (inline <svg role="img"> saved verbatim; no raster)
pull_purpose:    evidence about a number
tier:            5
tier_reason:     inherits e-case-boily-dental-geo-comparison-primary-2026-09-23.md
source_label:    vendor-reported (as the source raw file labels it)
lane:            E
sub_market:      organic recommendation
engine:          ChatGPT, Claude, Gemini, Perplexity (as in the substitute; the chart names no engine)
metric_kind:     visibility (mention rate, "AI 검색 노출률")
supersedes:      none — reads the image referenced in e-case-boily-dental-geo-comparison-primary-2026-09-23.md; page text is in e-case-boily-dental-geo-comparison-2026-09-23.md
captured:        one SVG chart, transcribed in full
```

## 01-geo-ai

image: docs/raw/img/e-case-boily-dental-geo-comparison-primary-2026-09-23/01-geo-ai.svg (viewBox 0 0 720 190)

Chart type: horizontal bar chart, two bars (one per clinic), each bar a filled portion of a 480-unit track, with a printed before → after value. No axes, no gridlines.

aria-label: "GEO 정비 전후 AI 검색 노출률 비교(익명)".

Title printed on the chart: "AI 검색 노출률 — 정비 전 → 정비 후 (병원명 비공개)".

| Bar label (printed) | Value label (printed) | Filled width / track width (SVG units) |
|---|---|---|
| "영통OOO치과 · 정비함" | "11% → 27% (+16%p)" | 324 / 480 |
| "강남OOO치과 · 비교군(정비 안 함)" | "11% → 10% (제자리)" | 120 / 480 |

Footnote printed on the chart (small grey text): "N=2 관찰(통제 실험 아님) · 인과 단정 아님 · 효과 보장 아님 · 같은 중립 측정으로 전후 비교".

Legend: none. Source line: none beyond the footnote. Date: none printed on the chart. Engine: none printed.

Text cross-check: the substitute text states "정비한 영통OOO치과는 약 11% → 27%(+16%p). 정비하지 않은 비교군(강남OOO치과)은 약 11% → 10%로 제자리였습니다" — same figures as the chart (text adds "약", approximately; chart prints the bare percentages). The text's "N=2 관찰입니다. 변수를 통제한 A/B 실험이 아니라서" matches the chart footnote. `findings/proof-scorecard.md` already carries "mention rate 11% → 27% treated; 11% → 10% untreated".
