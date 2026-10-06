import re, pathlib, json

h = pathlib.Path(r'claude\ADBMS Boss Rush.html').read_text(encoding='utf-8', errors='replace')

# Extract each module block between {i:'...'} ... q:[...]
# Parse questions: ['question text',['opt','opt','opt','opt'],answerIdx,'explanation']
qblocks = re.findall(r"q:\[(.*?)\]\}", h, re.S)
out = []
for qb in qblocks:
    qs = re.findall(r"\['([^']+)',\s*\[(.*?)\],(\d+),'((?:[^'\\]|\\.)*)'\]", qb, re.S)
    for q in qs:
        text = q[0]
        opts = re.findall(r"'([^']*)'", q[1])
        idx = int(q[2])
        expl = q[3].replace("\\'", "'")
        out.append({'q': text, 'options': opts, 'ans': idx, 'why': expl})

print(len(out))
pathlib.Path('_source/bossrush_mcqs.json').write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding='utf-8')
