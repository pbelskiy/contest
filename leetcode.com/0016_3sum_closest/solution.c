#define ABS(a, b)   ((a > b) ? a - b : b - a)

int get_pivot(int *nums, int left, int right)
{
    int n = nums[(left + right) / 2];

    while (left <= right) {
        while (nums[left] < n)
            left++;

        while (nums[right] > n)
            right--;

        if (left >= right)
            break;

        int tmp = nums[left];
        nums[left] = nums[right];
        nums[right] = tmp;

        left++;
        right--;
    }

    return right;
}

void quicksort(int *nums, int left, int right)
{
    if (left >= right)
        return;

    int p = get_pivot(nums, left, right);
    quicksort(nums, left, p);
    quicksort(nums, p + 1, right);
}

int threeSumClosest(int *nums, int numsSize, int target)
{
    quicksort(nums, 0, numsSize - 1);

    int closest = 0;
    int delta = INT_MAX;

    for (int i = 0 ; i < numsSize - 2 ; i++) {
        int left = i + 1;
        int right = numsSize - 1;

        while (left < right) {
            int sum = nums[i] + nums[left] + nums[right];

            if (sum == target) {
                return sum;
            } else if (sum > target) {
                right--;
            } else {
                left++;
            }

            int _d = ABS(sum ,target);

            if (_d < delta) {
                delta = _d;
                closest = sum;
            }
        }
    }

    return closest;
}
