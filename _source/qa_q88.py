import re, pathlib
t = pathlib.Path('exam/notes/question-bank.md').read_text(encoding='utf-8')
i88 = t.find('**Q88**')
print(repr(t[i88:i88 + 700]))
