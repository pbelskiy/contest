class Solution:
    def concatenatedBinary(self, n: int) -> int:
        r = 0
        for i in range(1, n + 1):
            r = (r << i.bit_length() | i) % (10**9 + 7)

        return r

