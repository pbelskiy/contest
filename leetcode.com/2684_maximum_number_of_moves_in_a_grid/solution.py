class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:

        @cache
        def dfs(y, x):
            m = 0

            for dy, dx in ((y - 1, x + 1), (y, x + 1), (y + 1, x + 1)):
                if not (0 <= dy < h and 0 <= dx < w):
                    continue

                if grid[dy][dx] > grid[y][x]:
                    m = max(m, dfs(dy, dx) + 1)

            return m

        h, w = len(grid), len(grid[0])
        return max(dfs(y, 0) for y in range(h))
