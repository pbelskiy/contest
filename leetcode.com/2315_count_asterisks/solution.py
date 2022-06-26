class Solution:
    def countAsterisks(self, s: str) -> int:
        t = 0
        a = s.split('|')

        for i in range(0, len(a), 2):
            t += a[i].count('*')

        return t
