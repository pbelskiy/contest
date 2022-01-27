#define MAX(a, b)   (a > b ? a : b)

int maxAscendingSum(int *nums, int numsSize)
{
    int max = nums[0];
    int total = nums[0];

    for (int i = 0 ; i < numsSize ; i++) {
        if (i > 0 && nums[i] > nums[i - 1]) {
            total += nums[i];
        } else {
            max = MAX(max, total);
            total = nums[i];
        }
    }

    return MAX(max, total);
}
