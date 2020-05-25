#include <stdio.h>
#include <string.h>

#define GOAL    1000000
#define SIZE    6

unsigned char coins[SIZE];

bool is_unique()
{
    unsigned char v[SIZE];

    memset(v, 0, sizeof(unsigned char) * SIZE);

    for (int i = 0 ; i < SIZE ; i++)
        v[coins[i]]++;

    for (int i = 0 ; i < SIZE ; i++)
        if (v[i] != 1)
            return false;

    return true;
}

void print()
{
    for (int i = 0 ; i < SIZE ; i++)
        printf("%d", coins[i]);
    printf("\n");
}

int main()
{
    bool overwritten = false;
    unsigned int ways = 0;

    while (!overwritten) {

        if (is_unique()) {
            print();
            ways++;
            if (ways == GOAL)
                break;
        }

        /* +1 */
        for (int j = SIZE - 1; j >= 0 ; j--) {
            if (coins[j] + 1 < SIZE) {
                coins[j]++;
                break;
            }

            coins[j] = 0;

            if (j == 0)
                overwritten = true;
        }


    }

    // 82 sec. brute force
    printf("Ways: %d\n", ways);
    print();
    return 0;
}