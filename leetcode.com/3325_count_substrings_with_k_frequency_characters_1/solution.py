class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        t = 0

        for i in range(len(s)):
            d = Counter()
            f = False
            for j in range(i, len(s)):
                d[s[j]] += 1

                if d[s[j]] >= k:
                    f = True

                if f:
                    t += 1

        return t
