class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        g = defaultdict(list)

        for a, b in paths:
            g[a].append(b)
            g[b].append(a)

        r = [1]*n
        v = set()

        def get_flower(i):
            a = {1, 2, 3, 4}
            b = {r[j - 1] for j in g[i]}
            return next(iter(a ^ b))

        def dfs(i, f):
            r[i - 1] = f

            for j in g[i]:
                if j in v:
                    continue
                v.add(j)
                dfs(j, get_flower(j))

        for i in g:
            if i not in v:
                dfs(i, 1)

        return r
