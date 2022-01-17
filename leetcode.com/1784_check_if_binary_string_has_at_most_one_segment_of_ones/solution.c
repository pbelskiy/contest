bool checkOnesSegment(char *s)
{
    for (int i = 0 ; i < strlen(s) - 1 ; i++) {
        if (s[i] == '0' && s[i + 1] == '1')
            return false;
    }

    return true;
}
