class Solution:
    def maxValue(self, n: str, x: int) -> str:
        x = str(x)

        if n[0] == '-':
            i = 1
            while i < len(n) and n[i] <= x:
                i += 1
        else:
            i = 0
            while i < len(n) and n[i] >= x:
                i += 1

        return n[:i] + x + n[i:]
