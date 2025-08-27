class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:

        @cache
        def dfs(y, x, t, d):
            m = 0

            for dy, dx, dd in ((y - 1, x - 1, 'UL'), 
                               (y - 1, x + 1, 'UR'), 
                               (y + 1, x - 1, 'DL'), 
                               (y + 1, x + 1, 'DR')):

                if not (0 <= dy < h and 0 <= dx < w):
                    continue

                if abs(grid[y][x] - grid[dy][dx]) != 2:
                    continue

                if dd == d:
                    m = max(m, dfs(dy, dx, t, dd) + 1)
    
                if t:
                    if ((d == 'UL' and dd == 'UR') or 
                        (d == 'UR' and dd == 'DR') or 
                        (d == 'DR' and dd == 'DL') or 
                        (d == 'DL' and dd == 'UL')):

                        m = max(m, dfs(dy, dx, False, dd) + 1)

            return m

        h, w = len(grid), len(grid[0])
        m = 0

        for y in range(h):
            for x in range(w):
                if grid[y][x] != 1:
                    continue

                m = max(m, 1)

                for dy, dx, dd in ((y - 1, x - 1, 'UL'), 
                                   (y - 1, x + 1, 'UR'), 
                                   (y + 1, x - 1, 'DL'), 
                                   (y + 1, x + 1, 'DR')):

                    if not (0 <= dy < h and 0 <= dx < w):
                        continue

                    if grid[dy][dx] == 2:
                        m = max(m, dfs(dy, dx, True, dd) + 2)

        return m

