int *sumEvenAfterQueries(
    int *nums,
    int numsSize,
    int **queries,
    int queriesSize,
    int *queriesColSize,
    int *returnSize)
{
    int sum = 0;
    int *r = malloc(sizeof(int)*queriesSize);

    for (int i = 0 ; i < numsSize ; i++)
        if (nums[i] % 2 == 0) sum += nums[i];

    for (int i = 0 ; i < queriesSize ; i++) {
        int n = queries[i][0];
        int j = queries[i][1];

        if (nums[j] % 2 == 0)
            sum -= nums[j];

        nums[j] += n;

        if (nums[j] % 2 == 0)
            sum += nums[j];

        r[i] = sum;
    }

    *queriesColSize = 1;
    *returnSize = queriesSize;
    return r;
}
