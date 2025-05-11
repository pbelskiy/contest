class Solution:
    def specialGrid(self, n: int) -> List[List[int]]:
        if n == 0:
            return [[0]]

        h = w = 2**n
        g = [[-1]*w for _ in range(h)]

        def dfs(y, x, d):
            if not (0 <= y < h and 0 <= x < w):
                return

            if g[y][x] == -1:
                g[y][x] = self.v
                self.v += 1

            if d == 0:
                return

            dfs(y, x, d // 2)
            dfs(y + d, x, d // 2)
            dfs(y + d, x - d, d // 2)
            dfs(y, x - d, d // 2)

        self.v = -1
        dfs(0, w - 1, 2**n)

        return g

