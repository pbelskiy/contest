int sf(const void *n1, const void *n2)
{
    if (*((int*)n1) > *((int*)n2))
        return 1;
    return 0;
}

int minIncrementForUnique(int *nums, int numsSize)
{
    int total = 0;

    qsort(nums, numsSize, sizeof(int), sf);

    for (int i = 0 ; i < numsSize - 1 ; i++) {
        if (nums[i] < nums[i + 1])
            continue;

        int d = nums[i] - nums[i + 1] + 1;

        total += d;
        nums[i + 1] += d;
     }

     return total;
}
