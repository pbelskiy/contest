class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7

        @cache
        def dfs(y, x):
            t = 0

            for cy, cx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                if not (0 <= cy < h and 0 <= cx < w):
                    continue

                if grid[cy][cx] <= grid[y][x]:
                    continue

                t += (dfs(cy, cx) + 1) % MOD

            return t % MOD

        t, h, w = 0, len(grid), len(grid[0])

        for y in range(h):
            for x in range(w):
                t += (dfs(y, x) + 1) % MOD

        return t % MOD
