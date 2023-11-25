class Solution:
    def minimumCoins(self, prices: List[int]) -> int:

        @cache
        def dp(i, f):
            if i >= len(prices):
                return 0

            m = dp(i + 1, i + 1) + prices[i]  # buy
            for j in range(f):
                m = min(m, dp(i + j + 1, 0))  # get free

            return m

        return dp(0, 0)
