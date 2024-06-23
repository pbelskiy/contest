class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        h, w = len(grid), len(grid[0])

        # reduce upper bound
        y1 = 0
        while y1 < h and sum(grid[y1]) == 0:
            y1 += 1

        # reduce lower bound
        y2 = h - 1
        while y2 > y1 and sum(grid[y2]) == 0:
            y2 -= 1

        # reduce left bound
        x1 = 0
        while x1 < w and sum(grid[y][x1] for y in range(h)) == 0:
            x1 += 1

        # reduce right bound
        x2 = w - 1
        while x2 > x1 and sum(grid[y][x2] for y in range(h)) == 0:
            x2 -= 1

        return (y2 - y1 + 1) * (x2 - x1 + 1)
