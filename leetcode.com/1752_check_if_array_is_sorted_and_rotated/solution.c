bool check(int* nums, int numsSize)
{
    int transitions = 0;

    for (int i = 0 ; i < numsSize - 1 ; i++) {
        if (nums[i] > nums[i + 1])
            transitions++;
    }

    if (nums[numsSize - 1] > nums[0])
        transitions++;

    return (transitions > 1) ? false : true;
}
