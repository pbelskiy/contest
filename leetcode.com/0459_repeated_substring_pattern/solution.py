class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        for i in range(len(s) // 2 + 1):
            ss = s[:i]
            if s.count(ss) * len(ss) == len(s):
                return True

        return False
