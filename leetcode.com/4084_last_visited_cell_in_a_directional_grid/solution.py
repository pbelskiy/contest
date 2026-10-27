class Solution:
    def lastVisitedCell(self, grid: list[list[str]]) -> list[int]:
        v = set([(0, 0)])
        y, x = 0, 0
        h, w = len(grid), len(grid[0])

        while True:
            if grid[y][x] == 'L':
                ny, nx = y, x - 1
            elif grid[y][x] == 'R':
                ny, nx = y, x + 1
            elif grid[y][x] == 'U':
                ny, nx = y - 1, x
            elif grid[y][x] == 'D':
                ny, nx = y + 1, x
            
            if not (0 <= ny < h and 0 <= nx < w):
                return [y, x]

            if (ny, nx) in v:
                return [y, x]

            v.add((y, x))
            y, x = ny, nx


