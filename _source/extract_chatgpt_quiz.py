import re, pathlib, json

base = pathlib.Path('chatgpt/adbms-papermorph/site/adbms')
allq = []
for i in range(1, 12):
    js = (base / f'ch{i:02d}/data.js').read_text(encoding='utf-8', errors='replace')
    m = re.search(r'"quiz"\s*:\s*\[(.*)\]\s*\};?\s*$', js, re.S)
    if not m:
        print('no quiz in', i); continue
    block = m.group(1)
    qs = re.findall(r'\{\s*"q"\s*:\s*"((?:[^"\\]|\\.)*)",\s*"opts"\s*:\s*\[(.*?)\],\s*"a"\s*:\s*(\d+),\s*"why"\s*:\s*"((?:[^"\\]|\\.)*)",\s*"whyWrong"\s*:\s*"((?:[^"\\]|\\.)*)"\s*\}', block, re.S)
    for q in qs:
        opts = re.findall(r'"((?:[^"\\]|\\.)*)"', q[1])
        allq.append({'ch': i, 'q': q[0], 'opts': opts, 'a': int(q[2]), 'why': q[3], 'whyWrong': q[4]})
    print(f'ch{i:02d}: {len(qs)} quiz questions')

pathlib.Path('_source/chatgpt_quizzes.json').write_text(json.dumps(allq, indent=1, ensure_ascii=False), encoding='utf-8')
print('TOTAL:', len(allq))
