class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        if len(s) == 1:
            return 0

        for i in range(len(s) - 1):
            if s[i] == s[len(s) - i - 1]:
                return i

        return -1

