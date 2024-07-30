class Solution:
    def minimumDeletions(self, s: str) -> int:

        @cache
        def dp(i, p):
            if i == len(s):
                return 0

            m = float('inf')

            # delete
            m = dp(i + 1, p) + 1

            # not delete
            if not (s[i] == 'a' and p == 'b'):
                m = min(m, dp(i + 1, s[i]))

            return m

        r = dp(0, '')
        dp.cache_clear()
        return r
