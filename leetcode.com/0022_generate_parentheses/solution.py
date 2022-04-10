class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def dfs(l, r, s):
            if r == n:
                self.values.append(s)
                return

            if l < n:
                dfs(l + 1, r, s + '(')

            if r < l:
                dfs(l, r + 1, s + ')')

        self.values = []
        dfs(0, 0, '')
        return self.values
