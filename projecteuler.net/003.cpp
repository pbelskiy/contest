#include <iostream>

using namespace std;

int main()
{
    long unsigned int input = 600851475143;

    unsigned int n = 1;

    while (input > 1) {
        n++;
        while (input % n == 0) input /= n;
    }

    cout << n << endl;
    return 0;
}