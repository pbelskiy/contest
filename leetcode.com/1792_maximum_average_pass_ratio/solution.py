"""
Use min heap to distribute students, greedily calculate
future impact of each new student.

TC: O(MlgN)
SC: O(N)
"""
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        def get_impact(p, t):
            return (p + 1) / (t + 1) - p / t

        h = []
        for p, t in classes:
            heappush(h, (-get_impact(p, t), p, t))

        for _ in range(extraStudents):
            _, p, t = heappop(h)
            heappush(h, (-get_impact(p + 1, t + 1), p + 1, t + 1))

        return sum(p / t for _, p, t in h) / len(h)
