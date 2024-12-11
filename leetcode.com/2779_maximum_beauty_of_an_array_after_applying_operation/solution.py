"""
We need to find longest subsequence, so it's sliding window.

Due to we can repalce any element from -k to +k it means the max
diff in subsequence is k*2.

Example:
    a = [1, 2, 4, 6]
    k = 2 (diff = k*2 => 4)

    result: [1, 2, 4] or [2, 4, 6]

TC: O(sort)
SC: O(sort)
"""


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()

        best = 0
        left = 0
        for right in range(len(nums)):
            while left < right and nums[right] - nums[left] > k*2:
                left += 1

            best = max(best, right - left + 1)

        return best
