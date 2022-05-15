class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total = 0

        for (x1, y1), (x2, y2) in zip(points, points[1:]):
            total += max(abs(x1 - x2), abs(y1 - y2))

        return total
