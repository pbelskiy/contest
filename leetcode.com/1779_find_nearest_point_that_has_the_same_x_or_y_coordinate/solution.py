class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        idx = -1
        val = float('inf')

        for i, (x1, y1) in enumerate(points):
            d = abs(x1 - x) + abs(y1 - y)
            if d < val and (x1 == x or y1 == y):
                val = d
                idx = i

        return idx
