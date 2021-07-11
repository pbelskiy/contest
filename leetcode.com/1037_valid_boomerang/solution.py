class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]

        a = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        b = math.sqrt((x2 - x3)**2 + (y2 - y3)**2)
        c = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)

        p = (a + b + c) / 2

        return round(math.sqrt(abs(p*(p - a)*(p - b)*(p - c))), 2) != 0.0
