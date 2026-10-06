import pathlib
p = pathlib.Path('_source/build_site.py')
t = p.read_text(encoding='utf-8')

old_units = """UNITS = [
    ('Foundations', 'Database systems, ER modeling, SQL', '#f4a48c', [1, 2, 3]),
    ('Normalization & Storage', 'FDs, the 1NF→5NF ladder, B+ trees, hashing', '#86c9e8', [4, 5, 6]),
    ('Transactions & Recovery', 'ACID, serializability, 2PL, WAL, checkpoints', '#f3c95c', [7, 8, 9]),
    ('Distributed & NoSQL', 'Fragmentation, 2PC, CAP/BASE, sharding, all five stores', '#8fd6b0', [10, 11]),
    ('Exam arena', 'Answer builder, drills, MCQ arena, mocks, cram', '#bba8ee', [12, 13, 14, 15, 16, 17, 18]),
    ('Narrated lessons', 'Watch + listen: animated beats with speech narration', '#f0b45a', [19, 20, 21]),
]"""
assert old_units in t, 'UNITS block not found'
new_units = """# Unit names follow ADBMS_MasterNotes.docx (exactly 5 units). String entries are
# unit-notes docs cards; int entries are progress-tracked chapters. 'Exam arena'
# is infrastructure, not a unit. Narrated lessons sit inside their real units.
UNITS = [
    ('Database Concepts & Modeling', 'Database systems, ER modeling, SQL', '#f4a48c',
     [1, 2, 3, ('unit-1', 'Unit 1 notes', 'all 9 chapters, P0–P2 tagged')], 'unit'),
    ('Normalization, Storage & Indexing', 'FDs, the 1NF→5NF ladder, B+ trees, hashing', '#86c9e8',
     [4, 5, 6, 19, ('unit-2', 'Unit 2 notes', 'all 14 chapters, P0–P2 tagged')], 'unit'),
    ('Transactions, Concurrency & Recovery', 'ACID, serializability, 2PL, WAL, checkpoints', '#f3c95c',
     [7, 8, 9, 20, ('unit-3', 'Unit 3 notes', 'all 12 chapters, P0–P2 tagged')], 'unit'),
    ('Distributed Databases & NoSQL', 'Fragmentation, 2PC, CAP/BASE, sharding', '#8fd6b0',
     [10, 21, ('unit-4', 'Unit 4 notes', 'all 12 chapters, P0–P2 tagged')], 'unit'),
    ('NoSQL Stores & Indexing', 'Cassandra, Redis, Neo4j, vectors, cross-system indexing', '#e8a0c8',
     [11, ('unit-5', 'Unit 5 notes', 'all 14 chapters, P0–P2 tagged')], 'unit'),
    ('Exam arena', 'Answer builder, drills, MCQ arena, mocks, cram', '#bba8ee',
     [12, 13, 14, 15, 16, 17, 18], 'arena'),
]"""
t = t.replace(old_units, new_units, 1)

old_loop = """units_html = []
for ui, (uname, sub, color, nums) in enumerate(UNITS, 1):
    cards = []
    for n in nums:
        f, t, m = chmap[n]
        cards.append(f'<a class="ch" data-ch="{n}" id="ch{n:02d}" href="{f}" style="--c:{color}"><b>{n}</b><span>{esc(t)}<small>{m}</small></span></a>')
    units_html.append(
        f'<section class="unit" style="--c:{color}"><h2><span class="n">Unit {ui}</span>{esc(uname)}</h2>'
        f'<p class="sub">{esc(sub)}</p><div class="grid">{"".join(cards)}</div></section>')"""
assert old_loop in t, 'units loop not found'
new_loop = """units_html = []
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
        f'<p class="sub">{esc(sub)}</p><div class="grid">{"".join(cards)}</div></section>')"""
t = t.replace(old_loop, new_loop, 1)

old_crumb = "crumb_unit = 'Exam arena' if ch >= 12 else f'Unit {(ch - 1) // 3 + 1}'"
assert old_crumb in t, 'crumb not found'
new_crumb = ("_CH_UNIT = {1: 'Unit 1', 2: 'Unit 1', 3: 'Unit 1', 4: 'Unit 2', 5: 'Unit 2', 6: 'Unit 2',\n"
             "             7: 'Unit 3', 8: 'Unit 3', 9: 'Unit 3', 10: 'Unit 4', 11: 'Unit 5',\n"
             "             19: 'Unit 2', 20: 'Unit 3', 21: 'Unit 4'}\n"
             "        crumb_unit = _CH_UNIT.get(ch, 'Exam arena')")
t = t.replace(old_crumb, new_crumb, 1)
p.write_text(t, encoding='utf-8')
print('units restructured')
