class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        h, w = len(grid), len(grid[0])

        for y in range(h):
            for x in range(w):
                if grid[y][x] == 0:
                    continue

                for cy, cx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                    if not (0 <= cy < h and 0 <= cx < w) or grid[cy][cx] == 0:
                        perimeter += 1

        return perimeter
