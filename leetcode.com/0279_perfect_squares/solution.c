#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#define MIN(a, b)   (a < b) ? a : b
#define MAX_LENGTH  10000

int minimum[MAX_LENGTH];

int numSquares(int n)
{
    /* pre compute values */
    if (minimum[1] == 0) {
        for (int i = 1 ; i < MAX_LENGTH ; i++) {
            int ps = (int) floor(sqrt(i));
            int delta = i - ps * ps;

            if (delta == 0) {
                minimum[i] = 1;
            } else {
                minimum[i] = minimum[ps * ps] + minimum[delta];

                for (int j = ps ; j > 0 ; j--) {
                    int delta = i - j * j;

                    minimum[i] = MIN(
                        minimum[i],
                        minimum[j * j] + minimum[delta]
                    );
                }
            }
        }
    }

    return minimum[n];
}

int main()
{
    printf("%d == 4\n", numSquares(7));
    return 0;
}
