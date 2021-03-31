/* inspired by https://leetcode.com/problems/total-hamming-distance/discuss/720409/Python-Bit-Manipulation-Explanation-with-Diagram */

int totalHammingDistance(int* nums, int numsSize)
{
    int diff_count = 0;

    for (int shift = 0 ; shift < sizeof(int)*8 ; shift++) {
        int count_of_0 = 0;
        int count_of_1 = 0;

        for (int i = 0 ; i < numsSize ; i++) {
            if ((((unsigned int)nums[i] >> shift) & 1) == 1) {
                count_of_1++;
            } else {
                count_of_0++;
            }
        }

        diff_count += count_of_0 * count_of_1;
    }

    return diff_count;
}
