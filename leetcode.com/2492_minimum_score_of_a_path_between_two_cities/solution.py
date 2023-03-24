class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(list)
        c = dict()
        for a, b, d in roads:
            g[a].append(b)
            g[b].append(a)
            c[(a, b)] = c[(b, a)] = d

        q = deque([(1)])
        v = set()
        s = float("inf")

        while q:
            i = q.popleft()

            for j in g[i]:
                s = min(s, c[i, j])
                if j in v:
                    continue
                q.append(j)
                v.add(j)

        return s
