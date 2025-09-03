class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:

        @cache
        def dfs(y, x):
            if y >= h or x >= w:
                return 0

            if (y, x) == (h - 1, w - 1):
                return 1

            t = 0

            # go right
            if x + 1 < w:
                dy, dx, dd = y, x + 1, 'R'
                while dy < h and dx < w and grid[dy][dx] == 1:
                    if dd == 'D':
                        dd = 'R'
                        dx += 1
                    else:
                        dd = 'D'
                        dy += 1

                t += dfs(dy, dx)

            # go down
            if y + 1 < h:
                dy, dx, dd = y + 1, x, 'D'
                while dy < h and dx < w and grid[dy][dx] == 1:
                    if dd == 'D':
                        dd = 'R'
                        dx += 1
                    else:
                        dd = 'D'
                        dy += 1

                t += dfs(dy, dx)

            return t % (10**9 + 7)

        h, w = len(grid), len(grid[0])
        return dfs(0, 0)

