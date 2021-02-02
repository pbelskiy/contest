#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int calculate(char* s)
{
    int sum = 0;
    unsigned int val = 0;
    bool add = true;
    int level = -1;
    int capacity = 1000;

    int* lsum = (int*) malloc(sizeof(int) * capacity);
    bool* ladd = (bool*) malloc(sizeof(bool) * capacity);

    for (int i = 0 ; s[i] != '\0' ; i++) {
        switch (s[i]) {
            case ' ':
                break;

            case '(':
                if (level + 10 > capacity) {
                    capacity *= 2;
                    lsum = (int*) realloc(lsum, sizeof(int) * capacity);
                    ladd = (bool*) realloc(ladd, sizeof(bool) * capacity);
                }

                level++;
                ladd[level] = add;
                lsum[level] = sum;
                sum = 0;
                add = true;
                break;

            case ')':
                if (level < 0)
                    break;

                if (ladd[level]) {
                    sum = lsum[level] + sum;
                } else {
                    sum = lsum[level] - sum;
                }

                level--;
                break;

            case '-':
                add = false;
                break;

            case '+':
                add = true;
                break;

            default:
                val = 0;
                while (s[i] >= '0' && s[i] <= '9' && s[i] != '\0') {
                    val = val * 10 + s[i] - '0';
                    i++;
                }

                i--;

                if (add)
                    sum += val;
                else
                    sum -= val;
        }
    }

    free(ladd);
    free(lsum);
    return sum;
}

int main()
{
    // printf("%d == 2\n", calculate("1 + 1"));
    // printf("%d == 4\n", calculate("3-(4-5)"));
    // printf("%d == -6\n", calculate("(0-(6))"));
    // printf("%d == -1\n", calculate("(9-10)"));
    // printf("%d == 23\n", calculate("(1+(4+5+2)-3)+(6+8)"));
    // printf("%d == -2\n", calculate("(9-(10+1))"));
    printf("%d == 2147483647\n", calculate("2147483647"));
    return 0;
}
