class Solution:
    def replaceDigits(self, s: str) -> str:
        l = []

        for i in range(0, len(s), 2):
            l.append(s[i])

            if i + 1 < len(s):
                l.append(chr(ord(s[i]) + int(s[i+1])))

        return ''.join(l)