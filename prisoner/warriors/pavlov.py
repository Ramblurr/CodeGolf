#!/usr/bin/python
import sys

if len(sys.argv) == 1:
    print 'c'
else:
    hist = sys.argv[1]
    if hist[-1] == 'K' or hist[-1] == 'E':
        print 'c'
    else:
        print 't'
