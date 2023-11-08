from functools import cache


class Solution:
    def numDecodings(self, s: str) -> int:

        @cache
        def dp(i, p):
            if i == len(s):
                return 1

            t = 0

            if s[i] == '*':
                for n in range(1, 10):
                    t += dp(i + 1, n)
                    if i > 0 and p*10 + n <= 26:
                        t += dp(i + 1, p*10 + n)

                return t % (10**9 + 7)

            if s[i] != '0':
                t += dp(i + 1, int(s[i]))

            n = p*10 + int(s[i])
            if i > 0 and n <= 26:
                t += dp(i + 1, n)

            return t % (10**9 + 7)

        r = dp(0, 0) % (10**9 + 7)
        dp.cache_clear()
        return r
