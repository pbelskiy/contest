int *selfDividingNumbers(int left, int right, int *returnSize)
{
    int *list = malloc(sizeof(int) * (right - left + 1));
    int count = 0;

    for (int n = left ; n <= right ; n++) {
        int x = n;
        bool ok = true;

        while (x > 0) {
            int ln = x % 10;

            if (ln == 0) {
                ok = false;
                break;
            }

            if (n % ln != 0) {
                ok = false;
                break;
            }

            x /= 10;
        }

        if (ok) {
            list[count++] = n;
        }
    }

    *returnSize = count;
    return list;
}
