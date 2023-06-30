class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        q = deque()
        t, h, w = 0, len(grid), len(grid[0])

        # find start position
        for y, x in product(range(h), range(w)):
            if grid[y][x] == '@':
                q.append((y, x, 0, ()))
            elif grid[y][x].islower():
                t += 1

        # run bfs
        v = set()
        while q:
            y, x, m, k = q.popleft()

            # key found
            if grid[y][x].islower() and grid[y][x] not in k:
                k += (grid[y][x],)

            if len(k) == t:
                return m

            for y, x in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                if not (0 <= y < h and 0 <= x < w):
                    continue

                if grid[y][x] == '#' or grid[y][x].isupper() and grid[y][x].lower() not in k:
                    continue

                if (y, x, k) in v:
                    continue

                q.append((y, x, m + 1, k))
                v.add((y, x, k))

        return -1
