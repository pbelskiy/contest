class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        area = 0

        for row in grid:
            area += len(row) - row.count(0) + max(row)

        for x in range(len(grid[0])):
            m = 0
            for y in range(len(grid)):
                m = max(m, grid[y][x])
            area += m

        return area
