import pathlib
t = pathlib.Path('exam/notes/question-bank.md').read_text(encoding='utf-8')
i = t.find('**Q85**')
print(repr(t[i:i + 650]))
