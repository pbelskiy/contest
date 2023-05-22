class Solution:
    def punishmentNumber(self, n: int) -> int:

        def dfs(s, p, n):
            if not s:
                return p == n

            for i in range(1, len(s) + 1):
                a = s[:i]
                b = s[i:]

                if dfs(b, p + int(a), n):
                    return True

            return False

        t = 0

        for i in range(1, n + 1):
            if dfs(str(i*i), 0, i):
                t += i*i

        return t
