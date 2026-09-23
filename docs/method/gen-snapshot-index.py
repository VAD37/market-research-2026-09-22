"""Generate the snapshot index: docs/method/snapshot-index.csv + snapshot-index.md.

Set 2026-09-24 (user: "build ledger, snapshot index ... include word tokens to help
agents guess how much it should split agents and task"). Outputs are generated files:
never hand-edit them; fix this script or its inputs and re-run.

    python docs/method/gen-snapshot-index.py [--budget 120000]

Inputs: docs/raw/*.md (YAML-ish header, first 45 lines), compiled folders
(markets, competitors, customers, findings), docs/method/orphan-audit-*.md verdict rows.
tokens_est = ceil(chars / 3.5) -- heuristic, not a tokenizer count.
"""
import csv, math, os, re, subprocess, sys, collections, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DOCS = os.path.join(ROOT, 'docs')
OUT_CSV = os.path.join(DOCS, 'method', 'snapshot-index.csv')
OUT_MD = os.path.join(DOCS, 'method', 'snapshot-index.md')
COMPILED = ['markets', 'competitors', 'customers', 'findings']
FIELDS = ['source', 'url_or_doc_id', 'published', 'pull_date', 'pull_method', 'tier', 'source_label']
LABELS = {'vendor-reported', 'analyst-derived', 'filed', 'company-stated', 'measured-by-us'}
LANES = {'a': 'A organic (GEO/AEO/LLMO)', 'b': 'B paid placement', 'c': 'C agentic commerce',
         'd': 'D manipulation', 'e': 'E measurement / proof', 'f': 'F transition evidence'}
DATE = re.compile(r'(20\d\d-\d\d-\d\d)')
BUDGET = 120000
MINKEY = 4  # lane-key groups under this many files fold into one row per lane ...
MINTOK = 15000  # ... unless they carry at least this many tokens
if '--budget' in sys.argv:
    BUDGET = int(sys.argv[sys.argv.index('--budget') + 1])


def read(p):
    return open(p, encoding='utf-8', errors='ignore').read()


def tok(chars):
    return int(math.ceil(chars / 3.5))


def raw_key(stem):
    parts = stem.split('-')
    if len(parts) < 2 or len(parts[0]) != 1:
        return '?'
    k = parts[1]
    if parts[0] == 'e' and k in ('case', 'market') and len(parts) > 2:
        k = k + '-' + parts[2]
    if parts[0] == 'f' and k in ('signal', 'roles', 'jobboards') and len(parts) > 2:
        k = k + '-' + parts[2]
    return k


def head_fields(text):
    head = '\n'.join(text.splitlines()[:45])
    out = {}
    for k in FIELDS:
        m = re.search(r'^[\s>*-]*\**' + k + r'\**\s*:\s*(.*)$', head, re.M | re.I)
        out[k] = m.group(1).strip().strip('"') if m else ''
    return out


def flags(h):
    f = []
    if not h['source']:
        f.append('no-header')
    t = h['tier'].split()[0].lower() if h['tier'] else ''
    if h['source'] and t in ('', 'n/a', 'mixed'):
        f.append('tier-' + (t or 'missing'))
    lab = h['source_label'].split()[0].lower().strip(',;') if h['source_label'] else ''
    if h['source'] and lab not in LABELS:
        f.append('label-' + (lab or 'missing'))
    return ';'.join(f)


def verdicts():
    v = {}
    for f in os.listdir(os.path.join(DOCS, 'method')):
        if not f.startswith('orphan-audit-'):
            continue
        for line in read(os.path.join(DOCS, 'method', f)).splitlines():
            cells = [c.strip().strip('`') for c in line.strip().strip('|').split('|')]
            if len(cells) >= 2 and re.match(r'^[a-f]-', cells[0]):
                stem = os.path.basename(cells[0])[:-3] if cells[0].endswith('.md') else os.path.basename(cells[0])
                cell = cells[1].lower()
                v[stem] = next((k for k in ('not briefable', 'compiled', 'covered', 'superseded') if k in cell),
                               cell[:20]).replace(' ', '-')
    return v


def main():
    head = subprocess.run(['git', '-C', ROOT, 'log', '-1', '--format=%h', '--', 'docs/raw'] + ['docs/' + d for d in COMPILED],
                          capture_output=True, text=True).stdout.strip() or 'unknown'
    today = datetime.date.today().isoformat()
    rawdir = os.path.join(DOCS, 'raw')
    raw = sorted(f for f in os.listdir(rawdir) if f.endswith('.md') and f != 'CLAUDE.md')
    rtext = {f[:-3]: read(os.path.join(rawdir, f)) for f in raw}
    comp = []
    for d in COMPILED:
        for dp, _, fs in os.walk(os.path.join(DOCS, d)):
            comp += [os.path.join(dp, f) for f in fs if f.endswith('.md')]
    ctext = {p: read(p) for p in comp}
    # direct compiled citations, then transitive reach through cited raw files
    # a cite may name the full stem or the stem without its trailing pull date
    def pat(s):
        base = re.sub(r'-20\d\d-\d\d-\d\d$', '', s)
        return re.compile(re.escape(base) + r'(?:-20\d\d-\d\d-\d\d)?(?![a-z0-9-])' if base != s else re.escape(s))
    pats = {s: pat(s) for s in rtext}
    cites = {s: sum(1 for t in ctext.values() if pats[s].search(t)) for s in rtext}
    reach = {s for s, n in cites.items() if n}
    changed = True
    while changed:
        changed = False
        for s, t in rtext.items():
            if s not in reach and any(pats[s].search(rtext[p]) for p in reach if p != s):
                reach.add(s)
                changed = True
    # named only in method/ or sources/ (generated index and audit files excluded)
    other = ''
    for d in ('method', 'sources'):
        for dp, _, fs in os.walk(os.path.join(DOCS, d)):
            for f in fs:
                if f.endswith(('.md', '.csv')) and not f.startswith(('orphan-audit-', 'snapshot-index')):
                    other += read(os.path.join(dp, f))
    vd = verdicts()

    rows = []
    for f in raw:
        s = f[:-3]
        t = rtext[s]
        h = head_fields(t)
        m = DATE.search(s[-10:])
        rows.append(dict(
            path='docs/raw/' + f, layer='raw', lane=s[0] if s[1:2] == '-' else '?', key=raw_key(s),
            date=m.group(1) if m else '', words=len(t.split()), tokens_est=tok(len(t)),
            repull='y' if re.search(r'-repull\d*-', s) else '', img='y' if '-img-' in s else '',
            cited_by=cites[s], reach='direct' if cites[s] else ('raw-chain' if s in reach else ('method-only' if pats[s].search(other) else 'orphan')),
            audit=vd.get(s, ''), flags=flags(h),
            tier=h['tier'][:12], source_label=h['source_label'][:24], pull_method=h['pull_method'][:24],
            sections='', latest_dated=''))
    for p in sorted(comp):
        t = ctext[p]
        hs = re.findall(r'^(#{2,3}) (.+)$', t, re.M)
        dated = [x[1] for x in hs if DATE.search(x[1])]
        latest = max(dated, key=lambda x: DATE.search(x).group(1)) if dated else ''
        rel = os.path.relpath(p, ROOT).replace('\\', '/')
        rows.append(dict(
            path=rel, layer=rel.split('/')[1], lane='', key=os.path.basename(p)[:-3],
            date='', words=len(t.split()), tokens_est=tok(len(t)), repull='', img='',
            cited_by='', reach='', audit='', flags='', tier='', source_label='', pull_method='',
            sections='%d (%d dated)' % (len(hs), len(dated)), latest_dated=latest[:80]))

    with open(OUT_CSV, 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

    R = [r for r in rows if r['layer'] == 'raw']
    C = [r for r in rows if r['layer'] != 'raw']
    L = []
    a = L.append
    a('# Snapshot index')
    a('')
    a('Generated %s; evidence as of commit %s (last commit touching raw or compiled) by `python docs/method/gen-snapshot-index.py` -- never hand-edit; '
      're-run after any landing. Per-file rows: `snapshot-index.csv` (same folder). '
      'Tokens are `ceil(chars/3.5)`, a heuristic. Split budget: %s tokens per agent (`--budget N`).'
      % (today, head, f'{BUDGET:,}'))
    a('')
    a('Staleness: if `git log -1 --format=%h -- docs/raw docs/markets docs/competitors docs/customers docs/findings` '
      'differs from that commit, or `git status` shows changes there, re-run.')
    a('')
    a('## Layers')
    a('')
    a('| layer | files | words | tokens_est | agents at budget |')
    a('|---|---|---|---|---|')
    for layer in ['raw'] + COMPILED:
        s = [r for r in rows if r['layer'] == layer]
        tk = sum(r['tokens_est'] for r in s)
        a('| %s | %d | %s | %s | %d |' % (layer, len(s), f"{sum(r['words'] for r in s):,}", f'{tk:,}',
                                          math.ceil(tk / BUDGET)))
    a('')
    a('## Raw by lane')
    a('')
    a('| lane | files | words | tokens_est | agents at budget | orphan | repull | img | flagged |')
    a('|---|---|---|---|---|---|---|---|---|')
    for ln in sorted(set(r['lane'] for r in R)):
        s = [r for r in R if r['lane'] == ln]
        tk = sum(r['tokens_est'] for r in s)
        a('| %s | %d | %s | %s | %d | %d | %d | %d | %d |' % (
            LANES.get(ln, ln), len(s), f"{sum(r['words'] for r in s):,}", f'{tk:,}', math.ceil(tk / BUDGET),
            sum(r['reach'] == 'orphan' for r in s), sum(bool(r['repull']) for r in s),
            sum(bool(r['img']) for r in s), sum(bool(r['flags']) for r in s)))
    a('')
    a('## Raw by lane x key')
    a('')
    a('Key = second name segment (`<lane>-<key>-...`); e-case, e-market, f-signal, f-roles, f-jobboards '
      'take the third. Select files with `ls docs/raw/<lane>-<key>-*`.')
    a('')
    a('| lane-key | files | tokens_est | dates | orphan |')
    a('|---|---|---|---|---|')
    g = collections.defaultdict(list)
    for r in R:
        g[r['lane'] + '-' + r['key']].append(r)
    small = collections.defaultdict(list)
    for k in list(g):
        if len(g[k]) < MINKEY and sum(r['tokens_est'] for r in g[k]) < MINTOK:
            small[k[0]].append(k)
            g['%s-other (%d keys)' % (k[0], 0)] = []
            del g[k]
    for k in [k for k in g if k.endswith('(0 keys)')]:
        del g[k]
    for ln, ks in small.items():
        g['%s-other (%d small keys)' % (ln, len(ks))] = [r for r in R if r['lane'] + '-' + r['key'] in ks]
    for k in sorted(g, key=lambda k: (k[0], 'other' in k, -sum(r['tokens_est'] for r in g[k]))):
        s = g[k]
        ds = sorted(set(r['date'] for r in s if r['date']))
        a('| %s | %d | %s | %s | %d |' % (k, len(s), f"{sum(r['tokens_est'] for r in s):,}",
                                          (ds[0] + (' .. ' + ds[-1] if ds[-1] != ds[0] else '')) if ds else '',
                                          sum(r['reach'] == 'orphan' for r in s)))
    a('')
    a('## Compiled files')
    a('')
    a('Dated sections stack on older text without supersede notes; read the latest dated section as '
      'the current reading and check earlier sections for the figure it replaces.')
    a('')
    a('| file | words | tokens_est | sections | latest dated section |')
    a('|---|---|---|---|---|')
    prof = [r for r in C if r['layer'] == 'competitors' and not r['path'].endswith('INDEX.md')]
    a('| `competitors/*.md` (%d profiles, per-file in CSV) | %s | %s | 10-11 each (%d with a dated section) | |' % (
        len(prof), f"{sum(r['words'] for r in prof):,}", f"{sum(r['tokens_est'] for r in prof):,}",
        sum(not r['sections'].endswith('(0 dated)') for r in prof)))
    for r in [r for r in C if r not in prof]:
        a('| `%s` | %s | %s | %s | %s |' % (r['path'][5:], f"{r['words']:,}", f"{r['tokens_est']:,}",
                                           r['sections'], r['latest_dated'].replace('|', '/')))
    a('')
    a('## Coverage and flags')
    a('')
    cnt = collections.Counter(r['reach'] for r in R)
    a('Raw reach: direct compiled cite %d, via another cited raw %d, named only in method/ or sources/ %d, '
      'orphan %d (of %d). Orphan = none of those; audit verdicts in `orphan-audit-*.md`.'
      % (cnt['direct'], cnt['raw-chain'], cnt['method-only'], cnt['orphan'], len(R)))
    av = collections.Counter(r['audit'] for r in R if r['audit'])
    if av:
        a('Audit verdicts: ' + ', '.join('%s %d' % kv for kv in sorted(av.items())) + '.')
    a('')
    fl = [r for r in R if r['flags']]
    fc = collections.Counter(x for r in fl for x in r['flags'].split(';'))
    a('Header flags on %d files (per-file in CSV `flags`): ' % len(fl)
      + ', '.join('%s %d' % kv for kv in fc.most_common()) + '. Labels outside the five kinds '
      '(vendor-reported, analyst-derived, filed, company-stated, measured-by-us) are flagged; '
      '`n/a` and `mixed` mark tables and censuses that aggregate several sources.')
    a('')
    nh = [r['path'][9:] for r in fl if 'no-header' in r['flags']]
    if nh:
        a('No header at all: ' + ', '.join('`%s`' % x for x in nh) + '.')
        a('')
    with open(OUT_MD, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write('\n'.join(L))
    print('wrote', OUT_CSV, len(rows), 'rows;', OUT_MD, len(L), 'lines')


if __name__ == '__main__':
    main()
