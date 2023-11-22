class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:

        def dfs(n, r):
            if n == 1:
                return 0

            if r > 0 and n % 2 == 0:
                return dfs(n // 2, r - 1) + 1

            if r == 0:
                return n - 1

            return dfs(n - 1, r) + 1

        return dfs(target, maxDoubles)
