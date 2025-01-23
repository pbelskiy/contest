class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:

        @cache
        def dfs(y, x, r):
            # we reach the final position
            if y == h - 1 and x == w - 1:
                return 0

            m = float('-inf')

            # go right
            if x + 1 < w:
                m = max(m, dfs(y, x + 1, r) + coins[y][x + 1])
                if r > 0:
                    m = max(m, dfs(y, x + 1, r - 1))

            # go down
            if y + 1 < h:
                m = max(m, dfs(y + 1, x, r) + coins[y + 1][x])
                if r > 0:
                    m = max(m, dfs(y + 1, x, r - 1))

            return m

        h, w = len(coins), len(coins[0])
        return max(dfs(0, 0, 2), dfs(0, 0, 2) + coins[0][0])
