class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        def bfs(u):
            q = deque([(u, 0)])
            s = set()
            while q:
                u, t = q.popleft()
                if u == n - 1:
                    return t

                for v in g[u]:
                    if v not in s:
                        s.add(v)
                        q.append((v, t + 1))

        g = defaultdict(list)
        for u in range(n - 1):
            g[u].append(u + 1)

        r = []
        for u, v in queries:
            g[u].append(v)
            g[u].sort(reverse=True)
            r.append(bfs(0))

        return r
