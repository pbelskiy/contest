class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:

        def dfs(a):
            t = values[a]
            v.add(a)

            for b in g[a]:
                if b not in v:
                    t += dfs(b)

            if t % k == 0:
                self.components += 1

            return t

        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        m = 0
        v = set()
        for a in range(n):
            self.components = 0
            if a not in v:
                dfs(a)
                m = max(m, self.components)
                break

        return m
