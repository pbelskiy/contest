class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        return bin(n).count('11') == 1 and bin(n).count('111') == 0

