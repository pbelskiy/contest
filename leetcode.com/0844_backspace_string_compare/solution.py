void trim(int *i, char *s, int *b)
{
    while (*i >= 0 && s[*i] == '#') {
        while (*i >= 0 && s[*i] == '#') { (*b)++; (*i)--; }
        while (*i >= 0 && *b > 0 && s[*i] != '#') { (*b) -= 1; (*i)--;}
    }
}

bool backspaceCompare(char *s, char *t)
{
    int i = strlen(s) - 1;
    int j = strlen(t) - 1;

    int ib = 0;
    int jb = 0;

    while (true) {
        trim(&i, s, &ib);
        trim(&j, t, &jb);

        if (i < 0 || j < 0)
            break;

        if (i >= 0 && j >= 0 && s[i] != t[j])
            return false;

        i--; j--;
    }

    return i == j;
}
