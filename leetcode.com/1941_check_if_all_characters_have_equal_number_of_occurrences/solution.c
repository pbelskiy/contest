#define TOTAL_CHARS 26

bool areOccurrencesEqual(char *s)
{
    int count[TOTAL_CHARS] = {0,};

    for (int i = 0 ; i < strlen(s) ; i++)
        count[s[i] - 'a']++;

    for (int i = 0 ; i < TOTAL_CHARS ; i++)
        if (count[i] == 0)
            count[i] = count[s[0] - 'a'];

    for (int i = 0 ; i < TOTAL_CHARS - 1; i++)
        if (count[i] != count[i + 1])
            return false;

    return true;
}
