import pathlib
p = pathlib.Path('_source/build_site.py')
t = p.read_text(encoding='utf-8')

docs_block = '''
# ---------------- docs library (every linked .md as a nice page) ----------------
(SITE / 'docs').mkdir(exist_ok=True)
STE_DOCS = {'unit-1', 'unit-2', 'unit-3', 'unit-4', 'unit-5', 'diagrams',
            'comparisons', 'processes', 'mistakes', 'examples', 'likely'}
DOC_SOURCES = {
    'unit-1': ('Unit 1 — concepts & modeling', 'notes/chapter-notes/unit-1.md'),
    'unit-2': ('Unit 2 — normalization & storage', 'notes/chapter-notes/unit-2.md'),
    'unit-3': ('Unit 3 — transactions & recovery', 'notes/chapter-notes/unit-3.md'),
    'unit-4': ('Unit 4 — distributed & NoSQL', 'notes/chapter-notes/unit-4.md'),
    'unit-5': ('Unit 5 — stores & indexing', 'notes/chapter-notes/unit-5.md'),
    'diagrams': ('Diagrams — draw these blind', 'notes/diagrams-and-mental-models.md'),
    'formulas': ('Formulas & rules', 'notes/formulas.md'),
    'comparisons': ('Comparisons — tables = marks', 'notes/comparisons.md'),
    'processes': ('Processes as flows', 'notes/processes-and-algorithms.md'),
    'mistakes': ('Common mistakes', 'notes/common-mistakes.md'),
    'definitions': ('Definitions (3-layer)', 'notes/definitions.md'),
    'answers': ('Answer bank', 'notes/answer-bank.md'),
    'examples': ('Examples', 'notes/examples.md'),
    'errata': ('Errata', 'notes/errata.md'),
    'likely': ('Likely questions', 'notes/likely-questions.md'),
    'tracker': ('Weakness tracker (your log)', 'weakness-tracker.md'),
    'guide': ('Master study guide', 'notes/master-study-guide.md'),
    'path': ('Learning path from zero', 'notes/learning-path-from-zero.md'),
}
for slug, (dtitle, rel) in DOC_SOURCES.items():
    body = '<div class="content">' + md_file(EXAM / rel) + '</div>'
    if slug in STE_DOCS:
        STE_PAIRS.append([body, None])
        body = ste_page(body)
        STE_PAIRS[-1][1] = body
    (SITE / 'docs' / f'{slug}.html').write_text(chrome(dtitle, body, base='../'), encoding='utf-8')
print('docs pages:', len(DOC_SOURCES))

# flashcards flip deck
fc_text = (EXAM / 'notes' / 'flashcards.md').read_text(encoding='utf-8')
fparts = re.split(r'(?m)^## (Deck [A-E])\\b.*$', fc_text)
CARDS = []
for i in range(1, len(fparts), 2):
    deck = fparts[i][-1]
    for m in re.finditer(r'^\\d+\\.\\s\\*\\*Q:\\*\\*\\s*(.+?)\\s*\\*\\*A:\\*\\*\\s*(.+)$', fparts[i + 1], re.M):
        CARDS.append({'deck': deck, 'q': m.group(1).strip(), 'a': m.group(2).strip()})
for m in re.finditer(r'^\\|\\s*(T\\d+)\\s*\\|\\s*(.+?)\\s*\\|\\s*\\*\\*(T|F)\\*\\*\\s*(.*?)\\|$', fc_text, re.M):
    CARDS.append({'deck': 'TF', 'q': m.group(2).strip() + ' — true or false?',
                  'a': ('TRUE. ' if m.group(3) == 'T' else 'FALSE. ') + m.group(4).strip('() ')})
print('flashcards parsed:', len(CARDS))

def fcard(i, c):
    return (
        f'<div class="fcard" id="C{i}" data-deck="{c["deck"]}" tabindex="0">'
        f'<div class="fq">{inline(c["q"])}</div><div class="fa">{inline(c["a"])}</div>'
        f'<div class="flip">tap / Enter to flip · then mark yourself</div>'
        f'<div class="qacts"><button class="btn small go cmark" data-v="1">✓ got it</button>'
        f'<button class="btn small quiet cmark" data-v="0.5">~ partial</button>'
        f'<button class="btn small quiet cmark" data-v="0">✗ missed</button></div></div>')

cards_page = chrome(
    'Flashcards (flip deck)',
    '<div class="content"><p>Say your answer out loud <b>before</b> flipping. Mark honestly — '
    'first marks only. Missed cards return in the <b>Missed only</b> filter.</p><p data-cscore></p></div>'
    '<div class="toolbar"><button class="fbtn on" data-cdeck="all">All</button>'
    + ''.join(f'<button class="fbtn" data-cdeck="{d}">Deck {d}</button>' for d in 'ABCDE')
    + '<button class="fbtn" data-cdeck="TF">True/False</button>'
    + '<button class="fbtn" id="cwrong">Missed only</button></div>'
    '<div id="cards">' + ''.join(fcard(i, c) for i, c in enumerate(CARDS)) + '</div>'
    '<div class="scorebar" data-cscore></div>'
    '<script>initCards();</script>', base='../')
(SITE / 'docs' / 'cards.html').write_text(cards_page, encoding='utf-8')

LIB = [('unit-1', 'Unit 1 notes', 'concepts & modeling'), ('unit-2', 'Unit 2 notes', 'normalization & storage'),
       ('unit-3', 'Unit 3 notes', 'transactions & recovery'), ('unit-4', 'Unit 4 notes', 'distributed & NoSQL'),
       ('unit-5', 'Unit 5 notes', 'stores & indexing'), ('diagrams', 'Diagrams', 'draw these blind'),
       ('formulas', 'Formulas', 'rules & criteria'), ('comparisons', 'Comparisons', 'tables = marks'),
       ('processes', 'Processes', 'ordered flows'), ('mistakes', 'Mistakes', 'what costs marks'),
       ('definitions', 'Definitions', '3-layer format'), ('answers', 'Answer bank', '2/5/10/20-mark models'),
       ('examples', 'Examples', 'concrete cases'), ('errata', 'Errata', 'traps & clarifications'),
       ('likely', 'Likely questions', 'HIGH/MED/LOW'), ('cards', 'Flashcards', 'flip deck + T/F'),
       ('tracker', 'Weakness tracker', 'your error log'), ('guide', 'Study guide', 'priority map'),
       ('path', 'Learning path', '12 lessons from zero')]
lib_section = ('<section class="unit" style="--c:#f0b45a"><h2><span class="n">Library</span>'
               'Every source note, readable</h2><p class="sub">Full files in site styling with contents navigation. '
               'Quizzable pages (bank, arena, drills, cards) track first tries.</p><div class="grid">'
               + ''.join(f'<a class="ch" href="docs/{s}.html" style="--c:#f0b45a"><b>§</b><span>{t}<small>{d}</small></span></a>'
                         for s, t, d in LIB) + '</div></section>')
units_html.append(lib_section)

# STE compliance metric
_pre_ok = _pre_tot = _post_ok = _post_tot = 0
for _pre, _post in STE_PAIRS:
    a, b = ste_metric(_pre)
    _pre_ok += a; _pre_tot += b
    a, b = ste_metric(_post)
    _post_ok += a; _post_tot += b
print(f'STE: {100.0 * _pre_ok / max(1, _pre_tot):.1f}% -> {100.0 * _post_ok / max(1, _post_tot):.1f}% sentences <=20 words '
      f'({_post_tot} sentences, {len(STE_PAIRS)} pages)')

'''

anchor = '# ---------------- written answer bank ----------------'
assert anchor in t
t = t.replace(anchor, docs_block + anchor, 1)
p.write_text(t, encoding='utf-8')
print('docs block inserted')
