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
