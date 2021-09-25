class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        h, w = len(grid) - 1, len(grid[0]) - 1
        visited = set((0, 0, k))
        q = collections.deque([(0, 0, k, 0)])

        while q:
            y, x, r, s = q.popleft()

            if (y, x) == (h, w):
                return s

            for cy, cx in ((y, x + 1), (y, x - 1), (y + 1, x), (y - 1, x)):
                if not (0 <= cy <= h and 0 <= cx <= w):
                    continue

                if grid[cy][cx] == 1 and r > 0:
                    if (cy, cx, r - 1) in visited:
                        continue
                    q.append((cy, cx, r - 1, s + 1))
                    visited.add((cy, cx, r - 1))

                elif grid[cy][cx] == 0:
                    if (cy, cx, r) in visited:
                        continue
                    q.append((cy, cx, r, s + 1))
                    visited.add((cy, cx, r))

        return -1
