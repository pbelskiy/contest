class Solution:
    def minimumSteps(self, s: str) -> int:
        t = 0
        c = 0

        for i in range(len(s)):
            if s[i] == '1':
                c += 1
            else:
                t += c

        return t
