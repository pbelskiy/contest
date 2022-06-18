class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        total = 0

        for i in range(len(s) - 2):
            if s[i] != s[i + 1] and s[i] != s[i + 2] and s[i + 1] != s[i + 2]:
                total += 1

        return total
