class Solution:
    def lexSmallest(self, s: str) -> str:
        m = s

        for k in range(1, len(s) + 1):
            m = min(m, s[:k][::-1] + s[k:], s[:k] + s[k:][::-1])

        return m

