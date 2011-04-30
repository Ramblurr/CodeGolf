#! /usr/bin/python
#
# Iterated prisoner's dilemma King of Hill Script Argument is a
# directory. We find all the executables therein, and run all possible
# binary combinations (including self-plays (which only count once!)).
import subprocess 
import os
import sys
import random

RESULTS = {"cc":(2,"K"), "ct":(-1,"R"), "tc":(4,"S"), "tt":(1,"E")}

def runOne(p,h):
    """Run process p with history h and return the standard output"""
    #print "Run '"+p+"' with history '"+h+"'."
    process = subprocess.Popen(p+" "+h,stdout=subprocess.PIPE,shell=True)
    return process.communicate()[0]

def scoreRound(r1,r2):
    return RESULTS.get(r1[0]+r2[0],0)

def runRound(p1,p2,h1,h2):
    """Run both processes, and score the results"""
    r1 = runOne(p1,h1)
    r2 = runOne(p2,h2)
    (s1, L1), (s2, L2) = scoreRound(r1,r2), scoreRound(r2,r1) 
    return (s1, L1+h1),  (s2, L2+h1)

def runGame(rounds,p1,p2):
    sa, sd = 0, 0
    ha, hd = '', ''
    for a in range(0,rounds):
        (na, ha), (nd, hd) = runRound(p1,p2,ha,hd)
        sa += na
        sd += nd
    return sa, sd



print "Finding warriors in " + sys.argv[1]
players=[sys.argv[1]+exe for exe in os.listdir(sys.argv[1]) if os.access(sys.argv[1]+exe,os.X_OK)]

num_iters = 1
if len(sys.argv) == 3:
    num_iters = int(sys.argv[2])
print "Running %s tournament iterations" % (num_iters)
total_scores={}
for p in players:
    total_scores[p] = 0
for i in range(1,num_iters+1):
    print "Tournament %s" % (i)
    scores={}
    for p in players:
        scores[p] = 0
    for i1 in range(0,len(players)):
        p1=players[i1];
        for i2 in range(i1,len(players)):
            p2=players[i2];
#        rounds = random.randint(50,200)
            rounds = 100
            #print "Running %s against %s (%s rounds)." %(p1,p2,rounds)
            s1,s2 = runGame(rounds,p1,p2)
            #print (s1, s2)
            if (p1 == p2):
                scores[p1] += (s1 + s2)/2
            else:
                scores[p1] += s1
                scores[p2] += s2

    players_sorted = sorted(scores,key=scores.get)
    for p in players_sorted:
        print (p, scores[p])
    winner = max(scores, key=scores.get)
    print "\tWinner is %s" %(winner)
    total_scores[p] += 1
print '-'*10
print "Final Results:"
players_sorted = sorted(total_scores,key=total_scores.get)
for p in players_sorted:
    print (p, total_scores[p])
winner = max(total_scores, key=total_scores.get)
print "Final Winner is " + winner
