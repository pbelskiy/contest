class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:

        h, w = len(grid), len(grid[0])
        for row in grid:
            if row[0] == 1:
                continue

            for i in range(len(row)):
                row[i] = int(not row[i])

        for x in range(w):
            s = sum(grid[y][x] for y in range(h))

            if s >= len(grid) - s:
                continue

            for y in range(h):
                grid[y][x] = int(not grid[y][x])

        t = 0
        for row in grid:
            t += int("".join(map(str, row)), 2)

        return t
