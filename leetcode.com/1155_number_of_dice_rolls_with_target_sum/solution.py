class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        @cache
        def solve(r, s):
            if r == 0:                        # no more dice
                return s == target            # is sum equal to target

            total = 0
            for i in range(1, k + 1):         # try each die side
                total += solve(r - 1, s + i)  # minus die, plus side value
            return total % (10**9 + 7)        # return total ways

        return solve(n, 0)                    # all die on hand, sum is zero
