class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        total = 0

        for _ in range(30):
            if c & 1 == 0:
                total += (a & 1) + (b & 1)
            elif not ((a & 1) | (b & 1) == c & 1):
                total += 1

            a >>= 1
            b >>= 1
            c >>= 1

        return total
