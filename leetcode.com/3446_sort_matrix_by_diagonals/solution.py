class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        h, w = len(grid), len(grid[0])

        # bottom-left triangle
        for sy in range(h - 1, -1, -1):
            # collect
            a = []
            y, x = sy, 0
            while y < h and x < w:
                a.append(grid[y][x])
                y, x = y + 1, x + 1

            a.sort(reverse=True)

            # put back
            i = 0
            y, x = sy, 0
            while y < h and x < w:
                grid[y][x] = a[i]
                y, x = y + 1, x + 1
                i += 1

        # top-right triangle
        for sx in range(1, h):
            # collect
            a = []
            y, x = 0, sx
            while y < h and x < w:
                a.append(grid[y][x])
                y, x = y + 1, x + 1

            a.sort()

            # put back
            i = 0
            y, x = 0, sx
            while y < h and x < w:
                grid[y][x] = a[i]
                y, x = y + 1, x + 1
                i += 1

        return grid
