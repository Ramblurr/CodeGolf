#!/usr/bin/env python

"""
BYGONES, entry to 1P5 Iterated Prisoner's Dilemma, by Josh Caswell

Cooperates at first, plays as Tit for Tat for `bygones * 2` rounds, then checks 
history: if there's too much ratting, get mad and defect; too much 
suckering, feel bad and cooperate.
"""

bygones = 5

import sys

# React to strangers with trust.
try:
    history = sys.argv[1]
except IndexError:
    print 'c'
    sys.exit(0)

replies = { 'K' : 'c', 'S' : 'c',
            'R' : 't', 'E' : 't' }

# Reply in kind.
if len(history) < bygones * 2:
    print replies[history[0]]
    sys.exit(0)

# Reflect on past interactions.
faithful_count = history.count('K')
sucker_count = history.count('S')
rat_count = history.count('R')

# Reprisal. 
if rat_count > faithful_count + bygones:
    # Screw you!
    print 't'
    sys.exit(0)

# Reparation.
if sucker_count > faithful_count + bygones:
    # Geez, I've really been mean.
    print 'c'
    sys.exit(0)

# Resolve to be more forgiving.
two_tats = ("RR", "RE", "ER", "EE")
print 't' if history[:2] in two_tats else 'c'
