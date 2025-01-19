class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        d = abs(nums[0] - nums[-1])

        for i in range(len(nums) - 1):
            d = max(d, abs(nums[i] - nums[i + 1]))

        return d
