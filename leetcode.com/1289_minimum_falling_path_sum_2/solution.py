class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)

        for y in range(1, n):
            for x in range(n):
                row = grid[y - 1][:]
                row.pop(x)
                grid[y][x] += min(row)

        return min(grid[-1])
