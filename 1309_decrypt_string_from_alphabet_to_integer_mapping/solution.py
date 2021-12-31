class Solution:
    def freqAlphabets(self, s: str) -> str:
        v, n, i = '', len(s), 0

        while i < n:
            if i + 2 < n and s[i + 2] == '#':
                v += chr(ord('a') + int(s[i:i+2]) - 1)
                i += 3
            else:
                v += chr(ord('a') + int(s[i]) - 1)
                i += 1

        return v
