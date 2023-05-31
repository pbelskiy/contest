class Solution:
    def integerReplacement(self, n: int) -> int:

        @cache
        def dfs(n):
            if n == 1:
                return 0

            if n % 2 == 0:
                return dfs(n // 2) + 1

            return min(dfs(n + 1) + 1, dfs(n - 1) + 1)

        return dfs(n)
