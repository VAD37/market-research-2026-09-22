# prompt-archive

Every human input typed into Claude Code while working in this repo, 2026-09-22 onward. Verbatim, chronological, one file per session plus one global timeline. Purpose: show others how the research programme was driven — what was asked, in what order, how corrections were phrased. Agent output is deliberately left out; only a 200-char head of each reply is kept for orientation.

## Files

| file | what |
|---|---|
| `extract-prompts.js` | the extractor. Source of truth; everything below is generated from it |
| `INDEX.md` | one row per session: start, span, prompt count, chars, model, compactions, first prompt |
| `TIMELINE.md` | all inputs across all sessions, chronological, grouped by day |
| `sessions/<date>-<hhmm>-<id8>.md` | one file per session, same content as its slice of the timeline |
| `prompts.csv` | same data flat: `timestamp_utc, session, kind, cwd, model, chars, prompt, reply_head` |

Generated files are never hand-edited. Re-run and commit:

```
node prompt-archive/extract-prompts.js
```

## Where the data comes from

Claude Code writes one JSONL transcript per session under `~/.claude/projects/<repo-slug>/`. Each line is one message. Human prompts carry `origin.kind == "human"`; everything else on the user role is machinery (tool results, peer-session messages, task notifications, compaction summaries, hook output). The extractor keeps four kinds:

| kind | meaning |
|---|---|
| typed | prompt typed at the prompt line |
| queued | typed while the previous turn was still running (delivered mid-turn) |
| interrupt | Esc / Ctrl-C (`[Request interrupted by user]`) |
| slash | `/compact`, `/clear`, `/model`, `/plugin`, … |

Subagent transcripts (`<session>/subagents/*.jsonl`) hold no human input and are not read.

## Reading notes

- Times are UTC. Local time (Asia/Ho_Chi_Minh) is +7h.
- Several sessions run in parallel, so the timeline interleaves terminals. The `· <id8>` after each timestamp says which session; `INDEX.md` maps id to file.
- Duplicate pairs with identical first prompts at the same minute (e.g. 1ef2b86d / 6482c801, 2af3fa87 / ab9c8d4f, 460d9a47 / 58b43776) are forks or resumed sessions. Both kept; the archive is lossless, not deduplicated.
- `<pasted_content>` blocks are content the operator pasted from elsewhere (usually a prior agent's reply) and are kept verbatim inside the prompt.
- `cwd` is shown only when the session ran from a subfolder of the repo.
- The `> →` line under a prompt is the first text the assistant said afterwards, cut at 200 chars. It is orientation, not the reply.
- Prompts are raw operator text: typos, Vietnamese fragments and shorthand are as typed.

## Caveats

- Sessions started before Claude Code 2.1.280 lack the `origin` field; the extractor falls back to text patterns for interrupts and slash commands only. All sessions here are 2.1.259+ and the fallback was needed only for those two kinds.
- A session's `models` column lists every model that answered in that session; the model shown per prompt is the last one that answered before it.
- Nothing here is research evidence. It is process record and stays out of `docs/`.
