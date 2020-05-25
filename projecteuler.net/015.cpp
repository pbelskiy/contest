#include <stdio.h>
#include <string.h>

// 20x20 = 30 min.

#define GRID_SIZE   2

int grid[GRID_SIZE + 1][GRID_SIZE + 1];

unsigned long ways = 0;

int walk(int y, int x)
{
    grid[y][x]++;

    /* right step */
    if (x + 1 <= GRID_SIZE) {
        walk(y, x + 1);
    }

    /* down step */
    if (y + 1 <= GRID_SIZE) {
        walk(y + 1, x);
    }

    /* final point */
    if (y == GRID_SIZE && x == GRID_SIZE) {
        ways++;
    }

    return 0;
}

void print()
{
    for (int i = 0 ; i <= GRID_SIZE ; i++ ) {
        for (int j = 0 ; j <= GRID_SIZE ; j++ ) {
            printf("%03d ", grid[i][j]);
        }
        printf("\n");
    }
}

int main()
{
    walk(0, 0);
    print();
    printf("\n%lu\n", ways);
    return 0;
}