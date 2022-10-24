int compare(void *a, void *b)
{
    return *((int*)a) < *((int*)b);
}

int *findErrorNums(int *nums, int numsSize, int *returnSize)
{
    *returnSize = 2;
    int *set = malloc(sizeof(int)*2);
    qsort(nums, numsSize, sizeof(int), compare);

    int sum_should = numsSize*(numsSize + 1) / 2;
    int sum_actual = nums[0];

    for (int i = 1 ; i < numsSize ; i++) {
        sum_actual += nums[i];

        if (nums[i] == nums[i - 1])
            set[0] = nums[i];
    }

    set[1] = set[0] + (sum_should - sum_actual);
    return set;
}
