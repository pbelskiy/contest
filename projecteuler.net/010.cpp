#include <iostream>
#include <math.h>

using namespace std;

bool is_prime(unsigned long n)
{
    unsigned long x = sqrt(n);

    while (x > 1) {
        if (n % x == 0)
            return false;
        x--;
    }

    return true;
}

int main()
{
    unsigned long sum = 0;

    for (unsigned long n = 2 ; n < 2 * 1000 * 1000 ; n++) {
        if (is_prime(n)) {
            sum += n;
        }
    }

    cout << sum << endl;
    return 0;
}