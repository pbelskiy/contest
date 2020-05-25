#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LAYERS  17
#define MAX_LENGTH  131072 // 2^MAX_LAYERS

int layers[MAX_LAYERS][MAX_LENGTH];

void print(int n)
{
    printf("-------------------------------\n");
    for (int l = 0 ; l <= n ; l++) {
        for (int i = 0 ; i < pow(2, n - l) ; i++) {
            printf("%d ", layers[l][i]);
        }
        printf("\n");
    }
    printf("-------------------------------\n\n");
}

int solve(int n, int p)
{
    for (int l = 1 ; l <= n ; l++) {

        int i1 = p;
        int i2 = p;

        if (p % 2 == 0)
            i2 += 1;
        else
            i2 -= 1;

        // printf("-> %d | %d\n", i1, i2);

        p >>= 1;

        if (l % 2 == 1) {
            layers[l][p] = layers[l-1][i1] | layers[l-1][i2];
        } else {
            layers[l][p] = layers[l-1][i1] ^ layers[l-1][i2];
        }

        // print(n);
    }

    return layers[n][0];
}

void construct(int n)
{
    for (int l = 1 ; l <= n ; l++) {
        for (int i = 0 ; i < pow(2, n - l) ; i++) {
            if (l % 2 == 1)
                layers[l][i] = layers[l-1][i<<1] | layers[l-1][(i<<1)+1];
            else
                layers[l][i] = layers[l-1][i<<1] ^ layers[l-1][(i<<1)+1];
        }
    }

    // print(n);
}

int main()
{
    int n, m, i, p, b;

    // freopen("input.txt", "r", stdin);
    // setbuf(stdout, NULL);

    scanf("%d %d", &n, &m);

    for (i = 0; i < pow(2, n) ; i++) {
        scanf("%d", &layers[0][i]);
    }

    construct(n);

    for (i = 0; i < m ; i++) {
        scanf("%d %d", &p, &b);
        p -= 1;
        layers[0][p] = b;
        printf("%d\n", solve(n, p));
        // break;
    }

    return 0;
}

