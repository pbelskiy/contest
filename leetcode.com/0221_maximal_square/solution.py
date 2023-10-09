class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        grid = [list(map(int, row)) for row in matrix]

        m = max(max(row) for row in grid)

        for y in range(1, len(grid)):
            for x in range(1, len(grid[0])):
                if grid[y][x] == 0:
                    continue

                grid[y][x] = min(
                    grid[y - 1][x],
                    grid[y - 1][x - 1],
                    grid[y][x - 1],
                ) + 1

                m = max(m, grid[y][x])

        return m**2
