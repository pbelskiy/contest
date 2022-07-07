char *p1, *p2, *p3;
int l1, l2;

int cache[101][101];

bool dfs(int i, int j)
{
    if (cache[i][j] != -1)
        return cache[i][j];

    if (i == l1 && j == l2)
        return true;

    bool r1 = false;
    bool r2 = false;

    if (i < l1 && p1[i] == p3[i+j])
        r1 = dfs(i + 1, j);

    if (j < l2 && p2[j] == p3[i+j])
        r2 = dfs(i, j + 1);

    cache[i][j] = r1 || r2;
    return cache[i][j];
}

bool isInterleave(char *s1, char *s2, char *s3)
{
    l1 = strlen(s1);
    l2 = strlen(s2);

    if (l1 + l2 != strlen(s3))
        return false;

    p1 = s1; p2 = s2; p3 = s3;
    memset(cache, -1, sizeof(cache));
    return dfs(0, 0);
}
