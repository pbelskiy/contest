class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def dfs(i, a):
            if i == len(s):
                res.append(a)
                return

            for j in range(i, len(s)):
                p = s[i:j+1]

                if p and p == p[::-1]:
                    dfs(j + 1, a[:] + [p])

        res = []
        dfs(0, [])
        return res
