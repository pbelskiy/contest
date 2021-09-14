#define IS_CHAR(ch)   (('a' <= ch && ch <= 'z') || ('A' <= ch && ch <= 'Z'))

char *reverseOnlyLetters(char *s)
{
    int left = 0;
    int right = strlen(s) - 1;

    while (left < right) {
        if (!IS_CHAR(s[left])) {
            left++;
            continue;
        }

        if (!IS_CHAR(s[right])) {
            right--;
            continue;
        }

        char tmp = s[right];
        s[right] = s[left];
        s[left] = tmp;

        left++;
        right--;
    }

    return s;
}
