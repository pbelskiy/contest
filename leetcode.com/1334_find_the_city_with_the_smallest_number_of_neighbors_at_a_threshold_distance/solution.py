class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], t: int) -> int:

        def bfs(a):
            q = [(0, a)]
            v = set()
            p = set()

            while q:
                s, a = heappop(q)
                p.add(a)
                for b, w in g[a]:
                    if ((a, b)) in v:
                        continue
                    if s + w > t:
                        continue

                    heappush(q, (s + w, b))
                    v.add((a, b))

            return len(p) - 1

        g = defaultdict(list)
        for a, b, w in edges:
            g[a].append((b, w))
            g[b].append((a, w))

        m = 0
        v = float("inf")
        for a in range(n):
            r = bfs(a)
            if r <= v:
                m = a
                v = r

        return m
