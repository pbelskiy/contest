class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        @cache
        def dp(i, j):
            if i == len(s1):
                return sum(ord(s2[k]) for k in range(j, len(s2)))

            if j == len(s2):
                return sum(ord(s1[k]) for k in range(i, len(s1)))

            if s1[i] == s2[j]:
                return dp(i + 1, j + 1)

            return min(
                dp(i + 1, j) + ord(s1[i]),
                dp(i, j + 1) + ord(s2[j])
            )

        return dp(0, 0)
