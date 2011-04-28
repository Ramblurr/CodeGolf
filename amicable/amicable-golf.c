s(n){int x=1,i=2;for(;i<=sqrt(n);++i)if(n%i==0)x+=i+n/i;return x;}main(i,a){for(;;)a=s(i),((a>i)?s(a):0)==i++?printf("%d,%d\n",i-1,a):0;}
