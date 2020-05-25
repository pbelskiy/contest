#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LENGHT      1024 * 15

char * convert(int *n1, bool print)
{
    bool skipped = true;
    int sum = 0;
    int p = 0;

    char * result = (char *) calloc(MAX_LENGHT, sizeof(int));

    for (unsigned int i = 0 ; i < MAX_LENGHT ; i++) {
        if (n1[i] != 0) {
            skipped = false;
        }

        if (!skipped) {
            result[p++] = n1[i] + 0x30;

            if (print)
                printf("%d", n1[i]);
        }
    }

    if (print)
        printf("\n");

    return result;
}

void op_mul(int *n1, int n2)
{
    int m = 0;

    for (int i = MAX_LENGHT - 1 ; i >= 0 ; i--)
    {
        int sum = n1[i] * n2 + m;

        if (sum == 0 && m != 0) {
            n1[i] = m;
            m = 0;
            continue;
        }

        if (sum < 10) {
            n1[i] = sum;
            m = 0;
        } else {
            n1[i] = sum % 10;

            m = sum / 10;
        }
    }
}

void op_add(int *n1, int *n2)
{
    int m = 0;

    for (int i = MAX_LENGHT - 1 ; i >= 0 ; i--)
    {
        int sum = n1[i] + n2[i] + m;

        if (sum < 10) {
            n1[i] = sum;
            m = 0;
        } else {
            n1[i] = sum % 10;

            m = sum / 10;
        }
    }
}

void op_left_shift(int *n1)
{
    for (int i = 0 ; i < MAX_LENGHT - 1 ; i++)
        n1[i] = n1[i + 1];

    n1[MAX_LENGHT - 1] = 0;
}

int * mul_two(const char *n1, const char *n2)
{
    int *pool[MAX_LENGHT];

    for (int rank = strlen(n2) - 1; rank >= 0  ; rank--) {
        pool[rank] = (int *) calloc(MAX_LENGHT, sizeof(int));

        for (int i = 0 ; i < strlen(n1) ; i++) {
            pool[rank][MAX_LENGHT - strlen(n1) + i] =  n1[i] - 0x30;
        }

        op_mul(pool[rank], n2[rank] - 0x30);

        for (int i = 0 ; i < strlen(n2) - rank - 1 ; i++)
            op_left_shift(pool[rank]);
    }

    for (int rank = 1; rank < strlen(n2) ; rank++) {
        op_add(pool[0], pool[rank]);
        free(pool[rank]);
    }

    return pool[0];
}

#define FACTORIAL   1000

int main()
{
    char buff[MAX_LENGHT];
    int *nr = mul_two("1", "2");
    char *result = convert(nr, false);
    int n = 3;
    unsigned long long sum = 0;

    while (n <= FACTORIAL) {
        sprintf(buff, "%d", n);
        nr = mul_two(result, buff);
        free(result);

        result = convert(nr, false);
        n++;

        if (n == FACTORIAL) {
            for (int i = 0 ; i < MAX_LENGHT ; i++)
                sum += nr[i];

            free(nr);
            break;
        }

        free(nr);
    }

    printf("%llu\n", sum);
    // printf("%s\n", result);
    free(result);
    return 0;
}