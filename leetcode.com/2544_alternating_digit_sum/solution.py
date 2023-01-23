class Solution:
    def alternateDigitSum(self, n: int) -> int:
        r = 0
        for i, d in enumerate(map(int, str(n))):
            if i % 2 == 0:
                r += d
            else:
                r -= d

        return r
