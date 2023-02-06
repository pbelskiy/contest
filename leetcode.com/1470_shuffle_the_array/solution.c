int *shuffle(int *nums, int numsSize, int n, int *returnSize)
{
    int *a = calloc(sizeof(int), numsSize);

    for (int i = 0 ; i < n ; i++) {
        a[i*2] = nums[i];
        a[i*2+1] = nums[n+i];
    }

    *returnSize = numsSize;
    return a;
}
