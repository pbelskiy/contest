int *addToArrayForm(int *num, int numSize, int k, int *returnSize)
{
    int cap = numSize + 10;
    int len = 0;
    int carry = 0;
    int *array = calloc(sizeof(int), cap);

    for (int i = numSize - 1 ; i >= 0 ; i--) {
        int v = num[i] + k % 10 + carry;

        // printf("%d + %d + %d = %d\n", k % 10, num[i], carry, v);

        if (v > 9) {
            carry = v / 10;
            v = v % 10;
        } else {
            carry = 0;
        }

        array[cap - len - 1] = v;

        len += 1;
        k /= 10;
    }

    while (k > 0) {
        int v = k % 10 + carry;

        if (v > 9) {
            carry = v / 10;
            v = v % 10;
        } else {
            carry = 0;
        }

        array[cap - len - 1] = v;

        len += 1;
        k /= 10;
    }

    if (carry > 0) {
        array[cap - len - 1] = carry;
        len += 1;
    }

    if (len < cap) {
        for (int i = 0 ; i < len ; i++)
            array[i] = array[cap - len + i];

        cap -= cap - len;
    }

    *returnSize = cap;
    return array;
}
