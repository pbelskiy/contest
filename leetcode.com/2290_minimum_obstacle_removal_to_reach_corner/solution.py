"""
BFS using priority queue, obstacles are + 1 cost.

TC: O(MlgN)
SC: O(N)
"""
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        h, w = len(grid), len(grid[0])
        v = set()
        q = [(0, 0, 0)]
        while q:
            t, y, x = heappop(q)
            if (y, x) == (h - 1, w - 1):
                return t

            for dy, dx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                if not (0 <= dy < h and 0 <= dx < w):
                    continue

                if (dy, dx) in v:
                    continue

                v.add((dy, dx))
                heappush(q, (t + grid[dy][dx], dy, dx))
