class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        b = bin(n)[:1:-1]
        return [b[0::2].count('1'), b[1::2].count('1')]
