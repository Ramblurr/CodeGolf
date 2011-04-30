#!/usr/bin/env python
import sys,re,lorem

strict = len(sys.argv) == 2 and sys.argv[1] == '-s'
stricter = len(sys.argv) == 2 and sys.argv[1] == '-ss'

text = sys.stdin.read()
dict = lorem.dictionary

splitter = re.compile(r'([a-zA-Z]+|\s+|[,\.]*)')
words = splitter.findall(text)
for w in words:
    if w.lower() in dict:
        code = int(dict[w.lower()])
        if strict:
            code = lorem.strict_code(code)
        elif stricter:
            code = lorem.base36encode(code)
        if w.istitle():
            code = '^%s' %(code)
        sys.stdout.write(str(code))
    elif w == '\n\n ':
        sys.stdout.write('~')
    else:
        sys.stdout.write(w)
