#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define UPPER_LIMIT 1000
#define MAX_LEN     UPPER_LIMIT * 2

unsigned char fraction[MAX_LEN];

int get_recurring_cycle()
{
    bool found = false;
    int fl = 1;
    int limit = 1;

    while (!found && limit < MAX_LEN) {
        found = true;

        for (int i = 0 ; i <= limit ; i++) {

            if (fraction[i] != fraction[limit + i]) {
                found = false;
                break;
            }

            if (i > fl)
                fl = i;
        }

        limit++;
    }

    return fl;
}

void op_div(unsigned int n)
{
    int d = 1 * 10;;

    memset(fraction, 0 , sizeof(unsigned char) * MAX_LEN);

    for (int x = 0 ; x < MAX_LEN ; x++) {
        if (d < n)
            d = d * 10;

        int r = 1;

        while (n * r <= d)
            r++;
        r--;

        d = (d - n * r);

        fraction[x] = r;
    }
}

int main()
{
    int max = 0;
    int num = 0;

    for (int n = 2 ; n < UPPER_LIMIT; n++) {
        op_div(n);

        int l = get_recurring_cycle();
        printf("Fract (1 / %03d) size: %d\n", n, l);

        if (l > max) {
            num = n;
            max = l;
        }
    }

    // 0.1 seconds
    printf("\nNumber is: %d, fraction len: %d\n", num, max);
    return 0;
}