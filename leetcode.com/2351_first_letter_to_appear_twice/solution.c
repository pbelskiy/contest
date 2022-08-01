char repeatedCharacter(char *s)
{
    char visited[128] = {0, };

    for (int i = 0 ; i < strlen(s) ; i++) {
        if (++visited[s[i]] == 2)
            return s[i];
    }

    return "";
}
