class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for n in range(num):
            if n + int(str(n)[::-1]) == num:
                return True

        return num == 0
