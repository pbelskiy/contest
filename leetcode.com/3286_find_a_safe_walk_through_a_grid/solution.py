class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        h, w = len(grid), len(grid[0])
        q = deque([(0, 0, health)])
        v = set()

        while q:
            y, x, s = q.popleft()

            if grid[y][x] == 1:
                s -= 1

            if s < 1:
                continue

            if y == h - 1 and x == w - 1 and h > 0:
                return True

            for dy, dx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                if not (0 <= dy < h and 0 <= dx < w):
                    continue

                if (dy, dx, s) not in v:
                    v.add((dy, dx, s))
                    q.append((dy, dx, s))

        return False
