/*
Mistrust (variant)

By Joey
http://codegolf.stackexchange.com/questions/2357/1p5-iterated-prisoners-dilemma/2358#2358
*/
#include <stdio.h>
#include <string.h>

int main(int argc, char* argv[]) {
    if (argc == 1)
        printf("t\n");
    else switch (strlen(argv[1])) {
        case 0:
            printf("t\n");
            break;
        case 1:
        case 2:
            printf("c\n");
            break;
        default:
            if (argv[1][0] == 'R' || argv[1][0] == 'E')
                printf("t\n");
            else
                printf("c\n");
            break;
    }

    return 0;
}
