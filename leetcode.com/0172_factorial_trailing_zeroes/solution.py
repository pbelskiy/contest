class Solution:
    def trailingZeroes(self, n: int) -> int:
        v = str(math.factorial(n))
        return len(v) - len(v.rstrip('0'))
