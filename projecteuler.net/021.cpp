#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int func_d(int n)
{
    int sum = 0;

    for (int i = n - 1 ; i > 0 ; i--)
        if (n % i == 0)
            sum += i;

    return sum;
}

int main()
{
    int sum = 0;

    for (int i = 0 ; i < 10000 ; i++) {
        int r = func_d(i);

        if (func_d(r) == i && r != i) {
            printf("%d %d\n", i, r);
            sum += i + r;

            i = r;
        }
    }

    printf("\n%d\n", sum);
    return 0;
}