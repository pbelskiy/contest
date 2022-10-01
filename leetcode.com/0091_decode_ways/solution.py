class Solution:
    def numDecodings(self, s: str) -> int:

        @cache
        def dfs(i):
            if i >= len(s):
                return 1

            if s[i] == '0':
                return 0

            # take 1 digit
            t = dfs(i + 1)

            # take 2 digits
            if i + 2 <= len(s) and int(s[i:i+2]) <= 26:
                t += dfs(i + 2)

            return t

        return dfs(0)
