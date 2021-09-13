class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp = [0] * len(nums)
        total = 0

        dp[0] = nums[0]
        dp[1] = nums[1]
        total = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[:i-1]) + nums[i]
            total = max(total, dp[i])

        return total
