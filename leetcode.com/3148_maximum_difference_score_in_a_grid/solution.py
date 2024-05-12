class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:

        @cache
        def dfs(y, x):
            m = 0

            dx = x + 1
            if dx < w:
                d = (grid[y][dx] - grid[y][x])
                self.other = max(self.other, d)
                m = max(m, dfs(y, dx) + d)

            dy = y + 1
            if dy < h:
                d = (grid[dy][x] - grid[y][x])
                self.other = max(self.other, d)
                m = max(m, dfs(dy, x) + d)

            return m

        self.other = float('-inf')
        m, h, w = 0, len(grid), len(grid[0])

        for y in range(h):
            for x in range(w):
                m = max(m, dfs(y, x))

        if m == 0:
            return self.other
        return max(m, self.other)
