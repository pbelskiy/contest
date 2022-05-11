char vowels[] = {'a', 'e', 'i', 'o', 'u'};

int cache[5][61];

int get(int i, int r)
{
    if (r == 0)
        return 1;

    if (cache[i][r] != -1)
        return cache[i][r];

    int total = 0;

    for (int j = i ; j < 5 ; j++) {
        total += get(j, r - 1);
    }

    cache[i][r] = total;
    return total;
}

int countVowelStrings(int n)
{
    memset(cache, -1, sizeof(cache));
    return get(0, n);
}
