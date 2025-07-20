class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:

        def bfs(y, x):
            q = deque([(y, x)])
            s = grid[y][x]
            v.add((y, x))

            while q:
                y, x = q.popleft()
                for dy, dx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                    if not (0 <= dy < h and 0 <= dx < w):
                        continue

                    if grid[dy][dx] == 0:
                        continue

                    if (dy, dx) in v:
                        continue

                    v.add((dy, dx))
                    q.append((dy, dx))
                    s += grid[dy][dx]

            return s

        h, w = len(grid), len(grid[0])
        v = set()
        t = 0

        for y in range(h):
            for x in range(w):
                if grid[y][x] == 0:
                    continue

                if (y, x) in v:
                    continue

                s = bfs(y, x)
                if s % k == 0:
                    t += 1
 
        return t

