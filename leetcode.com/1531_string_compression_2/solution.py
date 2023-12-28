class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:

        @cache
        def dp(i, k, p, f):
            if k < 0:
                return float('inf')

            if i == len(s):
                return 0

            # if current char not equal prev
            if s[i] != p:
                return min(
                    dp(i + 1, k, s[i], 1) + 1,  # pick
                    dp(i + 1, k - 1, p, f),     # skip
                )

            # such freq eats +1 len of final string
            if f in (1, 9, 99):
                return dp(i + 1, k, p, f + 1) + 1

            return dp(i + 1, k, p, f + 1)

        return dp(0, k, '', 0)
