import re, json, pathlib

EXAM = pathlib.Path('exam')
SITE = pathlib.Path('site/adbms')

# chapter -> priority from chapter-notes headings
prios = {}
for i in range(1, 6):
    t = (EXAM / 'notes' / 'chapter-notes' / f'unit-{i}.md').read_text(encoding='utf-8')
    for m in re.finditer(r'^## (U\d+-\d+).*?\*\*(P\d)\*\*', t, re.M):
        prios[m.group(1)] = m.group(2)

qb = (EXAM / 'notes' / 'question-bank.md').read_text(encoding='utf-8')
qtopics = re.findall(r'^\*\*Q\d+\*\* \[([^·\]]+)·\s*([^·\]]+)·', qb, re.M)
covered = set(t[1].strip() for t in qtopics)
# written bank topics like U1-1; also MCQ arena topics
qj = json.loads(pathlib.Path('_source/bossrush_mcqs.json').read_text(encoding='utf-8'))
print('chapters by priority:', {p: sum(1 for v in prios.values() if v == p) for p in ('P0', 'P1', 'P2')})

def chap_covered(ch):
    if ch in covered:
        return True
    # mixed-topic questions cover ranges: check unit-level fallbacks
    unit = ch.split('-')[0]
    return any(c == unit or c == 'mixed' for c in covered)

for pri in ('P0', 'P1', 'P2'):
    missing = [c for c, p in sorted(prios.items()) if p == pri and c not in covered]
    print(f'{pri} chapters with NO direct question: {missing or "NONE"}')

# HIGH likely-questions vs bank/lesson coverage
lk = (EXAM / 'notes' / 'likely-questions.md').read_text(encoding='utf-8')
highs = re.findall(r'^### (H\d+)\b.*$', lk, re.M)
print('HIGH items:', len(highs))
site = ''
for p in SITE.rglob('*.html'):
    site += p.read_text(encoding='utf-8')
# every HIGH section's distinctive nouns should appear site-wide
import collections
thin = []
for m in re.finditer(r'(?m)^### (H\d+)[^\n]*\n(.*?)(?=^### |^## |\Z)', lk, re.S):
    body = m.group(2)
    nouns = [w for w in re.findall(r'[A-Za-z]{6,}', m.group(0)) if w.lower() not in
             {'likely', 'questions', 'marks', 'marks:', 'answer', 'explain', 'define', 'discuss', 'describe', 'compare'}]
    absent = [w for w in set(nouns) if w.lower() not in site.lower()]
    if len(absent) > len(set(nouns)) / 2:
        thin.append((m.group(1), absent[:5]))
print('HIGH items with thin site coverage:', thin or 'NONE')
