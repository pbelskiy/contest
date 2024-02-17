class Solution:
    def maxOperations(self, nums: List[int]) -> int:

        @cache
        def dfs(i, j, p):
            if j - i + 1 < 2:
                return 0

            m = 0
            if nums[i] + nums[i + 1] == p:  # first two
                m = max(m, dfs(i + 2, j, p) + 1)

            if nums[j] + nums[j - 1] == p:  # last two
                m = max(m, dfs(i, j - 2, p) + 1)

            if nums[i] + nums[j] == p:  # first and last
                m = max(m, dfs(i + 1, j - 1, p) + 1)

            return m

        return max(
            dfs(2, len(nums) - 1, nums[0] + nums[1]),    # first two
            dfs(0, len(nums) - 3, nums[-1] + nums[-2]),  # last two
            dfs(1, len(nums) - 2, nums[0] + nums[-1]),   # first and last
        ) + 1
