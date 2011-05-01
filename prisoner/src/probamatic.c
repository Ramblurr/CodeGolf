#include <stdio.h>

void counts(char* str, int* k, int* r, int* s, int* e) {
    *k = *r = *s = *e = 0;
    for (char c = *str; c = *str; str++) {
        switch (c) {
            case 'K': (*k)++; break;
            case 'R': (*r)++; break;
            case 'S': (*s)++; break;
            case 'E': (*e)++; break;
        }
    }
}

// Calculates the expected value of cooperating and defecting in this round. If we haven't cooperated/defected yet, a 50% chance of the opponent defecting is assumed.
void expval(int k, int r, int s, int e, float* coop, float* def) {
    if (!k && !r) {
        *coop = .5;
    } else {
        *coop = 2 * (float)k / (k + r) - (float)r / (k + r);
    }
    if (!s && !e) {
        *def = 2.5;
    } else {
        *def = 4 * (float)s / (s + e) + (float)e / (s + e);
    }
}

int main(int argc, char** argv) {
    if (argc == 1) {
        // Always start out nice.
        putchar('c');
    } else {
        int k, r, s, e;
        counts(argv[1], &k, &r, &s, &e);
        float coop, def;
        expval(k, r, s, e, &coop, &def);
        if (coop > def) {
            putchar('c');
        } else {
            // If the expected values are the same, we can do whatever we want.
            putchar('t');
        }
    }
    return 0;
}
