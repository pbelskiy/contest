inline void fill(char *a, int l, int r, char ch)
{
    for (auto int j = l ; j <= r ; j++) a[j] = ch;
}

char *pushDominoes(char *dominoes)
{
    int len = strlen(dominoes);
    int l = 0;
    int r = -1;

    for (auto int i = 0 ; i < len ; i++) {
        if (dominoes[i] == '.')
            continue;

        if (dominoes[i] == 'L') {
            if (r == -1) {
                fill(dominoes, l, i, 'L');
            } else {
                int mid = (i - r - 1) / 2;
                fill(dominoes, r + 1, r + mid, 'R');
                fill(dominoes, i - mid, i - 1, 'L');
                r = -1;
                l = i;
            }
        } else if (dominoes[i] == 'R') {
            if (r != -1)
                fill(dominoes, r, i, 'R');
            r = i;
        }
    }

    if (r != -1)
        fill(dominoes, r, len - 1, 'R');

    return dominoes;
}
