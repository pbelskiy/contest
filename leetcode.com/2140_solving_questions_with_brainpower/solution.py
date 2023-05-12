class Solution:
    def mostPoints(self, q: List[List[int]]) -> int:

        @cache
        def solve(i):
            if i >= len(q):
                return 0

            return max(
                solve(i + 1),
                solve(i + q[i][1] + 1) + q[i][0]
            )

        return solve(0)
