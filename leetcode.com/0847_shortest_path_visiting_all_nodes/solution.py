class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:

        def bfs(i):
            v = set()
            q = deque([(i, 1 << i, 0)])

            while q:
                i, m, t = q.popleft()
                if m.bit_count() == len(g):
                    return t

                for j in g[i]:
                    key = (i, j, m | (1 << j))
                    if key in v:
                        continue
                    v.add(key)

                    q.append((j, m | (1 << j), t + 1))

            return float('inf')

        g = defaultdict(set)
        for i, nodes in enumerate(graph):
            for j in nodes:
                g[i].add(j)
                g[j].add(i)

        if not g:
            return 0

        # start from each node
        best = float('inf')

        for i in g:
            v = bfs(i)

            # already minimum possible solution
            if v == len(g) - 1:
                return v

            best = min(best, v)

        return best
