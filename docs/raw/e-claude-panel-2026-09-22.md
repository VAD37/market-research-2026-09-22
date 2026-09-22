# Claude — Pass 10 panel, day 0

```yaml
source:          Anthropic — Claude consumer chat surface
url_or_doc_id:   https://claude.ai/new
published:       n/a — live surface, not a document
pull_date:       2026-09-22
pull_method:     browser extension
pull_purpose:    evidence about a number
tier:            1
tier_reason:     table default — measured-by-us
source_label:    measured-by-us
lane:            E
sub_market:      n/a
engine:          Claude — model_version_shown "Fable 5.1" (effort selector: "High"), verbatim from the model picker on claude.ai/new
metric_kind:     visibility
supersedes:      none
captured:        full page, per run — chat transcript via get_page_text + screenshot for run_index 1
prompt_set:      panel-protocol v1
runs_n:          see achieved_n per prompt below
surface:         consumer chat
region:          intended US — observed: see deviations. No interface region selector found; account is heavily personalized to Vietnam/Ho Chi Minh City (see below)
pass:            P10
```

## deviations

- **Login state**: task instructions permit sampling logged-in when the browser already holds a researcher-owned session. `tabs_context_mcp` + navigation to `https://claude.ai/new` landed already authenticated as account "Andy" (plan shown in composer: "Andy · Max"). Recorded per run as `login_state: logged-in (researcher-owned)`. No login/logout/account action was taken.
- **Memory personalization — material confound**: this account has the "Memory" feature enabled (confirmed via the "+" tools menu: Web search checked, Memory checked). Every sampled answer that used web search came back **heavily localized to Vietnam / Ho Chi Minh City**: prices quoted in VND, retail chains named (Pharmacity, Guardian, Watsons), city references ("Saigon heat", "HCMC humidity"), "easy to find in Vietnam" framing. This happened even though the prompt set carries no location, `region_intended` is US, and this is nominally a "fresh chat, no carried context" per the protocol's run definition. The account's persistent Memory (a cross-chat personalization layer, not page/session context) appears to inject the user's inferred location into every fresh chat's answer. This is recorded once here rather than re-argued per run; each run's `region_observed` field states what that specific answer showed. The panel could not disable Memory or sign into a neutral account — doing so would be an account-settings change / new-account action outside this task's authorization. This confound applies to **every run in this file** and should be weighed by the analyst: mention/recommendation rates and even brand identities (a US drugstore panel would differ from a Vietnam pharmacy panel) are likely shifted by this personalization relative to what a neutral US logged-out session would show.
- **Search toggle default**: checked once before sampling began (Chrome extension screenshot of the "+" tools menu on the blank `/new` page): `Web search` was ON (checked) by default for this account. Recorded as `search_toggle: on` for every main-arm run; the toggle was not touched except for the one toggle-flipped arm run per vertical.
- **Timestamps for SK-01 runs 1-4**: `get_current_time` was not polled after each of the first four runs (the procedure was only fixed on run 5). Their `timestamp_utc` values below are reconstructed from tool-call sequence and are marked `~approximate`. From SK-01 run 5 onward every run's timestamp is taken from a `get_current_time` (UTC) call immediately after that run's answer completed, and is exact.
- **Composer automation flakiness**: the Chrome extension's `type` action, when issued as the first action of a fresh batch immediately after a `left_click` on the composer, intermittently failed to enter text (silently — the click registered, focus was visible, but no text appeared; occurred 3 times: SK-01 run 3 first attempt, run 4 first attempt, run 5 first attempt). Fix used throughout: click composer, wait 1s, then issue `type` as its own separate tool call, then verify via screenshot before clicking send. This added tool-call overhead but is mechanical only, not a finding about the surface.
- **Scope reached**: given per-run overhead (compose, wait for generation ~25-35s including this account's web-search step, extract, code brands), completing all 32 prompts x n=5 (160 runs) plus 3 toggle-arm runs was not reached in this session. Priority order per protocol followed: all 14 C prompts x n=5 across all three verticals first (achieved), then the 3 toggle-arm runs (achieved), then P prompts as budget allowed. X prompts were not reached. See per-prompt `achieved_n` and `not-sampled` lines below.

## Records

Schema per run follows `panel-protocol.md` "Record schema". `engine: Claude`, `surface: consumer chat`, `surface_url: https://claude.ai/new` (composer) / actual chat URL noted per run, `prompt_set_version: v1`, `region_intended: US`, `login_state: logged-in (researcher-owned)` for every run unless stated otherwise. Fields repeated per run are given in a compact block; `answer_text_verbatim` follows each block in full.

### Vertical: Skincare and beauty

#### SK-01 — C — "best moisturizer for dry sensitive skin" — achieved_n: 5/5

**Run 1**
```
sample_id: claude-2026-09-22-SK-01-r1
chat_url: https://claude.ai/chat/59ef294e-95f1-4974-bee7-de808e1249f0
timestamp_utc: 2026-09-22T08:01:00Z ~approximate  | local_utc_offset: unknown — surface displays none
model_version_shown: Fable 5.1 (effort: High) | region_observed: no VND/city cue this run; generic answer | search_toggle: on | arm: main
answer_outcome: answered
brands_mentioned (order): CeraVe (CeraVe Moisturizing Cream), La Roche-Posay (La Roche-Posay Toleriane Sensitive / "Riche version")
brands_cited: none observed — no linked/footnoted domains in answer
brands_recommended (rank_position, list_ordered:no, tie:no): 1. CeraVe Moisturizing Cream  2. La Roche-Posay Toleriane Sensitive
sponsored_units: none observed
screenshot_ref: none — not run_index 1 at time captured (see note); no sponsored unit
notes: web-search step shown ("Finding a good moisturizer for dry, sensitive skin", ~8s). No product-card/citation UI this run.
```
answer_text_verbatim:
> CeraVe Moisturizing Cream is the safe pick. Ceramides, hyaluronic acid, no fragrance, no alcohol. Cheap, sold in most Guardian/Watsons.
>
> Two notes:
> - In HCMC humidity the cream can feel heavy by day. Use the Moisturizing Lotion in the morning, the cream at night.
> - If your skin stings from everything, La Roche-Posay Toleriane Sensitive (or the Riche version) is the next step. Fewer ingredients, built for reactive skin. Costs about double.
>
> Skip anything with fragrance, essential oils, or "brightening" claims. Those are the usual culprits for sensitive skin.

**Run 2**
```
sample_id: claude-2026-09-22-SK-01-r2
chat_url: https://claude.ai/chat/e7d701a3-7655-438b-9dbd-f56095e79c30
timestamp_utc: 2026-09-22T08:03:30Z ~approximate | local_utc_offset: unknown — surface displays none
model_version_shown: Fable 5.1 (effort: High) | region_observed: VND pricing ("~350,000 to 500,000 VND (454g)"), "In HCMC humidity", "Widely stocked in Vietnam", pharmacy chains Pharmacity/Guardian named, Shopee named | search_toggle: on | arm: main
answer_outcome: answered
brands_mentioned (order): CeraVe (Moisturizing Cream, Moisturizing Lotion), La Roche-Posay (Toleriane Sensitive), Vanicream (Moisturizing Cream)
brands_cited: none observed — no brand's own domain linked. A product-image card showed three small watermark labels "walmart", "caretobeauty", "dalchaebi" on the product photos themselves (image-source attributions, not confirmed clickable citations, and not the brand CeraVe's own domain) — recorded under sponsored_units, not as citations
brands_recommended (rank_position, list_ordered:no, tie:no): 1. CeraVe Moisturizing Cream  2. La Roche-Posay Toleriane Sensitive  3. Vanicream Moisturizing Cream (CeraVe Moisturizing Lotion also named as the same brand's daytime variant)
sponsored_units: one visible unit — a product-photo gallery card (3 images) captioned "CeraVe Moisturizing Cream" with body copy and a price line "~350,000 to 500,000 VND (454g)", positioned immediately after the collapsed web-search step and before the main prose. No "Sponsored"/"Ad" label text found on close zoom (region 486,188-1083,400) — only small corner watermarks reading "walmart", "caretobeauty", "dalchaebi" on the three photos. Brand in it (CeraVe) also appears in the answer body: yes.
screenshot_ref: docs/raw/screenshots/e-claude-panel-2026-09-22-SK-01-r2.png (not saved to disk this pass — extension screenshot only, see Pull notes)
notes: web-search step ("Picking a top moisturizer recommendation for dry sensitive skin", ~20s+8s)
```
answer_text_verbatim:
> Two rules matter more than the brand.
>
> [product card: "CeraVe Moisturizing Cream" — Fragrance-free, three ceramides plus hyaluronic acid, no common irritants. Repairs the skin barrier rather than just sitting on top, and a barrier fix is what dry sensitive skin usually needs. Widely stocked in Vietnam so you won't fight for it. Trade-off: it's a rich cream. In HCMC humidity that can feel heavy by midday, so use it at night and switch to the lighter CeraVe Moisturizing Lotion or La Roche-Posay Toleriane Sensitive for daytime. If your skin reacts even to this, the stricter option is Vanicream Moisturizing Cream, which strips out almost every possible trigger, but it's harder to find locally. ~350,000 to 500,000 VND (454g)]
>
> Two rules matter more than the brand. Apply it to damp skin within a minute of washing. Buy from a pharmacy chain like Pharmacity or Guardian, not random Shopee sellers, since counterfeits are common for this exact product.
>
> Is this for face, body, or both? That changes the daytime pick.

**Run 3**
```
sample_id: claude-2026-09-22-SK-01-r3
chat_url: https://claude.ai/chat/a9c947d1-1732-4f61-8aab-48d33b18ab91
timestamp_utc: 2026-09-22T08:05:30Z ~approximate | local_utc_offset: unknown — surface displays none
model_version_shown: Fable 5.1 (effort: High) | region_observed: "easy to find in Vietnam", "In Saigon heat" | search_toggle: on | arm: main
answer_outcome: answered
brands_mentioned (order): CeraVe (Moisturizing Cream, Moisturizing Lotion), La Roche-Posay (Toleriane Sensitive)
brands_cited: none observed (image watermarks "walmart", "pharmeasy", "caretobeauty" seen mid-generation on a transient card; final answer text carried no linked domains)
brands_recommended (rank_position, list_ordered:no, tie:no): 1. CeraVe Moisturizing Cream  2. La Roche-Posay Toleriane Sensitive
sponsored_units: transient product-image card observed mid-stream (same pattern as run 2, watermarks "walmart"/"pharmeasy"/"caretobeauty"); not re-verified by zoom this run. Brand in it (CeraVe) also in answer body: yes.
screenshot_ref: none
notes: —
```
answer_text_verbatim:
> If CeraVe breaks you out or you want a backup, La Roche-Posay Toleriane Sensitive is the other safe bet.
>
> CeraVe Moisturizing Cream — Fragrance-free, no alcohol, three ceramides plus hyaluronic acid. That combination is what dry sensitive skin usually needs: repair the barrier, hold water in, add nothing that stings. Dermatologists reach for it first for a reason and it is easy to find in Vietnam. Trade-off: it is thick. In Saigon heat it can feel heavy by midday. If that bothers you, the CeraVe Moisturizing Lotion is the same formula thinned out, fine for daytime, keep the cream for night.
>
> If CeraVe breaks you out or you want a backup, La Roche-Posay Toleriane Sensitive is the other safe bet. Whatever you pick, apply it on damp skin within a minute of washing. That one habit matters more than the brand.

**Run 4**
```
sample_id: claude-2026-09-22-SK-01-r4
chat_url: https://claude.ai/chat/011015b6-2407-42b4-acff-d9a7cf698115
timestamp_utc: 2026-09-22T08:07:30Z ~approximate | local_utc_offset: unknown — surface displays none
model_version_shown: Fable 5.1 (effort: High) | region_observed: "in Saigon humidity", "easy to find in Vietnam", "cheap and everywhere in VN" | search_toggle: on | arm: main
answer_outcome: answered
brands_mentioned (order): La Roche-Posay (Toleriane Double Repair Moisturizer), CeraVe (Moisturizing Cream)
brands_cited: none observed (watermarks "laroche-posay" x2, "beautyartcare" seen on product card images — same image-source-watermark pattern, not a linked brand domain in the answer text)
brands_recommended (rank_position, list_ordered:no, tie:no): 1. La Roche-Posay Toleriane Double Repair Moisturizer  2. CeraVe Moisturizing Cream — note: top-ranked brand differs from runs 1-3 (CeraVe was rank 1 there)
sponsored_units: product-image card, brand La Roche-Posay, watermarks "laroche-posay", "laroche-posay", "beautyartcare"; no explicit ad/sponsored label text found. Brand in it (La Roche-Posay) also in answer body: yes.
screenshot_ref: none
notes: —
```
answer_text_verbatim:
> If it's very dry, add CeraVe Moisturizing Cream (the tub) at night.
>
> La Roche-Posay Toleriane Double Repair Moisturizer — Fragrance-free, ceramides plus niacinamide plus glycerin, and light enough to not feel greasy in Saigon humidity. It's the safe default for dry skin that reacts to things, and it's easy to find in Vietnam. Trade-off: if your skin is very dry rather than just dry, it may not be enough on its own.
>
> If it's very dry, add CeraVe Moisturizing Cream (the tub) at night. Heavier, same fragrance-free ceramide logic, cheap and everywhere in VN.
>
> Two rules that matter more than the brand: no fragrance, no essential oils. Patch test on the jaw for three days before going full face.
>
> Is this for face or body, and is the dryness flaking or just tight?

**Run 5**
```
sample_id: claude-2026-09-22-SK-01-r5
chat_url: https://claude.ai/chat/4e1229c7-84a1-44de-a3b0-2022f3a40f6a
timestamp_utc: 2026-09-22T08:10:09Z (measured, get_current_time UTC) | local_utc_offset: unknown — surface displays none
model_version_shown: Fable 5.1 (effort: High) | region_observed: "shopping advice tailored to the local market" (Claude's own research-step caption), "In humid heat" | search_toggle: on | arm: main
answer_outcome: answered
brands_mentioned (order): CeraVe (Moisturizing Cream, Moisturizing Lotion), Cetaphil (Daily Hydrating), La Roche-Posay (Toleriane Sensitive)
brands_cited: none observed (watermarks "walmart", "pharmeasy", "caretobeauty" on product card, same pattern)
brands_recommended (rank_position, list_ordered:no, tie:no): 1. CeraVe Moisturizing Cream  2. Cetaphil Daily Hydrating (gel, daytime alt)  3. La Roche-Posay Toleriane Sensitive (step-up option)
sponsored_units: product-image card, brand CeraVe, watermarks "walmart"/"pharmeasy"/"caretobeauty", no ad/sponsored label text found. Brand in it also in body: yes.
screenshot_ref: none
notes: research-step caption itself named "Considering shopping advice tailored to the local market" — the surface's own label for its web-search/personalization step, confirming the surface is deliberately localizing.
```
answer_text_verbatim:
> For dry, sensitive skin the safe default is a fragrance-free cream with ceramides and no actives.
>
> [product card: "CeraVe Moisturizing Cream" — Ceramides, hyaluronic acid, no fragrance, no alcohol. Repairs the skin barrier instead of just sitting on top. Cheap for the size and it rarely stings. Trade-off: it's thick. In humid heat it can feel heavy on the face during the day, so use it at night and switch to the lighter CeraVe Moisturizing Lotion or a gel like Cetaphil Daily Hydrating for daytime.]
>
> If your skin reacts to almost everything, La Roche-Posay Toleriane Sensitive is the step up. Fewer ingredients, more forgiving, costs more.
>
> Two rules matter more than the brand: apply on slightly damp skin, and drop anything with fragrance or essential oils. That fixes most "sensitive" complaints on its own.

#### SK-02 — C — "best vitamin C serum under $50" — achieved_n: 5/5

Common to all 5 runs unless noted: `region_intended: US`, `login_state: logged-in (researcher-owned)`, `search_toggle: on`, `arm: main`, `model_version_shown: Fable 5.1 (effort: High)`, `answer_outcome: answered`, `prompt_kind: C`, `slot_fill: n/a`. All 5 runs used web search ("Searched the web" shown). Citation convention used below: `brands_cited` lists only cases where the brand's own domain is printed verbatim (e.g. "maelove.com"); other small source-name chips seen near cards/citations (e.g. "brooklynblonde", "dermapproved", "ringly", "hudabeauty", "glow-log", "Substack") are third-party review/citation sources, not the discussed brand's own domain, and are kept in `notes` rather than counted as brand citations per the coding rule ("a link to a third-party page that merely names the brand is a citation for that third party, not for the brand").

**Run 1** — `sample_id: claude-2026-09-22-SK-02-r1` — `chat_url: https://claude.ai/chat/821be5e3-d8db-4b6f-afb8-646edcaa60fd` — `timestamp_utc: 2026-09-22T08:12:47Z` (measured) — `region_observed: none — USD pricing only, no VN cue this run`
brands_mentioned (order): Maelove (Glow Maker), SkinCeuticals (CE Ferulic — comparison reference only), CeraVe (Skin Renewing Vitamin C), Timeless (20% C+E Ferulic)
brands_cited: maelove.com (printed inline: "maelove.com · $32.95")
brands_recommended (rank, list_ordered:no, tie:no): 1. Maelove Glow Maker  2. CeraVe Skin Renewing Vitamin C (~$23)  3. Timeless 20% C + E Ferulic (~$28) — SkinCeuticals named only as the priced benchmark Maelove is compared against (mention, not recommendation)
sponsored_units: none observed — no product-image card, plain text + one inline citation link
screenshot_ref: docs/raw/screenshots/ — not captured (see Pull notes on screenshot policy)
notes: footer text changed to "Claude is AI and can make mistakes. Please double-check cited sources." (vs. "double-check responses" on SK-01) whenever a citation is present.
answer_text_verbatim:
> Two alternates depending on your skin:
>
> Maelove Glow Maker — The same gold-standard recipe as SkinCeuticals CE Ferulic (15% L-ascorbic acid, vitamin E, ferulic acid, hyaluronic acid) at roughly a third of the price. L-ascorbic acid is the form with the most clinical backing for brightening and collagen. Trade-offs: it oxidizes, so keep it capped and in the dark and use it within about 3 months; the 15% strength can sting if your skin is reactive. maelove.com · $32.95
>
> Two alternates depending on your skin:
> - Sensitive or first time: CeraVe Skin Renewing Vitamin C (~$23). 10% L-ascorbic acid plus ceramides, gentle and easy to find in stores.
> - Want max strength: Timeless 20% C + E Ferulic (~$28). More potent, but stings more and the dropper can leak.
>
> One rule regardless of pick: apply in the morning under sunscreen, and toss it once it turns dark orange.

**Run 2** — `sample_id: claude-2026-09-22-SK-02-r2` — `chat_url: https://claude.ai/chat/97dab254-0dd1-4d48-9e1d-2f332bc83e80` — `timestamp_utc: 2026-09-22T08:13:48Z` (measured) — `region_observed: none — USD pricing only`
brands_mentioned (order): Maelove (The Glow Maker), CeraVe (10%), La Roche-Posay (10%), e.l.f. (Bright Icon)
brands_cited: maelove.com ("maelove.com · $33")
brands_recommended (rank): 1. Maelove The Glow Maker  2. CeraVe 10% ($18)  3. La Roche-Posay 10% ($28, "best texture")  4. e.l.f. Bright Icon ($22)
sponsored_units: none observed
screenshot_ref: none
notes: source chips "brooklynblonde" (under Maelove), "glow-log" (under CeraVe/La Roche-Posay line), "dermapproved" (under e.l.f. line) — third-party citation sources per convention above, not brand domains.
answer_text_verbatim:
> Two cheaper alternatives if that doesn't fit:
>
> Maelove The Glow Maker — 15% L-ascorbic acid with vitamin E, ferulic acid and hyaluronic acid. This is the proven CE Ferulic formula, just cheaper. Trade-offs: pure L-ascorbic acid stings a bit on sensitive skin and oxidizes within a few months once opened, so buy small and use it up. Store it cool and dark. maelove.com · $33
>
> Two cheaper alternatives if that doesn't fit:
> - Sensitive or first-time skin: CeraVe 10% at $18, or La Roche-Posay 10% at $28 for the best texture.
> - Tightest budget: e.l.f. Bright Icon copies the CE Ferulic combination (15% dual vitamin C, 1% vitamin E, 0.5% ferulic) at $22.
>
> One rule that matters more than brand: opaque, airtight packaging. Clear dropper bottles of L-ascorbic acid go orange and useless fast.

**Run 3** — `sample_id: claude-2026-09-22-SK-02-r3` — `chat_url: https://claude.ai/chat/893b5711-31a7-49db-bcdc-4f566a6f5e66` — `timestamp_utc: 2026-09-22T08:15:09Z` (measured) — `region_observed: none — USD pricing only`
brands_mentioned (order): Maelove (The Glow Maker), SkinCeuticals (comparison only), Timeless (20% C+E Ferulic), CeraVe (Skin Renewing Vitamin C Serum)
brands_cited: none observed — Maelove card this run shows only a price ("~$33"), no "maelove.com" domain text printed
brands_recommended (rank): 1. Maelove The Glow Maker  2. Timeless 20% C+E Ferulic ($27.95)  3. CeraVe Skin Renewing Vitamin C Serum ($23)
sponsored_units: none observed — citation chips "maelove", "maelove", "brooklynblonde" appear as small source tags before the Maelove card, no ad/sponsored label text
screenshot_ref: none
notes: chips "ringly", "hudabeauty" near the fallback paragraph — third-party sources, not brand domains.
answer_text_verbatim:
> Maelove The Glow Maker — Same recipe as SkinCeuticals CE Ferulic (15% L-ascorbic acid + vitamin E + ferulic acid) at a third of the price. That trio is the formula with actual clinical backing for brightening and UV protection. Trade-off: pure L-ascorbic acid oxidizes, so buy the 30 ml, store it cool and dark, and toss it when it turns dark orange. Can sting on very sensitive skin. ~$33
>
> Two fallbacks depending on your skin: Timeless 20% Vitamin C + E Ferulic at $27.95 if you want max strength and don't mind a leaky dropper, or CeraVe Skin Renewing Vitamin C Serum at $23, 10% L-ascorbic acid with ceramides if your skin is reactive.
>
> Apply on clean skin in the morning, sunscreen on top. Skip it on retinol nights.

**Run 4** — `sample_id: claude-2026-09-22-SK-02-r4` — `chat_url: https://claude.ai/chat/ecb2c9e1-e94e-4793-ae70-be0e76d5f294` — `timestamp_utc: 2026-09-22T08:16:12Z` (measured) — `region_observed: "shipping to Vietnam is a pain" — explicit Vietnam cue`
brands_mentioned (order): Maelove (Glow Maker), SkinCeuticals (comparison only), e.l.f. (Bright Icon), Timeless (20% C+E+Ferulic), Medik8 (C-Tetra)
brands_cited: maelove.com is not printed as domain text this run (price shown as "$33" only) — brands_cited: none observed
brands_recommended (rank): 1. Maelove Glow Maker  2. e.l.f. Bright Icon (~$22)  3. Timeless 20% C+E+Ferulic (~$25)  4. Medik8 C-Tetra (~$48)
sponsored_units: citation chips "maelove", "maelove", "brooklynblonde" near the Maelove paragraph, no ad/sponsored label text
screenshot_ref: none
notes: explicit "Vietnam" mention — reinforces the Memory-personalization deviation noted in the file header.
answer_text_verbatim:
> Maelove Glow Maker is the pick.
>
> Maelove Glow Maker is the pick. Same chemistry as SkinCeuticals CE Ferulic at a fifth of the price, and it keeps showing up at the top of derm and editor lists.
>
> Maelove The Glow Maker — 15% L-ascorbic acid with vitamin E and ferulic acid, the proven C+E+ferulic combo. Fragrance-free, well tolerated even by sensitive skin. Trade-offs: it's pure L-ascorbic acid, so it oxidizes. Buy 30 mL, keep it cool and dark, and use it within ~3 months of opening. Mild tingle for the first week is normal. $33
>
> Two cheaper options if $33 feels steep or shipping to Vietnam is a pain: e.l.f. Bright Icon (~$22, same C+E+ferulic idea, easier to find) and Timeless 20% C+E+Ferulic (~$25, stronger, more likely to sting). If your skin is reactive, skip pure L-ascorbic acid entirely and go for a derivative like Medik8 C-Tetra (~$48).
>
> One thing that matters more than the brand: apply in the morning under sunscreen. Vitamin C without SPF is half the benefit.

**Run 5** — `sample_id: claude-2026-09-22-SK-02-r5` — `chat_url: https://claude.ai/chat/996d3f93-7f20-47d9-b484-95899be15463` — `timestamp_utc: 2026-09-22T08:17:59Z` (measured) — `region_observed: none — USD pricing only`
brands_mentioned (order): Maelove (The Glow Maker), SkinCeuticals (comparison only, "$180 SkinCeuticals benchmark"), Medik8 (C-Tetra), e.l.f. (Bright Icon)
brands_cited: maelove.com ("maelove.com · $33")
brands_recommended (rank): 1. Maelove The Glow Maker  2. Medik8 C-Tetra ($48)  3. e.l.f. Bright Icon ($22)
sponsored_units: chips "maelove", "maelove", "brooklynblonde" near card, no ad/sponsored label text
screenshot_ref: none
notes: chips "Substack" (near Medik8 line), "dermapproved" (near e.l.f. line) — third-party sources.
answer_text_verbatim:
> Maelove Glow Maker is the consensus pick. Same formula as SkinCeuticals CE Ferulic (15% L-ascorbic acid + vitamin E + ferulic acid) at a third of the price.
>
> Maelove The Glow Maker — 15% L-ascorbic acid plus vitamin E and ferulic acid. Same trio as the $180 SkinCeuticals benchmark, and it comes up as the closest dupe in nearly every under-$50 roundup. Trade-offs: pure L-ascorbic acid stings a little on sensitive skin and oxidizes within a few months once opened, so buy one bottle at a time and keep it out of light. maelove.com · $33
>
> Two alternates depending on your skin:
> - Sensitive or new to vitamin C: Medik8 C-Tetra, $48. Stable form, low irritation.
> - Cheapest good one: e.l.f. Bright Icon, $22. Same C + E + ferulic idea, fragrance-free.
>
> Whichever you pick, opaque bottle and morning use under sunscreen. That matters more than the brand.

#### SK-03 — C — "best sunscreen for daily use under makeup" — achieved_n: 5/5

Common to all 5 runs: `region_intended: US`, `login_state: logged-in (researcher-owned)`, `search_toggle: on`, `arm: main`, `model_version_shown: Fable 5.1 (effort: High)`, `answer_outcome: answered`, `prompt_kind: C`, `slot_fill: n/a`. All runs strongly Vietnam/Asia-localized (see file-header deviation) — recommendations lean K-beauty/J-beauty brands throughout, explicitly framed as "easy to find in HCMC/Vietnam/Asia".

**Run 1** — `sample_id: claude-2026-09-22-SK-03-r1` — `chat_url: https://claude.ai/chat/f890a4dd-fccc-4b0b-9bba-02fcccf4d8c1` — `timestamp_utc: 2026-09-22T08:20:18Z` — `region_observed: "Finding suitable sunscreens available locally in HCMC" (surface's own research-step caption), "easy to find in HCMC", "overpriced in Vietnam"`
brands_mentioned (order): Haruharu Wonder (Black Rice Airyfit SPF50+), Skin1004 (Hyalu-Cica Water-Fit Sun Serum SPF50+), Round Lab (Birch Juice Moisturizing UVLOCK SPF45), Supergoop (Unseen — negative mention)
brands_cited: none observed — no brand's own domain printed
brands_recommended (rank): 1. Haruharu Wonder Black Rice Airyfit  2. Skin1004 Hyalu-Cica Water-Fit Sun Serum  3. Round Lab Birch Juice UVLOCK. Supergoop Unseen named only to advise against it ("Skip Supergoop Unseen here, it's overpriced in Vietnam") = mention, not recommendation, per coding rule.
sponsored_units: two product cards with "Image unavailable" placeholders (images failed to render) — retailer/review citation chips beneath: card1 "dermapproved", "walmart", "business.walmart", "lazada.com"; card2 "megaeletronicos", "costco", "skincupid"; card3 (Round Lab, no chips captured). No ad/sponsored label text found. Brands in cards also in answer body: yes.
screenshot_ref: none
notes: —
answer_text_verbatim:
> Short answer: a lightweight Asian chemical/hybrid SPF 50+. They absorb fast, no white cast, no pilling, and they're easy to find in HCMC.
>
> Haruharu Wonder Black Rice Airyfit Daily Sunscreen SPF 50+ — Top pick for most skin types. Modern filter stack (Mexoryl SX, Tinosorb S, Uvinul A Plus), very light, fragrance free. Leaves skin smooth rather than shiny, so foundation sits well on top. ~$22
>
> Skin1004 Hyalu-Cica Water-Fit Sun Serum SPF 50+ — Best if you're oily or acne prone. Watery serum texture, disappears in seconds, no grease under makeup. Cheap and stocked everywhere in Vietnam.
>
> Round Lab Birch Juice Moisturizing UVLOCK SPF 45 — Best if you're dry or in aircon all day. Hydrating enough for dry patches without slipping on oily zones. Slight dewy finish, works as a primer.
>
> Two rules regardless of pick: give it a minute to absorb before makeup, or it pills, and chemical or hybrid formulas vanish into skin better than pure mineral ones. Skip Supergoop Unseen here, it's overpriced in Vietnam for what it does.

**Run 2** — `sample_id: claude-2026-09-22-SK-03-r2` — `chat_url: https://claude.ai/chat/023e810d-620a-485e-84cb-635fd28f7efe` — `timestamp_utc: 2026-09-22T08:21:19Z` — `region_observed: "in Saigon heat" (lead sentence), "cheap and everywhere in Vietnam"`
brands_mentioned (order): Haruharu Wonder (Black Rice Airyfit), Skin1004 (Madagascar Centella Hyalu-Cica Water-Fit Sun Serum), Biore (UV Aqua Rich Watery Essence), Round Lab (Birch Juice Moisturizing UVLOCK)
brands_cited: none observed
brands_recommended (rank): 1. Haruharu Wonder Black Rice Airyfit ($22, "ranked top pick by dermfnd's May 2026 list")  2. Skin1004 Hyalu-Cica Water-Fit Sun Serum  3. Biore UV Aqua Rich Watery Essence  4. Round Lab Birch Juice UVLOCK
sponsored_units: three product cards, all "Image unavailable"; citation chips: card1 "dermapproved"/"walmart"; card2 "walmart"/"shopee.co"; card3 "purplle"/"thebeautyprismng"/"ukbeautyroom"; card4 "costco"/"megaeletronicos"/"skincupid". No ad/sponsored label text.
screenshot_ref: none
notes: cites a third-party ranking site by name ("dermfnd's May 2026 list") inside the prose — treated as a claim, not a hyperlinked citation (no link rendered).
answer_text_verbatim:
> Short answer: in Saigon heat, a light chemical or hybrid K/J-beauty SPF 50+ is the sweet spot. They sink in fast, no white cast, no pilling. Mineral formulas tend to ball up under foundation.
>
> Haruharu Wonder Black Rice Airyfit Daily Sunscreen SPF 50+ — Modern four-filter stack, fragrance free, weightless. Ranked top pick by dermfnd's May 2026 list. Smooth satin finish that foundation grips well. Best all-rounder for combination or oily skin. $22
>
> Skin1004 Madagascar Centella Hyalu-Cica Water-Fit Sun Serum SPF 50+ — Feels like a hydrating serum, dries down clean. Good if your skin runs dry or gets irritated. Slightly dewy, so pair with powder if you shine by midday.
>
> Biore UV Aqua Rich Watery Essence SPF 50+ — The budget classic. Watery gel, disappears in seconds, cheap and everywhere in Vietnam. Contains alcohol, so skip it if your skin is sensitive. Reapply is easy since it never feels like a layer.
>
> Round Lab Birch Juice Moisturizing UVLOCK SPF 45 — Hydrating without greasiness. Smooth, fresh finish rather than shiny. Good middle ground if you don't know your skin type yet.
>
> One habit matters more than the brand: wait 2 to 3 minutes after applying before foundation. That alone kills most pilling.
>
> If you tell me the skin type (oily, dry, sensitive) I'll narrow it to one.

**Run 3** — `sample_id: claude-2026-09-22-SK-03-r3` — `chat_url: https://claude.ai/chat/3a61eb35-b255-4e32-9786-e8f8f31b3704` — `timestamp_utc: 2026-09-22T08:22:48Z` — `region_observed: "it's a K-beauty product so it's easy to find in Asia"`
brands_mentioned (order): Haruharu Wonder (Black Rice Airyfit), Biore (UV Aqua Rich Watery Essence), Supergoop (Unseen SPF 40 — positive this run, contrast with run 1)
brands_cited: none observed as printed domain
brands_recommended (rank): 1. Haruharu Wonder Black Rice Airyfit ($22)  2. Biore UV Aqua Rich Watery Essence  3. Supergoop Unseen SPF 40 — note: Supergoop flips from "skip it" (run 1) to a positive recommendation (run 3), a within-file stochastic contradiction worth flagging to the analyst.
sponsored_units: one product card (Haruharu Wonder), citation chips "kosco", "dermapproved", "walmart"; separate inline citation chip "dermfnd" after the "tops an independent ranking" sentence; chip "zacjohnson" near the Supergoop paragraph. No ad/sponsored label text.
screenshot_ref: none
notes: this run took two extraction passes — first read caught it mid-generation ("Claude is responding", 27s elapsed), second read after +20s wait showed completion. Generation time for this run exceeded the 28s used elsewhere.
answer_text_verbatim:
> Haruharu Wonder's Airyfit tops an independent ranking of sunscreens for under makeup, built on a modern four-filter stack, and it's a K-beauty product so it's easy to find in Asia.
>
> Haruharu Wonder Black Rice Airyfit Daily Sunscreen SPF 50+ — Modern filter stack (Tinosorb S, Uvinul A Plus, Mexoryl SX) so it's chemical, fragrance-free, no white cast, and dries down in about a minute so foundation won't pill. Light enough for humid weather and oily skin, but not drying. Trade-off: it's a clean-skin-feel formula, not a blurring primer. If you want pore blur or extra grip under makeup, layer a primer over it. $22
>
> Haruharu Wonder's Airyfit tops an independent ranking of sunscreens for under makeup, built on a modern four-filter stack, and it's a K-beauty product so it's easy to find in Asia.
>
> Two alternatives depending on what you want:
> - Cheaper and everywhere: Biore UV Aqua Rich Watery Essence SPF50+. Watery gel, absorbs in seconds, half the price. Slight alcohol smell, can sting sensitive eyes.
> - Primer feel: Supergoop Unseen SPF 40 is invisible, weightless and oil-free, with a velvety makeup-gripping finish. Best if you want the SPF to also blur and grip foundation. Pricier and harder to find outside Western markets.
>
> One rule that matters more than the brand: wait 60 to 90 seconds after applying before foundation. Most pilling comes from rushing that step, not from the sunscreen.

**Run 4** — `sample_id: claude-2026-09-22-SK-03-r4` — `chat_url: https://claude.ai/chat/a6aff4ae-f2be-4ece-9609-02ae0dd29c7f` — `timestamp_utc: 2026-09-22T08:23:53Z` — `region_observed: "Cheap and easy to find in HCMC"`
brands_mentioned (order): Biore (UV Aqua Rich Watery Essence), Skin Aqua (Tone Up UV Essence), Beauty of Joseon (Relief Sun), La Roche-Posay (Anthelios UVMune 400 Invisible Fluid)
brands_cited: none observed — no citation chips or "Searched the web" shown this run (footer read "double-check responses", not "cited sources" — no search-citation UI this run despite a "Finding a good daily sunscreen..." research-step caption)
brands_recommended (rank): 1. Biore UV Aqua Rich Watery Essence  2. Skin Aqua Tone Up UV Essence  3. Beauty of Joseon Relief Sun  4. La Roche-Posay Anthelios UVMune 400 Invisible Fluid
sponsored_units: none observed
screenshot_ref: none
notes: only run of the 5 with no visible citation/source-chip UI, despite the research-step caption implying a search occurred.
answer_text_verbatim:
> Top pick: Biore UV Aqua Rich Watery Essence SPF50+. Thin, sets fast, no white cast, makeup sits on it without pilling. Cheap and easy to find in HCMC.
>
> By skin type:
> - Oily / humid days: Skin Aqua Tone Up UV Essence. Slightly mattifying, evens tone so you need less base.
> - Dry / dehydrated: Beauty of Joseon Relief Sun. Dewy finish, but wait 3-5 min before foundation or it can pill.
> - Sensitive / acne-prone: La Roche-Posay Anthelios UVMune 400 Invisible Fluid. Best filters, pricier.
>
> Rule for under makeup: apply a full amount (about 1/4 tsp for face), let it set 3-5 minutes, then makeup. Reapply midday with a spray or cushion if you're outside a lot.

**Run 5** — `sample_id: claude-2026-09-22-SK-03-r5` — `chat_url: https://claude.ai/chat/ad4339e5-08a2-4722-95eb-74b157f4dbce` — `timestamp_utc: 2026-09-22T08:24:56Z` — `region_observed: "Easy to find in Vietnam, cheap"`
brands_mentioned (order): Beauty of Joseon (Relief Sun), Biore (UV Aqua Rich Watery Essence), Skin Aqua (Tone Up UV Essence), La Roche-Posay (Anthelios UVMune 400 Invisible Fluid)
brands_cited: none observed — no citation chips this run
brands_recommended (rank): 1. Beauty of Joseon Relief Sun  2. Biore UV Aqua Rich Watery Essence  3. Skin Aqua Tone Up UV Essence  4. La Roche-Posay Anthelios UVMune 400 Invisible Fluid
sponsored_units: none observed
screenshot_ref: none
notes: —
answer_text_verbatim:
> For under makeup you want light, fast-absorbing, no pilling. Chemical or hybrid filters, matte to natural finish.
>
> Top pick: Beauty of Joseon Relief Sun (SPF 50+ PA++++). Sits like a moisturizer, no white cast, foundation glides over it. Best for normal to dry skin. Easy to find in Vietnam, cheap.
>
> If your skin is oily: Biore UV Aqua Rich Watery Essence or Skin Aqua Tone Up UV Essence. Both dry down matte and hold makeup well in heat.
>
> If you want a Western option: La Roche-Posay Anthelios UVMune 400 Invisible Fluid. Excellent UVA protection, thin fluid, a bit pricier.
>
> Use two finger-lengths for the face, wait 5 minutes before makeup. Tell me your skin type if you want a single answer.

#### SK-04 — C — "best retinol for beginners" — achieved_n: 5/5

Common to all 5 runs: `region_intended: US`, `login_state: logged-in (researcher-owned)`, `search_toggle: on`, `arm: main`, `model_version_shown: Fable 5.1 (effort: High)`, `answer_outcome: answered`, `prompt_kind: C`, `slot_fill: n/a`.

**Run 1** — `sample_id: claude-2026-09-22-SK-04-r1` — `chat_url: https://claude.ai/chat/59ac52ee-b896-419b-973c-4ee14782098c` — `timestamp_utc: 2026-09-22T08:26:54Z` — `region_observed: "easy to find in HCMC" (x2), "especially in HCMC sun"`
brands_mentioned (order): CeraVe (Resurfacing Retinol Serum), The Ordinary (Retinol 0.2% in Squalane), Differin (adapalene 0.1%)
brands_cited: none observed as printed brand-own domain (citation chips present but all third-party: "skincare-au", "caretobeauty", "essentialshub", "smartoice.com", "luxurydesires", "Walmart", "differin" [likely a review-site handle, not differin.com], "everythingbeautygh", "janeyoomd")
brands_recommended (rank): 1. CeraVe Resurfacing Retinol Serum  2. The Ordinary Retinol 0.2% in Squalane  3. Differin Gel (adapalene 0.1%)
sponsored_units: two "Image unavailable" product cards (CeraVe, The Ordinary) with citation chips as listed above; a third product mention (Differin) with chip "Walmart"/"differin"/"everythingbeautygh". No ad/sponsored label text.
screenshot_ref: none
notes: extraction required 2 passes (first read caught "Claude is responding" mid-stream); this is the first run of this file to surface an explicit routine/usage-instructions block ("How to not ruin your face in week one") citing "janeyoomd" repeatedly (a named skincare-content creator/site) as the routine's source.
answer_text_verbatim:
> Short answer: The Ordinary or CeraVe. Both cheap, both easy to find in HCMC.
>
> CeraVe Resurfacing Retinol Serum — The safest first bottle. Low-dose encapsulated retinol buffered with ceramides and niacinamide, so it protects the barrier while it works. Dermatologists pick this one for beginners over and over. Trade-off: slow results, but that is the point when you're starting.
>
> The Ordinary Retinol 0.2% in Squalane — Cheapest entry point. Plain retinol in squalane oil, nothing fancy. Start here if you want to control the dose yourself and step up to 0.5% then 1% later. Trade-off: oily texture, and no barrier-support extras, so pair it with a decent moisturiser.
>
> Differin Gel (adapalene 0.1%) — Pick this instead if acne is your main problem. It's a former prescription retinoid, stronger than retinol but still tolerable. Works for early ageing too. Trade-off: more drying, so the slow ramp matters even more.
>
> How to not ruin your face in week one:
> - Start 1 to 2 nights a week, ramp up over 4 to 8 weeks. Pea-sized amount for the whole face. Apply to dry skin, 20 to 30 min after washing.
> - Sandwich it: moisturiser, retinol, moisturiser. Cuts irritation a lot.
> - No vitamin C or acids the same night at first.
> - SPF every morning. Non-negotiable, especially in HCMC sun.
>
> Expect 8 to 12 weeks before you see anything. Some flaking around week 2 to 3 is normal. Burning or raw skin means stop and drop the frequency.

**Run 2** — `sample_id: claude-2026-09-22-SK-04-r2` — `chat_url: https://claude.ai/chat/ad0f9733-f7b8-45b1-9e2f-f10eacf4a739` — `timestamp_utc: 2026-09-22T08:27:57Z` — `region_observed: "easy to find in HCMC (Hasaki, Watsons, Guardian)" — names a Vietnamese beauty retailer (Hasaki) explicitly`
brands_mentioned (order): CeraVe (Resurfacing Retinol Serum), Differin (adapalene 0.1%), The Ordinary (Retinol 0.2% in Squalane)
brands_cited: none observed (chip "janeyoomd" repeated — third-party content source, not a brand domain)
brands_recommended (rank): 1. CeraVe Resurfacing Retinol Serum  2. Differin (acne-prone alt)  3. The Ordinary Retinol 0.2% (budget alt)
sponsored_units: none observed — no product-image cards this run, plain text with citation chips only
screenshot_ref: none
notes: cites "A dermatologist guide for 2026" by name-checking "janeyoomd" as the source three times — a single named third-party creator dominates this run's citations.
answer_text_verbatim:
> Short answer: CeraVe Resurfacing Retinol Serum. Low dose, encapsulated, ceramides and niacinamide built in to buffer irritation, and it's easy to find in HCMC (Hasaki, Watsons, Guardian). A dermatologist guide for 2026 names it the best OTC retinol for beginners and recommends starting with OTC retinol at 0.025 to 0.05% before escalating.
>
> Alternatives depending on your skin:
> - Acne-prone or oily: Differin (adapalene 0.1%). Originally prescription, still one of the most effective OTC options for acne and early aging, gentler than tretinoin.
> - Budget: The Ordinary Retinol 0.2% in Squalane. Start at 0.2, not 0.5.
>
> How to start, the part people get wrong:
> 1 to 2 nights a week, ramp up over 4 to 8 weeks. Apply to dry skin, wait 20 to 30 minutes after cleansing. Pea-sized amount. Sandwich it between moisturizer layers. No AHA, BHA or vitamin C the same night. SPF every morning.
>
> Expect 2 to 3 weeks of mild flaking. Push through it, don't add more.

**Run 3** — `sample_id: claude-2026-09-22-SK-04-r3` — `chat_url: https://claude.ai/chat/bc596f5c-87b5-4796-af55-8ef9517dc929` — `timestamp_utc: 2026-09-22T08:28:52Z` — `region_observed: "easy to find in Southeast Asia", "especially in tropical sun"`
brands_mentioned (order): CeraVe (Resurfacing Retinol Serum), The Ordinary (Retinol 0.2% in Squalane), Differin (adapalene 0.1%)
brands_cited: none observed (chip "janeyoomd" repeated)
brands_recommended (rank): 1. CeraVe Resurfacing Retinol Serum  2. The Ordinary Retinol 0.2%  3. Differin (adapalene 0.1%) — all three presented as co-equal options under "Pick one" rather than a single top pick, unlike runs 1/2/4/5
sponsored_units: none observed
screenshot_ref: none
notes: —
answer_text_verbatim:
> Short answer: start low, go slow. The exact bottle matters less than the ramp-up.
>
> Pick one
> - CeraVe Resurfacing Retinol Serum: a dermatologist's pick for best OTC retinol for beginners. Encapsulated, cheap, easy to find in Southeast Asia.
> - The Ordinary Retinol 0.2% in Squalane: cheapest, lowest strength. Fine if you want to test tolerance first.
> - Differin (adapalene 0.1%): a strong starting point for acne-prone or oily skin, gentler than tretinoin but still highly effective. Pick this if breakouts are the goal, not fine lines.
>
> How to use it
> - Start 1 to 2 nights a week, increase over 4 to 8 weeks as tolerated
> - Apply to dry skin, wait 20 to 30 minutes after cleansing
> - Pea-sized amount. Moisturiser before and after (sandwich) if it stings.
> - No AHAs, BHAs, or vitamin C on the same night
> - SPF every morning. Non-negotiable, especially in tropical sun.
>
> First 2 to 4 weeks may bring some dryness or flaking. That is normal. Peeling and burning is not: pull back to once a week.

**Run 4** — `sample_id: claude-2026-09-22-SK-04-r4` — `chat_url: https://claude.ai/chat/15fdce58-c80b-4619-bffc-37101b672bd2` — `timestamp_utc: 2026-09-22T08:29:53Z` — `region_observed: none — USD pricing only this run`
brands_mentioned (order): The Ordinary (Retinol 0.2% in Squalane), CeraVe (Resurfacing Retinol Serum), The Inkey List (Starter Retinol Serum), Differin (adapalene)
brands_cited: theordinary.com ("theordinary.com · ~$6-8")
brands_recommended (rank): 1. The Ordinary Retinol 0.2% in Squalane  2. CeraVe Resurfacing Retinol Serum  3. The Inkey List Starter Retinol Serum (~$14)  4. Differin (adapalene) — offered conditionally ("if acne is the actual goal")
sponsored_units: none observed — plain text plus inline citation link
screenshot_ref: none
notes: chips "parse" (x2), "theinkeylist", "thenodmag" — third-party sources.
answer_text_verbatim:
> Short answer: The Ordinary Retinol 0.2% in Squalane. Cheap, gentle, easy to find.
>
> The Ordinary Retinol 0.2% in Squalane — Lowest common starting strength. Squalane base keeps irritation down. Start 2 nights a week, buffer with moisturizer, move to 0.5% after 2-3 months if your skin is bored. Trade-off: it oxidizes fast, so use it within a few months of opening and keep it away from light. theordinary.com · ~$6-8
>
> Two alternatives if that one's not around: CeraVe Resurfacing Retinol Serum, a gentle budget option that also fades post-acne marks and supports the barrier, and The Inkey List Starter Retinol Serum, made for beginners and sensitive skin, around $14.
>
> If acne is the actual goal, Differin (adapalene) is the better pick, though it's technically not a retinol.
>
> Rules that matter more than the brand: night only, pea-sized amount, moisturizer-retinol-moisturizer sandwich to protect the barrier, and daily SPF, since retinol is useless without it. Expect some dryness in weeks 2-4. That's normal, not a reason to quit.

**Run 5** — `sample_id: claude-2026-09-22-SK-04-r5` — `chat_url: https://claude.ai/chat/fac07b7f-4fc7-488d-a794-803677160a02` — `timestamp_utc: 2026-09-22T08:30:55Z` — `region_observed: the surface's own collapsed research-step caption rendered in **Vietnamese** this run: "Tìm gợi ý retinol phù hợp cho người mới bắt đầu" ("Find retinol suggestions suitable for beginners") — the prompt was typed in English and the final answer is in English; only the internal search-step caption switched language. Strongest single piece of evidence in this file for account-level language/locale personalization bleeding into a nominally fresh, English-language chat.`
brands_mentioned (order): CeraVe (Resurfacing Retinol Serum), The Ordinary (Retinol 0.2% in Squalane)
brands_cited: none observed (chips "skincare-au", "uae.microless", "caretobeauty" — third-party)
brands_recommended (rank): 1. CeraVe Resurfacing Retinol Serum  2. The Ordinary Retinol 0.2% in Squalane (runner-up)
sponsored_units: one "Image unavailable" product card (CeraVe) with the three chips above. No ad/sponsored label text.
screenshot_ref: none
notes: only run in this file where a mid-answer UI element (research-step caption) rendered in a non-English language.
answer_text_verbatim:
> Runner-up: The Ordinary Retinol 0.2% in Squalane.
>
> CeraVe Resurfacing Retinol Serum — Encapsulated retinol at a low concentration, so it releases slowly and irritates less. Ceramides and niacinamide in the base help the skin barrier while you adjust. Cheap, fragrance-free, easy to find in pharmacies. Trade-off: the percentage isn't disclosed and it's gentle, so results are slow. That's the point for a first retinol.
>
> Runner-up: The Ordinary Retinol 0.2% in Squalane. Cheaper, known dose, oilier feel.
>
> How to start: pea-sized amount at night, 2 nights a week for 3 weeks. Then every other night. Moisturiser on top. Sunscreen every morning, no exceptions. Some dryness and flaking in weeks 2 to 4 is normal. Stinging or redness that lasts means back off.
>
> Skip it if you're using benzoyl peroxide or strong acids at the same time. Alternate nights instead.

### Vertical: B2B SaaS

**Operational note for the whole vertical**: partway through BS-01 run 1, the surface began showing a persistent banner "You've used 75% of your weekly limit / Get more usage" on the composer page (first seen at `timestamp_utc: 2026-09-22T08:32:46Z`, still showing unchanged through the end of BS-01 at 08:37:41Z). This is the researcher account's own Claude usage quota, consumed in part by this panel's sampling. It did not block any BS-01 run (all 5 completed), but it is a live risk to completing the remaining prompt set in this session — recorded here per protocol's rate-limit handling ("record achieved_n and the limit message verbatim and continue with the next prompt"). No B2B SaaS answer showed any Vietnam/HCMC localization cue (contrast with the Skincare vertical above) — pricing was USD throughout, no city or country references. Also observed: a second, unrelated automated agent is sharing this browser's tab group concurrently (per task instructions, "another agent is using web search and fetch concurrently, that does not affect you") — its tabs (openai.com bot docs, Cloudflare Radar/blog pages) appeared and changed in `tabs_context_mcp`/screenshot output throughout this vertical's sampling; they were not interacted with.

#### BS-01 — C — "best help desk software for a 50-person support team" — achieved_n: 5/5

Common to all 5 runs: `region_intended: US`, `region_observed: none — USD pricing, no locale cues`, `login_state: logged-in (researcher-owned)`, `search_toggle: on`, `arm: main`, `model_version_shown: Fable 5.1 (effort: High)`, `answer_outcome: answered`, `prompt_kind: C`, `slot_fill: n/a`. Citation convention: `brands_cited` lists only cases where the vendor's own domain is printed; source-name chips such as "mojohelpdesk", "rework", "guideflow", "dupple", "costbench", "automationatlas", "helpdesk" are third-party review/comparison sites, not the discussed vendor's own domain, and are kept in `notes`.

**Run 1** — `sample_id: claude-2026-09-22-BS-01-r1` — `chat_url: https://claude.ai/chat/7e74de30-db36-4bd1-891f-278429e4ac55` — `timestamp_utc: 2026-09-22T08:32:46Z`
brands_mentioned (order): Zendesk (Suite), Freshdesk, Jira Service Management, Intercom (Fin)
brands_cited: none observed (chip "mojohelpdesk" x3, "helpdesk" x1 — third-party)
brands_recommended (rank): 1. Zendesk Suite  2. Freshdesk  3. Jira Service Management (conditional — internal IT)  4. Intercom (Fin) (conditional — AI-deflection/chat-first)
sponsored_units: none observed
screenshot_ref: none
notes: banner "You've used 75% of your weekly limit / Get more usage" first appeared on this run.
answer_text_verbatim:
> Short answer: Zendesk Suite, unless you're on a budget or doing internal IT.
>
> At 50 agents you're squarely mid-market. Zendesk Suite is the best overall for mid-market customer service, with feature depth and omnichannel, but it's expensive at ~$55+ per agent per month. Depth in routing, SLAs and reporting matters more at 50 seats than at 5, and that's where Zendesk earns its price.
>
> The two real alternatives:
> - Freshdesk is the best mid-market alternative to Zendesk, with comparable features and generally cheaper pricing, starting around $15+ per agent. Pick this if budget is the constraint. At 50 seats the gap is real money.
> - Jira Service Management is the natural fit if you already run Jira and this is an internal IT desk rather than customer support.
>
> If chat is your main channel and you want AI deflection front and center, Intercom (Fin) leads for AI-powered support.
>
> One question that changes the pick: is this customer-facing support or internal IT?

**Run 2** — `sample_id: claude-2026-09-22-BS-01-r2` — `chat_url: https://claude.ai/chat/c391bd93-4f6d-4e92-9c4e-f41bb0ad642a` — `timestamp_utc: 2026-09-22T08:33:56Z`
brands_mentioned (order): Zendesk, Freshdesk, Freshservice, Jira Service Management, Intercom (Fin), Help Scout, Hiver
brands_cited: none observed (chips "rework" x2, "guideflow" x2 — third-party)
brands_recommended (rank): 1. Zendesk  2. Freshdesk ("My default recommendation unless you have a specific reason to pay the Zendesk premium")  3. Freshservice / Jira Service Management (conditional, internal IT)  4. Intercom (conditional, SaaS chat-first). Help Scout and Hiver named explicitly to skip = mention, not recommendation ("Skip Help Scout and Hiver...").
sponsored_units: none observed
screenshot_ref: none
notes: this run gives specific pricing tiers (Zendesk Suite Team $55/agent/mo, Professional $115, AI Copilot +$50; Freshdesk Growth $19/agent/mo, Enterprise $89) and a concrete trial recommendation ("trial Freshdesk and Zendesk in parallel for two weeks").
answer_text_verbatim:
> Short answer: at 50 agents you're in Zendesk or Freshdesk territory. Pick between them on budget and channel mix.
>
> Zendesk has the deepest ticketing, routing, and reporting in the category. Suite Team runs $55/agent/mo annual, Professional jumps to $115, and the AI Copilot is a $50/agent add-on. That's the safe pick if you run phone plus chat plus email and need serious SLA and workflow tooling. Budget roughly $3k to $6k/month for 50 seats before AI.
>
> Freshdesk is the value pick for growing teams: Growth starts at $19/agent/mo with Freddy AI, though Enterprise hits $89 and omnichannel costs more. Comparable feature coverage for most teams at maybe half the cost. UI is a bit clunkier. My default recommendation unless you have a specific reason to pay the Zendesk premium.
>
> Two branches worth naming:
> - If this is internal IT rather than customer-facing, look at Freshservice or Jira Service Management instead, since they add ITSM, assets, and incident workflows.
> - If you're a SaaS running conversational, in-app support, Intercom is the pick, with the caveat that its Fin AI agent bills $0.99 per resolution on top of seats.
>
> Skip Help Scout and Hiver. They're clean but built for smaller email-first teams and get thin at your size.
>
> Practical move: trial Freshdesk and Zendesk in parallel for two weeks with a slice of real tickets. The routing and reporting differences show up fast at 50 agents.
>
> Is this customer support or an internal IT desk?

**Run 3** — `sample_id: claude-2026-09-22-BS-01-r3` — `chat_url: https://claude.ai/chat/802d21f9-b93c-4de6-8697-d21eb70fc2cd` — `timestamp_utc: 2026-09-22T08:35:38Z`
brands_mentioned (order): Freshdesk, Zendesk, Intercom, Help Scout, Zoho, Jira Service Management, Freshservice
brands_cited: none observed as a printed own-domain URL (a citation rendered as an article title this run: "Best Helpdesk Software in 2026: 8 Tools I'd Actually Recommend +2" — a third-party roundup title, not a vendor domain; chips "dupple" x2, "costbench", "automationatlas")
brands_recommended (rank): 1. Freshdesk ("my default pick")  2. Zendesk  3. Intercom (conditional)  4. Jira Service Management / Freshservice (conditional, internal IT). Help Scout and Zoho named explicitly to skip.
sponsored_units: none observed
screenshot_ref: none
notes: gives Freshdesk annualized cost at 50 seats (~$33k/yr Pro) vs Zendesk (~$69k/yr Suite Professional) — a rare direct cost comparison between the top two recommended brands.
answer_text_verbatim:
> For 50 agents, the shortlist is really three.
>
> Freshdesk is my default pick. Full ticketing with email, chat, phone, WhatsApp and social, automation, knowledge base and Freddy AI included. Paid plans run $19, $55 and $89 per agent per month billed annually. You get the AI copilot, automations and SLA management on plans that cost less than Zendesk's entry tier, and at mid-size the gap compounds into thousands a year. At 50 seats on Pro you're around $33k/year. The known catch: the interface can feel busy, and past a few dozen agents you hit the complexity tax that pushes big teams toward Zendesk. You're right at that edge.
>
> Zendesk if support is a strategic function and you need deep customization, reporting, or lots of integrations. Starts at $55/agent/mo, with feature depth and ~2,000 integrations. Suite Professional runs $115/agent/month, so ~$69k/year for 50. Roughly double Freshdesk for the equivalent tier.
>
> Intercom only if you're a SaaS product with chat-first support and want the strongest AI agent. $29/seat/mo plus $0.99 per AI resolution. Watch that per-resolution billing at volume. Its pivot to resolution-based pricing is exactly why teams are re-evaluating it.
>
> Skip Help Scout and Zoho at this size. Help Scout is built for small teams and Zoho is only worth it if you're already in that ecosystem.
>
> One question that changes the answer: is this customer-facing support for a product, or internal IT? If IT, the list is Jira Service Management or Freshservice instead.

**Run 4** — `sample_id: claude-2026-09-22-BS-01-r4` — `chat_url: https://claude.ai/chat/20d1e4c0-a802-4f67-b70e-a72e8a51b467` — `timestamp_utc: 2026-09-22T08:36:38Z`
brands_mentioned (order): Zendesk (Suite), Freshdesk, Intercom (Fin), Jira Service Management, HubSpot (Service Hub), ServiceNow, Salesforce (Service Cloud)
brands_cited: none observed (chip "mojohelpdesk" x2)
brands_recommended (rank): 1. Zendesk Suite  2. Freshdesk  3. Intercom (conditional)  4. Jira Service Management (conditional). HubSpot Service Hub, ServiceNow, Salesforce Service Cloud named explicitly to skip ("Skip: HubSpot Service Hub unless...ServiceNow and Salesforce Service Cloud are overkill at 50 seats") = mention only.
sponsored_units: none observed
screenshot_ref: none
notes: —
answer_text_verbatim:
> At 50 agents you're past the "cheap shared inbox" tier and not yet at ServiceNow scale. That narrows it to a few real options.
>
> My pick: Zendesk Suite if this is customer-facing support with email, chat, and phone. It's the safe default at your size. Deep routing, SLAs, reporting, and the biggest integration marketplace. Zendesk Suite starts around $55/agent/month, so budget roughly $3k to $5k per month depending on tier. Expensive, but it won't be the thing that limits you.
>
> Freshdesk if cost matters more. Comparable features to Zendesk, generally cheaper, starting near $15/agent. Reporting and automation are a step weaker. Fine for a team that mostly does email and ticket queues.
>
> Intercom if you're a SaaS product and most support happens in-app or via chat. Its AI agent (Fin) deflects a real share of tickets. Pricing is usage-based and can spike.
>
> Jira Service Management if this is internal IT support, not customers. Different category entirely.
>
> Skip: HubSpot Service Hub unless you already run HubSpot CRM. ServiceNow and Salesforce Service Cloud are overkill at 50 seats.
>
> One question changes the answer: is this external customer support or an internal IT help desk, and what channels matter (email, chat, phone, social)?

**Run 5** — `sample_id: claude-2026-09-22-BS-01-r5` — `chat_url: https://claude.ai/chat/4ae6bde1-8ebe-4a39-9743-641e493844e9` — `timestamp_utc: 2026-09-22T08:37:41Z`
brands_mentioned (order): Zendesk (Suite), Freshdesk, Intercom (Fin), Jira Service Management, Freshservice
brands_cited: none observed (chip "mojohelpdesk" x3, "helpdesk" x1)
brands_recommended (rank): 1. Zendesk Suite  2. Freshdesk  3. Intercom (conditional)  4. Jira Service Management / Freshservice (conditional, internal IT)
sponsored_units: none observed
screenshot_ref: none
notes: —
answer_text_verbatim:
> At 50 agents you're squarely mid-market. The pick depends on one thing: customer support or internal IT.
>
> Customer-facing: Zendesk Suite. It's the best overall for mid-market customer service, with feature depth and omnichannel, but it's expensive, starting around $55+ per agent per month. That's roughly $33k+/year at 50 seats before add-ons. Worth it if you need routing, SLAs, and reporting that hold up under real volume.
>
> Same job, half the bill: Freshdesk. Comparable features, generally cheaper, starting around $15+ per agent. My honest take: most 50-person teams don't use the Zendesk features they pay for. Trial Freshdesk first.
>
> Chat-heavy SaaS product: Intercom. Best AI-powered support with Fin. Strong if deflection matters more than ticket workflows.
>
> Internal IT: Jira Service Management if you already run Jira, else Freshservice.
>
> Which is it, customer or internal? And is your volume mostly email, chat, or voice? That narrows it to one answer.

#### BS-02 — C — "best CRM for a B2B startup under 20 employees" — achieved_n: 5/5

Common to all 5 runs: `region_intended: US`, `region_observed: none — USD pricing, no locale cues`, `login_state: logged-in (researcher-owned)`, `search_toggle: on`, `arm: main`, `model_version_shown: Fable 5.1 (effort: High)`, `answer_outcome: answered`, `prompt_kind: C`, `slot_fill: n/a`. Weekly-limit banner still showing unchanged at 75% throughout. Citation chips this prompt ("craftt", "dench", "vcbacked", "techsifted", "croclub", "withallo") are all third-party review/roundup sites, not vendor domains — no brand's own domain was printed in any of the 5 runs, so `brands_cited: none observed` for every run below.

**Run 1** — `sample_id: claude-2026-09-22-BS-02-r1` — `chat_url: https://claude.ai/chat/b6913b85-e58a-4f4f-8997-7d3feb7c5ee7` — `timestamp_utc: 2026-09-22T08:38:12Z ~approximate (banner-shift retry cycle; first exact read at completion 08:39:28Z, applied to run 2)`
brands_mentioned (order): Attio, Pipedrive, HubSpot, Close, Salesforce (told to skip)
brands_recommended (rank): 1. Attio  2. Pipedrive (conditional, sales-led)  3. HubSpot (conditional, inbound marketing)  4. Close (conditional, outbound calling). Salesforce = mention only ("Skip Salesforce. Overkill until 50+ reps.")
sponsored_units: none observed
screenshot_ref: none
notes: self-flagged vendor bias — "some of the 'best CRM' rankings online are written by Attio itself, so treat the hype with salt" — Claude naming a specific bias risk in its own cited source, worth flagging to the analyst as a rare instance of the surface disclosing potential search-result bias.
answer_text_verbatim:
> Short version: pick by sales motion, not headcount.
>
> Attio is the default I'd take for a modern B2B startup. Free for up to 3 users, fast, custom objects from day one, AI on every record, no marketing-suite bloat. Feels like Notion for CRM. Good if you're technical and want to shape the data model yourself.
>
> Pipedrive if you're pure sales-led. Go-to for teams that want a visual, stage-based pipeline with disciplined follow-ups. Simple, cheap, fewer opinions.
>
> HubSpot only if inbound marketing is part of the plan. Free tier genuinely useful, excellent integrations, marketing plus sales alignment, can get expensive at scale. The pricing cliff past the free tier is real.
>
> Close if you're doing high-volume outbound calling. Built-in calling and email, designed for SDR workflows.
>
> Skip Salesforce. Overkill until 50+ reps.
>
> My call: Attio. Under 20 people, you don't need a marketing suite, and its data model won't fight you when the process changes. Caveat: some of the "best CRM" rankings online are written by Attio itself, so treat the hype with salt. Trial it and Pipedrive side by side for a week.
>
> What's the motion, outbound sales or inbound/product-led? That decides it.

**Run 2** — `sample_id: claude-2026-09-22-BS-02-r2` — `chat_url: https://claude.ai/chat/7b5c32fe-72b0-47e6-88aa-2479044a2a73` — `timestamp_utc: 2026-09-22T08:39:28Z`
brands_mentioned (order): HubSpot, Pipedrive, Attio, Salesforce (told to skip)
brands_recommended (rank): 1. HubSpot ("Default pick")  2. Pipedrive (conditional, outbound)  3. Attio (conditional, technical founders). Salesforce Starter = mention only ("Skip Salesforce Starter at this size").
sponsored_units: none observed — one citation rendered as an article title: "Best CRM for Startups in 2026: 7 Tools That Scale With You +2" (third-party roundup, not a vendor domain)
screenshot_ref: none
notes: top pick flips from Attio (run 1) to HubSpot (run 2) — direct contradiction within the same prompt, n=5, same session.
answer_text_verbatim:
> Default pick: HubSpot. The free tier gives unlimited contacts, a visual deal pipeline, task management, email tracking, meeting scheduling and basic reporting, and paid seats start around $15/seat/mo. Under 20 people, you'll run free or Starter for a long time. Main trap: it gets expensive as you scale into Professional tiers. That's a later problem.
>
> Two cases where I'd pick something else:
> - Pure outbound sales team, pipeline is the whole job: Pipedrive, $14+/seat/mo. Cleaner deal view, less bloat.
> - Technical founders who want a flexible data model and hate rigid CRM schemas: Attio, free to $34+/seat/mo. Nicest to build on top of.
>
> Skip Salesforce Starter at this size. Cost and setup time buy you nothing until 50+ people.
>
> One question that changes the answer: is this for inbound/marketing-led selling or founder-led outbound?

**Run 3** — `sample_id: claude-2026-09-22-BS-02-r3` — `chat_url: https://claude.ai/chat/c5d1f97a-d89f-48e4-9104-72581ef896fb` — `timestamp_utc: 2026-09-22T08:40:33Z`
brands_mentioned (order): Attio, Pipedrive, HubSpot, Salesforce (skip), Close
brands_recommended (rank): 1. Attio ("unless you have a reason not to")  2. Pipedrive (conditional, 1-5 person sales team)  3. HubSpot (conditional, inbound marketing). Salesforce and Close named only in the skip/conditional-aside sentence, not as primary recs beyond Close's one-line mention.
sponsored_units: none observed
screenshot_ref: none
notes: —
answer_text_verbatim:
> Attio, unless you have a reason not to.
>
> For a sub-20 B2B team it hits the right balance: fast, flexible data model, no marketing-suite weight. One 2026 roundup puts it first for most B2B startups: free up to 3 users, custom objects from day one, AI on every record, no bloat. Feels like a database with a pipeline on top rather than a sales tool you fight with.
>
> Two cases where I'd pick something else:
> - Pipedrive if you're a pure sales-led team of 1 to 5 people that just needs a clean pipeline. Simplest to run. Weak reporting, but you won't care yet.
> - HubSpot only if you also need full inbound marketing. The free tier is solid, the paid tiers get expensive fast. Pick it for the ecosystem, not the CRM.
>
> Skip Salesforce. Overkill until 50+ reps. Close is worth a look only if you run heavy outbound with calling built in.
>
> One question that actually changes the answer: is your sales motion founder-led and relationship-heavy, or are you building an outbound SDR process? Attio for the first, Close or Pipedrive for the second.

**Run 4** — `sample_id: claude-2026-09-22-BS-02-r4` — `chat_url: https://claude.ai/chat/6466ff42-008b-4986-8a17-ad6a3f4047b6` — `timestamp_utc: 2026-09-22T08:41:36Z`
brands_mentioned (order): Attio, Close, HubSpot, Pipedrive, Salesforce
brands_recommended (rank): 1. Attio  2. Close (conditional, outbound)  3. HubSpot (conditional, inbound marketing). Pipedrive and Salesforce named only dismissively ("Pipedrive is fine but feels like a 2018 tool next to Attio. Salesforce is overkill...") = mention, not recommendation.
sponsored_units: none observed
screenshot_ref: none
notes: —
answer_text_verbatim:
> Attio. For a B2B startup under 20 people it hits the sweet spot: free for up to 3 users, fast, custom objects from day one, AI on every record, no marketing-suite bloat. Your data model is yours to shape without an admin, and it scales past 20 without a migration.
>
> Two cases where I'd pick something else:
> - Pure outbound sales team, heavy on calls and sequences: Close. Built-in calling and email, designed for SDR workflows, power dialer included.
> - You also need inbound marketing (landing pages, email nurture, forms): HubSpot. HubSpot only makes sense if you also need full inbound marketing. Otherwise you pay for a suite you won't use.
>
> Pipedrive is fine but feels like a 2018 tool next to Attio. Salesforce is overkill until you have dozens of reps.
>
> One caveat: is this sales-led (reps chasing deals) or product-led (self-serve signups)? Attio handles both, but if it's PLG the deciding factor is how well it ingests product usage signals, and that's worth a 30-minute trial before committing.

**Run 5** — `sample_id: claude-2026-09-22-BS-02-r5` — `chat_url: https://claude.ai/chat/42fd02bd-a44b-4117-bd3b-6db00284776e` — `timestamp_utc: 2026-09-22T08:43:33Z`
brands_mentioned (order): HubSpot, Attio, Pipedrive, Salesforce (skip)
brands_recommended (rank): 1. HubSpot Free → Starter ("Default")  2. Attio (conditional, technical/founder-led)  3. Pipedrive (conditional, pure outbound). Salesforce = mention only.
sponsored_units: none observed
screenshot_ref: none
notes: across 5 runs, top pick split: Attio rank-1 in runs 1, 3, 4 (3/5); HubSpot rank-1 in runs 2, 5 (2/5) — a genuine divided-consensus prompt, unlike BS-01's stable Zendesk-first pattern.
answer_text_verbatim:
> Pick by how you sell, not by feature lists. Three real contenders, one default:
>
> Default: HubSpot Free → Starter. The free tier includes unlimited contacts, a visual deal pipeline, task management, email tracking, meeting scheduling, and basic reporting, and the paid Starter at $15/seat/month adds automation and more pipeline stages. Nobody gets fired for this choice. Integrations everywhere, sales and marketing in one place, easy to hand to a first sales hire.
>
> If the team is technical or founder-led selling: Attio. From $29/user/month, billed annually. Flexible data model, feels like Notion or Linear instead of a 2012 sales tool. Weaker marketing side, and pricier per seat.
>
> If it's pure outbound pipeline and nothing else: Pipedrive. 14-day trial, $14/seat/mo, best for sales-focused teams. Simplest deal board there is. Gets cramped once you want marketing or support in the same tool.
>
> Skip Salesforce at this size. You'll pay for runway you won't use for two years and spend a week configuring it.
>
> One trap: per-seat pricing bites once everyone wants read access. Only license the people who actually touch deals.
>
> If you tell me whether it's inbound-led, outbound-led, or product-led, I'll narrow it to one.

#### BS-03 — C — "best project management tool for a remote engineering team" — achieved_n: 5/5

Common to all 5 runs: `region_intended: US`, `region_observed: none — USD pricing, no locale cues`, `login_state: logged-in (researcher-owned)`, `search_toggle: on`, `arm: main`, `model_version_shown: Fable 5.1 (effort: High)`, `answer_outcome: answered`, `prompt_kind: C`, `slot_fill: n/a`. Weekly-limit banner still at 75% throughout. **Linear won rank 1 in all 5 of 5 runs** — the most stable single-brand consensus observed anywhere in this file so far. Citation chips ("eesel", "automationatlas", "toolradar", "guptadeepak", "dupple", "ones") are third-party comparison sites, not vendor domains; `brands_cited: none observed` in every run (no vendor's own domain printed).

**Run 1** — `sample_id: claude-2026-09-22-BS-03-r1` — `chat_url: https://claude.ai/chat/d23b5b0b-985f-41af-8403-77a7eaeaff31` — `timestamp_utc: 2026-09-22T08:45:09Z`
brands_mentioned (order): Linear, Jira, GitHub Projects, Shortcut, Notion, ClickUp
brands_recommended (rank): 1. Linear  2. Jira (conditional, 50+/compliance)  3. GitHub Projects (conditional, <8 people)  4. Shortcut (conditional, "fair middle ground")  5. Notion / ClickUp (conditional, mixed eng+ops team)
sponsored_units: none observed
screenshot_ref: none
notes: explicit self-flagged search-bias note — "Note the search results skew toward vendor content (ONES.com and Shortcut ranking themselves first), so I'm going on what I know teams actually stick with rather than those lists." Second instance in this file (after BS-02 run 1's Attio-bias note) of the model naming vendor self-promotion in its own search results as a reason to discount them.
answer_text_verbatim:
> Linear. That's my pick for most remote engineering teams.
>
> Why: fast, keyboard-driven, tight GitHub/GitLab integration, cycles and projects map cleanly to how devs actually work. Async-friendly. Low ceremony. Engineers don't hate opening it, and that alone decides whether a tool gets used.
>
> When to pick something else:
> - Jira: you're 50+ people, need compliance audits, or non-engineering departments live in the same system. Powerful, heavy, everyone grumbles.
> - GitHub Projects: team under ~8, everything already lives in GitHub, you want zero extra tools. Free, but thin on planning views.
> - Shortcut: Linear-like feel with more built-in docs and roadmap features. Fair middle ground.
> - Notion / ClickUp: only if the team is mixed engineering plus ops/marketing and you want one workspace. Weaker for sprint tracking.
>
> Note the search results skew toward vendor content (ONES.com and Shortcut ranking themselves first), so I'm going on what I know teams actually stick with rather than those lists.
>
> One question that changes the answer: team size, and is it engineers only or cross-functional?

**Run 2** — `sample_id: claude-2026-09-22-BS-03-r2` — `chat_url: https://claude.ai/chat/d2b50128-2a62-48df-b81f-13aaf73a1784` — `timestamp_utc: 2026-09-22T08:46:08Z`
brands_mentioned (order): Linear, Jira, GitHub Projects, Notion, Asana, ClickUp, Monday
brands_recommended (rank): 1. Linear  2. Jira (conditional)  3. GitHub Projects (conditional, tiny team)  4. Notion / Asana (conditional, cross-functional). ClickUp and Monday named explicitly to avoid ("Avoid ClickUp and Monday for a pure eng team...listicles pushing them are mostly vendor blogs") = mention, not recommendation.
sponsored_units: none observed
screenshot_ref: none
notes: another vendor-blog-bias callout, same pattern as run 1.
answer_text_verbatim:
> Linear. Take it as the default for a remote engineering team under ~50 people. Fast, keyboard-driven, cycles and projects map cleanly onto how engineers actually work, GitHub/GitLab integration closes issues from PRs, and it stays out of the way. Async-friendly: good issue history, clean updates, no meeting-driven workflow baked in.
>
> When to pick something else:
> - Jira: you're in a larger org, need compliance/audit trails, or non-engineering departments already live there. Slower, uglier, but it bends to any process.
> - GitHub Projects: tiny team, everything already in GitHub, you want zero extra tool. Weak for roadmaps.
> - Notion or Asana: only if product/design/marketing need to plan in the same place and engineering is a minority. Engineers tend to resent both.
>
> Avoid ClickUp and Monday for a pure eng team. Feature bloat, and the "best of 2026" listicles pushing them are mostly vendor blogs.
>
> One question that changes the answer: is this eng-only, or do PMs and non-technical people need to work inside the same tool daily?

**Run 3** — `sample_id: claude-2026-09-22-BS-03-r3` — `chat_url: https://claude.ai/chat/5bc2b8b5-221a-4b90-86e9-121a576fe9f8` — `timestamp_utc: 2026-09-22T08:47:08Z`
brands_mentioned (order): Linear, Jira, GitHub Projects, ClickUp, Asana, Monday
brands_recommended (rank): 1. Linear  2. Jira (conditional, 500+ engineers)  3. GitHub Projects (conditional). ClickUp, Asana, Monday named explicitly to skip.
sponsored_units: none observed
screenshot_ref: none
notes: gives specific pricing — Linear Standard $8/user/month, free tier up to 250 issues / 2 teams; also names specific integrations (GitHub, GitLab, Sentry, Slack, Notion, Figma) plus "recently added AI agent integrations plus MCP support" as a claimed feature.
answer_text_verbatim:
> Linear. That's the answer for almost every remote engineering team under ~200 people.
>
> Why: fast, keyboard-driven, opinionated workflow so nobody spends a week configuring boards. It integrates natively with GitHub, GitLab, Sentry, Slack, Notion, and Figma, and recently added AI agent integrations plus MCP support. Async-friendly, which matters more than anything for remote. Standard is $8/user/month, free tier covers up to 250 issues and 2 teams.
>
> Two exceptions:
> - Jira. Pick it if you're above ~500 engineers, in a regulated environment, or already deep in Atlassian. Otherwise it's overhead you'll resent.
> - GitHub Projects. Good enough for small teams who live in GitHub and want zero extra tools. Falls apart once you need roadmaps or cross-repo planning.
>
> Skip ClickUp, Asana, Monday for an engineering team. They're built for general work management, not for people who think in issues and PRs.

**Run 4** — `sample_id: claude-2026-09-22-BS-03-r4` — `chat_url: https://claude.ai/chat/63e8b726-705f-409a-927c-3210f9088109` — `timestamp_utc: 2026-09-22T08:48:07Z`
brands_mentioned (order): Linear, Jira, GitHub Projects, Plane, ClickUp, Asana
brands_recommended (rank): 1. Linear  2. Jira (conditional, large org/compliance)  3. GitHub Projects (conditional, small team)  4. Plane (conditional, self-hosted/open source)  5. ClickUp / Asana (conditional, cross-functional)
sponsored_units: none observed
screenshot_ref: none
notes: pricing — Linear free plan 250 issues/2 teams unlimited members, Basic $10/user/month yearly (differs slightly from run 3's "$8/user/month Standard" — same vendor, different plan name/price quoted between runs).
answer_text_verbatim:
> Linear. That's the answer for most remote engineering teams under ~200 people, and the consensus across current comparisons agrees. It's fast, keyboard-first, and its opinionated triage → backlog → cycle workflow enforces good habits without the configuration overhead that buries teams in Jira. Remote teams benefit most from that: async triage, tight GitHub/PR linking, no one spending a week tuning workflows.
>
> When to pick something else:
> - Jira if you're a large org with compliance needs, many teams doing agile differently, or leadership that wants enterprise-grade reporting like velocity trends across sprints filtered by team and issue type. Linear can't do that.
> - GitHub Projects if the team is small, lives in GitHub already, and doesn't want another tool.
> - Plane if you need self-hosted or open source.
> - ClickUp / Asana only if non-engineers (marketing, ops) must share the same tool. Linear will fight cross-functional use rather than adapt.
>
> Pricing check: Linear's free plan covers 250 issues and 2 teams with unlimited members; Basic is $10/user/month yearly.
>
> If you tell me team size and whether non-engineers need in, I can narrow it further.

**Run 5** — `sample_id: claude-2026-09-22-BS-03-r5` — `chat_url: https://claude.ai/chat/8aeee138-de07-4d9a-a68f-b9b2a2480fdf` — `timestamp_utc: 2026-09-22T08:49:04Z`
brands_mentioned (order): Linear, Jira, GitHub Projects, ClickUp, Monday, Asana
brands_recommended (rank): 1. Linear  2. Jira (conditional, enterprise)  3. GitHub Projects (conditional, <10). ClickUp, Monday named explicitly to skip; Asana named as a narrow conditional exception, not a primary rec.
sponsored_units: none observed
screenshot_ref: none
notes: —
answer_text_verbatim:
> Linear. For most remote engineering teams under ~150 people it's the right default: fast, keyboard-driven, opinionated cycles, tight GitHub/GitLab integration, async-friendly (issues carry context so nobody needs a standup to know what's blocked). Engineers actually use it, which is the whole game.
>
> Two exceptions:
> - Jira if you're enterprise, need audit trails, compliance workflows, or already live in Atlassian. Slower and uglier, but nothing matches its configurability and reporting when procurement is in the room.
> - GitHub Projects if the team is small (under 10) and you want zero extra tools. Free, lives next to the code, good enough for a single squad.
>
> Skip ClickUp, Monday, Asana for pure eng teams. They're built for ops/marketing and engineers quietly stop updating them. Asana works for cross-functional planning when the actual engineering toolchain runs elsewhere, which is the polite way of saying that.
>
> One caveat: tool matters less than the async habits. Whatever you pick, enforce written context on every issue and a weekly written status. Remote teams die from missing context, not missing features.

#### BS-04 — C — "best HR and payroll platform for a US company with 200 staff" — achieved_n: 5/5

Common to all 5 runs: `region_intended: US`, `region_observed: none — USD pricing, explicitly US-context prompt`, `login_state: logged-in (researcher-owned)`, `search_toggle: on`, `arm: main`, `model_version_shown: Fable 5.1 (effort: High)`, `answer_outcome: answered`, `prompt_kind: C`, `slot_fill: n/a`. Weekly-limit banner still at 75% throughout. **Rippling won rank 1 in all 5 of 5 runs** — second unanimous-consensus C prompt in this vertical (after BS-03/Linear). Citation chips ("saasrat", "outsail", "johngalt-finance", "payrollsoftwareguide", "rework", "checkr", "paylocity" [likely a review-site handle, not confirmed as paylocity.com], "intervue", "hackernoon") are third-party sources; `brands_cited: none observed` for every run (no vendor's own domain printed as a link).

**Run 1** — `sample_id: claude-2026-09-22-BS-04-r1` — `chat_url: https://claude.ai/chat/02688b83-8da8-41dc-827c-f7ddce1a49a6` — `timestamp_utc: 2026-09-22T08:50:38Z`
brands_mentioned (order): Rippling, Paylocity, Paycor, ADP (Workforce Now), HiBob, Gusto (skip), Justworks (skip)
brands_recommended (rank): 1. Rippling  2. Paylocity / Paycor (conditional, hourly workforce)  3. ADP Workforce Now (conditional, "safest, most boring")  4. HiBob (conditional, culture/people-ops priority). Gusto and Justworks named to skip at 200 headcount = mention only.
sponsored_units: none observed
screenshot_ref: none
notes: gives specific PEPM pricing for Rippling ($20-35), Paylocity ($17-23), HiBob ($19-28).
answer_text_verbatim:
> Short answer: Rippling.
>
> Rippling is my pick for 200 US staff. One employee record drives payroll, benefits, IT (devices, app access), multi-state tax. Fast to run, engineer-friendly API, strong reviews. Roughly $20-35 PEPM depending on modules. Downside: pricing is modular and creeps.
>
> Alternatives depending on fit:
> - Paylocity or Paycor: classic mid-market HR+payroll, good for hourly-heavy workforces with heavy time and attendance needs. Paylocity gets above-average marks for ease of use, strong integrations, and runs about $17-23 PEPM.
> - ADP Workforce Now: safest, most boring, best tax compliance coverage. Clunkier UI, sales-heavy.
> - HiBob: modern HR platform with native US payroll, sweet spot 50-750 employees, $19-28 PEPM. Pick this if culture/people-ops matters more than payroll depth.
>
> Skip Gusto and Justworks at 200. Gusto tops out around 100-150. Justworks is a PEO, different model.
>
> One thing that changes the answer: are they mostly salaried knowledge workers, or hourly with shifts and multiple states? Salaried → Rippling. Hourly/multi-site → Paylocity or ADP.

**Run 2** — `sample_id: claude-2026-09-22-BS-04-r2` — `chat_url: https://claude.ai/chat/0b0ea7b9-c756-463e-bc77-4c2df21452dd` — `timestamp_utc: 2026-09-22T08:51:35Z`
brands_mentioned (order): Rippling, Paycor, Paylocity, Gusto (skip), ADP (Workforce Now, skip-at-this-size framing)
brands_recommended (rank): 1. Rippling ("My default pick for a software company")  2. Paycor (conditional, HR-team-run/price-sensitive)  3. Paylocity (conditional, employee UX priority). Gusto and ADP Workforce Now framed as things to skip/reconsider at this size = mention, not primary recommendation.
sponsored_units: none observed
screenshot_ref: none
notes: names a real-world M&A fact as context — "Paychex bought it [Paycor] in 2025, so it now has big-vendor backing" — a factual claim about corporate ownership embedded in a brand recommendation.
answer_text_verbatim:
> No single winner. At 200 staff the real shortlist is three names, pick by who runs it.
>
> Rippling if the company is tech-forward. HR, payroll, IT and device management in one system, roughly $2,500 to $4,000 a month at 250 employees, and the fastest implementation of the mid-market group at 3 to 6 weeks. My default pick for a software company.
>
> Paycor if an HR team runs it and price matters. Most aggressively priced platform with a real mid-market feature set, around $19 to $27 per employee per month. Paychex bought it in 2025, so it now has big-vendor backing.
>
> Paylocity if employee-facing UX matters more than price. Paycor wins on cost, Paylocity wins on modern UX.
>
> Two to skip at this size: Gusto is at its ceiling (fits lean mid-market under 300 employees, and you will outgrow it). ADP Workforce Now is solid but implementation realistically runs 10 to 16 weeks, worth it only for multi-entity or heavy compliance needs.
>
> One thing that changes the answer: is the company mostly salaried desk workers or hourly/shift workers? Hourly pushes you toward Paycor or Paylocity for time tracking.

**Run 3** — `sample_id: claude-2026-09-22-BS-04-r3` — `chat_url: https://claude.ai/chat/256dbf92-1a75-40d7-bf75-ea1302dc82d2` — `timestamp_utc: 2026-09-22T08:52:35Z`
brands_mentioned (order): Rippling, Paychex, ADP, Justworks, Gusto (skip), BambooHR
brands_recommended (rank): 1. Rippling  2. Paychex / ADP (conditional, hourly/regulated/traditional)  3. Justworks (conditional PEO, benefits-pricing pain point). Gusto explicitly named "the wrong answer at this size"; BambooHR named only as an alternative to Gusto at 100+, not a primary rec here.
sponsored_units: none observed
screenshot_ref: none
notes: gives specific blended cost comparison — Rippling "$60-$80 per user all-in" vs. "Gusto Plus $12/person" — the widest brand-to-brand price spread quoted in this vertical so far.
answer_text_verbatim:
> For 200 staff, the default answer is Rippling. Below that, it depends on one thing: what kind of company.
>
> Rippling is the pick if it's a tech or office company, salaried, some remote. For 50+ employee companies, Rippling is increasingly the default. The IT bundling alone saves an IT hire for the first year or two, and the HRIS is genuinely best-in-class. The downside is implementation: budget 4-6 weeks for a full rollout. Cost is real though. Rippling runs roughly $60-$80 per user all-in when quote-based, versus $12/person for Gusto Plus. At 200 heads that's a meaningful line item.
>
> Paychex or ADP if it's hourly, regulated, or traditional (manufacturing, healthcare, retail). Paychex specifically targets the 1-200 employee segment with a service-first model suited to traditional and regulated businesses. Less slick, but you get a human specialist on the phone.
>
> Justworks (PEO) only if benefits pricing is the pain point. As a PEO, employees are technically co-employed by Justworks, which gives access to large-group benefits rates a small company normally can't get. At 200 you're near the top of its range and close to where a PEO stops making sense.
>
> Gusto is the wrong answer at this size. Outgrowing basic HRIS at 100+ employees points to Rippling or BambooHR instead.
>
> What's the company: salaried tech, or hourly/regulated?

**Run 4** — `sample_id: claude-2026-09-22-BS-04-r4` — `chat_url: https://claude.ai/chat/413ef612-e4a5-4d13-ad3c-a87c8c74fd37` — `timestamp_utc: 2026-09-22T08:53:33Z`
brands_mentioned (order): Rippling, Paylocity, Paycor, ADP (Workforce Now), Gusto (skip)
brands_recommended (rank): 1. Rippling ("what I'd pick unless you have a specific reason not to")  2. Paylocity / Paycor (conditional, hourly/multi-state)  3. ADP Workforce Now (conditional, "safe, boring" choice). Gusto = mention only ("Skip Gusto...cramped by 200").
sponsored_units: none observed
screenshot_ref: none
notes: —
answer_text_verbatim:
> Rippling. At 200 staff it's the strongest default, and it's what I'd pick unless you have a specific reason not to.
>
> Why: it combines HR, payroll, IT and finance in one system and is built to scale with fast-growing teams, so you don't migrate again at 500. Pricing is modular and quote-based, so expect a sales call and costs that stack as you add modules.
>
> The two real alternatives:
> - Paylocity or Paycor if your workforce is mostly hourly, multi-state, and you want hands-on implementation. Rippling is self-service by nature, which suits tech-savvy teams but feels less guided than competitors with dedicated implementation specialists.
> - ADP Workforce Now if leadership wants the safe, boring, nobody-got-fired choice. Older UI, deeper compliance bench.
>
> Skip Gusto. It's payroll-first and built for small US businesses. Good to 50, cramped by 200.
>
> One thing that would change my answer: is this mostly salaried knowledge workers or hourly staff across several states? Hourly and multi-state pushes me toward Paylocity.

**Run 5** — `sample_id: claude-2026-09-22-BS-04-r5` — `chat_url: https://claude.ai/chat/cb8e6c6b-7f5a-4bd4-a148-7589edc2d818` — `timestamp_utc: 2026-09-22T08:54:42Z`
brands_mentioned (order): Rippling, ADP (Workforce Now), Paylocity, Paycor, BambooHR (skip), HiBob
brands_recommended (rank): 1. Rippling  2. ADP Workforce Now (conditional, "safest possible payroll")  3. Paylocity / Paycor (conditional, hourly). BambooHR named explicitly to skip at this size; HiBob mentioned only as "not a US payroll engine on its own" (a limitation note, not a recommendation).
sponsored_units: none observed
screenshot_ref: none
notes: gives an implementation-cost range not seen in other runs — "$20,000 to $200,000 for mid-market" and "a $25 per employee sticker can hit $60+ once integrations and admin are counted."
answer_text_verbatim:
> Short version: at 200 US staff, pick Rippling unless you want the safest possible payroll, then ADP Workforce Now.
>
> Why:
>
> Rippling wins on unified data. Payroll, benefits, devices, and app provisioning all run off one employee record, so onboarding and offboarding stay clean. It fits a tech-forward company with a lean HR team. Downside: modules get pricey as you stack them.
>
> ADP Workforce Now is the boring, safe choice. Certified payroll with guaranteed tax accuracy and penalty protection, plus built-in compliance alerts for FLSA, ACA, FMLA and state labor laws. Roughly $23 to 30 per employee per month base, $30 to 50 with outsourced services. UX is weaker, but multi-state payroll and audits are where it shines.
>
> Paylocity or Paycor sit between the two. Good if you have a lot of hourly staff and care about time and attendance.
>
> Skip BambooHR at this size. Companies with 200+ employees often find they need the configurability of a true mid-market platform, and it leans on third-party payroll. HiBob is a strong HR layer but not a US payroll engine on its own.
>
> One caveat: implementation runs $20,000 to $200,000 for mid-market, and a $25 per employee sticker can hit $60+ once integrations and admin are counted. Get all-in quotes, not module pricing.
>
> Deciding question: is your workforce mostly salaried and remote (Rippling), or hourly and multi-state (ADP or Paylocity)?

### Vertical: High-CPA regulated — cards, insurance, supplements

**Vertical-level deviation, flagged before the records**: on this vertical the Vietnam/HCMC personalization documented in the file header stops being a background flavor detail and becomes the entire answer. All 5 runs of HR-01 below answered with **Vietnamese bank credit cards** (VPBank, VIB, ACB, Vietcombank, Standard Chartered Vietnam, Techcombank, TPBank, MSB, UOB Vietnam) priced in VND, not US cards (no Chase, Amex, Capital One, Citi, Discover, or any US issuer named once across 5 runs) — despite `region_intended: US` and a prompt with no location content. Run 2, run 3 and run 5 state this outright in the answer body ("Assuming you're opening a card in Vietnam," "Two cards worth looking at in Vietnam," "Assuming you're picking from Vietnamese banks"). Run 5's collapsed research-step caption rendered in Vietnamese ("Đánh giá lợi ích của thẻ tích dặm bay so với chi phí thường niên") — the second such non-English caption in this file (after SK-04 run 5). Every run added an unprompted "I'm not a financial advisor" / "Not a financial advisor" disclaimer before signing off, and every run ended by asking a clarifying question rather than closing with a single hard recommendation — both consistent with the protocol's expectation that this vertical produces hedged, refusal-adjacent answers, though none of the 5 runs were a hard refusal (all coded `answered`). **Implication for the analyst**: HR-vertical mention/recommendation rates in this file are rates for Vietnamese financial brands answering a nominally-US prompt, not US brand visibility — a direct product of this account's Memory personalization, not of prompt wording. Recorded once here; not repeated at the same length in every subsequent HR run block below.

#### HR-01 — C — "best travel rewards credit card for someone who flies twice a year" — achieved_n: 5/5

Common to all 5 runs: `region_intended: US`, `region_observed: Vietnam — see vertical-level deviation above`, `login_state: logged-in (researcher-owned)`, `search_toggle: on`, `arm: main`, `model_version_shown: Fable 5.1 (effort: High)`, `answer_outcome: answered`, `prompt_kind: C`, `slot_fill: n/a`. Weekly-limit banner still at 75% throughout. Citation chips ("daiichivn", "t99", "fingo", "acb", "vietnamairlines", "rcgv", "buzdy", "vaynao", "goevo") are Vietnamese financial-content sites; none is a bank's own domain (a bank's own site, e.g. vib.com.vn, acb.com.vn, was never printed) — `brands_cited: none observed` in every run.

**Run 1** — `sample_id: claude-2026-09-22-HR-01-r1` — `chat_url: https://claude.ai/chat/5fddede0-c729-4ff9-b2d5-2a84ccf9d9ee` — `timestamp_utc: 2026-09-22T08:56:47Z`
brands_mentioned (order): VPBank (Vietnam Airlines Platinum), VIB (Premier Boundless, Travel Élite), Vietjet (VPBank YOJO), Vietnam Airlines (co-brand, generic)
brands_recommended (rank): 1. VIB Travel Élite (0% FX fee card, explicit top pick for a light flyer)  2. "flat cashback card with no fee" (generic, no brand named). VPBank Vietnam Airlines Platinum and VIB Premier Boundless named only as the poor-value baseline being argued against = mention, not recommendation. Vietjet VPBank YOJO named to skip.
sponsored_units: none observed
screenshot_ref: none
notes: unprompted disclaimer: "I'm not a financial advisor, and fees and earn rates change often, so verify on the bank's site before applying."
answer_text_verbatim:
> Short version: at two flights a year, a miles card is usually the wrong tool. The annual fee eats the rewards unless you spend heavily.
>
> Rough math on the Vietnam market: earn rates run about 1 mile per 20,000 to 25,000 VND spent on cards like the VPBank Vietnam Airlines Platinum or VIB Premier Boundless, with annual fees from 880,000 to 1.5 million VND. You'd need to put roughly 200 million VND a year through the card to earn a single decent redemption. Two trips a year doesn't justify that.
>
> What actually pays off for a light flyer:
> - A 0% foreign transaction fee card. That saves 3 to 4% on every overseas purchase, hotel, and foreign ticket. VIB Travel Élite is one option with 0% FX fees, though its 899,000 VND fee is only waived at 20 million spend a year. Check the waiver math against your real spend.
> - Or a flat cashback card with no fee. Buy the flights with the cash. Cash is worth more than locked-in miles you may never use.
>
> Skip Vietjet or Vietnam Airlines co-branded cards unless you're loyal to one airline. The Vietjet VPBank YOJO perks are tied to Vietjet and lose value if you don't fly them regularly.
>
> One caveat: if you already spend 15 to 20 million a month on card anyway, a Vietnam Airlines co-brand starts making sense. Then the miles come free.
>
> I'm not a financial advisor, and fees and earn rates change often, so verify on the bank's site before applying. If you tell me your rough monthly card spend and which airline you fly, I can narrow it to one pick.

**Run 2** — `sample_id: claude-2026-09-22-HR-01-r2` — `chat_url: https://claude.ai/chat/6ebc56d1-ba20-4860-8172-641a30a3e7d9` — `timestamp_utc: 2026-09-22T08:57:48Z`
brands_mentioned (order): VPBank (Vietnam Airlines Platinum), VIB (Premier Boundless, Travel Élite), Standard Chartered (EliteFly)
brands_recommended (rank): 1. VIB Travel Élite (explicit "the pick"). Others named only as the comparison baseline.
sponsored_units: none observed
screenshot_ref: none
notes: states outright "Assuming you're opening a card in Vietnam" as its opening line.
answer_text_verbatim:
> Assuming you're opening a card in Vietnam.
>
> At two flights a year, a miles card mostly doesn't pay off. Most of them hand out roughly one mile per 20-25k VND spent (VPBank Vietnam Airlines Platinum: 1 mile per 20,000 VND; VIB Premier Boundless: 1 per 25,000 domestic; Standard Chartered EliteFly: 1 per 25,000). You'd need to spend ~300-500 million VND a year to earn one decent redemption, and the annual fee eats a chunk of that.
>
> What actually matters for a light traveller is the foreign transaction fee (3-4% on every overseas swipe) and lounge access. On that basis the pick is VIB Travel Élite: 0% foreign transaction fee, free airport lounge, 899k VND annual fee waived at 20 million/year spend, lounge capped at 4 visits/year at the base tier. Two trips, four lounge visits, zero FX markup. Fits exactly.
>
> If your two flights are domestic, skip travel cards entirely and get a cashback card. Cashback beats miles at your volume.
>
> Not a financial advisor, and fees change often, so confirm the current terms on VIB's site before applying. Are the trips usually international?

**Run 3** — `sample_id: claude-2026-09-22-HR-01-r3` — `chat_url: https://claude.ai/chat/024e2c88-19d7-4bea-bdea-346d8f9809cf` — `timestamp_utc: 2026-09-22T08:59:12Z`
brands_mentioned (order): ACB (Lotusmiles Pay), Vietcombank (Vietnam Airlines Platinum Amex)
brands_recommended (rank): 1. ACB Lotusmiles Pay ("best fit if you fly Vietnam Airlines," no annual fee). Vietcombank Vietnam Airlines Platinum Amex named and then explicitly told to skip ("Skip it").
sponsored_units: none observed
screenshot_ref: none
notes: quotes a third-party reviewer's own verdict on the Vietcombank card ("the reviewer's own verdict: if you don't fly VNA much, don't use miles or lounges, the card stops being attractive").
answer_text_verbatim:
> Short version: at two flights a year, don't pay for a premium miles card. The annual fee eats the miles.
>
> Two cards worth looking at in Vietnam:
>
> ACB Lotusmiles Pay (best fit if you fly Vietnam Airlines). No issuance or annual fee, and every 20,000 VND spent earns 1 award mile, every 400,000 VND earns 1 qualifying mile. Zero fee means there's no break-even to worry about. Just put daily spend on it and let miles pile up slowly.
>
> Vietcombank Vietnam Airlines Platinum Amex if you want lounge access and trip insurance. 800,000đ/year, and the reviewer's own verdict: if you don't fly VNA much, don't use miles or lounges, the card stops being attractive. At two trips a year that's you. Skip it.
>
> One thing that matters more than miles for a light flyer: foreign transaction fees. Standard cards charge 2-3% on every foreign transaction plus FX markup; travel cards charge 0%. On a $3,000 holiday that's $90 saved. Check the FX fee on whatever you pick. It's the bigger lever at your volume.
>
> Not a financial advisor, so verify current terms before applying. Are those two flights domestic or international? That changes whether FX fees or Lotusmiles matter more.

**Run 4** — `sample_id: claude-2026-09-22-HR-01-r4` — `chat_url: https://claude.ai/chat/9a49b09d-25d7-4d6d-b936-d4f1f9539b38` — `timestamp_utc: 2026-09-22T09:00:11Z`
brands_mentioned (order): VIB (Travel Élite), VPBank (Visa Signature Travel Miles)
brands_recommended (rank): 1. VIB Travel Élite ("Pick"). VPBank Visa Signature Travel Miles offered as a conditional alt ("If you want miles anyway"). A generic "flat cashback card" also offered, unbranded.
sponsored_units: none observed
screenshot_ref: none
notes: "Assuming you're applying in Vietnam" stated outright, matching run 2's phrasing.
answer_text_verbatim:
> At two flights a year, miles cards are a bad deal. You'd need to spend tens of millions VND to earn one domestic ticket, and the annual fee eats most of that. What actually saves money at your frequency is zero FX fee and a couple of lounge visits.
>
> Assuming you're applying in Vietnam:
>
> Pick: VIB Travel Élite. 0% foreign transaction fee (saves 3-4% vs other cards), 899k annual fee waived from 20M spend/year, 4 lounge visits/year at the base tier. The FX saving alone pays for it if you spend abroad on those trips.
>
> If you want miles anyway: VPBank Visa Signature Travel Miles, up to 30 miles per 1,000 VND on travel and dining, Dragon Pass 4 visits/year, but 2M annual fee and 30M/month income requirement. Only makes sense if you put most of your monthly spend on it.
>
> Honest alternative: a flat cashback card and pay for lounges. At two trips a year, cashback likely beats any travel card.
>
> Not a financial advisor, and check the current terms on the bank sites before applying. Do you spend much abroad on those trips, or mostly domestic flights?

**Run 5** — `sample_id: claude-2026-09-22-HR-01-r5` — `chat_url: https://claude.ai/chat/c70d271d-97bf-4847-bd16-f7753bad6ce2` — `timestamp_utc: 2026-09-22T09:01:47Z`
brands_mentioned (order): VIB (Super Card, Travel Élite), Techcombank, TPBank, MSB, UOB (PRVI Miles, Vietnam), Wise
brands_recommended (rank): 1. "a no-fee or low-fee cashback card" — VIB and Techcombank named for cashback rate, TPBank and MSB named for free annual fee (a category recommendation naming 4 brands as co-equal, not one single winner)  2. VIB Travel Élite ("the only miles-adjacent card I'd consider"). UOB PRVI Miles named only as the FX-fee baseline being argued against; Wise named as a non-card alternative ("use a Wise card abroad").
sponsored_units: none observed
screenshot_ref: none
notes: research-step caption rendered in Vietnamese: "Đánh giá lợi ích của thẻ tích dặm bay so với chi phí thường niên" ("Evaluating the benefit of mile-accumulation cards versus annual cost"). Opens with "Assuming you're picking from Vietnamese banks."
answer_text_verbatim:
> Short version: at two flights a year, skip the miles cards. They don't pay off. Assuming you're picking from Vietnamese banks.
>
> Why: the miles cards here earn roughly 1 mile per 20,000 to 25,000 VND spent, with annual fees from 880,000 to 1.5M VND. That's a poor rate. One domestic redemption is ~10k+ miles, meaning 200M+ VND of spend. A cashback card returns more money on the same spend, and cash buys any flight on any airline.
>
> My pick: a no-fee or low-fee cashback card for daily spend. For cashback, VIB and Techcombank rate best; for free annual fees, TPBank and MSB. VIB Super Card lets you pick your own cashback or reward categories, up to 15%.
>
> For the two trips themselves: foreign transaction fees are the real leak. UOB PRVI Miles charges 1.99% on foreign spend, typical for the market. Either use a Wise card abroad, or if you want one "travel" card, VIB Travel Élite has 0% FX fees and lounge access, fee 899,000 VND, waived at 20M/year spend. That's the only miles-adjacent card I'd consider, and only because the fee waiver is easy.
>
> One question: are the flights mostly domestic or international? Domestic changes nothing above. Heavy international spend makes the 0% FX card worth more.
>
> Not a financial advisor. Check current terms on the bank sites before applying.

#### HR-02 — C — "best cashback credit card with no annual fee" — achieved_n: 5/5

Common to all 5 runs: `region_intended: US`, `region_observed: Vietnam (explicit "For Vietnam" / "Assuming Vietnam" openings in 4 of 5 runs)`, `login_state: logged-in (researcher-owned)`, `search_toggle: on`, `arm: main`, `model_version_shown: Fable 5.1 (effort: High)`, `answer_outcome: answered`, `prompt_kind: C`, `slot_fill: n/a`. **TPBank EVO Visa won rank 1 in all 5 of 5 runs** — third unanimous single-brand consensus prompt in this file (after BS-03/Linear and BS-04/Rippling), and the first in the High-CPA vertical. Run 2's research-step caption read "Comparing credit cards suited to an engineer's online spending" — the account's Memory appears to know the user's occupation, not just location, a new personalization dimension beyond city/country. Citation chips ("daiichivn", "fptshop", "crfnetwork", "goevo", "vaynao", "momo") are Vietnamese card-comparison sites; `brands_cited: none observed` in any run (no bank's own domain printed).

**Run 1** — `sample_id: claude-2026-09-22-HR-02-r1` — `chat_url: https://claude.ai/chat/08971c68-e8b0-431b-a77d-d1d27976df2d` — `timestamp_utc: 2026-09-22T09:03:33Z`
brands_mentioned (order): TPBank (EVO Visa), VPBank (StepUp), VIB (Max Card Elite)
brands_recommended (rank): 1. TPBank EVO Visa ("the simplest no-fee answer")  2. VPBank StepUp (conditional, higher rate with spend threshold). VIB Max Card Elite named only as the worse-value comparison point.
sponsored_units: none observed
screenshot_ref: none
notes: research-step caption "Finding no-annual-fee credit cards for Vietnam" — explicit in the collapsed reasoning step, not just the answer body.
answer_text_verbatim:
> For Vietnam, the simplest no-fee answer is TPBank EVO Visa: lifetime free with no conditions, 1% cashback on every transaction. Flat rate, zero maintenance.
>
> If you're willing to hit a spend condition to get the fee waived, two cards beat it on rate:
> - VPBank StepUp: 5% on Grab, Be, Shopee, Lazada, 2% on dining and movies. Fee is 499k but waived if you meet the spend condition. One comparison put its net return around 5.35% on 10M/month of online spend, the highest of the group.
> - VIB Max Card (Elite): 10% headline rate on 15M/month, but nets closer to 3.4% after fees. Worse deal than StepUp unless you spend big.
>
> Standard caveat: rates and waivers shift often, and I'm not a financial advisor. Check the bank's current T&C before applying.
>
> Where does most of your card spend go? Online subscriptions and cloud bills point to StepUp. Groceries and wet market point elsewhere.

**Run 2** — `sample_id: claude-2026-09-22-HR-02-r2` — `chat_url: https://claude.ai/chat/3585a1a3-0f7a-424d-bfc6-405630932b9a` — `timestamp_utc: 2026-09-22T09:04:57Z`
brands_mentioned (order): TPBank (EVO Visa), VPBank (StepUp), VIB (Max Card Elite), HSBC (Visa Cash Back)
brands_recommended (rank): 1. TPBank EVO Visa ("no single winner" framing, but positioned first as the no-condition default)  2. VPBank StepUp (conditional, cloud/SaaS/foreign spend)  3. HSBC Visa Cash Back (conditional, supermarket/education/insurance spend). VIB Max Card Elite named only as the weaker comparison point.
sponsored_units: none observed
screenshot_ref: none
notes: research-step caption "Comparing credit cards suited to an engineer's online spending" — occupation-level personalization, distinct from the location personalization seen throughout the file.
answer_text_verbatim:
> For Vietnam, the honest answer is there's no single winner. Depends on where your spend goes.
>
> Truly free, no conditions: TPBank EVO Visa. Lifetime free with no spending condition, 1% cashback on everything, and online spend tiers up higher: 10% back on online spend from 30M/month, 5% from 10M to under 30M. Boring but zero risk. Good "just have one card" pick.
>
> Free if you spend enough, better rates:
> - VPBank StepUp: 5% on Grab, Be, Shopee, Lazada, 2% dining and cinema. Fee waived on spend. One comparison of international online spend (ads, AWS, Amazon, Netflix) put it at roughly 5.35% net return on 10M/month after fees, beating VIB Max Card Elite at about 3.38%.
> - HSBC Visa Cash Back: 6% on supermarkets, education, insurance (capped 200k/month/category), 0.3% elsewhere. Fee waivable.
>
> My take: if most of your card spend is cloud, SaaS, and foreign online, StepUp wins. If it's scattered and you don't want to track waiver thresholds, EVO.
>
> Not a financial advisor, and promo terms shift often, so check the bank page before applying. What does most of your monthly card spend actually go to?

**Run 3** — `sample_id: claude-2026-09-22-HR-02-r3` — `chat_url: https://claude.ai/chat/f7aacc49-109b-4865-b1b4-b2ffa71efc3d` — `timestamp_utc: 2026-09-22T09:05:58Z`
brands_mentioned (order): TPBank (EVO Visa), VPBank (StepUp), HSBC (Visa Cash Back)
brands_recommended (rank): 1. TPBank EVO Visa ("the safe default")  2. VPBank StepUp (conditional). HSBC Visa Cash Back named with its cap/fee only, not pushed as a primary pick this run.
sponsored_units: none observed
screenshot_ref: none
notes: —
answer_text_verbatim:
> For Vietnam, truly free-for-life with cashback is a short list. The one that stands out: TPBank EVO Visa, lifetime free with no conditions, 1% cashback on every transaction. Flat 1% is not exciting, but zero fee and zero conditions makes it the safe default.
>
> If you can hit a spend threshold, the "free with conditions" cards pay more. VPBank StepUp comes out around 5.35% net on 10M/month online spend with the fee waived once you qualify, and it pays 5% on Grab, Be, Shopee, Lazada and 2% on dining and movies. HSBC Visa Cash Back gives 6% on supermarkets, education and insurance, capped at 200k/month per category, but carries a 499k fee.
>
> My take: EVO if you want zero maintenance. StepUp if most of your spend is Grab/Shopee/online subscriptions and you'll clear the waiver. Not a financial advisor, and card terms shift often, so check the bank's current T&C before applying.
>
> One question that changes the answer: where does most of your monthly spend go? Online/apps, supermarket, or foreign currency (AWS, SaaS)?

**Run 4** — `sample_id: claude-2026-09-22-HR-02-r4` — `chat_url: https://claude.ai/chat/07bbab3b-6e43-4185-9a85-da4473c4e043` — `timestamp_utc: 2026-09-22T09:06:56Z`
brands_mentioned (order): TPBank (EVO Visa), VPBank (StepUP), VIB, Techcombank (Spark)
brands_recommended (rank): 1. TPBank EVO Visa ("Best truly-free pick")  2. VPBank StepUP ("Runner-up"). VIB and Techcombank Spark named as higher-cashback but harder-to-waive alternatives, not pushed as primary.
sponsored_units: none observed
screenshot_ref: none
notes: research-step caption in Vietnamese: "Chọn thẻ ngân hàng phù hợp cho thị trường Việt Nam" ("Choosing a suitable bank card for the Vietnamese market") — third Vietnamese-language caption in this file (after SK-04 r5, HR-01 r5).
answer_text_verbatim:
> Assuming Vietnam. Quick take: almost every "free" cashback card here is only free with spend conditions, so the real question is which one you'll actually clear.
>
> Best truly-free pick: TPBank EVO Visa. It stands out for waiving the annual fee without any conditions, while most others require minimum spend. Cashback up to 10% on online spend, 0% instalments, and you can open it online. Catch: the 10% is capped per month and only on online categories, so real-world return is modest.
>
> Runner-up: VPBank StepUP. 5% on Grab, Be, Shopee, Lazada, plus a flat rate on everything else. Some sources list it as permanently fee-free, but others show a 499,000 VND fee. Confirm the current terms before applying.
>
> If you spend a lot: VIB and Techcombank pay higher cashback, but their fee waivers need big annual spend, e.g. Techcombank Spark needs 150M VND/year, otherwise 899,000 VND/year.
>
> If most of your spend is Grab and Shopee, StepUP wins on rate. If you want zero fee risk and mostly pay online, EVO. Not a financial advisor, just reading the fine print.

**Run 5** — `sample_id: claude-2026-09-22-HR-02-r5` — `chat_url: https://claude.ai/chat/9a6b18b7-a57f-4b65-9acb-cfd34d70915e` — `timestamp_utc: 2026-09-22T09:07:55Z`
brands_mentioned (order): TPBank (EVO Visa), VPBank (StepUp)
brands_recommended (rank): 1. TPBank EVO Visa  2. VPBank StepUp (conditional, online/dev-tool spend)
sponsored_units: none observed
screenshot_ref: none
notes: research-step caption in Vietnamese: "Chọn ra thẻ tín dụng miễn phí phù hợp nhất tại Việt Nam" ("Selecting the most suitable free credit card in Vietnam") — fourth Vietnamese-language caption in this file.
answer_text_verbatim:
> For Vietnam, the one that's actually free for life with no strings: TPBank EVO Visa. Free forever, no conditions, 1% cashback on every transaction. Flat, boring, reliable.
>
> If you're fine with a spend condition to waive the fee, VPBank StepUp beats it on most everyday stuff: 5% on Grab, Be, Shopee, Lazada and 2% on dining and movies. One recent comparison had it netting about 5.35% effective return on 10M/month spend with the fee waived, mostly from online and international payments (ads, AWS, subscriptions).
>
> Two notes. Most "miễn phí thường niên" cards here mean first year free plus waiver if you spend enough, not truly free. And cashback caps per category are usually 200k to 500k/month, so the headline rate only applies to the first few million.
>
> If most of your spend is online/dev tools: StepUp. If you just want zero hassle: EVO. Which bucket are you in?

#### HR-05 — C — "best term life insurance for a 35-year-old non-smoker" — achieved_n: 5/5 (0 of 5 produced a brand recommendation)

**Distinct behavior for this prompt**: unlike every other C prompt in this file, all 5 runs stopped short of naming a single winning brand. Each run gave general framing (what makes a policy "good": level premium, insurer rating, convertibility, ~10x income coverage) and then rendered an interactive multiple-choice widget asking which country/market the policy is for (options varied slightly: "Vietnam / US / Other country/Singapore / Somewhere else / Skip"), before any specific insurer was recommended. Per task instructions, no follow-up was sent (the protocol's prompt is the complete, single turn); each run is recorded as it stood at that widget. This is coded `answer_outcome: answered` for all 5 (substantive text was produced, and the clarifying-question behavior is itself the finding) rather than `refusal` — no run refused to engage with the topic. `region_observed: not resolved — the surface asked rather than assumed, in contrast to every other HR prompt in this file where it silently assumed Vietnam.` `region_intended: US`, `login_state: logged-in (researcher-owned)`, `search_toggle: on`, `arm: main`, `model_version_shown: Fable 5.1 (effort: High)`, `prompt_kind: C`, `slot_fill: n/a` common to all runs. Weekly-limit banner still at 75%.

**Run 1** — `sample_id: claude-2026-09-22-HR-05-r1` — `chat_url: https://claude.ai/chat/05a21b26-8fe5-40f6-9c78-b2a5e8f43ac2` — `timestamp_utc: 2026-09-22T09:09:35Z`
brands_mentioned: none — the answer stopped at "Depends a lot on which market" before naming any insurer
brands_cited: none observed
brands_recommended: none
sponsored_units: none observed
screenshot_ref: none
notes: shortest of the 5 — two sentences of prose then straight to the market-choice widget (options: Vietnam / US / Other country / Skip).
answer_text_verbatim:
> Depends a lot on which market. Insurers, pricing, and underwriting rules differ by country.
>
> [interactive widget: "Which market is this for?" — options: 1 Vietnam, 2 US, 3 Other country, Skip]

**Run 2** — `sample_id: claude-2026-09-22-HR-05-r2` — `chat_url: https://claude.ai/chat/1c10c1fa-a45b-4955-8e63-ff3df213a6e0` — `timestamp_utc: 2026-09-22T09:10:36Z`
brands_mentioned: none
brands_cited: none observed
brands_recommended: none
sponsored_units: none observed
screenshot_ref: none
notes: gives generic underwriting framing (20-year, 10x-income policy from "any top-rated insurer") without naming one; widget options: Vietnam / United States / Singapore / Other Asia / Somewhere else / Skip.
answer_text_verbatim:
> "Best" here mostly comes down to price and insurer strength, not brand. Term life is close to a commodity. For a healthy 35-year-old non-smoker, a 20-year, 10x-income policy from any top-rated insurer is usually the sane baseline. The big variables are which country you're buying in and whether you want level premiums, convertibility, or riders like critical illness.
>
> I'm not a financial advisor, so treat this as framing. Where is this policy being bought? That decides the actual shortlist.
>
> [interactive widget: "Which market is this for?" — options: 1 Vietnam, 2 United States, 3 Singapore / other Asia, 4 Somewhere else, Skip]

**Run 3** — `sample_id: claude-2026-09-22-HR-05-r3` — `chat_url: https://claude.ai/chat/8a925b57-f280-48cb-af13-0be2ebe9fe41` — `timestamp_utc: 2026-09-22T09:11:34Z`
brands_mentioned: none
brands_cited: none observed
brands_recommended: none
sponsored_units: none observed
screenshot_ref: none
notes: gives the fullest underwriting checklist of the 5 runs (level premium, A-rating, convertible, 10x income) without naming any insurer.
answer_text_verbatim:
> Quick framing first: the "best" term policy depends almost entirely on which country you're buying in. For a healthy 35-year-old non-smoker, the checklist is the same everywhere. Level premium locked for the full term (20 or 30 years). Insurer financial rating A or better. Convertible to permanent without a new medical exam. Coverage around 10x annual income. Then you shop the cheapest quote that clears those bars, since term is close to a commodity.
>
> Where the answer diverges is the actual insurers and prices.
>
> [interactive widget: "Which market are you buying in?" — options: 1 Vietnam, 2 US, 3 Other, Skip]

**Run 4** — `sample_id: claude-2026-09-22-HR-05-r4` — `chat_url: https://claude.ai/chat/e8227892-037b-44df-b9f8-2dbd5135a04b` — `timestamp_utc: 2026-09-22T09:12:35Z`
brands_mentioned (order, as market-context examples, not recommendations): Banner, Protective, Pacific Life (named as "strong US carriers"), Prudential, Manulife, AIA, FWD, Bao Viet (named as the Vietnam-market equivalents)
brands_cited: none observed
brands_recommended: none — all eight names are offered as "which brands exist in which market" context, explicitly not narrowed to one, before the same clarifying widget
sponsored_units: none observed
screenshot_ref: none
notes: the only HR-05 run to name any insurer brand at all — 8 named across two markets in a single contrastive sentence, coded as mentions per the coding rule ("named only as context...= mention, not recommendation").
answer_text_verbatim:
> "Best" depends a lot on country. Term life is priced and regulated locally, and the strong carriers in the US (Banner, Protective, Pacific Life) are irrelevant in Vietnam, where you'd be looking at Prudential, Manulife, AIA, FWD, or Bao Viet instead.
>
> The general rules hold anywhere. A healthy 35-year-old non-smoker is near the cheapest rate band, so lock in a 20 or 30 year level-premium term now. Cover 10 to 12x annual income, or enough to clear debts plus dependents' needs. Pick an insurer with a top financial-strength rating and a clean claims record. Skip riders and cash-value add-ons unless there's a specific reason. Not a financial advisor, just the standard framework.
>
> Tell me the market and I can compare actual carriers and rates.
>
> [interactive widget: "Which market is this for?" — options: 1 Vietnam, 2 US, 3 Singapore, 4 Somewhere else, Skip]

**Run 5** — `sample_id: claude-2026-09-22-HR-05-r5` — `chat_url: https://claude.ai/chat/22e44f33-6006-4935-8139-853ca6b5cfe0` — `timestamp_utc: 2026-09-22T09:13:37Z`
brands_mentioned: none
brands_cited: none observed
brands_recommended: none
sponsored_units: none observed
screenshot_ref: none
notes: the only run with **zero prose** — the research-step caption ("Weighing term life guidance and Vietnam market specifics before recommending") is itself notable: it names "Vietnam" as the working assumption in the internal step even though the final visible turn asked the user to choose a market rather than assuming it, a small internal/external inconsistency. No body text rendered before the widget.
answer_text_verbatim:
> [research-step caption only: "Weighing term life guidance and Vietnam market specifics before recommending" — Searched the web]
>
> [interactive widget: "Which market is the policy for?" — options: 1 Vietnam, 2 US, 3 Other country, Skip]

#### HR-06 — C — "best pet insurance for a puppy" — achieved_n: 5/5

Common to all 5 runs: `region_intended: US`, `region_observed: Vietnam (explicit "Assuming you're buying/insuring in Vietnam" in 4 of 5 runs)`, `login_state: logged-in (researcher-owned)`, `search_toggle: on`, `arm: main`, `model_version_shown: Fable 5.1 (effort: High)`, `answer_outcome: answered`, `prompt_kind: C`, `slot_fill: n/a`. Weekly-limit banner still at 75%. Notable: 3 of 5 runs' research-step listed **"read memory"** as an explicit sub-step alongside "searched the web" / "read a page" — the clearest direct confirmation in this file that the surface's Memory feature is an active input to these answers, not just an inference from a generic web search. `brands_cited`: **Fubon** is cited via its own domain ("fubonins" = fubonins.com.vn) in 3 of 5 runs — the first repeated brand-own-domain citation pattern in the High-CPA vertical. Other chips ("ecopets", "pethealthcentre") are third-party sites.

**Run 1** — `sample_id: claude-2026-09-22-HR-06-r1` — `chat_url: https://claude.ai/chat/5509236d-a4dd-45aa-9807-c1437e350cc1` — `timestamp_utc: 2026-09-22T09:15:38Z`
brands_mentioned (order): Liberty (PetCare), INSO, Opes, Bảo Minh, Fubon
brands_cited: Fubon ("Fubon Insurance" chip — ambiguous whether the own domain vs. a review chip; not counted as confirmed brand-domain citation for this run specifically, see run 2 for a clearer case)
brands_recommended (rank): 1. Liberty PetCare ("the one I'd take for a puppy")  2. INSO ("the budget pick")  3. Fubon (conditional, "worth a quote too"). Opes and Bảo Minh named and explicitly dismissed ("Not worth it over INSO").
sponsored_units: none observed
screenshot_ref: none
notes: research-step sequence read "Read memory, searched the web, read a page" — first explicit "read memory" step in this file.
answer_text_verbatim:
> Assuming you're buying in Vietnam. The market is thin, so it's really a two-way pick:
>
> Liberty PetCare is the one I'd take for a puppy. Covers dogs from 2 months to 9 years, accidents effective immediately, 30-day wait for illness, payout cap up to 100 million VND/year with 20% copay, from ~1.5 million VND/year. Only option with a cap big enough to matter for surgery or a serious illness.
>
> INSO is the budget pick. From ~300k VND/year, cap only 20 million VND, but it adds theft and third-party liability. Fine for accidents, thin for anything chronic.
>
> Opes and Bảo Minh sit below both. Caps of 11 million and 8 million respectively. Not worth it over INSO.
>
> Fubon is newer and worth a quote too, but check the fine print. It requires a microchip, age 2 months to 8 years, and excludes French Bulldog, Pit Bull, Tosa, Neapolitan, Dogo Argentino, Fila Brasileiro and Mastiff.
>
> Two things that apply everywhere: pre-existing conditions are never covered, so buying while the puppy is young and healthy is the whole point, and vaccines, deworming and neutering are not covered by any plan.
>
> Honest counterpoint: with a local mutt or a low-risk breed, a 300k to 500k VND/month emergency fund often beats a policy. Insurance earns its keep with high-risk breeds (Bulldog, Golden, Corgi backs).
>
> What breed is the puppy? That decides whether Liberty is worth the premium.

**Run 2** — `sample_id: claude-2026-09-22-HR-06-r2` — `chat_url: https://claude.ai/chat/8120eaf5-d4fb-4383-9fee-b07b95c17be7` — `timestamp_utc: 2026-09-22T09:16:42Z`
brands_mentioned (order): Liberty (PetCare), INSO, Opes, Bảo Minh, Fubon
brands_cited: Fubon (chip "fubonins" — fubonins.com.vn, the brand's own domain)
brands_recommended (rank): 1. Liberty PetCare  2. INSO. Opes, Bảo Minh named and dismissed; Fubon named as a fallback ("worth a quote if Liberty declines your breed").
sponsored_units: none observed
screenshot_ref: none
notes: —
answer_text_verbatim:
> Assuming you're insuring the puppy in Vietnam. Short version: buy now, and Liberty is the only one worth it if you want real coverage.
>
> Under-1-year is the golden window: cheaper premiums, and no pre-existing conditions yet, which is the most common exclusion. Waiting periods are the other reason to move early. Accidents cover from day 0, common illness after 30 days, serious stuff (cancer, hip dysplasia, heart, kidney) after 90 days.
>
> The main options:
> - Liberty PetCare: 2 months to 9 years, accident + illness + burial, up to 100M VND/year, 20% co-pay, from ~1.5M VND/year. The only one with a limit that covers a real surgery or a chronic illness.
> - INSO: up to 20M VND/year, 20-30% co-pay, from ~300k/year, includes theft and third-party liability, fast online signup. Cheap, but 20M caps out at one broken leg.
> - Opes (via VIB app): up to 11M/year, from ~400k, only insures 2 months to 6 years. Bảo Minh: dogs only, up to 8M/year, from ~450k. Both too low to matter.
> - Fubon: newer entrant. Requires microchip, and excludes French Bulldog, Pit Bull, Tosa, Neapolitan, Dogo Argentino, Fila, Mastiff. Worth a quote if Liberty declines your breed.
>
> Nothing covers vaccines, deworming, or neutering. Those are out of pocket everywhere.
>
> My take: Liberty, or skip insurance entirely and put 400k/month into a separate account. The cheap plans give you the paperwork hassle without the payout. One check before buying: confirm your puppy's breed isn't on the insurer's exclusion list, especially for brachycephalic breeds.

**Run 3** — `sample_id: claude-2026-09-22-HR-06-r3` — `chat_url: https://claude.ai/chat/98b74d7f-0292-4a2e-b23c-de34812267ae` — `timestamp_utc: 2026-09-22T09:18:16Z`
brands_mentioned (order): Liberty (PetCare), INSO
brands_cited: none observed this run — no fubonins-style domain printed
brands_recommended (rank): 1. Liberty PetCare  2. INSO ("Budget pick")
sponsored_units: none observed
screenshot_ref: none
notes: research step "Searched the web, read memory, read a page" — second explicit "read memory" instance. Explicitly flags its own source quality: "The article's numbers are from a blog, so confirm on Liberty's and INSO's own sites before paying."
answer_text_verbatim:
> Assuming you're insuring in Vietnam. The market here is thin, but there are real options.
>
> Liberty PetCare is my pick for a puppy if you want coverage that actually matters. Up to 100M VND/year, 20% copay, accidents covered immediately, illness after 30 days, ages 2 months to 9 years, from ~1.5M VND/year. Every other local option caps out at 8 to 20M, which barely covers one surgery.
>
> Budget pick: INSO. Up to 20M/year, from ~300k VND/year, quick online signup, also covers theft. Fine for a healthy mixed breed. Not enough for a Golden, Bulldog, Corgi or anything with known hereditary issues.
>
> Two things that matter more than the brand:
> - Buy now, while it's a puppy. Nothing here covers pre-existing conditions, so the clean slate at under 1 year is the whole value.
> - None of them pay for vaccines, deworming, or neutering. Budget those separately.
>
> The article's numbers are from a blog, so confirm on Liberty's and INSO's own sites before paying.
>
> What breed? That changes whether Liberty is worth the extra ~1.2M a year.

**Run 4** — `sample_id: claude-2026-09-22-HR-06-r4` — `chat_url: https://claude.ai/chat/2ab080e6-378b-478c-9db7-be20cf964f43` — `timestamp_utc: 2026-09-22T09:19:39Z`
brands_mentioned (order): Fubon, Pet Health Centre ("An Phúc Pet" — a clinic membership plan, not insurance)
brands_cited: Fubon (chip "fubonins" x3); Pet Health Centre (chip "pethealthcentre")
brands_recommended (rank): 1. Fubon Pet Insurance ("there's really only one true pet insurance product") — top pick differs from runs 1, 2, 3, 5 (all Liberty-first); Pet Health Centre named as a clinic-membership alternative, explicitly distinguished from real insurance ("closer to a loyalty plan than insurance"), not a competing recommendation.
sponsored_units: none observed
screenshot_ref: none
notes: research step "Searched the web, read memory, read a page" — third "read memory" instance. Gives explicit HCMC-specific tiered pricing (1.815M / 2.97M / 5.445M VND/year for basic/premium/elite) not seen in other runs. Rank-1 brand flips to Fubon here, in contrast to Liberty PetCare winning runs 1, 2, 3 and 5 — a genuine within-file split on this prompt (Liberty 4/5, Fubon 1/5).
answer_text_verbatim:
> Short version: in Vietnam there's really only one true pet insurance product, Fubon. Everything else is vet-clinic membership packages.
>
> Fubon Pet Insurance (HCMC-available)
>
> Dog premiums per year: 1,815,000 (basic), 2,970,000 (premium), 5,445,000 (elite) VND, VAT included. Cat is slightly cheaper.
>
> What you actually get on the basic plan: outpatient max 500k per visit and 1.5M per year, inpatient max 3M per visit and 3M per year, surgery max 6M per visit and 6M per year, all with a 10% deductible. Plus 300M liability cover if the dog hurts someone.
>
> Conditions that matter for a puppy: must be at least 2 months old, microchipped, and certain breeds are excluded (French Bulldog, Pit Bull, Tosa, Neapolitan, Dogo Argentino, Fila, Mastiff). Accidents covered from day 0, common illness after 30 days, hip dysplasia / patella / heart / cancer after 90 days. Anything pre-existing is excluded. Claims must be reported within 5 days and payout is within 15 days of a complete file.
>
> My honest read: the math is weak. Basic plan costs 1.8M to cap out at roughly 10.5M of medical cover. Premium plan costs 3M for a 25.5M cap. The elite plan (5.4M for 50M cap) is the only tier where one bad event, say a fracture surgery or a parvo ICU stay, clearly pays back the premium. The real hidden value is the 300M+ liability cover. Puppies bite and knock over motorbikes.
>
> The alternative most HCMC owners pick: self-insure. Put 300k VND a month in a separate account. After 12 months you have 3.6M, same as a basic payout cap, with no deductible, no exclusions, no claims paperwork. Clinic packages like Pet Health Centre's An Phúc Pet (from 2 months old, vaccinated) mostly bundle checkups and vaccine reminders plus surgery discounts, which is closer to a loyalty plan than insurance.
>
> If you do buy: buy in the first weeks after the 2-month mark, before any vet visit logs a condition. Chip first.
>
> One question that changes the answer: what breed? If it's a flat-faced or large breed, the exclusion list and the 90-day orthopedic wait matter a lot.

**Run 5** — `sample_id: claude-2026-09-22-HR-06-r5` — `chat_url: https://claude.ai/chat/ff09e3fd-c1ba-49b5-85e2-c3aa9c5b7ea7` — `timestamp_utc: 2026-09-22T09:20:38Z`
brands_mentioned (order): Liberty (PetCare), INSO, Fubon
brands_cited: Fubon (chip "fubonins")
brands_recommended (rank): 1. Liberty PetCare ("if you want real coverage")  2. INSO ("if you want cheap")  3. Fubon ("Also worth a look")
sponsored_units: none observed
screenshot_ref: none
notes: —
answer_text_verbatim:
> Assuming you're buying in Vietnam. The market is thin, so it comes down to two picks:
>
> Liberty PetCare if you want real coverage. Ages 2 months to 9 years, accidents covered immediately, illness after 30 days, up to 100 million VND per year with 20% copay, from about 1.5 million VND per year. Every other local plan caps at 8 to 20 million, which one surgery can blow through. The 100M cap is the only one that actually functions as insurance.
>
> INSO if you want cheap. From about 300k VND per year, 20 million cap, plus theft and third-party liability, quick online signup. Fine for a street-mix puppy with low genetic risk.
>
> Also worth a look: Fubon, which covers medical costs, liability, lost-pet ads, and funeral costs, but requires a microchip and excludes French Bulldog, Pit Bull, Mastiff and a few other breeds.
>
> Things that matter for a puppy specifically:
> - Buy now. Under 1 year is the golden window: cheaper premiums and no pre-existing conditions yet, which is the most common exclusion.
> - Vaccines, neutering, and routine checkups are not covered by any of them. Budget those separately.
> - Claims are reimbursement: you pay the vet first, then submit paperwork and wait 7 to 15 working days. Keep every receipt from day one.
>
> What breed? That changes the answer. High-risk breeds (Golden, Bulldog, Corgi backs) push toward Liberty. A mutt makes INSO plus a 500k/month emergency fund the smarter play.

#### HR-09 — C — "best creatine supplement" — achieved_n: 5/5

Common to all 5 runs: `region_intended: US`, `region_observed: Vietnam context ("easy to find in Vietnam", "Local note: in Vietnam...", Shopee/Lazada references in 4 of 5 runs; one run (r3) gave no locale cue)`, `login_state: logged-in (researcher-owned)`, `search_toggle: on`, `arm: main`, `model_version_shown: Fable 5.1 (effort: High)`, `answer_outcome: answered`, `prompt_kind: C`, `slot_fill: n/a`. Weekly-limit banner still at 75%. **Category consensus is on the ingredient (creatine monohydrate) not one bottled brand** — every run agrees monohydrate beats HCl/buffered/gummy forms, then names 2-4 co-equal retail brands rather than a single winner, a different pattern from the single-winner prompts elsewhere in this file. **Optimum Nutrition Micronized Creatine** is the one product named in all 5 runs (sometimes as the sole pick, sometimes among 2-3 named as equally fine).

**Run 1** — `sample_id: claude-2026-09-22-HR-09-r1` — `chat_url: https://claude.ai/chat/33755825-e01b-4479-9610-18538c47dbfe` — `timestamp_utc: 2026-09-22T09:22:20Z`
brands_mentioned (order): California Gold Nutrition (Sport Pure Creatine Monohydrate), Optimum Nutrition (Micronized Creatine)
brands_cited: none observed (chips "smartshopii", "ultimatesupsg", "probuilder.co" — third-party)
brands_recommended (rank): 1. California Gold Nutrition Sport Pure Creatine Monohydrate (named "a top creatine pick for 2026 by ExpertConsumers.org")  2. Optimum Nutrition Micronized Creatine (offered as the "buy locally" equivalent)
sponsored_units: one product card (no image described, direct text card) for California Gold Nutrition; no ad/sponsored label text.
screenshot_ref: none
notes: cites a named third-party ranking site by name in prose ("ExpertConsumers.org") without a live link.
answer_text_verbatim:
> Daily intake: 3 to 5 g every day, no loading needed.
>
> California Gold Nutrition Sport Pure Creatine Monohydrate — Single ingredient, 5 g per scoop, cheap per serving, and easy to get in Vietnam through iHerb. Named a top creatine pick for 2026 by ExpertConsumers.org on the strength of manufacturing transparency and controlled distribution. Trade-off: unflavored and a bit gritty. Mix in warm water or a shake and it's fine. If you'd rather buy locally, Optimum Nutrition Micronized Creatine is the widely stocked equivalent at Vietnamese supplement shops.
>
> Daily intake: 3 to 5 g every day, no loading needed. Takes 3 to 4 weeks to saturate. Drink an extra 500 ml water. Skip anything with a "proprietary blend" on the label.

**Run 2** — `sample_id: claude-2026-09-22-HR-09-r2` — `chat_url: https://claude.ai/chat/65e74666-c898-45be-b259-309730246a21` — `timestamp_utc: 2026-09-22T09:23:17Z`
brands_mentioned (order): Optimum Nutrition (Micronized Creatine), MyProtein (Creatine Monohydrate), NOW Sports (Creatine)
brands_cited: none observed
brands_recommended (rank): 1. Optimum Nutrition Micronized Creatine, MyProtein Creatine Monohydrate, NOW Sports Creatine — offered as three co-equal options ("Any of these is fine"), no single winner
sponsored_units: none observed
screenshot_ref: none
notes: explicitly frames the category as commodity — "Skip the 'best brand' question."
answer_text_verbatim:
> Skip the "best brand" question. Buy plain creatine monohydrate, ideally Creapure-sourced (German-made raw material, tested for purity). Everything else (HCl, buffered, gummies) costs more and works no better.
>
> Solid options easy to find in Vietnam via Shopee or supplement shops: Optimum Nutrition Micronized Creatine, MyProtein Creatine Monohydrate, or NOW Sports Creatine. Any of these is fine. Powder beats capsules on price.
>
> Dose: 3 to 5 g per day, every day, no loading needed. Mix in water or anything. Timing doesn't matter. Drink a bit more water than usual. Effects show after 3 to 4 weeks of consistent use.
>
> One thing to check when buying: the label should say "creatine monohydrate" as the only ingredient. No proprietary blends.

**Run 3** — `sample_id: claude-2026-09-22-HR-09-r3` — `chat_url: https://claude.ai/chat/1f2d17b2-2112-4aac-8d09-5602ee75b38a` — `timestamp_utc: 2026-09-22T09:24:18Z`
brands_mentioned: none — this run names no product brand at all, only the ingredient and certification standards (Creapure, Informed Sport, NSF)
brands_cited: none observed
brands_recommended: none — the only HR-09 run with zero brand names; recommends buying "any store brand that lists Creapure on the label," explicitly brand-agnostic
sponsored_units: none observed
screenshot_ref: none
notes: no Vietnam/locale cue this run (references Shopee/iHerb generically without naming Vietnam specifically) — the "in Vietnam" phrase appears in runs 1,2,4,5 but not verbatim in this run's text (it says "on Shopee/iHerb" without "in Vietnam").
answer_text_verbatim:
> Creatine monohydrate. Nothing else is worth paying for.
>
> Buy the plainest version: micronized creatine monohydrate powder, unflavored, ideally Creapure-sourced or third-party tested (Informed Sport / NSF). Skip HCl, buffered, "kre-alkalyn" and gummies. They cost more, have weaker evidence, and gummies in particular have tested badly underdosed.
>
> Solid picks that show up on Shopee/iHerb in Vietnam: Optimum Nutrition Micronized Creatine, MyProtein Creatine Monohydrate, Nutricost, or any store brand that lists Creapure on the label. Pick by price per gram, they are all the same molecule.
>
> Dose: 3 to 5 g per day, every day, timing does not matter. Loading (20 g/day split over 5 to 7 days) just gets you saturated a week sooner. Drink normal water, expect roughly 1 kg of water weight in the first weeks, that is muscle water, not fat.

Note: run 3's text does name Optimum Nutrition, MyProtein, and Nutricost in its second paragraph — correcting the "brands_mentioned: none" line above, which was written from an earlier partial read. Corrected: brands_mentioned (order): Optimum Nutrition (Micronized Creatine), MyProtein (Creatine Monohydrate), Nutricost. brands_recommended: all three offered as co-equal options ("Pick by price per gram, they are all the same molecule") — no single winner, consistent with run 2's pattern.

**Run 4** — `sample_id: claude-2026-09-22-HR-09-r4` — `chat_url: https://claude.ai/chat/96ae7699-875a-4988-935d-d923c450c5dd` — `timestamp_utc: 2026-09-22T09:25:17Z`
brands_mentioned (order): Optimum Nutrition (Micronized Creatine Monohydrate), Thorne, Momentous, Nutricost, BulkSupplements
brands_cited: none observed (chips "brandclub", "walmart", "bodycreate" on the product card; "ringly" separately)
brands_recommended (rank): 1. Optimum Nutrition Micronized Creatine Monohydrate ("the pick for most people")  2. Thorne / Momentous (conditional, purity-certification step-up)  3. Nutricost / BulkSupplements (conditional, cheapest per gram)
sponsored_units: one product card (Optimum Nutrition), chips "brandclub"/"walmart"/"bodycreate", no ad/sponsored label text.
screenshot_ref: none
notes: explicit "Local note: in Vietnam, ON and Nutricost are easy to find on Shopee or Lazada. Check the seal and expiry, fakes exist." — a counterfeit-goods warning not seen in other runs.
answer_text_verbatim:
> Micronized monohydrate at 3 to 5 grams a day is the whole recipe.
>
> Optimum Nutrition Micronized Creatine Monohydrate — Plain 5 g monohydrate per scoop, micronized so it mixes clean, banned-substance tested, and cheap per serving. It's the pick for most people simply because it's the same molecule as the premium stuff at a fraction of the price and it's available almost everywhere. If you want a step up: Thorne (NSF Certified for Sport) or Momentous (Creapure) buy you purity certification, not better results. Nutricost or BulkSupplements if you want the cheapest possible per gram.
>
> Micronized monohydrate at 3 to 5 grams a day is the whole recipe. No loading phase needed. Take it daily, timing doesn't matter, drink a bit more water.
>
> Local note: in Vietnam, ON and Nutricost are easy to find on Shopee or Lazada. Check the seal and expiry, fakes exist.

**Run 5** — `sample_id: claude-2026-09-22-HR-09-r5` — `chat_url: https://claude.ai/chat/c28c353b-2b4e-4767-a517-9cdbba3d6015` — `timestamp_utc: 2026-09-22T09:26:15Z`
brands_mentioned (order): Optimum Nutrition (Micronized Creatine), MyProtein (Creatine Monohydrate)
brands_cited: none observed
brands_recommended (rank): 1. Optimum Nutrition Micronized Creatine and MyProtein Creatine Monohydrate offered as co-equal ("are cheap, widely available in Vietnam, and fine") — no single winner
sponsored_units: none observed
screenshot_ref: none
notes: research-step caption in Vietnamese: "Đề xuất loại creatine phù hợp và dễ tìm" ("Suggest a suitable and easy-to-find creatine type") — fifth Vietnamese-language caption in this file.
answer_text_verbatim:
> Creatine monohydrate. Nothing else beats it, and the fancy forms (HCl, buffered, nitrate) cost more for no extra benefit.
>
> What to buy:
> - Plain creatine monohydrate powder, micronized if you want it to mix easier
> - Look for Creapure on the label (German-made, purity tested). Optimum Nutrition Micronized Creatine and MyProtein Creatine Monohydrate are cheap, widely available in Vietnam, and fine
> - Skip blends with added stuff. Unflavored, one ingredient
>
> Dose: 3 to 5 g daily, every day, timing doesn't matter. No loading phase needed. Expect 1 to 2 kg of water weight in the first weeks. Drink a bit more water.
>
> Check the seller is legit (official store on Shopee/Lazada or a known gym supplement shop). Fakes are the real risk here, not the brand.

#### HR-10 — C — "best magnesium supplement for sleep" — achieved_n: 5/5 (0 of 5 named a product brand)

**Distinct behavior for this prompt**: none of the 5 runs performed a web search (no "Searched the web" step in any run, unlike every other C prompt in this file) and none named a single manufacturer/product brand. Every run converged on the same formulation-level answer — magnesium glycinate (bisglycinate) — with near-identical dosing guidance (200-400 mg elemental, 1-2 hours before bed, RDA ~400-420 mg/day, supplement cap ~350 mg/day) and the same three forms dismissed (threonate: pricey/thin evidence; citrate: loosens stools; oxide: poorly absorbed). This reads as the model answering from its own training knowledge rather than retrieved content — consistent with a question where ingredient-level guidance is stable and well-established, unlike the fast-changing bank/card-rate prompts elsewhere in this file. Run 5 addressed the user as "men your age," a further personalization signal (age/demographic, not just location) beyond what any other run in this file showed explicitly. `region_intended: US`, `region_observed: none — no locale cue in any of the 5 runs (first HR-vertical C prompt with no Vietnam framing at all)`, `login_state: logged-in (researcher-owned)`, `search_toggle: on (default, though unused this prompt)`, `arm: main`, `model_version_shown: Fable 5.1 (effort: High)`, `answer_outcome: answered`, `prompt_kind: C`, `slot_fill: n/a`, `brands_mentioned: none`, `brands_cited: none observed`, `brands_recommended: none`, `sponsored_units: none observed`, `screenshot_ref: none` — common to all 5 runs. Weekly-limit banner still at 75%.

**Run 1** — `sample_id: claude-2026-09-22-HR-10-r1` — `chat_url: https://claude.ai/chat/a85c7b8b-7b10-4399-8b32-237baa730508` — `timestamp_utc: 2026-09-22T09:27:50Z`
answer_text_verbatim:
> Magnesium glycinate (bisglycinate). Well absorbed, gentle on the stomach, and glycine itself has a mild calming effect. That's the standard pick.
>
> Other forms, briefly:
> - Threonate: marketed for brain uptake. Pricier, sleep evidence is thin. Not worth the premium.
> - Citrate: absorbs fine but pulls water into the gut. Loose stools at higher doses.
> - Oxide: cheap and poorly absorbed. Skip.
>
> Dose: 200 to 400 mg elemental magnesium, 1 to 2 hours before bed. Check the label says "elemental" or "as magnesium", since a 1000 mg glycinate capsule is often only ~100 to 140 mg elemental.
>
> Daily intake: RDA for adult men is 400 to 420 mg total from food plus supplements. NIH upper limit for supplemental magnesium alone is 350 mg per day. Above that you mostly get diarrhea, not better sleep.
>
> One honest caveat. The sleep evidence is modest. It helps most if you're actually low (common with a high-sweat, low-leafy-greens diet). If two weeks at 300 mg does nothing, it's probably not your lever.

**Run 2** — `sample_id: claude-2026-09-22-HR-10-r2` — `chat_url: https://claude.ai/chat/fb463d68-539d-41f1-865f-b3c3d64c0328` — `timestamp_utc: 2026-09-22T09:28:49Z`
answer_text_verbatim:
> Magnesium glycinate (bisglycinate). Well absorbed, gentle on the stomach, and glycine itself has a mild calming effect. It's the one with the most consistent anecdotal and small-trial support for sleep.
>
> Dose: 200 to 400 mg elemental magnesium, taken 1 to 2 hours before bed. Start at 200 mg and see how you feel after a week.
>
> Daily intake: RDA for men is 400 to 420 mg total from food plus supplements. The supplement-only upper limit is 350 mg/day, mostly to avoid loose stools. Dark leafy greens, pumpkin seeds, nuts, and legumes cover a lot of the food side.
>
> Skip magnesium oxide (poorly absorbed, mostly a laxative) and citrate (fine for absorption, but loosens stools). L-threonate gets hyped for brain penetration, but it's pricey and the sleep evidence is thinner than the marketing.
>
> Honest caveat: magnesium helps most if you're actually low on it. If your diet is decent and sleep is still bad, it'll be a small nudge, not a fix. Worth a 2 to 3 week trial anyway. Cheap, low risk.

**Run 3** — `sample_id: claude-2026-09-22-HR-10-r3` — `chat_url: https://claude.ai/chat/50f16dbb-d826-4293-a8ab-2e9f96725d22` — `timestamp_utc: 2026-09-22T09:29:47Z`
answer_text_verbatim:
> Magnesium glycinate (bisglycinate). Best absorbed, gentle on the gut, glycine itself is mildly calming. That's the sleep pick.
>
> Others, quickly:
> - Threonate: marketed for brain/sleep, expensive, weak evidence. Skip unless you have money to burn.
> - Citrate: absorbs well but loosens stools. Fine if you're also constipated.
> - Oxide: cheap, poorly absorbed, mostly a laxative. Avoid.
>
> Dose: 200 to 400 mg elemental magnesium, 30 to 60 min before bed. Check the label says "elemental", not total compound weight. Start at 200 mg for a week, see how your gut handles it.
>
> Daily intake: RDA for men: ~400 to 420 mg/day total, food included. Supplement cap: ~350 mg/day from pills alone. Above that, diarrhoea is common. Food covers a lot: pumpkin seeds (~150 mg per 30 g dry), spinach, black beans, dark chocolate.
>
> Honest expectation: helps most if you're actually low (poor diet, heavy sweating, alcohol, stress). If your levels are fine, the effect is small. Give it 2 to 3 weeks before judging. If sleep is still bad after that, magnesium isn't the bottleneck.

**Run 4** — `sample_id: claude-2026-09-22-HR-10-r4` — `chat_url: https://claude.ai/chat/64cf238f-609b-4f1d-bfc9-c600735699f3` — `timestamp_utc: 2026-09-22T09:31:20Z`
answer_text_verbatim:
> Magnesium glycinate (also sold as bisglycinate). That's the pick.
>
> Why: glycine itself has mild sleep benefits, absorption is good, and it doesn't hit your gut the way citrate or oxide do. Oxide is the cheap one in most pharmacy bottles and barely absorbs. Threonate gets hyped for brain uptake but costs 3x and the sleep evidence is thinner.
>
> Dose: 200 to 300 mg elemental magnesium, 1 to 2 hours before bed. Check the label for "elemental" rather than total compound weight. Total daily intake target for adult men is around 400 to 420 mg from food plus supplements, and the upper limit from supplements alone is 350 mg.
>
> Give it two to three weeks before judging. Effect is modest, mostly better sleep depth and fewer wake-ups, not a knockout. If you're on any regular medication, worth a quick check with a pharmacist since magnesium can interfere with absorption of some drugs.

**Run 5** — `sample_id: claude-2026-09-22-HR-10-r5` — `chat_url: https://claude.ai/chat/da6c1208-732f-4046-a276-523bdeb011ec` — `timestamp_utc: 2026-09-22T09:32:23Z`
notes: addresses the user directly as "men your age" — an explicit age/demographic personalization cue, distinct from the location and occupation cues seen elsewhere in this file.
answer_text_verbatim:
> Magnesium glycinate (bisglycinate). That's the one.
>
> Why: absorbs well, doesn't hit your gut like citrate or oxide, and the glycine part is mildly calming on its own. Threonate gets hyped for brain stuff but costs 3x and the sleep evidence isn't better. Oxide is cheap and mostly passes straight through you.
>
> How to take it:
> - 200 to 300 mg elemental magnesium, 30 to 60 min before bed
> - Read the label carefully. "Magnesium bisglycinate 1000 mg" often means only ~100 to 200 mg elemental. The elemental number is what counts.
> - Give it 2 to 3 weeks before judging
>
> Daily intake: men your age need about 400 mg total per day from food plus supplements. Upper limit from supplements alone is 350 mg. Above that you get loose stools, not better sleep.
>
> Honest expectation: it helps most if you're actually low on magnesium. If your sleep problem is stress or screens, it'll take the edge off but won't fix it.

### Toggle arm — one run per vertical, search toggle flipped off

Per protocol: "Once per engine per sample date, re-run the vertical's first C prompt with the toggle flipped." Default state confirmed via the "+" tools menu before this file's first run: `Web search` checked (on). For this arm, `Web search` was unchecked via the same menu (confirmed by screenshot before and after each toggle action), one run of each vertical's first C prompt (SK-01, BS-01, HR-01) was sent, then `Web search` was re-checked (restored to on) at `2026-09-22T09:35:xxZ`, confirmed by a final menu screenshot showing both `Web search` and `Memory` checked. These 3 runs are excluded from the main-arm rate series per protocol (`arm: toggle-flipped`) and use `run_index: 1` conceptually (a single flipped-toggle observation, not part of the n=5 count for that prompt). `region_intended: US`, `login_state: logged-in (researcher-owned)`, `model_version_shown: Fable 5.1 (effort: High)`, `answer_outcome: answered` common to all three.

**SK-01 toggle-flipped** — `sample_id: claude-2026-09-22-SK-01-toggle` — `chat_url: https://claude.ai/chat/75965719-55cb-4aef-9b22-9166bf3c81dc` — `timestamp_utc: 2026-09-22T09:34:06Z` — `search_toggle: off` — `region_observed: Vietnam ("sold almost everywhere in Vietnam", "Saigon humidity")`
brands_mentioned (order): CeraVe (Moisturizing Cream), La Roche-Posay (Toleriane Sensitive)
brands_cited: none observed
brands_recommended (rank): 1. CeraVe Moisturizing Cream  2. La Roche-Posay Toleriane Sensitive (runner-up)
sponsored_units: none observed — no product-image card this run (consistent with no web search: the card feature seen in main-arm SK-01 runs 2/3/4/5 required search)
screenshot_ref: none
notes: still showed a 4x-repeated collapsed reasoning caption ("Finding the best moisturizer for dry sensitive skin") despite search being off — the surface's internal reasoning step ran regardless of the toggle state, only the external web-fetch was suppressed. No "Searched the web" label appeared. Footer read "double-check responses" (not "cited sources"), consistent with no search performed. Top brand (CeraVe) matches 4 of 5 main-arm runs.
answer_text_verbatim:
> CeraVe Moisturizing Cream — Fragrance free, no alcohol, no essential oils. Ceramides and hyaluronic acid repair the barrier instead of just sitting on top. Cheap, sold almost everywhere in Vietnam, and rarely stings on reactive skin. Trade-off: it is thick. In Saigon humidity use a thin layer at night and switch to the lotion version for daytime if it feels greasy.
>
> Runner-up if CeraVe breaks you out: La Roche-Posay Toleriane Sensitive. Lighter, same no-fragrance rule.
>
> Apply on damp skin within a minute of washing. That one habit matters more than the brand.

**BS-01 toggle-flipped** — `sample_id: claude-2026-09-22-BS-01-toggle` — `chat_url: https://claude.ai/chat/4b50b557-5cd1-4239-bfba-e3006f0a7a9f` — `timestamp_utc: 2026-09-22T09:35:16Z` — `search_toggle: off` — `region_observed: none — USD-context, no locale cues (matches main-arm pattern for this vertical)`
brands_mentioned (order): Zendesk (Suite), Freshdesk, Help Scout, HubSpot (Service Hub), Intercom
brands_recommended (rank): 1. Zendesk Suite ("the safe default")  2. Freshdesk ("the same thing cheaper")  3. Help Scout (conditional, B2B/email-first)  4. HubSpot Service Hub (conditional, existing HubSpot CRM)  5. Intercom (conditional, chat-first SaaS)
sponsored_units: none observed
brands_cited: none observed
screenshot_ref: none
notes: top-2 brands (Zendesk, Freshdesk) match the main-arm BS-01 pattern exactly (Zendesk rank-1 in 4 of 5 main-arm runs, Freshdesk consistently rank-2) — toggle-off did not change the category consensus for this prompt.
answer_text_verbatim:
> For 50 agents you're in the mid-market sweet spot. My pick: Zendesk Suite if you want the safe default, Freshdesk if you want the same thing cheaper.
>
> The short version:
> - Zendesk Suite (Team/Professional): most mature, best integrations and reporting, strongest automation. Priciest, and the upsells add up.
> - Freshdesk (Pro): 70-80% of Zendesk at maybe half the cost. Good enough for most teams. Reporting is weaker.
> - Help Scout: nicest agent experience, feels like shared email. Great if you're mostly B2B and don't need heavy workflows. Starts to strain past ~30 agents with complex routing.
> - HubSpot Service Hub: only if you're already on HubSpot CRM. Otherwise skip.
> - Intercom: pick this if support is chat-first and you sell SaaS. Expensive at 50 seats.
>
> Deciding questions: email/tickets vs live chat heavy? Any phone support? Need SLAs and multi-brand? Budget per seat? If you answer those I can narrow to one.

**HR-01 toggle-flipped** — `sample_id: claude-2026-09-22-HR-01-toggle` — `chat_url: https://claude.ai/chat/8df28289-48fb-4117-a1db-d848ac46f4a1` — `timestamp_utc: 2026-09-22T09:36:24Z` — `search_toggle: off` — `region_observed: Vietnam (implicit throughout: Vietcombank, Techcombank, HSBC, VIB named as Vietnamese cards)`
brands_mentioned (order): Vietcombank, Techcombank (Vietnam Airlines co-brand cards), HSBC (Live+, TravelOne), VIB (Cash Back)
brands_cited: none observed
brands_recommended (rank): 1. "a no-fee cashback card with a low foreign transaction fee (HSBC Live+ or VIB Cash Back type)" — generic category pick, two brands offered as equivalent examples  2. HSBC TravelOne (conditional, "If you still want a travel card"). Vietcombank/Techcombank Vietnam Airlines co-brand cards named only as the poor-value baseline.
sponsored_units: none observed
screenshot_ref: none
notes: **the clearest direct evidence in this file that the surface knows and discloses its own search-toggle state to the user** — the answer ends with a distinct UI element: "Web search is off / Turn it on so Claude can check current sources for this. [Turn on web search]" — a persistent banner, not just prose. The answer itself also self-qualifies: "Card terms in Vietnam shift often and I can't verify current fees or earn rates from here, so it's worth a quick check with web search on before you apply." No product card, no citation chips (consistent with search off). Top pick (HSBC-family cashback, then HSBC TravelOne) does not overlap with any single main-arm HR-01 top pick (VIB Travel Élite won 3 of 5 main-arm runs) — the only toggle-arm run in this file where the toggle-off answer's top brand differs from the main-arm consensus.
answer_text_verbatim:
> Flying twice a year, a miles card usually loses. Miles pile up slowly at normal spend, the annual fee eats most of the value, and airline co-brands (the Vietcombank or Techcombank Vietnam Airlines cards) only pay off if you push a lot of spend through them and fly that one carrier.
>
> My position: skip the travel card. Get a no-fee cashback card with a low foreign transaction fee (HSBC Live+ or VIB Cash Back type) and pay for flights in cash. You come out ahead and nothing expires.
>
> If you still want a travel card, HSBC TravelOne is the one I'd consider. Points transfer to several airline and hotel programs, so you're not locked into one carrier, and the fee gets waived past a spend threshold.
>
> Card terms in Vietnam shift often and I can't verify current fees or earn rates from here, so it's worth a quick check with web search on before you apply.
>
> [UI element: "Web search is off — Turn it on so Claude can check current sources for this." — button: "Turn on web search"]

Web search was re-enabled immediately after this run (confirmed via the "+" tools menu: both `Web search` and `Memory` checked as of `2026-09-22T09:36Z`), restoring the account to the state observed at the start of this file's sampling.

## P prompts — problem-shaped

Per protocol priority (C first, achieved above; then P; then X), sampling continued into P prompts with remaining session budget. `search_toggle: on` (restored default) for all P runs below.

### Vertical: Skincare and beauty — P prompts

#### SK-08 — P — "what should I use for hormonal acne on my chin?" — achieved_n: 5/5

Common to all 5 runs: `region_intended: US`, `region_observed: Vietnam (HCMC named in runs 1, 3; Vietnamese generic brand named in run 4)`, `login_state: logged-in (researcher-owned)`, `search_toggle: on`, `arm: main`, `model_version_shown: Fable 5.1 (effort: High)`, `answer_outcome: answered`, `prompt_kind: P`, `slot_fill: n/a`. Weekly-limit banner still at 75%. **New personalization dimension**: every one of the 5 runs assumed the user is male ("for a guy", "for a man", "on a man's chin", "for men") despite the prompt containing no gender indicator — a fourth personalization axis in this file (after location, occupation, and age), and the most consistent one observed (5/5 vs. partial signals elsewhere). All 5 runs converge on **adapalene 0.1% gel (Differin)** as the first-line recommendation — the most unanimous single-product consensus of any prompt in this file so far, C or P.

**Run 1** — `sample_id: claude-2026-09-22-SK-08-r1` — `chat_url: https://claude.ai/chat/13ec516e-1e53-4c91-8602-e5bd5e8ef426` — `timestamp_utc: 2026-09-22T09:38:45Z`
brands_mentioned (order): Differin (adapalene 0.1%, generic-name led)
brands_recommended (rank): 1. Adapalene 0.1% / Differin. Other steps (benzoyl peroxide, azelaic acid) are generic actives, not manufacturer brands.
brands_cited: none observed
sponsored_units: none observed
screenshot_ref: none
notes: structured as a numbered treatment ladder (adapalene → benzoyl peroxide → azelaic acid → dermatologist); explicit gender assumption ("for a guy") in the opening line; includes a medical disclaimer banner ("This is general information, not medical advice").
answer_text_verbatim:
> Short version: for a guy, "hormonal" chin acne usually means androgen-driven, so the female-specific fixes (spironolactone, the pill) don't apply. What works is a good topical routine, then a dermatologist if that fails after 8 to 12 weeks.
>
> Adapalene 0.1% at night — First-line retinoid. Sold OTC in Vietnam as Differin or generic. Works on the clog stage, so it prevents new spots rather than shrinking current ones. Pea-sized amount, whole chin, not spot treatment. Start 3 nights a week, build to nightly over a month. Expect a purge in weeks 2 to 6, judge results at week 12.
>
> Benzoyl peroxide 2.5% in the morning — Kills the bacteria behind red, inflamed bumps. Pairs well with adapalene. Higher percentages don't work better, just irritate more. Wash-off or leave-on, 2.5% only. Bleaches towels and pillowcases, use white ones. Skip if skin gets raw, add back slowly.
>
> Azelaic acid 15 to 20% — Gentler option if the above stings too much. Also fades the dark marks acne leaves on Asian skin. Twice daily, can replace BPO. Tingling for the first week is normal. Slower than adapalene, give it 3 months.
>
> Dermatologist for oral treatment — If it's deep, painful cysts or nothing topical moves it by month 3. Vietnam derm visits are cheap and same-week. Ask about a short doxycycline course. Isotretinoin if it scars or keeps coming back. Bring a photo log so they see the pattern.
>
> One thing today: buy adapalene. Two lifestyle levers worth a two-week test alongside it: cut whey protein and milk if you use them, and change your pillowcase every 2 to 3 days. Both have decent evidence for chin and jaw breakouts specifically.
>
> Is it mostly small clogged bumps, or deep painful ones? That changes whether the derm route should come first.

**Run 2** — `sample_id: claude-2026-09-22-SK-08-r2` — `chat_url: https://claude.ai/chat/398e321c-08de-4ce7-bdd7-ee21ff948be4` — `timestamp_utc: 2026-09-22T09:39:48Z`
brands_mentioned (order): Differin (adapalene 0.1%)
brands_recommended (rank): 1. Differin (adapalene 0.1%)
brands_cited: none observed
sponsored_units: none observed
screenshot_ref: none
notes: most explicit gender framing of the 5 runs — "For a man, 'hormonal' chin acne is usually less about hormones and more about the beard area" — and explicitly tells the user spironolactone "won't be prescribed to you," directly gendering the medical advice.
answer_text_verbatim:
> For a man, "hormonal" chin acne is usually less about hormones and more about the beard area: shaving irritation, ingrown hairs, or plain adult acne that just clusters there. Treatment is the same either way.
>
> Start with one thing: adapalene 0.1% gel (Differin) at night on the whole chin, not spot-treated. It's over the counter, it's the first-line pick for adult acne, and it takes 8 to 12 weeks to show results, so don't judge it early. Expect some dryness the first two weeks. Pair it with a plain non-foaming cleanser and a basic moisturiser.
>
> If it's more red bumps than blackheads, add benzoyl peroxide 2.5% in the morning. If you shave: sharp single blade, with the grain, and shave after washing, not before.
>
> Skip spironolactone or anything else marketed as "hormonal" acne treatment. Those are for women and won't be prescribed to you.
>
> If it's cystic (deep, painful, leaves marks) or three months of adapalene does nothing, see a dermatologist. That's the point where prescription options make sense and I'm not the right source for those.
>
> Is it mostly whiteheads and blackheads, or the painful under-the-skin kind?

**Run 3** — `sample_id: claude-2026-09-22-SK-08-r3` — `chat_url: https://claude.ai/chat/fd07ea6a-17cb-4356-8845-beae9bd804e7` — `timestamp_utc: 2026-09-22T09:40:48Z`
brands_mentioned (order): none by manufacturer name — this run uses only the generic "adapalene 0.1% gel" and "benzoyl peroxide 2.5%," no brand name printed
brands_recommended (rank): 1. Adapalene 0.1% gel (generic-only)
brands_cited: none observed
sponsored_units: none observed
screenshot_ref: none
notes: "sold at any pharmacy in HCMC" — explicit city reference; "A lot of 'hormonal' chin acne in men is really razor irritation" — gender assumption again.
answer_text_verbatim:
> Start with adapalene 0.1% gel at night. It's the strongest thing you can get without a prescription and it's the standard first move for stubborn chin breakouts. Pea-sized amount over the whole chin, not just spots. Expect 8 to 12 weeks before it looks better. Early weeks can get worse first. That's normal.
>
> Add benzoyl peroxide 2.5% in the morning if the spots are red and inflamed. Cheap, sold at any pharmacy in HCMC.
>
> Two things that matter alongside:
> - Moisturizer and sunscreen daily. Adapalene dries you out and sun makes marks last longer.
> - If you shave that area, a clean single blade and shave with the grain. A lot of "hormonal" chin acne in men is really razor irritation and ingrown hairs.
>
> If 3 months of this does nothing, or you're getting deep painful cysts, see a derm. That's when oral options come in. Not worth guessing at those yourself.
>
> One question: are these small red bumps or deep sore lumps under the skin? Changes what I'd push harder on.

**Run 4** — `sample_id: claude-2026-09-22-SK-08-r4` — `chat_url: https://claude.ai/chat/4f8fad42-2903-4fad-85fe-f4df50c7c6ac` — `timestamp_utc: 2026-09-22T09:41:48Z`
brands_mentioned (order): Differin (adapalene), Klenzit-C ("Vietnamese generic"), Winlevi (clascoterone, prescription-only mention)
brands_recommended (rank): 1. Differin / Klenzit-C (adapalene 0.1%, offered as equivalent OTC options). Winlevi named only as a prescription-route option for a dermatologist to consider, not a self-directed recommendation.
brands_cited: none observed
sponsored_units: none observed
screenshot_ref: none
notes: names a specific Vietnamese generic brand (Klenzit-C) not seen in any other run in this file; distinguishes "beard folliculitis" from acne, a diagnostic nuance not raised elsewhere; explicitly states spironolactone "is not used in men."
answer_text_verbatim:
> Start with adapalene 0.1% gel (Differin, or Vietnamese generics like Klenzit-C). Pea-sized amount on the whole chin at night, not just spots. Give it 8 to 12 weeks. Expect some dryness and a possible flare in weeks 2 to 4. That's normal, keep going.
>
> Pair it with a benzoyl peroxide 2.5% wash in the morning. Moisturize, use sunscreen. Skip harsh scrubs.
>
> Two things worth checking on a man's chin. Shaving irritation or beard folliculitis looks like acne but isn't. If bumps track your shave line, change razor habits first. And if it's deep, painful cysts rather than surface pimples, OTC won't cut it. See a dermatologist. For men the prescription route is topical clascoterone (Winlevi), short-course antibiotics, or isotretinoin if severe. Spironolactone is the usual "hormonal acne" drug but it's not used in men.
>
> One thing today: buy adapalene, start tonight.

**Run 5** — `sample_id: claude-2026-09-22-SK-08-r5` — `chat_url: https://claude.ai/chat/4e8f74dd-becc-499b-9ba6-63b619b32bc2` — `timestamp_utc: 2026-09-22T09:42:49Z`
brands_mentioned (order): Differin (adapalene 0.1%)
brands_recommended (rank): 1. Differin (adapalene 0.1%)
brands_cited: none observed
sponsored_units: none observed
screenshot_ref: none
notes: "For men the next steps are usually oral doxycycline or low-dose isotretinoin" — gender framing again, fifth of five runs.
answer_text_verbatim:
> Start with adapalene 0.1% gel (Differin). It's the OTC gold standard for hormonal chin and jaw acne. Pea-sized amount on the whole chin at night, not just spots. Takes 8 to 12 weeks, and it often gets worse around week 3 before it gets better. Stick with it.
>
> Pair it with benzoyl peroxide 2.5% in the morning if you get red inflamed bumps. Use a bland moisturizer and sunscreen, or the adapalene will wreck your skin barrier.
>
> Skip the harsh scrubs and drying toners. They make hormonal acne worse.
>
> If it's deep painful cysts, or three months of adapalene does nothing, see a dermatologist. For men the next steps are usually oral doxycycline or low-dose isotretinoin, and those need a prescription and monitoring. Not a doctor, but that's the standard ladder.
>
> One thing today: buy the adapalene.

#### SK-09 — P — "my skin barrier is damaged from over-exfoliating — what should I use?" — achieved_n: 5/5

**Mechanical deviation**: the prompt's em-dash ("—") could not be typed reliably by the browser extension's `type` action (produced a stray "—" character alone with no following text on first attempt). Retyped using a standard ASCII hyphen ("-") in its place; wording otherwise verbatim. Recorded here per the file-header instruction to log deviations rather than edit the protocol.

Common to all 5 runs: `region_intended: US`, `region_observed: none — no Vietnam/HCMC cue in any of the 5 runs (unusual for this file; possibly because the prompt itself carries no purchase-market signal)`, `login_state: logged-in (researcher-owned)`, `search_toggle: on`, `arm: main`, `model_version_shown: Fable 5.1 (effort: High)`, `answer_outcome: answered`, `prompt_kind: P`, `slot_fill: n/a`, no web search performed in any run (no "Searched the web" step), footer read "double-check responses" throughout. **CeraVe (Moisturizing Cream and/or Hydrating Cleanser) appears in all 5 runs** and **La Roche-Posay (Toleriane cleanser and/or Cicaplast Baume B5) in 4 of 5** — the strongest two-brand pairing seen in this file. `brands_cited: none observed` in any run (no product-card/citation UI, consistent with no search).

**Run 1** — `sample_id: claude-2026-09-22-SK-09-r1` — `chat_url: https://claude.ai/chat/e157d1bd-8a77-4ddc-9335-b21d64799a20` — `timestamp_utc: 2026-09-22T09:44:43Z`
brands_mentioned (order): CeraVe (Hydrating Cleanser, Moisturizing Cream), La Roche-Posay (Toleriane Dermo-Cleanser, Cicaplast Baume B5)
brands_recommended (rank): 1. CeraVe (cleanser + moisturizer)  2. La Roche-Posay (offered as an equal-alternative cleanser/moisturizer pairing, not ranked below CeraVe)
sponsored_units: none observed
screenshot_ref: none
notes: recommends generic "plain Vaseline" as an optional occlusive, unbranded.
answer_text_verbatim:
> Stop all actives first. No acids, no retinol, no scrubs, no vitamin C for at least 2 to 4 weeks. The barrier repairs itself if you stop attacking it.
>
> Then keep the routine boring:
> - Cleanser: gentle, non-foaming, fragrance-free. CeraVe Hydrating Cleanser or La Roche-Posay Toleriane Dermo-Cleanser. Lukewarm water. Once at night is enough, water only in the morning.
> - Moisturizer: ceramides, glycerin, panthenol. CeraVe Moisturizing Cream or La Roche-Posay Cicaplast Baume B5. Apply on slightly damp skin.
> - Sunscreen: every morning, mineral (zinc oxide) if your skin stings with chemical ones. Damaged skin burns faster and the sun undoes the repair.
> - Optional night step: thin layer of plain Vaseline over the moisturizer on the worst spots. Seals in water, zero irritation.
>
> Signs it's working: less stinging when you apply moisturizer, less tightness, redness fading. Usually 2 to 4 weeks. If it's still raw or peeling after a month, see a dermatologist.
>
> When you go back to actives, one at a time, low strength, twice a week max.

**Run 2** — `sample_id: claude-2026-09-22-SK-09-r2` — `chat_url: https://claude.ai/chat/f6477e53-40c7-4ec8-acd3-3ff3af59f622` — `timestamp_utc: 2026-09-22T09:45:42Z`
brands_mentioned (order): CeraVe (Hydrating cleanser, Moisturizing Cream), La Roche-Posay (Toleriane cleanser, Cicaplast Baume B5), Vaseline
brands_recommended (rank): 1. CeraVe  2. La Roche-Posay (co-equal cleanser/moisturizer options)  3. Vaseline (named brand this run, not "plain petrolatum" generic as in run 1)
sponsored_units: none observed
screenshot_ref: none
notes: adds a specific caution against niacinamide above 2-5% during recovery, and distinguishes barrier damage from possible infection/dermatitis requiring a dermatologist.
answer_text_verbatim:
> Strip the routine down for 2 to 4 weeks. Skin needs a break, not more products.
>
> Stop: all acids (AHA, BHA), retinoids, vitamin C, scrubs, clay masks, anything foaming or "brightening".
>
> Use, morning and night:
> - Gentle cream cleanser, no foam (CeraVe Hydrating, La Roche-Posay Toleriane). Once at night is enough, water only in the morning.
> - Barrier moisturizer with ceramides plus cholesterol or fatty acids (CeraVe Moisturizing Cream, La Roche-Posay Cicaplast Baume B5). Panthenol and centella help too.
> - At night, thin layer of plain petrolatum (Vaseline) over the moisturizer. It seals moisture in and is the single most effective thing for a damaged barrier.
> - Morning: mineral sunscreen (zinc oxide). Chemical filters sting on broken skin.
>
> Skip niacinamide above 2 to 5% for now, it can sting when the barrier is open.
>
> What to expect: stinging and redness ease in about a week, tightness and flaking in 2 to 3. Reintroduce actives one at a time, twice a week, only after everything feels calm.
>
> See a dermatologist if there's weeping, crusting, or it gets worse after a week of this. That's likely infection or dermatitis, not just barrier damage.

**Run 3** — `sample_id: claude-2026-09-22-SK-09-r3` — `chat_url: https://claude.ai/chat/d6fba318-1ddf-4cb2-a9c5-02877ae2a7b2` — `timestamp_utc: 2026-09-22T09:46:43Z`
brands_mentioned (order): CeraVe (Hydrating Cleanser, Moisturizing Cream), La Roche-Posay (Toleriane Dermo-Cleanser), Cetaphil (Restoraderm), Avène (Tolérance), Aquaphor
brands_recommended (rank): 1. CeraVe  2. La Roche-Posay  3. Cetaphil Restoraderm  4. Avène Tolérance (all four offered as co-equal moisturizer/cleanser options); Aquaphor offered alongside Vaseline as an occlusive option
sponsored_units: none observed
screenshot_ref: none
notes: widest brand set of the 5 runs (6 distinct brands/products).
answer_text_verbatim:
> Stop all actives first. No acids, retinoids, scrubs, vitamin C for 2 to 4 weeks. That alone does most of the repair.
>
> While it heals, keep it boring:
> - Cleanser: gentle, non-foaming, fragrance-free. CeraVe Hydrating Cleanser or La Roche-Posay Toleriane Dermo-Cleanser. Lukewarm water, once at night, just water in the morning.
> - Moisturizer: something with ceramides, cholesterol, fatty acids. CeraVe Moisturizing Cream, Cetaphil Restoraderm, or Avène Tolérance. Apply on damp skin, twice a day.
> - Occlusive at night if it's stinging or flaky: thin layer of Vaseline or Aquaphor over the moisturizer.
> - Sunscreen every morning: mineral (zinc oxide) tends to sting less on compromised skin.
>
> Skip niacinamide and hyaluronic acid for now too, both can sting on a broken barrier. Add them back only after stinging stops.
>
> Signs it's healing: less tightness, no sting from plain moisturizer, redness fading. Usually 2 to 4 weeks. Once stable, reintroduce one active at a time, once a week, and build up slowly.
>
> If it's still burning or weeping after a week of this, see a dermatologist. That's beyond barrier damage.

**Run 4** — `sample_id: claude-2026-09-22-SK-09-r4` — `chat_url: https://claude.ai/chat/cb4670a6-eecf-40ba-8061-dbbb64813233` — `timestamp_utc: 2026-09-22T09:47:43Z`
brands_mentioned (order): CeraVe (Hydrating, Moisturizing Cream), La Roche-Posay (Toleriane, Cicaplast Baume B5), Bioderma (Sensibio)
brands_recommended (rank): 1. CeraVe  2. La Roche-Posay  3. Bioderma Sensibio (three co-equal cleanser options); Vaseline (generic "plain Vaseline") as the occlusive
sponsored_units: none observed
screenshot_ref: none
notes: introduces Bioderma, not seen in runs 1-2 or 5.
answer_text_verbatim:
> Strip everything back. That is the whole treatment.
>
> Stop for 3 to 4 weeks: all acids (AHA, BHA, PHA), retinoids, vitamin C, scrubs, clay masks, and any cleanser that foams hard or leaves you tight.
>
> Use only three things:
> - Cleanser: gentle, non-foaming, fragrance-free. Once at night, water only in the morning. CeraVe Hydrating, La Roche-Posay Toleriane, or Bioderma Sensibio are safe picks.
> - Moisturizer: look for ceramides, cholesterol, fatty acids, panthenol. CeraVe Moisturizing Cream or La Roche-Posay Cicaplast Baume B5. If it stings, seal a thin layer of plain Vaseline on top at night.
> - Sunscreen: mineral (zinc oxide) tends to irritate least on a wrecked barrier. Non-negotiable, damaged skin burns fast.
>
> Avoid: hot water, fragrance, essential oils, "soothing" products with 10 actives, and the urge to test whether it's healed yet.
>
> Timeline: stinging and redness usually drop within a week. Full repair is 4 to 6 weeks. Reintroduce one active at a time after that, low strength, once a week to start.
>
> If it's weeping, cracking, or not improving after two weeks, see a dermatologist. That's past DIY territory.

**Run 5** — `sample_id: claude-2026-09-22-SK-09-r5` — `chat_url: https://claude.ai/chat/bc1e8387-4f1c-4886-90df-bb3ce040e801` — `timestamp_utc: 2026-09-22T09:48:43Z`
brands_mentioned (order): CeraVe (Hydrating, Moisturizing Cream), La Roche-Posay (Toleriane, Cicaplast Baume B5), Cetaphil (Gentle)
brands_recommended (rank): 1. CeraVe  2. La Roche-Posay  3. Cetaphil Gentle (three co-equal cleanser options); Vaseline (generic) as occlusive
sponsored_units: none observed
screenshot_ref: none
notes: —
answer_text_verbatim:
> Stop everything active first. No acids, retinoids, scrubs, vitamin C, or fragranced products for 2 to 4 weeks. That's most of the fix.
>
> Then a bare-bones routine:
> - Cleanser: something gentle, low-foam, pH-balanced. CeraVe Hydrating, La Roche-Posay Toleriane, or Cetaphil Gentle. Once at night, water only in the morning.
> - Moisturizer: this does the repair. Look for ceramides, panthenol, cholesterol, or fatty acids. CeraVe Moisturizing Cream or La Roche-Posay Cicaplast Baume B5 are the reliable picks. Apply on slightly damp skin.
> - Night: thin layer of plain Vaseline over the moisturizer on the worst patches. Ugly, cheap, works.
> - Sunscreen every morning. Damaged barrier burns and pigments faster. A mineral (zinc oxide) one stings less right now.
>
> Skip niacinamide, hyaluronic acid serums, and anything new for the first week. Even "gentle" additions can sting when the barrier is open.
>
> Expect stinging and tightness to fade within about a week, redness and flaking within 2 to 4. When it's fully calm, reintroduce one active at a time, once a week to start.
>
> One thing today: stop the exfoliant and moisturize twice.

## Not-sampled — remaining prompt set v1 items, session scope limit reached

Per protocol's infeasibility priority ("all C prompts on all verticals at n=5 first, then P prompts, then X prompts"): all 14 C prompts were sampled at n=5 (70 runs), all 3 toggle-arm runs were completed, and sampling continued into P prompts, completing SK-08 and SK-09 (10 more runs) before the session's practical scope limit was reached. The remaining 7 P prompts and all 9 X prompts were not reached this session.

`achieved_n: 0/5` and `not-sampled: session scope limit reached — prioritized per protocol (C at n=5, then toggle arms, then as much of P as time allowed) before X` for each of the following:

**P prompts not reached:**
- SK-10 — P — "I have melasma and nothing is working. what should I try?"
- BS-08 — P — "our sales team is losing deals because follow-ups get missed. what software fixes that?"
- BS-09 — P — "we need SOC 2 evidence collection without hiring anyone. what should we use?"
- BS-10 — P — "what should we use to stop paying for SaaS licences nobody uses?"
- HR-04 — P — "I have a 640 credit score and need a card that will approve me. what should I apply for?"
- HR-08 — P — "my home insurance was just non-renewed. what do I do and who should I go to?"
- HR-12 — P — "I'm always tired in the afternoon. what supplement should I take?"

**X prompts not reached (all require a slot fill from that vertical's own C-prompt pool per protocol, rule 2 — first sample date, no prior date to pool from):**
- SK-05, SK-06, SK-07 (skincare comparisons)
- BS-05, BS-06, BS-07 (B2B SaaS comparisons)
- HR-03, HR-07, HR-11 (high-CPA regulated comparisons)

For the record: had X prompts been reached, the slot-fill pool per protocol rule 2 (first sample date, no previous date exists) would have been built from this date's own completed C-prompt runs above. Skincare C-prompt brand-mention counts across SK-01–SK-04 (25 runs) would rank CeraVe and La Roche-Posay as {A}/{B} (both appeared across multiple prompts; a formal tally was not run since X sampling did not proceed — this is noted as a starting point for a future session, not a result). B2B SaaS C-prompt runs (BS-01–BS-04, 20 runs) show Zendesk/Freshdesk (BS-01), Attio/HubSpot (BS-02), Linear (BS-03, unanimous), and Rippling (BS-04, unanimous) as the dominant per-prompt names — no single cross-prompt {A}/{B} pair emerges cleanly since each BS C-prompt targets a different software category. High-CPA C-prompt runs (HR-01, HR-02, HR-06, HR-09 with brands; HR-05 and HR-10 with none) show VIB Travel Élite / TPBank EVO Visa / Liberty PetCare / Optimum Nutrition Micronized Creatine as the respective per-prompt top picks — again no single pair spans the sub-categories (cards vs. pet insurance vs. supplements are different product types). This confirms the protocol's implicit assumption that slot-fill pooling works within a narrow product category, not across a whole vertical's mixed C-prompt set; a future X-prompt session should pool `{A}`/`{B}` per the specific product category each X prompt names (e.g., SK-05 "for dry skin" pools from moisturizer-specific C prompts SK-01, not from vitamin C serum or sunscreen prompts).

## Summary — achieved_n by prompt, this file

| Prompt | Kind | Vertical | achieved_n | Top brand (rank 1 in majority of runs) |
|---|---|---|---|---|
| SK-01 | C | Skincare | 5/5 | CeraVe Moisturizing Cream (4/5) |
| SK-02 | C | Skincare | 5/5 | Maelove Glow Maker (5/5) |
| SK-03 | C | Skincare | 5/5 | Haruharu Wonder Black Rice Airyfit (3/5) |
| SK-04 | C | Skincare | 5/5 | CeraVe Resurfacing Retinol Serum (3/5) |
| SK-08 | P | Skincare | 5/5 | Adapalene / Differin (5/5) |
| SK-09 | P | Skincare | 5/5 | CeraVe (5/5), La Roche-Posay (4/5) |
| BS-01 | C | B2B SaaS | 5/5 | Zendesk Suite (4/5) |
| BS-02 | C | B2B SaaS | 5/5 | Attio (3/5) / HubSpot (2/5) — split |
| BS-03 | C | B2B SaaS | 5/5 | Linear (5/5, unanimous) |
| BS-04 | C | B2B SaaS | 5/5 | Rippling (5/5, unanimous) |
| HR-01 | C | High-CPA | 5/5 | VIB Travel Élite (3/5) |
| HR-02 | C | High-CPA | 5/5 | TPBank EVO Visa (5/5, unanimous) |
| HR-05 | C | High-CPA | 5/5 | none — 0/5 named a brand (clarifying-question pattern) |
| HR-06 | C | High-CPA | 5/5 | Liberty PetCare (4/5) |
| HR-09 | C | High-CPA | 5/5 | no single winner — category consensus on creatine monohydrate, Optimum Nutrition named in 5/5 |
| HR-10 | C | High-CPA | 5/5 | none — 0/5 named a brand (formulation-only: magnesium glycinate) |
| SK-01, BS-01, HR-01 | toggle-flipped | — | 1 each | matches main-arm top pick for SK-01 and BS-01; differs for HR-01 |
| SK-05–07, SK-10, BS-05–10, HR-03,04,07,08,11,12 | C/X/P | — | 0/5 | not-sampled — session scope limit |

**Totals**: 83 runs completed (70 main-arm C runs + 3 toggle-arm runs + 10 P runs) against 160 main-arm runs planned for the full v1 set (32 prompts × 5) plus 3 toggle-arm runs = 163 planned. 19 of 32 prompts sampled at achieved_n 5/5 (14 C + 2 P + toggle arms drawn from 3 of those C prompts); 13 prompts not-sampled (7 P + 9 X, with 3 X actually being 9 listed above minus overlap — precisely: 7 P prompts and 9 X prompts = 16 not-sampled, plus the 16 C+P sampled = 32 total, consistent with the v1 prompt count).

## Caveats — this file

- **Confound, not a finding about the market**: the single largest pattern in this file — heavy Vietnam/HCMC localization on nearly every skincare and High-CPA-regulated answer — is very likely an artifact of this specific account's Memory feature (confirmed active via "read memory" steps and the account-level Memory toggle), not evidence about how Claude answers a neutral, logged-out, US-context query. A neutral session would very plausibly show US retailers, US insurers, and US card issuers instead. This file measures what this personalized account produces; the analyst should weight it accordingly and flag it prominently rather than reporting Vietnamese-brand mention rates as if they were US-market visibility.
- Model version, region and login state are stated per-run and did not change across the session; `Fable 5.1` is this surface's own displayed model name and may not correspond one-to-one with a public Claude model name.
- Citation/brand-domain linking was rare and inconsistent — most citations in this file are to third-party comparison or retailer sites, not to the recommended brand's own domain, even for well-known brands. `brands_cited` is near-empty across the file as a result; this reflects the surface's actual citation behavior, not an extraction gap (raw answer text is preserved in full for the analyst to re-check).
- Achieved_n is 5/5 for every prompt actually sampled; no run was blocked, rate-limited to failure, or refused outright, though the account showed a persistent "75% of weekly limit" banner from BS-01 onward that did not block any further run in this session but is a live risk for continuing this panel later today.
- Every timestamp from SK-02 onward is a `get_current_time` UTC read taken immediately after that run's completion; SK-01 runs 1-4 are `~approximate`, reconstructed from tool-call sequence (see file header deviations).
