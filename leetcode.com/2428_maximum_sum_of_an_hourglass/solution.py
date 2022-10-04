class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:

        def get_sum(y, x):
            return sum(grid[y][x:x+3]) + grid[y+1][x+1] + sum(grid[y+2][x:x+3])

        best = 0
        for y in range(len(grid) - 2):
            for x in range(len(grid[0]) - 2):
                best = max(best, get_sum(y, x))

        return best
