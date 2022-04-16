class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        @functools.cache
        def dfs(y, x, r):
            if not (0 <= y < m and 0 <= x < n):
                return 1

            if r == 0:
                return 0

            total = 0
            for dy, dx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                total += dfs(dy, dx, r - 1)

            return total

        return dfs(startRow, startColumn, maxMove) % (10**9 + 7)
