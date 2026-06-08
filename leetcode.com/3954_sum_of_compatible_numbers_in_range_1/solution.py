class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        s = 0

        for x in range(1, n + k + 1):
            if abs(n - x) <= k and n & x == 0:
                s += x

        return s

