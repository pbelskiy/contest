class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        g = defaultdict(list)

        for i, p in enumerate(parent):
            if i == 0:
                continue
            g[i].append(p)
            g[p].append(i)

        @cache
        def dfs(i, p):
            r = 0
            for j in g[i]:
                if j == p:
                    continue
                if s[i] == s[j]:
                    continue

                r = max(r, dfs(j, i) + 1)

            return r

        if len(s) == 1:
            return 1

        return max(dfs(k, -1) for k in g) + 1
