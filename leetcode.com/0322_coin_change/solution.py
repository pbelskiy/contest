class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @cache
        def dfs(s, i):
            if s == 0:
                return 0

            if s < 0:
                return float('inf')

            return min([1 + dfs(s - coins[j], j) for j in range(i, len(coins))])

        coins.sort(reverse=True)
        r = dfs(amount, 0)
        return -1 if r == float('inf') else r
