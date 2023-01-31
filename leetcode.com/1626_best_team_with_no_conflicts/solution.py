class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:

        @cache
        def dfs(i, p):
            if i == len(a):
                return 0

            m = 0
            for j in range(i, len(a)):
                if a[j][1] > p:
                    continue
                m = max(m, dfs(j + 1, a[j][1]) + a[j][1])

            return m

        a = sorted(zip(ages, scores), reverse=True)
        return dfs(0, float('inf'))
