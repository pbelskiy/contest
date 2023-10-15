class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:

        @cache
        def dp(p, s):
            if s == 0:
                return 1 if p == endPos else 0

            return (dp(p - 1, s - 1) + dp(p + 1, s - 1)) % (10**9 + 7)

        return dp(startPos, k)
