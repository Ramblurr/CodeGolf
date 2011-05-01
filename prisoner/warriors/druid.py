#!/usr/bin/env python

"""
Druid, by Josh Caswell

Druids are slow to anger, but do not forget.
http://codegolf.stackexchange.com/questions/2357/1p5-iterated-prisoners-dilemma/2404#2404
"""

import sys
from itertools import groupby

FORBEARANCE = 7
TOLERANCE = FORBEARANCE + 5

try:
    history = sys.argv[1]
except IndexError:
    history = ""

# If there's been too much defection overall, defect
if (history.count('E') > TOLERANCE) or (history.count('R') > TOLERANCE):
    print 't'
# Too much consecutively, defect
elif max([0] + [len(list(g)) for k,g in     # The 0 prevents dying on []
                groupby(history) if k in 'ER']) > FORBEARANCE:
    print 't'
# Otherwise, be nice
else:
    print 'c'