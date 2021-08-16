class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0

        for i, ch in enumerate(s):

            for k in range(j, len(t)):
                j += 1

                if t[k] == ch:
                    break
            else:
                return False

        return True
