int search(int *nums, int numsSize, int target)
{
    int lo = 0;
    int hi = numsSize;

    while (lo < hi) {
        int mid = (hi + lo) / 2;

        if (nums[mid] == target)
            return mid;

        if (nums[mid] < target)
            lo = mid + 1;
        else
            hi = mid;
    }

    return -1;
}
