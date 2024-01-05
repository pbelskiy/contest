class Solution:
    def maximumLength(self, s: str) -> int:

        def get_length(i, j, k):
            d = 0

            while i + d < n and j + d < n and k + d < n and \
                  s[i+d] == s[j+d] == s[k+d] == s[i]:
                d += 1

            return d

        n = len(s)
        m = 0

        for i in range(n):
            for j in range(i + 1, n):
                if s[j] != s[i]:
                    continue
                for k in range(j + 1, n):
                    if s[k] != s[j]:
                        continue

                    m = max(m, get_length(i, j, k))

        return m if m != 0 else -1
