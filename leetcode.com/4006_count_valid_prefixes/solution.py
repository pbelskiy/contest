class Solution:
    def countValidPrefixes(self, s: str) -> int:
        t = 0
        d = Counter()

        for ch in s:
            d[ch] += 1
            if abs(d['0'] - d['1']) < 2:
                t += 1

        return t
