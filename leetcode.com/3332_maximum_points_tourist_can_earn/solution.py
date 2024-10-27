class Solution:
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:

        @cache
        def dfs(i, curr):
            if i == k:
                return 0

            m = dfs(i + 1, curr) + stayScore[i][curr]

            for dest in range(n):
                m = max(m, dfs(i + 1, dest) + travelScore[curr][dest])

            return m

        return max(dfs(0, curr) for curr in range(n))
