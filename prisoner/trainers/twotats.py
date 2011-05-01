#!/usr/bin/env python
"""
Tit For Two Tats, entry to 1P5 Iterated Prisoner's Dilemma, 
    by Josh Caswell (not an original idea).

Cooperates unless opponent has defected in the last two rounds.
"""

import sys
try:
    history = sys.argv[1]
except IndexError:
    history = ""

two_tats = ("RR", "RE", "ER", "EE")

if len(history) < 2:
    print 'c'
else:
    print 't' if history[:2] in two_tats else 'c'
