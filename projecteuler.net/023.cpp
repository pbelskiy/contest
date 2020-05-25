#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define LIMIT    28123

enum number_types {
    NUM_PERFECT,
    NUM_ABUNDANT,
    NUM_DEFICIENT,
};

int get_num_type(unsigned long long n)
{
    unsigned long long sum = 0;
    unsigned long long d = n / 2;

    while (d > 0) {
        if (n % d == 0)  {
            // printf("%llu - %llu\n", n, d);
            sum += d;
        }

        d--;
    }

    if (sum < n)
        return NUM_DEFICIENT;

    if (sum > n)
        return NUM_ABUNDANT;

    return NUM_PERFECT;
}

int main()
{
    unsigned long long n = 1;
    unsigned long long sum = 0;

    unsigned long long a[6965];

    while (n <= LIMIT) {
        if (get_num_type(n) == NUM_ABUNDANT)
            a[sum++] = n;

        n++;
    }

    unsigned long long total = 0;
    bool found = false;

    for (n = 1 ; n <= LIMIT ; n++)
    {
        found = false;
        for (int i = 0 ; i < sum ; i++) {
            for (int j = 0; j < sum; j++) {
                if (a[i] + a[j] == n) {
                    // printf("%llu + %llu == %llu\n", a[i], a[j], n);
                    found = true;
                    break;
                }
            }

            if (found) break;
        }

        if (!found)
            total += n;
    }

    // 170 sec.
    printf("%llu\n", total);
    return 0;
}