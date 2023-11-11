class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.g = defaultdict(list)
        self.w = {}

        for a, b, w in edges:
            self.g[a].append(b)
            self.w[(a, b)] = w

    def addEdge(self, edge: List[int]) -> None:
        a, b, w = edge
        self.g[a].append(b)
        self.w[(a, b)] = w

    def shortestPath(self, node1: int, node2: int) -> int:
        q = [(0, node1)]
        v = set()

        while q:
            t, a = heappop(q)
            if a == node2:
                return t

            for b in self.g[a]:
                if b not in v:
                    v.add(a)
                    heappush(q, (t + self.w[(a, b)], b))

        return -1
