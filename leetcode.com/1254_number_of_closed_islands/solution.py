class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        def bfs(y, x):
            q = collections.deque([(y, x)])

            while q:
                y, x = q.popleft()
                grid[y][x] = 1

                for dy, dx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                    if not (0 <= dy < h and 0 <= dx < w):
                        continue

                    if grid[dy][dx] == 0:
                        q.append((dy, dx))

        total = 0
        h, w = len(grid), len(grid[0])

        # erase edge connected
        for y in range(h):
            if grid[y][0] == 0:
                bfs(y, 0)
            if grid[y][w - 1] == 0:
                bfs(y, w - 1)

        for x in range(w):
            if grid[0][x] == 0:
                bfs(0, x)
            if grid[h - 1][x] == 0:
                bfs(h - 1, x)

        # count others
        for y in range(h):
            for x in range(w):
                if grid[y][x] == 0:
                    bfs(y, x)
                    total += 1

        return total
