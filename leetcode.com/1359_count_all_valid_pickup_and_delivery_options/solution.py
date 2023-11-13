class Solution:
    def countOrders(self, n: int) -> int:

        @cache
        def dp(p, d):
            if p == d == n:
                return 1

            t = 0
            if p < n:
                t += dp(p + 1, d)*(n - p)

            if d < p:
                t += dp(p, d + 1)*(p - d)

            return t % (10**9 + 7)

        return dp(0, 0) % (10**9 + 7)
