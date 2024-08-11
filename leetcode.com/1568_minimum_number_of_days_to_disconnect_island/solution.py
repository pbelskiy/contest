"""
Since there could be only three answers, we use simple brute force.

Answers:
  0 - When already disconnected grid
  1 - When graph is disconnected after one change (brute force here)
  2 - All other cases (becase it's worse case)

Not more that 2 changes here because nodes in the corner have at most
two nodes in neighbours.
"""
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:

        def is_connected():
            t = 0
            v = set()

            for y in range(h):
                for x in range(w):
                    if grid[y][x] == 0 or (y, x) in v:
                        continue

                    t += 1

                    if t > 1:
                        return False

                    q = deque([(y, x)])
                    while q:
                        cy, cx = q.popleft()
                        for dy, dx in ((cy + 1, cx), (cy - 1, cx),
                                       (cy, cx + 1), (cy, cx - 1)):
                            if (dy, dx) in v:
                                continue

                            if not (0 <= dy < h and 0 <= dx < w):
                                continue

                            if grid[dy][dx] == 0:
                                continue

                            v.add((dy, dx))
                            q.append((dy, dx))

            return t == 1

        def dfs():
            if not is_connected():
                return 0

            m = float('inf')
            for y in range(h):
                for x in range(w):
                    if grid[y][x] == 1:
                        grid[y][x] = 0
                        if not is_connected():
                            return 1
                        grid[y][x] = 1

            return 2

        h, w = len(grid), len(grid[0])
        if not is_connected():
            return 0

        return dfs()
