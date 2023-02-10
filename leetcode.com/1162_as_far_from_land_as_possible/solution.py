class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        v = set()

        z = 0
        for y in range(n):
            for x in range(n):
                if grid[y][x] == 1:
                    v.add((y, x))
                    q.append((y, x, 0))
                else:
                    z += 1

        if z == 0:
            return -1

        d = -1
        while q:
            y, x, m = q.popleft()
            d = max(d, m)

            for y, x in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                if not (0 <= y < n and 0 <= x < n):
                    continue

                if (y, x) in v:
                    continue

                v.add((y, x))
                q.append((y, x, m + 1))


        return d
