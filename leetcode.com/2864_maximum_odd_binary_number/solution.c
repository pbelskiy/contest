char *maximumOddBinaryNumber(char *s)
{
    int left = 0;
    int ones = 0;
    int length = strlen(s);

    /* move all bits to the left side */
    for (int i = 0 ; i < length ; i++) {
        if (s[i] == '0')
            continue;

        int tmp = s[left];
        s[left++] = s[i];
        s[i] = tmp;
        ones++;
    }

    /* move less significant 1 bit to the end to make it odd */
    if (ones < length)
        s[ones - 1] = '0';
    s[length - 1] = '1';
    return s;
}