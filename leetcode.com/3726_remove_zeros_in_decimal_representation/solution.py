class Solution:
    def removeZeros(self, n: int) -> int:
        return int(''.join([ch for ch in str(n) if ch != '0']))

