class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:

        @cache
        def ev(s):
            return eval(s)

        def dfs(p, s):
            if p >= n:
                if ev(s) == target:
                    values.append(s)
                return

            for i in range(1, n - p + 1):
                if i > 1 and num[p] == '0':  # prevent leading zero
                    break

                ns = s + num[p:p+i]
                if p + i == n:
                    dfs(p + i, ns)
                    break

                dfs(p + i, ns + '+')
                dfs(p + i, ns + '-')
                dfs(p + i, ns + '*')

        n, values = len(num), list()
        dfs(0, '')
        return values
