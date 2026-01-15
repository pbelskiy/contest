class Solution:
    def residuePrefixes(self, s: str) -> int:
        m = set()
        t = 0

        for i in range(len(s)):
            m.add(s[i])
            if (i + 1) % 3 == len(m):
                t += 1

        return t

