// Runtime: 0 ms, faster than 100.00% of C online submissions for Sequential Digits.
// Memory Usage: 5.7 MB, less than 100.00% of C online submissions for Sequential Digits.

#define MAX_VARIANTS    36

int v[MAX_VARIANTS] = {
    12, 23, 34, 45, 56, 67, 78, 89,
    123, 234, 345, 456, 567, 678, 789,
    1234, 2345, 3456, 4567, 5678, 6789,
    12345, 23456, 34567, 45678, 56789,
    123456, 234567, 345678, 456789,
    1234567, 2345678, 3456789,
    12345678, 23456789, 123456789
};

int* sequentialDigits(int low, int high, int* returnSize)
{
    int *r = malloc(MAX_VARIANTS * sizeof(int));
    int count = 0;

    for (int i = 0 ; i < MAX_VARIANTS ; i++)
        if (v[i] >= low && v[i] <= high)
            r[count++] = v[i];

    *returnSize = count;
    return r;
}