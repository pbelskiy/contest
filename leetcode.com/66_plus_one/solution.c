int* plusOne(int* digits, int digitsSize, int* returnSize)
{
    bool extend = false;
    int out_size = digitsSize + 1;
    int* out_digits = (int*) calloc(sizeof(int), out_size);

    /* copy input */
    for (int i = digitsSize - 1 ; i >= 0 ; i--)
    {
        out_digits[i + 1] = digits[i];
    }

    /* increment */
    for (int i = out_size - 1 ; i >= 0 ; i--)
    {
        if (out_digits[i] + 1 <= 9) {
            out_digits[i]++;
            break;
        }

        out_digits[i] = 0;

        if (i == 1)
            extend = true;
    }

    if (extend == false) {
         for (int i = 0 ; i < out_size - 1 ; i++) {
             out_digits[i] = out_digits[i + 1];
         }

        out_size--;
    }

    *returnSize = out_size;
    return out_digits;
}
