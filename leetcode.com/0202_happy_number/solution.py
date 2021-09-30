class Solution:
    def isHappy(self, n: int) -> bool:
        values = set()

        while n > 1:
            v = 0

            for ch in str(n):
                v += int(ch)**2

            n = int(v)

            if n in values:
                break
            values.add(n)

        return n == 1
