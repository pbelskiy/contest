class Solution:
    def numSteps(self, s: str) -> int:

        def dfs(n):
            if n == 1:
                return 0

            if n % 2 == 0:
                return dfs(n // 2) + 1
            return dfs(n + 1) + 1

        return dfs(int(s, 2))
