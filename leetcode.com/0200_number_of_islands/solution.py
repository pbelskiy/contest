class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(y, x):
            for cy, cx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                if not (0 <= cy < h and 0 <= cx < w):
                    continue

                if grid[cy][cx] == '1':
                    grid[cy][cx] = '0'
                    dfs(cy, cx)

        count = 0
        h, w = len(grid), len(grid[0])

        for y in range(h):
            for x in range(w):
                if grid[y][x] == '1':
                    dfs(y, x)
                    count += 1

        return count
