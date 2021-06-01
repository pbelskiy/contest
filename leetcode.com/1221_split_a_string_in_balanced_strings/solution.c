int balancedStringSplit(char *s)
{
    int total = 0;
    int r = 0;
    int l = 0;

    for (int i = 0 ; i < strlen(s) ; i++) {
        if (s[i] == 'R') r++; else l++;

        if (r == l) {
            r = 0;
            l = 0;
            total++;
        }
    }

    return total;
}