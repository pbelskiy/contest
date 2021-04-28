char *longestCommonPrefix(char **strs, int strsSize)
{
    char *prefix = calloc(sizeof(char), strlen(strs[0]) + 1);
    int len = 0;

    for (int i = 0 ; i < strlen(strs[0]) ; i++) {
        char c = strs[0][i];

        int j = 1;
        for (; j < strsSize ; j++) {
            if (strs[j][i] != c)
                break;
        }

        if (j != strsSize)
            break;

        prefix[len++] = c;
    }

    return prefix;
}
