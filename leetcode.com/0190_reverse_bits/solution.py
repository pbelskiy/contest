class Solution:

    def reverseBits(self, n):
        v = 0

        for i in range(32):
            if (1 << i) & n:
                v |= (1 << (31 - i))

        return v
