class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:

        @cache
        def dp(p, s):
            if s == 0:
                return 1 if p == 0 else 0

            w = dp(p, s - 1)

            if p + 1 < arrLen:
                w += dp(p + 1, s - 1)

            if p - 1 >= 0:
                w += dp(p - 1, s - 1)

            return w % (10**9 + 7)

        return dp(0, steps)
