import re, pathlib
t = pathlib.Path('exam/notes/question-bank.md').read_text(encoding='utf-8')
lines = t.splitlines()
for i, ln in enumerate(lines):
    m = re.match(r'\*\*Q(\d+)\*\* (\[.*\]) ?(.*)$', ln)
    if m:
        nxt = lines[i + 1] if i + 1 < len(lines) else ''
        if not nxt.startswith('- Expected:'):
            print('Q' + m.group(1), m.group(2), '->', (m.group(3) + ' | ' + nxt)[:150])
