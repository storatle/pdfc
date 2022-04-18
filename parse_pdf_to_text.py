from tika import parser # pip install tika
filename = 'energi21'
raw = parser.from_file(filename + '.pdf')
sourcefile = open(filename + '.txt','w', encoding="utf-8")
print(raw['content'],file = sourcefile)
sourcefile.close()
