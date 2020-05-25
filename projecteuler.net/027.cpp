#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define MAX_A   1000
#define MAX_B   1000

#define MAX( a, b ) ( ( a > b) ? a : b )

bool is_prime(unsigned long n)
{
    n = floor(sqrt(n));

    unsigned long x = n - 1;

    if (n > 2 && n % 2 == 0)
        return false;

    while(x > 1) {
        if (n % x == 0)
            return false;
        x--;
    }

    return true;
}

unsigned int get_prime_count(int a, int b)
{
    unsigned int count = 0;

    for (int n = 0 ; n < MAX(abs(a), abs(b)) ; n++) {

        unsigned long r = (n * n) + (n * a) + b;

        if (is_prime(r)) {
            // printf("%lu\n", r);
            count++;
        }

    }

    return count;
}

int main()
{
    unsigned int count;
    int _a = 0;
    int _b = 0;
    int _c = 0;

    // _a = -79;
    // _b = 1601;
    // _c = get_prime_count(_a, _b);

    for (int a = 0 ; a < MAX_A ; a++ ) {

        printf("a = %d\n", a);
        fflush(stdout);

        if (a % 2 == 0 && a > 0)
            continue;

        for (int b = 0 ; b < MAX_B ; b++) {

            // printf("b = %d\n", b);

            count = get_prime_count(a, b);

            if (count > _c) {
                _a = a;
                _b = b;
                _c = count;
            }

        }
    }

    printf("n^2 + %dn + %d = %d\n", _a, _b, _c);

    printf("Product of the coefficients is: %d\n", _a * _b);
    return 0;
}