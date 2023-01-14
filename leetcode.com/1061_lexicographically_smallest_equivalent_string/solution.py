class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        g = defaultdict(list)

        for a, b in zip(s1, s2):
            g[a].append(b)
            g[b].append(a)

        def bfs(i):
            q = deque([i])
            v = set([i])

            while q:
                i = q.popleft()
                for j in g[i]:
                    if j not in v:
                        v.add(j)
                        q.append(j)

            return min(v)

        r = list(baseStr)

        for i in range(len(r)):
            r[i] = bfs(r[i])

        return ''.join(r)
