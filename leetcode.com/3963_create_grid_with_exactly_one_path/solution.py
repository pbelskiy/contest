class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [['#']*n for _ in range(m)]
        grid[0][0] = '.'

        y, x = 0, 0
        while True:
            if y == m - 1 and x == n - 1:
                break
            
            if x + 1 < n:
                x += 1
                grid[y][x] = '.'
                continue
            
            if y + 1 < m:
                y += 1
                grid[y][x] = '.'
                continue

        return [''.join(row) for row in grid]

