class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:

        @cache
        def dfs(i, j):
            if i == len(satisfaction):
                return 0

            return max(dfs(i + 1, j), (satisfaction[i]*j) + dfs(i + 1, j + 1))

        satisfaction.sort()
        return dfs(0, 1)
