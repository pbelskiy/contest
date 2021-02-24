int* searchRange(int* nums, int numsSize, int target, int* returnSize)
{
    int min = 0, mid = 0, max = numsSize - 1;
    int* result = (int*) malloc(sizeof(int) * 2);
    *returnSize = 2;

    result[0] = -1;
    result[1] = -1;

    if (numsSize == 0)
        return result;

    while (true) {
        if (min > max)
            return result;

        mid = min + ((max - min) / 2);

        if (nums[mid] == target)
            break;
        else if (nums[mid] > target)
            max = mid - 1;
        else if (nums[mid] < target)
            min = mid + 1;
    }

    result[0] = mid;
    result[1] = mid;

    /* backward */
    mid = result[0];
    while (mid >= 0 && nums[mid] == target) {
        result[0] = mid--;
    }

    /* forward */
    mid = result[1];
    while (mid < numsSize && nums[mid] == target) {
        result[1] = mid++;
    }

    return result;
}
