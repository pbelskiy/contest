class Solution:
    def longestBalanced(self, s: str) -> int:
        m = 0

        for i in range(len(s)):
            d = Counter()
            for j in range(i, len(s)):
                d[s[j]] += 1

                if len(set(d.values())) == 1:
                    m = max(m, j - i + 1)

        return m

