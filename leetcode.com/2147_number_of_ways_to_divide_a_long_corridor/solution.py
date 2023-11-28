class Solution:
    def numberOfWays(self, a: str) -> int:
        s = [i for i in range(len(a)) if a[i] == 'S']
        if len(s) < 2 or len(s) % 2 == 1:
            return 0
        if len(s) == 2:
            return 1

        t = 1
        for i in range(1, len(s) - 1, 2):
            t = (t * (s[i + 1] - s[i])) % (10**9 + 7)

        return t
