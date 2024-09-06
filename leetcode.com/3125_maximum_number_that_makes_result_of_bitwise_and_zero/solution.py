class Solution:
    def maxNumber(self, n: int) -> int:
        for i in range(n.bit_length(), -1, -1):
            if (1 << i) & n:
                return 2**i - 1
