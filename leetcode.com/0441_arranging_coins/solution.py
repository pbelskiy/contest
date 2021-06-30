class Solution:
    def arrangeCoins(self, n: int) -> int:
        rows = 0

        while n >= 0:
            n -= rows
            rows += 1

        return rows - 2
