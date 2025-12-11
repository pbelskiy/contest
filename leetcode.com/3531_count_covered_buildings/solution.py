"""
Group by axes, and check covering using bisect.

TC: O(NlgN)
SC: O(N)
"""
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        h = defaultdict(list)
        for x, y in sorted(buildings, key=lambda t: t[1]):
            h[x].append(y)

        v = defaultdict(list)
        for x, y in sorted(buildings, key=lambda t: t[0]):
            v[y].append(x)

        t = 0

        for y, points in v.items():
            if len(points) < 3:
                continue

            for dx in points[1:-1]:
                if len(h[dx]) < 3:
                    continue

                i = bisect.bisect_left(h[dx], y)
                if 0 < i < len(h[dx]) - 1:
                    t += 1

        return t

