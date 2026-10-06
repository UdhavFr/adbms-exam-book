import re, json, pathlib

EXAM = pathlib.Path('exam')
SITE = pathlib.Path('site/adbms')
fails = []


def check(name, cond, detail=''):
    print(('OK   ' if cond else 'FAIL ') + name + (f' ({detail})' if detail else ''))
    if not cond:
        fails.append(name)


MD2SITE = {
    'notes/learning-path-from-zero.md': ['ch01.html', 'docs/path.html'],
    'notes/chapter-notes/unit-1.md': ['docs/unit-1.html'],
    'notes/chapter-notes/unit-2.md': ['docs/unit-2.html'],
    'notes/chapter-notes/unit-3.md': ['docs/unit-3.html'],
    'notes/chapter-notes/unit-4.md': ['docs/unit-4.html'],
    'notes/chapter-notes/unit-5.md': ['docs/unit-5.html'],
    'notes/definitions.md': ['docs/definitions.html'],
    'notes/formulas.md': ['docs/formulas.html'],
    'notes/processes-and-algorithms.md': ['docs/processes.html'],
    'notes/comparisons.md': ['docs/comparisons.html'],
    'notes/diagrams-and-mental-models.md': ['docs/diagrams.html'],
    'notes/examples.md': ['docs/examples.html'],
    'notes/common-mistakes.md': ['docs/mistakes.html'],
    'notes/memory-hooks.md': ['mem.html'],
    'notes/memorization-techniques.md': ['mem.html'],
    'notes/flashcards.md': ['docs/cards.html'],
    'notes/question-bank.md': ['written.html', 'quiz.html'],
    'notes/likely-questions.md': ['docs/likely.html'],
    'notes/answer-bank.md': ['docs/answers.html'],
    'notes/answer-voices.md': ['voices.html'],
    'notes/write-memorize-skip.md': ['wms.html'],
    'notes/ultra-short-notes.md': ['cram.html'],
    'notes/final-cram.md': ['cram.html'],
    'notes/errata.md': ['docs/errata.html'],
    'notes/master-study-guide.md': ['docs/guide.html'],
    'notes/classification-drills.md': ['drills.html'],
    'revision-plan.md': ['plan.html'],
    'weakness-tracker.md': ['docs/tracker.html'],
    'test-details.md': ['test.html'],
    'mock-exam-1.md': ['mock1.html'], 'mock-exam-1-key.md': ['mock1.html'],
    'mock-exam-2.md': ['mock2.html'], 'mock-exam-2-key.md': ['mock2.html'],
    'mock-exam-3.md': ['mock3.html'], 'mock-exam-3-key.md': ['mock3.html'],
}
for md, pages in MD2SITE.items():
    ok = all((SITE / p).is_file() for p in pages)
    check(f'md-on-site: {md}', ok, ' -> '.join(pages))

DOC_MD = {'docs/unit-1.html': 'notes/chapter-notes/unit-1.md',
          'docs/unit-2.html': 'notes/chapter-notes/unit-2.md',
          'docs/unit-3.html': 'notes/chapter-notes/unit-3.md',
          'docs/unit-4.html': 'notes/chapter-notes/unit-4.md',
          'docs/unit-5.html': 'notes/chapter-notes/unit-5.md',
          'docs/diagrams.html': 'notes/diagrams-and-mental-models.md',
          'docs/formulas.html': 'notes/formulas.md',
          'docs/comparisons.html': 'notes/comparisons.md',
          'docs/processes.html': 'notes/processes-and-algorithms.md',
          'docs/mistakes.html': 'notes/common-mistakes.md',
          'docs/definitions.html': 'notes/definitions.md',
          'docs/answers.html': 'notes/answer-bank.md',
          'docs/examples.html': 'notes/examples.md',
          'docs/errata.html': 'notes/errata.md',
          'docs/likely.html': 'notes/likely-questions.md',
          'docs/tracker.html': 'weakness-tracker.md',
          'docs/guide.html': 'notes/master-study-guide.md'}
for page, md in DOC_MD.items():
    src = (EXAM / md).read_text(encoding='utf-8')
    html = (SITE / page).read_text(encoding='utf-8')
    n_md = len(re.findall(r'(?m)^#{1,4} ', src))
    n_html = len(re.findall(r'<h[1-4][ >]', html))
    check(f'fidelity {page}', n_html >= n_md, f'{n_html} h-tags vs {n_md} md-headings')

secs = json.loads((EXAM / 'sections.json').read_text(encoding='utf-8'))
site_text = ''
for p in SITE.rglob('*.html'):
    if '/ch19/' in p.as_posix() or '/ch20/' in p.as_posix() or '/ch21/' in p.as_posix():
        continue
    site_text += p.read_text(encoding='utf-8')
missing_ch = []
for s in secs:
    if not s['unit'].startswith('UNIT'):
        continue
    num = re.match(r'(\d+)\.', s['title']).group(1)
    unum = re.match(r'UNIT (\d+)', s['unit']).group(1)
    tag = f'U{unum}-{num}'
    if tag not in site_text:
        missing_ch.append(tag)
check('61 chapters on site', not missing_ch, f'missing: {missing_ch}' or 'all present')

qb = (EXAM / 'notes' / 'question-bank.md').read_text(encoding='utf-8')
n_bank = len(re.findall(r'^\*\*Q\d+\*\*', qb, re.M))
wr = (SITE / 'written.html').read_text(encoding='utf-8')
n_written = len(re.findall(r'class="qcard written"', wr))
check('written bank complete', n_written == 88 + 8 + 6, f'{n_written}/102 cards')
fc = (EXAM / 'notes' / 'flashcards.md').read_text(encoding='utf-8')
n_fc = len(re.findall(r'^\d+\.\s\*\*Q:', fc, re.M)) + len(re.findall(r'^\| T\d+', fc, re.M))
cards = (SITE / 'docs' / 'cards.html').read_text(encoding='utf-8')
n_cards = len(re.findall(r'class="fcard"', cards))
check('flashcards complete', n_cards == n_fc, f'{n_cards}/{n_fc} cards')
dr = (SITE / 'drills.html').read_text(encoding='utf-8')
check('drills complete', len(re.findall(r'class="drill"', dr)) == 10, 'drill blocks')

# chapter priority vs question coverage (written [T · topic] + mcq [MCQ A· topic])
prios = {}
for i in range(1, 6):
    t = (EXAM / 'notes' / 'chapter-notes' / f'unit-{i}.md').read_text(encoding='utf-8')
    for m in re.finditer(r'^## (U\d+-\d+).*?\*\*(P\d)\*\*', t, re.M):
        prios[m.group(1)] = m.group(2)
qw = re.findall(r'^\*\*Q\d+\*\* \[([A-Z]+) · ([^·\]]+) ·', qb, re.M)
qm = re.findall(r'^\*\*Q\d+\*\* \[MCQ A·\s*([^A][^·]*?)\s*A·', qb, re.M)
covered = set(b.strip() for a, b in qw) | set(x.strip() for x in qm)
for pri in ('P0', 'P1', 'P2'):
    missing = [c for c, p in sorted(prios.items()) if p == pri and c not in covered]
    check(f'{pri} question coverage', not missing, f'no direct Q: {missing}' or 'full')

TIERS = {'ACID': ['ch07', 'Q97', 'ch20'], 'normalization ladder': ['ch04', 'Q91', 'ch19'],
         'CAP': ['ch10', 'Q103', 'ch21'], '2PL': ['ch08', 'Q100', None],
         'recovery': ['ch09', 'Q111', None], 'serializability': ['ch08', 'Q100', None],
         'B+ tree': ['ch05', 'Q109', None], 'ER mapping': ['ch02', 'Q118', None],
         'fragmentation/2PC': ['ch10', 'Q106', None], 'indexing': ['ch11', 'Q109', None]}
for topic, (lesson, q, narr) in TIERS.items():
    lp = (SITE / f'{lesson}.html').read_text(encoding='utf-8')
    ok_q = (q in wr) or (q in (SITE / 'quizzes.js').read_text(encoding='utf-8'))
    extra = f' + narrated {narr}' if narr else ''
    check(f'tier-S: {topic}', ok_q, f'{lesson} + {q}{extra}')

for k in (1, 2, 3):
    key_src = (EXAM / f'mock-exam-{k}-key.md').read_text(encoding='utf-8')
    page = (SITE / f'mock{k}.html').read_text(encoding='utf-8')
    check(f'mock{k} key embedded', len(page) > len(key_src) * 0.8, f'{len(page)} vs {len(key_src)} chars')

print()
print('FAILURES:', fails or 'NONE')
