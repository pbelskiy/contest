"""
There are only three variants.

TC: O(sort)
SC: O(sort)
"""
class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()

        return min(
            nums[-1] - nums[2],
            nums[-2] - nums[1],
            nums[-3] - nums[0],
        )

