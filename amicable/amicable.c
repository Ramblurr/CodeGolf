#include <math.h>
int s(int n) {
    int sum = 1,i=2;
    double m = n;
    for(;i<=sqrt(m);++i)
        if(n%i==0)sum +=(i+n/i);
    return sum;
}

main()
{
    int s1=0,s2=0,i=1,o=1;
    while(o) {
        s1 = s(i);
        s2 = (s1 > i) ? s(s1) : 0;
        if( s2 == i++) printf("%d,%d\n",i-1,s1);
    }
}
