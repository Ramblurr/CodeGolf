#!/usr/bin/env python

"""
Honor Among Thieves, by Josh Caswell

I'd never sell out a fellow thief, but I'll fleece a plump mark,
and I'll cut your throat if you try to cross me.
"""

from __future__ import division
import sys

PLUMPNESS_FACTOR = .33
WARINESS = 10

THIEVES_CANT = "E" + ("K" * WARINESS)

try:
    history = sys.argv[1]
except IndexError:
    history = ""

if history:
    sucker_ratio = (history.count('K') + history.count('S')) / len(history)
    seem_to_have_a_sucker = sucker_ratio > PLUMPNESS_FACTOR


# "Hey, nice t' meetcha."
if len(history) < WARINESS:
    #"Nice day, right?"
    if not set(history).intersection("RE"):
        print 'c'
    # "You sunnuvab..."
    else:
        print 't'

# "Hey, lemme show ya this game. Watch the queen..."
elif len(history) == WARINESS and seem_to_have_a_sucker:
    print 't'

# "Oh, s#!t, McWongski, I swear I din't know dat were you."
elif history[-len(THIEVES_CANT):] == THIEVES_CANT:

    # "Nobody does dat t' me!"
    if set(history[:-len(THIEVES_CANT)]).intersection("RE"):
        print 't'
    # "Hey, McWongski, I got dis job we could do..."
    else:
        print 'c'

# "Do you know who I am?!"
elif set(history).intersection("RE"):
    print 't'

# "Ah, ya almos' had da queen dat time. One more try, free, hey? G'head!"
elif seem_to_have_a_sucker:
    print 't'

# "Boy, you don't say much, do ya?"
else:
    print 'c'
