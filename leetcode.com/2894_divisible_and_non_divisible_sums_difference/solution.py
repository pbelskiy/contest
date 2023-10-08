class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = sum(v for v in range(1, n + 1) if v % m != 0)
        num2 = sum(v for v in range(1, n + 1) if v % m == 0)
        return num1 - num2
