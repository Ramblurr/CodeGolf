#!/usr/bin/env python

"""
The Little Schemer, by Josh Caswell

No relation to the book. Keeps opponent's trust > suspicion 
by at least 10%, trying to ride the line.
"""

from __future__ import division
import sys
from os import urandom

out = sys.stderr.write

def randrange(n):
    if n == 0:
        return 0
    else:
        return ord(urandom(1)) % n

try:
    history = sys.argv[1]
except IndexError:
    print 'c'
    sys.exit(0)

R_count = history.count('R')
S_count = history.count('S')
K_count = history.count('K')
E_count = history.count('E')

# Suspicion is _S_ and E because it's _opponent's_ suspicion
suspicion = (S_count + E_count) / len(history)
# Likewise trust
trust = (K_count + R_count) / len(history)

if suspicion > trust:
    print 'c'
else:
    projected_suspicion = (1 + S_count + E_count) / (len(history) + 1)
    projected_trust = (1 + K_count + R_count) / (len(history) + 1)

    leeway = projected_trust - projected_suspicion
    odds = int(divmod(leeway, 0.1)[0])

    print 't' if randrange(odds) else 'c'
