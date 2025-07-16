class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:

        def bfs(a):
            h = []
            q = deque([a])

            v.add(a)
            while q:
                a = q.popleft()
                heappush(h, a)

                for b in g[a]:
                    if b not in v:
                        q.append(b)
                        v.add(b)

            return h

        g = defaultdict(list)
        for a, b in connections:
            g[a].append(b)
            g[b].append(a)

        v = set()
        d = {}
        components = []

        for a in range(1, c + 1):
            if a in v:
                continue
            h = bfs(a)
            components.append(h)

            for b in h:
                d[b] = len(components) - 1

        # print(components)

        offline = set()
        answer = []

        for t, a in queries:
            if t == 2:
                offline.add(a)
                continue

            if a not in offline:
                answer.append(a)
                continue

            h = components[d[a]]
            m = -1
            while h:
                a = heappop(h)
                if a in offline:
                    continue
                m = a
                heappush(h, a)
                break

            answer.append(m)

        return answer

