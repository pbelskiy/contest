int removeDuplicates(int *nums, int numsSize)
{
    int prev = nums[0];
    int count = 1;
    int removed = 0;

    for (int i = 1 ; i < numsSize - removed ; i++) {

        if (nums[i] != prev) {
            prev = nums[i];
            count = 1;
            continue;
        }

        count++;
        if (count <= 2)
            continue;

        int extra = 1;
        while (i + extra < numsSize - removed && nums[i + extra] == nums[i])
            extra++;

        for (int j = i ; j + extra < numsSize ; j++)
            nums[j] = nums[j + extra];

        removed += extra;

        if (i >= numsSize - removed)
            break;

        i--;
    }

    return numsSize - removed;
}
