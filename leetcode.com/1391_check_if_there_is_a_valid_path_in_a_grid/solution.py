class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        L = (0, -1), (1, 4, 6)
        R = (0, +1), (1, 3, 5)
        U = (-1, 0), (2, 3, 4)
        D = (+1, 0), (2, 5, 6)

        dirs = {
            1: (L, R),
            2: (U, D),
            3: (L, D),
            4: (R, D),
            5: (L, U),
            6: (R, U),
        }

        h, w = len(grid), len(grid[0])
        q = collections.deque([(0, 0)])

        while q:
            y, x = q.popleft()

            if y == h - 1 and x == w - 1:
                return True

            v = grid[y][x]
            if v == 0:
                continue

            grid[y][x] = 0

            for (dy, dx), streets in dirs[v]:
                ny = y + dy
                nx = x + dx

                if not (0 <= ny < h and 0 <= nx < w):
                    continue

                if grid[ny][nx] in streets:
                    q.append((ny, nx))

        return False
