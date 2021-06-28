int maxProductDifference(int *nums, int numsSize)
{
    int b1 = 0;
    int b2 = 0;
    int l1 = INT_MAX;
    int l2 = INT_MAX;

    for (int i = 0 ; i < numsSize ; i++) {
        int n = nums[i];

        if (n >= b1) {
            b2 = b1;
            b1 = n;
        } else if (n >= b2) {
            b2 = n;
        }

        if (n <= l1) {
            l2 = l1;
            l1 = n;
        } else if (n <= l2) {
            l2 = n;
        }
    }

    return b1*b2 - l1*l2;
}
