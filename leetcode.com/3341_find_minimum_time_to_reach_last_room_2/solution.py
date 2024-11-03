class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        h, w = len(moveTime), len(moveTime[0])

        q = [(0, 0, 0, 0)]
        v = set()
        while q:
            t, y, x, s = heappop(q)
            if y == h - 1 and x == w - 1:
                return t

            for dy, dx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                if not (0 <= dy < h and 0 <= dx < w):
                    continue

                if (dy, dx) in v:
                    continue

                if t >= moveTime[dy][dx]:
                    nt = t + (s % 2 + 1)
                else:
                    nt = moveTime[dy][dx] + (s % 2 + 1)

                heappush(q, (nt, dy, dx, s + 1))
                v.add((dy, dx))
