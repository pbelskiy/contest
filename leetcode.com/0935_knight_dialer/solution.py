class Solution:
    def knightDialer(self, n: int) -> int:

        @cache
        def dp(p, t):
            if t == n:
                return 1

            return sum(dp(m, t + 1) for m in d[p]) % (10**9 + 7)

        d = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [],
             6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [4, 2]}

        return sum(dp(p, 1) for p in range(10)) % (10**9 + 7)
