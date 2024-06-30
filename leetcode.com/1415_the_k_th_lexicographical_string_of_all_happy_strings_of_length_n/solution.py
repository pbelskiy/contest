class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        def dfs(s):
            if len(s) == n:
                h.append(s)
                return

            if s[-1] == 'a':
                dfs(s + 'b')
                dfs(s + 'c')
            elif s[-1] == 'b':
                dfs(s + 'a')
                dfs(s + 'c')
            else:
                dfs(s + 'a')
                dfs(s + 'b')

        h = []
        dfs('a')
        dfs('b')
        dfs('c')

        if len(h) < k:
            return ''

        h.sort()
        return h[k - 1]
