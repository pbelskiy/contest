class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        h, w = len(moveTime), len(moveTime[0])

        v = set()
        q = [(0, 0, 0)]
        while q:
            t, y, x = heappop(q)
            if y == h - 1 and x == w - 1:
                return t

            for dy, dx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                if not (0 <= dy < h and 0 <= dx < w):
                    continue

                if (dy, dx) in v:
                    continue

                if t >= moveTime[dy][dx]:
                    heappush(q, (t + 1, dy, dx))
                else:
                    heappush(q, (moveTime[dy][dx] + 1, dy, dx))

                v.add((dy, dx))
