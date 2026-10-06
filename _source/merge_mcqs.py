import json, pathlib

mcqs = json.loads(pathlib.Path('_source/bossrush_mcqs.json').read_text(encoding='utf-8'))
# topic mapping (unit guess per question index order = 2 per module roughly); tag by content
tags = {
 0: ('U1-6', 'P1', '2'), 1: ('U1-6', 'P1', '1'),
 2: ('U2-1', 'P0', '1'), 3: ('U2-1', 'P0', '1'), 4: ('U2-1', 'P0', '1'),
 5: ('U2-2', 'P0', '1'), 6: ('U2-2', 'P1', '1'), 7: ('U2-2', 'P0', '1'),
 8: ('U3-1', 'P0', '1'), 9: ('U3-1', 'P0', '1'), 10: ('U3-1', 'P0', '1'),
 11: ('U3-3', 'P0', '1'), 12: ('U3-4', 'P0', '1'), 13: ('U3-4', 'P1', '1'),
 14: ('U4-3', 'P0', '1'), 15: ('U4-4', 'P1', '1'), 16: ('U4-4', 'P2', '1'),
 17: ('U4-5', 'P1', '1'), 18: ('U4-7', 'P1', '1'), 19: ('U4-7', 'P1', '1'),
 20: ('U2-6', 'P0', '1'), 21: ('U2-6', 'P0', '1'),
 22: ('U3-9', 'P0', '1'), 23: ('U3-8', 'P0', '1'),
 24: ('U5-3', 'P1', '1'), 25: ('U5-1', 'P0', '1'), 26: ('U5-1', 'P0', '1'),
 27: ('U5-5', 'P1', '1'), 28: ('U5-5', 'P0', '1'),
 29: ('U1-9', 'P0', '1'), 30: ('U1-10', 'P0', '1'), 31: ('U1-4', 'P0', '1'),
}

lines = []
lines.append('\n---\n')
lines.append('\n## SECTION H — MCQ RAPID-FIRE (32 items, mixed units)\n')
lines.append('*External-source additions:* these 32 MCQs were recovered from `claude/ADBMS Boss Rush.html` '
             '(another AI artifact in this folder) and **verified item-by-item against `ADBMS_MasterNotes.docx`** '
             '— every answer key and explanation agrees with the master notes. Use for speed drills: '
             'answer in 30 seconds each, no working.\n')

for i, m in enumerate(mcqs):
    topic, pri, diff = tags[i]
    opts = m['options']
    correct = opts[m['ans']].replace('*', '')
    lines.append(f"**Q{89+i}** [MCQ A· {topic} A· {pri} A· {diff}] {m['q']}")
    for j, o in enumerate(opts):
        marker = ' **[KEY]**' if j == m['ans'] else ''
        lines.append(f"- {chr(65+j)}. {o}{marker}")
    lines.append(f"- Why: {m['why']}")
    lines.append('')

section = '\n'.join(lines)

p = pathlib.Path('exam/notes/question-bank.md')
t = p.read_text(encoding='utf-8')
anchor = '\n---\n\n## Answer-quality checklist'
assert anchor in t, 'anchor not found'
t = t.replace(anchor, section + anchor)
p.write_text(t, encoding='utf-8')
print('appended', len(mcqs), 'MCQs; new total questions = 88 +', len(mcqs), '=', 88 + len(mcqs))
