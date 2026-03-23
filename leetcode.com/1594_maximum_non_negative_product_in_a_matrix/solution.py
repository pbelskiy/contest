class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:

        @cache
        def dfs(y, x, p):
            if y == h - 1 and x == w - 1:
                if (p + int(grid[y][x] < 0)) % 2 == 0 or grid[y][x] == 0:
                    return abs(grid[y][x])
                return -10**10

            m = -10**10
            p = p % 2 + int(grid[y][x] < 0)

            if y + 1 < h:
                m = max(m, dfs(y + 1, x, p) * abs(grid[y][x]))
            if x + 1 < w:
                m = max(m, dfs(y, x + 1, p) * abs(grid[y][x]))

            return m

        h, w = len(grid), len(grid[0])
        m = dfs(0, 0, 0)
        if m < 0:
            return -1
        return m % (10**9 + 7)

