class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        def is_collinear(x, y, z):
            x1, x2, x3 = x[0], y[0], z[0]
            y1, y2, y3 = x[1], y[1], z[1]
            return (y1 - y2) * (x1 - x3) == (y1 - y3) * (x1 - x2)

        if len(coordinates) < 3:
            return True

        for c in coordinates[2:]:
            if not is_collinear(coordinates[0], coordinates[1], c):
                return False

        return True
