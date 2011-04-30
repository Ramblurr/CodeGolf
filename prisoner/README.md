1P5: Iterated Prisoner's Dilemma
----
Author: [dmckee](http://codegolf.stackexchange.com/users/78/dmckee)

Source: http://codegolf.stackexchange.com/questions/2357/1p5-iterated-prisoners-dilemma/2367#2367

***

This task is part of the [First Periodic Premier Programming Puzzle Push][1] and is
intended as demonstration of the new [tag:king-of-the-hill] challenge-type [proposal][2].

**The task is the write a program to play the iterated prisoner's dilemma better than other entrants.**

> Look, Vinny. We know your cellmate---what's his name? Yeah McWongski, the Nippo-Irish-Ukranian mobster--is up to something and you know what it is. 

>We're trying to be nice here, Vinnie. Givin' you a chance. 

>If you tells us what he's plannin' we'll see you get a good work assignment. 

> And if you don't...

The Rules of the Game
---
* The contest consists of a full round-robin (all possible pairing) of two contestants at a time (including self plays).
* There are 100 rounds played between each pair
* In each round each player is asked to choose between cooperating with the other player or betraying them, without knowing the other players intentions in the matter, *but* with a memory of the outcomes of previous rounds played against this opponent.
* Points are awarded for each round based on the combined choice. If both players cooperate they each get 2 points. Mutual betrayal yields 1 point each. In the mixed case, the betraying player is awarded 4 points and the cooperator is penalized by 1.
* An "official" match will be run not sooner than 10 days after posting with all the submissions I can get to work and be used to select the "accepted" winner. I have a Mac OS 10.5 box, so POSIX solutions should work, but there are linuxisms that don't. Likewise, I have no support for the win32 API. I'm willing to make a basic effort to install things, but there is a limit. The limits of my system in no way represent the limits of acceptable responses, simply those that will be included in the "offical" match.

The Programmer's interface
---
* Entries should be in the form of programs that can be run from the command line; the decision must the (sole!) output of the program on the standard output. The history of previous rounds with this opponent will be presented as a command-line argument.
* Output is either "c" (for *clam up*) or "t" (for *tell all*).
* The history is a single string of characters representing previous rounds with the most recent rounds coming earliest in the string. The characters are 
  + "K" (for *kept the faith* meaning mutual cooperation)
  + "R" (for *rat b@st@rd sold me out!*)
  + "S" (for *sucker!* meaning you benefited from a betrayal)
  + "E" (for *everyone is looking out for number one* on mutual betrayal)

The bracket
---
Four players will be provided by the author

* Angel -- always cooperates
* Devil -- always talks
* TitForTat -- Cooperates on the first round then always does as he was done by in the last round 
* Random -- 50/50

to which I will add all the entries that I can get to run.

The total score will be the sum score against all opponents (including self-plays only once and using the average score).

Scorer
---

    #! /usr/bin/python
    #
    # Iterated prisoner's dilemma King of Hill Script Argument is a
    # directory. We find all the executables therein, and run all possible
    # binary combinations (including self-plays (which only count once!)).
    import subprocess 
    import os
    import sys
    
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
    
    def runGame(p1,p2):
        sa, sd = 0, 0
        ha, hd = '', ''
        for a in range(0,100):
            (na, ha), (nd, hd) = runRound(p1,p2,ha,hd)
            sa += na
            sd += nd
        return sa, sd
    
    
    
    print "Finding warriors in " + sys.argv[1]
    players=[sys.argv[1]+exe for exe in os.listdir(sys.argv[1]) if os.access(sys.argv[1]+exe,os.X_OK)]
    scores={}
    for p in players:
        scores[p] = 0
    for i1 in range(0,len(players)):
        p1=players[i1];
        for i2 in range(i1,len(players)):
            p2=players[i2];
            print "Running " + p1 + " against " + p2 + "."
            s1,s2 = runGame(p1,p2)
            #print (s1, s2)
            if (p1 == p2):
                scores[p1] += (s1 + s2)/2
            else:
                scores[p1] += s1
                scores[p2] += s2
    players_sorted = sorted(scores,key=scores.get)
    for p in players_sorted:
        print (p, scores[p])
    print "Winner is " + max(scores, key=scores.get)

 * Complaints about my horrible python are welcome, as I am sure this sucks more than one way
 * Bug fixes welcome

**Scorer Changelog:** 

 * Print sorted players and scores, and declare a winner (Casey)

Initial warriors
---
By way of example, and so that the results can be verified

**Angel**

    #include <stdio.h>
    int main(int argc, char**argv){
      printf("c\n");
      return 0;
    }

or 

    #!/bin/sh
    echo c

or

    #!/usr/bin/python
    print 'c'

**Devil**

    #include <stdio.h>
    int main(int argc, char**argv){
      printf("t\n");
      return 0;
    }

**Random**

    #include <stdio.h>
    #include <stdlib.h>
    #include <time.h>
    #include <unistd.h>
    int main(int argc, char**argv){
      srandom(time(0)+getpid());
      printf("%c\n",(random()%2)?'c':'t');
      return 0;
    }

Note that the scorer may re-invoke the warrior many times in one second, so a serious effort must be made to insure randomness of the results if time is being used to seed the PRNG.

**TitForTat**

    #include <stdio.h>
    #include <stdlib.h>
    
    int main(int argc, char**argv){
      char c='c';
      if (argv[1] && (
    		  (argv[1][0] == 'R') || (argv[1][0] == 'E')
    		  ) ) c='t';
      printf("%c\n",c);
      return 0;
    }

The first one that actually *does something* with the history.


**Running the scorer on only the provided warriors yields**

    Finding warriors in warriors/
    Running warriors/angel against warriors/angel.
    Running warriors/angel against warriors/devil.
    Running warriors/angel against warriors/random.
    Running warriors/angel against warriors/titfortat.
    Running warriors/devil against warriors/devil.
    Running warriors/devil against warriors/random.
    Running warriors/devil against warriors/titfortat.
    Running warriors/random against warriors/random.
    Running warriors/random against warriors/titfortat.
    Running warriors/titfortat against warriors/titfortat.
    ('warriors/angel', 365)
    ('warriors/devil', 832)
    ('warriors/random', 612)
    ('warriors/titfortat', 652)


That devil, he's a craft one, and nice guys apparently come in last.

  [1]: http://meta.codegolf.stackexchange.com/q/298/78
  [2]: http://meta.codegolf.stackexchange.com/q/302/78

