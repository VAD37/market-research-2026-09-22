#!/usr/bin/env python3
"""check-runs.py -- mechanical checks on brief bake-off runs (Pass 15).

One-off script. Python 3.9+, stdlib only, UTF-8 in and out. Read-only on every
input; writes only the paths given to --out and --detail.

Purpose
    For each run folder (docs/method/brief-bakeoff/runs/<id>/, holding brief.md,
    notes.md, trace.md) compute the mechanically checkable parts of README
    §Judge and shared-instruction.md constraints 1-16: word counts, trace
    verification against the frozen evidence snapshot, untraced body numbers,
    process leak, undefined acronyms, unknown count, verdict-push phrases.

Usage
    python check-runs.py runs/R0-baseline runs/R0b-baseline-repeat \
        [--snapshot D:/.../.bakeoff-snapshot/8badc05] [--map judge/map.csv] \
        [--returns returns.csv] --out checks.csv [--detail checks.md]

    --map <csv>      columns letter,run_id. Rows are keyed by letter and the
                     run id / folder name is never printed (blind judging).
                     run_id matches a folder name exactly or as its prefix
                     before '-' (R0 -> R0-baseline).
    --returns <csv>  columns run_id,words,rows,unknowns,overrides: the agent's
                     five-line return, compared with what this script counts.

Brief split
    Body = lines before the first level-2 heading titled Appendix or Glossary (optionally numbered, e.g. '## 9. Appendix')
    (case-insensitive). A '---' line directly above that heading (blank lines
    between allowed) is the separator and belongs to neither part.
    Appendix = everything from that heading on. No such heading: whole file is
    body and appendix is empty (flagged in files_present as 'no-appendix').

Output columns (one CSV row per run)
    key                 run folder name, or the letter under --map
    files_present       brief/notes/trace present, '-' prefix when missing
    body_words          whitespace split of body lines, tables and pipes
                        included (what `wc -w` gives on those lines)
    notes_words         whitespace split of notes.md
    notes_model_ids     claude-opus-*/claude-sonnet-*/claude-haiku-*/
                        claude-fable-* ids and '<synthetic>' found in notes.md
    notes_overrides     list items under a notes heading containing 'overrid'
    trace_rows          table rows of trace.md with >=5 cells (header and
                        separator excluded)
    trace_verified      EVERY row checked: each digit group of the number cell
                        (see Number tokens) occurs as a token on the cited
                        snapshot line, comma-insensitive. Exact line only (±0).
                        A cited range a:b uses all lines a..b. A path with a row
                        id instead of a line (e.g. 'demand-map.md (C1)', 'E19')
                        resolves to the table row whose first cell is that id.
                        Cells with no digits are checked by number words
                        (one..twenty, thirty..ninety, hundred): each word must
                        occur on the line as the word or its digits.
    trace_unverified    rows whose line resolved but a digit group is missing
    trace_unresolvable  rows with no parseable docs/ path, file absent from the
                        snapshot, line out of range, row id not found, or a
                        forbidden cite (counted here too, per README Amendments)
    forbidden_cites     trace rows citing STATE.md, plan.md, biz-review*, or a
                        file whose name contains -r2
    body_numbers        number tokens in the body
    body_numbers_traced tokens found in a trace row for the same brief line
    body_numbers_excluded   untraced tokens the classifier calls labels/dates
    body_numbers_untraced   untraced tokens the classifier does not exclude
    appendix_numbers_untraced   same test on the appendix (constraint 1 says
                        every number in brief.md)
    process_leak        body hits, non-overlapping, for: repo paths ('docs/',
                        '*.md', '.csv', '.py'), 'Pass N', 'H<digits>', 'P1<d>',
                        'REV-', 'BRIEF-N', 'GAP-', 'IMG-N', 'biz-review',
                        '-r2', 'Lane A-F', 'wave N', 'round N', 'first/second/
                        third round', a git short hash
    acronyms_undefined  distinct body tokens matching \b[A-Z]{2,}[a-z]?\b not
                        defined inline anywhere in the body as '(XX)' or
                        'XX (', and not in a glossary. Glossary = a section
                        whose heading says glossary/terms/abbreviations/
                        acronyms/definitions, or a table whose header's first
                        cell is Term/Acronym/Abbreviation. Its table first
                        cells and '- TERM — meaning' bullet leads count; a cell
                        is split on ; / , and each acronym token in it counts.
                        Other appendix tables (sources, figure pairs) do not.
                        A trailing lowercase 's' also matches the bare acronym
                        (LLMs -> LLM).
    unknown_count       occurrences in the whole brief of 'unknown — not in
                        repo' and 'unknown — checked' (any dash, any spacing)
    verdict_push_hits   body hits for go/no-go phrasing (VERDICT_PATTERNS)
                        not negated by no/not/never/nor/without within the
                        preceding 30 characters; negated hits listed in detail
    returns_match       'ok' or the mismatches, when --returns is given

Number tokens
    A token is \\d{1,3}(,\\d{3})+ or \\d+, optionally with .\\d+, not directly
    preceded by a digit, '.' or ','. Commas are stripped before comparison.
    '2026-09-23' yields 2026, 09, 23 on both sides, so dates compare as
    their parts. Trace number cells skip letter-prefixed tokens (R1, A4, Q2,
    FY2025, x402) and 'risk N' / 'rank N' / 'rule N' labels. The
    snapshot side keeps every token (a date inside a raw filename counts) and
    adds the digits of number words (Seven -> 7).

Body-number classifier (applied only to tokens with no trace row on their
line; excluded tokens are listed in --detail by category)
    hash         7-40 hex chars with a letter and a digit (git hashes); masked
    code         inside `backticks` (paths, path:line refs); masked
    heading      the section number right after '#'s ('## 3. Market')
    ordinal      list ordinal at line start: '1. ', '7–8. ', '2) '
    rownum       a table row whose first cell is a bare integer ('| 1 |')
    alnum        directly preceded by a letter, or letter + hyphen: R1, Q2,
                 H3, B2B, FY2025, x402, E6, HTTP-402, Apache-2.0, GPT-4
    legal-ref    after 'Art.', 'Article', '§', 'Section'
    form         followed by -K/-Q/-F etc.: 8-K, 10-K, 10-Q, 20-F
    date         part of YYYY-MM[-DD]; 'Month YYYY'; 'Q1 2026' year part
    year         bare 1990-2049 (forecast horizons, 'FY 2025', '2029–2030')
    tier         after 'tier(s)' ('tier 5–6', 'tier (1 strongest'); a source
                 kind then a digit ('filed 2', 'company-stated, 3',
                 'analyst-derived† 5–6'); a digit then a kind ('2 filed');
                 ', N)' and a bare '(N)' for N in 1-7; 'N strongest|weakest'
    tier (col)   a lone 1-7 or 'N–M' cell in a table column headed 'Tier'
    rank         after 'rank', 'risk', 'rule', '#', 'No.'
    path-line    directly after ':' with no space (':166')
    Dates and years are claims too; untraced ones are listed, not counted.

Caveat
    These columns are mechanical. They do not replace the judge's reading:
    a trace row can verify on digits while the brief misstates what the
    figure measures; a verified row can carry the wrong source kind or date;
    number words in the body ('four engines') are not tokenised; excluded
    categories can hide a real figure (a tier or year stated as a claim);
    process_leak counts strings, not 'what we did' narration; an acronym
    defined after first use still counts as defined. Read the detail file.
"""
import argparse
import csv
import io
import os
import re
import sys

DEFAULT_SNAPSHOT = r"D:\researchs\market-research-2026-09-22\.bakeoff-snapshot\8badc05"

NUM_RE = re.compile(r"(?<![\d.,])(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?")
APPX_RE = re.compile(r"^##\s+(?:\d+\.?\s*)?(?:appendix|glossary)\b", re.I)
HEADING_RE = re.compile(r"^#{1,6}\s")
KINDS = r"(?:vendor-reported|analyst-derived|filed|company-stated|measured-by-us)"
MONTHS = (r"(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|"
          r"Jul(?:y)?|Aug(?:ust)?|Sep(?:t(?:ember)?)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)")
DASH = r"[–—-]"

# spans inside which every token belongs to the category
SPAN_RULES = [
    ("date", re.compile(r"(?<!\d)\d{4}-\d{2}(?:-\d{2})?(?!\d)")),
    ("date", re.compile(MONTHS + r"\.?\s+\d{4}(?:\s*" + DASH + r"\s*" + MONTHS + r"\.?\s+\d{4})?")),
    ("date", re.compile(r"\d{1,2}\s+" + MONTHS + r"\.?\s+\d{4}")),
    ("date", re.compile(r"Q[1-4]\s+\d{4}")),
    ("tier", re.compile(r"\btiers?\s*\(?\s*\d(?:\s*" + DASH + r"\s*\d)?(?!\d)", re.I)),
    ("tier", re.compile(KINDS + r"(?:\s+inputs)?†?,?\s+\d(?:\s*" + DASH + r"\s*\d)?(?![\d%×x]|[.,]\d)")),
    ("tier", re.compile(r"(?<![\d.,])\d(?:\s*" + DASH + r"\s*\d)?\s+" + KINDS)),
    ("tier", re.compile(r",\s*\d(?:\s*" + DASH + r"\s*\d)?\)")),
    ("tier", re.compile(r"\(\s*[1-7]\s*\)")),
    ("tier", re.compile(r"(?<![\d.,])[1-7]\s+(?:strongest|weakest)")),
    ("rank", re.compile(r"(?:\brank|\brisk|\brule|#|\bNo\.)\s*\d+", re.I)),
    ("legal-ref", re.compile(r"(?:\bArt\.?|\bArticle|§|\bSection)\s*\d+(?:\.\d+)*")),
    ("form", re.compile(r"(?<![\d.,])\d+-[A-Z]{1,2}\b")),
    ("path-line", re.compile(r"(?<=\S):\d+(?:\s*" + DASH + r"\s*\d+)?")),
]
MASK_RULES = [
    ("hash", re.compile(r"\b(?=[0-9a-f]*[a-f])(?=[0-9a-f]*\d)[0-9a-f]{7,40}\b")),
    ("code", re.compile(r"`[^`]*`")),
]

LEAK_RE = re.compile(
    r"`?\bdocs/[^\s`|)]*`?"
    r"|[\w.\-/]+\.(?:md|csv|py)\b(?::\d+)?"
    r"|\bPass\s+\d+"
    r"|\bH\d+\b"
    r"|\bP1\d\b"
    r"|\bREV-[\w-]*"
    r"|\bBRIEF-\d+"
    r"|\bGAP-[A-Z]*"
    r"|\bIMG-\d+"
    r"|\bbiz-review[\w-]*"
    r"|-r2\b"
    r"|\bLane [A-F]\b"
    r"|\bwave \d+\b"
    r"|\bround \d+\b"
    r"|\b(?:first|second|third)[- ]round\b"
    r"|\b(?=[0-9a-f]*[a-f])(?=[0-9a-f]*\d)[0-9a-f]{7,40}\b",
    0)

VERDICT_PATTERNS = [
    r"\bwe recommend\b",
    r"\bI recommend\b",
    r"\brecommend(?:s|ation)?:?\s+(?:that\s+)?(?:you\s+)?(?:proceed|enter|invest|build|launch|pursue)",
    r"\bshould (?:invest|enter|proceed|build|launch|pursue|go ahead)\b",
    r"\bgo/no-go\b",
    r"\bno-go\b",
    r"\bgreen[- ]light",
    r"\bworth (?:pursuing|entering|building|investing)\b",
    r"\b(?:is|are) a (?:go|no-go)\b",
]
VERDICT_RE = re.compile("|".join(VERDICT_PATTERNS), re.I)
NEG_RE = re.compile(r"\b(?:no|not|never|nor|without)\b", re.I)

UNKNOWN_RE = re.compile(r"unknown\s*[—–-]+\s*(?:not in repo|checked)", re.I)
MODEL_RE = re.compile(r"claude-(?:opus|sonnet|haiku|fable)[\w.\-]*(?:\[1m\])?|<synthetic>", re.I)
ACRO_RE = re.compile(r"\b[A-Z]{2,}[a-z]?\b")

WORDNUM = {w: i for i, w in enumerate(
    "zero one two three four five six seven eight nine ten eleven twelve thirteen "
    "fourteen fifteen sixteen seventeen eighteen nineteen twenty".split())}
WORDNUM.update({"thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70,
                "eighty": 80, "ninety": 90, "hundred": 100})
WORDNUM_RE = re.compile(r"\b(" + "|".join(WORDNUM) + r")\b", re.I)

FORBIDDEN_RE = re.compile(r"STATE\.md|(?<![\w-])plan\.md|biz-review|-r2\b", re.I)
PATH_RE = re.compile(
    r"((?:docs/)?(?:findings|markets|competitors|customers|raw|method|sources)/[\w./\-*]+?\.(?:md|csv|json|txt|py))"
    r"(?::(\d+)(?:\s*[–—-]\s*:?(\d+))?)?")
ROWID_RE = re.compile(r"(?<![\w])([A-Z]{1,3}\d{1,3})(?![\w])")


def rd(path):
    with open(path, encoding="utf-8-sig", errors="replace") as f:
        return f.read()


def norm(tok):
    return tok.replace(",", "")


def tokens(text):
    """Number tokens (normalised) of a string, skipping letter-prefixed ones."""
    out = []
    for m in NUM_RE.finditer(text):
        pre = text[:m.start()]
        if re.search(r"[A-Za-z]-?$", pre):
            continue
        out.append(norm(m.group()))
    return out


# ---------------------------------------------------------------- brief split
def split_brief(lines):
    """Return (body_end_index_exclusive, appendix_start_index or None)."""
    for i, l in enumerate(lines):
        if APPX_RE.match(l):
            j = i - 1
            while j >= 0 and not lines[j].strip():
                j -= 1
            body_end = j if (j >= 0 and re.match(r"^\s*-{3,}\s*$", lines[j])) else i
            return body_end, i
    return len(lines), None


# ---------------------------------------------------------------- trace
def parse_trace(text):
    rows = []
    for ln, l in enumerate(text.splitlines(), 1):
        if "|" not in l:
            continue
        s = l.strip()
        if s.startswith("|"):
            s = s[1:]
        if s.endswith("|"):
            s = s[:-1]
        cells = [c.strip() for c in s.split("|")]
        if len(cells) < 5:
            continue
        if re.match(r"^:?-{2,}", cells[0]) or "brief line" in cells[1].lower():
            continue
        lines = set()
        for a, b in re.findall(r"(\d+)(?:\s*[–—-]\s*(\d+))?", cells[1]):
            a = int(a)
            b = int(b) if b else a
            lines.update(range(a, min(b, a + 200) + 1))
        rows.append({"tline": ln, "number": cells[0], "blines": lines,
                     "path": cells[2], "kind": cells[3], "date": cells[4], "raw": l})
    return rows


def cell_tokens(cell):
    """Digit groups of a trace number cell (rank/risk labels dropped)."""
    c = re.sub(r"\b(?:rank|risk|rule)\s+\d+", " ", cell, flags=re.I)
    return tokens(c)


class Snapshot:
    def __init__(self, root):
        self.root = root
        self.cache = {}

    def lines(self, rel):
        rel = rel.replace("\\", "/")
        if not rel.startswith("docs/"):
            rel = "docs/" + rel
        if rel not in self.cache:
            p = os.path.join(self.root, *rel.split("/"))
            self.cache[rel] = rd(p).splitlines() if os.path.isfile(p) else None
        return self.cache[rel]


def verify_row(row, snap):
    """Return (status, detail). status: verified | unverified | unresolvable."""
    path_cell = row["path"].replace("`", "")
    if FORBIDDEN_RE.search(path_cell):
        return "unresolvable", "forbidden cite"
    ms = list(PATH_RE.finditer(path_cell))
    if not ms:
        return "unresolvable", "no docs/ path"
    snap_lines = []
    cited = []
    for m in ms:
        rel, a, b = m.group(1), m.group(2), m.group(3)
        L = snap.lines(rel)
        if L is None:
            return "unresolvable", "file not in snapshot: " + rel
        if a:
            a = int(a)
            b = int(b) if b else a
            if b < a:
                b = a
            if a < 1 or b > len(L):
                return "unresolvable", "line out of range: %s:%s (file %d lines)" % (rel, m.group(2), len(L))
            for k in range(a, b + 1):
                snap_lines.append(L[k - 1])
            cited.append("%s:%d%s" % (rel, a, "-%d" % b if b != a else ""))
        else:
            rest = path_cell[m.end():]
            rid = ROWID_RE.search(rest)
            if not rid:
                return "unresolvable", "no line or row id: " + rel
            rid = rid.group(1)
            hit = None
            for k, l in enumerate(L, 1):
                if re.match(r"^\|\s*" + re.escape(rid) + r"\s*\|", l):
                    hit = k
                    break
            if hit is None:
                return "unresolvable", "row id %s not found in %s" % (rid, rel)
            snap_lines.append(L[hit - 1])
            cited.append("%s:%d (row %s)" % (rel, hit, rid))
    joined = "\n".join(snap_lines)
    have = set(norm(m.group()) for m in NUM_RE.finditer(joined))
    have.update(str(WORDNUM[w.lower()]) for w in WORDNUM_RE.findall(joined))
    # also accept letter-prefixed forms on the snapshot side (e.g. '$1B' fine,
    # 'FY2025' when the cell says FY2025 is skipped on both sides anyway)
    want = cell_tokens(row["number"])
    if want:
        missing = [t for t in want if t not in have]
    else:
        words = [w.lower() for w in WORDNUM_RE.findall(row["number"])]
        low = joined.lower()
        missing = [w for w in words
                   if not re.search(r"\b" + w + r"\b", low) and str(WORDNUM[w]) not in have]
        if not words:
            return "verified", "no digits or number words in cell; " + "; ".join(cited)
    if missing:
        return "unverified", "missing %s on %s :: %s" % (
            ", ".join(missing), "; ".join(cited), " / ".join(s.strip() for s in snap_lines)[:400])
    return "verified", "; ".join(cited)


# ---------------------------------------------------------------- classifier
def classify_line(line, tier_cols=()):
    """Return list of (token, category or None, start) for number tokens.

    Precedence: heading, ordinal, rownum, tier column, masks (hash, code),
    alnum, span rules in SPAN_RULES order, year.
    """
    cats = [None] * len(line)
    hm = re.match(r"^(#{1,6}\s+)(\d+(?:\.\d+)*)[.)]?\s", line)
    om = re.match(r"^(\s*)(\d+(?:\s*[–—-]\s*\d+)?)[.)]\s", line)
    rm = re.match(r"^\s*\|\s*(\d+)\s*\|", line)
    fixed = []
    if hm:
        fixed.append((hm.start(2), hm.end(2), "heading"))
    if om:
        fixed.append((om.start(2), om.end(2), "ordinal"))
    if rm:
        fixed.append((rm.start(1), rm.end(1), "rownum"))
    if tier_cols and line.strip().startswith("|"):
        pos = [k for k, ch in enumerate(line) if ch == "|"]
        for ci in range(len(pos) - 1):
            if ci in tier_cols:
                a, b = pos[ci] + 1, pos[ci + 1]
                if re.fullmatch(r"\s*[1-7](?:\s*[–—-]\s*[1-7])?\s*", line[a:b]):
                    fixed.append((a, b, "tier"))
    for a, b, cat in fixed:
        for k in range(a, b):
            cats[k] = cats[k] or cat
    for cat, rx in MASK_RULES:
        for m in rx.finditer(line):
            for k in range(m.start(), m.end()):
                cats[k] = cats[k] or cat
    for m in NUM_RE.finditer(line):
        if cats[m.start()] is None and re.search(r"[A-Za-z]-?$", line[:m.start()]):
            for k in range(m.start(), m.end()):
                cats[k] = "alnum"
    for cat, rx in SPAN_RULES:
        for m in rx.finditer(line):
            for k in range(m.start(), m.end()):
                cats[k] = cats[k] or cat
    out = []
    for m in NUM_RE.finditer(line):
        tok = m.group()
        cat = cats[m.start()]
        if cat is None and re.fullmatch(r"(?:199\d|20[0-4]\d)", tok):
            cat = "year"
        out.append((tok, cat, m.start()))
    return out


def tier_columns(lines):
    """Map line index -> set of pipe-gap indexes whose table header says 'tier'.

    Gap k is the text between the k-th and (k+1)-th '|' of the line. A header
    cell 'Kind, tier' is not a tier column (its cells hold 'filed 2' etc.,
    already covered by the kind rule).
    """
    res = {}
    cols = ()
    for i, l in enumerate(lines):
        s = l.strip()
        if not s.startswith("|"):
            cols = ()
            continue
        if i + 1 < len(lines) and re.match(r"^\s*\|?\s*:?-{2,}", lines[i + 1]):
            pos = [k for k, ch in enumerate(l) if ch == "|"]
            gaps = [l[pos[k] + 1:pos[k + 1]].strip().lower() for k in range(len(pos) - 1)]
            cols = tuple(k for k, c in enumerate(gaps) if "tier" in c and "kind" not in c)
            continue
        res[i] = cols
    return res


def check_numbers(lines, idx_range, trace_by_line):
    res = {"n": 0, "traced": 0, "excluded": [], "untraced": []}
    tcols = tier_columns(lines)
    for i in idx_range:
        line = lines[i]
        ln = i + 1
        pool = set()
        for r in trace_by_line.get(ln, []):
            pool.update(cell_tokens(r["number"]))
        for tok, cat, s in classify_line(line, tcols.get(i, ())):
            res["n"] += 1
            if norm(tok) in pool:
                res["traced"] += 1
            elif cat:
                res["excluded"].append((ln, tok, cat, line))
            else:
                res["untraced"].append((ln, tok, line))
    return res


# ---------------------------------------------------------------- acronyms
GLOSS_HEAD_RE = re.compile(r"glossary|abbreviation|acronym|\bterms\b|definitions", re.I)
GLOSS_COL_RE = re.compile(r"^(?:term|terms|acronym|abbreviation|abbr\.?)$", re.I)


def glossary_terms(lines, appx_start):
    """Acronyms a glossary defines.

    A glossary is (a) any section whose heading matches GLOSS_HEAD_RE, or
    (b) any table whose header's first cell is Term / Acronym / Abbreviation.
    Inside it, the first cell of each table row and the lead term of each
    '- TERM — meaning' / '- **TERM**: meaning' bullet count; the cell is split
    on ; / , and every acronym token in it is defined. Tables elsewhere in the
    appendix (sources, figure pairs) do not define anything.
    """
    terms = set()
    in_gloss = False
    in_gloss_table = False
    for i, l in enumerate(lines):
        if HEADING_RE.match(l):
            in_gloss = bool(GLOSS_HEAD_RE.search(l))
            in_gloss_table = False
            continue
        st = l.strip()
        cell = None
        if st.startswith("|"):
            cells = [c.strip() for c in st.strip("|").split("|")]
            is_header = i + 1 < len(lines) and re.match(r"^\s*\|?\s*:?-{2,}", lines[i + 1])
            if is_header:
                in_gloss_table = bool(cells and GLOSS_COL_RE.match(cells[0].replace("*", "")))
                continue
            if cells and re.match(r"^:?-{2,}", cells[0]):
                continue
            if in_gloss or in_gloss_table:
                cell = cells[0]
        else:
            if not st:
                in_gloss_table = False
            # a bold-only line such as '**Glossary**' opens a glossary like a heading
            if re.match(r"^\*\*[^*]+\*\*:?$", st):
                in_gloss = bool(GLOSS_HEAD_RE.search(st))
                continue
            if in_gloss:
                bm = re.match(r"^\s*[-*]\s+(\*\*[^*]+\*\*|[^—–:]+?)\s*[—–:]", l)
                if bm:
                    # every bold term on the bullet line counts ('**A**: x. **B**: y.')
                    bolds = re.findall(r"\*\*([^*]+)\*\*", l)
                    cell = ";".join(bolds) if bolds else bm.group(1)
        if cell:
            for part in re.split(r"[;/,]", cell.replace("*", "")):
                for a in ACRO_RE.findall(part):
                    terms.add(a)
                    if a.endswith("s"):
                        terms.add(a[:-1])
    return terms


def acronyms(lines, body_end, appx_start):
    body = "\n".join(lines[:body_end])
    found = []
    for a in ACRO_RE.findall(body):
        if a not in found:
            found.append(a)
    gl = glossary_terms(lines, appx_start)
    undefined = []
    for a in found:
        base = a[:-1] if a[-1].islower() else a
        cands = {a, base}
        if any(c in gl for c in cands):
            continue
        inline = any(re.search(r"\(" + re.escape(c) + r"s?\)", body) or
                     re.search(r"\b" + re.escape(c) + r"s?\s+\(", body) for c in cands)
        if inline:
            continue
        undefined.append(a)
    return undefined


# ---------------------------------------------------------------- notes
def notes_overrides(text):
    n = 0
    on = False
    for l in text.splitlines():
        if HEADING_RE.match(l):
            on = "overrid" in l.lower()
            continue
        if on and re.match(r"^\s*(?:\d+[.)]|[-*])\s+\S", l):
            n += 1
    return n


# ---------------------------------------------------------------- main
def run_one(folder, snap):
    r = {}
    det = {}
    fp = {k: os.path.isfile(os.path.join(folder, k + ".md")) for k in ("brief", "notes", "trace")}
    pres = [k if v else "-" + k for k, v in fp.items()]
    brief = rd(os.path.join(folder, "brief.md")) if fp["brief"] else ""
    notes = rd(os.path.join(folder, "notes.md")) if fp["notes"] else ""
    trace = rd(os.path.join(folder, "trace.md")) if fp["trace"] else ""
    lines = brief.splitlines()
    body_end, appx = split_brief(lines)
    if fp["brief"] and appx is None:
        pres.append("no-appendix")
    r["files_present"] = " ".join(pres)
    r["body_words"] = sum(len(l.split()) for l in lines[:body_end])
    r["notes_words"] = len(notes.split())
    ids = []
    for m in MODEL_RE.findall(notes):
        if m not in ids:
            ids.append(m)
    r["notes_model_ids"] = " ".join(ids)
    r["notes_overrides"] = notes_overrides(notes)

    rows = parse_trace(trace)
    r["trace_rows"] = len(rows)
    counts = {"verified": 0, "unverified": 0, "unresolvable": 0}
    det["trace"] = []
    forb = 0
    for row in rows:
        if FORBIDDEN_RE.search(row["path"]):
            forb += 1
        st, info = verify_row(row, snap)
        counts[st] += 1
        if st != "verified":
            det["trace"].append((st, row, info))
    r["trace_verified"] = counts["verified"]
    r["trace_unverified"] = counts["unverified"]
    r["trace_unresolvable"] = counts["unresolvable"]
    r["forbidden_cites"] = forb

    by_line = {}
    for row in rows:
        for bl in row["blines"]:
            by_line.setdefault(bl, []).append(row)
    bn = check_numbers(lines, range(0, body_end), by_line)
    an = check_numbers(lines, range(appx, len(lines)) if appx is not None else range(0), by_line)
    r["body_numbers"] = bn["n"]
    r["body_numbers_traced"] = bn["traced"]
    r["body_numbers_excluded"] = len(bn["excluded"])
    r["body_numbers_untraced"] = len(bn["untraced"])
    r["appendix_numbers_untraced"] = len(an["untraced"])
    det["body"] = bn

    # nearest trace rows for untraced tokens (audit aid)
    det["near"] = {}
    for ln, tok, _ in bn["untraced"] + an["untraced"]:
        hits = [bl for bl, rs in by_line.items()
                if abs(bl - ln) <= 3 and bl != ln and any(norm(tok) in cell_tokens(x["number"]) for x in rs)]
        if hits:
            det["near"][(ln, tok)] = sorted(hits)

    leaks = []
    for i in range(body_end):
        for m in LEAK_RE.finditer(lines[i]):
            leaks.append((i + 1, m.group(), lines[i]))
    r["process_leak"] = len(leaks)
    det["leaks"] = leaks

    und = acronyms(lines, body_end, appx)
    r["acronyms_undefined"] = len(und)
    det["acr"] = und

    r["unknown_count"] = len(UNKNOWN_RE.findall(brief))
    r["unknown_body"] = sum(len(UNKNOWN_RE.findall(l)) for l in lines[:body_end])

    vp, vneg = [], []
    for i in range(body_end):
        for m in VERDICT_RE.finditer(lines[i]):
            pre = lines[i][max(0, m.start() - 30):m.start()]
            (vneg if NEG_RE.search(pre) else vp).append((i + 1, m.group(), lines[i]))
    r["verdict_push_hits"] = len(vp)
    det["verdict"] = vp
    det["verdict_neg"] = vneg
    det["body_end"] = body_end
    det["appx"] = appx
    det["an"] = an
    return r, det


COLS = ["key", "files_present", "body_words", "notes_words", "notes_model_ids", "notes_overrides",
        "trace_rows", "trace_verified", "trace_unverified", "trace_unresolvable", "forbidden_cites",
        "body_numbers", "body_numbers_traced", "body_numbers_excluded", "body_numbers_untraced",
        "appendix_numbers_untraced", "process_leak", "acronyms_undefined", "unknown_count",
        "unknown_body", "verdict_push_hits", "returns_match"]


def load_csv(path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def match_id(run_id, folder_name):
    return folder_name == run_id or folder_name.startswith(run_id + "-")


def short(s, n=160):
    s = s.strip()
    return s if len(s) <= n else s[:n - 1] + "…"


def detail_md(key, r, d):
    o = []
    o.append("## %s\n" % key)
    o.append("Body = brief lines 1–%d; appendix from line %s. Summary: %s\n" % (
        d["body_end"], (d["appx"] + 1) if d["appx"] is not None else "none",
        ", ".join("%s=%s" % (c, r.get(c, "")) for c in COLS[1:])))
    bn, an = d["body"], d["an"]
    o.append("### Untraced body numbers (%d)\n" % len(bn["untraced"]))
    for ln, tok, line in bn["untraced"]:
        near = d["near"].get((ln, tok))
        o.append("- L%d `%s`%s — %s" % (ln, tok, " (trace row on L%s)" % ",".join(map(str, near)) if near else "",
                                         short(line)))
    o.append("\n### Untraced appendix numbers (%d)\n" % len(an["untraced"]))
    for ln, tok, line in an["untraced"]:
        near = d["near"].get((ln, tok))
        o.append("- L%d `%s`%s — %s" % (ln, tok, " (trace row on L%s)" % ",".join(map(str, near)) if near else "",
                                         short(line)))
    o.append("\n### Excluded body tokens, by category (%d) — audit the classifier\n" % len(bn["excluded"]))
    bycat = {}
    for ln, tok, cat, line in bn["excluded"]:
        bycat.setdefault(cat, []).append("L%d:%s" % (ln, tok))
    for cat in sorted(bycat):
        o.append("- **%s** (%d): %s" % (cat, len(bycat[cat]), " ".join(bycat[cat])))
    bycat = {}
    for ln, tok, cat, line in an["excluded"]:
        bycat.setdefault(cat, []).append("L%d:%s" % (ln, tok))
    o.append("\nExcluded appendix tokens: " + "; ".join("%s %d" % (c, len(v)) for c, v in sorted(bycat.items())))
    o.append("\n### Trace rows not verified (%d)\n" % len(d["trace"]))
    for st, row, info in d["trace"]:
        o.append("- trace L%d [%s] `%s` (brief L%s) — %s" % (
            row["tline"], st, short(row["number"], 80),
            ",".join(map(str, sorted(row["blines"]))) or "?", short(info, 420)))
    o.append("\n### Undefined acronyms (%d)\n" % len(d["acr"]))
    o.append(", ".join(d["acr"]) or "none")
    o.append("\n### Process-leak hits (%d)\n" % len(d["leaks"]))
    for ln, hit, line in d["leaks"]:
        o.append("- L%d `%s` — %s" % (ln, hit, short(line)))
    o.append("\n### Verdict-push hits (%d); negated, not counted (%d)\n" % (len(d["verdict"]), len(d["verdict_neg"])))
    for ln, hit, line in d["verdict"]:
        o.append("- L%d `%s` — %s" % (ln, hit, short(line)))
    for ln, hit, line in d["verdict_neg"]:
        o.append("- (negated) L%d `%s` — %s" % (ln, hit, short(line)))
    o.append("")
    return "\n".join(o)


def main(argv=None):
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
    ap = argparse.ArgumentParser(description="Mechanical checks on brief bake-off runs.")
    ap.add_argument("runs", nargs="+", help="run folders")
    ap.add_argument("--snapshot", default=DEFAULT_SNAPSHOT)
    ap.add_argument("--map", dest="mapcsv")
    ap.add_argument("--returns")
    ap.add_argument("--out")
    ap.add_argument("--detail")
    a = ap.parse_args(argv)

    snap = Snapshot(a.snapshot)
    if not os.path.isdir(os.path.join(a.snapshot, "docs")):
        sys.exit("snapshot has no docs/: " + a.snapshot)
    mp = load_csv(a.mapcsv) if a.mapcsv else None
    rets = load_csv(a.returns) if a.returns else None

    results = []
    for folder in a.runs:
        folder = os.path.normpath(folder)
        name = os.path.basename(folder)
        key = name
        if mp is not None:
            hit = [m for m in mp if match_id(m["run_id"].strip(), name)]
            if not hit:
                sys.exit("run folder not in --map: " + name)
            key = hit[0]["letter"].strip()
        r, d = run_one(folder, snap)
        r["key"] = key
        if rets is not None:
            rr = [x for x in rets if match_id(x["run_id"].strip(), name)]
            if not rr:
                r["returns_match"] = "no return row"
            else:
                rr = rr[0]
                mism = []
                for col, mine in (("words", r["body_words"]), ("rows", r["trace_rows"]),
                                  ("unknowns", r["unknown_count"]), ("overrides", r["notes_overrides"])):
                    v = (rr.get(col) or "").strip().replace(",", "")
                    if v and v != str(mine):
                        mism.append("%s %s vs %s" % (col, v, mine))
                r["returns_match"] = "ok" if not mism else "; ".join(mism)
        else:
            r["returns_match"] = ""
        results.append((key, r, d))
    if mp is not None:
        results.sort(key=lambda x: x[0])

    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=COLS, lineterminator="\n")
    w.writeheader()
    for key, r, d in results:
        w.writerow({c: r.get(c, "") for c in COLS})
    if a.out:
        with open(a.out, "w", encoding="utf-8", newline="") as f:
            f.write(buf.getvalue())
    sys.stdout.write(buf.getvalue())
    if a.detail:
        with open(a.detail, "w", encoding="utf-8", newline="\n") as f:
            f.write("# check-runs detail\n\nMechanical columns only; they do not replace the judge's reading.\n\n")
            for key, r, d in results:
                f.write(detail_md(key, r, d) + "\n")


if __name__ == "__main__":
    main()
