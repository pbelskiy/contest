class Solution:
    def getSmallestString(self, s: str) -> str:
        a = list(map(int, s))
        r = s

        for i in range(len(s) - 1):
            if a[i] % 2 == a[i + 1] % 2:
                na = a[:]
                na[i], na[i + 1] = na[i + 1], na[i]
                r = min(r, ''.join(map(str, na)))

        return r
