class Solution:
    def checkValidString(self, s: str) -> bool:

        @cache
        def dp(i, b):
            if  b < 0:
                return False

            if i == len(s):
                return b == 0

            r = False

            if s[i] == '(':
                r |= dp(i + 1, b + 1)
            elif s[i] == ')':
                r |= dp(i + 1, b - 1)
            else:
                r |= dp(i + 1, b)
                r |= dp(i + 1, b + 1)
                r |= dp(i + 1, b - 1)

            return r

        return dp(0, 0)
