#include <stdio.h>
#include <string.h>

#define TRIANGLE_HEIGHT 100

int triangle[TRIANGLE_HEIGHT][TRIANGLE_HEIGHT];

int triangle_weight[TRIANGLE_HEIGHT][TRIANGLE_HEIGHT];

void debug()
{
    for (int y = 0 ; y < TRIANGLE_HEIGHT ; y++) {

        for (int p = 0 ; p < TRIANGLE_HEIGHT - y - 1; p++) printf("  ");

        for (int x = 0 ; x < y + 1 ; x++) {

            printf("%03d ", triangle_weight[y][x]);
        }

        printf("\n");
    }
}

void calc_weight(int y, int x)
{
    if (y == 0) {
        triangle_weight[y][x] = triangle[y][x];
        return;
    }

    /* left and right neighbours */
    int ln = -1;
    int rn = -1;

    if (x - 1 >= 0)
        ln = triangle_weight[y - 1][x - 1];

    rn = triangle_weight[y - 1][x - 0];

    if (ln > rn) {
        triangle_weight[y][x] = ln + triangle[y][x];
    } else {
        triangle_weight[y][x] = rn + triangle[y][x];
    }

    // printf("y=%d x=%d neighbours is %d | %d\n", y, x, ln, rn);
}

int main()
{
    FILE *f = fopen("18.txt", "r");

    for (int y = 0 ; y < TRIANGLE_HEIGHT ; y++) for (int x = 0 ; x < y + 1 ; x++)
        fscanf(f, "%d", &triangle[y][x]);

    fclose(f);

    for (int y = 0 ; y < TRIANGLE_HEIGHT ; y++) {
        for (int x = 0 ; x < y + 1 ; x++) {
            calc_weight(y, x);
        }
        printf("\n");
    }
    debug();

    int max = 0;

    for (int x = 0 ; x < TRIANGLE_HEIGHT ; x++)
        if (triangle_weight[TRIANGLE_HEIGHT - 1][x] > max)
            max = triangle_weight[TRIANGLE_HEIGHT - 1][x];

    printf("\n%d\n", max);
    return 0;
}