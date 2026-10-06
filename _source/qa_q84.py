import re, pathlib
t = pathlib.Path('exam/notes/question-bank.md').read_text(encoding='utf-8')
i = t.find('**Q84**')
j = t.find('**Q86**')
seg = t[i:j]
pat = (r"^\*\*Q(\d+)\*\* \[([^·\]]+)·\s*([^·\]]+)·\s*([^·\]]+)·\s*([^\]]+)\]\s*(.+?)"
       r"\n- Expected:\s*(.+?)\n- Keywords:\s*(.+?)\n- Common wrong:\s*(.+?)(?=\n\n|\n\*\*Q|\Z)")
for m in re.finditer(pat, seg, re.M | re.S):
    print('matched Q' + m.group(1))
print('---Q84 raw---')
k = t.find('**Q84**')
print(repr(t[k:k + 500]))
