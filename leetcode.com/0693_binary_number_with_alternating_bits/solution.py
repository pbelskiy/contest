class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return not('11' in bin(n) or '00' in bin(n))
