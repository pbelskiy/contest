class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        h, w = len(grid), len(grid[0])

        for y in range(h):
            for x in range(w):
                if y == 0 and x == 0:
                    continue
                elif y > 0 and x > 0:
                    grid[y][x] += min(grid[y][x - 1], grid[y - 1][x])
                elif y > 0:
                    grid[y][x] += grid[y - 1][x]
                else:
                    grid[y][x] += grid[y][x - 1]

        return grid[-1][-1]
