#define MAX_CHARS 500

char *reformat(char *s)
{
    int l = 0, n = 0;

    char *letters = malloc(MAX_CHARS);
    char *numbers = malloc(MAX_CHARS);

    for (int i = 0 ; i < strlen(s) ; i++) {
        if (s[i] >= 'a') {
            letters[l++] = s[i];
        } else {
            numbers[n++] = s[i];
        }
    }

    if (l - n > 1 || n - l > 1)
        return "";

    char *string = calloc(l + n + 1 + 100, 1);
    int i = 0, j = 0, k = 0;

    if (l >= n) {
        while (i < strlen(s)) {
            if (j < l)
                string[i++] = letters[j++];
            if (k < n)
                string[i++] = numbers[k++];
        }
    } else if (n > l) {
        while (i < strlen(s)) {
            if (k < n)
                string[i++] = numbers[k++];
            if (j < l)
                string[i++] = letters[j++];
        }
    }

    return string;
}
