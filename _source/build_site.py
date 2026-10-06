"""Build site/adbms/ — Papermorph-styled static exam book from exam/ notes."""
import json, re, html, pathlib

ROOT = pathlib.Path('.')
EXAM = ROOT / 'exam'
SITE = ROOT / 'site' / 'adbms'
SRC = ROOT / '_source'

def esc(s):
    return html.escape(s, quote=False)

def inline(s):
    s = esc(s)
    s = re.sub(r'`([^`\n]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\*\*([^\n*]+)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<!\w)\*([^*\n]+)\*(?!\w)', r'<em>\1</em>', s)
    return s

def is_sep(line):
    cells = [c.strip() for c in line.strip().strip('|').split('|')]
    return bool(cells) and all(re.fullmatch(r':?-{2,}:?', c or '---') for c in cells)

SPECIAL = [
    ('**Checkpoint', 'checkpoint', 'Check'),
    ('**Wrap (3 steps):**', 'wrap', 'Wrap'),
    ('**Hooks:**', 'hooks', 'Memory hooks'),
    ('**Trap:**', 'trap', 'Trap'),
    ('**Read:**', 'read', 'Read'),
    ('**You must be able to produce:**', 'produce', 'Produce'),
]

def blocks(lines):
    out, i, n = [], 0, len(lines)
    paras, ul, ol = [], [], []
    def flush_p():
        if paras:
            txt = ' '.join(paras); paras.clear()
            for prefix, cls, tag in SPECIAL:
                if txt.startswith(prefix):
                    body = txt[len(prefix):].lstrip(': ').strip()
                    out.append(f'<div class="callout {cls}"><b class="tag">{tag}</b>{inline(body)}</div>')
                    return
            if txt.startswith('*External-source'):
                out.append(f'<p class="prov"><em>{inline(txt[1:])}</em></p>')
                return
            out.append(f'<p>{inline(txt)}</p>')
    def flush_list():
        if ul: out.append('<ul>' + ''.join(f'<li>{inline(x)}</li>' for x in ul) + '</ul>'); ul.clear()
        if ol: out.append('<ol>' + ''.join(f'<li>{inline(x)}</li>' for x in ol) + '</ol>'); ol.clear()
    while i < n:
        line = lines[i].rstrip()
        if not line.strip():
            flush_p(); flush_list(); i += 1; continue
        if re.match(r'^---+$', line.strip()):
            flush_p(); flush_list(); out.append('<hr>'); i += 1; continue
        m = re.match(r'^(#{1,4})\s+(.*)$', line)
        if m:
            flush_p(); flush_list()
            lvl = len(m.group(1))
            out.append(f'<h{lvl}>{inline(m.group(2))}</h{lvl}>'); i += 1; continue
        if line.lstrip().startswith('|') and i + 1 < n and is_sep(lines[i + 1]):
            flush_p(); flush_list()
            head = [c.strip() for c in line.strip().strip('|').split('|')]
            out.append('<div class="tscroll"><table><thead><tr>' + ''.join(f'<th>{inline(c)}</th>' for c in head) + '</tr></thead><tbody>')
            i += 2
            while i < n and lines[i].lstrip().startswith('|'):
                cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                out.append('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in cells) + '</tr>')
                i += 1
            out.append('</tbody></table></div>')
            continue
        m = re.match(r'^\s*[-*]\s+(.*)$', line)
        if m:
            flush_p(); ul.append(m.group(1)); i += 1; continue
        m = re.match(r'^\s*\d+[.)]\s+(.*)$', line)
        if m:
            flush_p(); ol.append(m.group(1)); i += 1; continue
        paras.append(line.strip()); i += 1
    flush_p(); flush_list()
    return '\n'.join(out)

def md_file(path):
    return blocks(pathlib.Path(path).read_text(encoding='utf-8').splitlines())

# ---------------- MCQ data ----------------
boss = json.loads((SRC / 'bossrush_mcqs.json').read_text(encoding='utf-8'))
gpt = json.loads((SRC / 'chatgpt_quizzes.json').read_text(encoding='utf-8'))
boss_fix = [
    ('mixed','P1'),('mixed','P1'),('U2-4','P0'),('U2-5','P0'),('U2-6','P0'),
    ('U2-1','P0'),('U2-9','P1'),('U2-9','P1'),('U3-3','P0'),('U3-3','P0'),
    ('U3-3','P0'),('U3-5','P0'),('U3-6','P0'),('U3-6','P1'),('U4-7','P0'),
    ('U4-8','P0'),('U4-9','P1'),('U4-2','P0'),('U4-4','P0'),('U4-4','P1'),
    ('U2-13','P0'),('U2-13','P0'),('U3-9','P0'),('U3-12','P0'),('U5-4','P1'),
    ('U4-11','P0'),('U4-12','P0'),('U5-7','P0'),('U5-6','P0'),('U1-5','P0'),
    ('U1-7','P0'),('U1-8','P0'),
]
gpt_tags = [
    ('U1-3','P0'),('U1-2','P1'),('U1-5','P0'),('U1-5','P1'),('U1-7','P0'),
    ('U1-8','P0'),('U2-4','P0'),('U2-6','P0'),('U2-13','P0'),('U2-14','P1'),
    ('U3-3','P0'),('U3-6','P0'),('U3-12','P0'),('U4-2','P0'),('U4-4','P0'),
    ('U4-7','P0'),('U4-10','P1'),('U5-1','P0'),('U5-6','P0'),('mixed','P1'),
    ('mixed','P1'),('mixed','P0'),
]
MCQS = []
for i, m in enumerate(boss):
    topic, pri = boss_fix[i]
    unit = topic.split('-')[0] if '-' in topic else 'mixed'
    MCQS.append({'id': f'Q{89+i}', 'topic': topic, 'unit': unit, 'pri': pri,
                 'text': m['q'], 'opts': m['options'], 'ans': m['ans'],
                 'why': m['why'], 'whyNot': None,
                 'hint': f'Recall the {topic} notes (priority {pri}) — answer from memory first.'})
for i, m in enumerate(gpt):
    topic, pri = gpt_tags[i]
    unit = topic.split('-')[0] if '-' in topic else 'mixed'
    MCQS.append({'id': f'Q{121+i}', 'topic': topic, 'unit': unit, 'pri': pri,
                 'text': m['q'], 'opts': m['opts'], 'ans': m['a'],
                 'why': m['why'], 'whyNot': m['whyWrong'],
                 'hint': 'Not this: ' + m['whyWrong']})
BY_ID = {m['id']: m for m in MCQS}

QUICK = {
    1: ['Q121', 'Q122', 'Q89'], 2: ['Q123', 'Q124', 'Q118'], 3: ['Q125', 'Q126', 'Q119'],
    4: ['Q91', 'Q92', 'Q127'], 5: ['Q129', 'Q130', 'Q110'], 6: ['Q141'],
    7: ['Q97', 'Q98', 'Q131'], 8: ['Q100', 'Q101', 'Q132'], 9: ['Q111', 'Q112', 'Q133'],
    10: ['Q103', 'Q107', 'Q134'], 11: ['Q114', 'Q137', 'Q117'], 12: ['Q90', 'Q140', 'Q142'],
}

(SITE).mkdir(parents=True, exist_ok=True)
(SITE / 'quizzes.js').write_text(
    'window.MCQS = ' + json.dumps(MCQS, ensure_ascii=False, indent=1) +
    ';\nwindow.MCQ_BY_ID = {};\nwindow.MCQS.forEach(q => window.MCQ_BY_ID[q.id] = q);\n',
    encoding='utf-8')
print('mcqs:', len(MCQS))

# ---------------- .md reference resolver: inline <details> if small, link if huge ----------------
# .md reference -> nice site page (fall back to the raw .md file URL)
DOCS = {
    'memory-hooks.md': 'mem.html',
    'memorization-techniques.md': 'mem.html',
    'final-cram.md': 'cram.html',
    'ultra-short-notes.md': 'cram.html',
    'question-bank.md': 'written.html',
    'revision-plan.md': 'plan.html',
    'answer-voices.md': 'voices.html',
    'test-details.md': 'test.html',
    'write-memorize-skip.md': 'wms.html',
    'chapter-notes/unit-1.md': 'docs/unit-1.html',
    'chapter-notes/unit-2.md': 'docs/unit-2.html',
    'chapter-notes/unit-3.md': 'docs/unit-3.html',
    'chapter-notes/unit-4.md': 'docs/unit-4.html',
    'chapter-notes/unit-5.md': 'docs/unit-5.html',
    'diagrams-and-mental-models.md': 'docs/diagrams.html',
    'formulas.md': 'docs/formulas.html',
    'comparisons.md': 'docs/comparisons.html',
    'processes-and-algorithms.md': 'docs/processes.html',
    'common-mistakes.md': 'docs/mistakes.html',
    'definitions.md': 'docs/definitions.html',
    'answer-bank.md': 'docs/answers.html',
    'examples.md': 'docs/examples.html',
    'errata.md': 'docs/errata.html',
    'likely-questions.md': 'docs/likely.html',
    'flashcards.md': 'docs/cards.html',
    'weakness-tracker.md': 'docs/tracker.html',
    'master-study-guide.md': 'docs/guide.html',
    'learning-path-from-zero.md': 'docs/path.html',
}

def md_target(ref):
    """Resolve a .md reference to a site-relative URL (nice page preferred)."""
    m = re.fullmatch(r'mock-exam-(\d)(?:-key)?\.md', ref)
    if m:
        return f'mock{m.group(1)}.html'
    key = ref[6:] if ref.startswith('notes/') else ref
    if key in DOCS:
        return DOCS[key]
    cands = [EXAM / 'notes' / ref, EXAM / ref.lstrip('/')]
    if ref.startswith('notes/'):
        cands.insert(0, EXAM / ref)
    for p in cands:
        if p.is_file():
            return '../../exam/' + p.relative_to(EXAM).as_posix()
    return None

def md_link(ref):
    url = md_target(ref)
    if url:
        return f'<a href="{url}"><code>{esc(ref)}</code></a>'
    return f'<code>{esc(ref)}</code>'

def split_sections(text, pat):
    """Split markdown into (key, section-md) by heading pattern (pat matches the #'s; key = rest of line)."""
    parts = re.split(r'(?m)^' + pat + r'[^\n]*$', text)
    keys = re.findall(r'(?m)^' + pat + r'([^\n]*)$', text)
    return list(zip(keys, parts[1:]))

def section_md(path, key):
    """Return markdown of one headed section (heading + body) or None."""
    name = path.name
    if name.startswith('unit-'):
        pat = r'#{2,3} '
    elif name in ('memory-hooks.md', 'formulas.md', 'processes-and-algorithms.md',
                  'comparisons.md', 'diagrams-and-mental-models.md', 'common-mistakes.md'):
        pat = r'#{2,3} '
    elif name == 'final-cram.md':
        pat = r'#{1,3} '
    else:
        return None
    for k, body in split_sections(path.read_text(encoding='utf-8'), pat):
        if k.strip().split()[0].rstrip('.') == key:
            head = re.search(r'(?m)^' + pat + re.escape(k) + r'[^\n]*$', path.read_text(encoding='utf-8'))
            return ((head.group(0) + '\n' if head else '') + body).strip()
    return None

def refbox(title, inner_html, source_label):
    return (f'<details class="ref"><summary>📖 {title} <span class="dim">— from {esc(source_label)} (tap to expand)</span></summary>'
            f'<div class="content">{inner_html}</div></details>')

def expand_range(prefix, a, b):
    try:
        return [f'{prefix}{i}' for i in range(int(a), int(b) + 1)]
    except ValueError:
        return [f'{prefix}{a}']

EMBED_LIMIT = 3500  # rendered chars: below → inline <details>, above → file link

REF_STASH = []

def stash(html):
    REF_STASH.append(html)
    return f'\n\n@@REFBOX{len(REF_STASH) - 1}@@\n\n'

def stash_inline(html):
    REF_STASH.append(html)
    return f'@@REFIN{len(REF_STASH) - 1}@@'

def unstash(html):
    for i, h in enumerate(REF_STASH):
        html = html.replace(f'<p>@@REFBOX{i}@@</p>', h)
        html = html.replace(f'@@REFBOX{i}@@', h)
        html = html.replace(f'@@REFIN{i}@@', h)
    return html

def lesson_refs(text):
    """Replace file+section mentions with placeholder tokens (resolved after markdown render)."""
    REF_STASH.clear()
    def chapters(ref_file, unit, ra, rb=None):
        p = EXAM / 'notes' / ref_file
        keys = expand_range(f'U{unit}-', ra, rb or ra)
        secs = [section_md(p, k) for k in keys]
        if any(s is None for s in secs) or len(keys) > 5:
            return stash_inline(md_link(ref_file))
        html = blocks('\n'.join(secs).splitlines())
        if len(html) > EMBED_LIMIT * len(keys):
            return stash_inline(md_link(ref_file))
        return stash(refbox(f'Read: {ref_file} ({keys[0]}→{keys[-1]})' if len(keys) > 1 else f'Read: {ref_file} ({keys[0]})',
                      html, ref_file))

    def one(ref_file, key, label):
        p = EXAM / 'notes' / ref_file
        if not p.is_file():
            return md_link(ref_file)
        s = section_md(p, key)
        if s is None:
            return stash_inline(md_link(ref_file))
        html = blocks(s.splitlines())
        if len(html) > EMBED_LIMIT:
            return stash_inline(md_link(ref_file))
        return stash(refbox(f'{label}: {key}', html, f'{ref_file} §{key}'))

    # chapter ranges: `chapter-notes/unit-2.md` U2-1→U2-11 (→ or – separators)
    def sub_ch(m):
        rng = m.group(2)
        mm = re.match(r'U(\d+)-(\d+)\s*[→–-]\s*U\d+-(\d+)', rng or '')
        one_ = re.match(r'U(\d+)-(\d+)$', (rng or '').strip())
        if mm:
            return chapters(m.group(1), mm.group(1), mm.group(2), mm.group(3))
        if one_:
            return chapters(m.group(1), one_.group(1), one_.group(2))
        return stash_inline(md_link(m.group(1)))
    text = re.sub(r'`(chapter-notes/unit-\d\.md)`\s*(U\d+-\d+(?:\s*[→–-]\s*U\d+-\d+)?)?', sub_ch, text)

    # single sections: `file.md` §N / D2 / C3 / P4 / letter
    def sub_sec(m):
        ref_file, key = m.group(1), m.group(2)
        label = {'memory-hooks.md': 'Hooks', 'diagrams-and-mental-models.md': 'Diagram',
                 'final-cram.md': 'Cram', 'common-mistakes.md': 'Mistakes',
                 'formulas.md': 'Rule', 'processes-and-algorithms.md': 'Process'}.get(ref_file, 'Section')
        return one(ref_file, key, label)
    text = re.sub(r'`((?:memory-hooks|diagrams-and-mental-models|final-cram|common-mistakes|formulas|processes-and-algorithms)\.md)`\s*[§#]([A-Za-z0-9]+)',
                  sub_sec, text)
    # comparison ranges Cn–Cm: embed only if small, else file link
    def sub_cmp(m):
        ref_file, a, b = m.group(1), m.group(2)[1:], m.group(3)[1:]
        keys = expand_range('C', a, b)
        secs = [section_md(EXAM / 'notes' / ref_file, k) for k in keys]
        if any(s is None for s in secs):
            return stash_inline(md_link(ref_file))
        html = blocks('\n'.join(secs).splitlines())
        if len(html) > EMBED_LIMIT:
            return stash_inline(md_link(ref_file))
        return stash(refbox(f'Compare: {keys[0]}→{keys[-1]} ({len(keys)} tables)', html, ref_file))
    text = re.sub(r'`(comparisons\.md)`\s*(C\d+)\s*[→–-]\s*(C\d+)', sub_cmp, text)
    text = re.sub(r'`(comparisons\.md)`\s*(C\d+)(?!\s*[→–-])', lambda m: one(m.group(1), m.group(2), 'Compare'), text)
    # process ranges Pn–Pm → file link (procedures span large); singles embed-if-small
    text = re.sub(r'`(processes-and-algorithms\.md)`\s*(P\d+)\s*[→–-]\s*P\d+',
                  lambda m: stash_inline(md_link(m.group(1))), text)
    text = re.sub(r'`(processes-and-algorithms\.md)`\s*(P\d+)(?!\s*[→–-])',
                  lambda m: one(m.group(1), m.group(2), 'Process'), text)
    return text

def linkify_mdfiles(html):
    """Turn bare `<code>x.md</code>` mentions into links to the .md file when it exists."""
    def rep(m):
        ref = m.group(1)
        url = md_target(ref)
        if url:
            return f'<a href="{url}"><code>{esc(ref)}</code></a>'
        return m.group(0)
    return re.sub(r'<code>([\w./-]+\.md)</code>', rep, html)

# ---------------- STE-lite: plain-language pass (prose only) ----------------
STE_SWAPS = [
    (r'\butiliz(?:e|es|ing)\b', 'use'), (r'\bUtiliz(?:e|es|ing)\b', 'Use'),
    (r'\bdemonstrat(?:e|es|ing)\b', 'show'),
    (r'\bapproximately\b', 'about'), (r'\bApproximately\b', 'About'),
    (r'\bsufficient\b', 'enough'), (r'\bobtain\b', 'get'), (r'\bobtains\b', 'gets'),
    (r'\bfacilitat(?:e|es)\b', 'help'), (r'\bprior to\b', 'before'), (r'\bPrior to\b', 'Before'),
    (r'\bin order to\b', 'to'), (r'\bIn order to\b', 'To'),
    (r'\bdue to the fact that\b', 'because'), (r'\bcommence\b', 'start'),
    (r'\bin the event that\b', 'if'),
]
STE_PAIRS = []  # (before, after) html samples for the compliance metric
STE_PROT = {'e.g.': 'EGX', 'i.e.': 'IEX', 'etc.': 'ETX', 'vs.': 'VSX', 'Fig.': 'FGX'}

def ste_wordcount(s):
    return len(re.findall(r'\S+', s))

def ste_split(sent):
    """Split an over-long sentence at safe joints. Returns list of sentences."""
    out, changed = [sent], True
    while changed:
        changed = False
        nxt = []
        for s in out:
            if ste_wordcount(s) > 22:
                for pat, join in [(r';\s+', '. '), (r'\s+—\s+', '. '), (r',\s+which\s+', '. ')]:
                    parts = re.split(pat, s, maxsplit=1)
                    if len(parts) == 2 and all(ste_wordcount(p) > 3 for p in parts):
                        s = (parts[0].rstrip(' ,;') + join + parts[1][:1].upper() + parts[1][1:])
                        changed = True
                        break
            nxt.append(s)
        out = nxt
    return out

def ste_text(text):
    for k, v in STE_PROT.items():
        text = text.replace(k, v)
    for pat, rep in STE_SWAPS:
        text = re.sub(pat, rep, text)
    out = []
    for s in re.split(r'(?<=[.!?])\s+(?=[A-Z0-9"“])', text):
        out.extend(ste_split(s.strip()))
    text = ' '.join(s for s in out if s).replace('  ', ' ')
    for k, v in STE_PROT.items():
        text = text.replace(v, k)
    return re.sub(r'\.\s+([a-z])', lambda m: '. ' + m.group(1).upper(), text)

def ste_segment(html):
    """Apply STE to <p>/<li> prose (no nested block tags)."""
    def rep(m):
        tag, inner = m.group(1), m.group(2)
        if '<' in inner.replace('</strong>', '').replace('<strong>', '').replace('</em>', '').replace('<em>', '') \
                .replace('</code>', '').replace('<code>', '').replace('</a>', '') or '<a ' in inner:
            # has links or complex markup: swaps only, no sentence surgery
            for pat, r in STE_SWAPS:
                inner = re.sub(pat, r, inner)
            return f'<{tag}>{inner}</{tag}>'
        return f'<{tag}>{ste_text(inner)}</{tag}>'
    return re.sub(r'<(p|li)>(.*?)</\1>', rep, html, flags=re.S)

def ste_page(html):
    """STE prose outside <details> (exam wording inside answers/keys stays exact)."""
    parts = re.split(r'(<details.*?</details>)', html, flags=re.S)
    for i in range(0, len(parts), 2):
        parts[i] = ste_segment(parts[i])
    return ''.join(parts)

def ste_metric(html):
    ok = total = 0
    for m in re.finditer(r'<(?:p|li)>(.*?)</(?:p|li)>', html, re.S):
        inner = re.sub(r'<[^>]+>', '', m.group(1))
        for s in re.split(r'[.!?]\s+', inner):
            if ste_wordcount(s) >= 4:
                total += 1
                if ste_wordcount(s) <= 20:
                    ok += 1
    return ok, total

# ---------------- heading ids + TOC ----------------
def add_ids_toc(body):
    used, heads = set(), []
    segs = re.split(r'(<details.*?</details>)', body, flags=re.S)
    for i in range(0, len(segs), 2):
        def rep(m):
            lvl, inner = m.group(1), m.group(2)
            text = re.sub(r'<[^>]+>', '', inner).strip()
            slug = re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')[:60] or 'sec'
            base, k = slug, 2
            while slug in used:
                slug = f'{base}-{k}'
                k += 1
            used.add(slug)
            heads.append((lvl, text, slug))
            return f'<h{lvl} id="{slug}">{inner}</h{lvl}>'
        segs[i] = re.sub(r'<h([12])>(.*?)</h\1>', rep, segs[i])
    body = ''.join(segs)
    if len(heads) >= 4:
        toc = '<nav class="toc" aria-label="On this page"><b>On this page</b><ol>' + ''.join(
            f'<li class="l{lvl}"><a href="#{slug}">{esc(text)}</a></li>' for lvl, text, slug in heads) + '</ol></nav>'
        body = toc + body
    return body

# ---------------- page chrome ----------------
CHAPTERS = [
    (1, 'ch01.html', 'What databases are · three-level map', '20 min'),
    (2, 'ch02.html', 'ER modeling and mapping to tables', '20 min'),
    (3, 'ch03.html', 'Relational model, SQL, integrity', '20 min'),
    (4, 'ch04.html', 'Functional dependencies · 1NF→5NF ladder', '25 min'),
    (5, 'ch05.html', 'Storage, B+ trees and hashing', '20 min'),
    (6, 'ch06.html', 'Anomalies and schema-design guidelines', '15 min'),
    (7, 'ch07.html', 'Transactions, ACID, isolation levels', '20 min'),
    (8, 'ch08.html', 'Concurrency: serializability, 2PL, deadlock', '20 min'),
    (9, 'ch09.html', 'Recovery: deferred/immediate, WAL, checkpoints', '20 min'),
    (10, 'ch10.html', 'Fragmentation, 2PC, CAP/BASE, sharding', '25 min'),
    (11, 'ch11.html', 'MongoDB · Cassandra · Redis · Neo4j · vectors', '25 min'),
    (12, 'ch12.html', 'The 20-mark answer builder', '20 min'),
    (13, 'drills.html', 'Classification drills (sorters + multi-select)', '20 min'),
    (14, 'quiz.html', 'MCQ rapid-fire arena (54 verified)', '30 min'),
    (15, 'mock1.html', 'Mock exam 1 + key', '100 min'),
    (16, 'mock2.html', 'Mock exam 2 + key', '100 min'),
    (17, 'mock3.html', 'Mock exam 3 (hardest) + key', '100 min'),
    (18, 'cram.html', 'Final cram sheet + ultra-short notes', '15 min'),
    (19, 'ch19/index.html', '▶ Narrated: the normalization ladder (pilot)', '12 min'),
    (20, 'ch20/index.html', '▶ Narrated: ACID, the big four', '12 min'),
    (21, 'ch21/index.html', '▶ Narrated: CAP, the precise claim', '12 min'),
    (22, 'ch22/index.html', '▶ Narrated: 2PL + deadlock', '12 min'),
    (23, 'ch23/index.html', '▶ Narrated: recovery', '12 min'),
    (24, 'ch24/index.html', '▶ Narrated: B+ tree indexing', '12 min'),
    (25, 'ch25/index.html', '▶ Narrated: 2PC + fragmentation', '12 min'),
]

def rebase(html, base):
    if not base:
        return html
    def rep(m):
        url = m.group(2)
        if url.startswith(('http', '#', 'data:')):
            return m.group(0)
        if url.startswith('../'):
            return m.group(1) + '="' + base + url + '"'

        if url.startswith('docs/'):
            url = url[5:]
        else:
            url = '../' + url
        return m.group(1) + '="' + url + '"'
    return re.sub(r'(href|src)="([^"]+)"', rep, html)

def chrome(title, body, ch=None, base=''):
    body = linkify_mdfiles(body)
    body = add_ids_toc(body)
    nav = ''
    if ch:
        prev = next((c for c in CHAPTERS if c[0] == ch - 1), None)
        nxt = next((c for c in CHAPTERS if c[0] == ch + 1), None)
        parts = []
        if prev: parts.append(f'<a class="btn small quiet" href="{prev[1]}">← Ch {prev[0]}</a>')
        parts.append('<a class="btn small quiet" href="index.html#contents">Contents</a>')
        if nxt: parts.append(f'<a class="btn small go" href="{nxt[1]}">Ch {nxt[0]} →</a>')
        parts.append(f'<button id="donebtn" class="btn small quiet donebtn" onclick="markDone({ch})">Mark finished</button>')
        nav = '<div class="chapnav">' + ''.join(parts) + '</div>'
        _CH_UNIT = {1: 'Unit 1', 2: 'Unit 1', 3: 'Unit 1', 4: 'Unit 2', 5: 'Unit 2', 6: 'Unit 2',
             7: 'Unit 3', 8: 'Unit 3', 9: 'Unit 3', 10: 'Unit 4', 11: 'Unit 5',
             19: 'Unit 2', 20: 'Unit 3', 21: 'Unit 4'}
        crumb_unit = _CH_UNIT.get(ch, 'Exam arena')
        title_html = f'<div class="crumb"><a href="index.html#contents">ADBMS exam book</a> · {crumb_unit} · Chapter {ch}</div><h2 class="ptitle">{esc(title)}</h2>'
    else:
        title_html = f'<h2 class="ptitle">{esc(title)}</h2>'
    page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} — ADBMS Exam Book</title>
<link rel="stylesheet" href="style.css">
<script src="app.js"></script>
</head>
<body>
<header class="top">
<a class="home" href="index.html"><strong>ADBMS <i>Exam Book</i></strong></a>
<span class="prog" id="prog"></span>
</header>
<main class="wrap-page">
<noscript><style>.rv{{opacity:1!important;transform:none!important}}</style><p class="callout checkpoint"><b class="tag">JavaScript off</b>Reading works fully. Quick checks, drill grading, the MCQ arena and saved progress need JavaScript.</p></noscript>
{title_html}
{body}
{nav}
<p class="foot">Source: your MasterNotes (36 pp.) + verified quiz imports. First tries count — retries never overwrite them.</p>
</main>
<script>initContents(25);initReveal();</script>
</body>
</html>
"""
    return rebase(page, base) if base else page

# ---------------- lessons ----------------
lp = (EXAM / 'notes' / 'learning-path-from-zero.md').read_text(encoding='utf-8')
parts = re.split(r'(?m)^#{2,3} Lesson (\d+)', lp)
intro_md = parts[0].split('---')[0]
lessons = {}
for i in range(1, len(parts), 2):
    n = int(parts[i])
    body = parts[i + 1]
    nxt = re.search(r'(?m)^##? UNIT |\Z', body)
    title_m = re.match(r'\s*·\s*(.+?)\n', body)
    title = title_m.group(1).strip() if title_m else f'Lesson {n}'
    lessons[n] = (title, body)
print('lessons:', sorted(lessons))

LESSON_FILE = {n: f'ch{n:02d}.html' for n in range(1, 13)}
# Memory device per lesson (from memorization-techniques.md §3) — rendered as a
# callout box above each lesson's quick check.
MEMDEV = {
    1: '<b>External</b> = user views · <b>Conceptual</b> = blueprint · <b>Internal</b> = storage. '
       'Schema = structure, instance = state. Discriminator: physical = storage changes, logical = schema changes.',
    2: '<b>Many gets the key</b> (FK on the N side) · M:N needs a middleman table. '
       'Chunk 2-2-3: [entity→table · attrs→columns] [1:N · M:N] [multivalued · composite · weak]. '
       'Cardinality = how-many, participation = mandatory.',
    3: 'Families: <b>DDL Defines, DML Manipulates, DCL Controls, TCL Tames.</b> Execution order: '
       '<b>Fat Worms Gobble Hot Spaghetti Often</b> (FROM→WHERE→GROUP→HAVING→SELECT→ORDER). WHERE filters rows, HAVING filters groups.',
    4: 'Story: pizza sheet → anomalies are the disease, normal forms the cure. Ladder sentence + '
       '<b>3NF = OR, BCNF = ONLY</b>. Closure: show every step, box the set. ▶ <a href="ch19/index.html">Watch the narrated ladder</a>.',
    5: '<b>B for Between</b> (ranges, linked sorted leaves) · <b>H for Has-exactly</b> (equality buckets). '
       'Indexes = faster reads + storage &amp; write cost.',
    6: 'Insert = can\'t add · Update = copies drift · Delete = destroys facts. Cure = each fact in exactly one place.',
    7: '<b>A</b>ll-or-nothing · <b>C</b>orrect · <b>I</b>solated · <b>D</b>urable. Recovery guards A &amp; D, concurrency control guards I. '
       '▶ <a href="ch20/index.html">Watch the narrated ACID lesson</a>.',
    8: '<b>Grow = grab, shrink = surrender, never regrow.</b> Cycle in the graph = bad news. '
       'Deadlock = circular wait, caught by the wait-for graph. <b>2PL ≠ 2PC</b> (locking vs agreement).',
    9: '<b>Deferred = Delay → REDO only. Immediate = I need both → UNDO + REDO.</b> WAL = ship\'s log written '
       '<b>before</b> the cargo moves (log-first, always). Checkpoint = bookmark in the log.',
    10: 'CAP = at most two of C/A/P <b>during a partition</b> — never "any two at all times". '
       '2PC = Prepare, then Commit; any NO = global abort. Rows = σ = horizontal (UNION); columns = π = vertical (JOIN-on-key). '
       '▶ <a href="ch21/index.html">Watch the narrated CAP lesson</a>.',
    11: 'Table→<b>collection</b>, row→<b>document</b>. <b>Partition = place, clustering = order.</b> '
       '<b>HNSW = graph, IVF = clusters.</b> Pipeline: <b>My Great Shoes</b> ($match first). Cosine = angle.',
    12: 'Walk the palace before every long answer: <b>Door</b> (define) → <b>Hallway picture</b> (diagram) → '
       '<b>Rooms</b> (components) → <b>Kitchen demo</b> (example) → <b>Scales</b> (pros/cons) → <b>Guestbook</b> (conclusion).',
}

def linkify_q(html):
    """Turn bare Q-numbers into links: written bank anchors, or the MCQ arena."""
    def rep(m):
        n = int(m.group(1))
        if 89 <= n <= 142:
            return f'<a href="quiz.html">Q{n}</a>'
        return f'<a href="written.html#Q{n}">Q{n}</a>'
    return re.sub(r'\bQ(\d{1,3})\b', rep, html)

for n in range(1, 13):
    title, body = lessons[n]
    _raw = '<div class="content">\n' + unstash(blocks(lesson_refs(body).splitlines())) + '\n</div>'
    STE_PAIRS.append([_raw, None])
    html_body = ste_page(_raw)
    STE_PAIRS[-1][1] = html_body
    dev = (f'<div class="callout hooks"><b class="tag">Memory device — recite, don\'t reread</b>'
           f'{MEMDEV[n]} <a href="mem.html">All devices</a></div>')
    qids = QUICK[n]
    qc = '<h2>Quick check</h2><p class="psub">Answer from memory — first tries count.</p><div id="qc"></div>'
    qc += '<script src="quizzes.js"></script><script>' + \
        'const _qc = document.getElementById("qc");' + \
        ''.join(f' renderChoice(_qc, window.MCQ_BY_ID["{q}"]);' for q in qids) + '</script>'
    page = chrome(f'Lesson {n} · {title}', linkify_q(html_body + dev) + qc, ch=n)
    (SITE / LESSON_FILE[n]).write_text(page, encoding='utf-8')

# ---------------- drills ----------------
dt = (EXAM / 'notes' / 'classification-drills.md').read_text(encoding='utf-8')
dparts = re.split(r'(?m)^## Drill (\d+)', dt)
NORMALIZE = {'neither itself': 'neither (switch root)',
             'horizontal': 'horizontal-fragment', 'vertical': 'vertical-fragment',
             'vertical-rebuild': 'vertical-fragment', '2PC prepare phase': '2PC-phase',
             'global abort': '2PC-phase', 'AP choice': 'CAP-choice',
             'range': 'sharding-strategy', 'hash': 'sharding-strategy'}

def match_opt(value, options):
    v = value.strip()
    if v in options: return v
    vl = v.lower()
    for o in options:
        if vl in o.lower(): return o
    return options[0]

drill_html = ['<div class="content">',
              '<p>Sorter + multi-select drills in Papermorph format. <strong>Cover the answers, commit to a choice, then Check.</strong> First tries are saved per row.</p></div>']
for i in range(1, len(dparts), 2):
    dn = int(dparts[i]); sec = dparts[i + 1]
    sec = sec.split('## Score log')[0]
    title_m = re.match(r'\s*·\s*(.+?)\n', sec)
    dtitle = title_m.group(1).strip() if title_m else f'Drill {dn}'
    lines = sec.splitlines()
    # intro = lines before first table row / numbered item / **Answers
    intro_lines = []
    for ln in lines[1:]:
        if ln.lstrip().startswith('|') or re.match(r'^\s*\d+\.\s', ln) or ln.startswith('**Answers:**'):
            break
        intro_lines.append(ln)
    intro = blocks(intro_lines)
    backticked = re.findall(r'`([^`]+)`', '\n'.join(intro_lines))
    # table rows (skip header + separator)
    rows = []
    for ln in lines:
        if ln.lstrip().startswith('|') and not is_sep(ln):
            cells = [c.strip() for c in ln.strip().strip('|').split('|')]
            if cells and re.match(r'^\d+$', cells[0]):
                rows.append(cells)
    ans_m = re.search(r'\*\*Answers:\*\*\s*(.+)', sec)
    why_m = re.search(r'\*\*Why:\*\*\s*(.+)', sec)
    why = why_m.group(1).strip() if why_m else ''
    h = [f'<div class="drill" data-drill="{dn}" data-kind="{"sort" if (rows and ans_m and "→" in ans_m.group(1)) else "ms"}">', f'<h3>Drill {dn} · {esc(dtitle)}</h3>', intro]
    if rows and ans_m and '→' in ans_m.group(1):
        amap = {}
        for item in ans_m.group(1).split('·'):
            item = item.strip()
            m = re.match(r'(\d+)\s*→\s*(.+)', item)
            if m:
                val = re.sub(r'\s*\(.*$', '', m.group(2)).strip()
                val = NORMALIZE.get(val, val)
                amap[int(m.group(1))] = val
        options = backticked if backticked else sorted(set(amap.values()))
        h.append('<table><thead><tr><th>#</th><th>Item</th><th>Your bucket</th></tr></thead><tbody>')
        for r in rows:
            num = int(re.match(r'(\d+)', r[0]).group(1))
            prompt = r[1] if len(r) > 1 else ''
            ans = match_opt(amap.get(num, options[0]), options)
            opts = ''.join(f'<option value="{esc(o)}">{esc(o)}</option>' for o in ['— choose —'] + options)
            h.append(f'<tr><td>{num}</td><td>{inline(prompt)}</td><td data-cell><select data-ans="{esc(ans)}" aria-label="Bucket for item {num}">{opts}</select></td></tr>')
        h.append('</tbody></table>')
    else:
        # multi-select: numbered statements + T/F answers
        stmts = []
        for ln in lines:
            m = re.match(r'^\s*(\d+)\.\s+(.*)$', ln)
            if m: stmts.append((int(m.group(1)), m.group(2)))
        tmap = {}
        if ans_m:
            for item in ans_m.group(1).split('·'):
                item = item.strip()
                m = re.match(r'(\d+)\s+([TF])\b\s*(\(.*\))?', item)
                if m: tmap[int(m.group(1))] = (m.group(2), (m.group(3) or '').strip('() '))
        for num, st in stmts:
            ans, reason = tmap.get(num, ('T', ''))
            h.append(f'<div class="msrow" data-ans="{ans}"><div>{inline(st)}<div class="explain" style="display:none">{inline(reason)}</div></div>'
                     f'<div class="msbtns"><button data-v="T">True</button><button data-v="F">False</button></div></div>')
    if why:
        h.append(f'<details class="key"><summary>Why</summary><p>{inline(why)}</p></details>')
    h.append('<div class="toolbar"><button class="btn small go checkbtn">Check</button><span class="drillscore"></span></div></div>')
    drill_html.append('\n'.join(h))

drills_page = chrome('Classification drills', '\n'.join(drill_html) +
                     '<script>initDrills();</script>', ch=13)
(SITE / 'drills.html').write_text(drills_page, encoding='utf-8')
print('drills built')

# ---------------- quiz arena ----------------
arena = ('<div class="content"><p>All 54 verified MCQs. First tries count — hint-assisted answers are logged as hinted.</p>'
         '<p data-score></p></div>'
         '<div class="toolbar">'
         '<button class="fbtn on" data-unit="all">All</button>'
         '<button class="fbtn" data-unit="U1">Unit 1</button>'
         '<button class="fbtn" data-unit="U2">Unit 2</button>'
         '<button class="fbtn" data-unit="U3">Unit 3</button>'
         '<button class="fbtn" data-unit="U4">Unit 4</button>'
         '<button class="fbtn" data-unit="U5">Unit 5</button>'
         '<button class="fbtn" data-unit="mixed">Mixed</button>'
         '<button class="fbtn" id="weakonly">Weak only</button>'
         '<button class="fbtn" id="resetmcq">Reset scores</button>'
         '<span id="arenacount"></span></div>'
         '<div id="arena" data-next="1"></div>'
         '<div class="scorebar" data-score></div>'
         '<script src="quizzes.js"></script><script>initArena();updateScores();</script>')
(SITE / 'quiz.html').write_text(chrome('MCQ rapid-fire arena', arena, ch=14), encoding='utf-8')

# ---------------- mocks ----------------
for k in (1, 2, 3):
    paper = md_file(EXAM / f'mock-exam-{k}.md')
    key = md_file(EXAM / f'mock-exam-{k}-key.md')
    body = (f'<div class="content">{paper}</div>'
            f'<details class="key"><summary>Answer key — open only after finishing</summary>'
            f'<div class="content">{key}</div></details>')
    (SITE / f'mock{k}.html').write_text(chrome(f'Mock exam {k}', body, ch=14 + k), encoding='utf-8')

# ---------------- cram + plan ----------------
cram_md = (EXAM / 'notes' / 'final-cram.md').read_text(encoding='utf-8')
ultra = (EXAM / 'notes' / 'ultra-short-notes.md').read_text(encoding='utf-8')
ultra = re.sub(r'(?m)^# ', '## ', ultra, count=1)
cram_page = chrome('Final cram sheet',
                   f'<div class="content">{blocks((cram_md + "\n\n---\n\n" + ultra).splitlines())}</div>', ch=18)
(SITE / 'cram.html').write_text(cram_page, encoding='utf-8')
plan_page = chrome('Revision plans',
                   f'<div class="content">{md_file(EXAM / "revision-plan.md")}</div>')
(SITE / 'plan.html').write_text(plan_page, encoding='utf-8')
voices_page = chrome('Answer voices, verbs & time budgets',
                     f'<div class="content">{md_file(EXAM / "notes" / "answer-voices.md")}</div>')
(SITE / 'voices.html').write_text(voices_page, encoding='utf-8')
wms_page = chrome('Write · Memorize · Skip (Tier-S top 10)',
                  f'<div class="content">{md_file(EXAM / "notes" / "write-memorize-skip.md")}</div>')
(SITE / 'wms.html').write_text(wms_page, encoding='utf-8')
test_page = chrome('Test details (format hypothesis + choice strategy)',
                   f'<div class="content">{md_file(EXAM / "test-details.md")}</div>')
(SITE / 'test.html').write_text(test_page, encoding='utf-8')
mem_page = chrome('Memory: devices + hooks (one hub)',
                   f'<div class="content">{md_file(EXAM / "notes" / "memorization-techniques.md")}</div>'
                   f'<div class="content">{blocks(re.sub(r"(?m)^# ", "## ", (EXAM / "notes" / "memory-hooks.md").read_text(encoding="utf-8")).splitlines())}</div>')
(SITE / 'mem.html').write_text(mem_page, encoding='utf-8')


# ---------------- docs library (every linked .md as a nice page) ----------------
(SITE / 'docs').mkdir(exist_ok=True)
STE_DOCS = {'unit-1', 'unit-2', 'unit-3', 'unit-4', 'unit-5', 'diagrams',
            'comparisons', 'processes', 'mistakes', 'examples', 'likely'}
DOC_SOURCES = {
    'unit-1': ('Unit 1 — concepts &amp; modeling', 'notes/chapter-notes/unit-1.md'),
    'unit-2': ('Unit 2 — normalization &amp; storage', 'notes/chapter-notes/unit-2.md'),
    'unit-3': ('Unit 3 — transactions &amp; recovery', 'notes/chapter-notes/unit-3.md'),
    'unit-4': ('Unit 4 — distributed &amp; NoSQL', 'notes/chapter-notes/unit-4.md'),
    'unit-5': ('Unit 5 — stores &amp; indexing', 'notes/chapter-notes/unit-5.md'),
    'diagrams': ('Diagrams — draw these blind', 'notes/diagrams-and-mental-models.md'),
    'formulas': ('Formulas & rules', 'notes/formulas.md'),
    'comparisons': ('Comparisons — tables = marks', 'notes/comparisons.md'),
    'processes': ('Processes as flows', 'notes/processes-and-algorithms.md'),
    'mistakes': ('Common mistakes', 'notes/common-mistakes.md'),
    'definitions': ('Definitions (3-layer)', 'notes/definitions.md'),
    'answers': ('Answer bank', 'notes/answer-bank.md'),
    'examples': ('Examples', 'notes/examples.md'),
    'errata': ('Errata', 'notes/errata.md'),
    'likely': ('Likely questions', 'notes/likely-questions.md'),
    'tracker': ('Weakness tracker (your log)', 'weakness-tracker.md'),
    'guide': ('Master study guide', 'notes/master-study-guide.md'),
    'path': ('Learning path from zero', 'notes/learning-path-from-zero.md'),
}
for slug, (dtitle, rel) in DOC_SOURCES.items():
    body = '<div class="content">' + md_file(EXAM / rel) + '</div>'
    if slug in STE_DOCS:
        STE_PAIRS.append([body, None])
        body = ste_page(body)
        STE_PAIRS[-1][1] = body
    (SITE / 'docs' / f'{slug}.html').write_text(chrome(dtitle, body, base='../'), encoding='utf-8')
print('docs pages:', len(DOC_SOURCES))

# flashcards flip deck
fc_text = (EXAM / 'notes' / 'flashcards.md').read_text(encoding='utf-8')
fparts = re.split(r'(?m)^## (Deck [A-E])\b.*$', fc_text)
CARDS = []
for i in range(1, len(fparts), 2):
    deck = fparts[i][-1]
    for m in re.finditer(r'^\d+\.\s\*\*Q:\*\*\s*(.+?)\s*\*\*A:\*\*\s*(.+)$', fparts[i + 1], re.M):
        CARDS.append({'deck': deck, 'q': m.group(1).strip(), 'a': m.group(2).strip()})
for m in re.finditer(r'^\|\s*(T\d+)\s*\|\s*(.+?)\s*\|\s*\*\*(T|F)\*\*\s*(.*?)\|$', fc_text, re.M):
    CARDS.append({'deck': 'TF', 'q': m.group(2).strip() + ' — true or false?',
                  'a': ('TRUE. ' if m.group(3) == 'T' else 'FALSE. ') + m.group(4).strip('() ')})
print('flashcards parsed:', len(CARDS))

def fcard(i, c):
    return (
        f'<div class="fcard" id="C{i}" data-deck="{c["deck"]}" tabindex="0">'
        f'<div class="fq">{inline(c["q"])}</div><div class="fa">{inline(c["a"])}</div>'
        f'<div class="flip">tap / Enter to flip · then mark yourself</div>'
        f'<div class="qacts"><button class="btn small go cmark" data-v="1">✓ got it</button>'
        f'<button class="btn small quiet cmark" data-v="0.5">~ partial</button>'
        f'<button class="btn small quiet cmark" data-v="0">✗ missed</button></div></div>')

cards_page = chrome(
    'Flashcards (flip deck)',
    '<div class="content"><p>Say your answer out loud <b>before</b> flipping. Mark honestly — '
    'first marks only. Missed cards return in the <b>Missed only</b> filter.</p><p data-cscore></p></div>'
    '<div class="toolbar"><button class="fbtn on" data-cdeck="all">All</button>'
    + ''.join(f'<button class="fbtn" data-cdeck="{d}">Deck {d}</button>' for d in 'ABCDE')
    + '<button class="fbtn" data-cdeck="TF">True/False</button>'
    + '<button class="fbtn" id="cwrong">Missed only</button></div>'
    '<div id="cards">' + ''.join(fcard(i, c) for i, c in enumerate(CARDS)) + '</div>'
    '<div class="scorebar" data-cscore></div>'
    '<script>initCards();</script>', base='../')
(SITE / 'docs' / 'cards.html').write_text(cards_page, encoding='utf-8')

LIB = [('unit-1', 'Unit 1 notes', 'concepts &amp; modeling'), ('unit-2', 'Unit 2 notes', 'normalization &amp; storage'),
       ('unit-3', 'Unit 3 notes', 'transactions &amp; recovery'), ('unit-4', 'Unit 4 notes', 'distributed &amp; NoSQL'),
       ('unit-5', 'Unit 5 notes', 'stores &amp; indexing'), ('diagrams', 'Diagrams', 'draw these blind'),
       ('formulas', 'Formulas', 'rules &amp; criteria'), ('comparisons', 'Comparisons', 'tables = marks'),
       ('processes', 'Processes', 'ordered flows'), ('mistakes', 'Mistakes', 'what costs marks'),
       ('definitions', 'Definitions', '3-layer format'), ('answers', 'Answer bank', '2/5/10/20-mark models'),
       ('examples', 'Examples', 'concrete cases'), ('errata', 'Errata', 'traps &amp; clarifications'),
       ('likely', 'Likely questions', 'HIGH/MED/LOW'), ('cards', 'Flashcards', 'flip deck + T/F'),
       ('tracker', 'Weakness tracker', 'your error log'), ('guide', 'Study guide', 'priority map'),
       ('path', 'Learning path', '12 lessons from zero')]
lib_section = ('<section class="unit" style="--c:#f0b45a"><h2><span class="n">Library</span>'
               'Every source note, readable</h2><p class="sub">Full files in site styling with contents navigation. '
               'Quizzable pages (bank, arena, drills, cards) track first tries.</p><div class="grid">'
               + ''.join(f'<a class="ch" href="docs/{s}.html" style="--c:#f0b45a"><b>§</b><span>{t}<small>{d}</small></span></a>'
                         for s, t, d in LIB) + '</div></section>')
LIB_SECTION = lib_section

# STE compliance metric
_pre_ok = _pre_tot = _post_ok = _post_tot = 0
for _pre, _post in STE_PAIRS:
    a, b = ste_metric(_pre)
    _pre_ok += a; _pre_tot += b
    a, b = ste_metric(_post)
    _post_ok += a; _post_tot += b
print(f'STE: {100.0 * _pre_ok / max(1, _pre_tot):.1f}% -> {100.0 * _post_ok / max(1, _post_tot):.1f}% sentences <=20 words '
      f'({_post_tot} sentences, {len(STE_PAIRS)} pages)')

# ---------------- written answer bank ----------------
qb_text = (EXAM / 'notes' / 'question-bank.md').read_text(encoding='utf-8')
wblocks = re.split(r'(?m)^## (UNIT \d|MIXED / CROSS-UNIT TRAPS|SECTION J.*)$', qb_text)
WRITTEN = []
for i in range(1, len(wblocks), 2):
    sec = wblocks[i]
    if sec.startswith('SECTION J'):
        unit = 'mixed'
    elif sec.startswith('MIXED'):
        unit = 'mixed'
    else:
        unit = 'U' + sec.split()[-1]
    for m in re.finditer(
            r"^\*\*Q(\d+)\*\* \[([^·\]]+)·\s*([^·\]]+)·\s*([^·\]]+)·\s*([^\]]+)\]\s*([^\n]+)"
            r"\n- Expected:\s*(.+?)\n- Keywords:\s*(.+?)\n- Common wrong:\s*(.+?)(?=\n\n|\n\*\*Q|\Z)",
            wblocks[i + 1], re.M | re.S):
        qn, typ, topic, pri, diff, q, exp, kw, wrong = m.groups()
        wunit = topic.strip().split('-')[0] if '-' in topic else 'mixed'
        WRITTEN.append({'id': f'Q{qn}', 'type': typ.strip(), 'topic': topic.strip(),
                        'unit': wunit if wunit in ('U1', 'U2', 'U3', 'U4', 'U5') else 'mixed',
                        'pri': pri.strip(), 'diff': diff.strip(), 'q': q.strip(),
                        'exp': exp.strip(), 'kw': kw.strip(), 'wrong': wrong.strip()})
    # one-liner verdict format (e.g. TF): **Qn** [..] statement — verdict? **True**; reason.
    for m in re.finditer(
            r"^\*\*Q(\d+)\*\* \[([^·\]]+)·\s*([^·\]]+)·\s*([^·\]]+)·\s*([^\]]+)\]\s*([^\n]+?)\s*—\s*verdict\?\s*(\*\*.+?)$",
            wblocks[i + 1], re.M):
        qn = m.group(1)
        if any(w['id'] == f'Q{qn}' for w in WRITTEN):
            continue
        typ, topic, pri, diff, stmt, verdict = m.group(2, 3, 4, 5, 6, 7)
        wunit = topic.strip().split('-')[0] if '-' in topic else 'mixed'
        WRITTEN.append({'id': f'Q{qn}', 'type': typ.strip(), 'topic': topic.strip(),
                        'unit': wunit if wunit in ('U1', 'U2', 'U3', 'U4', 'U5') else 'mixed',
                        'pri': pri.strip(), 'diff': diff.strip(),
                        'q': stmt.strip() + ' — verdict?',
                        'exp': verdict.strip(),
                        'kw': '(see verdict)',
                        'wrong': 'The opposite verdict.'})
print('written questions parsed:', len(WRITTEN))

def written_card(w):
    return (
        f'<div class="qcard written" id="{w["id"]}" data-unit="{w["unit"]}" data-type="{w["type"]}" data-pri="{w["pri"]}">'
        f'<div class="qtags"><span class="qtag">{w["id"]} · {esc(w["topic"])}</span>'
        f'<span class="qtag">{esc(w["type"])}</span>'
        f'<span class="qtag {w["pri"].lower()}">{esc(w["pri"])}</span>'
        f'<span class="wprev qtag"></span></div>'
        f'<div class="qprompt">{inline(w["q"])}</div>'
        f'<details class="key"><summary>Think first — then reveal the model answer</summary>'
        f'<p><b>Expected:</b> {inline(w["exp"])}</p>'
        f'<p><b>Keywords (the marks):</b> {inline(w["kw"])}</p>'
        f'<p><b>Common wrong:</b> {inline(w["wrong"])}</p></details>'
        f'<div class="qacts"><button class="btn small go wmark" data-v="1">✓ Got it</button>'
        f'<button class="btn small quiet wmark" data-v="0">✗ Missed</button></div></div>')

wtypes = sorted(set(w['type'] for w in WRITTEN))
written_page = chrome(
    'Written answer bank (102)',
    '<div class="content"><p>Every written question with its model answer hidden. '
    'Answer aloud or on paper, reveal, then mark yourself — first marks only, like everything else here. '
    'MCQs live separately in the <a href="quiz.html">rapid-fire arena</a>.</p><p data-wscore></p></div>'
    '<div class="toolbar"><button class="fbtn on" data-wunit="all">All</button>'
    + ''.join(f'<button class="fbtn" data-wunit="U{i}">Unit {i}</button>' for i in range(1, 6))
    + '<button class="fbtn" data-wunit="mixed">Mixed</button>'
    + '<button class="fbtn" id="wwrong">Missed only</button></div>'
    '<div id="written">' + '\n'.join(written_card(w) for w in WRITTEN) + '</div>'
    '<div class="scorebar" data-wscore></div>'
    '<script>initWritten();</script>')
(SITE / 'written.html').write_text(written_page, encoding='utf-8')

# ---------------- index: cover + contents ----------------
# Unit names follow ADBMS_MasterNotes.docx (exactly 5 units). String entries are
# unit-notes docs cards; int entries are progress-tracked chapters. 'Exam arena'
# is infrastructure, not a unit. Narrated lessons sit inside their real units.
UNITS = [
    ('Database Concepts & Modeling', 'Database systems, ER modeling, SQL', '#f4a48c',
     [1, 2, 3, ('unit-1', 'Unit 1 notes', 'all 9 chapters, P0–P2 tagged')], 'unit'),
    ('Normalization, Storage & Indexing', 'FDs, the 1NF→5NF ladder, B+ trees, hashing', '#86c9e8',
     [4, 5, 6, 19, 24, ('unit-2', 'Unit 2 notes', 'all 14 chapters, P0–P2 tagged')], 'unit'),
    ('Transactions, Concurrency & Recovery', 'ACID, serializability, 2PL, WAL, checkpoints', '#f3c95c',
     [7, 8, 9, 20, 22, 23, ('unit-3', 'Unit 3 notes', 'all 12 chapters, P0–P2 tagged')], 'unit'),
    ('Distributed Databases & NoSQL', 'Fragmentation, 2PC, CAP/BASE, sharding', '#8fd6b0',
     [10, 21, 25, ('unit-4', 'Unit 4 notes', 'all 12 chapters, P0–P2 tagged')], 'unit'),
    ('NoSQL Stores & Indexing', 'Cassandra, Redis, Neo4j, vectors, cross-system indexing', '#e8a0c8',
     [11, ('unit-5', 'Unit 5 notes', 'all 14 chapters, P0–P2 tagged')], 'unit'),
    ('Exam arena', 'Answer builder, drills, MCQ arena, mocks, cram', '#bba8ee',
     [12, 13, 14, 15, 16, 17, 18], 'arena'),
]
chmap = {n: (f, t, m) for n, f, t, m in CHAPTERS}
units_html = []
_unit_no = 0
for uname, sub, color, nums, kind in UNITS:
    if kind == 'unit':
        _unit_no += 1
        tag = f'Unit {_unit_no}'
    else:
        tag = 'Arena'
    cards = []
    for n in nums:
        if isinstance(n, int):
            f, t, m = chmap[n]
            cards.append(f'<a class="ch" data-ch="{n}" id="ch{n:02d}" href="{f}" style="--c:{color}"><b>{n}</b><span>{esc(t)}<small>{m}</small></span></a>')
        else:
            s, title, desc = n
            cards.append(f'<a class="ch" href="docs/{s}.html" style="--c:{color}"><b>§</b><span>{esc(title)}<small>{esc(desc)}</small></span></a>')
    units_html.append(
        f'<section class="unit" style="--c:{color}"><h2><span class="n">{tag}</span>{esc(uname)}</h2>'
        f'<p class="sub">{esc(sub)}</p><div class="grid">{"".join(cards)}</div></section>')
units_html.append(LIB_SECTION)
intro_html = blocks(intro_md.splitlines())
index = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ADBMS Exam Book — pass tomorrow</title>
<meta name="description" content="Exam-night ADBMS study book: 12 lessons, sorter drills, 54-MCQ arena, 3 mocks, cram sheet.">
<link rel="stylesheet" href="style.css">
</head>
<body>
<section id="cover">
<p class="kicker">An exam-night study book</p>
<h1>ADBMS <i>Exam Book</i></h1>
<p class="lede">Twelve lessons from zero, sorter drills, a 54-question MCQ arena, three mock exams and a final cram sheet — everything scored by first tries, nothing by passive reading.</p>
<div class="acts">
<a class="btn go" href="#contents">Open the book →</a>
<a class="btn quiet" id="resume" hidden></a>
<a class="btn quiet" href="plan.html">Tonight's plan</a>
</div>
<div class="examline"><span id="countdown">Exam in <b>…</b></span><br>
<label>Exam at: <input type="datetime-local" id="examAt"></label></div>
<p class="meta" id="meta"></p>
</section>
<main id="contents">
<noscript><style>.rv{{opacity:1!important;transform:none!important}}</style></noscript>
<header class="top">
<a class="home" href="#book"><strong>ADBMS <i>Exam Book</i></strong></a>
<span class="prog" id="prog"></span>
<a class="back-shelf contents-back" href="plan.html" style="color:var(--dim);font-size:13px;text-decoration:none">Plan →</a>
</header>
<section class="unit"><h2><span class="n">How this book works</span>Read this first</h2>
<div class="content">{intro_html}</div>
<p class="sub">The output rule for every 10/20-mark answer: <strong>Define (5–7 lines) → diagram → components under headings → example → pros/cons → 3–4 line conclusion.</strong></p>
</section>
{''.join(units_html)}
<section class="unit"><h2><span class="n">Reference</span>Study infrastructure</h2>
<div class="grid">
<a class="ch" href="plan.html" style="--c:#f0b45a"><b>§</b><span>Revision plans<small>30m · 1h · 2h · 4h · final-30 · final-10</small></span></a>
<a class="ch" href="voices.html" style="--c:#f0b45a"><b>V</b><span>Answer voices &amp; verbs<small>time per mark · 7 verb engines · chunking</small></span></a>
<a class="ch" href="wms.html" style="--c:#f0b45a"><b>W</b><span>Write · Memorize · Skip<small>Tier-S top-10 boxes</small></span></a>
<a class="ch" href="test.html" style="--c:#f0b45a"><b>T</b><span>Test details<small>assumed format · pick sides · gaps</small></span></a>
<a class="ch" href="mem.html" style="--c:#f0b45a"><b>M</b><span>Memory hub<small>devices + hooks · discriminators</small></span></a>
<a class="ch" href="written.html" style="--c:#f0b45a"><b>W</b><span>Written answer bank<small>96 with hidden model answers</small></span></a>
</div></section>
<div style="height:60px"></div>
</main>
<script src="app.js"></script>
<script>initCover();initContents(25);initCountdown();initReveal();</script>
</body>
</html>
"""
(SITE / 'index.html').write_text(index, encoding='utf-8')
print('index built; chapters:', len(CHAPTERS))
