class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        h, w = len(grid), len(grid[0])

        t = 0

        for x in range(w):
            for y in range(1, h):
                if grid[y][x] <= grid[y - 1][x]:
                    d = grid[y - 1][x] - grid[y][x] + 1
                    grid[y][x] += d
                    t += d

        return t
