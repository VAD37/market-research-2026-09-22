# Template — `docs/raw/` pull

One file per pull. **Exempt from compression and from line budgets** (root `CLAUDE.md`). Raw stays raw, in the source's own words.

**Never edited after the fact.** Not to shorten it, not to fix it, not to correct a tier. A wrong or stale pull is re-pulled into a new file; the old file stays exactly as landed.

**No interpretation.** A sentence beginning "this suggests" belongs in a compiled folder, not here. The only non-source text in this file is the header block and bracketed `[note: ...]` markers recording what the pull could not capture (paywall, login wall, rendered chart, truncation).

## Filename

`<lane>-<engine-or-vendor>-<topic>-<YYYY-MM-DD>.md` — lowercase, hyphens, ASCII only.

| Part | Rule |
|---|---|
| `<lane>` | `a`–`f` per `../glossary.md`. A cross-lane pull takes the lane that requested it |
| `<engine-or-vendor>` | The source's own short name, slugified. No vendor (registry, forum, paper, filing): use the publisher or venue |
| `<topic>` | One to three words: what the pull is about — `pricing`, `merchant-terms`, `case-study`, `methodology` |
| `<YYYY-MM-DD>` | The **pull** date, not the publication date |

Shape only: `b-<engine>-ad-policy-2026-09-22.md`, `e-<venue>-methodology-2026-09-22.md`.

## Re-pull

A new pull of an already-pulled source is a **new file** at the new pull date, same naming. The old file is kept and not touched. The new file names the old in `supersedes:`. Two pulls of the same source on the same date get a `-2` suffix on the topic.

## Tier and label

`tier:` is the 1–7 provenance score from `../trust-rubric.md`, and carries a reason whenever the tier was adjusted from the table default (hidden method drops one tier; vendor-authored paper on its own product is tier 5, bias flagged).

Tier 6 and 7 may be pulled **only** as evidence about the category's noise level, and the header says so in `pull-purpose:`. Never as evidence about a number. Discard-on-sight items in `../trust-rubric.md` are not pulled at all.

`source-label:` is one of `vendor-reported`, `analyst-derived`, `filed`, `company-stated`, `measured-by-us` — what kind of number the body carries. A body carrying no number still takes the label that fits its author.

---

<!-- Copy from here down into docs/raw/<filename>.md. Delete these guidance comments. -->

# <source name> — <topic>

```yaml
source:          <publisher or author, as the source names itself>
url_or_doc_id:   <full URL, or filing / document / DOI identifier>
published:       <YYYY-MM-DD of the source, or "undated — no date on page">
pull_date:       <YYYY-MM-DD — absolute, the date this file was made>
pull_method:     <fetch | browser extension | predecessor repo | manual>
pull_purpose:    <evidence about a number | evidence about category noise>
tier:            <1-7>
tier_reason:     <why, if adjusted from the trust-rubric default; else "table default">
source_label:    <vendor-reported | analyst-derived | filed | company-stated | measured-by-us>
lane:            <A-F>
sub_market:      <organic recommendation | paid placement | agentic commerce | n/a>
engine:          <engine and model version if the source names one; else "n/a">
metric_kind:     <visibility | traffic | sales | none — per glossary, if the body carries a number>
supersedes:      <path of the pull this one re-pulls; else "none">
captured:        <full page | section "<name>" | table only | transcript excerpt>
```

<!-- measured-by-us pulls add these four lines to the block above: -->
<!-- prompt_set: <name and version> | runs_n: <n> | surface: <consumer chat | API | search-integrated> | region: <as set> -->

## Verbatim

<!-- The source's own words, unedited. Quote blocks for prose, tables reproduced as tables,
     numbers exactly as printed including the source's units and rounding.
     Mark every gap: [note: paywall after paragraph 3], [note: figure 2 is an image, not captured]. -->

<paste here>

## Pull notes — mechanical only

<!-- What happened during the pull, not what it means. Access path, blocked elements,
     redirects, login state, truncation, whether the page was dynamic.
     Anything evaluative goes in a compiled file instead. -->

- <note>
