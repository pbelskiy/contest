class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s = sum(map(int, str(x)))
        return s if x % s == 0 else -1
