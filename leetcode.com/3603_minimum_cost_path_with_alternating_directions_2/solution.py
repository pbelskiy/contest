class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        q = [(1, 1, 0, 0)]
        h, w = m, n

        dist = [[[float('inf')] * 2 for _ in range(n)] for _ in range(m)]
        dist[0][0][1 % 2] = 1

        while q:
            t, s, y, x = heappop(q)
            # print(f'{t=} {s=} ({y=}, {x=})')
            if (y, x) == (h - 1, w - 1):
                return t

            parity = s % 2

            if t > dist[y][x][parity]:
                continue

            if parity == 0:
                new_t = t + waitCost[y][x]
                if new_t < dist[y][x][1]:
                    dist[y][x][1] = new_t
                    heappush(q, (new_t, s + 1, y, x))
            else:
                for dy, dx in ((y + 1, x), (y, x + 1)):
                    if 0 <= dy < m and 0 <= dx < n:
                        new_t = t + (dy + 1) * (dx + 1)
                        if new_t < dist[dy][dx][0]:
                            dist[dy][dx][0] = new_t
                            heappush(q, (new_t, s + 1, dy, dx))

