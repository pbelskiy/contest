int minimumSize(int *nums, int numsSize, int maxOperations)
{
    int lo = 1;
    int hi = 0;

    for (int i = 0 ; i < numsSize ; i++) {
        if (nums[i] > hi)
            hi = nums[i];
    }

    while (lo <= hi) {
        int mid = (lo + hi) / 2;

        // check is possible
        int t = maxOperations;
        for (int i = 0 ; i < numsSize ; i++) {
            t -= ceil((double)(nums[i] - mid) / mid);
        }

        if (t >= 0) {
            hi = mid - 1;
        } else {
            lo = mid + 1;
        }
    }

    return lo;
}
