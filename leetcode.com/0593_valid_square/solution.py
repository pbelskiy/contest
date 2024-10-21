"""
Check that every point has equal distance to other two.

TC: O(1)
SC: O(1)
"""
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = [p1, p2, p3, p4]

        if len(set(map(tuple, points))) != 4:
            return False

        count = Counter()

        for p1 in points:
            x1, y1 = p1

            dist = []
            for p2 in points:
                if p1 == p2:
                    continue
                x2, y2 = p2
                dist.append(abs(x1 - x2) + abs(y1 - y2))

            if len(set(dist)) > 2:
                return False

            count[tuple(sorted(dist))] += 1

        return len(count) == 1
