class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:

        @cache
        def dp(n):
            if n < 0:
                return float('inf')
            if n == 0:
                return 0

            m = float('inf')
            d = 0 if k > 0 else 1
            while True:
                v = d*10 + k
                if v > n:
                    break
                m = min(m, dp(n - v) + 1)
                d += 1

            return m

        r = dp(num)
        return -1 if r == float('inf') else r
