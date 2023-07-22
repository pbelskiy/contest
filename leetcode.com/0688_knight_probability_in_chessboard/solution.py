class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        @cache
        def dp(y, x, r):
            if not (0 <= y < n and 0 <= x < n):
                return 0

            if r == 0:
                return 1

            moves = (
                (y + 2, x + 1), (y - 2, x + 1),
                (y + 2, x - 1), (y - 2, x - 1),
                (y + 1, x + 2), (y - 1, x + 2),
                (y + 1, x - 2), (y - 1, x - 2)
            )

            p = 0
            for y, x in moves:
                p += (1/8) * dp(y, x, r - 1)

            return p

        return dp(row, column, k)
