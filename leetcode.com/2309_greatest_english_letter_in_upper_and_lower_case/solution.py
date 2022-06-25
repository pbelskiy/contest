class Solution:
    def greatestLetter(self, s: str) -> str:
        for a, b in zip(string.ascii_lowercase[::-1], string.ascii_uppercase[::-1]):
            if a in s and b in s:
                return b
        return ''
