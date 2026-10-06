import docx
d = docx.Document('ADBMS_MasterNotes.docx')
heads = [(p.style.name, p.text.strip()) for p in d.paragraphs
         if p.style.name.startswith('Heading') and p.text.strip()]
for style, text in heads:
    print(style, '|', text[:90])
print('total headings:', len(heads))
