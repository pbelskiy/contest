class Solution:
    def binaryGap(self, n: int) -> int:
        m, j = 0, 0

        for i, n in enumerate(bin(n)[2:]):
            if n == '1':
                m = max(m, i - j)
                j = i

        return m
