class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        @cache
        def is_valid(a):
            d = 0
            for p in a:
                if p == '(':
                    d += 1
                elif p == ')':
                    d -= 1

                if d < 0:
                    return False

            return d == 0

        @cache
        def dfs(s):
            for i in range(len(s)):
                ns = s[:i] + s[i+1:]
                if is_valid(ns):
                    res.add(ns)
                    found = True
                else:
                    dfs(ns)

        if is_valid(s):
            return [s]

        res = set()
        dfs(s)
        t = len(max(res, key=len))
        return sorted(filter(lambda x: len(x) == t, res))
