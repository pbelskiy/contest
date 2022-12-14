class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        @cache
        def dfs(i, n):
            if n < 0:
                return 0

            if n == 0:
                return 1

            total = 0

            for j in range(i, len(coins)):
                total += dfs(j, n - coins[j])

            return total

        coins.sort(reverse=True)
        return dfs(0, amount)
