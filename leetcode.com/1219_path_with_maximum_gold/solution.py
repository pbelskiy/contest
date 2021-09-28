class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        def dfs(y, x, s):
            prev = grid[y][x]
            grid[y][x] = 0

            for cy, cx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                if not (0 <= cy < h and 0 <= cx < w):
                    continue

                if grid[cy][cx] == 0:
                    continue

                dfs(cy, cx, s + grid[cy][cx])

            grid[y][x] = prev
            self.answer = max(self.answer, s)

        self.answer = 0

        h, w = len(grid), len(grid[0])

        for y in range(h):
            for x in range(w):
                if grid[y][x] != 0:
                    dfs(y, x, grid[y][x])

        return self.answer
