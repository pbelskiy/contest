class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:

        def dfs(y, x, n):
            if n == len(grid)**2 - 1:
                return True

            moves = [
                (y - 2, x + 1),
                (y - 1, x + 2),
                (y + 1, x + 2),
                (y + 2, x + 1),
                (y + 2, x - 1),
                (y + 1, x - 2),
                (y - 1, x - 2),
                (y - 2, x - 1),
            ]

            for ny, nx in moves:
                if not (0 <= ny < len(grid) and 0 <= nx < len(grid)):
                    continue

                if grid[ny][nx] == n + 1:
                    return dfs(ny, nx, n + 1)

            return False

        return dfs(0, 0, 0)
