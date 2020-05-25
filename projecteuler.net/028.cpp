#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SPIRAL_SIZE 1001

int spiral[SPIRAL_SIZE][SPIRAL_SIZE];

enum _directions {
    D_RIGHT, D_DOWN, D_LEFT, D_UP
};

void init_spiral()
{
    int y = (SPIRAL_SIZE - 1) / 2;
    int x = y;

    int direction = D_RIGHT;
    int move_count = 1;
    int moves = 1;
    int num = 1;

    while (num <= SPIRAL_SIZE * SPIRAL_SIZE) {
        spiral[y][x] = num;

        switch (direction) {
            case D_RIGHT: x++; break;
            case D_DOWN: y++; break;
            case D_LEFT: x--; break;
            case D_UP: y--; break;
        }

        moves--;

        /* change direction */
        if (moves == 0) {

            if (direction == D_UP) {
                direction = D_RIGHT;
            } else {
                direction += 1;
            }

            if (direction == D_LEFT || direction == D_RIGHT)
                move_count++;

            moves = move_count;
        }

        num++;
    }
}

void print()
{
    for (int y = 0 ; y < SPIRAL_SIZE ; y++) {
        for (int x = 0 ; x < SPIRAL_SIZE ; x++) {
            printf("%03d ", spiral[y][x]);
        }
        printf("\n");
    }
}

int main()
{
    init_spiral();

    // print();

    unsigned long sum = 0;

    /* calc diagonal sum */
    for (int xy = 0 ; xy < SPIRAL_SIZE ; xy++)
        sum += spiral[xy][xy];

    for (int xy = 0 ; xy < SPIRAL_SIZE ; xy++)
        sum += spiral[SPIRAL_SIZE - 1 - xy][xy];

    /* minus '1' in the center */
    printf("Diagonals sum is: %lu\n", sum - 1);
    return 0;
}