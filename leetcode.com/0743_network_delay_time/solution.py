class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for a, b, t in times:
            graph[a].append((b, t))

        m = 0
        visited = set()
        q = [(0, k)]

        while q:
            d, u = heapq.heappop(q)
            if u in visited:
                continue

            visited.add(u)
            m = max(m, d)

            for v, t in graph[u]:
                heapq.heappush(q, (d + t, v))

        if len(visited) != n:
            return -1

        return m
