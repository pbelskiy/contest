class Solution:
    def maxProduct(self, n: int) -> int:
        a = sorted(str(n))
        return int(a[-1])*int(a[-2])

