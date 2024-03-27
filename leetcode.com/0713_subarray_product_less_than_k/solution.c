int numSubarrayProductLessThanK(int *nums, int numsSize, int k) {
    int total = 0;

    for (int i = 0 ; i < numsSize ; i++) {
        int p = 1;
        for (int j = i ; j < numsSize ; j++) {
            if (p*nums[j] >= k)
                break;
            p *= nums[j];
            total++;
        }
    }

    return total;
}
