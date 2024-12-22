class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:

        @cache
        def dfs(y, x, v):
            if y == h - 1 and x == w - 1:
                return int(v == k)

            t = 0

            if y + 1 < h:
                t += dfs(y + 1, x, v ^ grid[y + 1][x])

            if x + 1 < w:
                t += dfs(y, x + 1, v ^ grid[y][x + 1])

            return t % (10**9 + 7)

        h, w = len(grid), len(grid[0])
        return dfs(0, 0, grid[0][0])
