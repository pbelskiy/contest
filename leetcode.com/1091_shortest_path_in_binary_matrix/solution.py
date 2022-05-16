class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid) - 1
        q = collections.deque([(0, 0, 1)])

        if grid[0][0] == 1:
            return -1

        while q:
            y, x, d = q.popleft()

            if y == x == n:
                return d

            for dy, dx in (
                (y + 1, x),
                (y - 1, x),
                (y, x + 1),
                (y, x - 1),
                (y + 1, x + 1),
                (y - 1, x - 1),
                (y + 1, x - 1),
                (y - 1, x + 1),
            ):
                if not (0 <= dy <= n and 0 <= dx <= n):
                    continue

                if grid[dy][dx] == 0:
                    grid[dy][dx] = 1
                    q.append((dy, dx, d + 1))

        return -1
