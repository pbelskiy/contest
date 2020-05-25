#include <iostream>

using namespace std;

int main()
{
    long int s = 0;
    long int b = 1;
    long int n = 1;

    while (n < 4 * 1000 * 1000) {
        // cout << n << " ";

        if (n % 2 == 0) s += n;

        long int tmp = n;
        n += b;
        b = tmp;
    }

    cout << s << endl;

    return 0;
}