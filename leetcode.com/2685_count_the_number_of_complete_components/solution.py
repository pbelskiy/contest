class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        def bfs(a):
            q = deque([(a)])
            edges = set()
            nodes = set()

            while q:
                a = q.popleft()
                nodes.add(a)
                for b in g[a]:
                    k = (min(a, b), max(a, b))
                    if k not in edges:
                        edges.add(k)
                        q.append(b)

            # how much edges must be on completed component
            t = len(nodes) * (len(nodes) - 1) // 2

            return nodes, t == len(edges)

        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        t = 0
        v = set()

        for a in range(n):
            if a not in v:
                sv, is_complete = bfs(a)

                v |= sv
                if is_complete:
                    t += 1

        return t
