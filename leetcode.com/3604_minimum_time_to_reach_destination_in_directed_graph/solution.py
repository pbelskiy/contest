class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for a, b, l, r in edges:
            g[a].append((b, l, r))

        min_time = [float('inf')] * n
        min_time[0] = 0

        q = [(0, 0)]
        while q:
            t, a = heappop(q)
            if t > min_time[a]:
                continue
            if a == n - 1:
                return t

            for b, l, r in g[a]:
                if t > r:
                    continue
                nt = max(t, l) + 1
                if nt < min_time[b]:
                    min_time[b] = nt
                    heappush(q, (nt, b))

        return -1

