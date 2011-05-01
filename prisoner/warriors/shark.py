#!/usr/bin/env python

"""
Shark, by Josh Caswell

Carpe stultores.
"""

import sys

HUNGER = 12

try:
    history = sys.argv[1]
except IndexError:
    print 'c'
    sys.exit(0)

if history.count('S') > HUNGER:
    print 't'
else:
    print 'c' if history[0] in "SK" else 't'
