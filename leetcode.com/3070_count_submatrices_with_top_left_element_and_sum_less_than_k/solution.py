class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        h, w = len(grid), len(grid[0])

        t = 0
        for y in range(h):
            # calculate
            for x in range(w):
                if x > 0:
                    grid[y][x] += grid[y][x - 1]

                d = grid[y - 1][x] if y > 0 else 0

                if grid[y][x] + d <= k:
                    t += 1

            # add above row
            if y == 0:
                continue

            for x in range(w):
                grid[y][x] += grid[y - 1][x]

        return t
