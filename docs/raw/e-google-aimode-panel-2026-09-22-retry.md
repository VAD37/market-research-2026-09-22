# Google AI Mode / AI Overviews — Pass 10 panel, day 0 (retry)

```yaml
source:          Google — AI Mode and AI Overviews, search-integrated surfaces
url_or_doc_id:   primary arm https://www.google.com/search?q=<query>&udm=50 ; secondary arm https://www.google.com/search?q=<query>
published:       n/a — live surface, not a document
pull_date:       2026-09-22
pull_method:     browser extension
pull_purpose:    evidence about a number
tier:            1
tier_reason:     table default — measured-by-us
source_label:    measured-by-us
lane:            E
sub_market:      n/a
engine:          Google AI Mode / Google AI Overviews — model_version_shown: unknown — surface displays none (see deviations)
metric_kind:     visibility
supersedes:      docs/raw/e-google-aimode-panel-2026-09-22.md
captured:        full page text per run via get_page_text; screenshot for run_index 1 of every prompt and any sponsored unit
prompt_set:      panel-protocol v1
runs_n:          see achieved_n per prompt below
surface:         Google AI Mode (primary, search-integrated) / Google AI Overviews (secondary, search-integrated)
region:          intended US — observed: see deviations (Vietnamese-language UI, VND-denominated prices, one run's full answer text in Vietnamese)
pass:            P10
```

## Deviations

- **Extension connected — supersedes the earlier blocked attempt.** The task naming this file (`P10-d0-google-aimode-retry`) instructed retrying with the `claude-in-chrome` extension after it reconnected at ~22:00 HCM (~15:00 UTC). `tabs_context_mcp` connected immediately; `google.com/search` with and without `udm=50` rendered normally on the very first navigation — **no bot-check, no CAPTCHA, no `/sorry/` interstitial at any point in this session**, unlike `e-google-aimode-panel-2026-09-22.md` (Playwright MCP browser, IP `159.26.119.97`, blocked on every request). This file's traffic ran from the extension's real-Chrome egress instead.
- **Login state.** Every navigation this session showed the top-right corner control reading `Đăng nhập` ("Sign in") — logged-out throughout. `login_state: logged-out` for every run.
- **Region / language personalization — material confound.** `region_intended` is US and no location was ever typed into any prompt. Observed on every run regardless: Google's own chrome (nav labels, buttons, "Hỏi bất cứ điều gì" composer placeholder) renders in **Vietnamese**; almost all product-card prices are in **VND** (a few cards mix in `(US$)` or `(CA$)` parenthetical conversions); store names skew Vietnamese/SEA retail (Hasaki.vn, Pharmacity, Chiaki.vn, Sasa Malaysia, Shopee.vn, Rosalinaboutique). On one run (SK-01 run 4) the **entire AI answer body itself was generated in Vietnamese**, not just the surrounding UI, despite the prompt being typed in English and identical across all 5 runs. This is the same personalization pattern the Claude-panel file (`e-claude-panel-2026-09-22.md`) recorded for its account, but here it persists **logged-out**, so it is IP/network-geolocation-based, not account-Memory-based. `region_observed` is recorded per run with whatever the run itself showed (UI language, price currency, answer language); the file-wide pattern is not re-argued per run.
- **Model version never disclosed.** Checked once, deliberately, on SK-01 run 1: an info affordance exists near the answer (button labelled `Thông tin về câu trả lời này`, "Information about this answer"); clicking it did not surface any model name or version string in the resulting UI state (screenshot before/after showed no visible panel change beyond composer focus). No model picker, footer tag, or "about this answer" panel anywhere on any AI Mode or AI Overviews page ever named a model. Recorded `model_version_shown: unknown — surface displays none` for every run in this file; not re-checked per run after this single establishing check, to conserve session budget.
- **Search toggle.** No exposed toggle control was found on the AI Mode page (no visible on/off switch for "AI Mode" itself beyond the top nav tab strip `Chế độ AI | Tất cả | Hình ảnh | ...`, which is surface **selection** — i.e. which tab of the results page — not an in-answer search toggle in the sense of other engines' web-search-on/off switch). Recorded `search_toggle: not exposed` for every AI Mode run. The **toggle arm** required by the protocol ("re-run the vertical's first C prompt with the toggle flipped") has no control to flip on this surface; per the protocol's own recording rule for this case ("record `not exposed` if none") this arm is recorded as `not-sampled: no toggle control exists on Google AI Mode / AI Overviews` rather than run.
- **Timestamp polling — batched per prompt, not per individual run, on the C-prompt block after SK-01.** SK-01 (the first prompt) was run with `get_current_time` polled after each of its 5 runs individually (see per-run timestamps below — genuinely distinct, seconds apart). Given this surface returns a full new answer in 6-10s per page load (far faster than a multi-turn chat conversation), polling after every single one of the remaining ~165 planned runs was not sustainable inside this session's tool-call budget. From SK-02 onward, each prompt's n runs were issued as one batched sequence of navigations, and `get_current_time` was polled **once per prompt**, immediately after that prompt's last run's page-text extraction. Per-run timestamps within a prompt are recorded as that single poll time with a `~clustered, all n runs of this prompt completed within nn s before this poll` note rather than distinct exact times. This is a disclosed efficiency deviation from "poll UTC after every run," not a silent one; it does not affect any brand, citation or sponsored-unit finding.
- **Screenshot policy.** One screenshot (`save_to_disk`) taken for `run_index: 1` of each prompt, per schema. Not repeated for runs 2-5 of the same prompt (no sponsored unit was observed in this file — see Records — so the "every run showing a sponsored unit" trigger never fired).
- **Save cadence.** This file is written to disk after each completed prompt (5 runs, or 1 run for the AI-Overviews secondary arm), not after every single individual run, for the same tool-budget reason as the timestamp batching above. Every prompt's full set of runs is captured in-session before the write, so no run's data is lost between saves within a prompt.
- **Unsolicited tab, not interacted with.** After the SK-01 run-1 screenshot, an unrequested tab (`www.kargo.com`, an ad-tech company's site) briefly appeared in the tab list, then a second unrequested blank `chrome://newtab/` tab appeared after SK-01 run 2. Neither was created by this session (`tabs_close_mcp` on the kargo.com tab returned "not in Claude's tab group"), neither was clicked, read, or navigated by this session, and both had disappeared from the tab list by the next `tabs_context_mcp` check. Recorded as a mechanical anomaly, not further investigated — plausibly a pop-under from an ad/tracker script on the AI Mode page's right-rail source cards, though this is not confirmed (no interaction was made to test that theory, per the hard constraint against clicking ads).
- **Sample scope reached this session.** See per-prompt `achieved_n` below and the closing summary. Order of work followed the task instructions: all 14 C prompts at n=5 on AI Mode first.

## Records

Schema per run follows `panel-protocol.md` "Record schema". `engine: Google AI Mode` (primary arm) or `Google AI Overviews` (secondary arm), `surface: search-integrated`, `prompt_set_version: v1`, `region_intended: US`, `login_state: logged-out` for every run unless stated otherwise, `model_version_shown: unknown — surface displays none` for every run (established once, see deviations). Fields repeated per run are given in a compact block; `answer_text_verbatim` follows each block in full.

### Vertical: Skincare and beauty

#### SK-01 — C — "best moisturizer for dry sensitive skin" — arm: main — achieved_n: 5/5

**Run 1**
```
sample_id: google-ai-mode-2026-09-22-SK-01-r1
surface_url: https://www.google.com/search?q=best+moisturizer+for+dry+sensitive+skin&udm=50
timestamp_utc: 2026-09-22T15:16:36Z | local_utc_offset: unknown — surface displays none
region_observed: UI in Vietnamese ("Chế độ AI", "Đăng nhập"); answer text in English; prices in VND (CeraVe 235.000₫) with one CA$ parenthetical | search_toggle: not exposed | arm: main
answer_outcome: answered
brands_mentioned (order): CeraVe (CeraVe Moisturizing Cream), Vanicream (Vanicream Moisturizing Cream), La Roche-Posay (Toleriane Double Repair Face Moisturizer), Skinfix (Barrier+ Triple Lipid-Peptide Cream), Aestura (Atobarrier365 Cream)
brands_cited: none observed — right-rail source cards link third-party publishers (Allure, Byrdie, Smytten, New York Magazine), not brand domains
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. CeraVe Moisturizing Cream  2. Vanicream Moisturizing Cream  3. La Roche-Posay Toleriane Double Repair Face Moisturizer  4. Skinfix Barrier+ Triple Lipid-Peptide Cream  5. Aestura Atobarrier365 Cream
sponsored_units: none observed
screenshot_ref: docs/raw/screenshots/ (not saved to repo — captured to local temp path C:\Users\vad\AppData\Local\Temp\claude-chrome-screenshots-qyXR2y\screenshot-1790090216086-0.jpg; see notes)
notes: info icon "Thông tin về câu trả lời này" checked once here for model version — no version string surfaced. Right rail carried 3 publisher source cards (Allure, Smytten, New York Magazine) with a "Hiện tất cả" (show all) expander, not expanded.
```
answer_text_verbatim:
> The best moisturizers for dry, sensitive skin focus on repairing a compromised skin barrier, locking in deep hydration, and eliminating common irritants like fragrance, drying alcohols, and essential oils. While there is no single absolute best choice for everyone, top dermatologist-recommended and expert-tested formulas excel at targeting specific skin sensitivities and texture preferences.
>
> Top-tier dermatologist-tested options include:
>
> **CeraVe Moisturizing Cream** — 235.000 ₫ — Mỹ Phẩm Hãng và nhiều cửa hàng khác — 4.8 (93,1 N)
> Best For: Intensive barrier restoration and long-lasting daily hydration for very dry skin types. Reviewers on Byrdie praise its non-greasy, rich texture that sinks in quickly.
> Key Ingredients: Formulated with three essential ceramides, hyaluronic acid, and utilizing MVE technology for sustained 24-hour hydration.
>
> **Vanicream Moisturizing Cream** — 538.999 ₫ — Chiaki.vn — 5.0 (27)
> Best For: Highly reactive or allergy-prone skin that cannot tolerate complex skincare formulations. Experts cited by The Strategist note it is an ideal baseline moisturizer to minimize inflammation.
> Key Ingredients: Simple, ultra-clean formula containing petrolatum and glycerin, entirely free from common chemical irritants like dyes, parabens, and lanolin.
>
> **La Roche-Posay Toleriane Double Repair Face Moisturizer** — 610.002 ₫ (32,95 CA$) — Rosalinaboutique — 4.1 (4,9 N)
> Best For: Lightweight yet deeply nourishing daytime wear that layers beautifully under sunscreen or makeup. Testers at Fortune highlight its weightless consistency and fast absorption.
> Key Ingredients: Packed with prebiotic thermal spring water, ceramide-3, niacinamide, and glycerin to calm redness and support the skin microbiome.
>
> [note: page also listed Skinfix Barrier+ Triple Lipid-Peptide Cream and Aestura Atobarrier365 Cream as additional product cards per the accessibility/text extraction of the equivalent run-1 fetch; full per-card copy for those two not re-quoted here to avoid restating — brand order and names as captured are in brands_mentioned/brands_recommended above]
>
> To help narrow down the selection, please share:
> - Are you looking for a heavy night cream or a lightweight daytime lotion?
> - Do you experience specific issues like eczema, acne flare-ups, or severe redness?
> - What is your ideal budget range?
>
> [Right rail: Allure — "11 Best Face Moisturizers for Sensitive Skin That ... - Allure", 10 thg 3, 2026; Smytten — "9 Dermatologist Recommended Moisturizers for Dry Sensitive ...", 20 thg 8, 2026; New York Magazine — "14 Best Moisturizers for Dry Skin | The Strategist", 19 thg 2, 2026]

**Run 2**
```
sample_id: google-ai-mode-2026-09-22-SK-01-r2
surface_url: https://www.google.com/search?q=best+moisturizer+for+dry+sensitive+skin&udm=50
timestamp_utc: 2026-09-22T15:17:34Z | local_utc_offset: unknown — surface displays none
region_observed: UI in Vietnamese; answer text in English; prices in VND (CeraVe 157.250₫) with CA$/US$ parentheticals on two cards | search_toggle: not exposed | arm: main
answer_outcome: answered
brands_mentioned (order): CeraVe (Moisturizing Cream), La Roche-Posay (Toleriane Double Repair Face Moisturizer), Vanicream (Daily Facial Moisturizer)
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. CeraVe Moisturizing Cream  2. La Roche-Posay Toleriane Double Repair Face Moisturizer  3. Vanicream Daily Facial Moisturizer
sponsored_units: none observed
screenshot_ref: none — not run_index 1
notes: price for CeraVe differs from run 1 (235.000₫ vs 157.250₫) — answer is regenerated per run, not a cached/static card.
```
answer_text_verbatim:
> The ideal moisturizers for dry, sensitive skin prioritize barrier repair, fragrance-free formulations, and intense hydration without irritating active ingredients. According to dermatologists and multi-product testing by experts, there isn't one absolute best option, but rather a few standout choices depending on your budget and preferred texture.
>
> Top Dermatologist & Expert Picks
>
> **CeraVe Moisturizing Cream** — 157.250 ₫ — Pharmacity và nhiều cửa hàng khác — 4.8 (73,1 N)
> Best for Barrier Repair: Highly recommended by dermatologists, it combines three essential ceramides and hyaluronic acid to reconstruct a compromised skin barrier and lock in all-day moisture.
> Texture: Thick and rich, yet non-greasy, making it perfect for severe dryness.
>
> **La Roche-Posay Toleriane Double Repair Face Moisturizer** — 610.002 ₫ (32,95 CA$) — Rosalinaboutique — 4.1 (4,9 N)
> Best for Daily Wear: A lightweight cream formulated with prebiotic thermal water, ceramides, and niacinamide to simultaneously hydrate and soothe skin redness.
> Safety: Completely fragrance-free, allergy-tested, and safe for highly reactive skin.
>
> **Vanicream Daily Facial Moisturizer** — 1.743.008 ₫ (67,00 US$) — Ubuy
> Best for Ultra-Sensitive Skin: Formulated with an exceptionally short ingredient list to eliminate common irritants like dyes, fragrance, parabens, and formaldehyde.
> Key Components: Relies on five ceramides, squalane, and hyaluronic acid to safely deep-hydrate hyper-reactive skin types.
>
> What to Look For vs. Avoid:
> Look for (Barrier-Supporting): Ceramides & Squalane (replenishes protective fats); Glycerin & Hyaluronic Acid (draws in deep hydration); Colloidal Oatmeal & Niacinamide (calms inflammation)
> Avoid (Irritants & Stripping Agents): Added Fragrance & Essential Oils (causes contact dermatitis); Drying Alcohols (SD alcohol, denatured alcohol); Harsh Exfoliating Acids (Glycolic/Salicylic acid in daily creams)
>
> To help tailor this, please let me know:
> - Are you looking for a daytime cream (that layers well under makeup/sunscreen) or a rich nighttime cream?
> - Do you experience specific issues like flaking, redness, or eczema flare-ups?
>
> [Right rail: Allure — "11 Best Face Moisturizers for Sensitive Skin That ... - Allure", 10 thg 3, 2026; Byrdie — "The 9 Best Moisturizers for Sensitive Skin, Tested by Byrdie", 20 thg 6, 2025; Sasa Malaysia — "Best Moisturizers for Dry and Sensitive Skin: Ultimate Guide"]

**Run 3**
```
sample_id: google-ai-mode-2026-09-22-SK-01-r3
surface_url: https://www.google.com/search?q=best+moisturizer+for+dry+sensitive+skin&udm=50
timestamp_utc: 2026-09-22T15:18:08Z | local_utc_offset: unknown — surface displays none
region_observed: UI in Vietnamese; answer text in English; prices in VND | search_toggle: not exposed | arm: main
answer_outcome: answered
brands_mentioned (order): CeraVe (Moisturizing Cream), Vanicream (Moisturizing Cream), Skinfix (Barrier+ Triple Lipid Peptide Cream)
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. CeraVe Moisturizing Cream  2. Vanicream Moisturizing Cream  3. Skinfix Barrier+ Triple Lipid Peptide Cream
sponsored_units: none observed
screenshot_ref: none — not run_index 1
notes: first `get_page_text` on this run returned only unrendered page CSS (page had not finished hydrating at 6s); a second wait (6s) plus re-fetch returned the real answer, quoted below. Total wait before successful extraction ~12s.
```
answer_text_verbatim:
> The top dermatologist-recommended choices for dry, sensitive skin include CeraVe Moisturizing Cream for affordable barrier repair, Vanicream Moisturizing Cream for maximum safety on reactive skin, and SkinFix Barrier+ Triple Lipid Peptide Cream for premium, clinical-grade lipid replenishment. Medical experts emphasize that the ideal formula must be completely fragrance-free and rich in skin-identical emollient fats like ceramides to seal in moisture without inducing inflammation.
>
> **CeraVe Moisturizing Cream** — 148.000 ₫ — Hasaki.vn và nhiều cửa hàng khác — 4.8 (73,1 N)
> Best Use: Affordable, deep all-day face and body hydration.
> Key Ingredients: Three essential ceramides and moisture-binding hyaluronic acid.
> Expert Review: Highly praised in The Strategist Skincare Review.
>
> **Vanicream Moisturizing Cream** — 538.999 ₫ — Chiaki.vn — 5.0 (27)
> Best Use: Maximum safety for highly reactive allergy-prone skin.
> Formula Spec: Completely free of dyes, fragrances, and parabens.
> Expert Review: Vetted thoroughly by the Wirecutter Moisturizer Guide.
>
> **SkinFix Barrier+ Triple Lipid Peptide Cream** — 1.480.000 ₫ — mmproface.com — 4.6 (5,9 N)
> Best Use: Rich nourishment for severely compromised skin barriers.
> Key Ingredients: Patented triple-lipid complex, active peptides, and niacinamide.
> Expert Review: Awarded top honors by Allure Skincare Awards.
>
> To find your exact match, let me know:
> - Do you prefer a lightweight texture for daytime wear or a thick cream for overnight recovery?
> - Are you currently managing secondary concerns like acne breakouts, eczema flares, or rosacea redness?
>
> [Right rail: Allure — "11 Best Face Moisturizers for Sensitive Skin That ... - Allure", 10 thg 3, 2026; Smytten — "9 Dermatologist Recommended Moisturizers for Dry Sensitive ...", 20 thg 8, 2026; Smytten — "11 Dermatologist Recommended Lotions for Dry Skin Relief", 11 thg 8, 2026]

**Run 4**
```
sample_id: google-ai-mode-2026-09-22-SK-01-r4
surface_url: https://www.google.com/search?q=best+moisturizer+for+dry+sensitive+skin&udm=50
timestamp_utc: 2026-09-22T15:18:28Z | local_utc_offset: unknown — surface displays none
region_observed: UI in Vietnamese; ANSWER BODY ITSELF in Vietnamese this run (prompt was sent in English, unchanged); prices in VND with CA$/US$ parentheticals | search_toggle: not exposed | arm: main
answer_outcome: answered
brands_mentioned (order): CeraVe, La Roche-Posay (Toleriane Double Repair), Vanicream, Aestura (Atobarrier365 Cream), Aveeno (Calm + Restore Oat Gel Moisturizer)
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. CeraVe Moisturizing Cream  2. La Roche-Posay Toleriane Double Repair Face Moisturizer  3. Vanicream Moisturizing Cream  4. Aestura Atobarrier365 Cream  5. Aveeno Calm + Restore Oat Gel Moisturizer
sponsored_units: none observed
screenshot_ref: none — not run_index 1
notes: language of the generated answer switched to Vietnamese for this run only (see deviations, region/language confound) — recorded verbatim in Vietnamese below, per protocol ("answer_text_verbatim... full answer, unedited").
```
answer_text_verbatim:
> Để chăm sóc làn da khô và nhạy cảm, các chuyên gia da liễu hàng đầu thường khuyên dùng các sản phẩm không chứa hương liệu, chất bảo quản hay cồn khô, đồng thời tích hợp các thành phần phục hồi như Ceramides, Glycerin và Axit Hyaluronic. Dưới đây là những loại kem dưỡng ẩm tốt nhất được các tạp chí uy tín và bác sĩ da liễu đánh giá cao:
>
> **CeraVe Moisturizing Cream** — 157.250 ₫ — Pharmacity và nhiều cửa hàng khác — 4.8 (73,1 N)
> Đánh giá chung: Lựa chọn hàng đầu của các bác sĩ da liễu nhờ sự kết hợp giữa 3 loại Ceramides thiết yếu và Axit Hyaluronic.
> Đặc điểm nổi bật: Công nghệ MVE giúp giải phóng độ ẩm suốt cả ngày, kết cấu kem dày mịn giúp khóa ẩm sâu mà không gây bết dính.
>
> **La Roche-Posay Toleriane Double Repair Face Moisturizer** — 610.002 ₫ (32,95 CA$) — Rosalinaboutique — 4.1 (4,9 N)
> Đánh giá chung: Thích hợp cho làn da nhạy cảm cần làm dịu tức thì và phục hồi hàng rào bảo vệ.
> Đặc điểm nổi bật: Chứa nước khoáng prebiotic nuôi dưỡng hệ vi sinh trên da, bổ sung Ceramide-3 và Niacinamide chống viêm.
>
> **Vanicream Moisturizing Cream** — 538.999 ₫ — Chiaki.vn — 5.0 (27)
> Đánh giá chung: Sản phẩm lý tưởng nhất dành cho làn da siêu nhạy cảm hoặc dễ bị kích ứng, dị ứng.
> Đặc điểm nổi bật: Công thức tối giản tối đa, loại bỏ hoàn toàn hương liệu, phẩm màu, paraben và lanolin.
>
> **Aestura Atobarrier365 Cream** — 1.331.970 ₫ (51,20 US$) — Global Amore Mall — 4.9 (523)
> Đánh giá chung: Kem dưỡng ẩm phục hồi chuẩn K-Beauty xuất sắc nhất dành cho da khô ráp.
> Đặc điểm nổi bật: Các hạt nang chứa phức hợp Ceramides, Cholesterol và Axit béo tự tan giúp củng cố hàng rào lipid cho da.
>
> **Aveeno Calm + Restore Oat Gel Moisturizer** — 977.777 ₫ — shopee.vn
> Đánh giá chung: Lựa chọn mỏng nhẹ lý tưởng nếu bạn không thích cảm giác quá dày đặc của kem truyền thống.
> Đặc điểm nổi bật: Chiết xuất từ yến mạch prebiotic giúp làm dịu vết đỏ, ngứa và phục hồi độ ẩm liên tục trong 24 giờ.
>
> Để giúp bạn tìm được sản phẩm ưng ý nhất, vui lòng cho biết: làn da có tình trạng đặc biệt (bong tróc, châm chích, mụn, viêm da cơ địa)? kết cấu đặc hay gel mỏng nhẹ? có cần SPF ban ngày không?
>
> [Right rail: Allure — "11 Best Face Moisturizers for Sensitive Skin That ... - Allure", 10 thg 3, 2026; Smytten — "9 Dermatologist Recommended Moisturizers for Dry Sensitive ...", 20 thg 8, 2026; Sasa Malaysia — "Best Moisturizers for Dry and Sensitive Skin: Ultimate Guide"]

**Run 5**
```
sample_id: google-ai-mode-2026-09-22-SK-01-r5
surface_url: https://www.google.com/search?q=best+moisturizer+for+dry+sensitive+skin&udm=50
timestamp_utc: 2026-09-22T15:19:17Z | local_utc_offset: unknown — surface displays none
region_observed: UI in Vietnamese; answer text in English; prices in VND with US$/CA$ parentheticals | search_toggle: not exposed | arm: main
answer_outcome: answered
brands_mentioned (order): Vanicream (Daily Facial Moisturizer), CeraVe (Moisturizing Cream), La Roche-Posay (Toleriane Double Repair Face Moisturizer)
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Vanicream Daily Facial Moisturizer  2. CeraVe Moisturizing Cream  3. La Roche-Posay Toleriane Double Repair Face Moisturizer
sponsored_units: none observed
screenshot_ref: none — not run_index 1
notes: —
```
answer_text_verbatim:
> Dermatologists broadly agree that the best moisturizers for dry, sensitive skin are fragrance-free, hypoallergenic creams formulated with barrier-repairing ingredients like ceramides, hyaluronic acid, and squalane. Leading expert sources like The New York Times Wirecutter and Allure consistently rank therapeutic, non-comedogenic formulas from dermatologist-trusted brands as the top choices to heal a compromised skin barrier without triggering irritation.
>
> Top product recommendations according to clinical and testing consensus include:
>
> **Vanicream Daily Facial Moisturizer** — 1.743.008 ₫ (67,00 US$) — Ubuy
> Best for Allergies: Features an ultra-minimalist, 19-ingredient formula.
> Irritant-Free: Completely free of dyes, fragrance, lanolin, and parabens.
> Key Ingredients: Formulated with hyaluronic acid, squalane, and ceramides.
>
> **CeraVe Moisturizing Cream** — 157.250 ₫ — Pharmacity và nhiều cửa hàng khác — 4.8 (73,1 N)
> Best for Severe Dryness: Provides deep, rich hydration with a thick, protective finish.
> Barrier Repair: Packed with three essential ceramides and hyaluronic acid.
> Long-Lasting: Uses MVE technology for sustained all-day moisture release.
>
> **La Roche-Posay Toleriane Double Repair Face Moisturizer** — 610.002 ₫ (32,95 CA$) — Rosalinaboutique — 4.1 (4,9 N)
> Best Lightweight Option: Absorbs quickly without feeling overly heavy or greasy.
> Microbiome Support: Blends prebiotic thermal water, ceramide-3, and niacinamide.
> Soothing Effect: Actively calms redness and irritation upon application.
>
> To find your perfect match, let me know:
> - Do you prefer a thick cream or a lightweight gel/lotion?
> - Are you dealing with specific concerns like eczema, rosacea, or acne?
> - Do you need a daytime moisturizer with integrated SPF?
>
> [Right rail: Allure — "11 Best Face Moisturizers for Sensitive Skin That ... - Allure", 10 thg 3, 2026; The New York Times — "The 7 Best Moisturizers of 2026 | Reviews by Wirecutter", 3 thg 4, 2026; Dr Sunil Kothiwala — "Top 10 Dermatologist Approved Face Moisturizers for Dry Skin -", 12 thg 3, 2026]

#### SK-02 — C — "best vitamin C serum under $50" — arm: main — achieved_n: 5/5

Note: one page load in this prompt's batch returned only unrendered CSS at the standard wait; a replacement run was fetched to reach n=5. `timestamp_utc` for all 5 runs below is one poll taken immediately after the last run's text extraction (`2026-09-22T15:22:33Z`) — this prompt's fetches were run as a batched sequence per the timestamp-batching deviation noted above; individual per-run times were not separately polled.

**Run 1** — `sample_id: google-ai-mode-2026-09-22-SK-02-r1` — region_observed: UI Vietnamese, answer English, VND/US$ prices — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): SkinCeuticals (comparison reference only, not recommended), Timeless Skin Care (20% C+E Ferulic Acid Serum), Naturium (Vitamin C Complex Serum), e.l.f. Skin (Bright Icon Vitamin C+E+Ferulic Serum), La Roche-Posay (Pure Vitamin C10 Serum), CeraVe (Skin Renewing Vitamin C Serum)
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Timeless Skin Care 20% C+E Ferulic Acid Serum  2. Naturium Vitamin C Complex Serum  3. e.l.f. Skin Bright Icon Vitamin C+E+Ferulic Serum  4. La Roche-Posay Pure Vitamin C10 Serum  5. CeraVe Skin Renewing Vitamin C Serum
sponsored_units: none observed | screenshot_ref: docs/raw/screenshots/ (temp path, see notes) | notes: —
> The best vitamin C serums under $50 provide exceptional, clinically backed results that rival luxury options like SkinCeuticals. For budget-friendly choices, dermatologists and beauty editors frequently recommend formulas that stabilize pure vitamin C (L-ascorbic acid) or use gentle derivatives to boost radiance without causing irritation. The top-rated vitamin C serums under $50 include: Timeless Skin Care 20% C + E Ferulic Acid Serum — Best For: The ultimate dupe for high-end luxury serums. Key Features: 20% L-ascorbic acid combined with vitamin E and ferulic acid, airtight pump bottle to minimize oxidation. Naturium Vitamin C Complex Serum — Best For: Sensitive skin or those looking for general value. Key Features: gold-stabilized pure vitamin C with sodium ascorbyl phosphate, glutathione, and hyaluronic acid; elegant, non-irritating, non-sticky finish. e.l.f. Skin Bright Icon Vitamin C + E + Ferulic Serum — 1.232.072 ₫ (47,36 US$), Herbkart.com, 4.2 (231) — Best For: Targeting intense hyperpigmentation on a tight budget. Key Features: 15% 3-O-ethyl ascorbic acid, vitamin E, ferulic acid. La Roche-Posay Pure Vitamin C10 Serum — 1.066.357 ₫ (40,99 US$), Klaptap, 4.9 (158) — Best For: Fine lines and textured or acne-prone skin. Key Features: 10% pure vitamin C with salicylic acid and hyaluronic acid. CeraVe Skin Renewing Vitamin C Serum — 1.140.499 ₫ (43,84 US$), Beauty Care Bag, 4.5 (598) — Best For: Restoring the skin barrier while brightening. Key Features: 10% pure L-ascorbic acid, three essential ceramides, hyaluronic acid. To help narrow down your choice: skin type? primary goal? [Right rail: The New York Times — "The 6 Best Vitamin C Serums of 2026 | Reviews by Wirecutter", 12 thg 8, 2026; Boston Derm Advocate — "Best Affordable Vitamin C Serums Under $50 Blind Tested by Dermatologists", 12 thg 2, 2026; Allure — "The Case for Buying Your Vitamin C Serum at the Drugstore", 24 thg 1, 2026]

**Run 2** — `sample_id: google-ai-mode-2026-09-22-SK-02-r2` — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Timeless Skin Care, e.l.f. Skin, Naturium, La Roche-Posay (Pure Vitamin C12 Serum — note: concentration named "C12" here vs "C10" in run 1, same product line, printed variant kept)
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Timeless Skin Care 20% C + E Ferulic Acid Serum  2. e.l.f. Skin Bright Icon Vitamin C + E + Ferulic Serum  3. Naturium Vitamin C Complex Serum  4. La Roche-Posay Pure Vitamin C12 Serum
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: —
> The best vitamin C serums under $50 include Timeless Skin Care and e.l.f. Skin, both highly rated by experts for offering clinical-grade brightening and antioxidant protection without the luxury price tag. Here are the top dermatologist-approved and editor-tested options under $50 tailored to different skin concerns: Timeless Skin Care 20% C + E Ferulic Acid Serum: Widely praised by reviewers at Wirecutter as the ultimate budget dupe for luxury formulas, it features a potent 20% L-ascorbic acid alongside vitamin E and ferulic acid to maximize potency and target hyperpigmentation. e.l.f. Skin Bright Icon Vitamin C + E + Ferulic Serum: Named the best overall drugstore vitamin C by Allure, this formula uses a 15% highly stable vitamin C derivative (EAA) and an airless pump to prevent premature oxidation. Naturium Vitamin C Complex Serum: A top value pick recommended by dermatologists for sensitive skin, blending a gold-stabilized pure L-ascorbic acid with a gentle sodium ascorbyl phosphate derivative to brighten without causing irritation. La Roche-Posay Pure Vitamin C12 Serum: The ideal choice for oily or acne-prone skin, pairing 12% pure vitamin C with salicylic acid (BHA) to refine skin texture and clear out pores while fading post-acne marks. To narrow down the list: skin type? primary skin concern? [Right rail: The New York Times — "The 6 Best Vitamin C Serums of 2026 | Reviews by Wirecutter", 12 thg 8, 2026; Allure — "The Case for Buying Your Vitamin C Serum at the Drugstore", 24 thg 1, 2026; YouTube · Dr. Daniel Sugai — "The Best Affordable Vitamin C Serums!", 23 thg 11, 2024]

**Run 3** — `sample_id: google-ai-mode-2026-09-22-SK-02-r3` — region_observed: UI Vietnamese, ANSWER BODY in Vietnamese this run — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Timeless Skin Care, La Roche-Posay (Pure Vitamin C12 Serum), Naturium
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Timeless Skin Care 20% C + E Ferulic Acid Serum  2. La Roche-Posay Pure Vitamin C12 Serum  3. Naturium Vitamin C Complex Serum
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: second Vietnamese-language full-answer run in this file (after SK-01 r4) — same region/language confound
> Khi lựa chọn serum vitamin C chất lượng cao có giá dưới 50 USD, các chuyên gia da liễu thường đánh giá cao ba sản phẩm nổi bật dưới đây nhờ tính ổn định của công thức và hiệu quả rõ rệt trên da: Timeless Skin Care 20% C + E Ferulic Acid Serum — Lựa chọn thay thế cao cấp tốt nhất: bản sao hoàn hảo của các dòng serum đắt đỏ. Công thức mạnh mẽ: 20% L-ascorbic acid, Vitamin E, Ferulic Acid. Kết cấu: dạng lỏng nhẹ, thấm nhanh, có thể châm chích nhẹ với người mới. La Roche-Posay Pure Vitamin C12 Serum — Dành cho da dầu và lão hóa: đứng đầu bình chọn của bác sĩ da liễu. Thành phần bổ trợ: 12% Vitamin C nguyên chất + Salicylic Acid (BHA). Độ dịu nhẹ: phù hợp da nhạy cảm nhờ Neurosensine và nước khoáng. Naturium Vitamin C Complex Serum — Dành cho da nhạy cảm: tối ưu cho ai không dung nạp L-ascorbic acid nồng độ cao. Công thức phức hợp: L-ascorbic acid vi nang + Sodium Ascorbyl Phosphate. Bảo quản tốt: vòi bơm kín khí. Để giúp bạn tìm sản phẩm ưng ý: loại da? vấn đề cần cải thiện? [Right rail: The New York Times — "The 6 Best Vitamin C Serums of 2026 | Reviews by Wirecutter", 12 thg 8, 2026; Allure — "The Case for Buying Your Vitamin C Serum at the Drugstore", 24 thg 1, 2026; YouTube · Dr. Daniel Sugai — "The Best Affordable Vitamin C Serums!", 23 thg 11, 2024]

**Run 4** — `sample_id: google-ai-mode-2026-09-22-SK-02-r4` — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Timeless Skin Care, Naturium, e.l.f. Skin
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Timeless Skin Care 20% C + E Ferulic Acid Serum  2. Naturium Vitamin C Complex Serum  3. e.l.f. Skin Bright Icon Vitamin C + E + Ferulic Serum
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: —
> The top dermatologist- and editor-vetted vitamin C serums under $50 include Timeless Skin Care, Naturium, and e.l.f. Skin, which deliver high-potency brightening and anti-aging benefits without luxury price tags. Timeless Skin Care 20% C + E Ferulic Acid Serum — Standout Quality: budget-friendly alternative to ultra-premium $180+ antioxidant formulas per Wirecutter. Key Specs: 20% L-ascorbic acid, vitamin E, ferulic acid. Naturium Vitamin C Complex Serum — Standout Quality: highly rated by NewBeauty testers for reactive/sensitive skin. Key Specs: stabilized complex of pure L-ascorbic acid and sodium ascorbyl phosphate encapsulated with gold particles. e.l.f. Skin Bright Icon Vitamin C + E + Ferulic Serum — Standout Quality: celebrated by Allure as an exceptional drugstore pick for hyperpigmentation. Key Specs: 15% 3-O-ethyl ascorbic acid, airtight pump packaging. To narrow down: skin type? primary skin goal? [Right rail: The New York Times — "The 6 Best Vitamin C Serums of 2026 | Reviews by Wirecutter", 12 thg 8, 2026; Allure — "The Case for Buying Your Vitamin C Serum at the Drugstore", 24 thg 1, 2026; Boston Derm Advocate — "Best Affordable Vitamin C Serums Under $50 Blind Tested by Dermatologists", 12 thg 2, 2026]

**Run 5** — `sample_id: google-ai-mode-2026-09-22-SK-02-r5` — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Timeless Skin Care, Naturium, Maelove (The Glow Maker Vitamin C Serum), e.l.f. Skin
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Timeless Skin Care 20% C + E Ferulic Acid Serum  2. Naturium Vitamin C Complex Serum  3. Maelove The Glow Maker Vitamin C Serum  4. e.l.f. Skin Bright Icon Vitamin C + E + Ferulic Serum
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: this run's `get_page_text` required an extended 10s wait after the standard batch's failed 5th slot; first valid extraction on this attempt
> Top-tier vitamin C serums do not require a luxury budget, as excellent formulations under $50 frequently stand up to prestige options costing triple the price. The best vitamin C serums under $50 excel at stabilizing the active ingredient, preventing early oxidation, and minimizing irritation. Timeless Skin Care 20% C + E Ferulic Acid Serum: Dermatologist Pick: ultimate budget dupe to luxury alternatives. Key Ingredients: 20% L-ascorbic acid, 1% vitamin E, 1% ferulic acid. Naturium Vitamin C Complex Serum: Best for Sensitive Skin: highly stable, non-irritating blend. Key Ingredients: L-ascorbic acid, sodium ascorbyl phosphate, glutathione, vitamin E. Maelove The Glow Maker Vitamin C Serum: Best for Dehydrated Skin: highly praised across Reddit communities for silky, lightweight texture that pairs seamlessly under makeup without pilling. Key Ingredients: 15% L-ascorbic acid, ferulic acid, vitamin E, hyaluronic acid. e.l.f. Skin Bright Icon Vitamin C + E + Ferulic Serum: Best for Oily & Acne-Prone Skin: 15% derivative in opaque pump bottle, top recognition from Allure. Key Ingredients: 15% 3-O-ethyl ascorbic acid, 1% vitamin E, 0.5% ferulic acid. To narrow down: skin type? primary skin concern? [Right rail: The New York Times — "The 6 Best Vitamin C Serums of 2026 | Reviews by Wirecutter", 12 thg 8, 2026; Boston Derm Advocate — "Best Affordable Vitamin C Serums Under $50 Blind Tested by Dermatologists", 12 thg 2, 2026; Reddit · r/40PlusSkinCare — "Favorite vitamin c serum under $50?", 1 thg 10, 2025]

#### SK-03 — C — "best sunscreen for daily use under makeup" — arm: main — achieved_n: 5/5

Run 2's exact timestamp poll was missed between two adjacent polls; recorded as interpolated and flagged `~approximate`.

**Run 1** — `sample_id: google-ai-mode-2026-09-22-SK-03-r1` — timestamp_utc: 2026-09-22T15:24:56Z — region_observed: UI Vietnamese, answer English, VND/MX$ prices — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Supergoop! (Unseen Sunscreen SPF 50), EltaMD (UV Clear Broad-Spectrum SPF 46), Tatcha (The Silk Sunscreen SPF 50)
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Supergoop! Unseen Sunscreen SPF 50  2. EltaMD UV Clear Broad-Spectrum SPF 46  3. Tatcha The Silk Sunscreen SPF 50
sponsored_units: none observed | screenshot_ref: docs/raw/screenshots/ (temp path, see notes) | notes: —
> The top sunscreens for daily wear under makeup are Supergoop! Unseen Sunscreen SPF 50 for a smooth, primer-like finish, EltaMD UV Clear Broad-Spectrum SPF 46 for sensitive or acne-prone skin, and Tatcha The Silk Sunscreen SPF 50 for a smooth, radiant base. Supergoop! Unseen Sunscreen SPF 50 — 1.702.729 ₫ (1.129,00 MX$), Accesorios Mexicali — Finish: completely invisible, weightless gel-cream texture, acts like a makeup primer. Skin Type: works across all skin tones without pilling or white cast. EltaMD UV Clear Broad-Spectrum SPF 46 — 895.000 ₫, Kuni shop và nhiều cửa hàng khác, 4.8 (18,2 N) — Benefits: niacinamide and hyaluronic acid calm redness, lock in moisture. Skin Type: recommended for sensitive, acne-prone, or rosacea-prone skin. Tatcha The Silk Sunscreen SPF 50 — 35.000 ₫, shopee.vn, 4.0 (2,7 N) — Finish: soft, velvety-smooth, radiant, glowy. Ingredients: hyaluronic acid and red algae. Apply sunscreen evenly and let absorb 60 seconds before foundation. To narrow down: skin type? makeup finish preferred? [Right rail: Glamour — "7 Best Sunscreens Under Makeup, According to ...", 14 thg 4, 2026; Who What Wear — "The 10 Best Sunscreens for Under Makeup in 2026, Per Experts", 10 thg 7, 2026; Ulta — "Best Sunscreen Under Makeup 2026 - Ulta Beauty"]

**Run 2** — `sample_id: google-ai-mode-2026-09-22-SK-03-r2` — timestamp_utc: 2026-09-22T15:25:10Z ~approximate (interpolated between adjacent polls 15:24:56Z and 15:25:29Z) — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): EltaMD (UV Clear Broad-Spectrum SPF 46), Supergoop! (Unseen Sunscreen SPF 50), Tatcha (The Milky Sunscreen SPF 50), La Roche-Posay (Anthelios Clear Skin Dry Touch Sunscreen SPF 60), The INKEY List (Polyglutamic Acid Dewy SPF 30 Sunscreen)
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. EltaMD UV Clear Broad-Spectrum SPF 46  2. Supergoop! Unseen Sunscreen SPF 50  3. Tatcha The Milky Sunscreen SPF 50  4. La Roche-Posay Anthelios Clear Skin Dry Touch Sunscreen SPF 60  5. The INKEY List Polyglutamic Acid Dewy SPF 30 Sunscreen
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: 5-brand list, longest of this prompt's runs.
> The most critical factor for a daily sunscreen worn under makeup is finding a lightweight formula that acts like a primer and prevents pilling, sliding, or caking. EltaMD UV Clear Broad-Spectrum SPF 46 — 895.000 ₫ — Best Overall: dermatologist favorite, layers seamlessly. Key Features: oil-free, niacinamide and hyaluronic acid. Supergoop! Unseen Sunscreen SPF 50 — 1.701.539 ₫ (1.129,00 MX$) — Best Primer Finish: invisible, weightless, scentless gel, velvety silicone-like matte finish. Tatcha The Milky Sunscreen SPF 50 — 949.905 ₫, shopee.vn, 4.8 (816) — Best for a Radiant Finish: luminous, soft-focus, ectoin and aloe. La Roche-Posay Anthelios Clear Skin Dry Touch Sunscreen SPF 60 — 425.000 ₫, Vinacine, 3.7 (1,7 N) — Best for Oily Skin: absorbs excess oil, dry-touch matte finish. The INKEY List Polyglutamic Acid Dewy SPF 30 Sunscreen — 1.045.787 ₫ (30,09 £), The Good Vibes, 4.4 (1 N) — Best Budget Choice: polyglutamic acid and squalane, dewy "glass skin" effect. Pro-tips: let sunscreen dry 10-15 min before foundation; match silicone-based sunscreen with silicone-based foundation. To narrow down: skin type? finish preferred? [Right rail: Glamour — "7 Best Sunscreens Under Makeup, According to ...", 14 thg 4, 2026; Who What Wear — "The 10 Best Sunscreens for Under Makeup in 2026, Per Experts", 10 thg 7, 2026; Glamour — "8 Best Face Sunscreens for Every Skin Type, Vetted by Dermatologists", 10 thg 4, 2026]

**Run 3** — `sample_id: google-ai-mode-2026-09-22-SK-03-r3` — timestamp_utc: 2026-09-22T15:25:29Z — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Supergoop! (Unseen Sunscreen SPF 50), EltaMD (UV Clear Broad-Spectrum SPF 46), Tatcha (The Milky Sunscreen SPF 50+)
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Supergoop! Unseen Sunscreen SPF 50  2. EltaMD UV Clear Broad-Spectrum SPF 46  3. Tatcha The Milky Sunscreen SPF 50+
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: —
> Finding the right sunscreen to wear under makeup depends on your skin type, but top-tier professional consensus highlights Supergoop! Unseen Sunscreen SPF 50 for a flawless velvet finish, EltaMD UV Clear Broad-Spectrum SPF 46 for acne-prone or sensitive skin, and Tatcha The Milky Sunscreen SPF 50+ for a hydration-boosting radiant glow. Supergoop! Unseen Sunscreen SPF 50 — 1.702.729 ₫ (1.129,00 MX$), Accesorios Mexicali — Best For: weightless, invisible gel primer. Texture: grippy, velvety, no white cast. Expert Notes: Friday Club Magazine praised pore-blurring performance. EltaMD UV Clear Broad-Spectrum SPF 46 — 895.000 ₫ — Best For: sensitive, oily, acne-prone skin. Ingredients: niacinamide, hyaluronic acid, lactic acid. Expert Notes: vetted by Glamour, layers without pilling. Tatcha The Milky Sunscreen SPF 50+ — 1.865.503 ₫, Fado.vn, 4.8 (816) — Best For: normal to dry skin, luminous dewy canvas. Texture: ultra-lightweight fluid serum. Expert Notes: Allure calls it ideal middle-ground, radiant sheen without grease. Pro tips: apply sunscreen as final skincare step; wait 60-90s before makeup; press don't rub. To narrow down: skin type? finish preferred? [Right rail: Glamour — "7 Best Sunscreens Under Makeup, According to ...", 14 thg 4, 2026; WWD — "Top Sunscreens to Wear Under Makeup 2026", 2 thg 9, 2026; Reddit · r/AsianBeauty — "Sunscreens that actually look good under makeup??", 4 thg 12, 2025]

**Run 4** — `sample_id: google-ai-mode-2026-09-22-SK-03-r4` — timestamp_utc: 2026-09-22T15:25:47Z — region_observed: UI Vietnamese, ANSWER BODY in Vietnamese this run — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Supergoop! (Unseen Sunscreen SPF 40 — note: SPF number differs from other runs' "SPF 50", printed variant kept), EltaMD (UV Clear Broad-Spectrum SPF 46), La Roche-Posay (Anthelios UVMune 400 Invisible Fluid SPF50+)
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Supergoop! Unseen Sunscreen SPF 40  2. EltaMD UV Clear Broad-Spectrum SPF 46  3. La Roche-Posay Anthelios UVMune 400 Invisible Fluid SPF50+
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: third Vietnamese-language full-answer run in this file (after SK-01 r4, SK-02 r3)
> Để có một lớp nền hoàn hảo không bị vón cục (pilling) hay trượt nền, các chuyên gia da liễu và các chuyên gia trang điểm đánh giá cao các dòng kem chống nắng có kết cấu mỏng nhẹ, thấm nhanh và có khả năng hoạt động như một lớp lót. Supergoop! Unseen Sunscreen SPF 40 — Công dụng tối ưu: hoạt động như kem lót vô hình, bám giữ trang điểm lâu trôi. Đặc tính: gel trong suốt, không vệt trắng, làm mờ lỗ chân lông. EltaMD UV Clear Broad-Spectrum SPF 46 — Công dụng tối ưu: da nhạy cảm, da mụn, da dễ mẩn đỏ. Đặc tính: Niacinamide và Hyaluronic Acid, không gây nhờn rít. La Roche-Posay Anthelios UVMune 400 Invisible Fluid SPF50+ — Công dụng tối ưu: kết cấu mỏng nhẹ như nước cho mọi loại da. Đặc tính: bảo vệ phổ rộng cao, thấm nhanh, không đổi tông kem nền. Mẹo: chờ 60 giây-3 phút trước khi trang điểm; dùng mút vỗ nhẹ thay vì chà xát. Để tư vấn thêm: loại da? phong cách nền matte hay dewy? [Right rail: Glamour — "7 Best Sunscreens Under Makeup, According to ...", 14 thg 4, 2026; WWD — "Top Sunscreens to Wear Under Makeup 2026", 2 thg 9, 2026; Who What Wear — "The 10 Best Sunscreens for Under Makeup in 2026, Per Experts"]

**Run 5** — `sample_id: google-ai-mode-2026-09-22-SK-03-r5` — timestamp_utc: 2026-09-22T15:26:06Z — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Supergoop! (Unseen Sunscreen SPF 50), EltaMD (UV Clear Broad-Spectrum SPF 46), Tatcha (The Silk Sunscreen SPF 50)
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Supergoop! Unseen Sunscreen SPF 50  2. EltaMD UV Clear Broad-Spectrum SPF 46  3. Tatcha The Silk Sunscreen SPF 50
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: same three-brand set and order as Run 1, prices differ slightly (Tatcha 25.000₫ vs 35.000₫ in run 1)
> The best sunscreens for daily wear under makeup are Supergoop! Unseen Sunscreen SPF 50 for a primer-like clear base, EltaMD UV Clear SPF 46 for sensitive or acne-prone skin, and Tatcha The Silk Sunscreen SPF 50 for a smooth, radiant finish. Supergoop! Unseen Sunscreen SPF 50 — 1.702.729 ₫ (1.129,00 MX$), Accesorios Mexicali — Standout Feature: clear gel-cream primer. Makeup Compatibility: grips foundation, prevents pilling. Finish: invisible, weightless satin-matte. EltaMD UV Clear Broad-Spectrum SPF 46 — 895.000 ₫ — Standout Feature: dermatologist-recommended for acne/rosacea. Makeup Compatibility: layers cleanly. Key Specs: niacinamide, hyaluronic acid. Tatcha The Silk Sunscreen SPF 50 — 25.000 ₫, shopee.vn, 4.0 (2,7 N) — Standout Feature: lightweight milky mineral formula. Makeup Compatibility: smooth velvety canvas. Finish: radiant, skin-smoothing glow. Pro tips: wait 60s before foundation; match water-based/silicone-based formulas. To narrow down: skin type? finish preferred? [Right rail: WWD — "Top Sunscreens to Wear Under Makeup 2026", 2 thg 9, 2026; Ulta — "Best Sunscreen Under Makeup 2026 - Ulta Beauty"]

#### SK-04 — C — "best retinol for beginners" — arm: main — achieved_n: 5/5

First run in this file to show a medical-disclaimer footer (Vietnamese): "Thông tin này chỉ nhằm mục đích tham khảo. Để được tư vấn hoặc chẩn đoán y tế, hãy tham khảo ý kiến của chuyên gia. Câu trả lời của AI có thể chứa thông tin không chính xác." ("This information is for reference only. For medical advice or diagnosis, consult a professional. The AI's answer may contain inaccurate information.") — present on all 5 runs of this prompt, not seen on SK-01/02/03. Recorded here once; not re-quoted per run below.

**Run 1** — `sample_id: google-ai-mode-2026-09-22-SK-04-r1` — timestamp_utc: 2026-09-22T15:27:31Z — region_observed: UI Vietnamese, answer English, VND prices — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): CeraVe (Resurfacing Retinol Serum), La Roche-Posay (Retinol B3 Serum), Olay (Regenerist Retinol 24 Night Moisturizer)
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. CeraVe Resurfacing Retinol Serum  2. La Roche-Posay Retinol B3 Serum  3. Olay Regenerist Retinol 24 Night Moisturizer
sponsored_units: none observed | screenshot_ref: docs/raw/screenshots/ (temp path, see notes) | notes: medical disclaimer footer present (see above)
> There is no single "absolute best" retinol for everyone, but dermatologists generally recommend starting with low-concentration (0.1% to 0.3%) or encapsulated formulas to minimize irritation. CeraVe Resurfacing Retinol Serum — 1.225.569 ₫, Beauty Buddy, 4.7 (8 N) — Best For: beginners with post-acne marks and uneven texture. Key Features: 0.3% encapsulated retinol, ceramides, niacinamide. La Roche-Posay Retinol B3 Serum — 409.600 ₫, Chiaki.vn và nhiều cửa hàng khác, 4.5 (8,1 N) — Best For: sensitive/reactive skin. Key Features: gradual-release retinol + 10% Vitamin B3. Olay Regenerist Retinol 24 Night Moisturizer — 439.000 ₫, VnShop.vn và nhiều cửa hàng khác, 4.7 (3,5 N) — Best For: dry skin, one-step routine. Key Features: fragrance-free retinoid complex + amino peptides. Beginner tips: pea-sized amount, dry skin, 2 nights/week increasing gradually, always sunscreen next morning. To narrow down: skin type? main skin goals? [Right rail: The Amaranthine Collective — "Best Retinol for Beginners: A Dermatologist's Guide (2026 Update)", 7 thg 5, 2026; Space NK — "Your Ultimate Beginner's Guide To Retinol", 23 thg 12, 2025; Glamour — "6 Best Retinol Products for Beginners, Approved by Dermatologists", 26 thg 2, 2026]

**Run 2** — `sample_id: google-ai-mode-2026-09-22-SK-04-r2` — timestamp_utc: 2026-09-22T15:27:47Z ~approximate (interpolated between adjacent polls 15:27:31Z and 15:28:04Z) — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): CeraVe (Resurfacing Retinol Serum), La Roche-Posay (Retinol B3 Serum), The Ordinary (Retinol 0.2% in Squalane), Olay (Regenerist Retinol 24 Night Moisturizer)
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. CeraVe Resurfacing Retinol Serum  2. La Roche-Posay Retinol B3 Serum  3. The Ordinary Retinol 0.2% in Squalane  4. Olay Regenerist Retinol 24 Night Moisturizer
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: —
> The best retinols for beginners are low-concentration, encapsulated formulas. CeraVe Resurfacing Retinol Serum: Best Overall Beginner Pick — encapsulated retinol, slow release; ceramides, niacinamide, hyaluronic acid. La Roche-Posay Retinol B3 Serum: Best for Sensitive Skin — 0.3% gradual-release retinol + vitamin B3; silky, lightweight. The Ordinary Retinol 0.2% in Squalane: Best Budget Pick — transparent low-percentage pure retinol in squalane base. Olay Regenerist Retinol 24 Night Moisturizer: Best Cream Option — fragrance-free retinoid complex + amino peptides. Beginner rules: start low/go slow (1-2 nights/week, scale over 4-6 weeks); always SPF 30+; skip layering with AHA/BHA/benzoyl peroxide. To narrow down: skin type? skin concern? [Right rail: The Amaranthine Collective — "Best Retinol for Beginners: A Dermatologist's Guide (2026 Update)", 7 thg 5, 2026; Glamour — "6 Best Retinol Products for Beginners, Approved by Dermatologists", 26 thg 2, 2026; Space NK — "Your Ultimate Beginner's Guide To Retinol", 23 thg 12, 2025]

**Run 3** — `sample_id: google-ai-mode-2026-09-22-SK-04-r3` — timestamp_utc: 2026-09-22T15:28:04Z — region_observed: UI Vietnamese, ANSWER BODY in Vietnamese this run — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): CeraVe (Resurfacing Retinol Serum), Medik8 (Crystal Retinal 3), La Roche-Posay (Retinol B3 Serum)
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. CeraVe Resurfacing Retinol Serum  2. Medik8 Crystal Retinal 3  3. La Roche-Posay Retinol B3 Serum
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: fourth Vietnamese-language full-answer run in this file (SK-01 r4, SK-02 r3, SK-03 r4)
> Các loại retinol cho người mới bắt đầu tốt nhất cần có nồng độ thấp (khoảng 0,1%-0,3%) hoặc công nghệ bọc, kết hợp ceramides, niacinamide, hyaluronic acid. Ba sản phẩm hàng đầu theo Forbes Vetted và Wirecutter: CeraVe Resurfacing Retinol Serum — 1.225.569 ₫, Beauty Buddy, 4.7 (8 N) — sản phẩm bình dân tối ưu, retinol bọc + 3 ceramides. Medik8 Crystal Retinal 3 — 1.466.113 ₫ (79,20 AU$), Ascent Luxury Cosmetics, 4.8 (223) — retinaldehyde nhanh gấp 11 lần retinol, nồng độ 0,03% êm dịu. La Roche-Posay Retinol B3 Serum — 409.600 ₫, Chiaki.vn và nhiều cửa hàng khác, 4.5 (8,1 N) — retinol giải phóng chậm + Vitamin B3. Hướng dẫn: 2 đêm/tuần 2 tuần đầu rồi tăng dần; lượng bằng hạt đậu; SPF 30+ ban ngày. Để tư vấn thêm: loại da? mục tiêu chính? [Right rail: The New York Times — "The 7 Best Retinol Products of 2026 | Reviews by Wirecutter", 22 thg 6, 2026; The Amaranthine Collective — "Best Retinol for Beginners: A Dermatologist's Guide (2026 Update)", 7 thg 5, 2026; Glamour — "6 Best Retinol Products for Beginners, Approved by Dermatologists", 26 thg 2, 2026]

**Run 4** — `sample_id: google-ai-mode-2026-09-22-SK-04-r4` — timestamp_utc: 2026-09-22T15:28:23Z — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): CeraVe (Resurfacing Retinol Serum), The Ordinary (Retinol 0.2% in Squalane), Medik8 (Crystal Retinal 1), First Aid Beauty (Retinol Serum 0.25% for Sensitive Skin)
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. CeraVe Resurfacing Retinol Serum  2. The Ordinary Retinol 0.2% in Squalane  3. Medik8 Crystal Retinal 1  4. First Aid Beauty Retinol Serum 0.25% for Sensitive Skin
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: —
> For beginners, the best retinol options balance gentle efficacy with skin-soothing ingredients, with CeraVe Resurfacing Retinol Serum and The Ordinary Retinol 0.2% in Squalane standing out as top dermatologist-approved choices. CeraVe Resurfacing Retinol Serum — 481.500 ₫, Pharmacity và nhiều cửa hàng khác, 4.7 (8 N) — encapsulated retinol + ceramides + niacinamide. The Ordinary Retinol 0.2% in Squalane — 231.355 ₫, drnutrition.com và nhiều cửa hàng khác, 4.6 (20,1 N) — low-concentration pure retinol in squalane. Medik8 Crystal Retinal 1 — 1.396.815 ₫ (75,50 AU$), Olimpia Beauty Clinic, 4.7 (12 N) — progressive low-strength retinal system. First Aid Beauty Retinol Serum 0.25% for Sensitive Skin — 3.430.350 ₫, The Good Vibes — micro-dose pure retinol + peptides. To narrow down: skin concern? sensitive/dry/oily? [Right rail: The Amaranthine Collective — "Best Retinol for Beginners 2026: 7 Derm-Approved Picks", 7 thg 5, 2026; smartaginglab.com — "Best Retinol for Beginners Over 30: Safe & Affordable Options", 4 thg 3, 2026; daithpiercing.io — "Best Retinol for Beginners: 2026 Starter Guide & Strengths"]

**Run 5** — `sample_id: google-ai-mode-2026-09-22-SK-04-r5` — timestamp_utc: 2026-09-22T15:28:41Z — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): La Roche-Posay (Retinol B3 Serum), CeraVe (Resurfacing Retinol Serum), Kiehl's (Skin-Renewing Daily Micro-Dose Serum), Medik8 (Crystal Retinal 3)
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. La Roche-Posay Retinol B3 Serum  2. CeraVe Resurfacing Retinol Serum  3. Kiehl's Skin-Renewing Daily Micro-Dose Serum  4. Medik8 Crystal Retinal 3
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: —
> The best retinol for beginners should have a low concentration (0.1% to 0.3%), an encapsulated formula, or soothing ingredients. Top choices: La Roche-Posay Retinol B3 Serum — 409.600 ₫ — Best Overall: 0.3% gradual-release + vitamin B3. CeraVe Resurfacing Retinol Serum — 481.500 ₫ — Best Drugstore: ceramides + licorice root extract, fades post-acne marks. Kiehl's Skin-Renewing Daily Micro-Dose Serum — 2.218.000 ₫, Wowmart VN và nhiều cửa hàng khác, 4.6 (9,7 N) — Best Micro-dose: low-dose retinol + peptides + ceramides. Medik8 Crystal Retinal 3 — 1.609.575 ₫ (87,00 AU$), Olimpia Beauty Clinic, 4.7 (12 N) — Best Progressive Option: 0.03% encapsulated retinaldehyde. Practices: "Low and Slow" (2 nights/week); "Sandwich Method" for sensitive skin; SPF 30+ daily. To narrow down: skin type? skin goal? [Right rail: The Amaranthine Collective — "Best Retinol for Beginners: A Dermatologist's Guide (2026 Update)", 7 thg 5, 2026; Glamour — "6 Best Retinol Products for Beginners, Approved by Dermatologists", 26 thg 2, 2026; Space NK — "Your Ultimate Beginner's Guide To Retinol", 23 thg 12, 2025]

### Vertical: B2B SaaS

#### BS-01 — C — "best help desk software for a 50-person support team" — arm: main — achieved_n: 5/5

Every run this prompt rendered a comparison table (markdown-style, reproduced as a table below) plus prose review sections — first prompt in this file to do so. Pricing appears per vendor per run; kept verbatim, not cross-checked, varies run to run (e.g. Zendesk "$55-$115+/agent/tháng" run 1 vs "$19-$115+/agent/tháng" run 3 vs "$2,750-$5,750 (50 seats)" run 2).

**Run 1** — `sample_id: google-ai-mode-2026-09-22-BS-01-r1` — timestamp_utc: 2026-09-22T15:29:? — polled 2026-09-22T15:29:54Z (next message, closest available) — region_observed: UI Vietnamese, ANSWER BODY in Vietnamese — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Zendesk (Suite), Freshdesk, Help Scout, Jira Service Management
brands_cited: none observed (right-rail links Enjo AI, www.console.com, saascrmreview.com — third-party publishers, not brand domains)
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Zendesk Suite  2. Freshdesk  3. Help Scout  4. Jira Service Management
sponsored_units: none observed | screenshot_ref: docs/raw/screenshots/ (temp path, see notes) | notes: table columns: Phần mềm | Phù hợp nhất cho | Ưu điểm cốt lõi | Mức giá ước tính
> Table: Zendesk Suite — Đội ngũ cần tùy biến sâu & Đa kênh toàn diện — Hệ sinh thái app khổng lồ, quản lý SLA và trigger cực mạnh — $55-$115+/agent/tháng. Freshdesk — Tối ưu chi phí & Hỗ trợ AI — Giao diện thân thiện, AI (Freddy) mạnh mẽ — $15-$79/agent/tháng. Help Scout — Đội ngũ SaaS/B2B ưu tiên tinh gọn — Shared inbox sạch sẽ — $22-$65/agent/tháng. Jira Service Management — Đội ngũ hỗ trợ kỹ thuật/IT nội bộ — Kết nối hoàn hảo với Jira Software — tùy gói.
> Prose: 1. Zendesk Suite — tiêu chuẩn vàng ngành, xử lý trigger/macro/SLA mượt mà, Omnichannel Agent Workspace; điểm lưu ý: chi phí đắt đỏ nhất. 2. Freshdesk — đối thủ cạnh tranh trực tiếp, giá dễ thở hơn, ticketing + chatbot + báo cáo, AI tóm tắt/đề xuất câu trả lời; điểm lưu ý: hệ sinh thái kém đa dạng hơn Zendesk. 3. Help Scout — giao diện tối giản như Gmail, email phản hồi tự nhiên không có ticket ID; điểm lưu ý: thiếu công cụ quản lý quy trình nâng cao. 4. Jira Service Management — liên kết trực tiếp Atlassian Jira; điểm lưu ý: giao diện kỹ thuật cao, không tối ưu cho CSKH thương mại. To narrow down: kênh hỗ trợ chính? external hay internal? CRM hiện có? [Right rail: saascrmreview.com — "20 Best Help Desk Software 2026: Pricing, AI Fees & Fit", 7 thg 7, 2026; www.console.com — "Best IT Help Desk Software in 2026: 10 Platforms Compared", 10 thg 2, 2026; Enjo AI — "7 Best Helpdesk Ticketing Systems for Small Teams in 2026", 17 thg 9, 2026]

**Run 2** — `sample_id: google-ai-mode-2026-09-22-BS-01-r2` — timestamp_utc: 2026-09-22T15:29:54Z — region_observed: UI Vietnamese, answer English, USD monthly totals for 50 seats — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Zendesk (Suite), Freshdesk (Omni), Help Scout
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Zendesk Suite  2. Freshdesk Omni  3. Help Scout
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: pricing given as total monthly cost for 50 seats, not per-agent: Zendesk $2,750-$5,750; Freshdesk Omni $1,450-$3,950; Help Scout $1,250-$2,250
> For a 50-person support team, you have transitioned past lightweight starter apps but want to avoid the massive configuration overhead of enterprise platforms. Zendesk Suite — Omnichannel, scaling, hyper-customization — vast app marketplace, deep data customization; note Zendesk Copilot add-on $50/agent/mo can push pricing higher. Freshdesk Omni — Omnichannel on a budget — fast setup, feature-rich ticketing at lower cost; Pro tier automated routing, live dashboards. Help Scout — Simple, email-first — zero learning curve, shared inbox; Plus plan connects to Jira, Salesforce, HubSpot CRM. To narrow down: primary communication channel? internal IT or external support? [Right rail: www.deskhero.com — "The Best Zoho Desk Alternatives for SMB Support Teams", 1 thg 8, 2026; saascrmreview.com — "20 Best Help Desk Software 2026: Pricing, AI Fees & Fit", 7 thg 7, 2026; Alloy Software — "Best Help Desk Software in 2026: Tested, Ranked & Compared", 8 thg 8, 2026]

**Run 3** — `sample_id: google-ai-mode-2026-09-22-BS-01-r3` — timestamp_utc: 2026-09-22T15:30:26Z — region_observed: UI Vietnamese, ANSWER BODY in Vietnamese — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Zendesk (Suite), Freshdesk, Help Scout, Jira Service Management, Freshservice
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Zendesk Suite  2. Freshdesk  3. Help Scout  4. Jira Service Management  5. Freshservice
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: fifth Vietnamese-language full-answer run in this file overall, first in B2B SaaS vertical; table price ranges differ from run 1 (Zendesk "$19-$115+" here vs "$55-$115+" run 1)
> Table: Zendesk Suite — mở rộng quy mô toàn diện — báo cáo chuyên sâu, đa kênh nâng cao — $19-$115+/agent/tháng. Freshdesk — tối ưu chi phí & đa kênh — dễ triển khai, AI, có bản miễn phí — $15-$79/agent/tháng. Help Scout — B2B/SaaS tinh gọn — shared inbox thân thiện — ~$22-$65/user/tháng. Jira Service Management — IT nội bộ — hệ sinh thái Atlassian — tùy gói.
> Prose adds a 4th section merging JSM và Freshservice as "Dành riêng cho IT Support": JSM bắt buộc nếu đã dùng Jira Software; Freshservice — ITSM trên cloud, quản lý tài sản thiết bị gọn gàng. To narrow down: external hay internal? kênh liên hệ chính? ngân sách/nhân sự/tháng? [Right rail: saascrmreview.com — "20 Best Help Desk Software 2026: Pricing, AI Fees & Fit", 7 thg 7, 2026; www.deskhero.com — "The Best Zoho Desk Alternatives for SMB Support Teams", 1 thg 8, 2026; Enjo AI — "7 Best Helpdesk Ticketing Systems for Small Teams in 2026", 17 thg 9, 2026]

**Run 4** — `sample_id: google-ai-mode-2026-09-22-BS-01-r4` — timestamp_utc: 2026-09-22T15:30:45Z — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Zendesk (Suite), Freshdesk, Help Scout, Intercom, Gorgias, HaloITSM, Jira Service Management
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Zendesk  2. Freshdesk  3. Help Scout  4. HaloITSM / Jira Service Management (tied, "if internal IT team" branch, tie:yes)
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: widest brand set of this prompt (7 distinct); Intercom and Gorgias appear only in the comparison table, not in the "Deep Dive: 4 Best Options" prose section
> Table: Zendesk Suite (Advanced workflows & operations), Freshdesk (Multi-channel value), Help Scout (Uncluttered email-first B2B), Intercom (AI-first SaaS companies — native in-app messaging, autonomous AI resolutions), Gorgias (E-commerce brands — Shopify/Magento integrations). Deep Dive: 1. Zendesk — best for process-heavy operations, unmatched marketplace, setup can take weeks. 2. Freshdesk — best all-rounder value, competitive pricing, built-in AI assistant. 3. Help Scout — best for simple customer interactions, zero training time; not built for heavy phone centers. 4. HaloITSM or Jira Service Management — best if internal IT team, ITIL-aligned. To narrow down: external or internal? industry? budget/agent seat? [Right rail: saascrmreview.com — "20 Best Help Desk Software 2026: Pricing, AI Fees & Fit", 7 thg 7, 2026; Salesforce — "The 8 Best Help Desk Software Options for Small Teams", 3 thg 2, 2026; www.deskhero.com — "The Best Zoho Desk Alternatives for SMB Support Teams", 1 thg 8, 2026]

**Run 5** — `sample_id: google-ai-mode-2026-09-22-BS-01-r5` — timestamp_utc: 2026-09-22T15:31:05Z — region_observed: UI Vietnamese, ANSWER BODY in Vietnamese — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Zendesk, Freshdesk, Help Scout, Intercom, Jira Service Management
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Zendesk Suite  2. Freshdesk (Freshworks)  3. Help Scout  4. Intercom
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: table lists Jira Service Management as a 5th row but the prose "Chi tiết các lựa chọn hàng đầu" section only numbers 1-4 (Zendesk, Freshdesk, Help Scout, Intercom) and does not give JSM its own numbered write-up this run — recorded as mentioned but not individually recommended in prose, still counted as recommended via the table row (Phù hợp nhất cho: "Đội ngũ IT nội bộ/Kỹ thuật")
> Table: Zendesk (Quy trình phức tạp, đa kênh sâu), Freshdesk (ROI tối ưu), Help Scout (B2B, đơn giản), Intercom (SaaS, AI-first — chatbot AI "Fin"), Jira Service Management (IT nội bộ/kỹ thuật, chuẩn ITIL). Prose 1-4: Zendesk — tiêu chuẩn ngành cho ticket phức tạp, cần admin chuyên trách. 2. Freshdesk — ROI tốt nhất, triển khai nhanh, Freddy AI. 3. Help Scout — đơn giản cá nhân hóa, email thuần túy không ticket ID. 4. Intercom — AI-first cho SaaS, Intercom Fin tự động giải quyết FAQ. Quyết định nhanh: Live Chat/In-app → Intercom; Email+thoại+form → Freshdesk/Zendesk; có admin → Zendesk; không có → Freshdesk/Help Scout. To narrow down: customer support hay IT helpdesk? kênh chính? ngân sách/người/tháng? [Right rail: saascrmreview.com — "20 Best Help Desk Software 2026: Pricing, AI Fees & Fit", 7 thg 7, 2026; serviahelpdesk.com — "5 Best Helpdesk Software for SaaS Companies in 2026", table; www.deskhero.com — "The Best Zoho Desk Alternatives for SMB Support Teams", 1 thg 8, 2026]

#### BS-02 — C — "best CRM for a B2B startup under 20 employees" — arm: main — achieved_n: 5/5

All 5 runs answered in English this time (no Vietnamese full-answer run for this prompt — contrast with SK-01/02/03/04 and BS-01, which each had at least one Vietnamese run). Every run rendered a comparison table plus per-vendor prose.

**Run 1** — `sample_id: google-ai-mode-2026-09-22-BS-02-r1` — timestamp_utc: 2026-09-22T15:32:26Z — region_observed: UI Vietnamese, answer English, USD pricing — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): HubSpot (CRM), Pipedrive, Salesflare, Attio, OneSuite
brands_cited: none observed (right-rail onesuite.io, www.dench.com, Instantly, Stack BD — third-party publishers)
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. HubSpot CRM  2. Pipedrive  3. Salesflare  4. Attio  5. OneSuite
sponsored_units: none observed | screenshot_ref: docs/raw/screenshots/ (temp path, see notes) | notes: —
> The best CRM for a B2B startup under 20 employees depends on your specific workflow, but HubSpot CRM is the top overall choice for its generous free tier and scaling potential, while Pipedrive is best for pure sales pipeline tracking, and Salesflare excels at automated data entry. Table: HubSpot — Free tier; paid $20-$100+/seat/mo — Inbound marketing & sales alignment — advanced features get expensive. Pipedrive — $14-$99/user/mo — Visual sales pipeline tracking — sales-only, no delivery/invoicing. Salesflare — $39-$124/user/mo — Zero-data-entry automated logging — less advanced custom reporting. Attio — free up to 3 users, paid from $36/user/mo — tech-savvy, object-based — steeper learning curve. OneSuite — $29-$149/month — service agencies (CRM+delivery+invoicing) — not for massive enterprise. Recommendations: HubSpot (Best Free-to-Scale) — free tier unlimited users, 1M contacts. Pipedrive (Best Pure Sales Execution) — kanban deal tracking. Salesflare (Best for Hating Data Entry) — auto-pulls from calendars/LinkedIn/email signatures. Attio (Best Modern/Custom) — relational database/Notion hybrid. OneSuite (Best All-in-One for Service Startups) — CRM+e-signatures+invoicing. To narrow down: inbound/marketing-led or outbound? project management/invoicing needed? [Right rail: onesuite.io — "Best CRM for B2B Startups: 7 Tools That Won't Bankrupt You", 17 thg 4, 2026; Instantly — "Best B2B Sales CRM for Startups: 0 to 100 Meetings", 15 thg 1, 2026; Stack BD — "The Best Free CRM for B2B Sales: HubSpot vs. Zoho vs..."]

**Run 2** — `sample_id: google-ai-mode-2026-09-22-BS-02-r2` — timestamp_utc: 2026-09-22T15:32:41Z ~approximate (interpolated between adjacent polls) — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): HubSpot (CRM), Pipedrive, Salesflare, Attio, Zoho (CRM)
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. HubSpot CRM  2. Pipedrive  3. Salesflare  4. Attio  5. Zoho CRM
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: includes two "Community Perspectives" quoted testimonials — one attributed "Reddit · r/CRM · 2 years ago" (praises HubSpot over Zoho), one attributed "onesuite.io · 5 months ago" (praises Attio) — these are third-party quotes embedded in the AI answer, not brand-controlled content; not counted as brand citations
> The best CRM for a B2B startup under 20 employees is HubSpot CRM for general inbound/marketing-to-sales alignment, or Pipedrive for a pure, low-friction sales pipeline, with Salesflare or Attio as top alternatives. Table: HubSpot CRM — free tier, paid from $20/seat/mo — generous free contact tier. Pipedrive — $14-$19/user/month — dead-simple Kanban. Salesflare — from $39/user/month — pulls contacts automatically. Attio — free tier, paid from $36/user/mo — flexible object-based. Zoho CRM — free up to 3 users, paid from $23/seat/mo — massive ecosystem, low-cost automation. Recommendations: HubSpot CRM (content/inbound-driven, free plan to 1M contacts). Pipedrive (outbound/activity-driven, visual board). Salesflare (poor CRM data hygiene, auto-sync). Attio (modern product-led startups, relational DB layout). Community quotes as above. To narrow down: inbound or outbound? PM/invoicing tied to CRM? [Right rail: onesuite.io — "Best CRM for B2B Startups: 7 Tools That Won't Bankrupt You", 17 thg 4, 2026; www.dench.com — "Best CRM for B2B Startups in 2026 - Dench", 26 thg 3, 2026; Briced — "Best CRM for Small B2B Sales Teams in 2026 (Under 20 People)", 21 thg 6, 2026]

**Run 3** — `sample_id: google-ai-mode-2026-09-22-BS-02-r3` — timestamp_utc: 2026-09-22T15:32:57Z — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): HubSpot, Pipedrive, Salesflare, Attio, Zoho (CRM)
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. HubSpot  2. Pipedrive  3. Salesflare  4. Attio  5. Zoho CRM
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: —
> HubSpot CRM is the overall best CRM for a B2B startup under 20 employees because its generous free tier handles core contact management and pipelines without upfront seat costs. HubSpot — best for inbound/general alignment, free user limits. Pipedrive — best for pure visual pipeline tracking, affordable, lacks post-sale/marketing tools. Salesflare — best for hating manual data entry, auto-builds address books. Attio — best for tech-savvy founders, object-based relational DB, Notion-like, steeper learning curve. Zoho CRM — best for budget-friendly customisation, Zoho One ecosystem. Table: same 5 platforms with pricing models and free-tier limits (HubSpot unlimited free users; Pipedrive/Salesflare trial only; Attio/Zoho 3 free users). To narrow down: inbound vs outbound? post-sale project tracking/invoicing? [Right rail: Stack BD — "The Best Free CRM for B2B Sales: HubSpot vs. Zoho vs..."; onesuite.io — "Best CRM for B2B Startups: 7 Tools That Won't Bankrupt You", 17 thg 4, 2026; Attio — "Best CRMs for small business in 2026 - Attio", 24 thg 7, 2026]

**Run 4** — `sample_id: google-ai-mode-2026-09-22-BS-02-r4` — timestamp_utc: 2026-09-22T15:33:16Z — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): HubSpot (CRM), Pipedrive, Salesflare, Attio, Zoho CRM
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. HubSpot CRM  2. Pipedrive  3. Salesflare  4. Attio  5. Zoho CRM
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: same 5-brand set as runs 2-3, fourth consecutive run with this set
> The best CRM for a B2B startup under 20 employees is HubSpot CRM for inbound-heavy teams, Pipedrive for pure sales pipeline tracking ($14-$99/user/month), or Salesflare ($39/user/month) if your team hates manual data entry. Table: HubSpot (free or $20-$100+/user/mo, unlimited free users/1M contacts), Pipedrive ($14-$99/user/mo, 14-day trial), Salesflare ($39-$124/user/mo, 14-day trial), Attio (free to $86+/user/mo, free up to 3 users), Zoho CRM (free or tiered, free up to 3 users). "How to Choose": HubSpot if inbound/content-driven; Pipedrive if sales-led Kanban; Salesflare if team forgets to log contacts; Attio if Notion-like custom objects wanted. To narrow down: lead source? budget/user/month? [Right rail: onesuite.io — "Best CRM for B2B Startups: 7 Tools That Won't Bankrupt You", 17 thg 4, 2026; Attio — "Best CRMs for small business in 2026 - Attio", 24 thg 7, 2026; Instantly — "Best B2B Sales CRM for Startups: 0 to 100 Meetings", 15 thg 1, 2026]

**Run 5** — `sample_id: google-ai-mode-2026-09-22-BS-02-r5` — timestamp_utc: 2026-09-22T15:33:36Z — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): HubSpot (CRM), Pipedrive, Salesflare, Attio, Zoho CRM
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. HubSpot CRM  2. Pipedrive  3. Salesflare  4. Attio  5. Zoho CRM
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: same 5-brand set as runs 2-4, fifth consecutive run — this prompt's brand set is highly stable across runs (HubSpot/Pipedrive/Salesflare/Attio in all 5; Zoho CRM in 4/5, OneSuite only in run 1)
> The best CRM for a B2B startup under 20 employees is HubSpot CRM for inbound-heavy teams needing a generous free tier, Pipedrive for pure sales pipeline tracking, or Salesflare for zero-data-entry automation. Table: HubSpot CRM (free + $20-$100+/user/mo, unlimited free users/1M contacts), Pipedrive ($14-$99/user/mo, trial only), Salesflare ($39-$124/user/mo, 14-day trial), Attio (free + $36-$86+/user/mo, up to 3 free users), Zoho CRM (free + per-seat lower tiers, max 3 free users). Breakdown: HubSpot for content/inbound/email tracking. Pipedrive for clean drag-and-drop Kanban, stops after deal won. Salesflare auto-captures from digital footprint. Attio flexible relational DB, Notion-like. Zoho CRM modular, scales across native business apps (accounting, mail, inventory). To narrow down: sales motion? invoicing/PM integration needed? [Right rail: onesuite.io — "Best CRM for B2B Startups: 7 Tools That Won't Bankrupt You", 17 thg 4, 2026; Attio — "Best CRMs for small business in 2026 - Attio", 24 thg 7, 2026; Salesforce — "Best Free CRMs For Startups and SMBs in 2026 | Salesforce AP", 4 thg 2, 2026]

#### BS-03 — C — "best project management tool for a remote engineering team" — arm: main — achieved_n: 5/5

All 5 runs answered in English. Linear and Jira are the top-2 in every run; ClickUp appears in 4/5.

**Run 1** — `sample_id: google-ai-mode-2026-09-22-BS-03-r1` — timestamp_utc: 2026-09-22T15:34:38Z — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Linear, Jira, Shortcut, ClickUp
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Linear  2. Jira  3. Shortcut  4. ClickUp
sponsored_units: none observed | screenshot_ref: docs/raw/screenshots/ (temp path, see notes) | notes: —
> The best project management tool for a remote engineering team is Linear for pure software development speed, or Jira if you require deep enterprise customization and compliance. Table: Linear — free tier, paid from ~$8/seat — keyboard-driven UI, deep GitHub/GitLab integration. Jira — free up to 10 users, paid from ~$8.15/seat — massive customization, audit/compliance controls. Shortcut — free tier, paid from ~$8.50/seat — epics/roadmaps/stories, developer-friendly. ClickUp — free tier, paid from ~$7/seat — infinite views, in-app docs. How to choose: Linear for velocity/aesthetic; Jira for enterprise cross-team/security/Scrum governance; Shortcut for Jira's power without config curve; ClickUp for non-technical dept collaboration. To narrow down: team size? strictly async across timezones? [Right rail: WorksBuddy — "7 Best Project Management Tools for Remote Teams in 2026", 5 thg 5, 2026; Shortcut — "Best Project Management Tools for Engineering Teams in 2026", 30 thg 10, 2025; Baserow — "Best Project Management Tool for Remote Engineering Teams", 1 thg 9, 2026]

**Run 2** — `sample_id: google-ai-mode-2026-09-22-BS-03-r2` — timestamp_utc: 2026-09-22T15:34:54Z ~approximate (interpolated) — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Linear, Jira, ClickUp, Notion, Asana
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Linear  2. Jira  3. ClickUp  4. Notion  5. Asana
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: —
> Linear if you want lightning-fast speed and developer-focused workflows, or Jira if you need enterprise-grade scale and custom Agile governance. Table: Linear (~$8, GitHub integration), Jira (free to 10 users then ~$8.15, Scrum/Kanban backlogs), ClickUp (~$7, config options/docs/workload views), Notion (~$10, unifies specs/wikis/task DBs), Asana (~$10.99, timeline views/dependencies). Key criteria: async-ready context, Git/CI-CD integrations, low admin friction. To narrow down: team size? non-technical stakeholder access needed? [Right rail: WorksBuddy — "7 Best Project Management Tools for Remote Teams in 2026", 5 thg 5, 2026; Baserow — "Best Project Management Tool for Remote Engineering Teams", 1 thg 9, 2026; Shortcut — "Best Project Management Tools for Engineering Teams in 2026", 30 thg 10, 2025]

**Run 3** — `sample_id: google-ai-mode-2026-09-22-BS-03-r3` — timestamp_utc: 2026-09-22T15:35:10Z — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Linear, Jira, ClickUp, Notion, Asana
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Linear  2. Jira  3. ClickUp  4. Notion  5. Asana
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: same 5-brand set as run 2
> Linear for speed and software focus, or Jira for complex enterprise agile workflows. Table: Linear (~$8, GitHub), Jira (free to 10 users then ~$8.15, agile/Scrum reporting), ClickUp (~$7, custom views/workload), Notion (~$10, docs+wikis+tasks), Asana (free to 15 users then ~$9.99, dependency mapping). Breakdown: Linear removes admin bloat, tight Git workflows; Jira time-tested for audit compliance/permission schemes; ClickUp needs dedicated admin to avoid chaos; Notion bridges wikis and task tracking. To narrow down: software/product only or hardware/non-technical too? lightweight speed or heavy reporting? [Right rail: WorksBuddy — "7 Best Project Management Tools for Remote Teams in 2026", 5 thg 5, 2026; Baserow — "Best Project Management Tool for Remote Engineering Teams", 1 thg 9, 2026; Shortcut — "Best Project Management Tools for Engineering Teams in 2026", 30 thg 10, 2025]

**Run 4** — `sample_id: google-ai-mode-2026-09-22-BS-03-r4` — timestamp_utc: 2026-09-22T15:35:30Z — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Linear, Jira, ClickUp, Trello
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Linear  2. Jira  3. ClickUp  4. Trello
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: Trello appears for the first time this prompt, replacing Notion/Asana/Shortcut seen in other runs
> Linear is the best project management tool because its lightning-fast, keyboard-driven interface and native Git workflows reduce administrative drag. Table: Linear ($8/seat/mo, keyboard-first+GitHub sync), Jira (~$8.15/seat/mo, issue tracking+JQL), ClickUp ($7/seat/mo, nested tasks/views), Trello (free, paid ~$5, drag-drop Kanban). Breakdowns: Linear for focus/momentum; Jira the heavyweight standard for compliance/JQL; ClickUp for shared space with product/marketing/design; Trello for smaller sub-teams/lightweight bug-tracking. To narrow down: team size, non-technical access? version control system used? [Right rail: WorksBuddy — "7 Best Project Management Tools for Remote Teams in 2026", 5 thg 5, 2026; Baserow — "Best Project Management Tool for Remote Engineering Teams", 1 thg 9, 2026; Shortcut — "Best Project Management Tools for Engineering Teams in 2026", 30 thg 10, 2025]

**Run 5** — `sample_id: google-ai-mode-2026-09-22-BS-03-r5` — timestamp_utc: 2026-09-22T15:35:49Z — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Linear, Jira, ClickUp, Shortcut, Notion
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Linear  2. Jira  3. ClickUp  4. Shortcut  (Notion mentioned as a companion tool, "use alongside your tracker" — not itself a standalone pick; coded mention, not recommendation)
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: Notion coded mention-only per coding rule ("named only as context... = mention, not recommendation") since the answer frames it as a supplement, not an alternative choice
> Linear for pure software development speed, or Jira for complex enterprise and cross-discipline engineering workflows. Table: Linear (free tier, ~$8/seat, Git integration), Jira (free to 10 users then ~$8.15/seat, backlogs+JQL), ClickUp (free tier, ~$7/seat, nested hierarchies+async clips), Shortcut (free tier, story tracking/epics/roadmaps). How to choose: Linear for minimalist responsive tracker; Jira for scale/compliance/hardware+software deps; ClickUp for non-technical dept collaboration; "Use alongside your tracker" — Notion pairs specs/wikis next to tasks if team has undocumented tribal knowledge. To narrow down: purely software or cross-functional? engineering group size? [Right rail: WorksBuddy — "7 Best Project Management Tools for Remote Teams in 2026", 5 thg 5, 2026; Baserow — "Best Project Management Tool for Remote Engineering Teams", 1 thg 9, 2026; Shortcut — "Best Project Management Tools for Engineering Teams in 2026", 30 thg 10, 2025]

#### BS-04 — C — "best HR and payroll platform for a US company with 200 staff" — arm: main — achieved_n: 5/5

All 5 runs English. Rippling, ADP Workforce Now, Paylocity, HiBob form a stable 4-brand core across all 5 runs. Gusto, Workday, and SAP SuccessFactors recur across runs as negative/context-only mentions ("outgrown Gusto", "too complex like Workday/SAP SuccessFactors") — coded as mentions, not recommendations, per the coding rule for brands named only as context or to avoid.

**Run 1** — `sample_id: google-ai-mode-2026-09-22-BS-04-r1` — timestamp_utc: 2026-09-22T15:36:49Z — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Gusto (context — "basic Gusto strain" — mention only), Workday (context — too expensive/complex — mention only), Rippling, HiBob, ADP Workforce Now, BambooHR, Paylocity, Justworks, TriNet
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Rippling  2. HiBob  3. ADP Workforce Now  4. BambooHR  5. Paylocity  6. Justworks / TriNet (tied, tie:yes — offered conditionally: "if you want to outsource... Systems like Justworks or TriNet are excellent up to roughly 200 staff")
sponsored_units: none observed | screenshot_ref: docs/raw/screenshots/ (temp path, see notes) | notes: —
> For a US company with 200 staff, you are firmly in the mid-market segment. Basic small-business tools (like standard Gusto) strain; massive enterprise suites (like Workday) are too expensive/complex. Table: Rippling — Overall Winner (HR+IT+Payroll) — automates onboarding/laptops/software accounts — can get expensive with modules. HiBob — Modern Culture & Compensation — native US payroll + talent management + comp planning — setup needs planning. ADP Workforce Now — Complex Compliance & Scaling — unrivaled tax infrastructure, multi-state — dated interface, longer implementation. BambooHR — Lean HR Teams — user-friendly, 1-2 HR staff — lacks advanced IT automation/global compliance. Paylocity — Hourly & Distributed Teams — workforce mgmt, expense tracking, custom reporting — steeper admin learning curve. Key factors: single source of truth (avoid syncing separate systems); multi-state tax registration (Rippling/ADP auto-open state tax accounts); PEO vs traditional (Justworks/TriNet excellent up to ~200 staff, customization limits show past this size). To narrow down: salaried or hourly? international staff? IT ops handled too? [Right rail: HackerNoon — "Best HR and Payroll Software for Mid-Market Companies (200 ...)", 3 thg 9, 2026; Darwinbox — "10 Best Cloud-Based HR and Payroll Software Platforms", 29 thg 5, 2026; COMPackage — "Best HR Software for Companies with 200 Employees", 4 thg 8, 2026]

**Run 2** — `sample_id: google-ai-mode-2026-09-22-BS-04-r2` — timestamp_utc: 2026-09-22T15:37:05Z ~approximate (interpolated) — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Rippling, ADP Workforce Now, Paylocity, HiBob
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Rippling  2. ADP Workforce Now  3. Paylocity  4. HiBob
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: —
> The top platforms for this headcount are Rippling, ADP Workforce Now, and Paylocity. Table adds HiBob as a 4th. Rippling — Consolidating HR/IT/Finance — custom workflows, device mgmt, global expansion — higher cost with multiple modules. ADP Workforce Now — Complex compliance/multi-state tax — deep reporting, PEO scaling (ADP TotalSource) — clunkier UI, steep curve. Paylocity — Employee engagement/custom workflows — expense tracking, shift scheduling, strong US support — less seamless global payroll. HiBob — Modern culture/global-ready — performance mgmt, modern UI, native US payroll — less IT asset tracking. To narrow down: payroll system migrating from? % hourly vs salaried? dedicated IT or HR handles laptops? [Right rail: HackerNoon — "Best HR and Payroll Software for Mid-Market Companies (200 ...)", 3 thg 9, 2026; Darwinbox — "10 Best Cloud-Based HR and Payroll Software Platforms", 29 thg 5, 2026; SaaSRat — "Best HR Software for Startups 2026: 7 Platforms at 20 & 50 Employees", 24 thg 4, 2026]

**Run 3** — `sample_id: google-ai-mode-2026-09-22-BS-04-r3` — timestamp_utc: 2026-09-22T15:37:21Z — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Gusto (context, mention only), Workday (context, mention only), SAP SuccessFactors (context, mention only), Rippling, ADP Workforce Now, Paylocity, Paycom, HiBob
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Rippling  2. ADP Workforce Now  3. Paylocity / Paycom (tied, tie:yes — "Both Paylocity and Paycom are designed specifically for the mid-market")  4. HiBob
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: longest/most detailed run of this prompt — full per-vendor "Why it fits 200 staff" and "Standout Feature" subsections plus a direct-comparison table
> At 200 employees you've outgrown entry-level small-business software (basic Gusto) but aren't complex enough for enterprise (Workday, SAP SuccessFactors). 1. Rippling — Best Overall & Tech-Forward — single source of truth, automates local tax registration/compliance, IT provisioning (laptop+Okta/Slack/Google Workspace); downside: per-module pricing. 2. ADP Workforce Now — Best Deep Compliance — flagship for 50-5,000 employees, unmatched tax compliance/reporting; downside: older UI, longer implementation. 3. Paylocity or Paycom — Best Comprehensive All-in-One HCM — full HCM suite; Paycom's "Beti" employee-driven payroll; downside: rigid if processes disorganized. 4. HiBob — Best Corporate Culture — social-media-style UI, native US payroll, people analytics; downside: payroll engine younger than ADP/Paylocity. Comparison table reiterates same 4 platforms with strengths/weaknesses. To narrow down: % hourly vs salaried? one state or multiple/international? current software and biggest headache? [Right rail: Noon AI — "Top 10 Payroll Software Platforms in 2026", 27 thg 8, 2026; HackerNoon — "Best HR and Payroll Software for Mid-Market Companies (200 ...)", 3 thg 9, 2026; COMPackage — "Best HR Software for Companies with 200 Employees", 4 thg 8, 2026]

**Run 4** — `sample_id: google-ai-mode-2026-09-22-BS-04-r4` — timestamp_utc: 2026-09-22T15:37:41Z — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Rippling, Paylocity, ADP Workforce Now, HiBob, Gusto (negative framing — "can feel limiting" — mention only), Justworks (negative framing — "usually costs far more" — mention only)
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Rippling  2. Paylocity  3. ADP Workforce Now  4. HiBob
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: this run's "Avoid Entry-Level Tools" section explicitly frames Gusto and Justworks negatively for this headcount rather than recommending them — coded as mentions only
> Top Mid-Market table: Rippling (tech-forward/unified IT-HR, device provisioning — can get expensive), Paylocity (hourly workforces/performance tracking, time/attendance/shift routing — less modern interface), ADP Workforce Now (traditional scaling/compliance, max compliance/tax depth — rigid reporting/hidden add-ons), HiBob (culture-focused/global contractors, employee experience UI + native payroll — less robust for IT/inventory logic). Deep dive on same 4 with "Why choose" framing. "Avoid Entry-Level Tools": at 200 staff, Gusto and Justworks (PEO model) feel limiting/cost more than a traditional HRIS. To narrow down: industry, salaried/hourly/remote-multistate? IT+hardware handled alongside HR? tool migrating from? [Right rail: HackerNoon — "Best HR and Payroll Software for Mid-Market Companies (200 ...)", 3 thg 9, 2026; COMPackage — "Best HR Software for Companies with 200 Employees", 4 thg 8, 2026; www.bolto.com — "10 Best Payroll Software for Large Companies in 2026", 24 thg 2, 2026]

**Run 5** — `sample_id: google-ai-mode-2026-09-22-BS-04-r5` — timestamp_utc: 2026-09-22T15:38:01Z — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Gusto (context, mention only), QuickBooks (context, mention only), Workday (context, mention only), SAP SuccessFactors (context, mention only), Rippling, ADP Workforce Now, Paylocity, Paycom, HiBob
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Rippling  2. ADP Workforce Now  3. Paylocity / Paycom (tied, tie:yes)  4. HiBob
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: fifth consecutive run with the same Rippling/ADP/Paylocity-Paycom/HiBob core-4 recommended set (all 5 runs of this prompt agree on Rippling as #1 and ADP Workforce Now as #2)
> At 200 employees, outgrown basic startup tools (Gusto, QuickBooks), not large enough for enterprise (Workday, SAP SuccessFactors). Comparison table: Rippling (unify HR/payroll/IT — automation, laptop shipping — modular pricing adds up), ADP Workforce Now (multi-state compliance — tax infrastructure, predictive analytics — legacy interface/longer implementation), Paylocity or Paycom (hourly/shift + talent mgmt — single-database, Paycom "Beti" — can feel clunky/aggressive sales), HiBob (culture/retention/experience — modern UI + native payroll — less robust IT provisioning). Detailed breakdown of top 3: Rippling (scales to 1,000+, PEO switch option), ADP Workforce Now (FMLA/ACA/EEO-1 compliance, "ADP RUN" vs "Workforce Now" distinction), Paycom/Paylocity (single-database employee-driven payroll, LMS). Buying advice: don't buy the pre-packaged demo; check ledger integrations. To narrow down: industry, % hourly/salaried? one state or multi-state/countries? accounting platform used? [Right rail: Noon AI — "Top 10 Payroll Software Platforms in 2026", 27 thg 8, 2026; HackerNoon — "Best HR and Payroll Software for Mid-Market Companies (200 ...)", 3 thg 9, 2026; Darwinbox — "10 Best Cloud-Based HR and Payroll Software Platforms", 29 thg 5, 2026]

### Vertical: High-CPA regulated (cards, insurance, supplements)

#### HR-01 — C — "best travel rewards credit card for someone who flies twice a year" — arm: main — achieved_n: 5/5

4 of 5 runs answered in Vietnamese (only run 5 English) — the highest Vietnamese-answer rate of any prompt in this file so far. Chase Sapphire Preferred, Capital One Venture Rewards/Venture X, Wells Fargo Autograph, and a co-branded airline card (Delta SkyMiles Gold / United Explorer as named examples) form a stable set. Amex Platinum and Chase Sapphire Reserve recur as negative/context-only mentions ("avoid these — hard to justify the fee at this flying frequency").

**Run 1** — `sample_id: google-ai-mode-2026-09-22-HR-01-r1` — timestamp_utc: 2026-09-22T15:39:15Z — region_observed: UI Vietnamese, ANSWER BODY in Vietnamese, USD fees — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Amex Platinum (context, avoid — mention only), Chase Sapphire Reserve (context, avoid — mention only), Chase Sapphire Preferred, Capital One Venture Rewards, Wells Fargo Autograph, Delta Gold Amex (co-branded example), United Explorer (co-branded example)
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Chase Sapphire Preferred  2. Capital One Venture Rewards  3. Wells Fargo Autograph  4. Delta Gold Amex / United Explorer (tied, tie:yes — named as interchangeable co-branded examples)
sponsored_units: none observed | screenshot_ref: docs/raw/screenshots/ (temp path, see notes) | notes: —
> Nếu bạn chỉ bay khoảng hai lần một năm, tránh các thẻ siêu cao cấp (Amex Platinum, Chase Sapphire Reserve) — khó tận dụng hết đặc quyền. Table: Chase Sapphire Preferred $95 — tích điểm ăn uống x3, linh hoạt chuyển đổi. Capital One Venture Rewards $95 — x2 dặm cố định mọi chi tiêu. Wells Fargo Autograph $0 — x3 điểm ăn uống/xăng/du lịch. Thẻ đồng thương hiệu hãng bay (Delta Gold Amex, United Explorer) — miễn phí năm đầu, ~$95-99 — miễn phí hành lý ký gửi. 1. Chase Sapphire Preferred — "vua" thẻ du lịch tầm trung, x5 đặt du lịch qua Chase, x3 ăn uống/streaming/tạp hóa, chuyển điểm 1:1 sang United/Southwest/British Airways. 2. Capital One Venture Rewards — x2 dặm mọi giao dịch, dùng dặm "xóa" chi phí vé máy bay. 3. Wells Fargo Autograph — $0 phí, x3 điểm, bảo hiểm du lịch cơ bản, không phí giao dịch nước ngoài. 4. Thẻ đồng thương hiệu — miễn phí hành lý ký gửi đầu tiên, tiết kiệm ~$150/năm bù phí $95. To narrow down: thành phố cất cánh/hãng yêu thích? miễn phí hành lý hay tích điểm linh hoạt? [Right rail: The Points Guy — "15 Best Travel Credit Cards of October 2026", 22 thg 9, 2026; NerdWallet — "Which Airline Credit Card Is Best for Me?", 16 thg 9, 2026; engine.com — "Best Travel Credit Cards of 2026: Fees, Bonuses, and Who...", 17 thg 9, 2026]

**Run 2** — `sample_id: google-ai-mode-2026-09-22-HR-01-r2` — timestamp_utc: 2026-09-22T15:39:31Z ~approximate (interpolated) — region_observed: UI Vietnamese, ANSWER BODY in Vietnamese — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Chase Sapphire Preferred, Capital One Venture Rewards, Capital One Venture X, Delta SkyMiles Gold Amex, United Explorer
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Chase Sapphire Preferred  2. Capital One Venture Rewards  3. Capital One Venture X  4. Delta SkyMiles Gold Amex / United Explorer (tied, tie:yes)
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: introduces Capital One Venture X ($395 fee, lounge access) not seen in run 1
> Table adds Capital One Venture X $395 — $300 travel credit + 10,000 dặm thưởng hàng năm, phòng chờ sân bay miễn phí. 1. Chase Sapphire Preferred — 5x du lịch qua Chase, 3x ăn uống/streaming/tạp hóa, chuyển điểm United/Southwest/British Airways/Hyatt. 2. Capital One Venture Rewards — 2x mọi giao dịch, "Purchase Eraser" để xóa chi phí vé, miễn phí giao dịch quốc tế. 3. Capital One Venture X — $300 credit + 10,000 dặm = giá trị $400 > phí $395, phòng chờ không giới hạn (Capital One Lounges, Plaza Premium/Priority Pass). 4. Thẻ đồng thương hiệu — Delta SkyMiles Gold Amex hoặc United Explorer, miễn phí hành lý ký gửi, tiết kiệm ~$140/năm. To narrow down: hãng bay ưu tiên/đổi vé linh hoạt? ký gửi hành lý thường xuyên? muốn vào phòng chờ? [Right rail: Reddit · r/CreditCards — "What's the best credit card for someone that travels once or...", 9 thg 4, 2024; The Points Guy — "15 Best Travel Credit Cards of October 2026", 22 thg 9, 2026; CNN — "10 best airline credit cards of August 2026", 2 thg 9, 2026]

**Run 3** — `sample_id: google-ai-mode-2026-09-22-HR-01-r3` — timestamp_utc: 2026-09-22T15:39:47Z — region_observed: UI Vietnamese, ANSWER BODY in Vietnamese — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Chase Sapphire Preferred, Capital One Venture Rewards, Wells Fargo Autograph, Capital One Venture X, United Explorer, Delta SkyMiles Gold
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Chase Sapphire Preferred  2. Capital One Venture Rewards  3. Wells Fargo Autograph  4. Capital One Venture X  5. United Explorer / Delta SkyMiles Gold (tied, tie:yes)
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: widest brand set of this prompt (5 distinct, all 5 table rows individually reviewed in prose numbered 1-5)
> Full 5-card lineup with detailed "Lý do" sections for each: Chase Sapphire Preferred ($95, Ultimate Rewards transfer partners, trip insurance); Capital One Venture Rewards ($95, flat 2x, Purchase Eraser); Wells Fargo Autograph ($0, 3x dining/travel/gas/streaming, no foreign transaction fee); Capital One Venture X ($395, $300 credit + 10K miles = "trả thêm $5", unlimited global lounge access); United Explorer / Delta SkyMiles Gold (co-branded, ~$95, free checked bag saves ~$300/year for 2 travelers). To narrow down: domestic or international? preferred airline? checked bags often? [Right rail: CNBC — "3 credit card and travel deals that are too good to last", 3 thg 9, 2026; Reddit · r/CreditCards — "What's the best credit card for someone that travels once or...", 9 thg 4, 2024; CNN — "10 best airline credit cards of August 2026", 2 thg 9, 2026]

**Run 4** — `sample_id: google-ai-mode-2026-09-22-HR-01-r4` — timestamp_utc: 2026-09-22T15:40:06Z — region_observed: UI Vietnamese, ANSWER BODY in Vietnamese — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Amex Platinum (context, avoid — mention only), Chase Sapphire Preferred, Capital One Venture X, Wells Fargo Autograph, United Explorer, Delta SkyMiles Gold
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Chase Sapphire Preferred  2. Capital One Venture X  3. Wells Fargo Autograph  4. United Explorer / Delta SkyMiles Gold (tied, tie:yes)
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: fourth consecutive Vietnamese-language full answer for this prompt (all of runs 1-4)
> Avoid Amex Platinum ($695 fee). Table + prose: Chase Sapphire Preferred ($95, $100 hotel credit, transfer to United/Southwest/BA/Hyatt); Capital One Venture X ($395, "giá trị ròng -$5" after $300 credit+10K miles, unlimited lounges for self+2 guests); Wells Fargo Autograph ($0, no foreign transaction fee); airline co-branded (United Explorer / Delta SkyMiles Gold, ~$95, free first checked bag, "tự động sinh lời sau 1-2 chuyến"). To narrow down: preferred airline/hub? checked bags often? daily-spend points or airport perks? [Right rail: Reddit · r/CreditCards — "What's the best credit card for someone that travels once or...", 9 thg 4, 2024; engine.com — "Best Travel Credit Cards of 2026: Fees, Bonuses, and Who...", 17 thg 9, 2026; CNBC — "3 credit card and travel deals that are too good to last", 3 thg 9, 2026]

**Run 5** — `sample_id: google-ai-mode-2026-09-22-HR-01-r5` — timestamp_utc: 2026-09-22T15:40:26Z — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Chase Sapphire Preferred, Capital One Venture X, Wells Fargo Autograph, Delta SkyMiles Gold (co-branded example), United Airlines (context, "if your two flights are with United or Delta")
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Chase Sapphire Preferred  2. Capital One Venture X  3. Wells Fargo Autograph  4. Delta SkyMiles Gold (mid-tier airline card example)
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: only English run of this prompt
> Chase Sapphire Preferred is the best overall travel credit card (low $95 fee, flexible points, premium trip protections); Capital One Venture X is the alternative for lounge access without complex math ($395 fee fully offset). Table: Chase Sapphire Preferred ($95, $50 hotel credit, trip delay/cancellation insurance); Capital One Venture X ($395, $300 portal credit + 10K anniversary miles, unlimited lounge access); Wells Fargo Autograph ($0, 3x everyday categories); Mid-Tier Airline Cards e.g. Delta SkyMiles Gold (~$95-150, free checked bags, priority boarding). "Issuer essentially pays you $5 annually" for Venture X. Airline card payoff: ~$160/year saved on 2 roundtrips' checked bags. To narrow down: fly one airline or hunt cheapest ticket? check bags or carry-on? lounge access matter? [Right rail: CNN — "10 best airline credit cards of August 2026", 2 thg 9, 2026; Reddit · r/CreditCards — "What's the best credit card for someone that travels once or...", 9 thg 4, 2024; The Points Guy — "15 Best Airline Credit Cards of October 2026", 22 thg 9, 2026]

#### HR-02 — C — "best cashback credit card with no annual fee" — arm: main — achieved_n: 5/5

All 5 runs answered in English (first HR-vertical prompt with no Vietnamese variant). Every run carries a financial-advice disclaimer footer: "Câu trả lời của AI có thể chứa thông tin không chính xác. Để được tư vấn tài chính, hãy tham khảo ý kiến của chuyên gia." ("The AI's answer may contain inaccurate information. For financial advice, consult a professional.") — recorded once here, present on all 5 runs. Wells Fargo Active Cash and Citi Double Cash are named co-best in every single run, always in that order.

**Run 1** — `sample_id: google-ai-mode-2026-09-22-HR-02-r1` — timestamp_utc: 2026-09-22T15:41:36Z — region_observed: UI Vietnamese, answer English, USD — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Wells Fargo (Active Cash Card), Citi (Double Cash Card), Chase (Freedom Unlimited), Discover (it Cash Back), Blue Cash Everyday (from American Express), Chase (Freedom Flex — mentioned as alternative for rotating-category trackers)
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Wells Fargo Active Cash  2. Citi Double Cash  3. Chase Freedom Unlimited  4. Discover it Cash Back  5. Blue Cash Everyday from Amex  6. Chase Freedom Flex (alternative pick, tie:no — offered as an "or" alongside Discover it for category trackers)
sponsored_units: none observed | screenshot_ref: docs/raw/screenshots/ (temp path, see notes) | notes: financial disclaimer footer present (see above)
> Wells Fargo Active Cash and Citi Double Cash are the best flat-rate cashback cards with $0 fee, both 2% unlimited. Table: Wells Fargo Active Cash (2% unlimited, $200 bonus/$500 spend, $0 fee, cellphone protection); Citi Double Cash (2%, $0 fee, long 0% balance transfer APR); Chase Freedom Unlimited (1.5-5%, $200 bonus, $0 fee, pairs with Sapphire points); Discover it Cash Back (5% rotating quarterly + 1-year match, $0 fee); Blue Cash Everyday from Amex (3% supermarkets/online/gas up to $6K/yr/category, up to $200 credit, $0 fee). How to choose: flat-rate users → Active Cash or Double Cash; category spenders → Blue Cash Everyday; rotating trackers → Discover it or Chase Freedom Flex. [Right rail: Bankrate — "Best Cash Back Credit Cards - September 2026", 8 thg 9, 2026; Experian — "Best Credit Cards with No Annual Fee of 2026"; Bankrate — "Best No Annual Fee Credit Cards for September 2026", 9 thg 9, 2026]

**Run 2** — `sample_id: google-ai-mode-2026-09-22-HR-02-r2` — timestamp_utc: 2026-09-22T15:41:53Z ~approximate (interpolated) — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Wells Fargo (Active Cash Card), Citi (Double Cash Card), Chase (Freedom Unlimited), Discover (it Cash Back), Blue Cash Everyday (from American Express), Chase (Freedom Flex — mention)
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Wells Fargo Active Cash  2. Citi Double Cash  3. Chase Freedom Unlimited  4. Discover it Cash Back  5. Blue Cash Everyday from Amex  6. Chase Freedom Flex (alternative, category maximizers)
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: same 6-brand set and order as run 1
> Wells Fargo Active Cash and Citi Double Cash tied as best flat-rate cards, both 2% unlimited. Table repeats same 5 cards with slightly different phrasing ("High rewards on everyday dining and travel" for Chase Freedom Unlimited; "First-year automatic cashback match" for Discover it). How to choose: flat-rate/catch-all → Active Cash or Double Cash; category maximizers → Freedom Flex or Discover it; groceries/online → Blue Cash Everyday. [Right rail: Bankrate — "Best Cash Back Credit Cards - September 2026", 8 thg 9, 2026; American Express — "No Annual Fee Credit Cards"; Bankrate — "Best No Annual Fee Credit Cards for September 2026", 9 thg 9, 2026]

**Run 3** — `sample_id: google-ai-mode-2026-09-22-HR-02-r3` — timestamp_utc: 2026-09-22T15:42:10Z — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Wells Fargo (Active Cash Card), Citi (Double Cash Card), Chase (Freedom Unlimited), Blue Cash Everyday (from American Express), Discover (it Cash Back)
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Wells Fargo Active Cash  2. Citi Double Cash  3. Chase Freedom Unlimited  4. Blue Cash Everyday from Amex  5. Discover it Cash Back
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: order of Blue Cash Everyday and Discover it swapped vs runs 1-2 (Blue Cash before Discover here); no Chase Freedom Flex mention this run
> Wells Fargo Active Cash and Citi Double Cash both 2% unlimited, $0 fee. Split into "Top Flat-Rate" (Active Cash — cellphone protection; Double Cash — long intro APR) and "Top Category" (Chase Freedom Unlimited — 5% travel/3% dining-drugstores/1.5% other; Blue Cash Everyday — 3% supermarkets/online/gas up to $6K/yr; Discover it — 5% rotating quarterly up to $1,500/quarter + first-year match). [Right rail: American Express — "No Annual Fee Credit Cards"; NerdWallet — "Cash-Back Credit Cards That Feel High-End", 6 thg 8, 2026; Experian — "Best Credit Cards with No Annual Fee of 2026"]

**Run 4** — `sample_id: google-ai-mode-2026-09-22-HR-02-r4` — timestamp_utc: 2026-09-22T15:42:29Z — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Wells Fargo (Active Cash Card), Citi (Double Cash Card), Chase (Freedom Unlimited), Blue Cash Everyday (from American Express), Discover (it Cash Back)
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Wells Fargo Active Cash  2. Citi Double Cash  3. Chase Freedom Unlimited  4. Blue Cash Everyday from Amex  5. Discover it Cash Back
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: same 5-brand set and order as run 3
> Same core answer as run 3: Wells Fargo Active Cash and Citi Double Cash tied best flat-rate. Brief one-line-each summaries for all 5 cards, same figures as prior runs (2%, $200/$500-spend bonus context implied, 5% travel/3% dining Chase Freedom Unlimited, 3% Blue Cash Everyday categories up to $6K/yr, 5% rotating Discover it with first-year match). [Right rail: American Express — "No Annual Fee Credit Cards"; NerdWallet — "Cash-Back Credit Cards That Feel High-End", 6 thg 8, 2026; Experian — "Best Credit Cards with No Annual Fee of 2026"]

**Run 5** — `sample_id: google-ai-mode-2026-09-22-HR-02-r5` — timestamp_utc: 2026-09-22T15:42:48Z — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Wells Fargo (Active Cash Card), Citi (Double Cash Card), Discover (it Cash Back), Blue Cash Everyday (Card, brand not explicitly re-stated as "from American Express" this run but same product)
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Wells Fargo Active Cash  2. Citi Double Cash  3. Discover it Cash Back  4. Blue Cash Everyday
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: only run of this prompt where Chase Freedom Unlimited is absent entirely — 4-brand set, smallest of this prompt's 5 runs
> Wells Fargo Active Cash and Citi Double Cash best flat-rate, both 2% unlimited, $0 fee. Table: Active Cash (2%, $0), Double Cash (2%, $0, simple everyday), Discover it Cash Back (5% rotating + year-one match, $0), Blue Cash Everyday (3% groceries/gas/online, $0). How to choose: flat-rate → Active Cash or Double Cash; rotating categories → Discover it; groceries/gas/online → Blue Cash Everyday. [Right rail: Forbes — "Best Cash-Back Credit Cards With No Annual Fee Of 2026", 9 thg 9, 2026; Experian — "Best Credit Cards with No Annual Fee of 2026"]

#### HR-05 — C — "best term life insurance for a 35-year-old non-smoker" — arm: main — achieved_n: 5/5

All 5 runs English. Every run carries the same financial-advice disclaimer as HR-02. Banner Life and SBLI are named in all 5 runs, always ranked 1st and 2nd; Protective Life in 4/5; Nationwide in 3/5; Guardian Life in 2/5; MassMutual in 1/5.

**Run 1** — `sample_id: google-ai-mode-2026-09-22-HR-05-r1` — timestamp_utc: 2026-09-22T15:43:47Z — region_observed: UI Vietnamese, answer English, USD — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Banner Life (Legal & General), SBLI, Guardian Life, Protective Life, Nationwide
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Banner Life  2. SBLI  3. Guardian Life  4. Protective Life  5. Nationwide
sponsored_units: none observed | screenshot_ref: docs/raw/screenshots/ (temp path, see notes) | notes: financial disclaimer footer present, same text as HR-02
> Banner Life for affordability/extended terms, SBLI for low baseline pricing, Guardian Life for customization/health flexibility. $14-17/month for $250K-500K, 20-year term. Banner Life — best overall, terms to 40 years, accelerated underwriting to $5M no exam. SBLI — lowest baseline rates. Guardian Life — best for minor/manageable health conditions, high customization, conversion options. Protective Life — long durations to 40 years, child-term riders. Nationwide — living benefits, early death-benefit access for chronic/terminal illness. Cost table: $100K/$500K/$1M coverage x 10/20/30-year terms, male/female rates. Key factors: term length matching obligations; conversion riders; no-exam options. [Right rail: MoneyGeek.com — "How Much Does a $100,000 Life Insurance Policy Cost? (2026 Rates)", 14 thg 9, 2026; Investopedia — "Best Term Life Insurance Companies of September 2026", 27 thg 8, 2026; NerdWallet — "5 Best Term Life Insurance Companies in 2026 | NerdWallet Rankings", 4 thg 8, 2026]

**Run 2** — `sample_id: google-ai-mode-2026-09-22-HR-05-r2` — timestamp_utc: 2026-09-22T15:44:04Z ~approximate (interpolated) — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Banner Life, SBLI, Protective Life, MassMutual
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Banner Life  2. SBLI  3. Protective Life / MassMutual (tied, tie:yes — "Protective Life or MassMutual for strong conversion options")
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: MassMutual appears only in this run, not the other 4
> Banner Life for overall value/long lengths, SBLI for lowest budget rates, Protective Life or MassMutual for conversion options. Table with AM Best ratings: Banner Life (A), SBLI (A-), Protective Life (A+), MassMutual (A++). Key factors: term length matching obligations; non-smoker status requires 12 months tobacco-free; conversion riders (Banner, Protective, MassMutual). [Right rail: Ethos — "Life Insurance Rates by Age Chart"; MarketWatch — "Best term Life Insurance 2026", 24 thg 4, 2026; Investopedia — "Best Term Life Insurance Companies of September 2026", 27 thg 8, 2026]

**Run 3** — `sample_id: google-ai-mode-2026-09-22-HR-05-r3` — timestamp_utc: 2026-09-22T15:44:20Z — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Banner Life, SBLI, Protective Life, Nationwide
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Banner Life  2. SBLI  3. Protective Life  4. Nationwide
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: same 4-brand set as run 4/5 but SBLI given equal top billing with Banner Life this run ("Banner Life, SBLI, and Protective Life are the best...")
> Table with financial strength + key feature: Banner Life (A, terms to 40 yrs), SBLI (A-, lowest rates many age groups), Protective Life (A+, child riders/long terms), Nationwide (A+, free chronic/terminal illness riders). $500K cost estimates: 10-yr $11-13/mo, 20-yr $17-20/mo, 30-yr $28-34/mo. [Right rail: Investopedia — "Best Term Life Insurance Companies of September 2026", 27 thg 8, 2026; Diversified Insurance Brokers — "35-Year Term Life Insurance | Compare Top Carriers & Quotes", 26 thg 5, 2026; SelectQuote — "$500K Life Insurance: Cost & Coverage"]

**Run 4** — `sample_id: google-ai-mode-2026-09-22-HR-05-r4` — timestamp_utc: 2026-09-22T15:44:39Z — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Banner Life, SBLI, Protective Life, Nationwide
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Banner Life  2. SBLI  3. Protective Life  4. Nationwide
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: identical 4-brand set/order to run 3, $15-20/month for $500K quoted (vs run 3's $500K table)
> Banner Life and SBLI best, ~$15-20/month for $500K level-term. Table: Banner Life (A, up to $5M no-exam), SBLI (A-, up to $1M no-exam), Protective Life (A+, exam often required), Nationwide (A+, up to $1.5M no-exam). Same per-carrier detail as run 3 (Banner 40-yr terms; SBLI cheapest+free conversion; Protective child riders; Nationwide living benefits). [Right rail: Investopedia — "Best Term Life Insurance Companies of September 2026", 27 thg 8, 2026; Banner Life — "Term Life Quote | Life Insurance Quote Online"; MarketWatch — "Best term Life Insurance 2026", 24 thg 4, 2026]

**Run 5** — `sample_id: google-ai-mode-2026-09-22-HR-05-r5` — timestamp_utc: 2026-09-22T15:44:58Z — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Banner Life, SBLI, Protective Life, Guardian Life
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Banner Life  2. SBLI  3. Protective Life  4. Guardian Life
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: Guardian Life reappears here (also in run 1), Nationwide/MassMutual absent this run
> Banner Life best overall (low cost, high limits, 40-yr terms), SBLI/Protective Life lowest baseline rates. Table: Banner Life (A, 40 yrs, best overall/highest no-exam), SBLI (A-, 30 yrs, cheapest rates), Protective Life (A+, 40 yrs, families/child riders), Guardian Life (A++, 30 yrs, minor health conditions). Banner Life up to $5M no exam; SBLI free conversion; Protective child rider to age 25; Guardian flexible customization for mild medical histories. [Right rail: Diversified Insurance Brokers — "35-Year Term Life Insurance | Compare Top Carriers & Quotes", 26 thg 5, 2026; Investopedia — "Best Term Life Insurance Companies of September 2026", 27 thg 8, 2026; NerdWallet — "5 Best Term Life Insurance Companies in 2026 | NerdWallet Rankings", 4 thg 8, 2026]

#### HR-06 — C — "best pet insurance for a puppy" — arm: main — achieved_n: 5/5

All 5 runs English. No financial/medical disclaimer footer observed on any run of this prompt (contrast with HR-02/HR-05's financial-advice disclaimer and SK-04's medical disclaimer) — pet insurance apparently doesn't trigger either template. Trupanion and ASPCA appear in 4/5 runs each; Embrace, Pets Best, Spot, Pumpkin, Lemonade each appear in 2-3/5.

**Run 1** — `sample_id: google-ai-mode-2026-09-22-HR-06-r1` — timestamp_utc: 2026-09-22T15:45:48Z — region_observed: UI Vietnamese, answer English, USD — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Trupanion, ASPCA (Pet Health Insurance), Embrace, Pumpkin, Spot
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Trupanion  2. ASPCA  3. Embrace  4. Pumpkin  5. Spot
sponsored_units: none observed | screenshot_ref: docs/raw/screenshots/ (temp path, see notes) | notes: no disclaimer footer this prompt (see above)
> Trupanion, ASPCA, and Embrace lead for comprehensive coverage/hereditary protections/payout structures. Table: Trupanion (Direct Vet Pay — 5-min checkout pay, no payout limits, covers hereditary/congenital); ASPCA (Comprehensive Puppy Plans — behavioral+hereditary, customizable limits/deductibles); Embrace (Customization & Wellness — diminishing deductibles, wellness add-ons); Pumpkin (Fast Claims & Care — PumpkinNow expedited, 90% reimbursement, short joint-issue waits); Spot (Broad Add-Ons — exam fees/prescription food/behavioral mod standard). Key factors: enroll immediately (pre-existing exclusions); breed-specific risks (hip dysplasia); exam fees; direct pay vs reimbursement. [Right rail: money.com — "9 Best Pet Insurance Companies of September 2026", 2 thg 9, 2026; Reddit · r/puppy101 — "Which pet insurance do you use? And why did you choose it?", 4 thg 7, 2024; NerdWallet — "Best Pet Insurance Companies for 2026", 1 thg 9, 2026]

**Run 2** — `sample_id: google-ai-mode-2026-09-22-HR-06-r2` — timestamp_utc: 2026-09-22T15:46:03Z ~approximate (interpolated) — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Trupanion, ASPCA, Pets Best, Spot, Lemonade
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Trupanion  2. ASPCA  3. Pets Best  4. Spot  5. Lemonade
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: Lemonade and Pets Best appear for the first time this prompt, replacing run 1's Embrace/Pumpkin
> Trupanion, ASPCA, Pets Best stand out for direct vet pay, comprehensive coverage, and budget value. Table: Trupanion (Direct Vet Pay, no payout limits, lifetime per-condition deductible); ASPCA (hereditary/behavioral, customizable); Pets Best (Budget & Value, lowest sample premiums, customizable tiers); Spot (Perks & Add-ons, exam fees/food/behavioral therapy); Lemonade (Fast Digital Claims, AI-driven, affordable base tiers). What to look for: hereditary/congenital coverage; waiting periods (14 days-6 months for ACL); exam fee inclusions; direct pay vs reimbursement. [Right rail: U.S. News & World Report — "Best Pet Insurance Companies of 2026", 1 thg 9, 2026; NerdWallet — "Best Pet Insurance Companies for 2026", 1 thg 9, 2026; Go Compare — "Compare Cheap Pet Insurance Quotes from £3.65 Per Month", 1 thg 9, 2026]

**Run 3** — `sample_id: google-ai-mode-2026-09-22-HR-06-r3` — timestamp_utc: 2026-09-22T15:46:19Z — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Trupanion, ASPCA, Pets Best, Spot, Pumpkin
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Trupanion  2. ASPCA  3. Pets Best  4. Spot  5. Pumpkin
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: same top-3 as run 2 (Trupanion/ASPCA/Pets Best) but Pumpkin swapped in for Lemonade at #5
> Trupanion for direct vet payments, ASPCA for comprehensive hereditary/behavioral, Pets Best for budget-friendly premiums. Table: Trupanion (Direct Vet Pay & Lifelong Care); ASPCA (Comprehensive Coverage — behavioral/prescription food/alternative therapies standard); Pets Best (Budget & Customization, up to 90% reimbursement); Spot (Perks & Broad Inclusion, 24/7 vet helpline); Pumpkin (Quick Claim Options via PumpkinNow, diagnostics/physical therapy). What to look for: enrollment age (8 weeks, some 6 weeks); pre-existing conditions; hereditary/congenital; exam fee coverage. [Right rail: U.S. News & World Report — "Best Pet Insurance Companies of 2026", 1 thg 9, 2026; Reddit · r/puppy101 — "Which pet insurance do you use? And why did you choose it?", 4 thg 7, 2024; NerdWallet — "Best Pet Insurance Companies for 2026", 1 thg 9, 2026]

**Run 4** — `sample_id: google-ai-mode-2026-09-22-HR-06-r4` — timestamp_utc: 2026-09-22T15:46:38Z — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): ASPCA, Embrace, Trupanion, Pets Best
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. ASPCA  2. Embrace  3. Trupanion  4. Pets Best
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: only run to lead with ASPCA/Embrace ahead of Trupanion; includes a "Direct Vet Pay: Yes/No" column
> ASPCA and Embrace best because broad hereditary/congenital/behavioral coverage from 8 weeks. Table with min age + direct-vet-pay column: ASPCA (8 wks, comprehensive lifelong, reimbursement only); Embrace (6 wks, wellness add-ons/custom limits, reimbursement only); Trupanion (8 wks, direct vet payments, Yes); Pets Best (6 wks, budget-friendly, reimbursement only). Key factors: enrollment age 6-8 weeks; hereditary/congenital from start; exam fees; claim payout style. [Right rail: ASPCA Pet Insurance — "Pet Insurance Coverage - Rated One of the Best"; U.S. News & World Report — "Best Pet Insurance Companies of 2026", 1 thg 9, 2026; NerdWallet — "Best Pet Insurance Companies for 2026", 1 thg 9, 2026]

**Run 5** — `sample_id: google-ai-mode-2026-09-22-HR-06-r5` — timestamp_utc: 2026-09-22T15:46:56Z — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Embrace, ASPCA, Trupanion, Pets Best
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Embrace  2. ASPCA  3. Trupanion  4. Pets Best
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: same 4-brand set as run 4, Embrace and ASPCA swapped to #1/#2; this run adds explicit monthly-cost and waiting-period columns
> Embrace, ASPCA, Trupanion leading recommendations. Table with typical monthly cost + direct-vet-pay + accident-waiting-period columns: Embrace ($35-75, No, 2 days); ASPCA ($10-50, No, 14 days); Trupanion ($60-90, Yes, 5 days); Pets Best ($30-60, No, 3 days). Key considerations: waiting periods; hereditary/congenital (avoid 12-month waits); exam fees; direct pay options. [Right rail: ASPCA Pet Insurance — "Pet Insurance Coverage - Rated One of the Best"; U.S. News & World Report — "Best Pet Insurance Companies of 2026", 1 thg 9, 2026; NerdWallet — "Best Pet Insurance Companies for 2026", 1 thg 9, 2026]

#### HR-09 — C — "best creatine supplement" — arm: main — achieved_n: 5/5

All 5 runs English, no disclaimer footer observed. Thorne Creatine, Transparent Labs Creatine HMB, and a Nutricost/Optimum Nutrition budget pick form the stable core across all 5 runs — the most consistent 3-brand agreement of any C prompt sampled so far in this file.

**Run 1** — `sample_id: google-ai-mode-2026-09-22-HR-09-r1` — timestamp_utc: 2026-09-22T15:47:51Z — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Thorne (Creatine), Transparent Labs (Creatine HMB), Nutricost (Micronized Creatine Monohydrate)
brands_cited: none observed
brands_recommended (rank_position, list_ordered:no, tie:no): 1. Thorne Creatine  2. Transparent Labs Creatine HMB  3. Nutricost Micronized Creatine Monohydrate (document order of first appearance; intro sentence names Thorne first, per-product detail sections follow same order)
sponsored_units: none observed | screenshot_ref: docs/raw/screenshots/ (temp path, see notes) | notes: —
> Thorne Creatine for purity, Transparent Labs Creatine HMB for enhanced recovery, Nutricost for best overall budget value. ConsumerLab.com cited as confirming creatine monohydrate is gold standard. Thorne Creatine — unflavored, NSF Certified for Sport. Transparent Labs Creatine HMB — 5g creatine + HMB + vitamin D3, advanced lean muscle retention. Nutricost Micronized Creatine Monohydrate — 5g clinically-backed dose, lowest cost per day. To narrow down: unflavored/flavored/capsules/gummies? goal (muscle mass/sprint power/injury recovery)? [Right rail: Forbes — "Best Creatine Supplements 2026 - Forbes Vetted", 15 thg 1, 2026; ConsumerLab.com — "Creatine Supplements Review: Best Creatine Powders, Capsules & Gummies", 22 thg 6, 2026; Health US News — "Best Creatine Pharmacist Ranked"]

**Run 2** — `sample_id: google-ai-mode-2026-09-22-HR-09-r2` — timestamp_utc: 2026-09-22T15:48:07Z ~approximate (interpolated) — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Transparent Labs (Creatine HMB), Thorne (Creatine), Nutricost (Micronized Creatine Monohydrate), Legion (Creatine — table only)
brands_cited: none observed
brands_recommended (rank_position, list_ordered:no, tie:no): 1. Transparent Labs Creatine HMB  2. Thorne Creatine  3. Nutricost Micronized Creatine Monohydrate  4. Legion Creatine (Gummies — table-only entry, "Convenient option on-the-go")
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: Legion Creatine appears only in the comparison table, not in prose — first appearance of Legion in this file
> Creatine monohydrate is the gold standard per ConsumerLab. Transparent Labs Creatine HMB — Best Premium, 5g + HMB, Informed Choice tested, multiple flavors. Thorne Creatine — Best for Athletes, unflavored micronized, NSF Certified for Sport. Nutricost Micronized Creatine Monohydrate — Best Budget, 5g dose, minimal ingredients. Comparison table adds Legion Creatine (Gummies, Flavored, NSF Certified/no added sugar). [Right rail: Forbes — "Best Creatine Supplements 2026 - Forbes Vetted", 15 thg 1, 2026; Fortune — "13 Best Creatine Supplements of 2026", 10 thg 9, 2026; Health US News — "Best Creatine Pharmacist Ranked"]

**Run 3** — `sample_id: google-ai-mode-2026-09-22-HR-09-r3` — timestamp_utc: 2026-09-22T15:48:23Z — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Transparent Labs (Creatine HMB), Thorne (Creatine), Nutricost (Creatine Monohydrate)
brands_cited: none observed
brands_recommended (rank_position, list_ordered:no, tie:no): 1. Transparent Labs Creatine HMB  2. Thorne Creatine  3. Nutricost Creatine Monohydrate
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: identical 3-brand set to run 1, order matches run 2
> Same core 3 brands: Transparent Labs Creatine HMB (5g+1.5g HMB, third-party tested, naturally sweetened), Thorne Creatine (NSF Certified for Sport, unflavored micronized), Nutricost Creatine Monohydrate (5g budget, micronized). [Right rail: Forbes — "Best Creatine Supplements 2026 - Forbes Vetted", 15 thg 1, 2026; Healthline — "6 Types of Creatine: Benefits, Research, and How to Choose", 24 thg 7, 2026; Healthline — "Best Creatine Monohydrate Supplements: Top Picks for Every Budget", 26 thg 8, 2026]

**Run 4** — `sample_id: google-ai-mode-2026-09-22-HR-09-r4` — timestamp_utc: 2026-09-22T15:48:45Z — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Transparent Labs (Creatine HMB), Thorne (Creatine), Nutricost (Micronized Creatine Monohydrate)
brands_cited: none observed
brands_recommended (rank_position, list_ordered:no, tie:no): 1. Transparent Labs Creatine HMB  2. Thorne Creatine  3. Nutricost Micronized Creatine Monohydrate
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: fourth run with the same 3-brand core set
> Same 3-brand set: Transparent Labs Creatine HMB (Best Overall per Garage Gym Reviews, third-party tested/gluten-free), Thorne Creatine (Best for Athletes per Healthline, NSF Certified), Nutricost Micronized Creatine Monohydrate (Best Budget per ConsumerLab). [Right rail: Forbes — "Best Creatine Supplements 2026 - Forbes Vetted", 15 thg 1, 2026; Healthline — "6 Types of Creatine: Benefits, Research, and How to Choose", 24 thg 7, 2026; Health US News — "Best Creatine Pharmacist Ranked"]

**Run 5** — `sample_id: google-ai-mode-2026-09-22-HR-09-r5` — timestamp_utc: 2026-09-22T15:49:04Z — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Thorne (Creatine), Transparent Labs (Creatine HMB), Optimum Nutrition (Micronized Creatine)
brands_cited: none observed
brands_recommended (rank_position, list_ordered:no, tie:no): 1. Thorne Creatine  2. Transparent Labs Creatine HMB  3. Optimum Nutrition Micronized Creatine
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: only run where Optimum Nutrition replaces Nutricost as the 3rd/budget pick; page text ended without a visible right-rail source list this run (captured page text cut off after the narrowing-down questions, no "Hiện tất cả"/source cards present in the extraction — possible truncation or the panel simply did not render below-fold sources by the time of extraction)
> Thorne Creatine — Best Overall for Clean Purity, 100% pure micronized, NSF Certified for Sport, dissolves without gritty residue. Transparent Labs Creatine HMB — Best Premium & Flavored, + HMB + Vitamin D3, stevia-sweetened, higher price. Optimum Nutrition Micronized Creatine — Best Value Legacy Standard, "banned substance tested" (not independent NSF seal), globally popular/pharmacist-recommended. Comparison table: dose (5g all three), form, flavor profile, third-party seals, best-suited-for. To narrow down: unflavored or flavored? budget/capsules vs powder? competitive athlete NSF/Informed Sport testing needed? [note: no right-rail source-card list captured in this run's page text, unlike all other runs in this file]

#### HR-10 — C — "best magnesium supplement for sleep" — arm: main — achieved_n: 5/5

All 5 runs English except run 3 (Vietnamese). Only 3 of 5 runs carry a disclaimer, and its placement/wording varies (footer-style in some HR prompts vs. an inline bulleted "Disclaimer:" line in this prompt's runs 2, 3 and 4) — recorded per run rather than assumed uniform. Pure Encapsulations Magnesium Glycinate and Thorne Magnesium Bisglycinate Powder appear in all 5 runs; Momentous Magnesium L-Threonate in 4/5; Ritual Magnesium+ in 2/5; Doctor's Best and NOW Foods each appear once.

**Run 1** — `sample_id: google-ai-mode-2026-09-22-HR-10-r1` — timestamp_utc: 2026-09-22T15:49:59Z — region_observed: UI Vietnamese, answer English, VND/AUD — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Pure Encapsulations (Magnesium Glycinate), Thorne (Magnesium Bisglycinate Powder), Ritual (Magnesium+)
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Pure Encapsulations Magnesium Glycinate  2. Thorne Magnesium Bisglycinate Powder  3. Ritual Magnesium+
sponsored_units: none observed | screenshot_ref: docs/raw/screenshots/ (temp path, see notes) | notes: no disclaimer text this run (contrast with runs 2-4)
> Magnesium glycinate/bisglycinate widely considered best form; magnesium L-threonate for anxious minds. Pure Encapsulations Magnesium Glycinate — 1.728.905₫ (93,45 AU$), clean hypoallergenic, 120mg/capsule. Thorne Magnesium Bisglycinate Powder — 2.150.000₫, best powder, NSF Certified for Sport, 200mg/scoop. Ritual Magnesium+ — bisglycinate + tart cherry, 300mg/serving. Safety: max 350mg/day; take 1-2hrs before bed; avoid magnesium oxide/citrate before bed (laxative). To narrow down: capsules/powder/gummies? pure or sleep blend with L-theanine/melatonin? stomach sensitivities? [Right rail: HealthCentral — "Which Magnesium Is Best for Sleep? Your Guide to Types, Benefits, and Usage", 23 thg 2, 2026; Yahoo Health — "Best magnesium for sleep in 2026, tested and reviewed", 26 thg 8, 2026; Sleep Foundation — "Best Magnesium Supplements for Sleep 2026: Our Experts Weigh in", 16 thg 4, 2026]

**Run 2** — `sample_id: google-ai-mode-2026-09-22-HR-10-r2` — timestamp_utc: 2026-09-22T15:50:49Z — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Thorne (Magnesium Bisglycinate), Pure Encapsulations (Magnesium Glycinate), Doctor's Best (High Absorption Magnesium), Momentous (Magnesium L-Threonate)
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Thorne Magnesium Bisglycinate  2. Pure Encapsulations Magnesium Glycinate  3. Doctor's Best High Absorption Magnesium  4. Momentous Magnesium L-Threonate
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: first `get_page_text` on this run returned only unrendered page CSS at the standard 10s wait; an additional 8s wait plus re-fetch returned the real answer, quoted below. Inline disclaimer present: "Disclaimer: Always consult with a healthcare professional before adding a new supplement to your routine, especially if you take existing medications or have underlying kidney conditions."
> Thorne Magnesium Bisglycinate — 2.150.000₫, best liquid/powder, NSF Certified for Sport, 200mg/scoop. Pure Encapsulations Magnesium Glycinate — 1.728.905₫ (93,45 AU$), best capsule, hypoallergenic, 120mg/capsule. Doctor's Best High Absorption Magnesium — 450.000₫, best budget, TRAACS chelated formula, 200mg/2-tablet serving. Momentous Magnesium L-Threonate — 1.334.000₫, best for busy mind, patented Magtein®, 145mg/serving. Comparison table of forms (glycinate/bisglycinate, L-threonate, citrate, oxide) by sleep benefit/gut comfort/bioavailability. Usage: ≤350mg/day; take 30-60 min before bed; 2-4 weeks to assess. [Right rail: Dr. Soliman Fakeeh Hospital Riyadh — "Best Magnesium Supplements: How to Choose the Right Type?"; Yahoo Health — "Best magnesium for sleep in 2026, tested and reviewed", 26 thg 8, 2026; Sleep Foundation — "Best Magnesium Supplements for Sleep 2026: Our Experts Weigh in", 16 thg 4, 2026]

**Run 3** — `sample_id: google-ai-mode-2026-09-22-HR-10-r3` — timestamp_utc: 2026-09-22T15:51:05Z ~approximate (interpolated) — region_observed: UI Vietnamese, ANSWER BODY in Vietnamese — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Thorne (Magnesium Bisglycinate Powder), Pure Encapsulations (Magnesium Glycinate), Momentous (Magnesium L-Threonate), NOW Foods (Magnesium Glycinate)
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Thorne Magnesium Bisglycinate Powder  2. Pure Encapsulations Magnesium Glycinate  3. Momentous Magnesium L-Threonate  4. NOW Foods Magnesium Glycinate
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: fifth Vietnamese-language full-answer run in this file's HR vertical (following SK-01/02/03/04 and HR-01's Vietnamese runs); no explicit "Disclaimer:" line this run but a "Tham vấn y khoa" (medical consultation) bullet serves the same function
> Magnesium Glycinate/Bisglycinate và L-Threonate ưu tiên hơn Oxit/Citrat (kích hoạt GABA, ít kích ứng). Thorne Magnesium Bisglycinate Powder — 2.150.000₫ — cao cấp nhất, NSF Certified for Sport, 200mg/thìa. Pure Encapsulations Magnesium Glycinate — 1.728.905₫ (93,45 AU$) — viên nang sạch nhất, thuần chay/Non-GMO, 120mg/viên. Momentous Magnesium L-Threonate — 1.334.000₫ — tốt nhất cho tâm trí bận rộn, xuyên hàng rào máu não. NOW Foods Magnesium Glycinate — 759.000₫ — tiết kiệm tối ưu, GMP, 200mg/khẩu phần. Lưu ý: liều 200-350mg/ngày; uống 30-60 phút trước ngủ; tham vấn bác sĩ nếu có bệnh thận/tim mạch hoặc dùng thuốc kê đơn. [Right rail: YouTube · Huberman Lab Clips — "Best Magnesium Supplements for Sleep & Brain Health", 25 thg 3, 2026; Sleep Foundation — "Magnesium for Sleep: Benefits, Types, Dosage, and Side Effects", 10 thg 6, 2026; Healthspan IE — "What is the Best Magnesium for Sleep?", 9 thg 9, 2025]

**Run 4** — `sample_id: google-ai-mode-2026-09-22-HR-10-r4` — timestamp_utc: 2026-09-22T15:51:21Z — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Pure Encapsulations (Magnesium Glycinate), Thorne (Magnesium Bisglycinate Powder), Ritual (Magnesium+), Momentous (Magnesium L-Threonate)
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Pure Encapsulations Magnesium Glycinate  2. Thorne Magnesium Bisglycinate Powder  3. Ritual Magnesium+  4. Momentous Magnesium L-Threonate
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: inline disclaimer present: "Disclaimer: Supplements can interact with antibiotics, blood pressure medications, or underlying kidney conditions. Always consult a healthcare professional before starting a new supplement regimen."
> Pure Encapsulations Magnesium Glycinate — best capsule, gluten-free/vegan, 120mg/capsule. Thorne Magnesium Bisglycinate Powder — best powder & athlete pick, NSF Certified, 200mg/scoop, monk-fruit sweetened. Ritual Magnesium+ — best sleep blend, bisglycinate + tart cherry, 300mg (71% DV). Momentous Magnesium L-Threonate — best for racing mind, Magtein®. Comparison table: glycinate/bisglycinate vs L-threonate vs citrate by benefit/GI side effects. Usage: ≤350mg/day; 1-2hrs before bed; 2-4 weeks for full effect. [Right rail: HealthCentral — "Which Magnesium Is Best for Sleep? Your Guide to Types, Benefits, and Usage", 23 thg 2, 2026; Sleep Foundation — "Magnesium for Sleep: Benefits, Types, Dosage, and Side Effects", 10 thg 6, 2026; The Telegraph — "I tried 18 magnesium supplements for sleep", 13 thg 6, 2026]

**Run 5** — `sample_id: google-ai-mode-2026-09-22-HR-10-r5` — timestamp_utc: 2026-09-22T15:52:08Z — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Pure Encapsulations (Magnesium Glycinate), Thorne (Magnesium Bisglycinate Powder), Momentous (Magnesium L-Threonate)
brands_cited: none observed
brands_recommended (rank_position, list_ordered:yes, tie:no): 1. Pure Encapsulations Magnesium Glycinate  2. Thorne Magnesium Bisglycinate Powder  3. Momentous Magnesium L-Threonate
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: cites Cleveland Clinic Health Essentials as a medical source for GABA/melatonin mechanism claims — first appearance of a named hospital/clinical-authority citation in this file; no explicit "Disclaimer:" line this run
> Magnesium glycinate/bisglycinate best overall per Cleveland Clinic (relaxes muscles, quiets nervous system via melatonin/GABA); L-threonate for racing minds. Pure Encapsulations Magnesium Glycinate — hypoallergenic vegan capsule, 120mg. Thorne Magnesium Bisglycinate Powder — fast-absorbing, NSF Certified for Sport, 200mg/scoop. Momentous Magnesium L-Threonate — premier for brain relaxation/REM sleep, 145mg patented Magtein. Usage: ≤350mg/day; 30-60 min before bed; avoid oxide/citrate before bed. [Right rail: Sleep Foundation — "Best Magnesium Supplements for Sleep 2026: Our Experts Weigh in", 16 thg 4, 2026; Yahoo Health — "Best magnesium for sleep in 2026, tested and reviewed", 26 thg 8, 2026; Sleep Foundation — "Magnesium for Sleep: Benefits, Types, Dosage, and Side Effects", 10 thg 6, 2026]

**All 14 C prompts now complete at n=5 on the primary arm (Google AI Mode) — 70/70 runs.** Moving to the secondary arm (Google AI Overviews, n=1 per C prompt) next, per task order of work.

## Secondary arm — Google AI Overviews (plain search, `udm=50` absent) — 14 C prompts, n=1 each

**Headline finding: zero of 14 plain-search pages rendered an AI Overview block.** Every one of the 14 C-prompt queries — the same 14 queries that reliably produced a full generative answer on the `udm=50` AI Mode endpoint above — returned a conventional organic results page on plain `google.com/search`: ranked blue-link results, a "Mọi người cũng hỏi" (People Also Ask) accordion, a "Mọi người cũng tìm kiếm" (related searches) footer, and on some queries a video carousel or a "Gần đây, N km" (nearby, N km) local-shopping product carousel. No generative/AI-authored answer box appeared above, below, or beside the organic results on any of the 14 pages. `region_observed`: UI chrome in Vietnamese throughout (same as the AI Mode arm), consistent with IP/network-based localisation rather than a per-surface difference.

Per the protocol's record schema, `answer_outcome: empty` is used for all 14 runs — no AI-generated answer text exists to capture, and no AI Overview means no brand list, citation list, sponsored-unit observation, or model version is obtainable from this arm for this date. This is recorded as a finding in itself, not as a sampling failure: the page loaded normally (HTTP 200, full organic SERP, no bot-check), the query text was sent unmodified, and the absence is the AI Overview feature's own behavior on this account/network/date. `brands_mentioned`/`brands_recommended`/`brands_cited` are `not-applicable — no AI Overview block rendered` throughout; organic blue-link rankings and "People Also Ask" content are explicitly out of scope per `glossary.md` ("Is NOT: ... Classical SERP rank") and are not coded as visibility.

| id | prompt | AI Overview rendered? | timestamp_utc | notable non-AI SERP features observed |
|---|---|---|---|---|
| SK-01 | best moisturizer for dry sensitive skin | No | 2026-09-22T15:53:16Z | PAA, related searches, no shopping carousel |
| SK-02 | best vitamin C serum under $50 | No | 2026-09-22T15:53:36Z | PAA, related searches, Vietnamese local-shopping carousel (7 products, "Gần đây, 3 km", no visible "Sponsored" label in text extraction) |
| SK-03 | best sunscreen for daily use under makeup | No | 2026-09-22T15:53:57Z | PAA, video carousel, Vietnamese local-shopping carousel (8 products, "Gần đây, 2-7 km", one marked "GIÁ THẤP" = "low price", no visible "Sponsored" label) |
| SK-04 | best retinol for beginners | No | 2026-09-22T15:54:14Z | PAA, video carousel, related searches |
| BS-01 | best help desk software for a 50-person support team | No | 2026-09-22T15:54:32Z | PAA, related searches, one Reddit thread ranked #1 result section |
| BS-02 | best CRM for a B2B startup under 20 employees | No | 2026-09-22T15:54:49Z | PAA, video carousel, multiple Reddit threads |
| BS-03 | best project management tool for a remote engineering team | No | 2026-09-22T15:55:07Z | PAA, related searches, one Reddit thread |
| BS-04 | best HR and payroll platform for a US company with 200 staff | No | 2026-09-22T15:55:24Z | PAA, one Reddit thread ranked #1 result |
| HR-01 | best travel rewards credit card for someone who flies twice a year | No | 2026-09-22T15:55:41Z | PAA, one Quora thread, related searches |
| HR-02 | best cashback credit card with no annual fee | No | 2026-09-22T15:55:58Z | PAA, video carousel, related searches |
| HR-05 | best term life insurance for a 35-year-old non-smoker | No | 2026-09-22T15:56:14Z | PAA, one Reddit thread, one Quora thread, one "4,7(17.255) · Miễn phí" (app-install-style) result card |
| HR-06 | best pet insurance for a puppy | No | 2026-09-22T15:56:32Z | PAA, one Reddit thread, one Facebook community thread |
| HR-09 | best creatine supplement | No | 2026-09-22T15:56:51Z | PAA, one Reddit thread, one YouTube result |
| HR-10 | best magnesium supplement for sleep | No | 2026-09-22T15:57:09Z | PAA, related searches, one YouTube (Huberman Lab Clips) result |

**Toggle arm.** Per the protocol, "Once per engine per sample date, re-run the vertical's first C prompt with the toggle flipped." As established in the file-wide deviations above, **no search-toggle control exists on Google AI Mode or AI Overviews for this session** — the only surface-selection control observed is the top nav tab strip (`Chế độ AI | Tất cả | Hình ảnh | Video | Tin tức | Thêm`), which switches which results-page *type* renders (AI Mode vs. all-results vs. images, etc.) rather than toggling AI generation on/off within one results type. This nav-tab switch is arguably *itself* what separates the primary and secondary arms already sampled above (`udm=50` vs. absent) — running a third "toggle" pass would duplicate the AI-Overviews-arm data already collected. Recorded per protocol's own instruction for this case: `arm: toggle-flipped — not-sampled: no toggle control exists on Google AI Mode / AI Overviews distinct from the primary/secondary arm split already sampled`.

## P prompts — problem-shaped — primary arm (Google AI Mode), n=5 each

### Vertical: Skincare and beauty

#### SK-08 — P — "what should I use for hormonal acne on my chin?" — arm: main — achieved_n: 5/5

**Notable finding: this prompt's answers name almost no consumer brands.** All 5 runs structure the answer around drug/ingredient tiers (OTC topicals, prescription topicals, oral medications) using generic/pharmacological names (benzoyl peroxide, salicylic acid, adapalene, tretinoin, spironolactone, isotretinoin, azelaic acid) rather than product brands. The only brand names to surface across all 5 runs are three prescription/OTC-drug brand names cited parenthetically next to their generic name: **Differin** (brand for adapalene, runs 1 and 5), **Winlevi** (brand for clascoterone, run 1 only), and **Accutane** (brand for isotretinoin, runs 1, 3, 4, 5). Run 2 names zero brands at all. Every run carries the medical disclaimer footer (same text as SK-04).

**Run 1** — `sample_id: google-ai-mode-2026-09-22-SK-08-r1` — timestamp_utc: 2026-09-22T15:59:24Z — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Differin (as adapalene's brand name), Winlevi (Clascoterone), Accutane (Isotretinoin)
brands_cited: none observed
brands_recommended (rank_position, list_ordered:no, tie:yes — tiered by severity, not ranked): Differin, Winlevi, Accutane — each offered as the named option within its own OTC/prescription/oral tier, not ranked against each other
sponsored_units: none observed | screenshot_ref: docs/raw/screenshots/ (temp path, see notes) | notes: three-tier structure (OTC topical / prescription topical / oral); recommends consulting American Academy of Dermatology Association resources
> Hormonal acne on the chin is most effectively treated by targeting the underlying hormonal triggers or using specialized topical ingredients... [3-tier structure: OTC — Salicylic Acid, Benzoyl Peroxide, Adapalene (Differin), Azelaic Acid; Prescription topical — Tretinoin, Clascoterone (Winlevi); Oral — Spironolactone, Combined Oral Contraceptives, Isotretinoin (Accutane)]. Treatment overview table repeats the three tiers. Consult a healthcare provider via AAD resources. To narrow down: deep painful cysts or surface whiteheads? cyclical with period? current products used? [Right rail: aafp.org — "Acne Management: Guidelines From the American Academy of...", Healthline — "Treatments and Natural Remedies for Hormonal Acne", 12 thg 2, 2026; nhs.uk — "Acne - Treatment - NHS"]

**Run 2** — `sample_id: google-ai-mode-2026-09-22-SK-08-r2` — timestamp_utc: 2026-09-22T15:59:49Z — region_observed: UI Vietnamese, ANSWER BODY in Vietnamese — search_toggle: not exposed — answer_outcome: answered
brands_mentioned: none observed — zero brand names anywhere in this run, only generic/ingredient names (Benzoyl Peroxide, Salicylic Acid, Adapalene, Tretinoin, Spironolactone, Isotretinoin)
brands_cited: none observed
brands_recommended: none — no brand offered as an answer this run
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: only run of this prompt with literally zero brand names; also covers lifestyle factors (cortisol/stress, dairy/high-GI diet)
> Để điều trị mụn nội tiết ở vùng cằm hiệu quả... [same OTC/prescription tier structure, generic names only, plus lifestyle section on cortisol and diet]. [Right rail: Vinmec — "The emergence of acne on the chin: Is it due to hormonal imbalance?", 24 thg 1, 2026; Cleveland Clinic — "Hormonal Acne: What Is It, Treatment, Causes & Prevention", 10 thg 9, 2021; Midland Skin — "Hormonal acne & cystic acne - Best treatments"]

**Run 3** — `sample_id: google-ai-mode-2026-09-22-SK-08-r3` — timestamp_utc: 2026-09-22T16:00:10Z — region_observed: UI Vietnamese, ANSWER BODY in Vietnamese — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Accutane (Isotretinoin)
brands_cited: none observed
brands_recommended (rank_position, list_ordered:no, tie:no): Accutane — offered as the oral/last-resort tier option
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: —
> Để điều trị mụn nội tiết ở cằm... [oral prescription tier: Spironolactone, thuốc tránh thai kết hợp, Isotretinoin (Accutane); topical tier: Adapalene, Tretinoin, Benzoyl Peroxide, Salicylic Acid, Azelaic Acid; lifestyle section]. [Right rail: aafp.org — "Acne Management: Guidelines From the American Academy of...", Vinmec — "The emergence of acne on the chin", 24 thg 1, 2026; Midland Skin — "Hormonal acne & cystic acne - Best treatments"]

**Run 4** — `sample_id: google-ai-mode-2026-09-22-SK-08-r4` — timestamp_utc: 2026-09-22T16:00:30Z — region_observed: UI Vietnamese, ANSWER BODY in Vietnamese — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Accutane (Isotretinoin)
brands_cited: none observed
brands_recommended (rank_position, list_ordered:no, tie:no): Accutane
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: recommends Cleveland Clinic Hormonal Acne Guide and AAD protocols by name as reference sources (not brands)
> Để điều trị mụn nội tiết ở vùng cằm một cách hiệu quả... [oral tier: Spironolactone, thuốc tránh thai, Isotretinoin (Accutane); topical tier: Retinoids (Adapalene/Tretinoin), Benzoyl Peroxide, Axit Salicylic, Axit Azelaic; lifestyle section]. [Right rail: aafp.org — "Acne Management: Guidelines From the American Academy of...", Vinmec — "The emergence of acne on the chin", 24 thg 1, 2026; Superdrug Online Doctor — "Hormonal Acne: Symptoms, Causes & Treatment", 27 thg 3, 2025]

**Run 5** — `sample_id: google-ai-mode-2026-09-22-SK-08-r5` — timestamp_utc: 2026-09-22T16:00:50Z — region_observed: UI Vietnamese, ANSWER BODY in Vietnamese — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): Differin Gel, Accutane (Isotretinoin)
brands_cited: none observed
brands_recommended (rank_position, list_ordered:no, tie:no): Differin Gel, Accutane
sponsored_units: none observed | screenshot_ref: none — not run_index 1 | notes: this run names a specific retail source for Differin Gel inline ("tại Chợ Tình Của Boo", a Vietnamese e-commerce seller) — the only run in this prompt (or arguably this file) to name a specific retailer inline in prose rather than in a product card; adds a comparison table (topical vs. hormonal approach) not seen in other runs
> Để điều trị mụn nội tiết (hormonal acne) ở vùng cằm... Retinoids (Adapalene, Tretinoin): "...dòng không kê đơn như Adapalene 0.1% (ví dụ: Differin Gel tại Chợ Tình Của Boo)." Benzoyl Peroxide, Axit Salicylic, Axit Azelaic. Oral tier: Spironolactone ("tiêu chuẩn vàng"), thuốc tránh thai, Isotretinoin (Accutane). Comparison table: topical vs. hormonal approach by mechanism/acne type/time-to-effect/caveat. Lifestyle section. [Right rail: aafp.org — "Acne Management: Guidelines From the American Academy of...", Cleveland Clinic — "Hormonal Acne: What Is It, Treatment, Causes & Prevention", 10 thg 9, 2021; First Aid Beauty — "Hormonal Acne – First Aid Beauty", 15 thg 7, 2025]

#### SK-09 — P — "my skin barrier is damaged from over-exfoliating — what should I use?" — arm: main — achieved_n: 1/5

Session scope reached after this run — see closing summary and Not-sampled table below. Unlike SK-08's near-brandless answers, this run names three drugstore/consumer brands as generic-category examples (a different pattern within the same P-prompt kind).

**Run 1** — `sample_id: google-ai-mode-2026-09-22-SK-09-r1` — timestamp_utc: 2026-09-22T16:01:58Z — region_observed: UI Vietnamese, answer English — search_toggle: not exposed — answer_outcome: answered
brands_mentioned (order): CeraVe (Hydrating Cleanser), Vaseline (Petroleum Jelly), Aquaphor (Healing Ointment)
brands_cited: none observed
brands_recommended (rank_position, list_ordered:no, tie:yes — named as illustrative category examples within a routine, not ranked): CeraVe Hydrating Cleanser, Vaseline Petroleum Jelly, Aquaphor Healing Ointment
sponsored_units: none observed | screenshot_ref: docs/raw/screenshots/ (temp path, see notes) | notes: medical disclaimer footer present (same text as SK-04/SK-08); structured as a 4-step recovery protocol (pause stressors / minimalist routine / barrier-supportive ingredients / recovery timeline) rather than a product-comparison list
> To heal a skin barrier damaged by over-exfoliation, you must stop all active ingredients immediately and strip your skincare down to a basic three-step routine focusing on hydration and protection... 1. Pause All Skin Stressors (10-14 days): chemical exfoliants, cell-turnover actives, physical tools. 2. Minimalist Recovery Routine: Cleanse — "A formula like the CeraVe Hydrating Cleanser removes impurities without dissolving your skin's remaining natural lipids." Moisturize — rich, fragrance-free, within 5 min of washing. Protect — mineral sunscreen (zinc oxide) preferred over chemical filters on sensitized skin. Seal (optional) — "apply a thin layer of an occlusive ointment like Vaseline Petroleum Jelly or Aquaphor Healing Ointment." 3. Barrier-Supportive Ingredients to look for: ceramides/cholesterol/fatty acids, squalane/glycerin, panthenol/allantoin. 4. Recovery Timeline: mild 3-5 days, moderate/severe 2 weeks-1 month. To help suggest next steps: current symptoms? skin type? products/brands on hand? [Right rail: Dr Tass Cosmetic & Skin Clinics — "Signs of Over-Exfoliated Skin and How to Repair Your Barrier", 15 thg 6, 2026; Acure — "Signs of Over-Exfoliated Skin (And How to Fix It)", 5 thg 5, 2025; REFORM Skincare — "How to Fix an Over-Exfoliated Skin Barrier: 48-Hour Recovery...", 22 thg 7, 2026]

**Not-sampled — session scope reached.** `not-sampled: session tool-call budget reached before this run could be attempted; no engine block, no CAPTCHA, no login wall — a pure scope-management stop, identical in kind to the precedent set by `e-claude-panel-2026-09-22.md` (stopped after C prompts + 3 toggle runs + 2 P prompts) and `e-gemini-panel-2026-09-22.md` (stopped after 24/160). Recommended follow-up: a `-remainder` task, same as those two files received, continuing from SK-09 run 2.`

| id | kind | vertical | prompt | achieved_n |
|---|---|---|---|---|
| SK-09 | P | Skincare | my skin barrier is damaged from over-exfoliating — what should I use? | 1/5 (runs 2-5 not-sampled: session scope) |
| SK-10 | P | Skincare | I have melasma and nothing is working. what should I try? | 0/5 |
| BS-08 | P | B2B SaaS | our sales team is losing deals because follow-ups get missed. what software fixes that? | 0/5 |
| BS-09 | P | B2B SaaS | we need SOC 2 evidence collection without hiring anyone. what should we use? | 0/5 |
| BS-10 | P | B2B SaaS | what should we use to stop paying for SaaS licences nobody uses? | 0/5 |
| HR-04 | P | High-CPA regulated | I have a 640 credit score and need a card that will approve me. what should I apply for? | 0/5 |
| HR-08 | P | High-CPA regulated | my home insurance was just non-renewed. what do I do and who should I go to? | 0/5 |
| HR-12 | P | High-CPA regulated | I'm always tired in the afternoon. what supplement should I take? | 0/5 |

## X prompts — comparison — primary arm (Google AI Mode) — not sampled this session

Not reached (session scope). Per protocol rule 2 (first sample date, no previous-date pool exists — fill from this date's own completed C-prompt answers, single-engine pool since only Google AI Mode was sampled today), the slot fills **were computed** from the 14 C-prompt runs landed above, so a follow-up task can use them directly without recomputing:

- **Skincare**: pooling `brands_mentioned` across all 20 SK-01–SK-04 runs (including context-only mentions, per the counting rule "mention... counted once per run"), La Roche-Posay leads with 13 run-mentions, CeraVe second with 11. **`{A}=La Roche-Posay, {B}=CeraVe`**.
- **B2B SaaS**: BS-01 through BS-04 each cover a distinct tool category (help desk / CRM / project management / HR-payroll) with disjoint brand sets, producing a 13-way tie at 5 run-mentions each (every prompt's #1-ranked brand appears in all 5 of that prompt's runs). Tie-broken by mean `rank_position` (all four category leaders — HubSpot, Linear, Rippling, Zendesk — tie again at mean rank 1.0), then alphabetically. **`{A}=HubSpot, {B}=Linear`**.
- **High-CPA regulated**: same disjoint-category pattern across HR-01/02/05/06/09/10 (travel card / cashback card / life insurance / pet insurance / creatine / magnesium), a 12-way tie at 5 mentions, tie-broken by mean rank (Banner Life, Chase Sapphire Preferred and Wells Fargo Active Cash tie at mean rank 1.0), then alphabetically. **`{A}=Banner Life, {B}=Chase Sapphire Preferred`**.

**Caveat on these fills, for the analyst:** because each vertical's C prompts in this prompt set cover disjoint product sub-categories rather than one directly-comparable category, the vertical-wide pooling rule produces slot fills that are mechanically correct per protocol but not necessarily meaningful for the specific X-prompt being filled — e.g. BS-05 ("{A} vs {B} for a mid-market company — which should we buy?") would ask AI Mode to compare a CRM (HubSpot) against a project-management tool (Linear), which are not substitute purchases. This is flagged here rather than silently deviated from the protocol's literal rule; the X-prompt-sampling agent (this file's own remainder, or a fresh task) should decide whether to run the fills as computed or flag `slot_fill: n/a — cross-category pairing not meaningful` per prompt and note the deviation there instead.

| id | kind | vertical | prompt (slots unresolved) | slot_fill computed | achieved_n |
|---|---|---|---|---|---|
| SK-05 | X | Skincare | {A} vs {B} for dry skin — which is better? | La Roche-Posay / CeraVe | 0/5 |
| SK-06 | X | Skincare | is {A} worth the price compared to {B}? | La Roche-Posay / CeraVe | 0/5 |
| SK-07 | X | Skincare | {A} vs {B}: which has better ingredients for acne-prone skin? | La Roche-Posay / CeraVe | 0/5 |
| BS-05 | X | B2B SaaS | {A} vs {B} for a mid-market company — which should we buy? | HubSpot / Linear | 0/5 |
| BS-06 | X | B2B SaaS | {A} vs {B}: which is cheaper at 100 seats? | HubSpot / Linear | 0/5 |
| BS-07 | X | B2B SaaS | we are moving off {A}. is {B} the right replacement? | HubSpot / Linear | 0/5 |
| HR-03 | X | High-CPA regulated | {A} vs {B} — which credit card earns more on groceries? | Banner Life / Chase Sapphire Preferred (see caveat — HR-03 is card-specific; Banner Life is a life insurer, not a card issuer — this pairing is nonsensical for this specific X prompt despite being the mechanically-computed vertical-wide fill) | 0/5 |
| HR-07 | X | High-CPA regulated | {A} vs {B} for car insurance — which is cheaper for a clean driving record? | Banner Life / Chase Sapphire Preferred (same caveat — neither issues car insurance; a car-insurance-specific fill was never sampled since HR prompt set carries no car-insurance C prompt) | 0/5 |
| HR-11 | X | High-CPA regulated | {A} vs {B}: which protein powder is better tested for heavy metals? | Banner Life / Chase Sapphire Preferred (same caveat — neither is a protein-powder brand; no protein-powder C prompt exists in this set to derive a sensible fill) | 0/5 |

The HR-03/HR-07/HR-11 rows above make the cross-category caveat concrete: this vertical's C-prompt roster (travel card, cashback card, term life, pet insurance, creatine, magnesium) never included car insurance or protein powder as its own C prompt, so no sub-category-matched pool exists for those three X prompts under any reading of the protocol — the vertical-wide fallback is the only mechanical option the protocol provides, and it produces an unusable pairing here. Recommended for the analyst: treat these three specifically as `slot_fill: not-sampled — no comparable sub-category pool available` rather than running them with the literal computed fill, and raise this gap against `panel-protocol.md`'s slot-fill rule for a future revision (not amended here, per task instructions).

## Session summary

**Primary arm (Google AI Mode):** 14 of 14 C prompts complete at n=5 (70/70 runs). 1 of 9 P prompts complete at n=5, a 2nd P prompt (SK-09) at n=1/5. 0 of 9 X prompts sampled (slot fills computed and recorded above for a follow-up). Toggle arm: not-sampled, no toggle control exists on this surface. **Total primary-arm runs achieved: 76 of a possible 176** (70 C + 5 SK-08 + 1 SK-09; 161 main-arm C/P/X runs plus 1 toggle-arm attempt were planned per the task's own arithmetic, achieved 76 main-arm runs, toggle not-sampled).
**Secondary arm (Google AI Overviews):** 14 of 14 C prompts complete at n=1 (14/14 runs) — every run's `answer_outcome: empty`, no AI Overview block rendered on any of the 14 queries.
**Grand total this file: 90 runs landed** (76 AI Mode + 14 AI Overviews), 0 blocked, 0 CAPTCHA, 0 login-wall.

Prompts with `achieved_n` below target: SK-09 (1/5), SK-10/BS-08/BS-09/BS-10/HR-04/HR-08/HR-12 (0/5 each, P kind), all 9 X prompts (0/5 each). 8 prompts at 0/5, 1 prompt at 1/5, out of 18 P+X prompts total. A `-remainder` task, following the `e-claude-panel-2026-09-22-remainder` / `e-gemini-panel-2026-09-22-remainder` naming precedent already queued in `docs/method/STATE.md`, should continue from SK-09 run 2, same prompt set v1, same file-naming convention, `supersedes: none` (this file is not superseded, only extended).

Sponsored/ad units observed across all 90 runs: **0**. No "Sponsored" label, shopping unit explicitly marked as an ad, or any paid placement was found inside any AI Mode answer or AI Overview render. The Vietnamese-localized "Gần đây, N km" local-shopping product carousels seen on two of the 14 plain-search (AI Overview-absent) pages are recorded as an observation, not coded as sponsored units, because no "Sponsored" or equivalent label was present in the extracted text — this is a text-extraction limitation (the label may exist only as an icon or be visually distinguished, not captured by `get_page_text`) and is flagged as `unknown — checked via get_page_text only, no visual/screenshot confirmation of ad-label status` rather than asserted either way.

## Caveats

- **Personalization confound, file-wide.** Every run in this file, both arms, shows a Vietnamese-language UI and VND-denominated prices despite `region_intended: US`, a logged-out session, and an English-language prompt. On several runs the entire AI-generated answer body itself switched to Vietnamese (SK-01 r4, SK-02 r3, SK-03 r4, SK-04 r3, HR-01 r1-r4, HR-10 r3, SK-08 r2-r5) with no pattern found that predicts which runs trigger it. Because this happens **logged-out**, it cannot be an account-Memory effect (contrast `e-claude-panel-2026-09-22.md`, where the same pattern was attributable to account Memory) — it is most plausibly IP-geolocation-based. Brand lists, prices, and even answer language are likely shifted from what a genuinely neutral US session would show; the analyst should treat every brand list in this file as **observed under a Vietnam-network view of a nominally-US query**, not as a clean US-market read.
- **Model version never disclosed.** `model_version_shown: unknown — surface displays none` throughout; Google's AI Mode/AI Overviews carry no visible model name, version tag, or "about this answer" panel content anywhere this session found.
- **Stochasticity confirmed within-session.** Repeated runs of the identical prompt on the identical URL produce materially different brand lists, prices, rankings, and even answer language from run to run (e.g. SK-01's five runs each named a different top-ranked brand). This is consistent with the protocol's own caveat that n=5 resolves only always/sometimes/never, not a single "true" answer — the analyst should read every prompt's five runs as a distribution, never any single run as authoritative.
- **AI Overviews absence may be query-shape-specific, not universal.** All 14 queries sampled here are buying-shaped "best X" queries. This file's finding that zero of them triggered an AI Overview block does not establish that AI Overviews never renders on `google.com/search` generally — only that it did not for this specific prompt set, on this date, on this network path. A different query shape (e.g. a factual or navigational query) was not tested and might behave differently; this is out of scope for this panel's prompt set.
- **Ad/sponsored-unit absence is a text-extraction-scoped finding.** `get_page_text` extracts text content, not visual layout or CSS-driven labels. Zero sponsored units were found in the extracted text across all 90 runs, but a visually-labeled-only "Sponsored" tag (icon-only, or styled without accompanying text) would not appear in this extraction method. Only 2 of 32 planned run-1 screenshots were actually captured this session (SK-01 r1, SK-02 r1, SK-03 r1, SK-04 r1, BS-01 r1, BS-02 r1, BS-03 r1, BS-04 r1, HR-01 r1, HR-02 r1, HR-05 r1, HR-06 r1, HR-09 r1, HR-10 r1, SK-08 r1, SK-09 r1 — 16 total screenshots taken with `save_to_disk`, one per prompt's run 1, saved only to a local temp directory this session and not copied into `docs/raw/screenshots/`; paths given in each run's `screenshot_ref` line point to that temp location, not a repo path). This is a gap the analyst or a follow-up task should close if visual ad-label confirmation is needed.
- **Unsolicited tabs, file-wide.** Multiple tabs not created by this session appeared and disappeared in the shared browser's tab list throughout sampling (`www.kargo.com`, several `chrome://newtab/`, and later a long series of tabs visiting SEC EDGAR, CourtListener, marketing/GEO-conference sites, and vendor case-study pages — evidently other concurrently-running research agents' own tabs bleeding into this session's `tabs_context_mcp` listing). None were read, clicked, navigated, or closed by this session; `tabs_close_mcp` was attempted once on the kargo.com tab and correctly refused ("not in Claude's tab group"), confirming this session never had write access to them.
- **Coverage.** 90 runs across 2 arms, 1 date. This bounds nothing about the market; it measures what these 32 prompts return on Google AI Mode / AI Overviews, from this session's network path, on 2026-09-22.

