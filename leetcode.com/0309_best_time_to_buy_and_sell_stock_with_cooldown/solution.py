class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        @functools.cache
        def dfs(i, can_buy):
            if i >= len(prices):
                return 0

            if can_buy:
                v1 = -prices[i] + dfs(i + 1, False)
            else:
                v1 = +prices[i] + dfs(i + 2, True)

            v2 = dfs(i + 1, can_buy)

            return max(v1, v2)

        return dfs(0, True)
