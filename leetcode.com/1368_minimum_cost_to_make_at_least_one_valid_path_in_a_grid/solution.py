"""
Simple BFS with priority queue.

TC: O(NlgN)
SC: O(NM)
"""
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        h, w = len(grid), len(grid[0])

        v = set()
        q = [(0, 0, 0)]
        while q:
            s, y, x = heappop(q)

            if y == h - 1 and x == w - 1:
                return s

            for dy, dx, dd in ((y, x + 1, 1), (y, x - 1, 2),
                               (y + 1, x, 3), (y - 1, x, 4)):
                # out of bounds
                if not (0 <= dy < h and 0 <= dx < w):
                    continue

                # already visited direction
                if (y, x, dy, dx) in v:
                    continue

                # try go new direction for free or with cost
                heappush(q, (s + int(grid[y][x] != dd), dy, dx))
                v.add((y, x, dy, dx))
