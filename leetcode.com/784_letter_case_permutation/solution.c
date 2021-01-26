#include <ctype.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char** letterCasePermutation(char* S, int* returnSize)
{
    int letters = 0;
    int count = 0;
    int length = strlen(S);

    for (int i = 0 ; i < length ; i++) {
        if (isdigit(S[i]))
            continue;

        letters++;
    }

    count = 1;
    if (letters > 0)
        count = pow(2, letters);

    char** cases = malloc(sizeof(char*) * count);

    for (int i = 0 ; i < count ; i++)
        cases[i] = malloc(sizeof(char) * (length + 1));

    strcpy(cases[0], S);

    for (int i = 1 ; i < count ; i++)
    {
        strcpy(cases[i], cases[i - 1]);

        for (int j = length ; j >= 0 ; j--) {
            if (isdigit(cases[i][j]))
                continue;

            if (islower(cases[i][j])) {
                cases[i][j] = toupper(cases[i][j]);
                break;
            }

            cases[i][j] = tolower(cases[i][j]);
        }
    }

    *returnSize = count;
    return cases;
}

int main()
{
    int count;
    char** cases = letterCasePermutation("a1b2", &count);

    for (int i = 0 ; i < count ; i++) {
        printf("%s\n", cases[i]);
        free(cases[i]);
    }

    free(cases);
    return 0;
}
