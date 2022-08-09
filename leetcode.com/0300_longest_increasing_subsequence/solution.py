class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        @cache
        def dfs(i):
            if i == len(nums):
                return 0

            m = 0
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    m = max(m, 1 + dfs(j))

            return m

        return max([dfs(i) for i in range(len(nums))]) + 1
