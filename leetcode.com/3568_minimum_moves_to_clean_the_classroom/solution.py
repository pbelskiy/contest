class Solution:
    def minMoves(self, grid: List[str], energy: int) -> int:
        h, w = len(grid), len(grid[0])
        v = set()
        q = deque()
        d = {}

        for y in range(h):
            for x in range(w):
                if grid[y][x] == 'S':
                    q.append((y, x, energy, 0, 0))
                elif grid[y][x] == 'L':
                    d[(y, x)] = len(d)

        while q:
            y, x, e, m, mask = q.popleft()

            if mask.bit_count() == len(d):
                return m

            if e == 0:
                continue

            for dy, dx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                if not (0 <= dy < h and 0 <= dx < w):
                    continue

                if grid[dy][dx] == 'X':
                    continue

                if grid[dy][dx] == 'L':
                    new_mask = mask | (1 << d[(dy, dx)])
                    if (dy, dx, e - 1, new_mask) not in v:
                        q.append((dy, dx, e - 1, m + 1, new_mask))
                        v.add((dy, dx, e - 1, new_mask))
                    continue

                if grid[dy][dx] == 'R':
                    if (dy, dx, energy, mask) not in v:
                        q.append((dy, dx, energy, m + 1, mask))
                        v.add((dy, dx, energy, mask))
                    continue

                # start or empty
                if (dy, dx, e - 1, mask) not in v:
                    q.append((dy, dx, e - 1, m + 1, mask))
                    v.add((dy, dx, e - 1, mask))

        return -1

