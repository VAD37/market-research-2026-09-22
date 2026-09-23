# Peec AI — "Introducing: Ads Page" (2026-07-16): competitor ChatGPT-ad monitoring inside the visibility tool

```yaml
source:          Peec AI (peec.ai blog)
url_or_doc_id:   https://peec.ai/blog/introducing-ads-page
published:       2026-07-16 ("Jul 16, 2026")
pull_date:       2026-09-23
pull_method:     fetch (curl, User-Agent "market-research-bot contact: research@example.invalid"; HTML tag-stripped)
pull_purpose:    evidence about a number
tier:            3
tier_reason:     table default — platform primary (vendor changelog-type post); the example figures ("79 brands ... 50 prompts ... 65 bidding") are illustrative copy, not a measurement
source_label:    vendor-reported
lane:            A
sub_market:      paid placement (monitoring of ads inside ChatGPT)
engine:          OpenAI — ChatGPT
metric_kind:     visibility (ad coverage per prompt)
supersedes:      none — extends raw/a-peec-changelog-2026-09-22.md
captured:        full post
```

## Verbatim

> Introducing: Ads Page — Jul 16, 2026
> ChatGPT now shows ads inside its answers, and they're landing on the same prompts you already track with Peec AI. That puts competitor ad activity in the middle of your own visibility data, but scattered across individual chats with no way to see the pattern.
> The Ads page turns that into one view.
> What the Ads page answers — Which brands are running ads on your branded prompts [...]
> It all starts with a one-line summary, something like "79 brands run ChatGPT ads on 50 prompts, with 65 bidding on your brand."
> Below that is a five-KPI row: advertisers in market, how many are bidding on your brand, ad coverage, how many of your prompts show ads at all, and the average number of prompts each advertiser runs on.
> Next comes the full advertiser list: every brand running ads on your prompts, their creatives, the topics they're active on, and a spend tier estimated relative to each other. You can view it as every advertiser, every individual ad, or just the brands you already track. Click into any advertiser and you get their actual ads: the copy, the image, the destination link, how often it's shown up [...]
> Worth noting: this is for monitoring competitor ad activity, not for buying ChatGPT ads yourself. And it only surfaces ads on the prompts your account already tracks, not a general ad library.
> → Start with your own brand terms. Advertisers running ads on your branded and comparison prompts are the ones directly contesting the queries that are about you.
> → Follow ad coverage over time. A topic whose ad coverage keeps climbing is one ChatGPT is actively monetizing, and worth watching before the competition deepens.
> The Ads page is rolling out now. It'll show up in your sidebar once it's enabled for your organization. See the docs for a closer look at everything the page covers.
> If you're not using Peec AI yet, start a free trial or book a demo to see who's advertising against you in ChatGPT.

## Pull notes — mechanical only

- Sitemap of peec.ai lists no ads-specific pricing URL; `/pricing` and `/pricing-agencies` exist and were pulled on 2026-09-22/23 (`raw/a-peec-pricing-*`). No separate SKU or surcharge for the Ads page is stated in this post.
- "Spend tier estimated relative to each other" is the only spend statement; no currency figure.
