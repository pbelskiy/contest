#include <stdio.h>
#include <string.h>
#include <math.h>

int main()
{
    unsigned long total_sum = 0;

    for (unsigned long n = 10 ; n < 1000000 ; n++) {

        int sum = 0;
        int tmp_n = n;

        while (tmp_n) {
            sum += pow(tmp_n % 10, 5);
            tmp_n /= 10;
        }

        if (sum == n) {
            total_sum += n;
            printf("%lu\n", n);
        }
    }

    printf("\n%lu\n", total_sum);
    return 0;
}