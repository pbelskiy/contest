class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:

        def is_possible(m):
            q = deque([0])
            v = set([0])
            while q:
                a = q.popleft()

                for b, w in g[a]:
                    if w <= m and b not in v:
                        q.append(b)
                        v.add(b)

            return len(v) == n

        g = defaultdict(list)
        m = 0
        for a, b, w in edges:
            g[b].append((a, w))
            m = max(m, w)

        if not is_possible(10**7):
            return -1

        lo, hi = 0, m
        while lo <= hi:
            mid = (lo + hi) // 2
            if is_possible(mid):
                hi = mid - 1
            else:
                lo = mid + 1

        return lo
