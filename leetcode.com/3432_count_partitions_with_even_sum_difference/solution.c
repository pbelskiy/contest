int countPartitions(int *nums, int numsSize)
{
    int left = 0;
    int right = 0;

    for (int i = 0 ; i < numsSize ; i++)
        right += nums[i];

    int total = 0;
    for (int i = 0 ; i < numsSize - 1 ; i++) {
        left += nums[i];
        right -= nums[i];

        if ((right - left) % 2 == 0) {
            total++;
        }
    }

    return total;
}
