memo = {}

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:

        def dp(r, v):
            if (r, v, x) in memo:
                return memo[(r, v, x)]

            if r == 0:
                return 1

            i, t = v, 0
            while True:
                new = r - i**x
                if new < 0:
                    break

                i += 1
                t += dp(new, i) % (10**9 + 7)

            result = t % (10**9 + 7)
            memo[(r, v, x)] = result
            return result

        return dp(n, 1) % (10**9 + 7)
