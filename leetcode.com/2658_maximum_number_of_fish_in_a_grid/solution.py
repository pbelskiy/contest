class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:

        def bfs(y, x):
            q = deque([(y, x)])
            v = set([(y, x)])
            m = 0

            while q:
                y, x = q.popleft()
                m += grid[y][x]

                for y, x in ((y, x + 1), (y, x - 1), (y + 1, x), (y - 1, x)):
                    if not (0 <= y < h and 0 <= x < w):
                        continue
                    if grid[y][x] == 0:
                        continue
                    if (y, x) in v:
                        continue
                    v.add((y, x))
                    q.append((y, x))

            return m

        m, h, w = 0, len(grid), len(grid[0])

        for y in range(h):
            for x in range(w):
                if grid[y][x] > 0:
                    m = max(m, bfs(y, x))

        return m
