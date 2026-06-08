class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        
        def dfs(s, t):
            if t > k:
                return

            if len(s) == n:
                a.append(s)
                return

            if s[-1] == '1':
                dfs(s + '0', t)
            else:
                dfs(s + '0', t)
                dfs(s + '1', t + len(s))

        a = []
        dfs('0', 0)
        dfs('1', 0)
        return sorted(a)

