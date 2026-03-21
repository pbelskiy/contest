class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0

        return min(n, 100000) - 1000 + 1

