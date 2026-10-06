import re, pathlib
s = pathlib.Path('site/adbms')
# drills: every select's data-ans must be one of its options
t = (s / 'drills.html').read_text(encoding='utf-8')
sels = re.findall(r'<select data-ans="([^"]+)"[^>]*>(.*?)</select>', t, re.S)
print('sorter selects:', len(sels))
bad = 0
for ans, inner in sels:
    opts = re.findall(r'<option value="([^"]+)">', inner)[1:]
    if ans not in opts:
        bad += 1
        print('  MISMATCH:', ans, 'not in', opts)
print('mismatches:', bad)
print('msrows:', len(re.findall(r'class="msrow"', t)))
print('drill blocks:', len(re.findall(r'class="drill"', t)))
# lessons: quick check ids exist in BY_ID
import json
q = (s / 'quizzes.js').read_text(encoding='utf-8')
ids = set(re.findall(r'"id": "(Q\d+)"', q))
print('mcq ids:', len(ids))
for n in range(1, 13):
    h = (s / f'ch{n:02d}.html').read_text(encoding='utf-8')
    used = re.findall(r'MCQ_BY_ID\["(Q\d+)"\]', h)
    missing = [u for u in used if u not in ids]
    print(f'ch{n:02d}: quick={used} missing={missing}')
# index chapters
idx = (s / 'index.html').read_text(encoding='utf-8')
print('index cards:', len(re.findall(r'class="ch"', idx)))
for f in ['quiz.html', 'mock1.html', 'mock2.html', 'mock3.html', 'cram.html', 'plan.html']:
    p = s / f
    print(f, 'bytes:', p.stat().st_size)
