#include <stdio.h>
#include <string.h>

#define MIN_A   2
#define MAX_A   5

#define MIN_B   2
#define MAX_B   5

#define MAX_SIZE    (MAX_A - MIN_A + 1) * (MAX_B - MIN_B + 1)

unsigned long long discovered[MAX_SIZE];



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

void op_pow2()
{
    int m = 0;
    int len = MAX_LENGHT - 1;
    n[MAX_LENGHT - 1] = 2;

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

int main()
{
    int count = 0;
    bool already_added;

    for (int a = MIN_A ; a <= MAX_A ; a++) {

        for (int b = MIN_B ; b <= MAX_B ; b++) {

            unsigned long long n = pow(a, b);

            already_added = false;

            for (int i = 0 ; i < count ; i++) {
                if (discovered[i] == n) {
                    already_added = true;
                    break;
                }
            }

            if (!already_added) {
                discovered[count] = n;
                count++;
            }

        }

    }

    for (int i ; i < count ; i++)
        printf("%lu\n", discovered[i]);

    printf("Count: %d\n", count);
    return 0;
}