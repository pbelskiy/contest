class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = 0
        p = 1

        for ch in str(n):
            s += int(ch)
            p *= int(ch)

        return n % (s + p) == 0

