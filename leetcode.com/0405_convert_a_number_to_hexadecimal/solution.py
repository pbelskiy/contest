class Solution:
    def toHex(self, num: int) -> str:
        d = {
            10: 'a',
            11: 'b',
            12: 'c',
            13: 'd',
            14: 'e',
            15: 'f',
        }

        s = []

        if num < 0:
            num = 2**32 + num

        while True:
            v = num % 16

            if v < 10:
                s.append(str(v))
            else:
                s.append(d[v])

            num //= 16
            if num == 0:
                break

        return ''.join(reversed(s))
