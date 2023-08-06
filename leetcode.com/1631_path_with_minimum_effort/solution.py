class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        def bfs():
            q = [(0, 0, 0)]
            v = set([(0, 0)])
            m = float('inf')

            while q:
                d, y, x = heappop(q)
                if y == h - 1 and x == w - 1:
                    m = min(m, d)

                for dy, dx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                    if (y, x, dy, dx) in v:
                        continue

                    if not (0 <= dy < h and 0 <= dx < w):
                        continue

                    v.add((y, x, dy, dx))
                    heappush(q, (max(d, abs(heights[y][x] - heights[dy][dx])), dy, dx))

            return m

        h, w = len(heights), len(heights[0])
        return bfs()
