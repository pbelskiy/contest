class Solution:
    def maxScore(self, nums: List[int]) -> int:

        @cache
        def dfs(i):
            if i == len(nums):
                return 0

            m = 0
            for j in range(i + 1, len(nums)):
                m = max(m, dfs(j) + (j - i) * nums[j])

            return m

        return dfs(0)
