class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        p, total = 0, 0

        for ch in t:
            while p < len(s) and s[p] != ch:
                p += 1

            if p >= len(s):
                total += 1
            elif s[p] == ch:
                p += 1

        return total
