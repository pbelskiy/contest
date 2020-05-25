#include <stdio.h>
#include <string.h>

#define MAX_LENGHT      100000
#define NUM_DEGREE      20000

int n[MAX_LENGHT];

int debug()
{
    bool skipped = true;
    int sum = 0;

    for (unsigned int i = 0 ; i < MAX_LENGHT ; i++) {
        if (n[i] != 0) {
            skipped = false;
        }

        if (!skipped) {
            sum += n[i];
        }
    }

    return sum;
}

int main()
{
    int m = 0;
    int len = MAX_LENGHT - 1;
    n[MAX_LENGHT - 1] = 2;

    for (int d = 2 ; d <= NUM_DEGREE ; d++) {

        for (int i = MAX_LENGHT - 1 ; i >= 0 ; i--) {


            int r = n[i] * 2;
            if (r < 10) {
                n[i] = r;
                n[i] += m;
                m = 0;
            } else {
                n[i] = (r - 10) + m;
                m = 1;
            }
        }
    }

    // printf("sum is %d\n", debug());
    return 0;
}