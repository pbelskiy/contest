#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define GOAL_LEN    10000
#define MAX_LEN     GOAL_LEN + 1

typedef unsigned char byte;

unsigned long long n1l;
unsigned long long n2l;
unsigned long long n3l;

byte n1[MAX_LEN];
byte n2[MAX_LEN];
byte n3[MAX_LEN];

int op_add(byte *n1, byte *n2)
{
    byte m = 0;

    for (int i = MAX_LEN ; i >= 0 ; i--) {
        byte sum = n1[i] + n2[i] + m;

        if (sum < 10) {
            n1[i] = sum;
            m = 0;
        } else {
            n1[i] = sum % 10;
            m = sum / 10;
        }
    }
}

inline void op_mov(byte *dst, byte *src)
{
    memcpy(dst, src, MAX_LEN);
}

int op_print(byte *n)
{
    bool skip = true;
    int len = 0;

    for (int i = 0 ; i < MAX_LEN ; i++) {

        if (n[i] != 0)
            skip = false;

        if (!skip) {
            printf("%d", n[i]);
            len++;
        }
    }

    printf("\n");
    return len;
}

int op_len(byte *n)
{
    bool skip = true;
    int len = 0;

    for (int i = 0 ; i < MAX_LEN ; i++) {
        if (n[i] != 0)
            skip = false;

        if (!skip)
            len++;
    }

    return len;
}

int main()
{
    unsigned long long index = 2;

    /* first two Fibonacci numbers */
    n1[MAX_LEN - 1] = 1;
    n2[MAX_LEN - 1] = 1;

    while (true) {

/* heuristic */
#if GOAL_LEN > 5
        int heuristic_len = index / 5;

        if (heuristic_len >= GOAL_LEN - 5) {
            if (op_len(n1) >= GOAL_LEN) {
                // op_print(n1);

                printf("index is: %llu\n", index);
                break;
            }
        }
#else
        if (op_len(n1) >= GOAL_LEN) {
            op_print(n1);

            printf("index is: %llu\n", index);
            break;
        }
#endif

        op_mov(n3, n1);
        op_add(n1, n2);
        op_mov(n2, n3);

        index++;
    }

    return 0;
}