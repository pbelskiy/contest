class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:

        @cache
        def get_vertical(cx):
            return sum(grid[y][cx] for y in range(h))

        @cache
        def get_horizontal(cy):
            return sum(grid[cy][x] for x in range(w))

        def count(cy, cx):
            vertical = get_vertical(cx)
            horizontal = get_horizontal(cy)

            vertical -= grid[cy][cx]
            horizontal -= grid[cy][cx]

            return vertical * horizontal

        t, h, w = 0, len(grid), len(grid[0])

        for y in range(h):
            for x in range(w):
                if grid[y][x] == 1:
                    t += count(y, x)

        return t
