class Solution:

    def is_collinear(self, p1, p2, p3):
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3

        return (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) == 0

    def maxPoints(self, points: List[List[int]]) -> int:
        max_points = 1

        for p1, p2 in itertools.combinations(points, 2):
            total = 2
            for p3 in points:
                if p3 != p1 and p3 != p2 and self.is_collinear(p1, p2, p3):
                    total += 1

            max_points = max(max_points, total)

        return max_points
