class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        letters = {'a', 'e', 'i', 'o', 'u'}

        t, m = 0, 0

        # init sliding window
        for i in range(k):
            if s[i] in letters:
                t += 1
                m += 1

        # move window forward
        for i in range(k, len(s)):
            if s[i] in letters:
                t += 1
            if s[i - k] in letters:
                t -= 1

            m = max(m, t)

        return m
