class Solution:
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):

        def bfs(x):
            q = deque([(0, 'r', 0), (0, 'b', 0)])
            v = set()
            while q:
                i, p, m = q.popleft()
                if i == x:
                    return m

                if p == 'r':
                    for j in bg[i]:
                        if (j, 'b') not in v:
                            v.add((j, 'b'))
                            q.append((j, 'b', m + 1))
                else:
                    for j in rg[i]:
                        if (j, 'r') not in v:
                            v.add((j, 'r'))
                            q.append((j, 'r', m + 1))

            return -1

        rg = defaultdict(list)
        for a, b in redEdges:
            rg[a].append(b)

        bg = defaultdict(list)
        for a, b in blueEdges:
            bg[a].append(b)

        return [bfs(x) for x in range(n)]
