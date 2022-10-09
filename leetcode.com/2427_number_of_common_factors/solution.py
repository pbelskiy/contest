class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        total = 0

        for f in range(1, min(a, b) + 1):
            if a % f == 0 and b % f == 0:
                total += 1

        return total
