class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda k: k[1])
        n, t, i = len(points), 0, 0

        while i < n:
            j = i
            while i + 1 < n and points[j][1] >= points[i + 1][0]:
                i += 1
            else:
                i += 1

            t += 1

        return t
