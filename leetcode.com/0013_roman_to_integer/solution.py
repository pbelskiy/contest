class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        total = 0
        lc = s[0]

        for c in s:
            total += m[c]
            if m[c] > m[lc]:
                total -= m[lc]*2
            lc = c

        return total
