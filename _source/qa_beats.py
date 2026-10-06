import re, json, pathlib

q = pathlib.Path('site/adbms/quizzes.js').read_text(encoding='utf-8')
ids = set(re.findall(r'"id": "(Q\d+)"', q)) | {'QAC1', 'QAC2', 'QAC3', 'QAC4', 'QAC5', 'QAC6', 'QAC7', 'QAC8'}

PAGES = ['site/adbms/ch19/index.html', 'site/adbms/ch20/index.html', 'site/adbms/ch21/index.html', 'site/adbms/ch22/index.html', 'site/adbms/ch23/index.html', 'site/adbms/ch24/index.html', 'site/adbms/ch25/index.html']

def parse_marks(say):
    marks, wi = {}, 0
    for m in re.finditer(r'\[\[(\w+)\]\]|(\S+)', say):
        if m.group(1):
            marks[m.group(1)] = wi
        else:
            wi += 1
    return marks, wi

problems = []
for page in PAGES:
    print('=====', page)
    h = pathlib.Path(page).read_text(encoding='utf-8')
    says = re.findall(r"say: '((?:[^'\\]|\\.)*)'", h)
    print('beats with say:', len(says))

    # steps referenced in each svg: collect per-beat by splitting on "{ id:"
    blocks = re.split(r"\{ id: '", h)[1:]
    for b in blocks:
        bid = b.split("'", 1)[0]
        saym = re.search(r"say: '((?:[^'\\]|\\.)*)'", b)
        marks, nwords = parse_marks(saym.group(1)) if saym else ({}, 0)
        steps = set(re.findall(r'data-step="(\w+)"', b))
        # T() helper calls: 7th positional arg is the step name
        for m in re.finditer(r"T\(\d+,\s*\d+,\s*'(?:[^'\\]|\\.)*',\s*\d+,\s*C\.\w+,\s*'(?:middle|start)',\s*'(\w+)'", b):
            steps.add(m.group(1))
        for m in re.finditer(r"data-step=\"\$\{[^}]*\? *'(\w+)'", b):
            steps.add(m.group(1))
        # steps fired by marks: step names should equal a mark (timed[] none used)
        unfired = steps - set(marks)
        askm = re.search(r'ask: \[([^\]]*)\]', b)
        ask = re.findall(r"'(Q[A-Z]*\d+)'", askm.group(1)) if askm else []
        badq = [a for a in ask if a not in ids]
        print(f'{bid}: words={nwords} marks={sorted(marks)} steps={sorted(steps)} ask={ask}')
        if unfired:
            problems.append(f'{page} {bid}: steps never fired by marks: {sorted(unfired)}')
        if badq:
            problems.append(f'{page} {bid}: unknown MCQ ids: {badq}')
print('PROBLEMS:', problems or 'NONE')
