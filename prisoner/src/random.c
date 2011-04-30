#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
int main(int argc, char**argv){
  srandom(time(0)+getpid());
  printf("%c\n",(random()%2)?'c':'t');
  return 0;
}
