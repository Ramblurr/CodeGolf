
int happy(n) {
    while(n != 1 && n!= 4) {
        int tot = 0;
        while( n ) {
            int dig = n%10;
             n /= 10;
             tot += dig*dig;
        }
        n = tot;
    }
    return n == 1;
}
main(int c, char *argv[]) {
    int x = atoi(argv[1]);
    if(happy(x))
        printf("Happy\n");
    else
        printf("UnHappy\n");
return 0;
}
