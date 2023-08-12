class Solution:
    def minSteps(self, n: int) -> int:

        @cache
        def dp(t, b):
            if t == n:
                return 0

            if t > n:
                return float('inf')

            m = float('inf')
            if b > 0:
                m = dp(t + b, b) + 1  # paste

            if t != b:
                m = min(m, dp(t, t) + 1)  # copy

            return m

        return dp(1, 0)
