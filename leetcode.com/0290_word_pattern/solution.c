#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_CHARS   26
#define NON_TERM(s) (*s != ' ' && *s != '\0')

bool is_same_string(char* s1, char* s2)
{
    while (true) {
        if (!(NON_TERM(s1) || NON_TERM(s2)))
            return true;

        if (*s1 != *s2)
            return false;

        s1++;
        s2++;
    }

    return false;
}

bool wordPattern(char* pattern, char* s)
{
    char* map[MAX_CHARS] = {NULL,};

    for (int pi = 0 ; pi < strlen(pattern) ; pi++)
    {
        /* there are unmapped words */
        if (*s == '\0')
            return false;

        if (pi > 0)
            s++;

        char pc = pattern[pi] - 'a';

        if (map[pc] && !is_same_string(map[pc], s))
            return false;

        for (int j = 0 ; j < MAX_CHARS ; j++) {
            if (j != pc && map[j] && is_same_string(map[j], s))
                return false;
        }

        map[pc] = s;

        /* next word */
        while (NON_TERM(s)) s++;
    }

    if (*s != '\0')
        return false;

    return true;
}

int main()
{
    printf("%d == 0\n", wordPattern("jquery", "jquery"));
    printf("%d == 1\n", wordPattern("abba", "dog cat cat dog"));
    printf("%d == 0\n", wordPattern("abba", "dog dog dog dog"));
    printf("%d == 0\n", wordPattern("aaa", "aa aa aa aa"));
    return 0;
}
