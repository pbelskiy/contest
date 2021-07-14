int *getConcatenation(int *nums, int numsSize, int *returnSize)
{
    int *array = malloc(sizeof(int) * numsSize * 2);

    for (int i = 0 ; i < numsSize ; i++)
        array[i] = array[numsSize + i] = nums[i];

    *returnSize = numsSize * 2;
    return array;
}
