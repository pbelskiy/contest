int lengthOfLastWord(char *s)
{
    int len = 0;
    bool new = false;

    while (*s != '\0') {

        if (*s == ' ') {
            new = true;
        } else {
            if (new) {
                len = 0;
                new = false;
            }

            len++;
        }

        s++;
    }

    return len;
}