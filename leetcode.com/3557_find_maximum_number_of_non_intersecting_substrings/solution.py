class Solution:
    def maxSubstrings(self, s: str) -> int:
        t = 0
        d = {}

        for i, ch in enumerate(s):
            if ch not in d:
                d[ch] = i
                continue

            if i - d[ch] + 1 >= 4:
                t += 1
                d = {}

        return t
