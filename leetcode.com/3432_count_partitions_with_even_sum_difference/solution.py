"""
Sum balance

TC: O(N)
SC: (1)
"""
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = 0
        left, right = 0, sum(nums)

        for i in range(len(nums) - 1):
            left += nums[i]
            right -= nums[i]

            if (left - right) % 2 == 0:
                total += 1

        return total
