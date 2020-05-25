#include <stdio.h>

#define GOAL    200
#define SIZE    8

const int values[SIZE] = {200, 100, 50, 20, 10, 5, 2, 1};

int main()
{
    unsigned int coins[SIZE] = {0, 0, 0, 0, 0, 0, 0, 0};
    bool overwritten = false;
    unsigned int ways = 0;

    while (!overwritten) {

        /* +1 */
        for (int j = SIZE - 1; j >= 0 ; j--) {
            if (coins[j] + 1 <= values[j]) {
                coins[j]++;
                break;
            }

            coins[j] = 0;

            if (j == 0)
                overwritten = true;
        }

        unsigned int r = 1 * coins[0] + \
                         2 * coins[1] + \
                         5 * coins[2] + \
                        10 * coins[3] + \
                        20 * coins[4] + \
                        50 * coins[5] + \
                       100 * coins[6] + \
                       200 * coins[7];

        if (r == 200) ways++;
    }

    // 1 min. brute.
    printf("Ways: %u\n", ways);

    // for (int i = 0 ; i < SIZE ; i++) printf("%03d ", coins[i]); printf("\n");
    return 0;
}