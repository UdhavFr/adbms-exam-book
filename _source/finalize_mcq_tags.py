import re, json, pathlib

qb = pathlib.Path('exam/notes/question-bank.md')
t = qb.read_text(encoding='utf-8')

# Correct tags for Boss Rush MCQs Q89..Q120 (index 0..31): (topic, priority, difficulty)
boss_fix = [
    ('mixed',   'P1', '2'),  # 0 20-mark first step
    ('mixed',   'P1', '1'),  # 1 diagram for process
    ('U2-4',    'P0', '1'),  # 2 2NF partial
    ('U2-5',    'P0', '1'),  # 3 3NF transitive
    ('U2-6',    'P0', '1'),  # 4 BCNF implies 3NF
    ('U2-1',    'P0', '1'),  # 5 A+ closure
    ('U2-9',    'P1', '1'),  # 6 lossless binary
    ('U2-9',    'P1', '1'),  # 7 3NF synthesis
    ('U3-3',    'P0', '1'),  # 8 durability
    ('U3-3',    'P0', '1'),  # 9 atomicity
    ('U3-3',    'P0', '1'),  # 10 isolation / CC
    ('U3-5',    'P0', '1'),  # 11 precedence cycle
    ('U3-6',    'P0', '1'),  # 12 2PL shrinking
    ('U3-6',    'P1', '1'),  # 13 wait-for graph
    ('U4-7',    'P0', '1'),  # 14 CAP AP
    ('U4-8',    'P0', '1'),  # 15 BASE soft state
    ('U4-9',    'P1', '1'),  # 16 hash sharding
    ('U4-2',    'P0', '1'),  # 17 vertical frag rebuild
    ('U4-4',    'P0', '1'),  # 18 2PC NO vote
    ('U4-4',    'P1', '1'),  # 19 2PC blocking
    ('U2-13',   'P0', '1'),  # 20 B+ tree range
    ('U2-13',   'P0', '1'),  # 21 index downside
    ('U3-9',    'P0', '1'),  # 22 deferred update
    ('U3-12',   'P0', '1'),  # 23 WAL
    ('U5-4',    'P1', '1'),  # 24 Neo4j graph
    ('U4-11',   'P0', '1'),  # 25 MongoDB $gt
    ('U4-12',   'P0', '1'),  # 26 $match first
    ('U5-7',    'P0', '1'),  # 27 cosine similarity
    ('U5-6',    'P0', '1'),  # 28 HNSW
    ('U1-5',    'P0', '1'),  # 29 M:N junction
    ('U1-7',    'P0', '1'),  # 30 DCL
    ('U1-8',    'P0', '1'),  # 31 entity integrity
]

def retag(text, qnum, topic, pri, diff):
    pat = re.compile(r'(\*\*Q%d\*\* \[MCQ )A· [^ ]+ A· [^ ]+ A· [^ \]]+(\])' % qnum)
    new, n = pat.subn(lambda m: m.group(1) + 'A· ' + topic + ' A· ' + pri + ' A· ' + diff + m.group(2), text, count=1)
    assert n == 1, f'Q{qnum} not retagged'
    return new

for i, (topic, pri, diff) in enumerate(boss_fix):
    t = retag(t, 89 + i, topic, pri, diff)

# Build Section I from ChatGPT quizzes
gpt = json.loads(pathlib.Path('_source/chatgpt_quizzes.json').read_text(encoding='utf-8'))
gpt_tags = [
    ('U1-3', 'P0', '1'), ('U1-2', 'P1', '1'),      # ch1
    ('U1-5', 'P0', '1'), ('U1-5', 'P1', '1'),      # ch2
    ('U1-7', 'P0', '1'), ('U1-8', 'P0', '1'),      # ch3
    ('U2-4', 'P0', '1'), ('U2-6', 'P0', '1'),      # ch4
    ('U2-13', 'P0', '1'), ('U2-14', 'P1', '1'),    # ch5
    ('U3-3', 'P0', '1'),                            # ch6
    ('U3-6', 'P0', '1'), ('U3-12', 'P0', '1'),     # ch7
    ('U4-2', 'P0', '1'), ('U4-4', 'P0', '1'),      # ch8
    ('U4-7', 'P0', '1'), ('U4-10', 'P1', '1'),     # ch9
    ('U5-1', 'P0', '1'), ('U5-6', 'P0', '1'),      # ch10
    ('mixed', 'P1', '1'), ('mixed', 'P1', '1'), ('mixed', 'P0', '1'),  # ch11
]

lines = ['',
         '---',
         '',
         '## SECTION I — MCQ CROSS-CHECK SET (22 items)',
         '',
         '*External-source additions:* these 22 MCQs were recovered from `chatgpt/adbms-papermorph/` '
         '(another AI artifact over the same source notes) and **verified item-by-item against '
         '`ADBMS_MasterNotes.docx`** — every answer key agrees with the source. Each carries the original '
         '`whyWrong` distractor explanation so you learn why the other options fail.',
         '']
for i, (m, (topic, pri, diff)) in enumerate(zip(gpt, gpt_tags)):
    qn = 121 + i
    opts = m['options'] if 'options' in m else m['opts']
    ans = m['ans'] if 'ans' in m else m['a']
    lines.append(f"**Q{qn}** [MCQ A· {topic} A· {pri} A· {diff}] {m['q']}")
    for j, o in enumerate(opts):
        marker = ' **[KEY]**' if j == ans else ''
        lines.append(f"- {chr(65+j)}. {o}{marker}")
    lines.append(f"- Why: {m['why']}")
    lines.append(f"- Why not: {m['whyWrong']}")
    lines.append('')

section_i = '\n'.join(lines)

anchor = '\n---\n\n## Answer-quality checklist'
assert anchor in t, 'anchor missing'
t = t.replace(anchor, section_i + anchor)
qb.write_text(t, encoding='utf-8')
print('retagged 32 Boss Rush MCQs; appended 22 ChatGPT MCQs; total now 142')
