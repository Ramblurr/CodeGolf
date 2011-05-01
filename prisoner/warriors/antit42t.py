#!/usr/bin/python

"""
Anti-T42T Missile, by Josh Caswell

That Tit-for-two-tats, what a push-over!
  T42T: ccctcctcc...
AT42TM: cttcttctt...
        KSSRSSRSS...
"""
import sys
try:
    history = sys.argv[1]
except IndexError:
    print 'c'
    sys.exit(0)

if history[:2] == 'SS':
    print 'c'
else:
    print 't'
