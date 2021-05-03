int removeDuplicates(int *nums, int numsSize)
{
    int removed = 0;

    for (int i = 1 ; i < numsSize - removed ; i++) {
        if (nums[i] != nums[i - 1])
            continue;

        for (int j = i ; j < numsSize - removed - 1; j++) {
            nums[j] = nums[j+1];
        }

        i--;
        removed++;
    }

    return numsSize - removed;
}
