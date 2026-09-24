# Deck instruction — identical for every run. Only {RUN_ID}, {RUN_DIR}, {PDF_PATH}, {DECK_SKILL_FILES} differ.

Set 2026-09-24 by the user: "Do we not run the judge. make prompt and subagents foreach brief so it have enough context and making pdf output presentation based their skills. all brief presentation go to findings/". Earlier the same day: "I want pdf file as final output as presentation … since brief is missing presentation power".

You are deck run {RUN_ID}. Write only to `{RUN_DIR}\deck\` and to `{PDF_PATH}`. Do not run git. Do not use the web. Under `.claude/` read only the files named below. Do not open any other `runs/` folder, any file with `-r2` in its name, `docs/method/gen-director-deck*.py`, or any `.pptx`.

## Situation

A director who has never heard of this project, market or any of its acronyms will sit through, or flip through, one presentation. They want: what is this, why now, how big, who is already there, what could kill it, what is asked of them. The subject: whether real demand exists, per segment, for brand visibility and product recommendation inside AI assistants (ChatGPT, Gemini, Perplexity, Copilot, Claude), and what evidence shows it works. The programme is research only. It produces evidence, not a go/no-go. The verdict belongs to the director.

Your run already wrote a text brief for this director. It has the storyline but no presentation power. Your job is to turn it into a presentation, a PDF, that lands in the room.

## Read first, in order

1. `{RUN_DIR}\PROMPT.md`: the brief contract your run followed, including its storyline method files. Its constraints 1–16 still apply, except constraint 9 (word cap) and the output paths.
2. `{RUN_DIR}\brief.md`, `trace.md`, `notes.md`: your storyline, its verified numbers, your method notes.
3. Your deck method. Treat these files as your operating instruction for slides. Where they conflict with the constraints below, the constraints win and you record the conflict:
{DECK_SKILL_FILES}
4. Only if a number you need is not in your `trace.md`: `docs/method/brief-bakeoff/fact-pack-8badc05.md`, then the snapshot export `.bakeoff-snapshot/8badc05/docs/` (cite paths as `docs/...`). Input snapshot is commit `8badc05`; cite nothing newer.

## Deck constraints (win over the deck method)

1. **Numbers.** Every number on a slide, in a chart, or in speaker notes is in your `trace.md` or gets a new row in `deck\trace-deck.md`: `number | slide | repo path:line | source kind | source date`. A number you cannot trace does not go in.
2. **No arithmetic** on repo numbers unless a repo file already did it. Charts plot traced values only: no interpolation, no smoothing, no illustrative or placeholder data. Axis units and scale are stated. Two figures in different units or metrics never share an axis.
3. **Conflicts** sit side by side, attributed, never averaged. Unknowns show as `unknown — not in repo`, never as an empty bar or a zero.
4. **Source on the slide.** Each content slide has a footer line with source kind and date for the numbers on it (e.g. "filed, 2026-02; vendor-reported, 2026-09"). Full path:line goes in `trace-deck.md`, not on the slide.
5. **Research only.** No action dates, budgets, MVPs, roadmaps, owners, go/no-go or "we recommend proceeding". The answer slot the method demands (governing thought, recommendation, so-what) carries what the evidence supports and where it stops. The ask, if any, is a decision the director owns, framed as options with evidence.
6. **Cold reader.** Every acronym is defined on first use or on a glossary slide. No internal codenames in the deck: no pass numbers, hypothesis codes, run ids, file or folder names, review round names. Evidence tiers are defined on a slide before they are used.
7. **Length.** At most 20 main slides, plus an appendix of any length. The title slide carries "Research only: evidence, not a verdict" and "Evidence as of 2026-09".
8. **Legibility.** 16:9. Body text 14 pt or larger, slide titles 24 pt or larger, footers 10 pt or larger. No text overflow, clipping or overlap. Charts readable in greyscale (labels on the marks, not colour alone).

## Build

- Author `deck\deck.html`: one `<section class="slide">` per slide, self-contained, with CSS inline, charts as inline SVG hand-built from traced values, no external scripts, fonts or images. Page setup: `@page { size: 13.333in 7.5in; margin: 0 }`, each section exactly `13.333in × 7.5in`, `page-break-after: always`, `overflow: hidden`.
- Speaker notes, if your method uses them: `deck\speaker-notes.md`, one heading per slide. The same number rules apply.
- Render (Git Bash; your own profile dir so parallel runs don't collide):

```
"/c/Program Files/Google/Chrome/Application/chrome.exe" --headless=new --disable-gpu --no-pdf-header-footer \
  --user-data-dir="$(cygpath -w "{RUN_DIR_POSIX}/deck/.chrome")" \
  --print-to-pdf="$(cygpath -w "{PDF_PATH_POSIX}")" "file:///$(cygpath -m "{RUN_DIR_POSIX}/deck/deck.html")"
```

- **Visual QA, required.** Open the PDF with the Read tool (`pages` parameter, at most 20 per call) and look at every page. Fix overflow, clipping, unreadable charts and orphaned slides, then re-render. Repeat until clean. Record the number of QA rounds. Delete `deck\.chrome\` when done.

## Also write

`deck\notes-deck.md`, at most 300 words:
- Model id and timestamp.
- What the deck method made you do that you would not have done unaided. Quote the rule with its file path and line. For `strategyu-skills` and `strategy-skills-for-claude` (no licence), give path:line plus a paraphrase of 12 words or fewer, never verbatim.
- Every override of the deck method by a constraint above: the rule, the constraint.
- Where the storyline changed from `brief.md` and why.
- QA rounds, and any defect left unfixed.

## Return

Six lines: run id · main slide count · appendix slide count · PDF path · rows in `trace-deck.md` (0 if all numbers came from `trace.md`) · overrides in `notes-deck.md`.
