class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        r = ''

        for i in range(len(s)):
            r += s[(i + k) % len(s)]

        return r
