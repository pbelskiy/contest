class UnionFind:

    def __init__(self, n):
        self.p = list(range(n))

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        self.p[a] = b

    def find(self, a):
        if self.p[a] == a:
            return a

        self.p[a] = self.find(self.p[a])
        return self.p[a]

    def connected(self, a, b):
        return self.find(a) == self.find(b)


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []

        for i in range(len(points)):
            for j in range(i, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                weight = abs(x1 - x2) + abs(y1 - y2)
                edges.append((i, j, weight))

        edges.sort(key=lambda t: t[2])

        n = len(points)
        t = 0
        v = 0
        uf = UnionFind(n)

        for a, b, w in edges:
            if uf.connected(a, b):
                continue

            uf.union(a, b)
            t += w
            v += 1

            if v == n:
                break

        return t
