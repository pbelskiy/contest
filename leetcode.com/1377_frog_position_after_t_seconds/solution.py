class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:

        def dfs(a, p, t):
            ways = [b for b in g[a] if b != p]

            if a == target:
                if len(ways) == 0:
                    return 1
                return t == 0

            if t == 0:
                return 0

            m = 0
            for b in ways:
                m = max(m, dfs(b, a, t - 1) * (1 / len(ways)))

            return m

        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        return dfs(1, 1, t)
