class Solution:
    def numTrees(self, n: int) -> int:
        # TODO: need to solve using DP

        # https://en.wikipedia.org/wiki/Catalan_number
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            dp[i] = (2*(2*i-1)*dp[i-1]) // (i + 1)

        return dp[n]
