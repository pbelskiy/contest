class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        r = ''

        while n > 0:
            for x in range(9, 0, -1):
                if s - x >= 0:
                    r += str(x)
                    s -= x
                    n -= 1
                    break
            else:
                break

        if s != 0:
            return -1

        for _ in range(n):
            r += '0'

        return int(r)

