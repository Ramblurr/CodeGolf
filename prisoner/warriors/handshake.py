#!/usr/bin/python
# The Secret Handshake
# By Aaron
# http://codegolf.stackexchange.com/questions/2357/1p5-iterated-prisoners-dilemma/2375#2375
import sys

TAG = "ctttctttct"
TAGMATCH = "KEEEKEEEKE"

def main():
    if len(sys.argv) == 1:
        hist = ""
    else:
        hist = sys.argv[1]
    if len(hist) <= len(TAG) and hist == TAGMATCH[len(TAG) - len(hist):]:
        print TAG[len(TAG) - len(hist) - 1]
        return
    if hist[-len(TAG):] == TAGMATCH:
        print 'c'
        return
    print "t"

if __name__ == "__main__":
    main()
