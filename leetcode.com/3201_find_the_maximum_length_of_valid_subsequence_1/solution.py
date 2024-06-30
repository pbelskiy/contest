class Solution:
    def maximumLength(self, nums: List[int]) -> int:

        @cache
        def dfs(i, m):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j]) % 2 == m:
                    return dfs(j, m) + 1

            return 0

        best = 0
        for i in range(len(nums)):
            best = max(best, max(dfs(i, 0), dfs(i, 1)) + 1)

        return best
