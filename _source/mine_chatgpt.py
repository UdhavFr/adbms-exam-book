import re, pathlib, json

base = pathlib.Path('chatgpt/adbms-papermorph')
out = {}

# chapters.md title map
chapters_md = (base / 'books/adbms/chapters.md').read_text(encoding='utf-8')

for i in range(1, 12):
    js = (base / f'site/adbms/ch{i:02d}/data.js').read_text(encoding='utf-8', errors='replace')
    # beats: title/body/purpose/memory/trap
    beats = []
    for m in re.finditer(r'\{\s*"title":\s*"((?:[^"\\]|\\.)*)",\s*"body":\s*"((?:[^"\\]|\\.)*)",\s*"purpose":\s*"((?:[^"\\]|\\.)*)"(.*?)(?=\n    \},|\n  \]\})', js, re.S):
        tail = m.group(4)
        mem = re.search(r'"memory":\s*"((?:[^"\\]|\\.)*)"', tail)
        trap = re.search(r'"trap":\s*"((?:[^"\\]|\\.)*)"', tail)
        beats.append({
            'title': m.group(1), 'body': m.group(2), 'purpose': m.group(3),
            'memory': mem.group(1) if mem else None,
            'trap': trap.group(1) if trap else None,
        })
    # MCQs in data.js if any
    mcqs = re.findall(r'\{\s*"q"\s*:\s*"((?:[^"\\]|\\.)*)",\s*"opts"\s*:\s*\[(.*?)\],\s*"ans"\s*:\s*(\d+)(.*?)\}', js, re.S)
    out[f'ch{i:02d}'] = {'beats': beats, 'mcq_count': len(mcqs),
                          'traps': [b['trap'] for b in beats if b['trap']],
                          'memories': [b['memory'] for b in beats if b['memory']]}

pathlib.Path('_source/chatgpt_mined.json').write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding='utf-8')
for k, v in out.items():
    print(k, 'beats:', len(v['beats']), 'traps:', len(v['traps']), 'mem:', len(v['memories']), 'mcqs:', v['mcq_count'])
