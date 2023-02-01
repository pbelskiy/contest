class Solution:
    def splitString(self, s: str) -> bool:

        def dfs(i, n, p):
            if i == len(s):
                return n > 1

            r = False
            for j in range(i, len(s)):
                v = int(s[i:j+1])

                if p is None or p - 1 == v:
                    if dfs(j + 1,  n + 1, v):
                        return True

            return False

        return dfs(0, 0, None)
