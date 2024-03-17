class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        rev = s[::-1]

        for i in range(len(s) - 1):
            if s[i] + s[i+1] in rev:
                return True

        return False
