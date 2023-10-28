class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:

        @cache
        def dp(i, s):
            if s == target:
                return 0

            if i == len(nums) or s > target or nums[i] > target:
                return float('-inf')

            return max(dp(i + 1, s + nums[i]) + 1, dp(i + 1, s))

        nums.sort()
        r = dp(0, 0)
        dp.cache_clear()
        if r == float('-inf'):
            return -1
        return r
