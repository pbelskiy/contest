class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        covered = set()

        for i in range(n):
            b, e = intervals[i]

            for j in range(n):
                if i == j or j in covered:
                    continue

                _b, _e = intervals[j]

                if b <= _b and _e <= e:
                    covered.add(j)

        return n - len(covered)
