#!/usr/bin/python
import sys

if len(sys.argv) == 1:
    print 'c'
else:
    hist = sys.argv[1]
    if hist[0] == 'K' or hist[0] == 'E':
        print 'c'
    else:
        print 't'
