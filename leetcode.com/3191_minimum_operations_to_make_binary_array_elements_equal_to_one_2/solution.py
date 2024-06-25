"""
Flip index by index, virtually change following subarray using `last`.

TC: O(N)
SC: O(1)
"""
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        total, last = 0, 1

        for i in range(len(nums)):
            if nums[i] != last:
                last ^= 1
                total += 1

        return total
