#include <iostream>

using namespace std;

int main()
{
    long unsigned int n = 2520;
    bool found = true;

    while (true) {
        found = true;

        for (int i = 1 ; i <= 20 ; i++) {
            if (n % i != 0) {
                found = false;
                break;
            }
        }
        if (found) break;

        n++;
    }

    cout << n << endl;

    return 0;
}