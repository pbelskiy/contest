char *replaceDigits(char *s)
{
    for (int i = 1 ; i < strlen(s) ; i += 2)
        s[i] = s[i-1] + s[i] - '0';

    return s;
}