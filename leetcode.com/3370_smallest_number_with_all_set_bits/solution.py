class Solution:
    def smallestNumber(self, n: int) -> int:
        for i in range(n.bit_length()):
            n |= 1 << i

        return n
