"""
Use bisect for find bounds.

TC: O(NlgN)
SC: O(sort)
"""
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        total = 0
        for i in range(len(nums)):
            left = bisect.bisect_left(nums, lower - nums[i], lo=i+1)
            right = bisect.bisect_right(nums, upper - nums[i], lo=i+1)

            total += right - left

        return total

