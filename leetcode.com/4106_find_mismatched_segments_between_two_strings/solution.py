class Solution:
    def findMismatchedSegments(self, s1: str, s2: str) -> list[list[str]]:
        r = []
        s = ['', '']

        s1 += '@'
        s2 += '@'

        for a, b in zip(s1, s2):
            if a == b:
                if s[0]:
                    r.append(s)
                s = ['', '']
            else:
                s[0] += a
                s[1] += b

        return r

