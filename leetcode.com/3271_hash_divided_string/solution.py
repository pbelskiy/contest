class Solution:
    def stringHash(self, s: str, k: int) -> str:
        r = ''

        for i in range(0, len(s), k):
            t = 0
            for j in range(i, i + k):
                t += ord(s[j]) - ord('a')
            r += chr(ord('a') + t % 26)

        return r
