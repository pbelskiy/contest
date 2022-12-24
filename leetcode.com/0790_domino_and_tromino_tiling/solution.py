class Solution:
    def numTilings(self, n: int) -> int:

        @cache
        def dfs(i, t, b):
            if i > n:
                return 0

            if i == n:
                return int(t == 0 and b == 0)

            s = 0

            if t == 0 and b == 0:
                s += dfs(i + 1, 0, 0)  # domino standing
                s += dfs(i + 2, 0, 0)  # two dominos lie
                s += dfs(i + 1, 1, 0)  # tromino
                s += dfs(i + 1, 0, 1)  # tromino

            elif t == 0 and b == 1:
                s += dfs(i + 1, 1, 0)  # domino
                s += dfs(i + 2, 0, 0)  # tromino

            elif t == 1 and b == 0:
                s += dfs(i + 1, 0, 1)  # domino
                s += dfs(i + 2, 0, 0)  # tromino

            return s % (10**9 + 7)

        return dfs(0, 0, 0)
