#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

bool isIsomorphic(char* s, char* t)
{
    char* copy = (char*) malloc(strlen(s) + 1);
    char* map_1 = (char*) calloc(sizeof(char), 256);
    char* map_2 = (char*) calloc(sizeof(char), 256);

    strcpy(copy, s);

    for (int i = 0 ; i < strlen(s) ; i++) {

        if (map_1[s[i]])
            continue;

        for (int j = 0 ; j < strlen(t) ; j++) {

            if (map_2[t[j]])
                continue;

            // printf("%c -> %c\n", s[i], t[j]);

            map_1[s[i]] = t[j];
            map_2[t[j]] = s[i];
            break;
        }
    }

    for (int i = 0 ; i < strlen(copy) ; i++)
        copy[i] = map_1[copy[i]];

    printf("%s\n", copy);
    printf("%s\n", t);

    bool r = (strcmp(copy, t) == 0);
    free(copy);
    free(map_1);
    free(map_2);
    return r;
}

int main()
{
    printf("%d == 1\n", isIsomorphic("egg", "add"));
    printf("%d == 0\n", isIsomorphic("bba", "aba"));
    return 0;
}
