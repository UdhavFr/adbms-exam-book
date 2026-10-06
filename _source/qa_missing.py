import re, pathlib
t = pathlib.Path('exam/notes/question-bank.md').read_text(encoding='utf-8')
allq = [int(x) for x in re.findall(r'^\*\*Q(\d+)\*\*', t, re.M)]
print('total **Q headers:', len(allq))
expect = set(list(range(1, 89)) + list(range(143, 151)))
missing = sorted(expect - set(allq))
print('missing headers:', missing)
extra = sorted(set(allq) - expect)
print('unexpected headers:', extra[:10], '... total extras:', len(extra))
