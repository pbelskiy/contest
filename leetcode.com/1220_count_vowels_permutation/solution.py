class Solution:
    def countVowelPermutation(self, n: int) -> int:

        @cache
        def dp(p, s):
            if s == n:
                return 1

            if p == 'a':
                ret = dp('e', s + 1)
            elif p == 'e':
                ret = (dp('a', s + 1) + dp('i', s + 1))
            elif p == 'i':
                ret = sum(dp(ch, s + 1) for ch in 'aeou')
            elif p == 'o':
                ret = dp('i', s + 1) + dp('u', s + 1)
            elif p == 'u':
                ret = dp('a', s + 1)

            return ret % (10**9 + 7)

        return sum(dp(ch, 1) for ch in 'aeiou') % (10**9 + 7)
