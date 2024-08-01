class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        @cache
        def dp(i, s):
            if i == len(nums):
                return s == t

            if s > t:
                return False

            return dp(i + 1, s + nums[i]) or dp(i + 1, s)

        if sum(nums) % 2 == 1:
            return False

        t = sum(nums) // 2
        return dp(0, 0)
