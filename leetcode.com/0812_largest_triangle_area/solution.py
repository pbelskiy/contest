class Solution:

    def get_triangle_area(self, p1, p2, p3):
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3

        a = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        b = math.sqrt((x2 - x3)**2 + (y2 - y3)**2)
        c = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)

        p = (a + b + c) / 2

        return math.sqrt(abs(p*(p - a)*(p - b)*(p - c)))

    def largestTriangleArea(self, points: List[List[int]]) -> float:
        largest = 0

        for p1, p2, p3 in itertools.combinations(points, 3):
            largest = max(largest, self.get_triangle_area(p1, p2, p3))

        return largest
