#!/usr/bin/env python
import sys,re,lorem

strict = len(sys.argv) == 2 and sys.argv[1] == '-s'
stricter = len(sys.argv) == 2 and sys.argv[1] == '-ss'

text = sys.stdin.read()

# create the inverse of the dictionary
dict = dict((v,k) for k, v in lorem.dictionary.iteritems())

splitter = re.compile(r'(\s+|\^?[0-9a-zA-Z]+|[a-zA-Z]+|\^?\d+|[,\.~]?)')
words = splitter.findall(text)
for w in words:
    code = w
    upper = False
    if len(code) > 1 and code[0] == '^':
        code = code[1:]
        upper = True
    if strict:
        #print code, lorem.strict_str(code)
        code = lorem.strict_str(code)
    elif stricter:
        try:
            #print "\n'"+code+"'", lorem.base36decode(code)
            code = str(lorem.base36decode(code))
        except ValueError:
            pass
    if code in dict:
        sys.stdout.write(dict[code].title() if upper else dict[code])
    elif w == '~':
        sys.stdout.write('\n\n ')
    else:
        sys.stdout.write(w)
