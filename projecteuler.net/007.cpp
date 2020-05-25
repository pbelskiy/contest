#include <iostream>

using namespace std;

bool is_prime(unsigned long n)
{
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

int main()
{
    unsigned long n = 2;
    unsigned long c = 1;

    while (c <= 10001) {
        if (is_prime(n)) c++;
        n++;
    }

    cout << c - 1 << " - " << n - 1 << endl;
    return 0;
}