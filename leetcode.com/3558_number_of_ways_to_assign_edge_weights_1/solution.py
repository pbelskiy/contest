class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:

        @cache
        def dfs(a, p, odd, target):
            if a == target:
                return 1 if odd else 0

            m = 0

            for b in g[a]:
                if b == p:
                    continue

                # + 1
                if odd:
                    m += dfs(b, a, False, target)
                else:
                    m += dfs(b, a, True, target)

                # + 2
                if odd:
                    m += dfs(b, a, True, target)
                else:
                    m += dfs(b, a, False, target)

            return m % (10**9 + 7)

        def get_leafs(a, p, d):
            # we are leaf
            if len(g[a]) == 1 and list(iter(g[a])) == [p]:
                leafs[a] = d
                return d

            m = 0
            for b in g[a]:
                if b != p:
                    m = max(m, get_leafs(b, a, d + 1))

            return m

        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        leafs = {}
        max_depth = get_leafs(1, 0, 0)

        m = 0
        for leaf, depth in leafs.items():
            if depth == max_depth:
                m = max(m, dfs(1, 0, False, leaf))
                dfs.cache_clear()
                break

        return m
