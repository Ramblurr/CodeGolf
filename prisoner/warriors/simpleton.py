#!/usr/bin/env python

"""
Simpleton, by Josh Caswell

Quick to anger, quick to forget, unable to take advantage of opportunity.
http://codegolf.stackexchange.com/questions/2357/1p5-iterated-prisoners-dilemma/2409#2409
"""

import sys
from os import urandom

WHIMSY = 17

try:
    history = sys.argv[1]
except IndexError:
    if not ord(urandom(1)) % WHIMSY:
        print 't'
    else:
        print 'c'
    sys.exit(0)

if history[0] in "RE":
    print 't'
elif not ord(urandom(1)) % WHIMSY:
    print 't'
else:
    print 'c'