"""
Use bisect to find result, check(i) count number
of components before i edge.

TC: O(sort)
SC: O(sort)
"""
class Solution:
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:

        def bfs(a, g, v):
            q = deque([a])
            while q:
                a = q.popleft()
                for b in g[a]:
                    if b not in v:
                        q.append(b)
                        v.add(b)

        def check(i):
            g = defaultdict(list)
            for a, b, t in edges[i+1:]:
                g[a].append(b)
                g[b].append(a)

            v = set()
            t = 0
            for a in g:
                if a not in v:
                    bfs(a, g, v)
                    t += 1

            return n - len(v) + t

        # sort by time
        edges.sort(key=lambda t: t[2])

        # without removals it's already okay
        if check(-1) >= k:
            return 0

        # use bisect to find minimum time
        lo, hi = 0, len(edges) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid) < k:
                lo = mid + 1
            else:
                hi = mid - 1

        return edges[lo][2]

