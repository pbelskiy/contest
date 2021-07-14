class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            num = sum(map(int, list(str(num))))
            if num < 10:
                return num
