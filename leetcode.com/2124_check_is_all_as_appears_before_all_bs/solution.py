class Solution:
    def checkString(self, s: str) -> bool:
        a = float('-inf')
        b = float('+inf')

        for i, ch in enumerate(s):
            if ch == 'a':
                a = i
            elif b == float('+inf'):
                b = i

        return a < b
