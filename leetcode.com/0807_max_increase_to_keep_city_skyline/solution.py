class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        total = 0
        rev = list(zip(*grid))

        for y in range(len(grid)):
            for x in range(len(grid)):
                total += min(max(grid[y]), max(rev[x])) - grid[y][x]

        return total
