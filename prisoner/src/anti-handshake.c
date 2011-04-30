/*
Anti-handshake
This is intended to play the secret handshake and if it recognizes the other party as the handshaking cellmate, then sucker-punch him. Otherwise it plays like Tit for Tat.

By Joey
http://codegolf.stackexchange.com/questions/2357/1p5-iterated-prisoners-dilemma/2389#2389
*/

#include <stdio.h>
#include <string.h>

int main(int argc, char* argv[]) {
    char * TAG = "ctttctttct";
    char * TAGMATCH = "EKEEEKEEEK";
    size_t tl;
    char * x;

    tl = argc==1 ? 0 : strlen(argv[1]);

    if (tl < 10) {
        printf("%c\n", TAG[tl]);
    } else {
        x = strstr(argv[1], TAGMATCH);
        if (x != NULL && strlen(x) == 10) {
            printf("t\n");
        } else
            printf("%c\n", (argv[1][0] == 'R' || argv[1][0] == 'E') ? 't' : 'c');
    }

    return 0;
}
