#!/usr/bin/env node
// extract-prompts.js — pull every human input from Claude Code session transcripts
// for this repo and render them as markdown + CSV. Output is generated; never hand-edit.
//
// Usage:  node prompt-archive/extract-prompts.js [--src <dir>] [--out <dir>] [--no-reply]
//   --src       transcript dir (default: ~/.claude/projects/<slug of this repo>)
//   --out       output dir (default: the folder this script lives in)
//   --no-reply  omit the one-line head of the assistant reply after each prompt
//
// What counts as human input (kept):
//   typed      origin.kind == "human", promptSource "typed"   — prompt typed at the REPL
//   queued     origin.kind == "human", promptSource "queued"  — typed while a turn was running
//   interrupt  "[Request interrupted by user...]"             — Esc / Ctrl-C
//   slash      "<command-name>/x</command-name>" or bare "/compact ..." — slash commands
// Dropped (not human input):
//   tool_result blocks, peer messages from other sessions (origin "peer"), task notifications,
//   compaction summaries (isCompactSummary), meta/system lines (isMeta), local-command stdout,
//   "## Context Usage" statusline dumps, subagent transcripts (subagents/*.jsonl).

const fs = require('fs');
const path = require('path');
const os = require('os');

const args = process.argv.slice(2);
const opt = (k, d) => { const i = args.indexOf(k); return i >= 0 ? args[i + 1] : d; };
const REPLY = !args.includes('--no-reply');
const REPO = path.resolve(__dirname, '..');
const slug = REPO.replace(/[:\\\/]/g, '-');
const SRC = opt('--src', path.join(os.homedir(), '.claude', 'projects', slug));
const OUT = opt('--out', __dirname);
const REPLY_MAX = 200;

const files = fs.readdirSync(SRC).filter(f => f.endsWith('.jsonl'));
const sessions = [];

for (const f of files) {
  const lines = fs.readFileSync(path.join(SRC, f), 'utf8').split('\n').filter(Boolean);
  const recs = [];
  for (const l of lines) { try { recs.push(JSON.parse(l)); } catch { /* skip */ } }
  const prompts = [];
  let model = null, version = null, compactions = 0;
  const modelsSeen = new Set();
  for (let i = 0; i < recs.length; i++) {
    const o = recs[i];
    if (o.version) version = o.version;
    if (o.type === 'assistant' && o.message && o.message.model && !o.message.model.startsWith('<')) {
      model = o.message.model; modelsSeen.add(model);
    }
    if (o.isCompactSummary) compactions++;
    if (o.type !== 'user' || o.isSidechain) continue;
    const c = o.message && o.message.content;
    if (Array.isArray(c) && c.some(b => b.type === 'tool_result')) continue;
    const text = Array.isArray(c) ? c.map(b => b.text || '').join('\n') : (c || '');
    let kind = null;
    if (o.origin && o.origin.kind === 'human') kind = o.promptSource === 'queued' ? 'queued' : 'typed';
    else if (o.origin || o.isCompactSummary || o.isMeta) continue;
    else if (/^\[Request interrupted by user/.test(text)) kind = 'interrupt';
    else if (/^<command-name>\//.test(text)) kind = 'slash';
    else if (/^\/[a-z]/.test(text)) kind = 'slash';
    else continue;
    let shown = text;
    if (kind === 'slash' && text.startsWith('<command-name>')) {
      const n = (text.match(/<command-name>([^<]*)<\/command-name>/) || [])[1] || '';
      const a = (text.match(/<command-args>([^<]*)<\/command-args>/) || [])[1] || '';
      shown = (n + ' ' + a).trim();
    }
    let reply = '';
    if (REPLY) {
      for (let j = i + 1; j < recs.length; j++) {
        const r = recs[j];
        if (r.type === 'user' && r.origin && r.origin.kind === 'human') break;
        if (r.type !== 'assistant' || !r.message || !Array.isArray(r.message.content)) continue;
        const t = r.message.content.filter(b => b.type === 'text').map(b => b.text).join(' ').trim();
        if (t) { reply = t; break; }
      }
    }
    prompts.push({
      ts: o.timestamp, kind, text: shown, chars: shown.length,
      cwd: (o.cwd || '').replace(REPO, '.').replace(/\\/g, '/') || '.',
      model: model || 'unknown', reply: oneLine(reply, REPLY_MAX),
    });
  }
  if (!prompts.length) continue;
  const humanOnly = prompts.filter(p => p.kind === 'typed' || p.kind === 'queued');
  sessions.push({
    id: f.replace('.jsonl', ''), short: f.slice(0, 8), prompts, version,
    models: [...modelsSeen], compactions,
    first: prompts[0].ts, last: prompts[prompts.length - 1].ts,
    nHuman: humanOnly.length, chars: humanOnly.reduce((s, p) => s + p.chars, 0),
    title: oneLine((humanOnly[0] || prompts[0]).text, 70),
  });
}
sessions.sort((a, b) => a.first.localeCompare(b.first));

// ---- render ----
function oneLine(s, n) { s = (s || '').replace(/\s+/g, ' ').trim(); return s.length > n ? s.slice(0, n - 1) + '…' : s; }
function fence(s) { const m = (s.match(/`+/g) || []).reduce((a, x) => Math.max(a, x.length), 0); const q = '`'.repeat(Math.max(3, m + 1)); return `${q}text\n${s}\n${q}`; }
function hhmm(ts) { return ts.slice(11, 16); }
function day(ts) { return ts.slice(0, 10); }
function csvq(s) { return '"' + String(s).replace(/"/g, '""') + '"'; }
function slugName(s) { return `${s.first.slice(0, 10)}-${hhmm(s.first).replace(':', '')}-${s.short}`; }
const kindMark = { typed: '', queued: ' _(queued mid-turn)_', interrupt: ' _(interrupt)_', slash: ' _(slash)_' };

function renderPrompt(p, withSession) {
  const hdr = `### ${day(p.ts)} ${hhmm(p.ts)}Z${withSession ? ` · ${withSession}` : ''}${kindMark[p.kind]}`;
  const meta = [];
  if (p.cwd !== '.') meta.push(`cwd \`${p.cwd}\``);
  if (p.model !== 'unknown') meta.push(p.model);
  let out = hdr + '\n' + (meta.length ? `<sub>${meta.join(' · ')}</sub>\n\n` : '\n');
  out += p.kind === 'typed' || p.kind === 'queued' ? fence(p.text) : `\`${p.text}\``;
  if (REPLY && p.reply) out += `\n\n> → ${p.reply}`;
  return out + '\n';
}

fs.mkdirSync(path.join(OUT, 'sessions'), { recursive: true });
for (const f of fs.readdirSync(path.join(OUT, 'sessions'))) fs.unlinkSync(path.join(OUT, 'sessions', f));

// per-session files
for (const s of sessions) {
  const name = slugName(s);
  let md = `# Session ${s.short} — ${day(s.first)}\n\n`;
  md += `Generated by \`extract-prompts.js\`; do not hand-edit.\n\n`;
  md += `| | |\n|---|---|\n| session id | \`${s.id}\` |\n| span (UTC) | ${s.first.slice(0, 16)} → ${s.last.slice(0, 16)} |\n| human prompts | ${s.nHuman} (${s.chars} chars) |\n| other inputs | ${s.prompts.length - s.nHuman} (interrupts / slash) |\n| models | ${s.models.join(', ') || 'unknown'} |\n| compactions | ${s.compactions} |\n| claude code | ${s.version || 'unknown'} |\n\n---\n\n`;
  md += s.prompts.map(p => renderPrompt(p, null)).join('\n');
  fs.writeFileSync(path.join(OUT, 'sessions', name + '.md'), md);
  s.file = `sessions/${name}.md`;
}

// index
let idx = `# Prompt archive — session index\n\nGenerated by \`extract-prompts.js\`; do not hand-edit. Times UTC.\n\n`;
idx += `| # | start | span | prompts | chars | models | compact | first prompt | file |\n|---|---|---|---|---|---|---|---|---|\n`;
sessions.forEach((s, i) => {
  idx += `| ${i + 1} | ${s.first.slice(0, 16).replace('T', ' ')} | ${hhmm(s.first)}–${hhmm(s.last)} | ${s.nHuman} | ${s.chars} | ${s.models.map(m => m.replace('claude-', '')).join(', ')} | ${s.compactions} | ${oneLine(s.title, 50).replace(/\|/g, '\\|')} | [${s.short}](${s.file}) |\n`;
});
const all = sessions.flatMap(s => s.prompts.map(p => ({ ...p, short: s.short }))).sort((a, b) => a.ts.localeCompare(b.ts));
const human = all.filter(p => p.kind === 'typed' || p.kind === 'queued');
idx += `\n**Totals:** ${sessions.length} sessions · ${human.length} human prompts · ${human.reduce((s, p) => s + p.chars, 0)} chars · ${all.length - human.length} interrupts/slash · ${day(all[0].ts)} → ${day(all[all.length - 1].ts)}\n`;
fs.writeFileSync(path.join(OUT, 'INDEX.md'), idx);

// global timeline
let tl = `# Prompt archive — timeline\n\nEvery human input across all sessions, chronological, verbatim. Generated by \`extract-prompts.js\`; do not hand-edit. Times UTC.\n\n`;
let curDay = '';
for (const p of all) {
  if (day(p.ts) !== curDay) { curDay = day(p.ts); tl += `\n## ${curDay}\n\n`; }
  tl += renderPrompt(p, p.short) + '\n';
}
fs.writeFileSync(path.join(OUT, 'TIMELINE.md'), tl);

// csv
let csv = 'timestamp_utc,session,kind,cwd,model,chars,prompt' + (REPLY ? ',reply_head' : '') + '\n';
for (const p of all) csv += [p.ts, p.short, p.kind, p.cwd, p.model, p.chars, csvq(p.text)].concat(REPLY ? [csvq(p.reply)] : []).join(',') + '\n';
fs.writeFileSync(path.join(OUT, 'prompts.csv'), csv);

console.log(`${sessions.length} sessions, ${human.length} human prompts, ${all.length - human.length} other inputs -> ${OUT}`);
