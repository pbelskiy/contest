#include <iostream>

using namespace std;

#define MAX_NUM 100

int main()
{
    unsigned long s1 = 0;
    unsigned long s2 = 0;

    for (int i = 1 ; i <= MAX_NUM ; i++) {
        s1 += i;
    }

    s1 = s1 * s1;

    for (int i = 1 ; i <= MAX_NUM ; i++) {
        s2 += i * i;
    }

    cout << s1 - s2 << endl;

    return 0;
}