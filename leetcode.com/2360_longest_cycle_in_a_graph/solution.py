class Solution:
    def longestCycle(self, edges: List[int]) -> int:

        def bfs(i, seen):
            q, v = deque([(i, 0)]), {}
            while q:
                i, l = q.popleft()
                if i in seen:
                    break

                j = edges[i]
                if j == -1:
                    return -1, v

                if j not in v:
                    v[j] = l
                    q.append((j, l + 1))
                    continue

                return l - v[j], v

            return -1, v

        m = -1
        seen = set()
        for i in range(len(edges)):
            r, v = bfs(i, seen)
            seen |= set(v.keys())
            m = max(m, r)

        return m
