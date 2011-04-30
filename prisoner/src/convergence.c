/* convergence
 *
 * A iterated prisoners dilemma warrior for
 *
 * Strategy is to randomly chose an action based on the opponent's
 * history, weighting recent rounds most heavily. Important fixed
 * point, we should never be the first to betray.
 */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <string.h>

int main(int argc, char**argv){
  srandom(time(0)+getpid()); /* seed the PRNG */
  unsigned long m=(1LL<<31)-1,q,p=m;
  if (argc>1) {
    size_t i,l=strlen(argv[1]);
    for (i=l; --i<l; ){
      switch (argv[1][i]) {
      case 'R':
      case 'E':
    q = 0;
    break;
      case 'K':
      case 'S':
    q = m/3;
    break;
      }
      p/=3;
      p=2*p+q;
    }
  }
  /* printf("Probability of '%s' is %g.\n",argv[1],(double)p/(double)m); */
  printf("%c\n",(random()>p)?'t':'c'); 
  return 0;
}
