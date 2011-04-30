#!/usr/bin/env python

from nltk.probability import *
from nltk.tokenize import *
from sets import Set

txt = open('lorem', 'r').read()
tokens = list(WordTokenizer().tokenize(txt))
freq = FreqDist()
for w in tokens:
    freq.inc(w.lower())
tokens_sorted = sorted(freq, key=freq.get, reverse=True)

d = {}
star_count = 0
for i in tokens_sorted:
    d[i] = str(star_count)
    star_count += 1

print d

