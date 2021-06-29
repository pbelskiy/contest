#define MAX(a, b)   ((a > b) ? (a) : (b))

int maxLengthBetweenEqualCharacters(char *s)
{
    int p1[26] = {0,};
    int p2[26] = {0,};

    for (int i = 1 ; *(s + i - 1) != '\0' ; i++) {
        char x = *(s + i - 1) - 'a';

        if (p1[x] == 0) {
            p1[x] = i;
        } else {
            p2[x] = i;
        }

    }

    int distance = -1;

    for (int i = 0 ; i < 26 ; i++) {
        if (p1[i] != 0)
            distance = MAX(distance, p2[i] - p1[i] - 1);
    }

    return distance;
}
