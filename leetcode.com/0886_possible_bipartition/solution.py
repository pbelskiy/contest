class Solution:
    """
    1) construct bidirectional graph
    2) run BFS with coloring from each non visited node
    3)
    """
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        def bfs(i):
            q = deque([(i, False)])
            while q:
                i, m = q.popleft()
                if v.get(i, m) != m:
                    return False

                v[i] = m
                for j in g[i]:
                    if j not in v:
                        q.append((j, not m))

            return True

        g = defaultdict(list)
        for a, b in dislikes:
            g[a].append(b)
            g[b].append(a)

        v = {}
        for i in range(1, n + 1):
            if i in v:
                continue
            if not bfs(i):
                return False

        return True
