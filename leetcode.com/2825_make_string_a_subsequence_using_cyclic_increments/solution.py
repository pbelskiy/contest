class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len(str1) < len(str2):
            return False

        i, j = 0, 0
        t = 0

        while i < len(str1) and j < len(str2):
            cond = False

            if str1[i] == 'z' and str2[j] == 'a':
                cond = True

            if ord(str1[i]) + 1 == ord(str2[j]):
                cond = True

            if (str1[i] == str2[j]) or cond:
                t += 1
                j += 1

            i += 1

        return t == len(str2)
