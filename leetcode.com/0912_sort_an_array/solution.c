int partition(int *a, int l, int r)
{
    int v  = a[(l+r) / 2];

    while (l <= r) {
        while (a[l] < v)
            l++;
        while (a[r] > v)
            r--;

        if (l >= r)
            break;

        int tmp = a[r];
        a[r] = a[l];
        a[l] = tmp;

        l++;
        r--;
    }

    return r;
}

void sort(int *a, int l, int r)
{
    if (l >= r)
        return;

    int q = partition(a, l, r);
    sort(a, l, q);
    sort(a, q + 1, r);
}

int *sortArray(int *nums, int numsSize, int *returnSize)
{
    sort(nums, 0, numsSize - 1);
    *returnSize = numsSize;
    return nums;
}
