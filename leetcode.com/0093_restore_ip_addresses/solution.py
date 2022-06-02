class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        def dfs(i, v, d):

            if v and int(v.split('.')[-1]) > 255:
                return

            if i == len(s):
                if d == 3:
                    res.append(v)
                return

            if not v or v[-2:] != '.0' and not (len(v) == 1 and v[0] == '0'):
                    dfs(i + 1, v + s[i], d)

            if d < 3 and v and v[-1] != '.':
                dfs(i + 1, v + '.' + s[i], d + 1)

        res = []
        if 4 <= len(s) <= 12:
            dfs(0, '', 0)
        return res
