class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:

        @cache
        def dfs(i, t, s):
            l = 0

            for j in range(i, len(nums)):
                if s + nums[j] <= t:
                    l = max(l, dfs(j + 1, t, s + nums[j]) + 1)
                break

            return l

        nums.sort()
        return [dfs(0, q, 0) for q in queries]
