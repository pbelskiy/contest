class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        m = 0

        for i in range(len(s)):
            t = False

            for j in range(i, len(s)):
                # if there is at most one consecutive pair of the same digits inside t
                if j > i and s[j] == s[j - 1]:
                    if exists:
                        break
                    exists = True

                m = max(m, j - i + 1)

        return m
