class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        
        @cache
        def dfs(i):
            if i == n:
                return 0

            m = float('inf')
            for j in range(i + 1, min(n + 1, i + 4)):
                m = min(m, dfs(j) + costs[j - 1] + (j - i)**2)

            return m

        return dfs(0)

