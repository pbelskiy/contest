class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False

        # left to right
        free = op = cl = 0
        for i in range(len(s)):
            if locked[i] == '0':
                free += 1
            elif s[i] == '(':
                op += 1
            elif s[i] == ')':
                cl += 1

            if free + op - cl < 0:
                return False

        # right to left
        free = op = cl = 0
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == '0':
                free += 1
            elif s[i] == '(':
                op += 1
            elif s[i] == ')':
                cl += 1

            if free - op + cl < 0:
                return False

        return True
