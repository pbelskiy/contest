class Solution:
    def addMinimum(self, word: str) -> int:
        s = list(word)

        for i in range(len(s) - 1, -1, -1):
            if s[i] == 'a' and (i + 1 == len(s) or s[i + 1] != 'b'):
                s.insert(i + 1, 'b')

        for i in range(len(s) - 1, -1, -1):
            if s[i] == 'b' and (i + 1 == len(s) or s[i + 1] != 'c'):
                s.insert(i + 1, 'c')

        d = 0
        for i in range(len(s)):
            if s[i + d] == 'c' and (i == 0 or s[i + d - 1] != 'b'):
                s.insert(i + d, 'b')
                d += 1

        d = 0
        for i in range(len(s)):
            if s[i + d] == 'b' and (i == 0 or s[i + d - 1] != 'a'):
                s.insert(i + d, 'a')
                d += 1

        return len(s) - len(word)
