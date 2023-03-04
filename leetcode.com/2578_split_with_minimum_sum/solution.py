class Solution:
    def splitNum(self, num: int) -> int:
        a, b = '', ''

        digits = sorted(str(num))

        for i in range(len(digits) & ~1):
            if len(a) == len(b):
                a += digits[i]
            else:
                b += digits[i]

        if len(digits) % 2 == 1:
            v1 = int(a + digits[-1]) + int(b)
            v2 = int(a) + int(b + digits[-1])
            return min(v1, v2)

        return int(a) + int(b)
