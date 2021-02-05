#include <stdbool.h>
#include <stdio.h>
#include <math.h>

#define MAX_NUMBERS 5000000

int countPrimes(int n)
{
    int prime_index = 0;

    for (int i = 2 ; i < MAX_NUMBERS ; i ++) {
        bool found = false;

        for (int j = 2 ; j <= sqrt(i) ; j ++) {
            if (i % j == 0) {
                found = true;
                break;
            }
        }

        if (!found) {
             prime_index++;

            if (i + 1 > n)
                return prime_index - 1;
        }
    }

    return -1;
}

int main()
{
    printf("%d == 0\n", countPrimes(0));
    printf("%d == 0\n", countPrimes(1));
    printf("%d == 0\n", countPrimes(2));
    printf("%d == 4\n", countPrimes(10));

    printf("%d == 41537\n", countPrimes(499979));
    printf("%d == 41537\n", countPrimes(499979));
    return 0;
}
