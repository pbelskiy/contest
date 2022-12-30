class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == str2:
            return str1

        i = max(len(str1), len(str2)) - 1

        while i > 0:
            prefix = str1[:i]
            m1, m2 = len(str1) // i, len(str2) // i

            if prefix*m1 == str1 and prefix*m2 == str2:
                return prefix

            i -= 1

        return ''
