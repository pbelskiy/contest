class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        n = 1

        while n**2 < num:
            n *= 2

        while n**2 > num:
            n -= 1

        return n**2 == num
