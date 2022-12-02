class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        w = float('-inf')
        points.sort(key=lambda p: p[0])

        for i in range(len(points) - 1):
            w = max(w, abs(points[i][0] - points[i + 1][0]))

        return w
