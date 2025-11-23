class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = ''
        s = 0

        for ch in str(n):
            if int(ch) == 0:
                continue
            x += ch
            s += int(ch)

        if x == '':
            return 0

        return int(x) * s

