int countSubstrings(char *s)
{
    int total = 0;
    int n = strlen(s);

    for (int i = 0 ; i < n ; i++) {
        for (int j = i ; j < n ; j++) {

            int a = i;
            int b = j;
            bool invalid = false;

            while (a < b) {
                if (s[a] != s[b]) {
                    invalid = true;
                    break;
                }

                a += 1;
                b -= 1;
            }

            if (!invalid)
                total += 1;
        }
    }

    return total;
}