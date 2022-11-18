class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:

        @cache
        def solve(n):
            if n > high:
                return 0

            r = solve(n + zero) + solve(n + one)
            if low <= n <= high:
                r += 1
            return r % (10**9 + 7)

        return solve(0)
