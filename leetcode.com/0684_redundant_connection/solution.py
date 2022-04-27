class UnionFind:

    def __init__(self, n):
        self.p = list(range(n + 1))

    def find(self, x):
        if self.p[x] == x:
            return x

        self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        self.p[x] = y

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))

        for x, y in edges:
            if uf.connected(x, y):
                return [x, y]
            uf.union(x, y)
