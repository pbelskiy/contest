class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:

        def is_valid(p1, p2, p3, p4):
            # check works for only parallel to axes rectangle
            coords = sorted([p1, p2, p3, p4], key=lambda x: (x[0], x[1]))

            if (coords[0][0] == coords[1][0] and
                coords[0][1] == coords[2][1] and
                coords[1][1] == coords[3][1] and
                coords[2][0] == coords[3][0]):
                return True

            return False

        best = -1

        for group in combinations(points, 4):
            rest = [p for p in points if p not in group]

            # is valid rectangle
            p1, p2, p3, p4 = group[0], group[1], group[2], group[3]
            if not is_valid(p1, p2, p3, p4):
                continue

            # does not contain any other point inside or on its border
            min_x = min(p1[0], p2[0], p3[0], p4[0])
            max_x = max(p1[0], p2[0], p3[0], p4[0])
            min_y = min(p1[1], p2[1], p3[1], p4[1])
            max_y = max(p1[1], p2[1], p3[1], p4[1])

            inside = False
            for x, y in rest:
                if min_x <= x <= max_x and min_y <= y <= max_y:
                    inside = True
                    break

            if inside:
                continue

            area = (max_x - min_x) * (max_y - min_y)
            best = max(best, area)

        return best
