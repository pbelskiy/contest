"""
Greedy, sort and two pointers.

TC: O(sort)
SC: O(sort)
"""
class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        nums.sort()
        total = 0

        left, right = 0, len(nums) - 1
        while left <= right:
            total += nums[right - 1]
            left += 1
            right -= 2

        return total

